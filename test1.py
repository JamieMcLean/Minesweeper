import random

def playGame():

    Field = []
    LA = ["X","X","X","X","X","X","X"]
    LB = ["X","X","X","X","X","X","X"]
    LC = ["X","X","X","X","X","X","X"]
    LD = ["X","X","X","X","X","X","X"]
    LE = ["X","X","X","X","X","X","X"]
    LF = ["X","X","X","X","X","X","X"]
    LG = ["X","X","X","X","X","X","X"]

    Field.append(LA)
    Field.append(LB)
    Field.append(LC)
    Field.append(LD)
    Field.append(LE)
    Field.append(LF)
    Field.append(LG)



    print("Select row starting from top = 1 and column from left = 0")
    numa = random.randint(1,7)
    numb = random.randint(0,6)
    MINE = "O"

    row=9
    column = 9
    one = "1"
    blank = "-"

    while row != numa and column != numb:
        for i in Field:
            print(i, end="\n")
        print('')           

        print("Enter a row")
        row = int(input('Please select a row from rows 1 - 7: '))
        column = int(input('Please enter a column from columns 1 - 7: '))
        columA = int(column) + 1
        columB = int(column) - 1
        rowA = row + 1
        rowB = row - 1
        if rowA == numa and column  == numb:
            if row == 1:
                del LA[column]
                LA.insert(column, one)
            if row == 2:
                del LB[column]
                LB.insert(column, one)     
            if row == 3:
                del LC[column]
                LC.insert(column, one)   
            if row == 4:
                del LD[column]
                LD.insert(column, one) 
            if row == 5:
                del LE[column]
                LE.insert(column, one)         
            if row == 6:
                del LF[column]
                LF.insert(column, one)  
            if row == 7:
                del LG[column]
                LG.insert(column, one)
        elif rowB == numa and column  == numb:
            if row == 1:
                del LA[column]
                LA.insert(column, one)
            if row == 2:
                del LB[column]
                LB.insert(column, one)     
            if row == 3:
                del LC[column]
                LC.insert(column, one)   
            if row == 4:
                del LD[column]
                LD.insert(column, one) 
            if row == 5:
                del LE[column]
                LE.insert(column, one)         
            if row == 6:
                del LF[column]
                LF.insert(column, one)  
            if row == 7:
                del LG[column]
                LG.insert(column, one)       
        elif row == numa and columA  == numb: 
            if row == 1:
                del LA[column]
                LA.insert(column, one)
            if row == 2:
                del LB[column]
                LB.insert(column, one)     
            if row == 3:
                del LC[column]
                LC.insert(column, one)   
            if row == 4:
                del LD[column]
                LD.insert(column, one) 
            if row == 5:
                del LE[column]
                LE.insert(column, one)         
            if row == 6:
                del LF[column]
                LF.insert(column, one)  
            if row == 7:
                del LG[column]
                LG.insert(column, one)
        elif row  == numa and columB == numb:
            if row == 1:
                del LA[column]
                LA.insert(column, one)
            if row == 2:
                del LB[column]
                LB.insert(column, one)     
            if row == 3:
                del LC[column]
                LC.insert(column, one)   
            if row == 4:
                del LD[column]
                LD.insert(column, one) 
            if row == 5:
                del LE[column]
                LE.insert(column, one)         
            if row == 6:
                del LF[column]
                LF.insert(column, one)  
            if row == 7:
                del LG[column]
                LG.insert(column, one)        
        else:
            if row == 1:
                del LA[column]
                LA.insert(column, blank)
            if row == 2:
                del LB[column]
                LB.insert(column, blank)     
            if row == 3:
                del LC[column]
                LC.insert(column, blank)   
            if row == 4:
                del LD[column]
                LD.insert(column, blank) 
            if row == 5:
                del LE[column]
                LE.insert(column, blank)         
            if row == 6:
                del LF[column]
                LF.insert(column, blank)  
            if row == 7:
                del LG[column]
                LG.insert(column, blank) 



    if row == 1:
        del LA[column]
        LA.insert(column, MINE)
    if row == 2:
        del LB[column]
        LB.insert(column, MINE)     
    if row == 3:
        del LC[column]
        LC.insert(column, MINE)   
    if row == 4:
        del LD[column]
        LD.insert(column, MINE) 
    if row == 5:
        del LE[column]
        LE.insert(column, MINE)         
    if row == 6:
        del LF[column]
        LF.insert(column, MINE)  
    if row == 7:
        del LG[column]
        LG.insert(column, MINE)

    for i in Field:
        print(i, end="\n")
    print('') 

    print("Game over")

playGame()
