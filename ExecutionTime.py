# Calculating the excution time of the programme
from time import time

start = time()

word = "Python program to create acronyms"
text = word.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time: {:.12f}".format(execution_time))