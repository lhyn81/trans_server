# 从JSON文件加载所有算法数据结构
import json

with open("model\\blue.json",'rb') as modjs:
    modbody = json.load(modjs)
modGroup = modbody["modGroup"]
modItems = modbody["modItems"]

# Debug
# for k in modItems:
# 	print(k)