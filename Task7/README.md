## Sales Summary Visualization using SQLite & Python

This project is part of a Data Analyst Internship task that demonstrates how to:
- Connect Python with an SQLite database
- Run SQL queries to analyze sales data
- Visualize results using multiple types of charts in one figure

## 📊 Features

- Automatically creates an `orders_data.db` file with a sample `orders` table (if it doesn't exist)
- Executes a SQL query to calculate total units sold and total sales per item
- Generates **5 types of visualizations**:
  - **Bar Chart** – total sales by item (colorful)
  - **Line Chart** – total sales trend
  - **Histogram** – distribution of units sold
  - **Pie Chart** – share of total sales
  - **Gantt Chart** – task timeline of orders (opens in browser)
- Saves the matplotlib visualizations as `orders_all_charts.png`
- Saves the Gantt chart as `gantt_chart.html`

## 🛠 Tools Used

- Python 3.x
- SQLite (`sqlite3`)
- Pandas
- Matplotlib
- Plotly

## ▶️ How to Run

1. Install required packages:
   ```bash
   pip install pandas matplotlib plotly


Run the script:

  '''bash
            python Sales.py


## 📤 Output


  A printed order summary in the terminal

  A saved image: orders_all_charts.png (Bar, Line, Histogram, Pie in one figure)

  A saved HTML: gantt_chart.html (interactive Gantt chart)