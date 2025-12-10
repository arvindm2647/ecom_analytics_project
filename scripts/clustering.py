import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib

def cluster_customers(rfm, n_clusters=4, save_model_path=None):
    df = rfm[['recency_days','frequency','monetary']].copy()
    scaler = StandardScaler()
    X = scaler.fit_transform(df)
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    rfm['cluster'] = labels
    if save_model_path:
        joblib.dump({'model':model,'scaler':scaler}, save_model_path)
    return rfm

if __name__ == '__main__':
    from data_prep import load_data, aggregate_orders
    customers, orders, products = load_data('data')
    rfm = aggregate_orders(orders)
    print(cluster_customers(rfm, n_clusters=4).head())
