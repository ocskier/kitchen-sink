import time

# Mutations
def connect(obj, info, payload):
    print(payload)
    try: 
        payload = {
            "success": True,
            "msg": "Successfully connected %s to the backend server" % (payload)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
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
    