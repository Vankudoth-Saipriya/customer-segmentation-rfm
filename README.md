# 🧠 Customer Segmentation Using RFM and K-Means Clustering

This project analyzes customer behavior using the **Online Retail II** dataset from Kaggle. The goal is to segment customers using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering for targeted marketing.

## 📂 Project Structure

- `load_and_explore.py`: Loads the data and does initial inspection.
- `clean_data.py`: Cleans and preprocesses the dataset.
- `rfm_analysis.py`: Calculates RFM metrics.
- `rfm_visualization.py`: Shows distribution of RFM values.
- `rfm_cluster.py`: Applies KMeans clustering.
- `label_segments.py`: Labels and saves final segments.
- `rfm_final.csv`: Final segmented customer data.
- `*.png`: Saved plots (RFM histograms, elbow plot, cluster plot).

## 📊 Techniques Used

- RFM Analysis
- K-Means Clustering
- Data Cleaning (Pandas)
- Visualization (Matplotlib, Seaborn)
- Scaling (StandardScaler)

## 📁 Data

- [Online Retail II Dataset](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-data-set-from-uci-ml-repo)

## 🛠 Tools Used

- Python (Pandas, Matplotlib, Seaborn, Scikit-learn)
- Jupyter/VS Code
- Git & GitHub

## 🎯 Outcome

- Identified distinct customer segments.
- Saved labeled segments to `rfm_final.csv`.
- Suitable for targeting marketing strategies.
