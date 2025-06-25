"""
Reads 9 rows of the Sudoku, each containing 9 digits
Outputs Yes if the Sudoku is valid, and No otherwise.
"""

def sudokuChecker(answerSet):
    #Check horizontal lines

    #Iterate over horizontal lines
    for setX in answerSet:
        #Check for duplicates in the horizontal line
        if len(set(str(setX))) != len(str(setX)):
            #Return 'No' if there is a duplicate in the horizontal line
            return 'No'
        
    #Check vertical lines

    verticalSet = []
    index = 0

    #Iterate over each vertical line
    for i in range(9):
        #Create new set from vertical line values
        for setX in answerSet:
            verticalSet.append(list(str(setX))[index])

        #Check for duplicates in the vertical line
        if len(set(verticalSet)) != len(verticalSet):
            #Return 'No' if there is a duplicate in the vertical line
            return 'No'
        
        #Increase index and reset the vertical line set
        index += 1
        verticalSet = []

    #Check 3x3 squares

    #Create 3x3 blocks

    blockSet = []
    indexStart = 0
    indexEnd = 3
    answerIndexS = 0
    answerIndexE = 3

    #Iterate over each 3x3 block
    for i in range(9):
        #Create new set from 3x3 block values
        for setX in answerSet[answerIndexS:answerIndexE]:
            for i in list(str(setX))[indexStart:indexEnd]:
                blockSet.append(i)

        #Check for duplicates in the 3x3 block
        if len(set(blockSet)) != len(blockSet):
            #Return 'No' if there is a duplicate in the block
            return 'No'
        
        #Increase index and reset the block set
        indexStart += 3
        indexEnd += 3
        blockSet = []

        #Increase indexes to move onto the next row of 3x3 blocks
        if indexStart > 6:
            indexStart = 0
            indexEnd = 3  
            answerIndexS += 3
            answerIndexE += 3  

    #Return 'Yes' if all checks are passed    
    return 'Yes'




answerSet = [295743861,
431865927,
876192543,
387459216,
612387495,
549216738,
763524189,
928671354,
154938672]

print(sudokuChecker(answerSet))


"""
Example values: 

[295743861,
431865927,
876192543,
387459216,
612387495,
549216738,
763524189,
928671354,
154938672]
Answer -> Yes

[195743862,
431865927,
876192543,
387459216,
612387495,
549216738,
763524189,
928671354,
254938671]
Answer -> No
"""