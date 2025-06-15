MENU = {
        "Tea": {
            "ingredient": {
                "water":300,
                "sugar":200,
                "milk":500,
            },   
            "cost":7
        },
        "fufu": {
            "ingredient": {
                "water":300,
                "sugar":200,
                "milk":500,
            },   
            "cost":6
        },
        "gari": {
            "ingredient": {
                "water":300,
                "sugar":200,
                "milk":500,
                "gari":400,
            },   
            "cost":5
        }

}
items_use = {
    "gari":3000,
    "sugar":2000,
    "milk":3000,
    "water":1000,
    
}


def checking_the_amount(money, choice):
    cost = MENU[choice]["cost"]
    if money >= cost:
        change = money - cost
        print(f"Your change is cedis {change}")
        return True
    return False
    
    
def make_drink(resource, ingredients):
    for item in ingredients:
        resource[item] -= ingredients[item]
    print("Enjoy your drink!")

#create a funtion to check weather the ingradiants are wnoutj to produce

def is_items_enough_to_produce(ingredients, resource):
    for item in ingredients:
        if ingredients[item] > resource.get(item, 0):
            print(f"Sorry, there is not enough {item}")
            return False
    return True
   
    

def main():
    resource = items_use.copy()
    while True:
        try:
            print("\nAvailable items:")
            for item in MENU:
                print(f"- {item}: {MENU[item]['cost']} cedis")
            
            choice = input("\nWhat do you want to buy? ").strip()
            if choice not in MENU:
                print("Invalid choice. Please select from the menu.")
                continue

            ingredients = MENU[choice]["ingredient"]
            if not is_items_enough_to_produce(ingredients, resource):
                continue

            try:
                money = int(input("Insert your money: "))
                if checking_the_amount(money, choice):
                    make_drink(resource, ingredients)
            except ValueError:
                print("Please enter a valid amount.")
                continue

        except KeyboardInterrupt:
            print("\nThank you for using our service!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
    

    
