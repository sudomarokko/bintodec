import re
import datetime as dt
import time
import sys
import msvcrt

d = ''

while True:

    d = str(input('Please, type binary number: '))

    regex = "^[0-1]+$"
    pattern = re.compile(regex)

    if pattern.search(d) is None:
        print('Please, type binary number correctly. Try again.')
    else:
        break

b = 0
c = str(d)[::-1]

for j in range(0, len(d)):
    b = b + int(c[j]) * 2**j

print(d ,'(2) =', b, '(10)')
hs = True
while hs == True:
    a = dt.datetime.now().strftime('Обновлено в %d.%m.%Y, %H:%M:%S')
    message = ('\r{0}'.format(a))
    sys.stdout.write(str(message))
    time.sleep(10)

    if msvcrt.kbhit():
        k = ord(msvcrt.getch())
        if k == 27:
            hs = False