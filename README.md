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

### Data Cleaning and Validation

1. **Convert Date Columns to Datetime Format:**
   - `date_time`
   - `srch_ci`
   - `srch_co`

2. **Handle Invalid or Missing Date Value:**
   - `errors='coerce'` converts invalid date strings in `srch_ci` and `srch_co` into NaT (not a time, missing datetime), preventing errors during date operations.

3. **Calculate Trip Length and Lead Time:**
   - `trip_length` - Number of days between check-out and check-in (`srch_co - srch_ci`).
   - `lead_time` - Number of days between booking/search date and check-in (`srch_ci - date_time`).
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