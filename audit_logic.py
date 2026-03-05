import pandas as pd
import datetime

# I built this script to act as the "First Responder" for data quality.
# At Industrility, we couldn't afford bad data hitting our dashboards, 
# so I automated the audit process to catch anomalies early.

def run_inventory_audit(df):
    print(f"--- 🔍 Investigation Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ---")
    
    # 🕵️ Detective Check 1: Finding "Ghost Inventory" 
    # (High stock levels where sales velocity is zero for 30+ days)
    choke_points = df[(df['inventory_level'] > 500) & (df['sales_velocity'] == 0)]
    
    # 🕵️ Detective Check 2: OTIF (On-Time In-Full) Quality Check
    # If the OTIF rate is missing, our reporting pipeline is broken.
    reporting_anomalies = df['otif_rate'].isnull().sum()
    
    # Generating the 'Verdict'
    summary = {
        "Critical Choke Points": len(choke_points),
        "Data Quality Gaps": reporting_anomalies,
        "Integrity Score": 100 - (reporting_anomalies / len(df) * 100)
    }
    
    print(f"Audit Complete: Found {summary['Critical Choke Points']} choke points.")
    if summary['Data Quality Gaps'] > 0:
        print(f"⚠️ Warning: {summary['Data Quality Gaps']} anomalies detected. Investigating root cause...")
    
    return summary

# Mimicking the AWS Glue transaction environment
if __name__ == "__main__":
    # Example transactional data
    sample_data = pd.DataFrame({
        'item_id': [101, 102, 103, 104],
        'inventory_level': [700, 150, 800, 300],
        'sales_velocity': [0, 15, 0, 5],
        'otif_rate': [0.92, 0.88, None, 0.95]
    })
    
    run_inventory_audit(sample_data)
