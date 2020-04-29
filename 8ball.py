"""Magic 8 ball
"""

import random
import time
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 
'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 
'Try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 
'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')
print('I am the Magic 8 Ball, What is your name?')
name = input()
print('\nHello ' + name)


def magic_8_ball():
    input("You may ask me yes or no question, give it a try: \n")
    print("Thinking...")
    time.sleep(random.randrange(0,5))
    print (random.choice(answers) )
    print('I hope that helped!')
    replay()
    
def replay():
    reply = input("Would you like to ask another question? (Y or N) ").upper()
    if reply == 'Y':
        magic_8_ball()
    elif reply == 'N':
        print("Come back if you have more questions!")
    else:
        print('I apologies, I did not catch that. Please repeat.')
        replay()

if __name__ == "__main__" :		
    magic_8_ball()