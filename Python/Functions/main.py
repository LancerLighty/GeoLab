def kilometres_to_miles(number):
    return number * 0.62
print(kilometres_to_miles(10))

def calculate_volume(num1=0, num2=1, num3=1):
    return num1 * num2 * num3
print(calculate_volume(2, 10))
def calculate_average(*num):
    return sum(num) / len(num)

print(calculate_average(2, 6, 8, 10))

def filter_vowel_starting_words(*words):
    words = list(words)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for word in words:
        if not word.lower().startswith(tuple(vowels)):
            words.remove(word);
    return words
def filter_vowel_starting_words2(*words):
    return [word for word in words if word[0].lower() in "aeiou"]
print(filter_vowel_starting_words("Iaragi", "Globusi", "Energia", "Manqana"))
