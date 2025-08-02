# Traveler-Segmentation-Marketing-Insights

## Business Problem
How can a travel platform like Expedia identify distinct types of travelers to deliver personalized marketing campaigns that increase engagement, conversion rates, and customer satisfaction?

Understanding traveler behavior and segmenting users based on preferences, spending habits, and booking patterns allows travel companies to:

- Improve the effectiveness of marketing by targeting the right users with relevant offers
- Increase booking conversion rates through personalization
- Enhance customer experience and loyalty by tailoring promotions to match user needs
- Increase marketing effectiveness by identifying and reaching high-value or less-saturated audiences

## The Dataset

| Column                         | Description                                                   |
|--------------------------------|---------------------------------------------------------------|
|                                | Unique identifier for each booking                            |
| `date_time`                    | Timestamp: Customer booked/clicked                            |
| `site_name`                    | ID of the Expedia point of sale (POS)                         |
| `posa_continent`               | ID of continent associated with site_name                     |
| `user_location_country`        | ID of country where customer is located                       |
| `user_location_region`         | ID of region where customer is located                        |
| `user_location_city`           | ID of city where customer is located                          |
| `orig_destination_distance`    | Distance between hotel and customer at time of search         |
| `user_id`                      | Customer ID                                                   |
| `is_mobile`                    | `1`: Search made on mobile device. `0`: No.                   |
| `is_package`                   | `1`: Search includes package. `0`: No.                        |
| `channel`                      | ID of marketing channel                                       |
| `srch_ci`                      | Check-in date                                                 |
| `srch_co`                      | Check-out date                                                |
| `srch_adults_cnt`              | Number of adults in hotel room                                |
| `srch_children_cnt`            | Number of children in hotel room                              |
| `srch_rm_cnt`                  | Number of rooms requested                                     |
| `srch_destination_id`          | ID of destination                                             |
| `srch_destination_type_id`     | Type of destination                                           |
| `is_booking`                   | `1`: The record is a booking, `0`: Search or click.           |
| `cnt`                          | Number of similar search records from the same user/session   |
| `hotel_continent`              | Continent code where the hotel is located                     |
| `hotel_country`                | Country code where the hotel is located                       |
| `hotel_market`                 | Market/sub-region code where the hotel is located             |
| `hotel_cluster`                | Cluster ID representing a group of similar hotels             |

This project uses the [Expedia Travel Dataset](https://www.kaggle.com/datasets/jacopoferretti/expedia-travel-dataset/).

## Approach

### Tools & Technologies Used
- **Python** - For data cleaning and validation. Creating and exporting dataset.
- **Tableau** -  Data visualization and dashboard creation.
- **Excel** - For data cleaning and validation.

### Data Cleaning and Validation

#### Expedia Segmentation Dataset

1. **Convert Date Columns to Datetime Format:**
   - `date_time`
   - `srch_ci`
   - `srch_co`

2. **Handle Invalid or Missing Date Value:**
   - `errors='coerce'` converts invalid date strings in `srch_ci` and `srch_co` into NaT (not a time, missing datetime), preventing errors during date operations.

3. **Calculate Trip Length and Lead Time:**
   - `trip_length` - Number of days between check-out and check-in (`srch_co - srch_ci`).
   - `lead_time` - Number of days between booking/search date and check-in (`srch_ci - date_time`). Normalized to handle same-day bookings and prevent negative values.
   - Both calculations automatically handle missing date values due to datetime coercion.

4. **Create Group Size Feature:**
   - Sum of adults (`srch_adults_cnt`) and children (`srch_children_cnt`) to get total group size.

5. **Create Traveler Type Segments:**
   - Initialized `traveler_type` as `Unknown` for all rows.
   - `Family` if children count > 0.
   - `Solo` if 1 adult and no children.
   - `Couple` if 2 adults and no children.
   - `Group` if more than 2 adults and no children.

6. **Handle Missing Distance Values:**
   - Filled missing values in `orig_destination_distance` with -1 for unknown/missing distances.

7. **Dropped Columns or Rows:**
   - Unnamed column (first column).
   - Rows with no guests (0 adults, 0 children).

8. **Add Time-Based Feature**
   - Parsed `date_time` column into datetime format
   - Extracted `hour_of_day` and `time-of-day` classification: Morning, Afternoon, Evening, Night

### Funnel Stages Dataset Creation

1. **Classify Traveler Types**
   - `Solo`: 1 adult, 0 children
   - `Couple`: 2 adults, 0 children
   - `Group`: >2 adults, 0 children
   - `Family`: With at least 1 child 

2. **Aggregate Funnel Metrics**

For each traveler type:

   - `Total Visits`: Unique users (`user_id`)
   - `Searches`: Total number of search rows
   - `Completed Bookings`: Unique users where `is_booking == 1`

## Results

### Traveler Segmentation
   - `Solo` travelers have the highest booking rate at `12.2%`, which is significantly higher than other groups. 
   - `Families` follow a booking rate of `7.1%`, closely matched by `Groups` (`7.0%`) and `Couples` (`7.0%`).
   - `Solo` travelers tend to complete more bookings after searching, possibly due to quicker decision-making or fewer logistical constraints.
   - `Desktop` devices account for the majority of bookings across all traveler types. This indicates a clear preference for desktop platforms, probably due to easier navigation and more effective comparison features.
   - Booking volume peaks during `daytime hours`, especially in the `morning` and `afternoon`, for all traveler types.
   - `Couples` make up the largest portion of bookings throughout the day. This suggests they are the most active users on the platform.

### Trip Planning Behavior
   - `Families` typically book slightly longer stays, possibly due to more complex travel plans or vacation needs.
   - `Solo` travelers tend to take shorter trips.
   - `Couples` and `Groups` fall somewhere in between, which could mean varying travel purposes and preferences.
   - `Groups` and `Families` tend to plan their trips further in advance, likely due to coordinating multiple people and schedules. 
   - `Solo` travelers book more last-minute trips. This suggests more spontaneous travel or simpler logistics.

### User Search Usage and Distance
   - `Couples` lead in overall booking volume, but `Solo` travelers have a strong booking rate compared to their search numbers.
   - `Groups` are the smallest segment in terms of engagement and bookings.
   - All travelers prefer hotels closer to their location. This could be due to convenience, familiarity, or travel limitations, showing a natural preference for nearby accommodations.

## Key Business Insights

   - `Solo` travelers, despite having a smaller user base, had the highest booking conversion rate, indicating they could be a lucrative segment for targeted marketing.
   - `Desktop` was the preferred platform among all users. Enhancing the desktop user experience could drive more conversions.
   - Peak booking time were in the `morning` and `afternoon`. Promotional efforts or notifications could be targeted during these periods.
   - `Couples` accounted for a large portion of booking volume. Tailoring offers or packages for this segment could increase revenue.
   - `Families` and `Groups` showed longer lead times. Early-bird promotions or trip planning resources could be directed towards these segments.
   - All travelers preferred hotels near their location. This presents an opportunity for localized marketing or geo-targeted offers.

## Summary of Recommendations Based on Findings

   - Focus marketing on `Solo` travelers to capitalize on their higher booking rates.
   - Optimize `Desktop` platform features: Comparison tools, navigation, and security to boost bookings.
   - Schedule promotional campaigns during peak booking hours, especially in the `Morning` and `Afternoon`.
   - Create targeted campaigns and special packages for `Couples` to leverage their high booking volume.
   - Develop early-planning incentives (discounts, reminders) for `Families` and `Groups` to encourage earlier bookings.
   - Implement localized, geo-targeted marketing strategies to promote hotels and events near users.

## Author
Jennifer Nguyen