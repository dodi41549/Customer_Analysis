import matplotlib.pyplot as plt
import seaborn as sns

def plot_retention_curve(avg_retention):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=avg_retention.index, y=avg_retention.values, marker='o', color='teal')
    plt.title('Retention Rate Curve', fontsize=16)
    plt.xlabel('Cohort Period (Months)')
    plt.ylabel('Average Retention Rate')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_rfm_distribution(rfm):
    rfm['RFM_Score_Sum'] = rfm['RFM_Score'].astype(str).apply(lambda x: sum([int(d) for d in x]))
    rfm_score_count = rfm['RFM_Score_Sum'].value_counts().sort_index()

    plt.figure(figsize=(10,6))
    sns.barplot(x=rfm_score_count.index, y=rfm_score_count.values, palette='viridis')
    plt.title('Distribution of RFM Score (Summed)', fontsize=16)
    plt.xlabel('RFM Score Sum', fontsize=14)
    plt.ylabel('Number of Customers', fontsize=14)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_clv_histogram(rfm):
    plt.figure(figsize=(10, 6))
    sns.histplot(rfm['Monetary'], bins=50, kde=True, color='orange')
    plt.title('Customer Lifetime Value (Monetary) Distribution')
    plt.xlabel('Monetary Value')
    plt.ylabel('Number of Customers')
    plt.tight_layout()
    plt.show()
