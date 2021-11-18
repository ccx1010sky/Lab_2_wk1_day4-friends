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

def find_no_friends(people):
    
    no_friends_list = []
    
    for person in people:
        if person["friends"] == []:
             no_friends_list.append(person)
    
    return no_friends_list   

def favourite_tv_shows(people):
    fav_tv_list = [] 

    for person in people:
        
        person_list = person["favourites"]["tv_show"]
        if fav_tv_list.count(person_list) == 0:
            fav_tv_list.extend(person["favourites"]["tv_show"])
        fav_tv_list.count()
    










      
    