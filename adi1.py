s=input("Input:")
space=0
words=1
char=0
for i in s:
    char+=1
    if i.isspace():
        space+=1
words+=space
print("Spaces: ", space, "\n", "Words: ", words, "\n", "characters: ", char)
    
