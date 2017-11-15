import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS
my_style=LS('#336699',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title="Python Preject"
chart.x_labels=['awesome-python','httpie','thefuck']
plot_dicts=[
	{'value':41101,'label':'Description of awesome-python'},
	{'value':32565,'label':'Description of httpie'},
	{'value':32068,'label':'Description of thefuck'},
]
chart.add('',plot_dicts)
chart.render_to_file("char.svg")