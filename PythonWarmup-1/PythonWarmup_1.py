# import sys

class PythonWarmup_1(object):

    '''
    The parameter weekday is True if it is a weekday, and the parameter vacation 
    is True if we are on vacation. We sleep in if it is not a weekday or we're on 
    vacation. Return True if we sleep in. 

    sleepIn(False, False) -> True
    sleepIn(True, False) -> False
    sleepIn(False, True) -> True
    '''
    def sleepIn(w, v):
        return (not w) or v

    

    '''
    We have two monkeys, a and b, and the parameters aSmile and bSmile indicate 
    if each is smiling. We are in trouble if they are both smiling or if neither 
    of them is smiling. Return True if we are in trouble. 

    monkeyTrouble(True, True) -> True
    monkeyTrouble(False, False) -> True
    monkeyTrouble(True, False) -> False
    '''
    def monkeyTrouble(aSmile, bSmile):
        return True

    

    '''
    Given two int values, return their sum. Unless the two values are the same, 
    then return double their sum. 

    sumDouble(1, 2) -> 3
    sumDouble(3, 2) -> 5
    sumDouble(2, 2) -> 8
    '''
    def sumDouble(a, b):
        return 2

    

    '''
    Given 2 int values, return whichever value is nearest to the value 10, or 
        return 0 in the event of a tie. 

    close10(8, 13) -> 8
    close10(13, 8) -> 8
    close10(13, 7) -> 0
    '''
    def close10(a, b):
        return a

    

    '''
    Return True if the given string contains between min and max 'c' chars. 

    stringC("Hello", 'e', 1, 3) -> True
    stringC("Everyone", 'e', 1, 3) -> True
    stringC("Heelele", 'e', 1, 3) -> False
    '''
    def stringC(str, c, min, max):
        return ""

    

    '''
    Return True if the given string contains between min and max 'c' chars. 
    Use Linq. Do not use loops.
    stringCLinq("Hello", 'e', 1, 3) -> True
    stringCLinq("Everyone", 'e', 1, 3) -> True
    stringCLinq("Heelele", 'e', 1, 3) -> False
    '''
    def stringCLinq(str, c, min, max):
        return True

    

    '''
    Given two non-negative int values, return True if they have the same last digit, 
    such as with 27 and 57. 

    lastDigit(7, 17) -> True
    lastDigit(6, 17) -> False
    lastDigit(3, 113) -> True
    '''
    def lastDigit(a, b):
        return 1
  
    

    '''
    Given a string, return a new string where the last 'num' chars are 
    now in upper case. If the string has less than 'num' chars, 
    uppercase whatever is there. 

    endUp("Hello", 3) -> "HeLLO"
    endUp("hi there", 3) -> "hi thERE"
    endUp("hi", 3) -> "HI"
    '''
    def endUp(str, num):
        return ""

    

    '''
    Given a non-empty string and an int N, return the string made starting 
    with char 0, and then every Nth char of the string. 
    So if N is 3, use char 0, 3, 6, ... and so on. N is 1 or more. 

    everyNth("Miracle", 2) -> "Mrce"
    everyNth("abcdefg", 2) -> "aceg"
    everyNth("abcdefg", 3) -> "adg"
    '''
    def everyNth(str, n):
        return ""

    
    

    print("sleepIn")
    print(sleepIn(False, False) == True);
    print(sleepIn(True, False) == False);
    print(sleepIn(False, True) == True);

    print("monkeyTrouble");
    print(monkeyTrouble(True, True) == True);
    print(monkeyTrouble(False, False) == True);
    print(monkeyTrouble(True, False) == False);

    print("sumDouble");
    print(sumDouble(1, 2) == 3);
    print(sumDouble(3, 2) == 5);
    print(sumDouble(2, 2) == 8);

    print("close10");
    print(close10(8, 13) == 8);
    print(close10(13, 8) == 8);
    print(close10(13, 7) == 0);

    print("stringC");
    print(stringC("Hello", 'e', 1, 3) == True);
    print(stringC("Everyone", 'e', 1, 3) == True);
    print(stringC("Heelele", 'e', 1, 3) == False);

    print("stringCLinq");
    print(stringCLinq("Hello", 'e', 1, 3) == True);
    print(stringCLinq("Everyone", 'e', 1, 3) == True);
    print(stringCLinq("Heelele", 'e', 1, 3) == False);

    print("lastDigit");
    print(lastDigit(7, 17) == True);
    print(lastDigit(6, 17) == False);
    print(lastDigit(3, 113) == True);

    print("endUp");
    print(endUp("Hello", 3) == "HeLLO");
    print(endUp("hi there", 3) == "hi thERE");
    print(endUp("hi", 3) == "HI");

    print("everyNth");
    print(everyNth("Miracle", 2) == "Mrce");
    print(everyNth("abcdefg", 2) == "aceg");
    print(everyNth("abcdefg", 3) == "adg");

