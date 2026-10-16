import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Establish database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="commonwealth_games_2026"
)

query_1 = """
SELECT 
    c.country_name,
    SUM(m.gold) AS total_gold,
    SUM(m.silver) AS total_silver,
    SUM(m.bronze) AS total_bronze,
    (SUM(m.gold) + SUM(m.silver) + SUM(m.bronze)) AS total_medals
FROM medal_standings m
JOIN countries c ON m.country_id = c.country_id
GROUP BY c.country_id, c.country_name
ORDER BY total_medals DESC;
"""

df_q1 = pd.read_sql(query_1, con)
con.close()

# 3. Create figure and wrap axis in a list so axes[0] works properly
fig, ax = plt.subplots(figsize=(10, 6))
axes = [ax]

# 4. Chart 1: Horizontal Bar Chart
sns.barplot(
    ax=axes[0],
    x="total_medals",
    y="country_name",
    data=df_q1,
    palette="viridis",
    hue="country_name",
    legend=False
)
axes[0].set_title("1. Top Countries by Total Medals (Query 1)")
axes[0].set_xlabel("Total Medals")
axes[0].set_ylabel("Country")

plt.tight_layout()
plt.show()