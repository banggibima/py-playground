name = input("What's your name? ")

print(f"Hello, {name}!")

price = input("How much for the truck? ")
price = float(price)
if price < 10000:
  print("I'll take it.")
