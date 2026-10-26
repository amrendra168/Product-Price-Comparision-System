from comparison import search_products, get_cheapest_offers, filter_by_category
from data_loader import load_products
from data_collector import add_or_update_offer
from database import save_offers, get_price_history
from analytics import show_price_chart

CSV_FILE = "products.csv"

def show_products(products):
    if not products:
        print("No products found.")
        return

    print("\n{:<22} {:<15} {:>10}  {:<15}".format(
        "Product", "Store", "Price (Rs.)", "Category"
    ))
    print("-" * 67)

    for product in products:
        print("{:<22} {:<15} {:>10.2f}  {:<15}".format(
            product["name"],
            product["store"],
            product["price"],
            product["category"]
        ))


def main():
    products = load_products(CSV_FILE)

    if not products:
        print("No product data could be loaded. Check products.csv.")
        return

    while True:
        print("\n=== Online Product Price Comparison System ===")
        print("1. View all offers")
        print("2. Search for a product")
        print("3. Show cheapest offer for a product")
        print("4. Filter products by category")
        print("5. Add or update an offer")
        print("6. Save current offers to database")
        print("7. View saved price history")
        print("8. Show price comparison chart")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_products(products)

        elif choice == "2":
            keyword = input("Enter product name to search: ").strip()
            results = search_products(products, keyword)
            show_products(results)

        elif choice == "3":
            keyword = input("Enter product name: ").strip()
            results = search_products(products, keyword)

            if not results:
                print("Product not found.")
            else:
                cheapest = get_cheapest_offers(results)
                print("\nCheapest available offer(s):")
                show_products(cheapest)

        elif choice == "4":
            category = input("Enter category: ").strip()
            results = filter_by_category(products, category)
            show_products(results)

        elif choice == "5":
            products = add_or_update_offer(CSV_FILE, products)

        elif choice == "6":
            if save_offers(products):
                print("Offers saved to prices.db.")
            else:
                print("Could not save offers to the database.")

        elif choice == "7":
            keyword = input("Enter product name for history: ").strip()
            history = get_price_history(keyword)

            if not history:
                print("No saved history for that product. Save offers first.")
            else:
                print("\n{:<22} {:<15} {:>10}  {}".format(
                    "Product", "Store", "Price (Rs.)", "Saved at"
                ))
                print("-" * 75)
                for item in history:
                    print("{:<22} {:<15} {:>10.2f}  {}".format(
                        item["name"], item["store"], item["price"], item["saved_at"]
                    ))

        elif choice == "8":
            keyword = input("Enter product name for chart: ").strip()
            results = search_products(products, keyword)
            show_price_chart(results)

        elif choice == "0":
            print("Thank you for using the Price Comparison System.")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 8.")


if __name__ == "__main__":
    main()
