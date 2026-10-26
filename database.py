import sqlite3
from datetime import datetime

DATABASE_FILE = "prices.db"

def create_tables(connection):
    """Create database tables if they do not already exist."""
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            store TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT,
            url TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            store TEXT NOT NULL,
            price REAL NOT NULL,
            saved_at TEXT NOT NULL
        )
    """)

    connection.commit()


def save_offers(products):
    """Save current offers and add a price-history record for each offer."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        create_tables(connection)
        cursor = connection.cursor()

        for product in products:
            cursor.execute("""
                SELECT id FROM offers
                WHERE lower(name) = lower(?) AND lower(store) = lower(?)
            """, (product["name"], product["store"]))

            existing_offer = cursor.fetchone()

            if existing_offer:
                cursor.execute("""
                    UPDATE offers
                    SET price = ?, category = ?, url = ?
                    WHERE id = ?
                """, (
                    product["price"], product["category"],
                    product["url"], existing_offer[0]
                ))
            else:
                cursor.execute("""
                    INSERT INTO offers (name, store, price, category, url)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    product["name"], product["store"], product["price"],
                    product["category"], product["url"]
                ))

            cursor.execute("""
                INSERT INTO price_history (name, store, price, saved_at)
                VALUES (?, ?, ?, ?)
            """, (
                product["name"], product["store"], product["price"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))

        connection.commit()
        connection.close()
        return True

    except sqlite3.Error as error:
        print("Database error:", error)
        return False


def get_price_history(keyword):
    """Return saved history records for product names containing a keyword."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        create_tables(connection)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT name, store, price, saved_at
            FROM price_history
            WHERE lower(name) LIKE lower(?)
            ORDER BY saved_at DESC
        """, ("%" + keyword + "%",))

        rows = cursor.fetchall()
        connection.close()

        history = []
        for row in rows:
            history.append({
                "name": row[0],
                "store": row[1],
                "price": row[2],
                "saved_at": row[3]
            })

        return history

    except sqlite3.Error as error:
        print("Database error:", error)
        return []
