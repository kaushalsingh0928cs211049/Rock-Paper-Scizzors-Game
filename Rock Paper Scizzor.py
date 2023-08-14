#kaushal
print("--------------Welcome Stone Paper Scissor Game--------------")
def singleplayer():
    import random
    l=['rock','paper','scissor']
    n=1 
    count1=0
    count2=0
    while(n<=5):
        user1=input("Enter your choice : ").lower()
        user2=random.choice(l)
        if user1==user2:
            count1+=1
            count2+=1
            print("Match Draw!")
        elif (user1=='scissor'and user2=='paper') or (user1=='rock'and user2=='scissor') or (user1=='paper'and user2=='rock'):
            count1+=1
            print("You won the match!")
        else:
            count2+=1
            print("Computer won the match!")
        n=n+1
    print("Points of User:" ,count1)
    print("Points of Computer:",count2)
    if count1>count2:
        print("User won the match")
    elif count2>count1:
        print("Computer won the match")
    elif count1==count2:
        print("Match Draw")
    print("Game Over")   

def multiplayer():
    n=1 
    count1=0
    count2=0
    while(n<=5):
        user1=input("Enter your choice user1: ").lower()
        user2=input("Enter your choice user2: ").lower()

        if user1==user2:
            count1+=1
            count2+=1
            print("Match Draw")

        elif (user1=='scissor'and user2=='paper') or (user1=='rock'and user2=='scissor') or (user1=='paper'and user2=='rock'):
            count1+=1
            print("User1 won the match")
        else:
            count2+=1
            print("User2 won the match")
        n=n+1
    print("Points of User1:" ,count1)
    print("Points of User2:",count2)
    if count1>count2:
        print("User1 won the match")
    elif count2>count1:
        print("User2 won the match")
    elif count1==count2:
        print("Match Draw")
    print("Game Over")   
    
choice=int(input('''Enter mode
press 1 for single player
press 2 for multiplayer :'''))            
if choice==1:
    singleplayer()
elif choice==2:
    multiplayer()  