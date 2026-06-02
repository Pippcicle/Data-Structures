order_ids = [101, 105, 110, 115, 120, 125, 130, 135, 140, 145]
customers = [
"Oliver",
"Emma",
"Liam",
"Sophia",
"Noah",
"Isabella",
"James",
"Charlotte",
"Ethan",
"Amelia"
]
food_items = [
"Cheese Burger",
"Pepperoni Pizza",
"Chicken Pasta",
"Club Sandwich",
"BBQ Wings",
"Ramen Noodles",
"French Fries",
"Chocolate Cake",
"Tacos",
"Iced Coffee"
]
status = [
"Delivered",
"Preparing",
"Out for Delivery",
"Delivered",
"Preparing",
"Cancelled",
"Delivered",
"Out for Delivery",
"Preparing",
"Delivered"
]
bill = [25, 45, 32, 18, 50, 22, 15, 12, 20, 17]

def display_orders():
    print("\n======== ALL ORDERS ========\n")
    for i in range(len(order_ids)):
        print("Order ID : ", order_ids[i])
        print("Customer : ", customers[i])
        print("Food Item : ", food_items[i])
        print("Order Status : ", status[i])
        print("Total Bill : £",bill[i])

        print("----------------------------------")

def linear_search(customer_name):

    found = False
    print("\nPerforming Linear Search... \n")

    for i in range(len(customers)):
        print("Checking : ", customers[i])

        if customers[i].lower() == customer_name.lower():
            print("\nOrder Found!")
            print("Order ID : ", order_ids[i])
            print("Customer : ", customers[i])
            print("Food Item : ", food_items[i])
            print("Order Status : ", status[i])
            print("Total Bill : £",bill[i])
            
            found = True
            break

    if found == False:
        print("\nCustomer Order Not Found!")

def binary_search(order_to_find):
    low = 0
    high = len(order_ids) - 1 
    print("\nPerforming Binary Search... \n")

    while low <= high : 
        mid = (low+high)//2
        print("Checking Order ID : ", order_ids[mid])

        #order found
        if order_ids[mid] == order_to_find:
            print("\nOrder Found!")
            print("Order ID : ", order_ids[mid])
            print("Customer : ", customers[mid])
            print("Food Item : ", food_items[mid])
            print("Order Status : ", status[mid])
            print("Total Bill : £",bill[mid])
            return
        
        #search right side
        elif order_to_find > order_ids[mid]:
            low= mid+1

        #search left side
        else:
            high = mid-1
    
    print("\n Order not found")

def highest_bill():
    highest = bill[0]
    index = 0

    for i in range(len(bill)):
        if bill[i]>highest:
            highest = bill[i]
            index = i
    
    print("\n======== HIGHEST BILL ========")

    print("Customer : ", customers[index])
    print("Food Item : ", food_items[index])
    print("Bill Amount : £",highest)

while True : 
    print("\n ==========================================")
    print("         FOOD DELIVERY SYSTEM")
    print("==========================================")

    print("\n1. Display All Orders")
    print("2. Search Customer Order(Linear Seacrh")
    print("3. Search Order by ID(Binary Search)")
    print("4. Show Highest Bill")
    print("5. Exit")

    choice = int(input("\nEnter your choice : "))

    if choice == 1 :
        display_orders()

    elif choice ==2 : 
        name = input("Enter Customer name : ")
        linear_search(name)

    elif choice == 3 : 
        order = int(input("\nEnter Order ID : "))
        binary_search(order)
    
    elif choice == 4 : 
        highest_bill()

    elif choice == 5 : 
        print("\n Thank you for using the app")
        break

    else :
        print("\n Invalid Choice. Try again.")