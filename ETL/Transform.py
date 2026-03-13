import pandas as pd

def create_war_details():
    df = pd.read_csv('wars.csv')

    # set ID as index
    df.index.name = 'ID'

    # take the last two columns
    war_details = df.iloc[:, -2:]

    # keep same index
    war_details.index = df.index
    war_details.index.name = 'ID'
    df = df[['ID','Name','Start Year','End Year','US Killed','US Wounded','Total Casualties (All Sides)','GDP Impact (Estimated % of GDP at Peak)']]
    df.to_csv('wars.csv', index=False)
    war_details.to_csv('war_details.csv', index=False)

create_war_details()