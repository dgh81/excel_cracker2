import timeit

def myCopy(n):
    lineNumber = 100   # resulting file line count
    filename = 'password_' + str(n+1) + '.txt'
    print(filename)

    with open('password.txt', 'r', encoding='UTF-8') as rf:
        with open(filename, 'w', encoding='UTF-8') as wf:
            for i, line in enumerate(rf):
                if i >= lineNumber * n and i < lineNumber * (n+1):
                    wf.write(line)

for n in range (20):
    myCopy(n)

# print('Time: ', timeit.timeit(myCopy, number=1))

