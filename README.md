# Customer Segmentation Using K-Means Clustering

## Overview

This project demonstrates customer segmentation using the **K-Means clustering algorithm**. The dataset is derived from online retail transactions and processed to create meaningful clusters of customers based on their purchase behavior. The project is an academic assignment for my **Machine Learning course** and showcases practical application of clustering for customer analytics.

## Table of Contents
- [Project Description](#project-description)
- [Dataset](#dataset)
- [Preprocessing Steps](#preprocessing-steps)
- [Methodology](#methodology)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Files Included](#files-included)

## Project Description

The goal of this project is to segment customers into distinct groups based on their purchase behavior, including total spending, purchase frequency, and total quantity purchased. Such segmentation is valuable for targeted marketing strategies and personalized customer interactions.

## Dataset

- **Source**: The dataset was obtained from an online retail platform and processed for analysis. 
- **Key Attributes**:
  - `InvoiceNo`: Transaction invoice number.
  - `StockCode`: Product code.
  - `Quantity`: Number of items purchased.
  - `UnitPrice`: Price per item.
  - `CustomerID`: Unique identifier for each customer.
  - `InvoiceDate`: Date of the transaction.

### Preprocessing Steps

1. Removed duplicate and null records.
2. Filtered out transactions with negative quantities and unit prices.
3. Created new features:
   - `TotalPrice`: Product of `Quantity` and `UnitPrice`.
   - Aggregated customer-level data (`TotalSpend`, `PurchaseFrequency`, `TotalQuantity`).

## Methodology

1. **Feature Scaling**: Standardized customer data using `StandardScaler` to normalize `TotalSpend`, `PurchaseFrequency`, and `TotalQuantity`.
2. **Clustering**: 
   - Applied K-Means clustering with 4 clusters.
   - Evaluated clustering performance using the **Silhouette Score**.
3. **Visualization**: Plotted customer clusters using Seaborn to identify distinct behavioral patterns.

## Results

- **Silhouette Score**: Achieved a score of `0.54`, indicating well-separated clusters.
- Clustering visualization reveals clear segmentation of customers based on spending habits and purchase frequency.

![Customer Segments](cluster_visualization.png)  
(*Replace this placeholder with an actual image of your scatterplot visualization.*)

## Technologies Used

- **Languages**: Python
- **Libraries**: 
  - Pandas
  - NumPy
  - Scikit-learn
  - Matplotlib
  - Seaborn

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/customer-segmentation.git

