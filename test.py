def ask_fruit():
    while True:
        fruits = input("Enter a for Apple, b for Banana: ")
        if fruits.lower() == "a":
            return "Apple"
        elif fruits.lower() == "b":
            return "Banana"
        else:
            print("Invalid input. Please try again!")

def get_fruit_list():
    container = []
    while True:
        fruit = ask_fruit()
        container.append(fruit)
        response = input("Do you want to add another fruit? (y/n): ")
        if response.lower() != "y":
            break
    finalresult = ",".join(container[:-1]) + " and " + container[-1]
    print(f"You have entered {finalresult} on your list")

get_fruit_list()