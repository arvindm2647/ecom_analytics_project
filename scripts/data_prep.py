import pandas as pd

def load_data(path='data'):
    customers = pd.read_csv(f'{path}/customers.csv', parse_dates=['join_date'])
    orders = pd.read_csv(f'{path}/orders.csv', parse_dates=['order_date'])
    products = pd.read_csv(f'{path}/products.csv')
    return customers, orders, products

def aggregate_orders(orders):
    # compute RFM-like features
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    snapshot = orders['order_date'].max() + pd.Timedelta(days=1)
    rfm = orders.groupby('customer_id').agg({
        'order_date': lambda x: (snapshot - x.max()).days,
        'order_id': 'nunique',
        'total_amount': 'sum'
    }).rename(columns={'order_date':'recency_days','order_id':'frequency','total_amount':'monetary'})
    rfm = rfm.reset_index()
    return rfm

if __name__ == '__main__':
    customers, orders, products = load_data('data')
    rfm = aggregate_orders(orders)
    print(rfm.head())
