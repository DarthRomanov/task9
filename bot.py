#bas
Contacts = {}
WW = True
Listen_comand = False
comand = ""

def add():
    print("pleese input name andd number in format 'name number'")
    new_number = input()
    new_number.split(" ")
    a = new_number[0]
    b = new_number[1]
    Contacts.update([a, b])
    
    

def change():
    new_number = input()
    new_number.split(" ")
    a = new_number[0]
    b = new_number[1]
    Contacts[a] = b

    

def phone():
    print("input name")
    name = input()
    result = Contacts[name]
    

def show_all():

    print(f"{Contacts}")
    

def bye():
    WW = False
    print("Good bye!")
    

while WW == True:
    comand = input()
    if comand == "hello":
        Listen_comand = True
        print("How can I help you?")
        comand = ""
    #else:
        #print("Whait for hello")
while Listen_comand == True:
    if comand == "add":
        add()
    elif comand == "change":
        change()
    elif comand == "phone":
        phone()
    elif comand == "show all":
        show_all()
    elif comand == "good bye" or comand == "close" or comand == "exit":
        bye()