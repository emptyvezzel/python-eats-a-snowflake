import snowflake.connector
import pandas as pd

# Snowflake connection configuration
account = 'your_account'
user = 'your_user'
password = 'your_password'
warehouse = 'your_warehouse'
database = 'your_database'
schema = 'your_schema'

# Connect to Snowflake
def connect_to_snowflake():
    try:
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        print("Successfully connected to Snowflake.")
        return conn
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        return None

# Fetch data from Snowflake
def fetch_data_from_snowflake(conn):
    query = "SELECT * FROM your_table LIMIT 10;"  # Change this to your actual query
    try:
        df = pd.read_sql(query, conn)
        print("Data fetched successfully.")
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Perform data transformation (example: simple addition of a new column)
def transform_data(df):
    if df is not None:
        df['new_column'] = df['existing_column'] * 2  # Change this transformation as needed
        print("Data transformed successfully.")
        return df
    return None

# Main function to execute the process
def main():
    conn = connect_to_snowflake()
    if conn:
        df = fetch_data_from_snowflake(conn)
        transformed_df = transform_data(df)
        if transformed_df is not None:
            print("Transformed Data:")
            print(transformed_df)
        conn.close()

if __name__ == "__main__":
    main()
