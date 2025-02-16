# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# %%
df=pd.read_csv('merged_data.csv')

# Exploratory Data Analysis (EDA)
# Top 10 Most Popular Destinations
top_destinations = df["Destination"].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_destinations.values, y=top_destinations.index, palette="Blues_r")
plt.xlabel("Number of Bookings")
plt.ylabel("Destination")
plt.title("Top 10 Most Popular Destinations")
plt.show()

# %%
# Convert date columns to datetime format
df["Booking_Date"] = pd.to_datetime(df["Booking_Date"], format="%d-%m-%Y")
df["Travel_Date"] = pd.to_datetime(df["Travel_Date"], format="%d-%m-%Y")

# Booking Trends Over Time
df["Booking_Month"] = df["Booking_Date"].dt.strftime("%Y-%m")
monthly_trends = df.groupby("Booking_Month")["Booking_ID"].count().reset_index()
plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_trends, x="Booking_Month", y="Booking_ID", marker="o", color="b")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Number of Bookings")
plt.title("Booking Trends Over Time")
plt.show()


# %%
# Ticket Price Variation by Bus Type
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Bus_Type", y="Ticket_Price (INR)", palette="Set2")
plt.xticks(rotation=45)
plt.xlabel("Bus Type")
plt.ylabel("Ticket Price (INR)")
plt.title("Ticket Price Variation by Bus Type")
plt.show()

# %%
Age_Group_Seates_Booked=merged_data.groupby('Age_Group')['Seats_Booked'].sum()
print(Age_Group_Seates_Booked)
Age_Group_Seates_Booked.plot(kind='bar',color='indigo')
plt.title('Age Distribution of Customers')
plt.xticks(rotation=0)
plt.ylabel('Seats Booked')
plt.show()



# %%

Month=merged_data['Booking_Date'].apply(lambda x: x.split('-')[1])
Month.value_counts().sort_index().plot(kind='bar',color='lightblue')
plt.title('Monthly Booking Trends')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=0)
plt.show()

# %%
day_of_week=merged_data['Booking_Date'].apply(lambda x: x.split('-')[0])
day_of_week.value_counts().sort_index().plot(kind='bar',color='lightblue')
plt.title('Booking Trends of Date')
plt.xlabel('Day')
plt.ylabel('Number of Bookings')
plt.xlim(-1,31)
plt.xticks(rotation=0)
plt.show()

# %%
popular_rotes=merged_data['Route_ID'].value_counts().head(10)
popular_rotes.plot(kind='bar',color='y')
plt.title('Top 10 Most Popular Routes')
plt.xlabel('Destination')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=0)
plt.show()

# %%
year_booking=merged_data['Booking_Date'].apply(lambda x: x.split('-')[2])
year_booking.value_counts().sort_index().plot(kind='bar',color='lightblue')
plt.title('Booking Trend of Year')
plt.xlabel('Year')
plt.ylabel('Number of Bookings')
plt.xlim(-1,4)
plt.xticks(rotation=0)
plt.show()

# %%



