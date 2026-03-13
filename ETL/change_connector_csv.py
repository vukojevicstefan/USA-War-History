import pandas as pd

# Read the CSV files
participants_df = pd.read_csv('Participants.csv')
war_participants_df = pd.read_csv('War Participants.csv')

# Rename ID column in participants to avoid conflict
participants_df = participants_df.rename(columns={'ID': 'Participant ID'})
merged_df = war_participants_df.merge(participants_df[['Name', 'Participant ID']], on='Name', how='left')

# Remove 'Name' column from the merged dataframe
merged_df = merged_df.drop(columns=['Name'])

# Save the result
merged_df.to_csv('Merged War Participants.csv', index=False)

print(merged_df.head())