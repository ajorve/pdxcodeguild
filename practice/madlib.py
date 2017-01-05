"""
This is a Multiline Comment. THis is the first thing in the file.
AKA 'Module' Docstring.
"""


# Nouns
noun = input("Enter a noun...")
noun2 = input("Enter another noun...")
noun3 = input("Enter final noun...")

# Verbs
verb = input("Enter a verb..")
verb2 = input("Enter another verb...")
verb3 = input("Enter final verb...")

# Adjectives
adj = input("Enter an adjective...")
adj2 = input("Enter another adjective")
adj3 = input("Enter final adjective...")

print("The fox jumped over the {noun}, and the fork ran away with the {noun2}, who did the {noun3} run away with? \n "
      "The {adj} fox {verb} over the fork, the fork {verb2} the spoon, and the {noun} {adj2} {verb2} away, \n "
      "so {noun2} can say that the {adj3} {noun3} {verb3} dug a hole and went away. The End"

      .format(noun, noun2, noun3, verb, verb2, verb3, adj, adj2, adj3))
