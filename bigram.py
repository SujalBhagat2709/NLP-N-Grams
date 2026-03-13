def bigrams(tokens):
    
    return [(tokens[i], tokens[i+1]) for i in range(len(tokens)-1)]


text = "I love natural language processing".split()

print(bigrams(text))