import pandas as pd

# Paths
wars_path = r'D:\Internship Stefan\Historic Analysis\Final Data\Wars.csv'
details_path = r'D:\Internship Stefan\Historic Analysis\Final Data\War Details.csv'
output_path = r'D:\Internship Stefan\Historic Analysis\Final Data\War_Locations.csv'

# Load data
wars_df = pd.read_csv(wars_path)
details_df = pd.read_csv(details_path)

# Merge datasets on ID
merged_df = pd.merge(wars_df[['ID', 'Name']], details_df[['ID', 'Location']], on='ID', how='inner')

# Save result
merged_df.to_csv(output_path, index=False)

print("War_Locations.csv created successfully.")