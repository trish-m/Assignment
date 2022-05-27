# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


#receive input from user
word1, word2 = input().split()

def find_anagrams(word1,word2):
    # [assignment] Add your code here

    if (sorted(word1) == sorted(word2)):
        return True
    else:
       return False

print(find_anagrams(word1,word2))

