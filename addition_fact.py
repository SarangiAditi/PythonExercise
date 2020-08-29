start=0
end=int(input("Addition fact of "))
print("")
for i in range(start,end+1):
    print(f'{i} + {end} = {i+end} ')
    i=i+1
    end=end-1
