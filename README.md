# 🛍️ Customer Segmentation using RFM Analysis

This project performs customer segmentation on an e-commerce dataset using **RFM (Recency, Frequency, Monetary) analysis** and **K-Means Clustering**. It's ideal for businesses to target different customer groups with personalized marketing strategies.

---

## 📁 Project Structure

| File/Folder             | Description                                           |
|-------------------------|-------------------------------------------------------|
| `load_and_explore.py`   | Loads and explores the dataset                        |
| `rfm_analysis.py`       | Performs RFM metric calculation and saves CSV         |
| `rfm_visualization.py`  | Generates and saves distribution & elbow plots        |
| `label_segments.py`     | Labels customer segments after clustering             |
| `rfm.csv`               | Final RFM data with cluster labels                    |
| `.png` files            | Saved plots (histograms, elbow plot, cluster plot)    |

---

## 📊 Dataset

- **Source:** Kaggle – [Online Retail II Dataset](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)
- **Contains:** ~1 Million transactions from a UK-based online retailer (2010–2011)

---

## 📌 Objective

Segment customers based on:
- **Recency**: Days since last purchase
- **Frequency**: Number of purchases
- **Monetary**: Total spend

Apply **K-Means Clustering** to group similar customers and assign labels such as:

- `Champions`
- `Loyal Customers`
- `At Risk`
- `Hibernating`
- etc.

---

## 🧰 Tools & Libraries Used

- `Python 3.x`
- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`

---

## 📈 Outputs & Visualizations

- Histograms of Recency, Frequency, Monetary
- Elbow plot for optimal clusters
- Final RFM CSV with segment labels

📂 Check the `.png` plots uploaded in this repo.

---

## 🚀 Steps to Run

1. Clone this repository or download files.
2. Run `load_and_explore.py` to inspect and clean the dataset.
3. Run `rfm_analysis.py` to generate `rfm.csv`.
4. Run `rfm_visualization.py` to visualize distributions and elbow method.
5. Run `label_segments.py` to add human-readable segment labels.

---

## 🤝 Credits

Dataset from UCI & Kaggle  
Project guided and organized with help from [ChatGPT 🤖].

---

## 📌 Author

**Sai Priya Vankudoth**  
IIT Intern-level Data Analytics Project  
📫 _GitHub Profile_: [Your GitHub URL]

---

