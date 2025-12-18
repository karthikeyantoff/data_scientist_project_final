# import pandas as pd
# df=pd.read_csv('DATA_SETS/housing_data.csv')
# print("--- Raw Data Loaded ---")
# print(df.info())
# avg_bedrooms = df['total_bedrooms'].mean()
# df['total_bedrooms'] = df['total_bedrooms'].fillna(avg_bedrooms)

# mapping = {
#     '<1H OCEAN': 0,
#     'INLAND': 1,
#     'NEAR OCEAN': 2,
#     'NEAR BAY': 3,
#     'ISLAND': 4
# }
# df['ocean_proximity'] = df['ocean_proximity'].map(mapping)

# # 4. SELECT MAIN FEATURES
# # We will use: Median Income, House Age, Total Rooms, Ocean Proximity
# # Target: Median House Value
# df = df[['median_income', 'housing_median_age', 'total_rooms', 'ocean_proximity', 'median_house_value']]

# # 5. SAVE CLEAN DATA
# df.to_csv('housing_cleaned.csv', index=False)
# print("\n✅ Data Cleaned & Saved as 'housing_cleaned.csv'")
# from flask import Flask,render_template,request
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib
df=pd.read_csv('DATA_SETS/Social_Network_Ads.csv')
x=df.drop('Purchased',axis=1)
y=df['Purchased']
AI_model=KNeighborsClassifier(n_neighbors=300)
AI_model.fit(x,y)
new_data1=int(input("ENTER AGE:"))
new_data2=int(input("ENTER SALARY:"))
p=AI_model.predict([[new_data1,new_data2]])
joblib.dump(AI_model,'ans.pkl')
print("saved")