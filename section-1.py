import pandas as pd
df = pd.read_csv('Section 1 data.csv')


'''
1. How many unique restaurants could be found in this data set? 
(Hint: Use the [Business_ID] column for this evaluation.) 
'''
unique_restaurants = df['Business_ID'].nunique()
print(f'Unique Restaurants: {unique_restaurants}')


'''
2. Which restaurant received the highest 
    number of reviews? What about percentage-wise?
'''
review_counts = df['Business_Name'].value_counts()
highest_reviews = review_counts.idxmax()
total_reviews = df.shape[0]
highest_reviews_count = review_counts.max()
percentage = (highest_reviews_count / total_reviews) * 100
print(f'Restaurant with the highest reviews: {highest_reviews}, Reviews: {highest_reviews_count}, Percentage: {percentage:.2f}%')


'''
3. Which cities have got at least one 5-star review in Nevada (NV) state?
'''
nv_five_star = df[(df['State'] == 'NV') & (df['Avg_Business_Star_Rating'] == 5)]
cities_with_5_star = nv_five_star['City'].unique()
print(f'Cities in NV with at least one 5-star review: {cities_with_5_star}')


'''
4. Which city has the highest number of reviews in the 
    Business Category of “Hotels & Travel”? What about percentage-wise?   
'''
hotels_travel = df[df['Business_Category'] == 'Hotels & Travel']
city_reviews = hotels_travel['City'].value_counts()
highest_city = city_reviews.idxmax()
highest_city_count = city_reviews.max()
percentage_city = (highest_city_count / hotels_travel.shape[0]) * 100
print(f'City with the most reviews in Hotels & Travel: {highest_city}, Reviews: {highest_city_count}, Percentage: {percentage_city:.2f}%')


'''
5. At what day of the week people are more likely to post their reviews?
'''
df['Review_Date'] = pd.to_datetime(df['Review_Date'])
df['Day_of_Week'] = df['Review_Date'].dt.day_name()
most_common_day = df['Day_of_Week'].value_counts().idxmax()
print(f'Most common day of week for reviews: {most_common_day}')


'''
6. Showcase if there are any trends regarding restaurant performance as time goes by.
'''
import matplotlib.pyplot as plt
df['Avg_Star_Over_Time'] = df.groupby('Review_Date')['Avg_Business_Star_Rating'].transform('mean')
df.plot(x='Review_Date', y='Avg_Star_Over_Time', kind='line')
plt.title('Average Star Rating Over Time')
plt.show()


'''
7. Based on analyzed data showcase if there are any steps 
    that the restaurant can take to improve their public appeal.    
'''
from collections import Counter
negative_reviews = df[df['Avg_Business_Star_Rating'] < 3]['Review_Text']
keywords = Counter(" ".join(negative_reviews).split())
common_issues = keywords.most_common(10)
print(f'Common complaints: {common_issues}')
