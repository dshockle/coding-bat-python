import enum
import sys

class PythonString_1(object):

        '''
        Given a string, if the string begins with "red", "blue", "green" or "yellow" 
        return that color string, otherwise return the empty string. 

        seeColor("redxx") -> "red"
        seeColor("xxred") -> ""
        seeColor("blueTimes") -> "blue"
        '''
        def seeColor(sc):
            scColors = ["red", "green", "blue", "yellow"]
            lowStr = sc.strip().lower()
            for color in scColors:
                if lowStr.startswith(color):
                    return color
            return ""


        '''
        Given a string, return True if the first 2 chars in the string also appear at 
        the end of the string, such as with "edited". 

        frontAgain("edited") -> True
        frontAgain("edit") -> False
        frontAgain("ed") -> True
        '''
        def frontAgain(fa):
            return len(fa) >= 2 and fa[:2] == fa[-2:]
        

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
        def minCat(mcA, mcB):
            mlen = min(len(mcA), len(mcB))
            if len(mcA) > len(mcB):
                return mcA[-mlen:] + mcB
            elif len(mcA) < len(mcB):
                return mcA + mcB[-mlen:]
            else:
                return mcA + mcB
        

        '''
        Given a string, return a new string made of n copies of the first n chars. 
        If there are fewer than n chars, use whatever is there. 

        extraFront("Hello", 3) -> "HelHelHel"
        extraFront("ab", 2) -> "abab"
        extraFront("H", 3) -> "HHH"        
        '''
        def extraFront(ef, efn):
            return ef[:efn] * efn
        

        '''

        Given a string, if a length 2 substring appears at both its beginning 
        and end, return a string without the substring at the beginning, 
        so "HelloHe" yields "lloHe". The substring may overlap with itself, 
        so "Hi" yields "". Otherwise, return the original string unchanged. 

        without2("HelloHe") -> "lloHe"
        without2("HelloHi") -> "HelloHi"
        without2("Hi") -> ""        
        '''
        def without2(wo2):
            if len(wo2) < 2:
                return str
            elif wo2[:2] == wo2[2:]:
                return wo2[2:]
            else:
                return wo2
        

        '''
        Given a string, return a version without the first 2 chars. 
        Except keep the first char if it is 'a' and keep the second 
        char if it is 'b'. The string may be any length. Harder than it looks. 

        deFront("Hello") -> "llo"
        deFront("java") -> "va"
        deFront("away") -> "aay"        
        '''
        def deFront(df):
            sb = ""
            if len(df) > 0 and df[0] == 'a':
                sb += str[0]
            if len(df) > 1 and df[1] == 'b':
                sb += df[1]
            if len(df) > 2:
                sb += df[:2]
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
        def startWord(sw1, sw2):
            mlen = min(len(sw1), len(sw2))
            if str[1:mlen] == word[1:mlen]:
                return str[:mlen]
            else:
                return ""


        '''
        Given a string, if the first or last chars are 'x', return the string 
        without those 'x' chars, and otherwise return the string unchanged. 

        withoutX("xHix") -> "Hi"
        withoutX("xHi") -> "Hi"
        withoutX("Hxix") -> "Hxi"        
        '''
        def withoutX(wx):
        
            wxResult = ""

            if len(wx) > 0 and wx[0] != 'x':
                wxResult +=(wx[0])

            if len(wx) > 2:
                wxResult += wx[1:len(wx)-2]

            if len(wx) > 1 and wx[len(wx)-1] != 'x':
                wxResult += wx[len(wx)-1]

            return wxResult
        

        '''
        Given a string, if one or both of the first 2 chars is 'x', return 
        the string without those 'x' chars, and otherwise return the string 
        unchanged. This is a little harder than it looks. 

        withoutX2("xHi") -> "Hi"
        withoutX2("Hxi") -> "Hi"
        withoutX2("Hi") -> "Hi"        
        '''
        def withoutX2(wx2):
            wx2Result = ""
            slen = len(wx2)
            if slen > 0 and wx2[0] != 'x':
                wx2Result += wx2[0]
            if slen > 1 and wx2[1] != 'x':
                wx2Result += wx2[1]
            if slen > 2:
                wx2Result += wx2[:2]
            return wx2Result
        


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

