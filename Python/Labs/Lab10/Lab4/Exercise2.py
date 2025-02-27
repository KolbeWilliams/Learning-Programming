#Exercise 2: Filter out consonants in a string
def findVowels(x):
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    for i in range(len(vowels)):
        if(x == vowels[i]):
            return True
    return False

str1 = 'Computer Science'
print('The vowels in the string are:', list(filter(findVowels,str1)))
