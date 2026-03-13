import pandas as pd

# Read the CSV files
war_details = pd.read_csv('Final Data/War Details.csv')
wars = pd.read_csv('wars.csv')

# Columns to move
columns_to_move = ['ID', 'Declared War?', 'Outcome', 'Cold War Proxy?']

# Extract the relevant columns from wars
subset = wars[columns_to_move]

# Merge into war_details on ID
war_details_updated = pd.merge(
    war_details,
    subset,
    on='ID',
    how='left'
)

# Remove the columns from wars
wars = wars.drop(columns=['Declared War?', 'Outcome', 'Cold War Proxy?'])

# Save updated files
war_details_updated.to_csv('Final Data/War Details1.csv', index=False)
wars.to_csv('wars.csv', index=False)

print("Columns moved successfully! War Details updated, and wars cleaned.")