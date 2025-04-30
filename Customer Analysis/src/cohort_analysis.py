def create_cohort_index(df):
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
    cohort = df.groupby('CustomerID')['InvoiceMonth'].min().reset_index()
    cohort.columns = ['CustomerID', 'InvoiceMonth_Cohort']
    df = df.merge(cohort, on='CustomerID')
    df['CohortIndex'] = (df['InvoiceMonth'].astype(int) -
                         df['InvoiceMonth_Cohort'].astype(int))
    return df

def create_cohort_pivot(df):
    cohort_counts = df.groupby(['InvoiceMonth_Cohort', 'CohortIndex'])['CustomerID'].nunique().reset_index()
    pivot = cohort_counts.pivot_table(index='InvoiceMonth_Cohort', columns='CohortIndex', values='CustomerID')
    return pivot
