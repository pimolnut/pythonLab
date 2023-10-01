password = input()
count = ""
ans = 0
for i in password:
    if i.isalpha():
        count += " "
    elif (ord(i) > 32 and ord(i) < 48) or (ord(i) > 57 and ord(i) < 65):
        count += ""
    else:
        count += i
num = count.split(" ")
for char in num:
    if char == '':
        pass
    else:
        ans += int(char)
covert = str(ans)
if len(covert) < 4:
    covert = "00" + covert
    print(covert)
else:
    print(ans)
