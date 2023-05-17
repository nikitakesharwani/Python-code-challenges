t1 = (10,20,30,40,50)

def sum_of_tuple(tuple_list):
    sumOfT1 = 0
    for item in tuple_list:
        sumOfT1 += item 
    return sumOfT1

total = sum_of_tuple(t1)
print(total)

# unpacking tuple
a, b, c, d, e = t1 
print(a)
print(b)
print(c)
print(d)
print(e)
print("Total of Tuple : %i" %sum(t1))

t2 = (4,6,8,10)
print(f"t1 , t2 before swapping: {t1} , {t2}")
# swapping t1 and t2
t1 , t2 = t2 , t1

print(f"t1 , t2 after swapping: {t1} , {t2}")

# changing specific value in t1
t1[0] = 2
print(t1) #tuples are immutable