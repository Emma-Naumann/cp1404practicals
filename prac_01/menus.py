"""
CP1404 - Practical 1
Menus
"""

MENU_STRING = "(H)ello \n(G)oodbye \n(Q)uit"
name = input("Enter name: ")
print(MENU_STRING)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
    elif choice == "g":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU_STRING)
    choice = input(">>> ").lower()
print("Finished.")

