# 🕵️ Case File: The Supply Chain Choke Point
**Status:** Solved | **Outcome:** 15% Reduction in Inventory Costs

### 🔍 The Investigation
At Industrility, our inventory data was moving too fast for manual tracking to keep up. We were processing thousands of daily transactions, but we couldn't see the bottlenecks (the "choke points") until they impacted our operations. I stepped in to build an automated detective tool that could spot these bottlenecks in real-time.

### 🛠️ The Detective's Toolkit
* **AWS Glue & S3**: To handle the heavy lifting of processing daily transaction logs.
* **Python (CloudWatch Integration)**: To build an automated "alarm system" that flags data quality issues before they reach leadership.
* **AWS QuickSight**: To turn raw logs into a visual "Command Center" for senior leadership.

### 📉 The Verdict (Results)
* **15% Savings**: Reduced inventory carrying costs by giving leadership a tool to see OOS (Out-of-Stock) risks early.
* **60% More Accurate**: My automated tests slashed reporting anomalies, ensuring high data integrity.
* **Faster Decisions**: Cut data latency from hours to minutes, enabling immediate operational decision cycles.

---

## 📁 Repository Contents
1. `audit_logic.py`: The Python engine used to sniff out "Ghost Inventory" and data gaps.
2. `kpi_analysis.sql`: The logic used to calculate core KPIs like OTIF (On-Time In-Full).
3. `USAGE_GUIDE.md`: The technical documentation I authored to bridge the gap between engineering and the end-user.
