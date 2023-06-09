#Год является високосным, если он делится на 4, за исключением того, что годы, которые делятся на 100,
# не являются високосными, если только они также не делятся на 400. Попросите пользователя ввести год и,
# используя оператор //, определите, сколько високосные годы были между 1600 и этим годом.
hashvich = 0
ls = []
year1 = int(input("write your year \n "))
year = year1 - 1600
year = abs(year)
for i in range(year):

    if (i % 4 == 0):
        true_or_false = 1 
    else:
        true_or_false = 0 

    if ((i % 100) == 0):
        true_or_false = 0 
        if (i % 400 == 0):
            true_or_false = 1
    if true_or_false == 1:
        ls.append(i)
        hashvich += 1
print(ls)
print(hashvich)



