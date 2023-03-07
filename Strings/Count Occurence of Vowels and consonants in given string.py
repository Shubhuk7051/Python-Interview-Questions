string=input("Enter a number=")
count_vowels,count_consonant=0,0
for i in string:
    if (i in 'aeiou' or i in 'AEIOU'):
        count_vowels+=1
    else:
        count_consonant+=1
print("Count Occurence of vowels is", count_vowels, "and consonants is", count_consonant)
