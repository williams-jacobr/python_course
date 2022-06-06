temps = [221, 234, 340, -9999, 230]

#USING A FOR LOOP
# new_temps = []
# for temp in temps:
#     new_temps.append(temp/10)

#USING LIST COMPREHENSIONS
# new_temps=[temp / 10 for temp in temps]

#USING AN IF STATEMENT IN LIST COMP
# new_temps=[temp / 10 for temp in temps if temp !=-9999]

#USING AN IF-ELSE STATEMENT IN LIST COMP
new_temps=[temp / 10 if temp !=-9999 else 0 for temp in temps ]

print(new_temps)