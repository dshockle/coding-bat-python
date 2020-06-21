import re
import sys

class PythonWarmup_2(object):

        '''
        Given a string and a non-negative int n, return a larger string 
        that is n copies of the original string. 
        stringTimes("Hi", 2) -> "HiHi"
        stringTimes("Hi", 3) -> "HiHiHi"
        stringTimes("Hi", 1) -> "Hi"
        '''
        def stringTimes(str, n):
            return str * n
        

        '''
        Given a string and a non-negative int n, 
        we'll say that the front of the string is the first 3 chars, 
        or whatever is there if the string is less than length 3. 
        Return n copies of the front; 

        frontTimes("Chocolate", 2) -> "ChoCho"
        frontTimes("Chocolate", 3) -> "ChoChoCho"
        frontTimes("Abc", 3) -> "AbcAbcAbc"
        '''
        def frontTimes(str, n):
            return str[:3] * n

        '''
        Count the number of "xx" in the given string. 
        We'll say that overlapping is allowed, so "xxx" contains 2. 
        countXX("abcxx") -> 1
        countXX("xxx") -> 2
        countXX("xxxx") -> 3
        '''
        def countXX(str):
            count = 0
            for i in range (0, len(str)-1):
                if str[i:i+2] == "xx":
                    count += 1
            return count
        

        '''
        Given a string, return True if the first instance of "x" in the string 
        is immediately followed by another "x". 
        doubleX("axXbb") -> True
        doubleX("axaxx") -> False
        doubleX("Xxabc") -> True
        '''
        def doubleX(str):
            lowstr = str.lower()
            posXX = lowstr.find("xx")
            posX = lowstr.find("x")
            return posXX != -1 and posXX == posX
        

        '''
        Given a string, return a new string made of every other char starting 
        with the first, so "Hello" yields "Hlo". 

        stringBits("Hello") -> "Hlo"
        stringBits("Hi") -> "H"
        stringBits("Heeololeo") -> "Hello"
        '''

        def stringBits(str):
            return str[::2]
        

        '''
        Given a non-empty string like "Code" return a string like "CCoCodCode". 

        stringSplosion("Code") -> "CCoCodCode"
        stringSplosion("abc") -> "aababc"
        stringSplosion("ab") -> "aab"
        '''
        def stringSplosion(str):
            result = ""
            for i in range(0, len(str)+1):
                result += str[:i]
            return result
        
        '''
        Given a string, return a version where all the "x" have been removed. 
        Except an "x" at the very start or end should not be removed. 

        stringX("xxHxix") -> "xHix"
        stringX("abxxxcd") -> "abcd"
        stringX("xabxxxcdx") -> "xabcdx"
        '''
        def stringX(str):
            middle = re.sub('x', '', str[1:-1])
            return str[0] + middle + str[-1]
        

        '''
        Given a string, return a string made of the chars at 
        indexes 0,1, 4,5, 8,9 ... so "kittens" yields "kien". 

        altPairs("kitten") -> "kien"
        altPairs("Chocolate") -> "Chole"
        altPairs("CodingHorror") -> "Congrr
        '''
        def altPairs(str):
            result = ''
            for i in range(0, len(str), 4):
                result += str[i:i+2]
            return result

        '''
        Suppose the string "yak" is unlucky. 
        Given a string, return a version where all the "yak" are removed, 
        but the "a" can be any char. The "yak" strings will not overlap. 

        stringYak("yakpak") -> "pak"
        stringYak("pakyak") -> "pak"
        stringYak("yak123ya") -> "123ya"
        '''
        def stringYak(str):
            return re.sub('y.k', '', str)
        

        '''
        Given an array of ints, we'll say that a triple is a value appearing 3 times 
        in a row in the array. Return True if the array does not contain any triples. 

        noTriples(1, 1, 2, 2, 1) -> True
        noTriples(1, 1, 2, 2, 2, 1) -> False
        noTriples(1, 1, 1, 2, 2, 2, 1) -> False
        '''
        def noTriples(nums):
            result = True
            last = len(nums) - 1
            for i in range (2, last):
                if (nums[i] == nums[i - 1] and nums[i] == nums[i - 2]):
                    result = False
                    break
            return result
        


        print("stringTimes")
        print(stringTimes("Hi", 2) == "HiHi")
        print(stringTimes("Hi", 3) == "HiHiHi")
        print(stringTimes("Hi", 1) == "Hi")

        print("frontTimes")
        print(frontTimes("Chocolate", 2) == "ChoCho")
        print(frontTimes("Chocolate", 3) == "ChoChoCho")
        print(frontTimes("Abc", 3) == "AbcAbcAbc")

        print("countXX")
        print(countXX("abcxx") == 1)
        print(countXX("xxx") == 2)
        print(countXX("xxxx") == 3)

        print("doubleX")
        print(doubleX("axXbb") == True)
        print(doubleX("axaxx") == False)
        print(doubleX("Xxabx") == True)

        print("stringBits")
        print(stringBits("Hello") == "Hlo")
        print(stringBits("Hi") == "H")
        print(stringBits("Heeololeo") == "Hello")

        print("stringSplosion")
        print(stringSplosion("Code") == "CCoCodCode")
        print(stringSplosion("abc") == "aababc")
        print(stringSplosion("ab") == "aab")

        print("stringX")
        print(stringX("xxHxix") == "xHix")
        print(stringX("abxxxcd") == "abcd")
        print(stringX("xabxxxcdx") == "xabcdx")

        print("altPairs")
        print(altPairs("kitten") == "kien")
        print(altPairs("Chocolate") == "Chole")
        print(altPairs("CodingHorror") == "Congrr")

        print("stringYak")
        print(stringYak("yakpak") == "pak")
        print(stringYak("pakyak") == "pak")
        print(stringYak("yak123ya") == "123ya")

        print("noTriples")
        print(noTriples([ 1, 1, 2, 2, 1]) == True)
        print(noTriples([ 1, 1, 2, 2, 2, 1]) == False)
        print(noTriples([ 1, 1, 1, 2, 2, 2, 1]) == False)

