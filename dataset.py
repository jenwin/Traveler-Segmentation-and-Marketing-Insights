import pandas as pd

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/jenwin/Travel_Data/refs/heads/main/expedia_segmented.csv")

# Convert date columns: date_time, srch_ci, and srch_co to datetime format
df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')
df['srch_ci'] = pd.to_datetime(df['srch_ci'], errors='coerce')
df['srch_co'] = pd.to_datetime(df['srch_co'], errors='coerce')

# Extract hour of day from date_time
df['hour_of_day'] = df['date_time'].dt.hour

# Define time_of_day categories based on hour
def time_of_day(hour):
    # 5 AM to 12 AM -> Morning
    if 5 <= hour < 12:
        return 'Morning'
    # 12 PM to 5 PM -> Afternoon
    elif 12 <= hour < 17:
        return 'Afternoon'
    # 5 PM to 9 PM -> Evening
    elif 17 <= hour < 21:
        return 'Evening'
    # 9 PM to 5 AM -> Night & Early Morning
    else:
        return 'Night'

df['time_of_day'] = df['hour_of_day'].apply(time_of_day)

# Create new behavioral features
df['trip_length'] = (df['srch_co'] - df['srch_ci']).dt.days  # Trip length in days
df['lead_time'] = (df['srch_ci'].dt.normalize() - df['date_time'].dt.normalize()).dt.days  # Lead time in days
df['group_size'] = df['srch_adults_cnt'] + df['srch_children_cnt']  # Total group size

# Create simple traveler type segments: Solo, Couple, Family, Group
df.loc[df['srch_children_cnt'] > 0, 'traveler_type'] = 'Family'
df.loc[(df['srch_adults_cnt'] == 1) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Solo'
df.loc[(df['srch_adults_cnt'] == 2) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Couple'
df.loc[(df['srch_adults_cnt'] > 2) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Group'

# Remove entries with no adults or children
df = df[~((df['srch_adults_cnt'] == 0) & (df['srch_children_cnt'] == 0))]

# Fill missing values in orig_destination_distance with -1
df['orig_destination_distance'] = df['orig_destination_distance'].fillna(-1)

# Export cleaned and segmented data to a new CSV
df.to_csv("expedia_segmented.csv", index=False)