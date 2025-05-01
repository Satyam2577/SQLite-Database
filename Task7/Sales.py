import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import os

db_path = "orders_data.db"
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            date TEXT,
            item TEXT,
            units INTEGER,
            unit_price REAL
        )
    ''')
    sample_orders = [
        ('2025-04-01', 'Smartphone', 6, 20000),
        ('2025-04-01', 'Tablet', 4, 15000),
        ('2025-04-02', 'Smartwatch', 10, 5000),
        ('2025-04-03', 'Smartphone', 3, 20000),
        ('2025-04-04', 'Earbuds', 20, 2000),
        ('2025-04-04', 'Tablet', 2, 15000),
        ('2025-04-05', 'Earbuds', 15, 2000)
    ]
    cursor.executemany('INSERT INTO orders (date, item, units, unit_price) VALUES (?, ?, ?, ?)', sample_orders)
    conn.commit()
    conn.close()

conn = sqlite3.connect("orders_data.db")
df_summary = pd.read_sql_query('''
    SELECT item, SUM(units) AS total_units, SUM(units * unit_price) AS total_sales
    FROM orders GROUP BY item
''', conn)
df_orders = pd.read_sql_query("SELECT * FROM orders", conn)
conn.close()

print("=== Order Summary ===")
print(df_summary)

colors = plt.cm.tab10.colors[:len(df_summary)]
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Sales Summary Charts", fontsize=16)

axs[0, 0].bar(df_summary['item'], df_summary['total_sales'], color=colors)
axs[0, 0].set_title("Bar Chart - Total Sales")
axs[0, 0].set_xlabel("Item")
axs[0, 0].set_ylabel("Sales (INR)")
axs[0, 0].tick_params(axis='x', rotation=45)

axs[0, 1].plot(df_summary['item'], df_summary['total_sales'], marker='o', linestyle='-', color='green')
axs[0, 1].set_title("Line Chart - Total Sales")
axs[0, 1].set_xlabel("Item")
axs[0, 1].set_ylabel("Sales (INR)")
axs[0, 1].tick_params(axis='x', rotation=45)

axs[1, 0].hist(df_orders['units'], bins=5, color='orange', edgecolor='black')
axs[1, 0].set_title("Histogram - Units Sold")
axs[1, 0].set_xlabel("Units")
axs[1, 0].set_ylabel("Frequency")

axs[1, 1].pie(df_summary['total_sales'], labels=df_summary['item'], autopct='%1.1f%%', colors=colors)
axs[1, 1].set_title("Pie Chart - Sales Share")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("orders_all_charts.png")
plt.show()

df_orders['start'] = pd.to_datetime(df_orders['date'])
df_orders['finish'] = df_orders['start'] + pd.Timedelta(days=1)
gantt_data = df_orders[['item', 'start', 'finish']]
gantt_data = gantt_data.rename(columns={"item": "Task", "start": "Start", "finish": "Finish"})

fig_gantt = ff.create_gantt(gantt_data, index_col="Task", show_colorbar=True, group_tasks=True, title="Gantt Chart - Order Timeline")
fig_gantt.write_html("gantt_chart.html")
fig_gantt.show()
