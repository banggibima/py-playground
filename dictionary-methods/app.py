capitals = {
  'AK': 'Juneau',
  'AL': 'Montgomery',
  'AZ': 'Phoniex',
}

print(capitals.get('AK'))
print(capitals.get('WY'))
print(capitals.get('WY', 'unknown'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())