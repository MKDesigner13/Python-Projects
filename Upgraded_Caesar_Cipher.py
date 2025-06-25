#Upgraded Caesar Cipher

"""
Description:
This code takes in a phrase and returns an encrypted version.
Each letter in the code is moved ahead in the alphabet by the user-given encryption value.
If a letter goes beyon 'z', it will contiune cycling from 'a'.
The case of each letter is maintained.

#Sample usage
input:
The die is cast
2

output:
Sgd chd hr bzrs
"""



def setValues():
    
    inputStr = input('Enter phrase to be encrypted: ')
    while True:
        try:
            shiftValue = int(input('Enter an integer between 1 and 25 inclusive as an ecryption value: '))
            if 1 <= shiftValue <= 25:
                break
            else:
                print('That integer is out of range\n')
        except ValueError:
            print('That was not a valid integer\n')

    return inputStr, shiftValue

def changeUpper(char, shiftValue):
    code = ord(char) + shiftValue
    while code > 90:
        code -= 26
    return chr(code)

def changeLower(char, shiftValue):
    code = ord(char) + shiftValue
    while code > 122:
        code -= 26
    return chr(code)


def main():

    #Set values
    inputStr, shiftValue = setValues()

    print(inputStr, shiftValue)

    #Encode values
    inputList = list(inputStr)
    for i in range(len(inputList)):
        if not inputList[i].isalpha():
            continue
        if inputList[i].isupper():
            inputList[i] = changeUpper(inputList[i], shiftValue)
        elif inputList[i].islower():
            inputList[i] = changeLower(inputList[i], shiftValue)

    print (''.join(inputList))



main()
