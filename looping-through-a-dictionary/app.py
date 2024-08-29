capitals = {
  'AK': 'Juneau',
  'AL': 'Montgomery',
  'AZ': 'Phoniex',
}

for state in capitals:
  print(f"State: {state}")

for capital in capitals.values():
  print(f"Capital: {capital}")

for state, capital in capitals.items():
  print(f"{capital}, {state}")