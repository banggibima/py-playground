while True:
  name = input("What's your name? ")
  if name == 'quit':
    break
  print(f"Hello, {name}!")

while True:
  age = input("How old are you? ")
  age = int(age)
  if age < 0:
    print("That makes no sense!")
    continue
  print(f"{age} is a great age!")