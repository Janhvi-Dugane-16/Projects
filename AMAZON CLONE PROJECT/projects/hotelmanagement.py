#Define the menu of restaurant
menu ={
    'Pizza':80,
    'Pasta':40,
    'Burger':50,
    'Salad':30,
    'Coffee':20,
    'Tea':10,
}

#Greet
print("Welcome to the restaurant")
print("Pizza: Rs.80\nPasta: RS.40\nBurger: Rs.50\nSalad: Rs30\nCoffee: Rs.20\nTea: Rs.10")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Order item {item_1} is not available yet")

    another_order = input("Do you want to add another item? (Yes/No)")
    if another_order == "Yes":
        item_2 = input("Enter the name of the second item you want to order = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item{item_2} has been added to your order")

        else:
          print(f"Ordered item {item_2} is not available!")
print(f"The total amount of item to pay is {order_total}")