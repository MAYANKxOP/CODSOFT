from random import randint

def rps():
    print("WELCOME TO ROCK, PAPER, SICCOR GAME\nPRESS 1 FOR ROCK\nPRESS 2 FOR PAPER\nPRESS 3 FOR SCISSOR")
    user = int(input("ENTER YOUR CHOICE : "))
    comp = randint(1, 3)
    print("COMPUTER'S CHOICE :" ,comp)

    comp_score = 0
    user_score = 0

    if (user == 1 and comp == 1) or (user == 2 and comp == 2) or (user == 3 and comp == 3):
        print("TIE")
        
    elif (comp == 1 and user == 2) or (comp == 2 and user == 1) or (comp == 3 and user == 2): 
        print("COMPUTER WINS")
        comp_score += 1
        print("USER_SCORE = " ,user_score)
        print("COMPUTER_SCORE = " ,comp_score)

    else:
        print("USER WIN'S")
        user_score += 1
        print("COMPUTER_SCORE = " ,comp_score)
        print("USER_SCORE = " ,user_score)
        
while True:
   rps()
   print("Enter OK if you want to play again")
   resume = input().lower()
   if resume != "ok":
      break
   
print("THANKYOU FOR PLAYING")