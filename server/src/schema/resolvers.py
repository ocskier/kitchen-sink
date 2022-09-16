import asyncio
import strawberry
import time
from typing import AsyncGenerator, Optional

from .types import ConnectResult, TimeResult

from ..stores import queues

# Queries
@strawberry.type
class Query:
    @strawberry.field
    def getTime() -> TimeResult:
        try:
            return TimeResult(success=True, time=time.time(), errors=None)
        except Exception as error:
            return TimeResult(success=False, time=None, errors=[str(error)])

# Mutations
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def connect(self, payload: Optional[str]) -> AsyncGenerator[ConnectResult, None]:
        try: 
            for queue in queues:
                await queue.put('User 123 Connected')
            return ConnectResult(success=True, msg="Successfully connected %s to the backend server" % (payload), errors=None)
        except Exception as error: 
            return ConnectResult(success=False, msg=None, errors=[str(error)])

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def userConnected(self) -> AsyncGenerator[ConnectResult, None]:
        queue = asyncio.Queue()
        queues.append(queue)
        try:
            while True:
                print('listen')
                connection = await queue.get()
                queue.task_done()
                if not connection:
                    yield ConnectResult(success=False, msg=None, errors=['Connection failed!'])
                yield ConnectResult(success=True, msg=connection, errors=None)
        except asyncio.CancelledError:
            queues.remove(queue)
            raise
