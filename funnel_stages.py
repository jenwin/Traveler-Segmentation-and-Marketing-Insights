import pandas as pd

# Load the dataset
df = pd.read_csv("https://raw.githubusercontent.com/jenwin/Travel_Data/refs/heads/main/expedia_segmented.csv")

# Traveler Type Classification/Function
def classify_travelers(df):        
    df.loc[(df['srch_adults_cnt'] == 1) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Solo' # Solo: 1 adult, 0 children
    df.loc[(df['srch_adults_cnt'] == 2) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Couple' # Couple: 2 adults, 0 children
    df.loc[(df['srch_adults_cnt'] > 2) & (df['srch_children_cnt'] == 0), 'traveler_type'] = 'Group' # Group: >2 adults, 0 children
    df.loc[(df['srch_children_cnt'] > 0), 'traveler_type'] = 'Family' # Family: >0 children

    return df

df = classify_travelers(df)

# Get unique traveler types
all_types = df['traveler_type'].unique()

# Total Visits: Unique users by traveler_type
total_visits = df.groupby('traveler_type')['user_id'].nunique().reindex(all_types, fill_value=0)

# Searches: Total rows by traveler_type
searches = df.groupby('traveler_type').size().reindex(all_types, fill_value=0)

# Completed Bookings: Unique users where is_booking = 1
completed_bookings = (
    df[df['is_booking'] == 1]
    .groupby('traveler_type')['user_id']
    .nunique()
    .reindex(all_types, fill_value=0)
)

# Combine into single DataFrame
summary = pd.DataFrame({
    'Traveler Type': all_types,
    'Total Visits': total_visits.values,
    'Searches': searches.values,
    'Completed Bookings': completed_bookings.values
})

# Melt for Tableau format
summary_melted = summary.melt(id_vars='Traveler Type', var_name='Stage', value_name='Count')

# Export
summary_melted.to_csv('funnel_summary_by_travelertype.csv', index=False)

# Show summary results
print(summary_melted)