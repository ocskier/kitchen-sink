import time

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

# Mutations
def connect(obj, info):
    print(obj)
    print(info)
    try: 
        payload = {
            "success": True,
            "msg": 'Successfully connected to the backend server!'
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
