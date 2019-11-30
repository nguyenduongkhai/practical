def main():
    #Example
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    #a
    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    #b
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    #c
    stars =int(input("How many starts you want me to print:"))
    for i in range(stars ):
        print('*',end='')
    print('\n\n')

    #d
    count_stars=(int)(input("Input here:"))
    for i in range(count_stars+1):
        for j in range (i):
            print('*',end='')
        print()

main()