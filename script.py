import numpy as np

def login():
    arr_user = np.array = ([["admin", "admin123", "admin"], ["user", "user123", "user"]])

    print("\n" "*** LOGIN ****" "\n")
    username = input("Username : " "\t")
    password = input("Password : " "\t")

    while True:
        for x in arr_user:
            if username == x[0] and password == x[1] and x[2] == "admin":
                print("\n\n" + "*** Welcome to Admin ***" + x[0])
                admin1()
                break

        print("Akun yang anda masukkan salah \n\n")
        break

def admin1():
    r = input(
        "\n1. Masukkan Data Mobil \n2. List Data Mobil \n3. Delete \n4. Keluar \n\nMasukkan Inputan Anda: " "\t")

arr_admin = np.array = ([[]])
login()