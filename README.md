# Customer_Analysis
# 🛒 Customer Analytics Project - Online Retail

Proyek ini menganalisis data transaksi e-commerce untuk memahami perilaku pelanggan dan membantu pengambilan keputusan bisnis melalui segmentasi pelanggan, analisis retensi, serta perhitungan lifetime value menggunakan teknik **RFM Analysis**, **Cohort Analysis**, dan **Customer Retention Metrics**.

EN :
This project analyzes e-commerce transaction data to understand customer behavior and help make business decisions through customer segmentation, retention analysis, and lifetime value calculation using **RFM Analysis**, **Cohort Analysis**, and **Customer Retention Metrics** techniques.

---

## 📌 Tujuan Proyek (Project Objective)

- Membersihkan dan mempersiapkan data transaksi ritel.
- Mengidentifikasi pelanggan berdasarkan nilai dan perilaku pembelian.
- Menganalisis retensi dan churn pelanggan.
- Memberikan insight melalui visualisasi dan segmentasi.
- Menyediakan dasar untuk strategi pemasaran dan peningkatan loyalitas pelanggan.

EN:
- Cleaning and preparing retail transaction data.
- Identify customers based on value and purchase behavior.
- Analyze customer retention and churn.
- Provide insights through visualization and segmentation.
- Provides the basis for marketing strategies and increased customer loyalty.

---

## 📁 link Dataset Raw and Dataset Clean
- Dataset Raw        : https://www.kaggle.com/datasets/ishanshrivastava28/tata-online-retail-dataset?resource=download
- Dataset Clean      : https://drive.google.com/file/d/1Uwr6nTHvKex2j1bEkFpDfJ3PFVdfXggL/view?usp=sharing

---

## 🛠️ Tools & Technology

- Python 3.10+
- Pandas, Matplotlib, Seaborn, Scikit-Learn
- Google Colab
- Power BI (for interactive dashboards)
- GitHub (for version control & portfolio)

---

## 📊 Tahapan Analisis (Stages of Analysis)

### 1. Data Cleaning
- Menghapus nilai **null** pada kolom `CustomerID` dan `Description`
- Menghapus baris **duplikat**
- Deteksi dan hapus **outlier** menggunakan metode IQR

EN:
- Delete **null** values in `CustomerID` and `Description` columns
- Remove **duplicate** rows
- Detect and remove **outliers** using IQR method

### 2. Feature Engineering
- Menambahkan kolom **TotalPrice**
- Membuat fitur RFM (Recency, Frequency, Monetary)
- Segmentasi menggunakan RFM Score dan KMeans Clustering

EN:
- Added **TotalPrice** column
- Creating RFM features (Recency, Frequency, Monetary)
- Segmentation using RFM Score and KMeans Clustering

### 3. Customer Retention Analysis
- Menghitung **Repeat Purchase Rate**
- Mengklasifikasi pelanggan: **New**, **Active**, **Churn**
- Visualisasi: **Customer Funnel**

EN:
- Calculating **Repeat Purchase Rate**
- Classifying customers: **New**, **Active**, **Churn**
- Visualization: **Customer Funnel**

### 4. Cohort Analysis
- Mengelompokkan pelanggan berdasarkan bulan pertama transaksi
- Menghitung **Retention Rate** dan **visualisasi heatmap cohort**

EN:
- Categorize customers based on the first month of transaction
- Calculate **Retention Rate** and **visualize cohort heatmap**

---

## 📈 Visualization

Beberapa visualisasi utama yang dihasilkan:
- 📉 Retention Rate Curve (line chart)
- 🔥 Heatmap Cohort Retention
- 📊 RFM Segmentation (scatter + histogram)
- 📌 CLV Distribution (histogram)
- 📈 Monthly Active Customers
- 💸 Average Order Value Over Time
- 🔺 Funnel Chart: New → Active → Churn

Semua grafik tersedia di dalam notebook dan bisa diintegrasikan ke Power BI untuk presentasi lebih lanjut.

EN:
Some of the key visualizations generated:
- 📉 Retention Rate Curve (line chart)
- 🔥 Retention Cohort Heatmap
- 📊 RFM Segmentation (scatter + histogram)
- 📌 CLV Distribution (histogram)
- 📈 Monthly Active Customers
- 💸 Average Order Value Over Time
- 🔺 Funnel Chart: New → Active → Churn

All charts are available in the notebook and can be integrated into Power BI for further presentation.

---

## 🚀 Cara Menjalankan Proyek (How to Run the Project)

1. **Buka file notebook:**
   - `notebooks/Customer_Analyst.ipynb` di Google Colab
2. **Pastikan dataset tersedia atau upload:**
   - `Online Retail Data Set.xlsx`
3. **Run semua sel secara berurutan**
4. (Opsional) Simpan hasil `.csv` untuk digunakan di Power BI
5. Lihat hasil visualisasi atau bangun dashboard dari file `data/*.csv`

EN:
1. **Open the notebook file:**
   - `notebooks/Customer_Analyst.ipynb` in Google Colab
2. **Make sure the dataset is available or upload:**
   - `Online Retail Data Set.xlsx`
3. **Run all cells in sequence**
4. (Optional) Save the `.csv` result for use in Power BI
5. View visualization results or build dashboard from `data/*.csv` file

---

## 🧠 Insight & Recomendation

- Mayoritas pelanggan hanya bertransaksi satu kali. Tingkat repeat purchase sekitar **67%**.
- **Segmentasi pelanggan** menunjukkan bahwa sebagian kecil pelanggan memberikan kontribusi tinggi terhadap revenue.
- Pelanggan dengan **recency rendah dan frequency tinggi** adalah target ideal untuk program loyalitas.
- Retention rate turun signifikan setelah bulan ke-1 ➜ perlu strategi onboarding atau re-engagement.
- Disarankan melakukan:
  - 📦 Optimasi stok untuk produk yang sering dibeli ulang
  - 💌 Kampanye khusus untuk pelanggan dengan skor RFM tinggi
  - 🎯 Remarketing untuk pelanggan dengan RFM rendah namun Monetary tinggi

EN:
- The majority of customers only transact once. The repeat purchase rate is around **67%**.
- Customer segmentation** shows that a small percentage of customers contribute highly to revenue.
- Customers with low recency and high frequency** are ideal targets for loyalty programs.
- Retention rate drops significantly after month 1 ➜ need onboarding or re-engagement strategy.
- Recommended to do:
  - 📦 Stock optimization for frequently repurchased products
  - 💌 Special campaigns for customers with high RFM scores
  - 🎯 Remarketing for low RFM but high monetary customers

---

## ✍️ Contributor

**Dodi Al Farisy**  
Data Analyst & Developer  
GitHub: [@dodi41549](https://github.com/dodi41549)

---

## 📄 License

Proyek ini digunakan untuk keperluan pembelajaran dan portofolio pribadi.

EN:
The project is used for learning purposes and personal portfolio.



