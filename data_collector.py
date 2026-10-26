from data_loader import save_products

def add_or_update_offer(filename, products):
    """
    Manually add an offer or update the price for the same product and store.
    This function does not collect live prices from websites.
    """
    name = input("Product name: ").strip()
    store = input("Store name: ").strip()

    if not name or not store:
        print("Product name and store name cannot be empty.")
        return products

    price_text = input("Price in rupees: ").strip()

    try:
        price = float(price_text)
        if price < 0:
            print("Price cannot be negative.")
            return products
    except ValueError:
        print("Please enter a valid number for the price.")
        return products

    category = input("Category (for example, Electronics): ").strip()
    url = input("Product URL (optional): ").strip()

    updated = False

    for product in products:
        same_name = product["name"].lower() == name.lower()
        same_store = product["store"].lower() == store.lower()

        if same_name and same_store:
            product["price"] = price
            product["category"] = category
            product["url"] = url
            updated = True
            break

    if not updated:
        new_product = {
            "name": name,
            "store": store,
            "price": price,
            "category": category,
            "url": url
        }
        products.append(new_product)

    if save_products(filename, products):
        if updated:
            print("Offer updated in products.csv.")
        else:
            print("New offer added to products.csv.")
    else:
        print("The offer was changed in memory but could not be saved to the CSV file.")

    return products
