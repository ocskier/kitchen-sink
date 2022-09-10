import asyncio
import time

from ..stores import queues

# Mutations
async def connect(obj, info, payload):
    try: 
        payload = {
            "success": True,
            "msg": "Successfully connected %s to the backend server" % (payload)
        }
        for queue in queues:
            await queue.put('User 123 connected')
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    print(payload)
    return payload

# Queries
def getTime(obj, info):
    try:
        payload = {
            "success": True,
            "time": time.time()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
    