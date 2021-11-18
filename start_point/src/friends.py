def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person,food):
    for snacks in (person["favourites"]["snacks"]):
        if snacks == food:
    
             return True
    return False

def add_friend(person,new_friend):
    person["friends"].append(new_friend)

def remove_friend(person,bad_friend):
    person["friends"].remove(bad_friend)

def total_money(people):
    all_money = 0
    
    for person in people:
    
      all_money += person["monies"]    
    return all_money 
    
def lend_money(person_1,person_2,amount):
    person_1["monies"] -= amount
    person_2["monies"] += amount 

def all_favourite_foods(people):
    food_list = []
    for person in people:
        food_list.extend(person["favourites"]["snacks"])
    return food_list

def 






      
    