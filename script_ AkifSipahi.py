import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Online Retail.xlsx'
df = pd.read_excel(file_path, sheet_name='Online Retail')

df = df.dropna(subset=['InvoiceNo', 'StockCode', 'Quantity', 'UnitPrice', 'CustomerID'])

df = df.drop_duplicates()

df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

customer_data = df.groupby('CustomerID').agg({
    'TotalPrice': 'sum',    
    'InvoiceNo': 'count',   
    'Quantity': 'sum'      
}).reset_index()

customer_data.columns = ['CustomerID', 'TotalSpend', 'PurchaseFrequency', 'TotalQuantity']

scaler = StandardScaler()
customer_data_scaled = scaler.fit_transform(customer_data[['TotalSpend', 'PurchaseFrequency', 'TotalQuantity']])

kmeans = KMeans(n_clusters=4, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(customer_data_scaled)

score = silhouette_score(customer_data_scaled, customer_data['Cluster'])
print(f"Silhouette Score: {score}")

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=customer_data['TotalSpend'], 
    y=customer_data['PurchaseFrequency'], 
    hue=customer_data['Cluster'], 
    palette='viridis', 
    s=100
)
plt.title("Customer Segments Based on Total Spend and Purchase Frequency")
plt.xlabel("Total Spend")
plt.ylabel("Purchase Frequency")
plt.legend(title="Cluster")
plt.show()

customer_data.to_csv("Clustered_Customers.csv", index=False)
print("Clustered customer data saved as 'Clustered_Customers.csv'.")
