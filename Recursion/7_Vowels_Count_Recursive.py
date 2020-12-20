def IsVowels(character):
    character=character.lower()
    vowels="aeiou"
    if character in vowels:
        return 1
    else:
        return 0

def CountVowels(string,num):
    if num ==1:
        return IsVowels(string[0])
    else:
        return (CountVowels(string, num-1) + IsVowels(string[num-1]))



string="concentratoin"
print(CountVowels(string,len(string)))