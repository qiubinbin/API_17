import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# import json

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:go&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)
# 将API响应存储在变量中
response_dict = r.json()  # 把响应转换成json字典
# with open("test.json",'w') as temp:
# 	json.dump(response_dict,temp)
# 处理结果
# print(response_dict)
print(response_dict.keys())
print("Total repositories", response_dict["total_count"])
# 探索有关仓库的信息
repo_dicts = response_dict["items"]
print("Repositories returned: ", len(repo_dicts))
# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
names, plot_dicts = [], []
for repo in repo_dicts:
	names.append(repo["name"])
	plot_dict = {
		'value': repo["stargazers_count"],
		'label': str(repo["description"]),  # 调用str很关键，不然会报属性错误
		'xlink': repo["url"],
	}
	plot_dicts.append(plot_dict)
# 可视化
my_style = LS("#333766", base_style=LCS)
#修改配置
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15  # 将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名
my_config.show_y_guides = False  # 将show_y_guides设置为False，以隐藏图表中的水平线
my_config.width = 1000
show_star = pygal.Bar(my_config, style=my_style)
"""
让标签绕x轴旋转45度（x_label_rotation=45）
并隐藏了图例（show_legend=False）
"""
show_star.title = "Stars"
show_star.x_labels = names
show_star.add('', plot_dicts)
show_star.render_to_file("names_stars.svg")
