

<br>
a = int(input())<br>
m = a%10<br>
a = a//10<br>
while a > 0:<br>
    if a%10 > m:<br>
        m = a%10<br>
    a = a//10<br>
print(m)<br>
