import random
import string
wins = []
loses = []
print(f'''H A N G M A N''')
while True:
    while True:
        act = (input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > '))
        if act == 'exit':
            exit()
        if act == 'results':
            print(f'You won: {len(wins)} times.')
            print(f'You lost: {len(loses)} times.')
        if act == 'play':
            low = string.ascii_lowercase
            options = ['python', 'java', 'swift', 'javascript']
            rand = random.choice(options)
            randl = list(rand)
            i = 8
            print('')
            print(len(randl)*'-')
            rand2 = randl
            store = set()
            store2 = set()
            while i > 0:
                att = (f' # {i} attempts')
                letter = input(f'{i}Input a letter: > ')
                rand2 = [x if x == letter or x in store else '-' for x in randl]
                if letter in randl and letter not in store:
                    store.add(letter)
                    a = (str(rand2)).replace('[','')
                    a = a.replace(']','')
                    a = a.replace(',','')
                    a = a.replace("'",'')
                    a = a.replace(' ','')
                    print('')
                    print(a)
                    if a == rand:
                        break
                elif len(letter) > 1 or len(letter) == 0:
                    print('Please, input a single letter.')
                    a = (str(rand2)).replace('[', '')
                    a = a.replace(']', '')
                    a = a.replace(',', '')
                    a = a.replace("'", '')
                    a = a.replace(' ', '')
                    print('')
                    print(a)
                elif letter not in low and len(letter) == 1:
                    print('Please, enter a lowercase letter from the English alphabet.')
                    a = (str(rand2)).replace('[', '')
                    a = a.replace(']', '')
                    a = a.replace(',', '')
                    a = a.replace("'", '')
                    a = a.replace(' ', '')
                    print('')
                    print(a)
                elif letter in randl and letter in store or letter in store2:
                    print("You've already guessed this letter.")
                    a = (str(rand2)).replace('[', '')
                    a = a.replace(']', '')
                    a = a.replace(',', '')
                    a = a.replace("'", '')
                    a = a.replace(' ', '')
                    print('')
                    print(a)
                else:
                    i -= 1
                    store2.add(letter)
                    print("That letter doesn't appear in the word.")
                    a = (str(rand2)).replace('[', '')
                    a = a.replace(']', '')
                    a = a.replace(',', '')
                    a = a.replace("'", '')
                    a = a.replace(' ', '')
                    print('')
                    print(a)
            print('')
            if a == rand:
                wins.append('a')
                print(f'You guessed the word {a}!')
                print('You survived!')
            else:
                loses.append('a')
                print('You lost!')
