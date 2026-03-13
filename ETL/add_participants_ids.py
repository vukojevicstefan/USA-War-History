import pandas as pd

# Load datasets
war_df = pd.read_csv(r'D:\Internship Stefan\Historic Analysis\Final Data\Wars.csv')
participants_df = pd.read_csv(r'D:\Internship Stefan\Historic Analysis\Final Data\War Participants.csv')

# Separate allies and opponents
allies = participants_df[participants_df['Side'] == 'Allies']
opponents = participants_df[participants_df['Side'] == 'Opponents']

# Group by War ID and collect Participant IDs
allies_grouped = allies.groupby('War ID')['Participant ID'].apply(list).reset_index()
allies_grouped.rename(columns={'Participant ID': 'Allies_ID'}, inplace=True)

opponents_grouped = opponents.groupby('War ID')['Participant ID'].apply(list).reset_index()
opponents_grouped.rename(columns={'Participant ID': 'Opponents_ID'}, inplace=True)

# Merge into war dataframe
war_df = war_df.merge(allies_grouped, how='left', left_on='ID', right_on='War ID')
war_df = war_df.merge(opponents_grouped, how='left', left_on='ID', right_on='War ID')
war_df.drop(columns=['War ID_x', 'War ID_y'], inplace=True)
# Save result
war_df.to_csv(r'D:\Internship Stefan\Historic Analysis\Final Data\war_updated.csv', index=False)

print("War dataset updated with Allies_ID and Opponents_ID.")