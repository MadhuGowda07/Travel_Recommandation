# %%
import pandas as pd

data=pd.read_csv('merged_data.csv')



# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import NearestNeighbors

# Load the dataset
data= "merged_data.csv"
df = pd.read_csv(data)

# Collaborative Filtering Recommendation System
customer_destination_matrix = df.pivot_table(index="Customer_ID", columns="Destination", values="Rating").fillna(0)
knn_model = NearestNeighbors(metric="cosine", algorithm="brute")
knn_model.fit(customer_destination_matrix)

def recommend_destinations(customer_id, num_recommendations=5):
    if customer_id not in customer_destination_matrix.index:
        return "Customer ID not found!"
    
    customer_vector = pd.DataFrame([customer_destination_matrix.loc[customer_id]], columns=customer_destination_matrix.columns)

    distances, indices = knn_model.kneighbors(customer_vector, n_neighbors=num_recommendations + 1)
    
    recommended_destinations = []
    for idx in indices[0][1:]:  # Skip the first as it's the input customer
        similar_customer = customer_destination_matrix.index[idx]
        top_destination = df[df["Customer_ID"] == similar_customer]["Destination"].mode()[0]
        recommended_destinations.append(top_destination)
    
    return recommended_destinations

# Example Usage
sample_customer = df["Customer_ID"].sample(1).values[0]
print(f"Recommended Destinations for Customer {sample_customer}: {recommend_destinations(sample_customer)}")


# %%
# Create a dictionary to store recommendations
all_recommendations = {}

# Loop through all unique customers
for customer_id in customer_destination_matrix.index:
    recommendations = recommend_destinations(customer_id)
    all_recommendations[customer_id] = recommendations

# Convert to DataFrame for better visualization
recommendations_df = pd.DataFrame.from_dict(all_recommendations, orient="index", columns=[f"Recommendation_{i+1}" for i in range(5)])

# Save recommendations to a CSV file
recommendations_df.to_csv("customer_recommendations.csv", index=True)

# Display first few recommendations
print(recommendations_df)


# %%



