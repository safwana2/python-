MENU = {
        "Tea": {
            "ingradient": {
                "water":300,
                "sugar":200,
                "milk":500,
            },   
            "cost":7
        },
        "fufu": {
            "ingradient": {
                "water":300,
                "sugar":200,
                "milk":500,
            },   
            "cost":6
        },
        "gari": {
            "ingradient": {
                "water":300,
                "sugar":200,
                "milk":500,
                "gari":400,
            },   
            "cost":5
        }


items_use = {
    "gari":3000,
    "sugar":2000,
    "mailk":3000,
    "water":1000,
    
}


def checking_the_amount(moneys):
    profit = 0
    cost = MENU[choice]["cost"];
    if moneys >= cost:
       change = moneys - cost
       print(f"your change is cedis {change } " )
       profit+=cost
       
   

       return True
    return False
    
    
def make_coffea(res,ing):
    for items in ingradienst:
         resource[items] - ingradienst[items]
         
    print("enjoy your coffeae")

#create a funtion to check weather the ingradiants are wnoutj to produce

def is_items_enough_to_produce(ingradient): 
     for items in ingradienst:
        if ingradienst[items] > resource.get(items, 0):
           print("sorry there is no enough resources")
           return False

        else:
            return False
   
    

is_true = True


resource = items_use
while is_true :
    choice = input("what do you want to buy ")
    ingradienst = MENU[choice]["ingradient"]
   

    if choice == "Tea" or "gari" or "fufu":
        is_items_enough_to_produce(ingradienst)
        money = int(input("insert in your money "))
        if  checking_the_amount(money):
            make_coffea(resource,ingradienst)
    
        else:
            print("sorry your money is not enough to get you are a tea thank you")
        # check weather the item are ok to be us
    
        

       
    

    
