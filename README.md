# E-Commerce Analytics Project (Sample)
Description:
A sample e-commerce analytics pipeline that computes RFM, estimates CLV, performs KMeans clustering, and prepares CSVs for Power BI visualization.

Folder structure:
- data/ (sample CSV datasets)
- scripts/
  - data_prep.py
  - clv.py
  - clustering.py
- notebook.md
- dashboard_instructions.md
- INTERVIEW_QUESTIONS.md
- requirements.txt
- run.sh

Quick start:
1. Unzip the project and `cd ecom_analytics_project`.
2. (Optional) create and activate a virtualenv.
   python3 -m venv .venv
   source .venv/bin/activate
3. Install requirements:
   pip install -r requirements.txt
4. Run python scripts:
   python3 scripts/data_prep.py
   python3 scripts/clustering.py
   python3 scripts/clv.py
5. Export enriched CSVs for Power BI:
   - Run the notebook steps in notebook.md or run a quick script:
     python3 - <<PY
import pandas as pd
from scripts.data_prep import load_data, aggregate_orders
customers, orders, products = load_data('data')
rfm = aggregate_orders(orders)
rfm.merge(customers, on='customer_id').to_csv('data/customers_enriched.csv', index=False)
orders.to_csv('data/orders_for_powerbi.csv', index=False)
products.to_csv('data/products_for_powerbi.csv', index=False)
PY

6. Open Power BI Desktop and import the CSVs from the `data/` folder.

Notes:
- The sample data is synthetic and for demonstration only.
- Replace sample CSVs with your real data for production use.
- To schedule weekly runs, use cron, Airflow, or Prefect; store outputs to a shared location or DB.
