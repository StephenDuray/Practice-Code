def ask_user():
    try:
       return int(input("Enter a Number: "))
    except ValueError:
        print("Enter number only")
        return ask_user()


def ask_fruit():
    try:
        fruits = input("Enter a for Apple b for Banana: ").upper()
        if fruits == "A":
            return "Apple"
        elif fruits == "B":
            return "Banana"
        else:
            return fruits
    except Exception:
        return ask_fruit()



display = ask_user()
container = []
for i in range(display):
    container.append(ask_fruit())
    if len(container) > 1:
        finalresult = ",".join(container[:-1]) + " and " + container[-1]
    else:
        finalresult = container[0]
    print(f"You have entered {finalresult} on you list")
