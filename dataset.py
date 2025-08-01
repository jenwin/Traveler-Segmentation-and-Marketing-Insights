import pandas as pd

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/jenwin/Travel_Data/refs/heads/main/expedia_segmented.csv")

# Convert date columns: date_time, srch_ci, and srch_co to datetime format
df['date_time'] = pd.to_datetime(df['date_time'])
df['srch_ci'] = pd.to_datetime(df['srch_ci'], errors='coerce')
df['srch_co'] = pd.to_datetime(df['srch_co'], errors='coerce')

# Create new behavioral features
df['trip_length'] = (df['srch_co'] - df['srch_ci']).dt.days
df['lead_time'] = (
    df['srch_ci'].dt.normalize() - df['date_time'].dt.normalize()
).dt.days
df['group_size'] = df['srch_adults_cnt'] + df['srch_children_cnt']

# Create simple traveler type segments: Solo, Couple, Family, Group
df.loc[df['srch_children_cnt'] > 0, 'traveler_type'] = 'Family'
df.loc[(df['srch_adults_cnt'] == 1) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Solo'
df.loc[(df['srch_adults_cnt'] == 2) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Couple'
df.loc[(df['srch_adults_cnt'] > 2) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Group'
df = df[~((df['srch_adults_cnt'] == 0) & (df['srch_children_cnt'] == 0))] # Remove entries with no adults or children

# Fill missing distance values
df['orig_destination_distance'] = df['orig_destination_distance'].fillna(-1)

# Export cleaned and segmented data to a new CSV
df.to_csv("expedia_segmented.csv", index=False)