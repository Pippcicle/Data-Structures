patient_id = [101, 105, 110, 115, 120, 125, 130, 135, 140, 145]
patient_name = [
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
disease = [
"Influenza",
"Diabetes",
"Asthma",
"Tuberculosis",
"Malaria",
"COVID",
"Chicken pox",
"Hepatitis",
"Measles",
"Pneumonia"
]
doctor = [
"Dr. Maya Thompson",
"Dr. Samuel Patel",
"Dr. Elena Rossi ",
"Dr. Daniel Okafor",
"Dr. Aisha Rahman",
"Dr. Lucas Schneider ",
"Dr. Sofia Alvarez ",
"Dr. Henry Collins",
"Dr. Priya Nair ",
"Dr. Jacob Stein"
]

def display_patients():
    print("Patients")

    for i in range(len(patient_id)):
        print("Patient ID : ", patient_id[i])
        print("Patient name : ", patient_name[i])
        print("Disease : ", disease[i])
        print("Doctor : ", doctor[i])
        print("-" *40)


def linear_search(patient_to_find):
    found = False
    print("\nLinear Search")
    for i in range(len(patient_name)):
        print("Checking : ", patient_name[i])
        if patient_name[i].lower() == patient_to_find.lower():
            print("\nPatiemt Found!")
            print("Patient ID : ", patient_id[i])
            print("Patient Name : ", patient_name[i])
            print("Disease : ", disease[i])
            print("Doctor : ", doctor[i])

            found = True
            break
    if found == False:
        print("Patient is not in database")

def binary_search(id_to_find):
    low = 0
    high= len(patient_id) - 1

    print("\nBinary Search")
    while low <= high :
        mid = (low+high)//2 
        print("Checking Patient ID : ", patient_id[mid])
        if patient_id[mid] == id_to_find:
            print("\nPatient Found!")
            print("Patient ID : ", patient_id[mid])
            print("Patient Name : ", patient_name[mid])
            print("Disease : ", disease[mid])
            print("Doctor : ", doctor[mid])
            return
        elif id_to_find > patient_id[mid]:
            low = mid+1

        else:
            high = mid-1

    print("Patient is not in database")


while True:
    print("\n----------------------------------------")
    print("Hospital Patient Database")
    print("----------------------------------------")

    print("\n1. ) Display All Patients")
    print("\n2. ) Seatch Patient by name (Linear Search)")
    print("\n3. ) Search Patient by ID (Binary Search)")
    print("\n4. ) Exit")

    choice = int(input("\nEnter Your Choice : "))

    if choice == 1 : 
        display_patients()
    elif choice == 2 :
        search_name = input("\nEnter Patients Name : ")
        linear_search(search_name)
    elif choice == 3 : 
        search_id = int(input("\nEnter Patients ID : "))
        binary_search(search_id)
    elif choice == 4 : 
        print("\nThank you. Goodbye")
        break
    else:
        print("Invalid Choice!")