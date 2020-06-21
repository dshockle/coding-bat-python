import enum
import sys

class Colors(enum.Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4

class PythonString_1(object):

        #enum Colors  red, green, blue, yellow 

        '''
        Given a string, if the string begins with "red" or "blue" return that color string, 
        otherwise return the empty string. 

        seeColor("redxx") -> "red"
        seeColor("xxred") -> ""
        seeColor("blueTimes") -> "blue"
        '''
        def seeColor(str):
            for color in Colors:
                if (str.strip().lower().startswith(color.name)):
                    return color.name
            return ""


        '''
        Given a string, return True if the first 2 chars in the string also appear at 
        the end of the string, such as with "edited". 

        frontAgain("edited") -> True
        frontAgain("edit") -> False
        frontAgain("ed") -> True
        '''
        def frontAgain(str):
            return len(str) >= 2 and str[:2] == str[-2:]
        

        '''
        Given two strings, append them together and return the result. 
        However, if the strings are different lengths, omit chars 
        from the longer string so it is the same length as the 
        shorter string. So "Hello" and "Hi" yield "loHi". 
        The strings may be any length including empty. 

        minCat("Hello", "Hi") -> "loHi"
        minCat("Hello", "java") -> "ellojava"
        minCat("java", "Hello") -> "javaello"        
        '''
        def minCat(a, string b):
            if len(a) > len(b):
                return a[len(a) - len(b)] + b
            else if (len(a) < len(b)):
                return a + b[len(b) - len(a)]
            else:
                return a + b
        

        '''
        Given a string, return a new string made of n copies of the first n chars. 
        If there are fewer than n chars, use whatever is there. 

        extraFront("Hello", 3) -> "HelHelHel"
        extraFront("ab", 2) -> "abab"
        extraFront("H", 3) -> "HHH"        
        '''
        def extraFront(str,n):
            return str[:n] * n
        

        '''

        Given a string, if a length 2 substring appears at both its beginning 
        and end, return a string without the substring at the beginning, 
        so "HelloHe" yields "lloHe". The substring may overlap with itself, 
        so "Hi" yields "". Otherwise, return the original string unchanged. 

        without2("HelloHe") -> "lloHe"
        without2("HelloHi") -> "HelloHi"
        without2("Hi") -> ""        
        '''
        def without2(str):
            if len(str) < 2:
                return str
            elif str[:2] == str[-2:]:
                return str[2:]
            else:
                return str
        

        '''
        Given a string, return a version without the first 2 chars. 
        Except keep the first char if it is 'a' and keep the second 
        char if it is 'b'. The string may be any length. Harder than it looks. 

        deFront("Hello") -> "llo"
        deFront("java") -> "va"
        deFront("away") -> "aay"        
        '''
        def deFront(str):
            sb = ""
            if (len(str) > 0 && str[0] == 'a'):
                sb += str[0]
            if (len(str) > 1 && str[1] == 'b'):
                sb += str[1]
            if (len(str) > 2):
                sb += str[:2]
            return sb
        

        '''
        Given a string and a second "word" string, we'll say that the word matches 
        the string if it appears at the front of the string, except its first char 
        does not need to match exactly. On a match, return the front of the string, 
        or otherwise return the empty string. So, so with the string "hippo" 
        the word "hi" returns "hi" and "xip" returns "hip". The word will be at 
        least length 1. 

        startWord("hippo", "hi") -> "hi"
        startWord("hippo", "xip") -> "hip"
        startWord("hippo", "z") -> "h"        
        '''
        def startWord(str, string word):
            if (str[:1], len(word) - 1).Equals(word[:1])):
                return str[:0, len(word))
            else:
                return ""
        

        '''
        Given a string, if the first or last chars are 'x', return the string 
        without those 'x' chars, and otherwise return the string unchanged. 

        withoutX("xHix") -> "Hi"
        withoutX("xHi") -> "Hi"
        withoutX("Hxix") -> "Hxi"        
        '''
        def withoutX(str):
        
            sb = ""

            if (len(str) > 0 && str[0] != 'x'):
                sb +=(str[0])

            if (len(str) > 2):
                sb +=(str[:1, len(str) - 2))

            if (len(str) > 1 && str[len(str) - 1] != 'x'):
                sb +=(str[len(str) - 1])

            return sb
        

        '''
        Given a string, if one or both of the first 2 chars is 'x', return 
        the string without those 'x' chars, and otherwise return the string 
        unchanged. This is a little harder than it looks. 

        withoutX2("xHi") -> "Hi"
        withoutX2("Hxi") -> "Hi"
        withoutX2("Hi") -> "Hi"        
        '''
        def withoutX2(str):
            sb = ""

            if (len(str) > 0 && str[0] != 'x'):
                sb +=(str[0])

            if (len(str) > 1 && str[1] != 'x'):
                sb +=(str[1])

            if (len(str) > 2):
                sb +=(str[:2))

            return sb
        


            print("seeColor")
            print(seeColor("redxx") == "red")
            print(seeColor("xxred") == "")
            print(seeColor("blueTimes") == "blue")
    
            print("frontAgain")
            print(frontAgain("edited") == True)
            print(frontAgain("edit") == False)
            print(frontAgain("ed") == True)

            print("minCat")
            print(minCat("Hello", "Hi") == "loHi")
            print(minCat("Hello", "java") == "ellojava")
            print(minCat("java", "Hello") == "javaello")

            print("extraFront")
            print(extraFront("Hello", 3) == "HelHelHel")
            print(extraFront("ab", 2) == "abab")
            print(extraFront("H", 3) == "HHH")

            print("without2")
            print(without2("HelloHe") == "lloHe")
            print(without2("HelloHi") == "HelloHi")
            print(without2("") == "")
            print(without2(null) == "")
            print(without2("H") == "H")
            print(without2("Hi") == "")

            print("deFront")
            print(deFront("Hello") == "llo")
            print(deFront("java") == "va")
            print(deFront("away") == "aay")

            print("startWord")
            print(startWord("hippo", "hi") == "hi")
            print(startWord("hippo", "xip") == "hip")
            print(startWord("hippo", "z") == "h")

            print("withoutX")
            print(withoutX("xHix") == "Hi")
            print(withoutX("xHi") == "Hi")
            print(withoutX("Hxix") == "Hxi")

            print("withoutX2")
            print(withoutX2("xHi") == "Hi")
            print(withoutX2("Hxi") == "Hi")
            print(withoutX2("Hi") == "Hi")

