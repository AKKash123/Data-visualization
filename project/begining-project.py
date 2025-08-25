
# -------------------------------
# 1. importing the library using the command to install it in your system
# pip install mysql-connector-python 
# pip install pandas 
# pip install matplotlib
# -------------------------------
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
# -------------------------------
#  Connect to MySQL Database
# -------------------------------
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",   # leave blank for XAMPP
#     database="testdb"
# )

connection = mysql.connector.connect(
    host="localhost",       # Your host, e.g., "127.0.0.1"
    user="root",            # Your MySQL username
    password="",            # Your MySQL password
    database="testdb"       # Your database name
)

# -------------------------------
# 2. Fetch Data from MySQL
# -------------------------------
query = "SELECT id, name, salary, department FROM employees"
df = pd.read_sql(query, connection)

print("Data fetched from MySQL:")
print(df.head())

# -------------------------------
# 3. Data Analysis with Pandas
# -------------------------------
# Average salary by department
avg_salary = df.groupby("department")["salary"].mean().reset_index()

print("\nAverage Salary by Department:")
print(avg_salary)

# -------------------------------
# 4. Data Visualization with Matplotlib
# -------------------------------
plt.figure(figsize=(8,5))
plt.bar(avg_salary["department"], avg_salary["salary"], color="skyblue", edgecolor="black")
plt.title("Average Salary by Department", fontsize=14)
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# -------------------------------
# 5. Close DB Connection
# -------------------------------
connection.close()