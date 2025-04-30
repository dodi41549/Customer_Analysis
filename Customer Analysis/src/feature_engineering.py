def add_total_price(df):
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df

def add_invoice_month(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
    return df
