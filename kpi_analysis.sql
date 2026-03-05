/* INVESTIGATION: Supply Chain Performance Metrics
   This query calculates the core KPIs I tracked in AWS QuickSight.
   Goal: Identify stockouts (OOS) before they impact revenue.
*/

WITH DailyMetrics AS (
    SELECT 
        product_id,
        transaction_date,
        inventory_on_hand,
        -- Calculate if an item is Out-of-Stock (OOS)
        CASE WHEN inventory_on_hand <= 0 THEN 1 ELSE 0 END AS is_oos,
        -- Calculate On-Time In-Full (OTIF) success
        CASE WHEN delivery_status = 'On-Time' AND fulfillment_status = 'Full' THEN 1 ELSE 0 END AS is_otif
    FROM inventory_transactions
)

SELECT 
    product_id,
    ROUND(AVG(is_otif) * 100, 2) as otif_percentage,
    SUM(is_oos) as days_out_of_stock
FROM DailyMetrics
GROUP BY 1
HAVING days_out_of_stock > 0
ORDER BY days_out_of_stock DESC;
