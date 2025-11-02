import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def rock_paper_scissors():
    actions = [rock, paper, scissors]
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
    computer_choice = random.randint(0,2)
    
    print(actions[choice])
    print("Computer chooses: \n", actions[computer_choice])

    # if (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    #     print("Win")
    # elif (choice == computer_choice):
    #     print("Draw")
    # else:
    #     print("Lose")

    result = (choice - computer_choice) % 3
    if result == 0:
        print("It's a draw")
    elif result == 1:
        print("You win!")
    else:
        print("You lose")

def main():
    rock_paper_scissors()

if __name__ == "__main__":
    main()