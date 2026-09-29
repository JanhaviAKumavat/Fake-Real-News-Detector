import mysql.connector
from mysql.connector import Error
from config import Config


# ==========================================
# Initialize Database
# ==========================================

def init_db():

    try:

        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            use_pure=True
        )

        cursor = connection.cursor()

        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DB}"
        )

        print("Database initialized successfully")

        cursor.close()
        connection.close()

    except Error as e:

        print(
            "Database Initialization Error:",
            e
        )


# ==========================================
# Create Database Connection
# ==========================================

def get_db_connection():

    try:

        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            use_pure=True
        )

        if connection.is_connected():

            return connection


    except Error as e:

        print(
            "Database Connection Error:",
            e
        )

        return None



# ==========================================
# Execute SELECT Queries
# ==========================================

def fetch_query(query, values=None):

    connection = get_db_connection()

    if connection:

        cursor = connection.cursor(dictionary=True)

        try:

            cursor.execute(
                query,
                values
            )

            result = cursor.fetchall()

            return result


        except Error as e:

            print(
                "Fetch Error:",
                e
            )

            return None


        finally:

            cursor.close()
            connection.close()

    return None



# ==========================================
# Execute INSERT / UPDATE / DELETE Queries
# ==========================================

def execute_query(query, values=None):

    connection = get_db_connection()

    if connection:

        cursor = connection.cursor()

        try:

            cursor.execute(
                query,
                values
            )

            connection.commit()

            return cursor.lastrowid


        except Error as e:

            print(
                "Query Execution Error:",
                e
            )

            connection.rollback()

            return None


        finally:

            cursor.close()
            connection.close()

    return None