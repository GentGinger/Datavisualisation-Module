import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.subplots import make_subplots
import pandas as pd

# Open updated csv
DNDdata = 'data/updated_dnd_monsters.csv'
df = pd.read_csv(DNDdata)

# Make a list of lists containing each individual creatures attributes

all_stats = []
i = 0
for name in df['name']:
    stats = []
    strength = df.loc[i, 'str']
    dexterity = df.loc[i, 'dex']
    constitution = df.loc[i, 'con']
    intelligence = df.loc[i, 'int']
    wisdom = df.loc[i, 'wis']
    charisma = df.loc[i, 'cha']
    stats.append(strength)
    stats.append(dexterity)
    stats.append(constitution)
    stats.append(intelligence)
    stats.append(wisdom)
    stats.append(charisma)
    all_stats.append(stats)
    i += 1

# Create list for the grid for the radar plots to position into

spec =[]
innerSpecs = []
graph = {"type":"polar"}
for i in range(1):
    # Create 20 lines of type : Polar
    for i in range(20):
        innerSpecs.append(graph)
        spec.append(innerSpecs)
    # One line of one radar
    end = [{"type":"polar"},None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    spec.append(end)

#Create the grid itself

fig = make_subplots(
    rows=21, cols=20,
    specs=spec,
    subplot_titles = (df['name'])
)

#Set radial axes

stats = ['Strength', 'Dexterity', 'Constitution', 'Itelligence', 'Wisdom', 'Charisma']
stats = [*stats, stats[0]]

# Create plots for the grid

rows = 1
cols = 0
for i in range(len(all_stats)):
    # Updating position of each chart
    if rows <= 20 and cols <= 19:        
       cols += 1
    elif rows <= 20 and cols > 19:
        cols = 1
        rows += 1
    elif rows == 20 and cols == 20:
        rows = 21
        cols = 1
    #Calling up the attributes
    statblock = all_stats[i]
    statblock = [*statblock, statblock[0]]
    #Adding individual chart at location
    fig.add_trace(go.Scatterpolar(r=statblock,
                                  theta=stats, 
                                  name = 'Statblock',
                                  fill = 'toself',
                                  marker = dict(color = 'darkslategrey',
                                  size = 12)
                                  ),
                row = rows, col = cols)

#Altering design to fit better

fig.update_layout(height=8500,
                  width =8500, 
                  showlegend=False, 
                  title = dict(text='Radar Plots of all Creatures Stats')
                  )

#Setting continuous axis range

fig.update_polars(radialaxis=dict(range=[0, 30]))

#Run visualisation

pyo.plot(fig)