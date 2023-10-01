values = []
sortnum = []
for i in range(5):
    user_input = int(input())
    values.append(user_input)
values.sort()
values.reverse()
for a in values:
    print(a)

