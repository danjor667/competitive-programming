# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}
for i in range(n):
    name_phone = input().split(" ")
    name = name_phone[0]
    phone = name_phone[1]
    phoneBook[name] = phone
entry = ' '
while bool(entry) != False:
    try:
        entry = input()
    except Exception:
        break
    res = phoneBook.get(entry, "Not found")
    if res == "Not found":
        print(res)
    else:
        print(f'{entry}={res}')
