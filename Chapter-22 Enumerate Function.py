l1 = ["Hokage", "Tsuchikage", "Kazekage", "Raikage", "Mizukage"]
i = 0
for item in l1:
    if i%2 == 0:
        print(item)
    i += 1 

for index,item in enumerate(l1):
    if index%2 == 0:
        print(item)