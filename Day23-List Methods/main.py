l = [1,2,4,6]
print(type(l))
print(l)
l.append(7)
l.sort()
l.sort(reverse=True)
l.reverse()
print(l.index(4))
print(l.count(1))

m=l.copy()
m[0]=0

l.insert(1,899)

m= [900, 1000, 1100]
k = l+m
print(k)
l.extend(m)

print(l)