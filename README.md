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
| `#`                            | Unique identifier for each booking                            |
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