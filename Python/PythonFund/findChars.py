word_list = ['hello','world','my','name','is','Anna']
char = 'm'

def chars(char, words):
    ans = []
    for word in words:
        if word.find(char) != -1:
            ans.append(word)
    return ans

print chars(char, word_list)