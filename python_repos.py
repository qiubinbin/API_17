import requests
# import json

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)
# 将API响应存储在变量中
response_dict = r.json()  # 把响应转换成json字典
# with open("test.json",'w') as temp:
# 	json.dump(response_dict,temp)
# 处理结果
print(response_dict)
print(response_dict.keys())
