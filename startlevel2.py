num_rows = 5
for i in range(1, num_rows + 1):
    for j in range(num_rows - i):
        print(" ", end='')
    for k in range(i):
        if k == i - 1:
            print("$", end='\n')
        else:
            print("$", end=' ')