def minion_game(string_s):
    # your code goes here
    VOWELS = ['A','E','I','O','U']
    len_string = len(string_s)
    stuart_score = 0
    kevin_score = 0
    num_poss_words = 0
    for i, char in enumerate(string_s):
        num_poss_words = len_string - i
        if char in VOWELS:
            kevin_score += num_poss_words
        else:
            stuart_score += num_poss_words
    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif stuart_score < kevin_score:
        print(f'Kevin {kevin_score}')
    else:
        print(f'Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)