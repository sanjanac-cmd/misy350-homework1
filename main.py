inventory = [
    {"item_id": 1, "name": "Espresso", "unit_price": 2.50, "stock": 40},
    {"item_id": 2, "name": "Latte", "unit_price": 4.25, "stock": 25},
    {"item_id": 3, "name": "Cold Brew", "unit_price": 3.75, "stock": 30},
    {"item_id": 4, "name": "Mocha", "unit_price": 4.50, "stock": 20},
    {"item_id": 5, "name": "Blueberry Muffin", "unit_price": 2.95, "stock": 18},
]

orders = [
    {"order_id": "Order_101", "item_id": 2, "quantity": 2, "status": "Placed", "total": 8.50},
    {"order_id": "Order_102", "item_id": 3, "quantity": 1, "status": "Placed", "total": 3.75},
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


# 2. Process: [Validate and create order]
# ...
for item in inventory:
    if item_id == item["item_id"]:
        if item["stock"] >= quantity:
            item["stock"] -= quantity
            price = quantity * item["unit_price"]
            key = 100 + len(orders) + 1
            orders.append(
                    {"order_id": "Order_" + str(key), "item_id": item["item_id"], "quantity": quantity, "status": "Placed", "total": price},
                    )
        else:
            print("Not enough stock")

# 3. Output:
# ...
for item in inventory:
    print(item)


# Query 2: View all orders placed for a particular item.
# Prompt the user for the item name.

# 1. Input:
# ...
search_item = input("Enter the item name to search (e.g. 'Latte'): ")



# 2. Process: [Find orders for item]
# ...
search_item_orders = []
for item in inventory:
    if item["name"] == search_item:
        item_id = item["item_id"]
        for order in orders:
            if order["item_id"] == item_id:
                search_item_orders.append(order)


# 3. Output:
# ...
for order in search_item_orders:
    print(order)


# Query 3: Total number of orders placed for "Cold Brew".

# 1. Input:
# ...




# 2. Process: [Count Cold Brew Orders]
# ...
order_amount = 0
for item in inventory:
    if item["name"] == "Cold Brew":
        item_id = item["item_id"]
        for order in orders:
            if order["item_id"] == item_id:
                order_amount += 1

# 3. Output:
# ...
print("Number of orders of Cold Brew: ", order_amount)



# Query 4: Update item stock quantity by item id.

# 1. Input:
# ...
item_id = int(input("Enter ID of item to update: "))
new_stock = int(input("Enter new stock quantity: "))



# 2. Process: [Name process here, e.g. "Validate and update stock"]
# ...
for item in inventory:
    if item["item_id"] == item_id:
        item["stock"] = new_stock


# 3. Output:
# ...
print(f"item id: {item_id} stock changed to {new_stock} \n")
for item in inventory:
    print(item)


# Query 5: Cancel an order and restore stock.

# 1. Input:
# ...
cancel_order_id = input("Enter Order ID to cancel: ")


# 2. Process: [Name process here, e.g. "Cancel order"]
# ...
for order in orders:
    if order["order_id"] == cancel_order_id:
        order["status"] = "Cancelled"
        item_id = order["item_id"]
        quantity = order["quantity"]
        for item in inventory:
            if item["item_id"] == item_id:
                item["stock"] += quantity

# 3. Output:
# ...
for item in inventory:
    print(item)
for order in orders:
    print(order)
