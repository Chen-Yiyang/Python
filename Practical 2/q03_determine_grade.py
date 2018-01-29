# Determining grade
# by Yiyang 29/01/18

_score = int(input("Enter score: "))

if 70 <= _score <= 100:
    print('A')
elif  60 <= _score <= 69:
    print('B')
elif 55 <= _score <= 59:
    print('C')
elif 50 <= _score <= 54:
    print('D')
elif 45 <= _score <= 49:
    print('E')
elif 35 <= _score <= 44:
    print('S')
elif 0 <= _score <= 35:
    print('U')
else:
    print("Invalid! Score must be within 0 - 100.")
