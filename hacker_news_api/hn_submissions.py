import requests
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle as LCS
from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'  # 此网站需挂VPN
r = requests.get(url)
print("Status: ", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
titles,submission_dicts = [],[]
for submission in submission_ids[:30]:
	# 对于每篇文章，都执行一个API调用
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()
	titles.append(response_dict["title"])
	submission_dict = {
		'label':response_dict["by"],
		'xlink': 'http://news.ycombinator.com/item?id=' + str(submission),
		'value': response_dict.get('descendants', 0)
		# 方法dict.get()，它在指定的键存在时返回与之相关联的值，
		# 并在指定的键不存在时返回你指定的值（这里是0）。
	}
	submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)
# 函数itemgetter():向这个函数传递了键'comments'，因此它将从这个列表的每个字典中提取与键'comments'相关联的值。
# reverse=True表示降序

my_style=RotateStyle(color='#ff2d51',base_style=LCS)
show_sub=pygal.Bar(style=my_style,x_label_rotation=45,truncate_label=15)
show_sub.title="Show Submission"
show_sub.x_labels=titles
show_sub.add('',submission_dicts)
show_sub.render_to_file("show_submission.svg")
