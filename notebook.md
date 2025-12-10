# E-Commerce Analytics — Notebook
This notebook walks through loading sample data, computing RFM, CLV, and performing KMeans clustering.
Run each cell in order.

## 1. Setup
```python
import pandas as pd
from data_prep import load_data, aggregate_orders
from clv import simple_clv
from clustering import cluster_customers

customers, orders, products = load_data('data')
rfm = aggregate_orders(orders)
display(rfm.head())
```

## 2. CLV
```python
clv_df = simple_clv(rfm)
display(clv_df.sort_values('clv', ascending=False).head())
```

## 3. Clustering
```python
clustered = cluster_customers(rfm, n_clusters=4)
display(clustered.head())
```

## 4. Export for Power BI
```python
clustered.merge(customers, on='customer_id').to_csv('data/customers_enriched.csv', index=False)
orders.to_csv('data/orders_for_powerbi.csv', index=False)
products.to_csv('data/products_for_powerbi.csv', index=False)
```
