Power BI Dashboard Instructions
-------------------------------
1. Open Power BI Desktop.
2. Get Data -> Text/CSV -> select the CSVs in the `data/` folder (customers_enriched.csv, orders_for_powerbi.csv, products_for_powerbi.csv)
3. Model: join orders.product_id -> products.product_id, orders.customer_id -> customers_enriched.customer_id
4. Create calculated columns/measures:
   - Conversion Rate = (Orders) / (Sessions)  <-- sample data doesn't include sessions; replace with real events
   - CLV measure: use the 'clv' field from customers_enriched
   - AOV = SUM(total_amount)/COUNT(order_id)
5. Visuals: KPI cards for total revenue, AOV, conversion rate; clustered bar charts for top categories; map for location-based revenue; slicers for date and category.
6. Publish to Power BI service to share.
Note: this repo includes exported CSVs ready for import.
