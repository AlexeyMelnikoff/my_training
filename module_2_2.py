first = int(input())
second = int(input())
third = int(input())
if first != second and first != third:
    print(0)
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)