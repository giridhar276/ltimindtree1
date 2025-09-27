aset = {10,20,20,20,20,20,30}
bset = {30,30,30,30,30,40,40,50,50}

print(aset)
print(bset)

#union opreation
print(aset.union(bset))

#intersection
print(aset.intersection(bset))

# difference
print(aset.difference(bset))

# issubset - if all the elements of A are present in B then True else False
print(aset.issubset(bset))
## issuperset - if all the elemnets of B are present in A then True else False
print(aset.issuperset(bset))

#adding new value to set
aset.add(10)  # no change in set
print(aset)
aset.add(40)   # 40 ggets added to set
print(aset)



