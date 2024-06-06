'''docstring'''

#imports
import sqlite3
#constants and variable
DATABASE = "clashroyale_database.db"
user_input = ''

#functions

def search_cards():
    '''opens up a menu to search for cards'''
    print("Please type the corresponding number, then press Enter.")
    user_input = input('''1. Print all Cards
2. Print all Goblin related cards
3. Print all Skeleton related cards
4. Print all troops that die to Zap
5. Print all troops that die to The Log
6. Print all troops that die to Fireball
7. Print all troops that die to Poison
8. Print all troops that die to Lightning
9. Print all Buildings
10. Print all Spells
11. Print all Troops\n''')
    if user_input == "1":
        print_all_cards()
    elif user_input == "2":
        print_all_goblins()
    elif user_input == '3':
        print_all_skeletons()
    elif user_input == "4":
        print_all_cards_that_die_to_zap()
    elif user_input == "5":
        print_all_cards_that_die_to_log()
    elif user_input == "6":
        print_all_cards_that_die_to_fireball()
    elif user_input == "7":
        print_all_cards_that_die_to_poison()
    elif user_input == "8":
        print_all_cards_that_die_to_lightning()
    elif user_input == "9":
        print_all_buildings()
    elif user_input == "10":
        print_all_spells()
    elif user_input == "11":
        print_all_troops()
    else:
        print("")
        print("INVALID INPUT, PLEASE TRY AGAIN\n")
        search_cards()

def print_all_cards():
    '''prints all cards nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_goblins():
    '''prints all goblin card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE name LIKE '%goblin%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_skeletons():
    '''prints all skeleton card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE name LIKE '%Skeleton%';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_cards_that_die_to_zap():
    '''prints all zappable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '192' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_cards_that_die_to_log():
    '''prints all loggable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '290' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_cards_that_die_to_fireball():
    '''prints all fireballable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '689' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_cards_that_die_to_poison():
    '''prints all poisonable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '728' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_cards_that_die_to_lightning():
    '''prints all lightningable card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE hp < '1056' AND type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_buildings():
    '''prints all building card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE type_id = '2';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_spells():
    '''prints all spell card names'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE type_id = '3';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def print_all_troops():
    '''prints all troop cards'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM card WHERE type_id = '1';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('')
    print("ID  NAME               ELIXIR   RARITY ID   DAMAGE   HP   HIT SPEED   SPEED        TYPE ID")
    for cards in results:
        print(f"{cards[0]:<3} {cards[-1]:<18} {cards[4]:<8} {cards[2]:<11} {cards[3]:<8} {cards[-3]:<4} {cards[-2]:<11} {cards[-4]:<12} {cards[1]}")
    db.close()

def edit_data():
    print("Please type the corresponding number, then press Enter.")
    user_input = input('''1. Add data
2. Remove data
3. Change existing data\n''')

def add_data():
    name = input('What is the name of the card?\n')
    elixir = input('How much does it cost?\n')
    hp = input(f"What is the hp of {name}?\n")
    dmg = input("How much damage does it deal?\n")
    attack_speed = input(f"What is the attack speed of {name}?")
    type_id = input(f'''What is the card type of {name}?
    Please type the corresponding number, then press enter
    1. Troop
    2. Building
    3. Card''')
    rarity_id = input(f'''What is the rarity of {name}?
    Please type the corresponding number, then press enter
    1. Common
    2. Rare
    3. Epic
    4. Legendary
    5. Champion''')
    speed = input(f'''What is the speed of {name}?
    Please type the corresponding number, then press enter
    1. Slow
    2. Medium
    3. Fast
    4. Very Fast''')
    if speed == "1":
        speed = "Slow"
    elif speed == "2":
        speed = "Medium"
    elif speed == "3":
        speed = "Fast"
    elif speed == "4":
        speed = "Very Fast"
    else:
        print("Invalid response")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"INSERT INTO card (type_id, rarity_id, dmg, elixir, speed, hp, attack_speed, name) VALUES ()"
    cursor.execute(sql)
    db.commit()



def remove_data():
    print('tk remove')

def change_data():
    print("tk change")

#maincode
print("Hello! Welcome to Alex Yao's Clash Royale Database.")
print("What would you like to do?")
print("Please type the corresponding number, then press Enter.")
print('''1. Search cards
2. Edit data
3. COMING SOON''')
user_input = input()

if user_input == "1":
    search_cards()
elif user_input == "2":
    edit_data()
elif user_input == "3":
    print('tk')
else:
    print("That is not a valid response, please try again")


