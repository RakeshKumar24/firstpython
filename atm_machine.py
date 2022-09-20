import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="atm_machinedb"

)
mycursor_1=mydb.cursor()
def insert_data(name,pin_number,balance):
    sql="insert into kandhan_table(name,pin_number,balance) values(%s,%s,%s)"
    values=("name,pin_number,balance")
    mycursor_1.execute(sql,values)
    mydb.commit()



print("Hi Welcome To kandhan Bank !")
print("insert the card")
name=input("enter your name")
pin=2456
balance=20000

while pin != 0:
    user_pin=int(input("please enter the pin number"))
    if user_pin != pin:
        print("you are entered wrong pin number")
    else:
        user_choices = input("B : balance, D : deposit, W : withdraw")
        if user_choices == "B":
            print(F"your total balance is {balance}")
        if user_choices == "D":
            deposit_user = int(input("enter a amount to deposit"))
            total_balance = balance  + deposit_user
            print(f"you have successfully deposited {deposit_user}")
            print(f"Now your total balance is {total_balance}")
        if user_choices == "W":
            withdraw_user = int(input("enter a amount for withdraw"))
            total_balance = balance - withdraw_user
            print(f"you withdrawn {withdraw_user}")
            print(f"now your available balance {total_balance}")
    user_exit = input("would you like to exit? Yes/No")
    if user_exit == "Yes":
        print("Thank you for using Me")
        break
    else:
        continue       




