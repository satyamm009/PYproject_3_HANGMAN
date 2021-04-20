import random

print("H A N G M A N")


def show_menu():
    print('Type "play" to play the game, "exit" to quit:')


def main_module():
    choices = ['python', 'java', 'kotlin', 'javascript']
    solution = random.choice(choices)
    unknown = list("-" * (len(solution)))
    shown = "".join(unknown)
    counter = 8
    tried = []
    while counter > 0:
        print()
        shown = "".join(unknown)
        print(shown)
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
        elif letter.islower() != True:
            print('Please enter a lowercase English letter')
        elif letter in tried:
            print("You've already guessed this letter")
        elif letter not in solution:
            print("That letter doesn't appear in the word")
            counter -= 1

        if letter in solution:
            for i in range(len(solution)):
                if letter == solution[i]:
                    unknown[i] = letter

        tried.append(letter)
        if shown == solution:
            print(f'You guessed the word {solution}!')
            print('You survived!')
            break

        if counter == 0:
            if shown == solution:
                print(f'You guessed the word {solution}!')
                print('You survived!')
                break
            else:
                print('You lost!')
                break


while True:
    show_menu()
    in_put = input()
    if in_put == 'play':
        main_module()
    elif in_put == 'exit':
        break
    break

