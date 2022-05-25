import pandas as pd
import plotly.express as px

#Pull updated csv

DNDdata = 'data/updated_dnd_monsters.csv'
df = pd.read_csv(DNDdata)

#Use express function to create 3D plot

fig = px.scatter_3d(df, x='ac', y='cr', z='hp',
                    color='type', 
                    hover_name = 'name', 
                    hover_data = ['str','dex','con','int','wis','cha'],
                    color_discrete_sequence = ['rgb(152, 13, 106)', 'rgb(190, 240, 93)',
                                                'rgb(250, 60, 60)','rgb(46, 240, 161)',
                                                'rgb(183, 150, 16)', 'rgb(162, 96, 240)',
                                                'rgb(240, 185, 108)', 'rgb(83, 96, 240)',
                                                'rgb(240, 238, 60)', 'rgb(72, 174, 240)',
                                                'rgb(86, 233, 240)', 'rgb(240, 98, 190)',
                                                'rgb(27, 148, 18)','rgb(240, 125, 50)',
                                                'rgb(80, 240, 62)'],
                    opacity = 0.85)

#Update layout to make it more appealing

fig.update_layout(margin=dict(l=0, r=0, b=0),
                  title = dict(text='Comparison of Monsters AC vs CR vs HP'),
                  funnelmode = 'group',
                  legend = dict(title = 'Creature Type', tracegroupgap = 10))
fig.show()