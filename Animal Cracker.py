def animal_crackers(st):
    for pos,i in enumerate(st):
        if i==" ":
            if st[pos+1]==st[0]:
                return True
            else:
                return False

m=input("Enter a two word String:")
print(animal_crackers(m))
