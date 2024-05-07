import requests

def start():
    selection = input("""
    What function would you like to run? (Type your selection)
    [1] List of All Countries              
    [2] Search Specific Countries
    [3] Vets List
    [4] Add Vet
    [5] Delete Vet   
    [6] Exit             
    """)
    doingthecheck(selection)

def doingthecheck(selection):
    if selection == "2":
        try:
            country = input("Please Input a Country ")
            results = requests.get(f"http://localhost:8000/api/country_info?country={country}")
            data = results.json()
            dict = data['results'][0]
            for i in dict:
                print(f"{i.capitalize()}: {dict[i]}")
        except:
            print("Sorry, that country does not exist")
         
    elif selection == "1":
        try:
            results = requests.get(f"http://localhost:8000/api/list_countries")
            data = results.json()
            for i in data["results"]:
                print(i["name"])
        except:
            print("Sorry, the host can't be reached")

    elif selection == "3":
        try:
            results = requests.get("http://localhost:8000/api/vets_list")
            data = results.json()
            for i in data["results"]:
                print(f"""{i["first_name"]} {i["last_name"]}""")
        except:
            print("Sorry, the host can't be reached")
            
    elif selection == "4":
        try:
            firstname = input("Please Enter the Vets First Name ")
            lastname = input("Please Enter the Vets Last Name ")
            phone = input("Please Enter the Vets Phone ")
            address = input("Please Enter the Vets Address ")
            room = input("Please Enter the Vets Room ")
            apptime = input("Please Enter the Vets Appointment Times ")
            email = input("Please Enter the Vets Email ")
            results = requests.get(f"http://localhost:8000/api/add_vet?first_name={firstname}&last_name={lastname}&phone={phone}&address={address}&room={room}&appointment_times={apptime}&email={email}")
            data = results.json()
            for i in data["results"]:
                print(i)
        except:
            print("Sorry, that action cannot be excecuted")

    elif selection == "5":
        try:
            firstname = input("What is the Vets First Name? ")
            lastname = input("What is the Vets Last Name? ")
            results = requests.get(f"http://localhost:8000/api/delete_vet?first_name={firstname}&last_name={lastname}")
            data = results.json()
            for i in data["results"]:
                print(i)
        except:
            print("Sorry, that command cannot be excecuted")
    elif selection == "6":
        try:
            exit()
        except:
            print("Only God knows why this failed")
    start()
start()

