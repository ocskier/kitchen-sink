import time

def getTime(obj, info):
    # sample query:
    # query GetTime {
    #     getTime {
    #         time
    #         success
    #         errors
    #     }
    # }
    try:
        # print(obj)
        # print(info)
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
