set3 = []
set4 = []                                       #sets for numbers that are divisible by 3 and 4

numb = 1 
while numb <= 2001:                             #goes through all numbers between 1 and 2001 to see if they match
    if numb / 3 == int(numb/3):
        set3.append(numb)
    if numb / 4 == int(numb/4):
        set4.append(numb)

    numb = numb + 1

set34 = []
for element in set3:                            #combines elements that are present in both lists
    for element2 in set4:
        if element == element2:
            set34.append(element)
print(set34)
final = []                                      #removes all elemets divisble by 5
for part in set34:
    if part / 5 != int(part/5):
        final.append(part)
print(final)
print(len(final))
