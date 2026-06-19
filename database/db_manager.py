import sqlite3

def create_database():

    conn = sqlite3.connect("tracker.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_name TEXT,
        ats_score REAL
    )
    """)

    conn.commit()
    conn.close()


def save_result(name, score):

    conn = sqlite3.connect("tracker.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analysis
        (candidate_name, ats_score)
        VALUES (?, ?)
        """,
        (name, score)
    )

    conn.commit()
    conn.close()


def get_results():

    conn = sqlite3.connect("tracker.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analysis")

    data = cursor.fetchall()

    conn.close()

    return data