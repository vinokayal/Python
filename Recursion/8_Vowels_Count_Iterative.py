def IsVowels(character):
    character=character.lower()
    vowels="aeiou"
    if character in vowels:
        return 1
    else:
        return 0

def CountVowels(string):
    count =0
    for i in range(len(string)):
        if IsVowels(string[i]):
            count += 1
    return count


string="Educative"
print(CountVowels(string))