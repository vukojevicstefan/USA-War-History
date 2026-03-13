import pandas as pd

# Read the CSV files
war_details = pd.read_csv('Final Data/War Details.csv')
wars = pd.read_csv('wars.csv')

# Merge only Start Year and End Year into war_details
years = wars[['ID', 'Start Year', 'End Year']]  # extract only the year columns
merged = pd.merge(war_details, years, on='ID', how='left')

# Save the updated War Details with years
merged.to_csv('Final Data/War Details1.csv', index=False)

# Remove Start Year and End Year from wars dataframe
wars = wars.drop(columns=['Start Year', 'End Year'])

# Save the updated wars table without years
wars.to_csv('wars1.csv', index=False)

print("Start Year and End Year moved to War Details and removed from Wars.")