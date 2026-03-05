import pandas as pd

def get_war_participants():
    df = pd.read_csv('america_war_history.csv')

    allies_df = df[['Conflict', 'Allies']]
    allies_df['Side'] = 'Allies'

    opponents_df = df[['Conflict', 'Opponent(s)']]
    opponents_df['Side'] = 'Opponents'
    participant_df = pd.concat(
        [allies_df, opponents_df],
        ignore_index=True
    )

    participant_df['Name'] = participant_df['Opponent(s)'].fillna(participant_df['Allies'])

    participant_df = participant_df[['Conflict', 'Name', 'Side']].dropna()

    # remove quotes
    participant_df['Name'] = participant_df['Name'].str.replace('"', '')

    # split participants
    participant_df['Name'] = participant_df['Name'].str.split(',')

    # one participant per row
    participant_df = participant_df.explode('Name')

    # clean spaces
    participant_df['Name'] = participant_df['Name'].str.strip()

    participant_df = participant_df.drop_duplicates().reset_index(drop=True)

    # set index name to ID
    participant_df.index.name = 'ID'

    participant_df.to_csv('War Participants.csv')


get_war_participants()