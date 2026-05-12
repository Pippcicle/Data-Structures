#library book search system

book_ids = [
    101,
    105,
    110,
    115,
    120,
    125,
    130,
    135,
    140,
    145,
    150,
    155,
    160,
    165,
    170,
    175,
    180,
    185,
    190,
    195,
]

book_names = [
    "Python Basics",
    "C Programming",
    "Java Fundamentals",
    "HTML and CSS",
    "JavaScript Essentials",
    "React JS Guide",
    "Data Structures",
    "Algorithms Made Easy",
    "Database Management",
    "Machine Learning Intro",
    "Artificial Intelligence",
    "Operating Systems",
    "Computer Networks",
    "Cyber Security",
    "Cloud Computing",
    "Software Engineering",
    "Web Development",
    "Android Development",
    "Game Development",
    "UI UX Design",
]

authors = [
    "John Smith",
    "Ramesh Kumar",
    "David Miller",
    "Sarah Wilson",
    "Chris Johnson",
    "Emily Brown",
    "Robert Lee",
    "Daniel Clark",
    "Sophia White",
    "Michael Scott",
    "Andrew Tate",
    "Kevin Hart",
    "Lisa Ray",
    "Tony Stark",
    "Steve Rogers",
    "Natasha Romanoff",
    "Bruce Wayne",
    "Clark Kent",
    "Peter Parker",
    "Diana Prince",
]

def display_books():
    print("\n =====LIBRARY BOOK LIST=====")

    for i in range(len(book_ids)):
        print("Book ID : ", book_ids[i])
        print("Book name : ", book_names[i])
        print("Author : ", authors[i])
        print("-" *40)

def linear_search(book_to_find):
    found = False
    print("\nPerforming Linear Search... ")
    for i in range(len(book_names)):
        print("Checking : ", book_names[i])
        if book_names[i].lower() == book_to_find.lower():
            print("\nBook Found!")
            print("Book ID : ", book_ids[i])
            print("Book Name : ", book_names[i])
            print("Author : ", authors[i])

            found = True
            break
    if found == False:
        print("\Book Not Found!")

def binary_search(id_to_find):
    low = 0
    high= len(book_ids) - 1

    print("\nPerforming Binary Search...")
    while low <= high :
        mid = (low+high)//2 
        print("Checking Book ID : ", book_ids[mid])
        if book_ids[mid] == id_to_find:
            print("\nBook Found!")
            print("Book ID : ", book_ids[mid])
            print("Book Name : ", book_names[mid])
            print("Author : ", authors[mid])
            return
        elif id_to_find > book_ids[mid]:
            low = mid+1

        else:
            high = mid-1

    print("\nBook Not Found!")

while True:
    print("\n----------------------------------------")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("----------------------------------------")

    print("\n1. ) Display All Books")
    print("\n2. ) Seatch Book by Name (Linear Search)")
    print("\n3. ) Search Book by ID (Binary Search)")
    print("\n4. ) Exit")

    choice = int(input("\nEnter Your Choice : "))

    if choice == 1 : 
        display_books()
    elif choice == 2 :
        search_name = input("\nEnter Book Name : ")
        linear_search(search_name)
    elif choice == 3 : 
        search_id = int(input("\nEnter Book ID : "))
        binary_search(search_id)
    elif choice == 4 : 
        print("\nThank you. Goodbye")
        break
    else:
        print("Invalid Choice!")