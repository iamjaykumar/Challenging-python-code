items = [int, float, "jay ", 8 , 3, 2 , 22 , 22 , 32 ]

for item in items:

    if str(item).isnumeric() and item>=10:
        print(item)