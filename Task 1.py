# Gar = int(input("Namber: "))
# F_Gar = Gar % 10
#  print("Last number:", F_Gar)
# number1 = -120
# Puz = (number1 > 0 and number1 % 2 == 0)
# print(Puz)
#
# Didgit = input('Put Your Didgit ')
# Didgit = int(Didgit)
# if Didgit < 0 or Didgit > 100:
#     print( Didgit, 'Vrong Didjit')
# else:
#     print( Didgit, 'Correct didgit')

# digit = input('Your number')
# digit = int(digit)
# if digit % 3 != 0:
#     print('vrong')
# else: print('Ok')

name = input('Your name is ? ')
age = input('Haw long you worc in QA ?')
Nambr = input('Du you nou wat is peremenay ?').lower()

key_concepts = [
    'oblasti pamyti',
    'data storeg',
    'neemted',
    'saevted',
    'data',
    'mining',
    'konteiner',
    'identifikator'
]

understending_score = sum(concept in Nambr for concept in key_concepts)

if understending_score >= 2:
    print(f'Gud Job!, {name}')
else:
    print(f'Ti Lox {name}  !')