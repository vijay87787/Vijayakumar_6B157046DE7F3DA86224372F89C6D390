def linear_search_product(product_list, target_product):
    indices = []

    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)

    return indices

# Example usage:
products = ["apple", "banana", "orange", "apple", "grape", "apple"]
target = "apple"

result = linear_search_product(products, target)

if result:
    print(f"The target product '{target}' was found at indices: {result}")
else:
    print(f"The target product '{target}' was not found in the list.")