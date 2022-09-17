import flask
from flask import render_template
from strawberry import Schema
from strawberry.flask.views import AsyncGraphQLView
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from .schema.resolvers import Query, Mutation, Subscription

schema = Schema(query=Query, mutation=Mutation, subscription=Subscription)

app = flask.Flask(__name__, static_url_path='', static_folder='build', template_folder="build")

app.config["DEBUG"] = True

app.config.from_pyfile('settings.py')

app.add_url_rule('/graphql', view_func=AsyncGraphQLView.as_view(
    'graphql_view',
    schema=schema,
    graphiql=True
))

@app.route("/")
def my_index():
    return render_template("index.html")
