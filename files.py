import json

with open("C:/tools/config.json") as f: # см урок 27_with.mp4
    try:
        res = json.load(f)
    except ValueError as ex: # перехват исключения ValueError
        print(ex)
        res = {}
# finally: # блок finally выполняется при любых обстоятельствах
#     f.close()

print(res)
