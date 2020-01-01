from helpers import get_team_plays
import plotly.graph_objects as go
import plotly as plt
import numpy as np



team = "Florida State"
o_or_d = "offense"
year_range = range(2010, 2020)

fig = go.Figure()
for year in year_range:
    data = get_team_plays(team=team, year=year)

    df = data[data[o_or_d]==team]


    fig.add_trace(go.Box(x=[year] * len(df),
                            y=df['yards_gained'],
                            name=year,
                            ))
                            #box_visible=True,
                            #meanline_visible=True))

fig.update_traces(#meanline_visible=True,
                  #points='all', # show all points
                  jitter=0.05,)  # add jitter on points for better visibility
                  #scalemode='count') #scale violin plot area with total count
fig.update_layout(title="{} {} Output (yards) by year".format(team, o_or_d),
                  title_x=0.5,
                  template="plotly_dark")

fig.show()
