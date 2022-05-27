# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string

def read_file_content(filename):
    # [assignment] Add your code here 
    filename = open('story.txt' , 'r')
    contents = filename.read()
    
    return contents
    
    #return "Hello World"
print(read_file_content('story.txt'))

def count_words(text):
    text = read_file_content('story.txt')
    new_text = text.translate(str.maketrans('', '', string.punctuation))
    # [assignment] Add your code here
    result = {}
    words = str.split(new_text)

    for word in words:
        if word in result:
            result[word.lower()] +=1
        else:
            result[word.lower()] = 1
    
    return result
   # return {"as": 10, "would": 20}
print(count_words('story.txt'))