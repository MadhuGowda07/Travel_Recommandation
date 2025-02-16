# %%
import boto3 as b3
import pandas as pd
s3_client=b3.client('s3')
s3=b3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# %%
bucket_name='praveen-travels'
object_name='routes.csv'

responce=s3_client.get_object(Bucket=bucket_name,Key=object_name)
routes_data=pd.read_csv(responce['Body'])
routes_data.head()

# %%
object_name='bookings.csv'

responce=s3_client.get_object(Bucket=bucket_name,Key=object_name)
bookings_data=pd.read_csv(responce['Body'])
bookings_data.head()

# %%
object_name='customers.csv'

responce=s3_client.get_object(Bucket=bucket_name,Key=object_name)
customers_data=pd.read_csv(responce['Body'])
customers_data.head()

# %%
print(bookings_data.isnull().sum())
print(routes_data.isnull().sum())
print(customers_data.isnull().sum())

# %%
for column in bookings_data.columns:
    if bookings_data[column].isnull().any():  # Check if column has missing values
        if bookings_data[column].dtype == "object":  # Categorical column
            bookings_data[column].fillna(bookings_data[column].mode()[0], inplace=True)
        else:  # Numerical column
            bookings_data[column].fillna(bookings_data[column].median(), inplace=True)


# Handling missing values in routes_data
for column in routes_data.columns:
    if routes_data[column].isnull().any():  # Check if column has missing values
        if routes_data[column].dtype == "object":  # Categorical column
            routes_data[column].fillna(routes_data[column].mode()[0], inplace=True)
        else:  # Numerical column
            routes_data[column].fillna(routes_data[column].median(), inplace=True)


# Handling missing values in customers_data
for column in customers_data.columns:
    if customers_data[column].isnull().any():  # Check if column has missing values
        if customers_data[column].dtype == "object":  # Categorical column
            customers_data[column].fillna(customers_data[column].mode()[0], inplace=True)
        else:  # Numerical column
            customers_data[column].fillna(customers_data[column].median(), inplace=True)


# %%
merged_data=pd.merge(bookings_data,customers_data,on='Customer_ID')
merged_data=pd.merge(merged_data,routes_data,on='Route_ID')
merged_data.head()


merged_data.to_csv('merged_data.csv',index=False)

# %%
print("Total_Seats =",merged_data['Seats_Booked'].sum())
merged_data['Ticket_Price (INR)'].sum()
print("Total tickets Prize = ",merged_data['Seats_Booked'].sum()*merged_data['Ticket_Price (INR)'].sum())



# %%
merged_data.head()

# %%
bucket_name='praveen-travels'

object_name='merged_data.csv'
s3_client.upload_file(r'C:\Users\madhu\OneDrive\Desktop\Project_Travels\Scripts\merged_data.csv',bucket_name,object_name)

# %%



