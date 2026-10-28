def count_words_init_in(i, string_s, dictionary):
    len_string = len(string_s)
    for j in range(i, len_string):
        current_word = string_s[i:j+1]
        if current_word in dictionary:
            dictionary[current_word] = dictionary[current_word] + 1
        else: # init dictionary
            dictionary[current_word] = 1

def minion_game(string_s):
    # your code goes here
    VOWELS = ['A','E','I','O','U']
    words_init_vowel = dict()
    words_init_consonant = dict()
    for i, char in enumerate(string_s, start=0):
        if char in VOWELS:
            count_words_init_in(i, string_s, words_init_vowel)
        else:
            count_words_init_in(i, string_s, words_init_consonant)
    stuart_score = sum(words_init_consonant.values())
    kevin_score = sum(words_init_vowel.values())
    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif stuart_score < kevin_score:
        print(f'Kevin {kevin_score}')
    else:
        print(f'Draw {kevin_score}')

if __name__ == '__main__':
    s = input()
    minion_game(s)