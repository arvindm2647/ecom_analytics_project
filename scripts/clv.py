import pandas as pd

def simple_clv(rfm, margin_rate=0.3):
    # simple historical CLV = average_order_value * frequency * gross margin
    rfm = rfm.copy()
    rfm['avg_order_value'] = rfm['monetary'] / rfm['frequency']
    rfm['clv'] = rfm['avg_order_value'] * rfm['frequency'] * margin_rate
    return rfm[['customer_id','clv']]

if __name__ == '__main__':
    from data_prep import load_data, aggregate_orders
    customers, orders, products = load_data('data')
    rfm = aggregate_orders(orders)
    print(simple_clv(rfm).sort_values('clv', ascending=False).head())
