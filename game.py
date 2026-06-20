import random
secret_number=random.randint(1,100)
guess=1
count=0
while True:
  guess =int(input("Enter the number you guess:"))
  count+=1
  if secret_number==guess:
    print("Congrats,you guessed in",count," attempts!!")
    break
  if guess>secret_number:
    print(" you are close ! try a smaller number.")
  elif guess<secret_number:
    print("you are close ! try a larger number.")
