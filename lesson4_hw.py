contacts = ["Pippa", "Wilbur", "Paul", "Waffle", "Arthur", "Sofia", "Megan","Katsuo", "Elara" ]
target = input("Who are you looking for ? ")
found = False
for i in range(len(contacts)) :
    if contacts[i] == target:
        print("Found", target, "at index", i)
        found = True
        break

if not found:
    print("Contact not found")