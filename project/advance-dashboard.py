#lets rewrite the previous code again and generate a interactive dash board
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Connect to MySQL (XAMPP)
# -------------------------------
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",        # default XAMPP user
        password="",        # leave blank (no password by default)
        database="testdb"   # make sure this DB exists in phpMyAdmin
    )
    #make use the try except for error handeling purpose
    print("Connected to MySQL (XAMPP)")
except mysql.connector.Error as err:
    print("Connection Error:", err)
    exit()

# -------------------------------
# 2. Fetch Data from MySQL
# -------------------------------
query = "SELECT id, name, salary, department FROM employees"
df = pd.read_sql(query, connection)

print("\n Data fetched from MySQL:")
print(df.head())

# -------------------------------
# 3. Pandas Analysis
# -------------------------------
# Average salary per department
avg_salary = df.groupby("department")["salary"].mean().reset_index()

# Count of employees per department
emp_count = df["department"].value_counts().reset_index()
emp_count.columns = ["department", "count"]

# Salary trend (sorted by employee id)
salary_trend = df.sort_values("id")[["id", "salary"]]

# -------------------------------
# 4. Visualization Dashboard
# -------------------------------
plt.figure(figsize=(14, 8))

# --- Bar Chart: Average Salary ---
plt.subplot(2, 2, 1)
plt.bar(avg_salary["department"], avg_salary["salary"], color="skyblue", edgecolor="black")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# --- Pie Chart: Employee Count ---
plt.subplot(2, 2, 2)
plt.pie(emp_count["count"], labels=emp_count["department"], autopct="%1.1f%%", startangle=140,
        colors=["lightcoral", "lightgreen", "lightblue", "gold"])
plt.title("Employee Distribution by Department")

# --- Line Chart: Salary Trend ---
plt.subplot(2, 1, 2)
plt.plot(salary_trend["id"], salary_trend["salary"], marker="o", linestyle="-", color="purple")
plt.title("Employee Salary Trend (by ID)")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

# -------------------------------
# 5. Close DB Connection
# -------------------------------
connection.close()
print("MySQL connection closed")
