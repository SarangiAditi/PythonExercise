start=int(input("Table from: "))
end=int(input("Table to: "))
print("")
for i in range(start,end+1):
  print(f'Table of {i}')
  print("___________")
  for j in range(1,11):
    print(f'{i} x {j} {i*j}')
