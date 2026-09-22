# ==============================================================================
# SMART WAREHOUSE & INVENTORY MANAGEMENT SYSTEM (SWIMS)
# Built using core Python data structures: Lists, Tuples, Dictionaries, Strings, Loops
# ==============================================================================

# GLOBAL DATA STRUCTURES
# 1. Categories Tuple (Immutable fixed categories)
CATEGORIES = ('Electronics', 'Apparel', 'Groceries', 'Stationery', 'Home Decor')

# 2. Suppliers Dictionary
# Format: {supplier_id: {'name': str, 'phone': str, 'city': str}}
suppliers = {
    'S001': {'name': 'Apex Tech Distributors', 'phone': '9876543210', 'city': 'Mumbai'},
    'S002': {'name': 'Global Threads Ltd', 'phone': '9123456780', 'city': 'Surat'},
    'S003': {'name': 'FreshHarvest Agro', 'phone': '9988776655', 'city': 'Pune'},
    'S004': {'name': 'Woodify', 'phone': '9468935670', 'city': 'Kolkata'},
    'S005': {'name': 'Phoolan Devi Wallpaper limited', 'phone': '9545678670', 'city': 'Delhi'}
}

# 3. Inventory Dictionary
# Format: {item_id: {'name': str, 'category': str, 'price': float, 'quantity': int, 'supplier_id': str}}
inventory = {
    'P101': {'name': 'Wireless Mouse', 'category': 'Electronics', 'price': 450.0, 'quantity': 120, 'supplier_id': 'S001'},
    'P102': {'name': 'Cotton T-Shirt', 'category': 'Apparel', 'price': 299.0, 'quantity': 250, 'supplier_id': 'S002'},
    'P103': {'name': 'Organic Basmati Rice', 'category': 'Groceries', 'price': 1200.0, 'quantity': 50, 'supplier_id': 'S003'},
    'P104': {'name': 'Phone', 'category': 'Electronics', 'price': 40000.0, 'quantity': 10, 'supplier_id': 'S001'},
    'P105': {'name': 'LED Bulb', 'category': 'Electronics', 'price': 100.0, 'quantity': 100, 'supplier_id': 'S001'},
    'P106': {'name': 'Pants', 'category': 'Apparel', 'price': 2000.0, 'quantity': 20, 'supplier_id': 'S002'},
    'P107': {'name': 'Turmeric', 'category': 'Groceries', 'price': 35.0, 'quantity': 50, 'supplier_id': 'S003'},
    'P108': {'name': 'Almonds', 'category': 'Groceries', 'price': 305.0, 'quantity': 70, 'supplier_id': 'S003'},
    'P109': {'name': 'Poha', 'category': 'Groceries', 'price': 100.0, 'quantity': 30, 'supplier_id': 'S003'},
    'P110': {'name': 'Jacket', 'category': 'Apparel', 'price': 3000.0, 'quantity': 20, 'supplier_id': 'S002'},
    'P111': {'name': 'Television', 'category': 'Electronics', 'price': 50000.0, 'quantity': 5, 'supplier_id': 'S001'},
    'P112': {'name': 'Pen', 'category': 'Stationery', 'price': 10.0, 'quantity': 200, 'supplier_id': 'S004'},
    'P113': {'name': 'Pencil', 'category': 'Stationery', 'price': 5.0, 'quantity': 100, 'supplier_id': 'S004'},
    'P114': {'name': 'Eraser', 'category': 'Stationery', 'price': 5.0, 'quantity': 50, 'supplier_id': 'S004'},
    'P115': {'name': 'Notebook', 'category': 'Stationery', 'price': 100.0, 'quantity': 40, 'supplier_id': 'S004'},
    'P116': {'name': 'Wallpaper', 'category': 'Home Decor', 'price': 500.0, 'quantity': 10, 'supplier_id': 'S005'},
    'P117': {'name': 'Photo Frame', 'category': 'Home Decor', 'price': 100.0, 'quantity': 50, 'supplier_id': 'S005'},
    'P118': {'name': 'Socks', 'category': 'Apparel', 'price': 200.0, 'quantity': 20, 'supplier_id': 'S002'},
    'P119': {'name': 'Wall Hanging', 'category': 'Home Decor', 'price': 200.0, 'quantity': 35, 'supplier_id': 'S005'},
    'P120': {'name': 'Fake Grass', 'category': 'Home Decor', 'price': 300.0, 'quantity': 15, 'supplier_id': 'S005'}
}

