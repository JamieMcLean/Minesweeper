def bombBoard3():
    placement = ['O','1','@','2','@','O','O','1','@',
                 'O','O','1','O','O','1','O','O','1',
                 'O','O','O','O','2','O','O','O','O',
                 '1','@','1','O','@','@','O','O','O',
                 'O','O','O','O','O','3','O','O','O',
                 'O','O','O','1','O','O','@','O','O',
                 'O','O','@','O','O','2','@','2','O',
                 '1','2','O','O','O','1','O','O','O',
                 '@','1','O','O','O','O','O','O','O']
    counter = 0
    for x in range(0,9):
        print ('\n')
        for y in range(0,9):
            print(placement[counter],'',end='')
            counter = counter + 1


