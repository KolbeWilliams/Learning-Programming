#Exercsie 2: Filter out non-palindrome words from a list
def is_Pal(word):
    check = 0
    word = word.upper()
    if(len(word) % 2 == 0):
        middle = int(len(word) / 2)
    else:
        middle = round((len(word) / 2))
    for x in range(middle - 1):
            if(word[x] != word[len(word) - (x+ 1)]):
                check += 1
    if(check == 0):
        return True
    else:
        return False

words = ['Anna', 'hELLo', 'rotor', 'wow', 'CS', 'kayAK', 'programming']
result = list(filter(is_Pal,words))
print(f'Palindrome words in the list: {result}')