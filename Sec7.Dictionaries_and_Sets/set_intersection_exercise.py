# which prepositions have been used in the quote

text = """Education is not the learning of facts but the training of the mind to think – Albert Einstein"""
prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
# split text to create a list of words
# create intersection of the sets of words with the preposition

list = text.split()
words = set(list)
print(words)

preps_used = words & prepositions
print(preps_used)

# their solution is to set(words) in the intersection
# words = text.split()

# preps_used = set(words) & prepositions
# print(preps_used)
