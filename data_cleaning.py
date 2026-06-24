import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# =========================
# NAV HISTORY
# =========================
nav = pd.read_csv("data/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

# =========================
# INVESTOR TRANSACTIONS
# =========================
txn = pd.read_csv("data/08_investor_transactions.csv")

txn = txn.drop_duplicates()

txn = txn[txn["amount_inr"] > 0]

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

txn.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

# =========================
# SCHEME PERFORMANCE
# =========================
perf = pd.read_csv("data/07_scheme_performance.csv")

perf = perf.drop_duplicates()

perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Cleaning completed successfully")
print("Files saved in data/processed/")