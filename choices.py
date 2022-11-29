from random import randint
from time import sleep

choice1 = input("Write your choice 1: ")
choice2 = input("Write your choice 2: ")
print("\n")
n1 = ""
n2 = ""
i = 0
j = 0
while (i <= 10 and j <= 10):
  n1 = "-" * i
  n2 = "-" * j
  i += randint(0, 1)
  j += randint(0, 1)
  if (i == 9 and j == 9):
    aux = randint(0,1)
    if aux == 0:
      i +=1
    else:
      j +=1
  sleep(0.7)
  print("Choice 1",[n1.ljust(10)], "Choice 2",[n2.ljust(10)])
  if i == 10:
    n1 = "-" * i
    sleep(0.7)
    print("Choice 1",[n1.ljust(10)], "Choice 2",[n2.ljust(10)])
    print("\n")
    print(f"{choice1} is better!")
    break
  elif j == 10:
    n2 = "-" * j
    sleep(0.7)
    print("Choice 1",[n1.ljust(10)], "Choice 2",[n2.ljust(10)])
    print("\n")
    print(f"{choice2} is better!")
    break