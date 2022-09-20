import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="travel_agency"
)
mycursor_1=mydb.cursor()
def insert_data(name,departure,book):
    sql="insert into murugan_travel(name,departure,book) values(%s,%s,%s)"
    values=("name,departure,book")
    mycursor_1.execute(sql,values)
    mydb.commit()

print("welcome to murugan travel agency")
global user_name 
def user_info():
    user_name  =(input("enter the user's name"))
    user_address=(input("enter the user's address"))
    user_phoneno=int(input("enter the user's current phone number"))
    departure()
def departure():
    place={   #choose the departure point
           """1 = tiruppur:karur
              2 = karur:trichy
              3 = trichy:tanzore
              4 = tanzore:thiruvarur """
          }
    print(place)
    from_1=(int(input("enter the number for route 1/ 2/ 3/ 4")))
    if from_1==1:
        print("you choosen the route 1")
        route_1()
    elif from_1==2:
        print("you choosen the route 2")
        route_2()
    elif from_1==3:
        print("you choosen the route 3")
        route_3()
    elif from_1==4:
        print("you choosen the route 4")
        route_4()
    else:
        print("please enter 1 or 2 or 3 or 4 otherwise not move to further verification")
def route_1():
    print("tiruppur:karur")
    print("timing:5.30am")
    book_tick()
def route_2():
    print("karur:trichy")
    print("timing:6.00am")
    book_tick()
def route_3():
    print("trichy:tanzore")
    print("timing:8.30pm")
    book_tick()
def route_4():
    print("tanzore:thiruavrur")
    print("timing:9.15pm")
    book_tick()

def book_tick():
    tick_get=(input("choose yes /no for ticket"))
    tick_gets=int(input("enter how many ticket you want"))
    if tick_get=="yes":
        print(f"your booked ticket is {tick_gets} ")
        print("thank you  for booking your tickets in murugan agency")
    else:
        print("your wrong! choose the  correct one")

entry =int(input("enter 1 to register"))
if entry==1:
    print(user_info())
else:
    print("you choose the wrong one! 1 for register ,if not can't move forwards ")   