# 4. Transaction Audit Log List (Stores transaction strings)
transaction_logs = [
    "INIT: System initialized with 20 default items and 5 suppliers."
]


def display_header(title):
    print("\n" + "=" * 60)
    print(f" {title.center(56)} ")
    print("=" * 60)


def view_inventory():
    display_header("INVENTORY STOCK LIST")
    if not inventory:
        print("\n[!] Inventory is currently empty.")
        return

    print(f"{'ID':<6} | {'Product Name':<22} | {'Category':<14} | {'Price (₹)':<10} | {'Qty':<5} | {'Supplier':<6}")
    print("-" * 75)
    for item_id, details in inventory.items():
        print(f"{item_id:<6} | {details['name']:<22} | {details['category']:<14} | ₹{details['price']:<9.2f} | {details['quantity']:<5} | {details['supplier_id']:<6}")
    print("-" * 75)


def add_product():
    display_header("ADD NEW PRODUCT")
    item_id = input("Enter unique Product ID (e.g., P104): ").strip().upper()
    if item_id in inventory:
        print(f"\n[Error] Product ID '{item_id}' already exists!")
        return

    name = input("Enter Product Name: ").strip()
    if not name:
        print("\n[Error] Product name cannot be empty.")
        return

    print("\nAvailable Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
    
    try:
        cat_choice = int(input("Select category number: "))
        if cat_choice < 1 or cat_choice > len(CATEGORIES):
            print("\n[Error] Invalid category selection.")
            return
        category = CATEGORIES[cat_choice - 1]
    except ValueError:
        print("\n[Error] Please enter a valid number.")
        return

    try:
        price = float(input("Enter Unit Price (₹): "))
        quantity = int(input("Enter Initial Quantity: "))
        if price < 0 or quantity < 0:
            print("\n[Error] Price and quantity cannot be negative.")
            return
    except ValueError:
        print("\n[Error] Invalid numerical input for price or quantity.")
        return

    supplier_id = input("Enter Supplier ID (e.g., S001): ").strip().upper()
    if supplier_id not in suppliers:
        print(f"\n[Warning] Supplier '{supplier_id}' not found in registry. Adding product with unverified supplier.")

    inventory[item_id] = {
        'name': name,
        'category': category,
        'price': price,
        'quantity': quantity,
        'supplier_id': supplier_id
    }
    
    log_msg = f"ADD: Added item {name} (ID: {item_id}), Qty: {quantity}, Price: ₹{price}"
    transaction_logs.append(log_msg)
    print(f"\n[Success] Product '{name}' added successfully!")


def update_stock():
    display_header("UPDATE STOCK (INBOUND / OUTBOUND)")
    item_id = input("Enter Product ID to update: ").strip().upper()
    if item_id not in inventory:
        print(f"\n[Error] Product ID '{item_id}' not found.")
        return

    item = inventory[item_id]
    print(f"\nProduct: {item['name']} | Current Stock: {item['quantity']}")
    print("1. Restock (Add Stock)")
    print("2. Dispatch / Sell (Reduce Stock)")
    
    choice = input("Select operation (1 or 2): ").strip()
    if choice not in ('1', '2'):
        print("\n[Error] Invalid choice.")
        return

    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("\n[Error] Quantity must be greater than zero.")
            return
    except ValueError:
        print("\n[Error] Please enter a valid integer.")
        return

    if choice == '1':
        item['quantity'] += qty
        log_msg = f"RESTOCK: Added {qty} units to {item['name']} (ID: {item_id})"
        transaction_logs.append(log_msg)
        print(f"\n[Success] Restocked successfully! New quantity: {item['quantity']}")
    else:
        if qty > item['quantity']:
            print(f"\n[Error] Insufficient stock! Only {item['quantity']} units available.")
        else:
            item['quantity'] -= qty
            log_msg = f"DISPATCH: Dispatched {qty} units of {item['name']} (ID: {item_id})"
            transaction_logs.append(log_msg)
            print(f"\n[Success] Stock dispatched successfully! Remaining quantity: {item['quantity']}")


def search_product():
    display_header("SEARCH INVENTORY")
    keyword = input("Enter product name or category keyword to search: ").strip().lower()
    if not keyword:
        print("\n[Error] Search query cannot be empty.")
        return

    found = False
    print(f"\nSearch Results for '{keyword}':")
    print(f"{'ID':<6} | {'Product Name':<22} | {'Category':<14} | {'Price (₹)':<10} | {'Qty':<5}")
    print("-" * 65)
    
    for item_id, details in inventory.items():
        if keyword in details['name'].lower() or keyword in details['category'].lower():
            print(f"{item_id:<6} | {details['name']:<22} | {details['category']:<14} | ₹{details['price']:<9.2f} | {details['quantity']:<5}")
            found = True
            
    if not found:
        print("No matching products found.")
    print("-" * 65)


def manage_suppliers():
    while True:
        display_header("SUPPLIER MANAGEMENT DIRECTORY")
        print("1. View All Suppliers")
        print("2. Add New Supplier")
        print("3. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '1':
            print("\nRegistered Suppliers:")
            print(f"{'ID':<6} | {'Supplier Name':<28} | {'Phone':<12} | {'City':<12}")
            print("-" * 64)
            for s_id, s_info in suppliers.items():
                print(f"{s_id:<6} | {s_info['name']:<28} | {s_info['phone']:<12} | {s_info['city']:<12}")
            print("-" * 64)
        elif choice == '2':
            s_id = input("Enter Supplier ID (e.g., S004): ").strip().upper()
            if s_id in suppliers:
                print("\n[Error] Supplier ID already exists.")
                continue
            name = input("Enter Supplier Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            city = input("Enter City: ").strip()
            
            suppliers[s_id] = {'name': name, 'phone': phone, 'city': city}
            transaction_logs.append(f"SUPPLIER: Added new supplier {name} (ID: {s_id})")
            print(f"\n[Success] Supplier '{name}' added successfully!")
        elif choice == '3':
            break
        else:
            print("\n[Error] Invalid choice. Please choose between 1 and 3.")


def view_reports():
    display_header("WAREHOUSE REPORTS & ANALYTICS")
    if not inventory:
        print("\n[!] No inventory data available for reports.")
        return

    total_items = len(inventory)
    total_units = sum(item['quantity'] for item in inventory.values())
    total_inventory_value = sum(item['price'] * item['quantity'] for item in inventory.values())
    
    # Find most expensive and lowest stock items
    most_expensive = max(inventory.values(), key=lambda x: x['price'])
    low_stock_items = [item['name'] for item in inventory.values() if item['quantity'] < 20]

    print(f"Total Unique Products : {total_items}")
    print(f"Total Physical Units  : {total_units}")
    print(f"Total Inventory Value : ₹{total_inventory_value:,.2f}")
    print(f"Most Expensive Item   : {most_expensive['name']} (₹{most_expensive['price']:.2f})")
    
    print("\nLow Stock Alerts (< 20 units):")
    if low_stock_items:
        for name in low_stock_items:
            print(f" - [!] {name} is running low on stock.")
    else:
        print(" - All items have healthy stock levels.")

    print("\nRecent Transaction Audit Logs:")
    for log in transaction_logs[-5:]:  # Show last 5 logs
        print(f" > {log}")


def main_menu():
    while True:
        display_header("ARUSHI'S SMART WAREHOUSE & INVENTORY SYSTEM")
        print("1. View Inventory Stock")
        print("2. Add New Product")
        print("3. Update Stock (Restock / Dispatch)")
        print("4. Search Product")
        print("5. Manage Suppliers Directory")
        print("6. Warehouse Reports & Analytics")
        print("7. Exit System")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_product()
        elif choice == '3':
            update_stock()
        elif choice == '4':
            search_product()
        elif choice == '5':
            manage_suppliers()
        elif choice == '6':
            view_reports()
        elif choice == '7':
            print("\nThank you for using Smart Warehouse & Inventory Management System. Goodbye!\n")
            break
        else:
            print("\n[Error] Invalid choice! Please select an option between 1 and 7.")


# Program Entry Point
if __name__ == "__main__":
    main_menu()