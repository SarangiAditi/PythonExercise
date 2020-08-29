animals_list=list([])
for i in range(1,11):
  animals_list.append(input("Enter animal name: "))
for i,v in enumerate(animals_list):
  print(f'({i}) {v}')
