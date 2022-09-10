import asyncio
import flask
from flask import request, jsonify, render_template
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, MutationType, QueryType, SubscriptionType
from ariadne.constants import PLAYGROUND_HTML

from .schema.resolvers import connect, getTime

from .stores import queues

mutations = MutationType()
mutations.set_field('connect', connect)

queries = QueryType()
queries.set_field("getTime", getTime)

subscriptions = SubscriptionType()

@subscriptions.source("userConnected")
async def connected_generator(obj, info):
    queue = asyncio.Queue()
    queues.append(queue)
    try:
        while True:
            print('listen')
            connection = await queue.get()
            queue.task_done()
            if not connection:
                yield None
            yield connection
    except asyncio.CancelledError:
        queues.remove(queue)
        raise


@subscriptions.field("userConnected")
async def connected_resolver(user, info):
    if not user:
        return {
            "success": False,
            "errors": ['Connection failed!']
        }
    return {
            "success": True,
            "msg": user
        }

resolvers = [mutations, queries, subscriptions]

type_defs = load_schema_from_path("./server/src/schema/type-defs.graphql")
schema = make_executable_schema(
    type_defs, resolvers, snake_case_fallback_resolvers
)

app = flask.Flask(__name__, static_url_path='', static_folder='build', template_folder="build")

app.config["DEBUG"] = True

app.config.from_pyfile('settings.py')

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route("/")
def my_index():
    return render_template("index.html")
