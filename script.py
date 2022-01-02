import numpy as np

allcharacter = [{"Name" : "Eula", "Element" : "Cryo", "Waepon Type" : "Claymore", "Waepon" : "Waster Greatsword", "ATK" : 50},
                {"Name" : "Raiden Shogun", "Element" : "Electro", "Waepon Type" : "Polearm", "Waepon" : "Beginner's Protector", "ATK" : 40},
                {"Name" : "Sangonomiya Kokomi", "Element" : "Hydro", "Waepon Type" : "Catalyst", "Waepon" : "Apprentice's Notes", "ATK" : 30},
                {"Name" : "Jean", "Element" : "Anemo", "Waepon Type" : "Sword", "Waepon" : "Dull Blade", "ATK" : 20},
                {"Name" : "Mona", "Element" : "Hydro", "Waepon Type" : "Catalyst", "Waepon" : "Apprentice's Notes", "ATK" : 30},
                {"Name" : "Kaedahara Kazuha", "Element" : "Anemo", "Waepon Type" : "Sword", "Waepon" : "Dull Blade", "ATK" : 20},
                {"Name" : "Kamisato Ayaka", "Element" : "Cryo", "Waepon Type" : "Sword", "Waepon" : "Dull Blade", "ATK" : 50},
                {"Name" : "Keqing", "Element" : "Electro", "Waepon Type" : "Sword", "Waepon" : "Dull Blade", "ATK" : 40}]

sword = [{"Name" : "Mistsplitter Reforged", "ATK" : 200},
         {"Name" : "Aquila Favonia", "ATK" : 200},
         {"Name" : "Freedom-Sworn", "ATK" : 100},
         {"Name" : "Dull Blade", "ATK" : 10}]
catalyst = [{"Name" : "Everlasting Moonglow", "ATK" : 300},
            {"Name" : "Dodoco Tales", "ATK" : 200},
            {"Name" : "Solar Pearl", "ATK" : 200},
            {"Name" : "Apprentice's Notes", "ATK": 10}]
claymore = [{"Name" : "Song of Broken Pines", "ATK" : 300},
            {"Name" : "Skyward Pride", "ATK" : 200},
            {"Name" : "Akuoumaru", "ATK" : 100},
            {"Name" : "Waster Greatsword", "ATK" : 10}]
polearm = [{"Name" : "Engulfing Lightning", "ATK" : 300},
           {"Name" : "Staff of Homa", "ATK" : 250},
           {"Name" : "The Catch", "ATK" : 150},
           {"Name" : "Beginner's Protector", "ATK" : 10}]


def login():
    arr_user = np.array = ([["user", "user123", "user"]])

    print("\n" "*** LOGIN ****" "\n")
    username = input("Username : " "\t")
    password = input("Password : " "\t")

    while True:
        for x in arr_user:
            if username == x[0] and password == x[1] and x[2] == "user":
                print("\n\n*** Welcome to Game ***\n")
                menu(chooseHero())
                break
        print("Wrong Input \n\n")
        break

def chooseHero():
  print("\nSelect 1 Hero you want to play: ")
  selectedhero = []
  inputarr = []
  for i in range(len(allcharacter)):
    print("Id : {}".format(i))
    print("Detail : {}".format(allcharacter[i]))
  try:
    for i in range(4):
        isValid = False
        inputs = 0
        while isValid == False :
            inputs = input("\nSilahkan masukkan pilihan Id: ")
            if(inputs in inputarr):
                print("\nError: hero has been picked!")
                isValid = False
            else:
                isValid = True
        inputarr.append(inputs)
        selectedhero.append(allcharacter[int(inputs)])
    return selectedhero
  except:
    return "Wrong Input!"

def checkChara(hero):
    print("=================CHECK CHARA==================")
    for i in range(len(hero)) :
        print(hero[i]["Name"], " - ", hero[i]["Element"], " - ", hero[i]["Waepon"], " - ", hero[i]["ATK"])
    print("")
    print("")


