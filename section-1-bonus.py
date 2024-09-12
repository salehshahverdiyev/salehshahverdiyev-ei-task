'''
8. Bonus Question - Based on this data set which user had the highest cumulative travel distance? 
What distance has been covered by him/her?
'''
import pandas as pd
import numpy as np
from haversine import haversine


df = pd.read_csv('Section 1 data.csv')
user_groups = df.groupby('User_ID')

'''
Calculates cumulative travel distance for a user
Steps:
Loop through each consecutive pair of reviews to calculate distance
Calculate the distance between two consecutive locations
'''
def calculate_cumulative_distance(user_reviews):
    user_reviews = user_reviews.sort_values(by='Review_Date')
    coords = user_reviews[['Latitude', 'Longitude']].to_numpy()
    total_distance = 0
    for i in range(1, len(coords)):
        loc1 = coords[i - 1]
        loc2 = coords[i]
        distance = haversine(loc1, loc2)
        total_distance += distance
    return total_distance

'''
Steps
Create a dictionary to store total travel distances for each user
Iterate over each user and calculate the total distance
Find the user with the highest cumulative travel distance
'''

user_distances = {}
for user_id, reviews in user_groups:
    total_distance = calculate_cumulative_distance(reviews)
    user_distances[user_id] = total_distance

max_user_id = max(user_distances, key=user_distances.get)
max_distance = user_distances[max_user_id]
print(f"User with the highest cumulative travel distance: {max_user_id}")
print(f"Total distance covered: {max_distance:.2f} km")
