def calculate_repeat_purchase_rate(df):
    repeat_counts = df.groupby('CustomerID')['InvoiceNo'].nunique()
    total_customers = len(repeat_counts)
    repeat_customers = (repeat_counts > 1).sum()
    one_time_customers = (repeat_counts == 1).sum()
    return {
        "total": total_customers,
        "repeat": repeat_customers,
        "one_time": one_time_customers,
        "repeat_rate": repeat_customers / total_customers * 100,
        "one_time_rate": one_time_customers / total_customers * 100
    }
