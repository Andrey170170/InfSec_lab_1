import random

array = ["qwertyuiopasdfghjklzxcvbnm",
         "QWERTYUIOPASDFGHJKLZXCVBNM",
         "йцукенгшщзхъфывапролджэячсмитьбю",
         "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ",
         "1234567890",
         "!@#$',;%^:&?*()`-+/|/{}[']_~"
         ]
random.seed()
answer = []
numberOfPasswords = int(input("Enter number of passwords: "))
while numberOfPasswords < 1:
    print('Wrong input, try again')
    numberOfPasswords = int(input("Enter number of passwords: "))
numberOfLetters = int(input("Enter number of letters in password: "))
while numberOfLetters < 6:
    print('Wrong input, try again')
    numberOfLetters = int(input("Enter number of letters in password: "))
print("Options\n1. Low english letters\n2. Up english letters\n3. Low russian letters\n4. Up russian letters\n5. "
      "Numbers\n6. Special symbols")
strOfOptions = input("Enter the options for the password, separated by a space:")
strOfOptions = strOfOptions.split()
numOfOption = list(map(int, strOfOptions))
while (not all(map(lambda el: 0 < el < 7 if True else False, numOfOption))) or (not len(numOfOption) == len(list(set(numOfOption)))):
    print('Wrong input, try again')
    strOfOptions = input("Enter the options for the password, separated by a space:")
    strOfOptions = strOfOptions.split()
    numOfOption = list(map(int, strOfOptions))
for i in range(numberOfPasswords):
    password = ''
    for j in range(numberOfLetters):
        index = random.choice(numOfOption) - 1
        password += random.choice(array[index])
    answer.append(password)
for el in answer:
    print(el)
