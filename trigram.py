def trigrams(tokens):
    
    return [
        (tokens[i], tokens[i+1], tokens[i+2])
        for i in range(len(tokens)-2)
    ]


text = "I love natural language processing".split()

print(trigrams(text))