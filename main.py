inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

orders = [
    {"order_id": "Order_1", "item_id": 2, "quantity": 2, "status": "Placed", "total": 8.50},
    {"order_id": "Order_2", "item_id": 3, "quantity": 1, "status": "Placed", "total": 3.75},
]


# Query 0: View all items in the inventory with stock less than 20.

# 1. Input:
# Define the threshold for low stock (20) and access the inventory list.
threshold = 20

# 2. Process: Find items with stock below threshold
# Loop through the inventory to find matches
low_stock_items = []
for item in inventory:
    if item["stock"] < threshold:
        # Found one! Add it to our result list
        low_stock_items.append(item)

# 3. Output:
# Print the results
if len(low_stock_items) > 0:
    print("Low stock items found:")
    for item in low_stock_items:
        print(f"- {item['name']}: {item['stock']}")
else:
    print("No low stock items.")



# Query 1: Place a new order for an item and quantity.


# 1. Input:
# ...
item_id = int(input("Enter the Item ID to order: "))
quantity = int(input("Enter the quantity: "))


# 2. Process: [Name process here, e.g. "Validate and create order"]
# ...
for item in inventory:
    if item_id == item["item_id"]:
        if item["stock"] >= quantity:
            item["stock"] -= quantity
            price = quantity * item["unit_price"]
            key = len(orders) + 1
            orders.append(
                    {"order_id": "Order_" + str(key), "item_id": item["item_id"], "quantity": quantity, "status": "Placed", "total": price},
                    )

# 3. Output:
# ...
for order in orders:
    print(order)