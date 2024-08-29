musicians = []

e_fitzgerald = {
  'first': 'Ella',
  'last': 'Fitzgerald',
}

musicians.append(e_fitzgerald)

j_joplin = {
  'first': 'Janis',
  'last': 'Joplin',
}

musicians.append(j_joplin)

for musician in musicians:
  full_name = f"{musician['first']} "
  full_name += f"{musician['last']}"
  print(full_name)
