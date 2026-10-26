def search_products(products, keyword):
    """Return products whose names contain the search keyword."""
    matches = []
    keyword = keyword.lower()

    for product in products:
        if keyword in product["name"].lower():
            matches.append(product)

    return matches

def get_cheapest_offers(products):
    """Return every offer tied for the lowest price."""
    if not products:
        return []

    lowest_price = products[0]["price"]

    for product in products:
        if product["price"] < lowest_price:
            lowest_price = product["price"]

    cheapest = []
    for product in products:
        if product["price"] == lowest_price:
            cheapest.append(product)

    return cheapest


def filter_by_category(products, category):
    """Return products that match a category, ignoring letter case."""
    matches = []
    category = category.lower()

    for product in products:
        if product["category"].lower() == category:
            matches.append(product)

    return matches


def sort_by_price(products):
    """Return a new list sorted from lowest to highest price."""
    sorted_products = products.copy()

    for i in range(len(sorted_products)):
        for j in range(i + 1, len(sorted_products)):
            if sorted_products[j]["price"] < sorted_products[i]["price"]:
                temporary = sorted_products[i]
                sorted_products[i] = sorted_products[j]
                sorted_products[j] = temporary

    return sorted_products