def changeWeapon(hero):
    isRepeatInput = "y"
    while isRepeatInput != "n" and isRepeatInput != "N":
        print("\nSelect 1 Hero you want to change the weapon: ")
        for i in range(len(hero)):
            print("Id : {}".format(i))
            print("Detail : {}".format(hero[i]))
        try:
            selectedWeapon = ""
            selectedAtt = 0
            idx = int(input("silahkan masukkan pilihan Id: "))
            if hero[idx]["Waepon Type"] == "Sword":
                for weapon in range(len(sword)):
                    print("Id : ", format(weapon))
                    print("Detail : ", format(sword[weapon]))
                inputWeapon = int(input("Select your weapon : "))
                selectedWeapon = sword[inputWeapon]["Name"]
                selectedAtt = sword[inputWeapon]["ATK"]
            elif hero[idx]["Waepon Type"] == "Catalyst":
                for weapon in range(len(catalyst)):
                    print("Id : ", format(weapon))
                    print("Detail : ", format(catalyst[weapon]))
                inputWeapon = int(input("Select your weapon : "))
                selectedWeapon = catalyst[inputWeapon]["Name"]
                selectedAtt = catalyst[inputWeapon]["ATK"]
            elif hero[idx]["Waepon Type"] == "Claymore":
                for weapon in range(len(claymore)):
                    print("Id : ", format(weapon))
                    print("Detail : ", format(claymore[weapon]))
                inputWeapon = int(input("Select your weapon : "))
                selectedWeapon = claymore[inputWeapon]["Name"]
                selectedAtt = claymore[inputWeapon]["ATK"]
            elif hero[idx]["Waepon Type"] == "Polearm":
                for weapon in range(len(polearm)):
                    print("Id : ", format(weapon))
                    print("Detail : ", format(polearm[weapon]))
                inputWeapon = int(input("Select your weapon : "))
                selectedWeapon = polearm[inputWeapon]["Name"]
                selectedAtt = polearm[inputWeapon]["ATK"]
            print("Select weapon what you want: ")
            hero[idx]["Waepon"] = selectedWeapon
            if hero[idx]["Element"] == "Cyro":
                selectedAtt *= 5
            elif hero[idx]["Element"] == "Electro":
                selectedAtt *= 4
            elif hero[idx]["Element"] == "Hydro":
                selectedAtt *= 3
            elif hero[idx]["Element"] == "Anemo":
                selectedAtt *= 2
            hero[idx]["ATK"] = selectedAtt
        except Exception as e:
            print(e)
        print("Success changed!")
        checkChara(hero)
        print("=====================")
        isRepeatInput = input("Do you wanna change the weapon again? (input \'n\' or \'N\' for break the input) : ")
    checkChara(hero)


def azdahaFight(attHero, hp):
    print("Azdaha HP : ", hp)
    if(hp < 0):
        print("YOU LOSE : HP IS LOWER THAN ZERO!")
    elif(hp == 0):
        print("YOU WIN : AZDAHA IS END")
    else:
        azdahaFight(attHero, hp-attHero)

def menu(hero):
    repeat = True
    while repeat == True:
        print("1. Check Chara")
        print("2. Change Weeapon")
        print("3. Fight Azdaha")
        print("4. Exit")
        inputMenu = int(input("Select menu : "))
        if(inputMenu == 1):
            checkChara(hero)
        elif(inputMenu == 2) :
            changeWeapon(hero)
        elif(inputMenu == 3):
            defaultHpAzdaha = 10000
            for i in range(len(hero)):
                print("Id : {}".format(i))
                print("Detail : {}".format(hero[i]))
            inputFighter = int(input("Select your fighter : "))

            print("Azhdaha Stage!!")
            print("Azhdaha Stage!!")
            print("Azhdaha Stage!!")

            azdahaFight(hero[inputFighter]["ATK"], defaultHpAzdaha)
        elif(inputMenu == 4):
            repeat = False

# menu(chooseHero())

arr_admin = np.array = ([[]])
login()
