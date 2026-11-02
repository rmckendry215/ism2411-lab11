# customers.py
# Author: Randall McKendry
# Module 11 Lab: Customer Dictionary & Lookup

print("--- Exercise 1 ---")
customer = {
    "name": "Alice", #Key : Value
    "email": "alice@example.com",
    "tier": "gold", 
    "ytd_spend": 12400,
}

print(customer["name"]) #Alice
print(customer["email"]) #alice@example.com
print(customer["tier"]) #gold
print(customer["ytd_spend"]) #12400

print("--- Exercise 2 ---")
customer['phone'] = '555-5555' #adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum' #updating the value of an existing key
print(customer)
del customer['name'] #removing a key-value pair from the dictionary
print(customer)

print(customer.get('ytd_spend',0))

print("--- Exercise 3 ---")
print(customer.get('email', 'no email on file'))

# try:
#     print(customer['email'])
# except KeyError as error:
#     print("KeyError caught: ", error)

for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("--- Exercise 4 ---")
tier_discounts = { 
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.1, 
    "platinum": 0.15 
}

purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']})")
print(f"Discount Rate: {discount_rate*100}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise 5 ---")

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record['tier'], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for name, details in catalog.items():
    print(f"LOW STOCK: {name} - only {details['stock']} left")

print("--- Exercise 8 ---")


# Reflection Questions: [2-3 sentences each]

# In Exercise 3 you saw the difference between .get() and bracket notation. When in real work would you use each one, and what's your rule of thumb for choosing?
#

# Exercise 8 asked you to build a summary dictionary with a loop. What does this pattern remind you of from Excel, and why might the Python version be more useful for large datasets?
#