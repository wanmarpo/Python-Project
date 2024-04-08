# A mini calculator that can calculate mean, median and mode

list = [int(item) for item in input("Enter the list items : ").split()]

# Mean
list1 = list
mean = sum(list1)/len(list1)
print(mean)

# Median
list2 = list1
list2.sort()

if len(list2) % 2 == 0:
    m1 = list2[len(list2)//2]
    m2 = list2[len(list2)//2-1]
    median = (m1+m2)/2
else:
    median = list2[len(list2)//2]
print(median)

# Mode
list3 = list1
frequency = {}
for i in list3:
    frequency.setdefault(i,0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)