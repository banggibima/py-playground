states_visited = {
  'Eric': ['AK', 'WY', 'WA', 'NH'],
  'Isaac': ['CO', 'WY', 'AK'],
}

for name, states in states_visited.items():
  print(f"{name} has visited:")
  for state in states:
    print(f"\t{state}")