import pandas as pd

DNDdata = 'Data/dnd_monsters.csv'
df = pd.read_csv(DNDdata)

# Drop unnecessary columns

# 1) 
df = df.drop(columns=['url','speed', 'align', 'legendary', 'source'])
# 2) 
df = df.dropna(subset = ['str','dex','con','int','wis','cha'])

#Replace fractions with decimal for plotting
for cr in df['cr']:
    if '1/4' in cr:
         df['cr'] =df['cr'].replace([cr],[0.25])
    elif '1/2' in cr:
        df['cr'] =df['cr'].replace([cr],[0.5])
    elif '1/8' in cr:
        df['cr'] =df['cr'].replace([cr],[0.125])

# Replace indiviual types in type columns with generic names (humanoid, monstrosity, fiend, giant, undead)
for name in df['type']:
    if 'humanoid' in name:
         df['type'] =df['type'].replace([name],['humanoid'])
    elif 'fiend' in name:
        df['type'] =df['type'].replace([name],['fiend'])
    elif 'monstrosity' in name:
        df['type'] =df['type'].replace([name],['monstrosity'])
    elif 'giant' in name:
        df['type'] =df['type'].replace([name],['giant'])
    elif 'undead' in name:
        df['type'] =df['type'].replace([name],['undead'])
    elif 'swarm' in name:
        df['type'] =df['type'].replace([name],['swarm'])

# save new data set
df.to_csv(path_or_buf='Data/updated_dnd_monsters.csv', index = False)

