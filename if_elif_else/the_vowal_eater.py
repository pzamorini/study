import time
# Prompt the user to enter a word
# and assign it to the user_word variable.

words_without_vowel = ''
word = input('Enter a word: ')
user_word = word.upper()

for letter in user_word:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        words_without_vowel += letter


# ignoro as vogais e atribuo a uma variavel
# a palavra sem vogais

for results in words_without_vowel:
    time.sleep(0.5)
    print(results, sep='\n')

# aqui foi só para que o print saisse do jeito que eu queria
