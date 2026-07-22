word = "deba l"

for i in range(len(word)):
    if word[i] == " ":
        word = word[:i] + " "
        break

print(word)