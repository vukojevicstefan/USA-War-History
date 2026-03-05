import pandas as pd

def participant():
    df = pd.read_csv('War Participants.csv')

    participant_df = df['Name'].dropna().drop_duplicates().reset_index(drop=True).to_frame()

    participant_df['ID'] = participant_df.index

    participant_df[['ID','Name']].to_csv('Participants.csv', index=False)

participant()