import random
verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced', '24/7', 'Lean In', '30,000 foot']
abjectives = ['A/B Tested', 'Freemium', 'Haperlocal', 'Siloed','B-to-B', 'Oriented', 'Claud-based', 'API-Based',]
nouns = ['Erley Adopted', 'Low Hanging Fruit', 'Pipeline', 'Splah Page', 'Productiviti', 'Process', 'Triping point', 'Paradigm']

verb = random.choice(verbs)
abjective = random.choice(abjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + abjective + ' ' + noun

print(phrase)