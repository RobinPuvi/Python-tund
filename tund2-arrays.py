#numbrid = [1, 2, 3, 4, 65, 6, 7, 8, 9, 10]

#suurem_number = 0
#for x in numbrid:
#    if x > suurem_number:
#        suurem_number = x
#print(suurem_number)

from statistics import median

numbrid = []

mitu_vanust = int(input("Mitu vanust soovid sisestada: "))

for i in range (0, mitu_vanust):
    number = int(input("Number " + str(i) + ": "))
    numbrid.append(number)

summa = 0
for x in numbrid:
    summa = summa + x
print(summa / mitu_vanust)
