"""Query the database"""

import sqlite3


def query():
    """Query the database and perform insert, update, and delete operations"""
    conn = sqlite3.connect("BirthDataDB.db")
    cursor = conn.cursor()

    # Perform SELECT
    cursor.execute("SELECT * FROM BirthDataDB")
    print("Current records in BirthDataDB:")
    print(cursor.fetchall())

    # Perform INSERT only if the record does not already exist
    cursor.execute(
        "SELECT COUNT(*) FROM BirthDataDB WHERE year = 2000 AND month = 1 "
        "AND date_of_month = 15"
    )
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            """
            INSERT INTO BirthDataDB (
                year, month, date_of_month, day_of_week, births
            ) VALUES (
                2000, 1, 15, 7, 9500
            )
            """
        )

    # Perform UPDATE
    cursor.execute(
        """
        UPDATE BirthDataDB 
        SET births = 10000
        WHERE year = 2000 AND month = 1 AND date_of_month = 16
        """
    )

    # Perform DELETE
    cursor.execute(
        """
        DELETE FROM BirthDataDB 
        WHERE year = 2000 AND month = 1 AND date_of_month = 17
        """
    )

    conn.commit()  # Ensure all changes are saved
    conn.close()
    return "Success"  # Return success for testing
