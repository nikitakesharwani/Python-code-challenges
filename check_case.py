
def check_case(sentence):
    countUpper = 0
    countLower = 0
    countDigit = 0
    countSymbol = 0
    for i  in sentence:
        if i.isupper():
            countUpper +=1 
        elif i.islower():
            countLower +=1 
        elif i.isdigit():
            countDigit +=1
        else:
            countSymbol +=1

    return (countUpper , countLower , countDigit , countSymbol)

upperCount , lowerCount , digitCount , symbolCount = check_case("AAArrt4545@#$45&axD")
print(f"Upper count : {upperCount} , Lower count : {lowerCount} , Digit count : {digitCount} , Symbol count : {symbolCount}")
