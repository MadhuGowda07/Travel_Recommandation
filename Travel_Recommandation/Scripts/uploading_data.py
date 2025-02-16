# %%
import boto3 as b3
import pandas as pd
s3_client=b3.client('s3')
s3=b3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# %%
bucket_name='praveen-travels'

object_name='bookings.csv'
s3_client.upload_file(r"C:\Users\madhu\OneDrive\Desktop\Project_Travels\Data\bookings.csv",bucket_name,object_name)
object_name='customers.csv'
s3_client.upload_file(r"C:\Users\madhu\OneDrive\Desktop\Project_Travels\Data\customers.csv",bucket_name,object_name)
object_name='routes.csv'
s3_client.upload_file(r"C:\Users\madhu\OneDrive\Desktop\Project_Travels\Data\routes.csv",bucket_name,object_name)


# %%
bucket_name='praveen-travels'
object_name='routes.csv'

responce=s3_client.get_object(Bucket=bucket_name,Key=object_name)
df=pd.read_csv(responce['Body'])
print(df)

# %%



