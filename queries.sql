-- 1. Total NAV records
SELECT COUNT(*) AS total_nav_records
FROM fact_nav;

-- 2. Average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Highest NAV
SELECT MAX(nav) AS highest_nav
FROM fact_nav;

-- 4. Lowest NAV
SELECT MIN(nav) AS lowest_nav
FROM fact_nav;

-- 5. Total Transactions
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- 6. Transaction Type Distribution
SELECT transaction_type,
COUNT(*) AS total_count
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Total Schemes
SELECT COUNT(*) AS total_schemes
FROM fact_performance;

-- 8. Top 5 Funds by AUM
SELECT scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 9. Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- 10. Risk Grade Distribution
SELECT risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;