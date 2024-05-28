import random
def computer_choice():
    return random.choice(['rock','paper','scissors'])
def user_choice():
    while True:
        choice=int(input('1.Rock\n2.Paper\n3.Scissors\nChoose an option:'))
        if(choice!=0 and choice<=3):
            break
        else:
            print('Please choose valid option')
    return choice
def decide_winner(get_computer_choice,get_user_choice):
    if get_user_choice==get_computer_choice:
        return "It's won"
    elif (get_user_choice=='rock' and get_computer_choice=='scissors') or (get_user_choice=='scissors' and get_computer_choice=='paper') or(get_user_choice=='Paper' and get_computer_choice=='rock'):
        return 'You won'
    else:
        return 'Computer won'

def main():
    user_score=0
    computer_score=0
    rps_dict={
        1:'rock',
        2:'paper',
        3:'scissors'
    }
    while  True:
        option=user_choice()
        get_user_choice=rps_dict[option]
        get_computer_choice=computer_choice()
        print(f'You choose:{get_user_choice}')
        print(f'Computer choose:{get_computer_choice}')
        result=decide_winner(get_computer_choice,get_user_choice)
        if result=="It's won":
            user_score+=1
        else:
            computer_score+=1
        print(f'Score - You:{user_score} computer:{computer_score}')
        play_again=input('Do you want to play again(Y/N)').lower()
        if play_again=='n':
            print('Thank you for Playing')
            break
        else:
            continue
main()