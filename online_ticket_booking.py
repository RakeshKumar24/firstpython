print("welcome to kandha cinemas")
print("1 for ticket booking")
def movies():
    print("1.movie,2.movie,3.movie")
    moto=int(input("choose the movies 1,2,3"))
    if moto==1:
        print("you choosen the movie 1")
        theater()
    elif moto==2:
        print("you choosen the movie 2")
        theater()
    elif moto==3:
        print("you choosen the movie 3")
        theater()
    else:
        print("wrong selection choose the given option")
        movies()
def theater():
    print("1.screen,2.screen,3.screen")
    moto_1=int(input("choose the screen"))
    if moto_1<4:
        print("timing")
        timings()
    else:
        print("wrong option buddy")
        theater()
def timings():
    moto_2=int(input("enter the number of ticket you need"))
    print(f"you have choosen {moto_2} tickets")
    ticket()
def ticket():    
    print("9am:12am, 12pm:3pm, 6pm:10pm, 10pm:1am")
    moto_3=int(input("enter 1 for morningshow,2 for matneeshow,3 for eveningshow,4 for nightshow"))
    if moto_3==1:
        print("you choosen the moringshow 9am:12pm")
    elif moto_3==2:
        print("you choosen the moringshow 12pm:3pm")
    elif moto_3==3:
        print("you choosen the moringshow 6pm:10pm")
    elif moto_3==4:
        print("you choosen the moringshow 10pm:1pm")
    print("thank you for booking the tickets")
booking=int(input("enter number 1 to continue:"))
if booking==1:
     print("now you are allowed to book the ticket")
     movies()

