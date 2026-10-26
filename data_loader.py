import csv
import os

def load_products(filename):
    """Read product offers from a CSV file."""
    products = []

    if not os.path.exists(filename):
        print("CSV file not found:", filename)
        return products

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            required_columns = {"name", "store", "price", "category", "url"}
            if not required_columns.issubset(set(reader.fieldnames or [])):
                print("CSV file is missing one or more required columns.")
                return products

            for row in reader:
                try:
                    price = float(row["price"])
                    if price < 0:
                        print("Skipping a row with a negative price.")
                        continue

                    product = {
                        "name": row["name"].strip(),
                        "store": row["store"].strip(),
                        "price": price,
                        "category": row["category"].strip(),
                        "url": row["url"].strip()
                    }

                    if product["name"] and product["store"]:
                        products.append(product)

                except (ValueError, TypeError):
                    print("Skipping a row with an invalid price.")

    except OSError as error:
        print("Could not read CSV file:", error)

    return products


def save_products(filename, products):
    """Write product offers to a CSV file."""
    columns = ["name", "store", "price", "category", "url"]

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

            for product in products:
                writer.writerow({
                    "name": product["name"],
                    "store": product["store"],
                    "price": "{:.2f}".format(product["price"]),
                    "category": product["category"],
                    "url": product["url"]
                })

        return True

    except OSError as error:
        print("Could not save CSV file:", error)
        return False
