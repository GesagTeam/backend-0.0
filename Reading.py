import mysql.connector
import pandas as pd

# Database connection details
db_config = {
    'user': 'admin',
    'password': 'Gesag%5&7(9',
    'host': 'gesag.cj8ywoakqg0b.ap-southeast-2.rds.amazonaws.com',
    'database': 'university_db'  # Replace with the name of your database
}

# Connect to the MySQL database
connection = mysql.connector.connect(**db_config)

# Query to fetch data from the UNIVERSITY table
university_query = "SELECT * FROM university;"
major_query = "SELECT * FROM major;"

# Fetch data and load it into Pandas DataFrame
university_df = pd.read_sql(university_query, con=connection)
major_df = pd.read_sql(major_query, con=connection)

# Display the data from the UNIVERSITY table
print("UNIVERSITY Data:")
print(university_df)

# Display the data from the MAJOR table
print("\nMAJOR Data:")
print(major_df)

# Close the database connection
connection.close()
