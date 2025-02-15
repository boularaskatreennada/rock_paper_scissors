import random

def main():
   print("welcom to Rock Paper Scissor game\n"
      + "Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")
   
   while True:
      print("enter your choice :\n"
            +"1-ROCK\n"
            +"2-PAPER\n"
            +"3-SCISSORS\n")
      player_choice=int(input ("select a number"))
      
      while player_choice<1 or player_choice>3:
         print("select a valid value between 1 and 3")
         player_choice=int(input ("select a number"))

      if player_choice==1:
         Pname="rock"
      elif player_choice==2:
         Pname=="paper" 
      elif player_choice==3:
          Pname="scissors"

      print(f"your choice is {Pname}\n"
            +"now it's computer's turn")
      
      computer_choice=random.randint(1,3)

      if computer_choice==1:
         name="rock"
      elif computer_choice==2:
          name="paper" 
      elif computer_choice==3:
           name="scissors"

      print(f"computer's choice is {name}")

      if player_choice == computer_choice:
        result="Tie"

      elif (player_choice == 1 and computer_choice == 2) or (computer_choice == 1 and player_choice == 2):
        result = "Paper"

      elif (player_choice == 1 and computer_choice == 3) or (computer_choice == 1 and player_choice == 3):
        result = "Rock"

      elif (player_choice == 2 and computer_choice == 3) or (computer_choice == 2 and player_choice == 3):
        result = "Scissors"
      
      if result == "DRAW":
        print("<== It's a tie! ==>")
      elif result == Pname:
        print("<== User wins! ==>")
      else:
        print("<== Computer wins! ==>")
        
      print("Do you want to play again? (Y/N)")
      ans = input().lower()
      if ans == 'n':
         break

if __name__ == "__main__":
   main()
