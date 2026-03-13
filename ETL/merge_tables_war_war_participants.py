import pandas as pd

def merge_war_participants():

    participants = pd.read_csv('Merged War Participants.csv').drop(columns=['War_ID'])
    wars = pd.read_csv('wars.csv')

    merged = participants.merge(
        wars[['ID', 'Name']],
        left_on='Conflict',
        right_on='Name',
        how='left'
    )

    merged = merged.rename(columns={'ID_y': 'War ID'})
    merged = merged.rename(columns={'ID_x': 'ID'})
    merged = merged.drop(columns=['Name'])
    merged.drop(columns=['Conflict'], inplace=True)

    # convert to whole number
    merged['War ID'] = merged['War ID'].astype('Int64')

    merged.to_csv('Merged War Participants1.csv', index=False)

merge_war_participants()