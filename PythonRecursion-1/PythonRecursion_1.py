import sys

class PythonRecursion_1(object):
        '''
        Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. 
        Compute the result recursively (without loops). 

        factorial(1) -> 1
        factorial(2) -> 2
        factorial(3) -> 6
        '''
        def factorial(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return n * factorial(n-1)
        

        '''        
        We have a number of bunnies and each bunny has two big floppy ears. We want to compute the 
        total number of ears across all the bunnies recursively (without loops or multiplication). 

        bunnyEars(0) -> 0
        bunnyEars(1) -> 2
        bunnyEars(2) -> 4
        '''
        def bunnyEars(bunnies):
            if bunnies == 0:
                return 0
            elif bunnies == 1:
                return 2
            else:
                return 2 + bunnyEars(bunnies-1)

        

        '''
        The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive 
        definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). 
        Each subsequent value is the sum of the previous two values, so the whole sequence is: 
        0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns 
        the nth fibonacci number, with n=0 representing the start of the sequence. 

        fibonacci(0) -> 0
        fibonacci(1) -> 1
        fibonacci(2) -> 1
        '''
        def fibonacci(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        

        '''        
        We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the 
        normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a 
        raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without 
        loops or multiplication). 

        bunnyEars2(0) -> 0
        bunnyEars2(1) -> 2
        bunnyEars2(2) -> 5
        '''
        def bunnyEars2(bunnies):
            if bunnies == 0:
                return 0
            elif bunnies == 1:
                return 2
            else:
                return 3 - bunnies%2 + bunnyEars(bunnies-1)
        

        '''
        We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, 
        the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the 
        total number of blocks in such a triangle with the given number of rows. 

        triangle(0) -> 0
        triangle(1) -> 1
        triangle(2) -> 3
        '''
        def triangle(rows):
            if rows == 0:
                return 0
            elif rows == 1:
                return 1
            else:
                return rows + triangle(rows-1)
        

        '''        
        Given a non-negative n, return the sum of its digits recursively (no loops).

        sumDigits(126) -> 9
        sumDigits(49) -> 13
        sumDigits(12) -> 3
'''
        def sumDigits(n):
            if n == 0:
                return 0
            else:
                return n%10 + sumDigits(n/10)
        

        '''        
        Given a non-negative n, return the count of the occurrences of 7 as a digit, so for 
        example 717 yields 2. (no loops). 

        count7(717) -> 2
        count7(7) -> 1
        count7(123) -> 0
        '''
        def count7(n):
            if n == 0:
                return 0
            elif n % 10 == 7:
                return 1 + count7(n/10)
            else:
                return count7(n/10)
        

        '''        
        Given a non-negative n, compute recursively (no loops) the count of the occurrences 
        of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, 
        so 8818 yields 4. 

        count8(8) -> 1
        count8(818) -> 2
        count8(8818) -> 4
        '''
        def count8(n):
            if n == 0:
                return 0
            elif n % 10 == 8:
                if (n / 10) % 10 == 8:
                    return 2 + count8(n / 10)
                else:
                    return 1 + count8(n / 10)
            else:
                return count8(n / 10)
        


        '''
        Given baseNum and n that are both 1 or more, compute recursively (no loops) the value of 
        baseNum to the 'pow' power, so powerN(3, 2) is 9 (3 squared). 

        powerN(3, 1) -> 3
        powerN(3, 2) -> 9
        powerN(3, 3) -> 27
        '''
        def powerN(baseNum, pow):
            if pow == 0:
                return 1
            elif pow == 1:
                return baseNum
            else:
                return baseNum * powerN(baseNum, pow-1)
        


        '''
        Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string. 

        countX("xxhixx") -> 4
        countX("xhixhix") -> 3
        countX("hi") -> 0

            '''
        def countX(str):
            if len(str) == 0:
                return 0
            elif str[0] == 'x':
                return 1 + countX(str[1:])
            else:
                return countX(str[1:])
        


        '''
        Given a string, compute recursively (no loops) the number of times lowercase "hi" appears 
        in the string. 

        countHi("xxhixx") -> 1
        countHi("xhixhix") -> 2
        countHi("hi") -> 1
        '''
        def countHi(str):
            if len(str) < 2:
                return 0
            elif str[:2] == "hi":
                return 1 + countHi(str[1:])
            else:
                return countHi(str[1:])
        

        '''
        Given a string, compute recursively (no loops) a new string where all the lowercase 'x' 
        chars have been changed to 'y' chars. 

        changeXY("codex") -> "codey"
        changeXY("xxhixx") -> "yyhiyy"
        changeXY("xhixhix") -> "yhiyhiy"
        '''
        def changeXY(str):
            if len(str) == 0:
                return ""
            elif str[0] == 'x':
                return "y" + changeXY(str[1:])
            else:
                return str[0] + changeXY(str[1:])

        

        '''
        Given a string, compute recursively (no loops) a new string where all appearances of "pi" 
        have been replaced by "3.14". 

        changePi("xpix") -> "x3.14x"
        changePi("pipi") -> "3.143.14"
        changePi("pip") -> "3.14p"
        '''
        def changePi(str):
            if len(str) < 2:
                return str
            elif str.Substring(0, 2).Equals("pi"):
                return "3.14" + changePi(str[2:])
            else:
                return str[:1] + changePi(str[1:])
        

        '''        
        Given a string, compute recursively a new string where all the 'x' chars have been removed.

        noX("xaxb") -> "ab"
        noX("abc") -> "abc"
        noX("xx") -> ""
        '''
        def noX(str):
            if len(str) < 1:
                return str
            elif str[0] == 'x':
                return noX(str[1:])
            else:
                return str[0] + noX(str[1:])
        

        '''
        Given an array of ints, compute recursively if the array contains a 6. We'll use the 
        convention of considering only the part of the array that begins at the given index. 
        In this way, a recursive call can pass index+1 to move down the array. The initial 
        call will pass in index as 0. 

        array6(1, 6, 4, 0) -> True
        array6(1, 4, 0) -> False
        array6(6, 0) -> True
        '''
        def array6(nums, index):
            if len(nums) == 0:
                return False
            elif len(nums) <= index:
                return False
            elif nums[index] == 6:
                return True
            else:
                return array6(nums, index+1)
        

        '''
        Given an array of ints, compute recursively the number of times that the value 11 appears 
        in the array. We'll use the convention of considering only the part of the array that begins 
        at the given index. In this way, a recursive call can pass index+1 to move down the array. 
        The initial call will pass in index as 0. 

        array11(1, 2, 11, 0) -> 1
        array11(11, 11, 0) -> 2
        array11(1, 2, 3, 4, 0) -> 0
        '''
        def array11(nums, index):
            if len(nums) == 0 or len(nums) <= index:
                return 0
            elif nums[index] == 11:
                return 1 + array11(nums, index + 1)
            else:
                return array11(nums, index + 1)
        

        '''
        Given an array of ints, compute recursively if the array contains somewhere a value followed 
        immediately by that value times 10. We'll use the convention of considering only the part of 
        the array that begins at the given index. In this way, a recursive call can pass index+1 to 
        move down the array. The initial call will pass in index as 0. 

        array220(1, 2, 20, 0) -> True
        array220(3, 30, 0) -> True
        array220(3, 0) -> False
        '''
        def array220(nums, index):
            if len(nums) < 2:
                return False
            elif nums[index] * 10 == nums[index + 1]:
                return True
            else:
                return array220(nums, index + 1)
        

        '''
        Given a string, compute recursively a new string where all the adjacent chars are now separated 
        by a "*". 

        allStar("hello") -> "h*e*l*l*o"
        allStar("abc") -> "a*b*c"
        allStar("ab") -> "a*b"
        '''

        def allStar(str):
            if string.IsNullOrEmpty(str) or len(str) == 1:
                return str
            else:
                return str[0] + "*" + allStar(str[1:])
        

        '''
        Given a string, compute recursively a new string where identical chars that are adjacent in 
        the original string are separated from each other by a "*". 

        pairStar("hello") -> "hel*lo"
        pairStar("xxyy") -> "x*xy*y"
        pairStar("aaaa") -> "a*a*a*a"
        '''
        def pairStar(str):
            if string.IsNullOrEmpty(str) or len(str) == 1:
                return str
            elif str[0] == str[1]:
                return str[0] + "*" + pairStar(str[1:])
            else:
                return str[0] + pairStar(str[1:])

        

        '''
        Given a string, compute recursively a new string where all the lowercase 'x' chars have been 
        moved to the end of the string. 

        endX("xxre") -> "rexx"
        endX("xxhixx") -> "hixxxx"
        endX("xhixhix") -> "hihixxx"
        '''
        def endX(str):
            if string.IsNullOrEmpty(str):
                return str
            elif str[0] == 'x':
                return endX(str[1:]) + 'x'
            else:
                return str[0] + endX(str[1:])
        

        '''
        We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" 
        the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. 
        Recursively compute the number of pairs in the given string. 

        countPairs("axa") -> 1
        countPairs("axax") -> 2
        countPairs("axbx") -> 1
        '''
        def countPairs(str):
            if string.IsNullOrEmpty(str) or len(str) < 3:
                return 0
            elif str[0] == str[2]:
                return 1 + countPairs(str[1:])
            else:
                return countPairs(str[1:])
        


        '''        
        Count recursively the total number of "abc" and "aba" substrings that appear in the given string. 

        countAbc("abc") -> 1
        countAbc("abcxxabc") -> 2
        countAbc("abaxxaba") -> 2
        '''
        def countAbc(str):
            if string.IsNullOrEmpty(str) or len(str) < 3:
                return 0
            elif str.Substring(0,3).Equals("abc") or str.Substring(0,3).Equals("aba"):
                return 1 + countAbc(str[1:])
            else:
                return countAbc(str[1:])
        

        '''
        Given a string, compute recursively (no loops) the number of "11" substrings in the string. 
        The "11" substrings should not overlap. 

        count11("11abc11") -> 2
        count11("abc11x11x11") -> 3
        count11("111") -> 1
        '''
        def count11(str):
            if string.IsNullOrEmpty(str) or len(str) < 2):
                return 0
            elif str.Substring(0, 2) == "11":
                return 1 + count11(str[2:])
            else
                return count11(str[1:])
        

        '''
        Given a string, return recursively a "cleaned" string where adjacent chars that are the same 
        have been reduced to a single char. So "yyzzza" yields "yza". 

        stringClean("yyzzza") -> "yza"
        stringClean("abbbcdd") -> "abcd"
        stringClean("Hello") -> "Helo"
        '''
        def stringClean(str):
            if string.IsNullOrEmpty(str) or len(str) < 2):
                return str
            elif str[0] == str[1]:
                return stringClean(str[1:])
            else:
                return str[0] + stringClean(str[1:])
        

        '''
        Given a string, compute recursively the number of times lowercase "hi" appears in the string, 
        however do not count "hi" that have an 'x' immedately before them. 

        countHi2("ahixhi") -> 1
        countHi2("ahibhi") -> 2
        countHi2("xhixhi") -> 0
        '''
        def countHi2(str):
            if string.IsNullOrEmpty(str) or len(str) < 2):
                return 0
            elif len(str) == 2:
                if str == "hi":
                    return 1
                else:
                    return 0
            elif str[0] == 'x':
                return countHi2(str[2:])
            elif str.Substring(0,2).Equals("hi"):
                return 1 + countHi2(str[2:])
            else:
                return countHi2(str[1:])
        

        '''
        Given a string that contains a single pair of parenthesis, compute recursively a new string 
        made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)". 

        parenBit("xyz(abc)123") -> "(abc)"
        parenBit("x(hello)") -> "(hello)"
        parenBit("(xy)1") -> "(xy)"
        '''
        def parenBit(str):
            if string.IsNullOrEmpty(str) or len(str) < 2:
                return ""
            elif str[0] == '(' and str[len(str) - 1] == ')'):
                return str
            elif str[0] == '(':
                return parenBit(str.Substring(0, len(str) - 1):
            elif str[len(str) - 1] == ')':
                return parenBit(str[1:])
            else:
                return parenBit(str.Substring(1, len(str) - 1))
        

        '''
        Given a string, return True if it is a nesting of zero or more pairs of parenthesis, 
        like "(())" or "((()))". Suggestion: check the first and last chars, and then recur 
        on what's inside them.

        nestParen("(())") -> True
        nestParen("((()))") -> True
        nestParen("(((x))") -> False
        nestParen("((())") -> False
        nestParen("((()()") -> False
        nestParen("()") -> True
        nestParen("") -> True
        nestParen("(yy)") -> False
        nestParen("(())") -> True
        nestParen("(((y))") -> False
        nestParen("((y)))") -> False
        nestParen("((()))") -> True
        nestParen("(())))") -> False
        nestParen("((yy())))") -> False
        nestParen("(((())))") -> True
        '''
        def nestParen(str):
            if string.IsNullOrEmpty(str):
                return True
            elif len(str) == 1):
                return False
            else:
                start = str[0]
                end = str[len(str) - 1]

                if start != '(' or end != ')':
                    return False
                else:
                    return nestParen(str.Substring(1, len(str) - 2))
            
        

        '''        
        Given a string and a non-empty substring sub, compute recursively the number of times that 
        sub appears in the string, without the sub strings overlapping. 

        strCount("catcowcat", "cat") -> 2
        strCount("catcowcat", "cow") -> 1
        strCount("catcowcat", "dog") -> 0
        '''
        def strCount(str, sub):
            if string.IsNullOrEmpty(str) or string.IsNullOrEmpty(sub):
                return 0
            elif len(str) < len(sub)):
                return 0
            elif str.Substring(0, len(sub)).Equals(sub)):
                return 1 + strCount(str.Substring(len(sub)), sub)
            else:
                return strCount(str[1:], sub)
        


        '''
        Given a string and a non-empty substring sub, compute recursively if at least n copies of 
        sub appear in the string somewhere, possibly with overlapping. N will be non-negative. 

        strCopies("catcowcat", "cat", 2) -> True
        strCopies("catcowcat", "cow", 2) -> False
        strCopies("catcowcat", "cow", 1) -> True
        '''
        def strCopies(str, sub, n):
            if n == 0:
                return True
            elif string.IsNullOrEmpty(str) or string.IsNullOrEmpty(sub):
                return False
            elif len(str) < len(sub):
                return False
            elif str.Substring(0, len(sub)).Equals(sub):
                return strCopies(str.Substring(len(sub)), sub, n - 1)
            else:
                return strCopies(str[1:], sub, n)
        

        '''      
        Given a string and a non-empty substring sub, compute recursively the largest substring 
        which starts and ends with sub and return its length. 

        strDist("catcowcat", "cat") -> 9
        strDist("catcowcat", "cow") -> 3
        strDist("cccatcowcatxx", "cat") -> 9
        '''
        def strDist(str, sub):
            if string.IsNullOrEmpty(str) or string.IsNullOrEmpty(sub):
                return 0
            elif len(str) < len(sub):
                return 0
            elif str.Substring(0, len(sub)).Equals(sub) and str.Substring(len(str) - len(sub)).Equals(sub):
                return len(str)
            elif str.Substring(0, len(sub)).Equals(sub):
                return strDist(str.Substring(0, len(str) - 1), sub)
            elif str.Substring(len(str) - len(sub)).Equals(sub):
                return strDist(str[1:], sub)
            else 
                return strDist(str.Substring(1, len(str) - 1), sub)
        


            print("factorial")
            print(factorial(1) == 1)
            print(factorial(2) == 2)
            print(factorial(3) == 6)

            print("bunnyEars")
            print(bunnyEars(0) == 0)
            print(bunnyEars(1) == 2)
            print(bunnyEars(2) == 4)

            print("fibonacci")
            print(fibonacci(0) == 0)
            print(fibonacci(1) == 1)
            print(fibonacci(2) == 1)

            print("bunnyEars2")
            print(bunnyEars2(0) == 0)
            print(bunnyEars2(1) == 2)
            print(bunnyEars2(2) == 5)

            print("triangle")
            print(triangle(0) == 0)
            print(triangle(1) == 1)
            print(triangle(2) == 3)

            print("sumDigits")
            print(sumDigits(126) == 9)
            print(sumDigits(49) == 13)
            print(sumDigits(12) == 3)

            print("count7")
            print(count7(717) == 2)
            print(count7(7) == 1)
            print(count7(123) == 0)

            print("count8")
            print(count8(8) == 1)
            print(count8(818) == 2)
            print(count8(8818) == 4)

            print("powerN")
            print(powerN(3, 1) == 3)
            print(powerN(3, 2) == 9)
            print(powerN(3, 3) == 27)

            print("countX")
            print(countX("xxhixx") == 4)
            print(countX("xhixhix") == 3)
            print(countX("hi") == 0)

            print("countHi")
            print(countHi("xxhixx") == 1)
            print(countHi("xhixhix") == 2)
            print(countHi("hi") == 1)

            print("changeXY")
            print(changeXY("codex") == "codey")
            print(changeXY("xxhixx") == "yyhiyy")
            print(changeXY("xhixhix") == "yhiyhiy")

            print("changePi")
            print(changePi("xpix") == "x3.14x")
            print(changePi("pipi") == "3.143.14")
            print(changePi("pip") == "3.14p")

            print("noX")
            print(noX("xaxb") == "ab")
            print(noX("abc") == "abc")
            print(noX("xx") == "")

            print("array6")
            print(array6(new int[]  1, 6, 4, 0) == True)
            print(array6(new int[]  1, 4, 0) == False)
            print(array6(new int[]  6 , 0) == True)

            print("array11")
            print(array11(new int[]  1, 2, 11, 0) == 1)
            print(array11(new int[]  11, 11, 0) == 2)
            print(array11(new int[]  1, 2, 3, 4, 0) == 0)

            print("array220")
            print(array220(new int[]  1, 2, 20, 0) == True)
            print(array220(new int[]  3, 30, 0) == True)
            print(array220(new int[]  3 , 0) == False)

            print("allStar")
            print(allStar("hello") == "h*e*l*l*o")
            print(allStar("abc") == "a*b*c")
            print(allStar("ab") == "a*b")

            print("pairStar")
            print(pairStar("hello") == "hel*lo")
            print(pairStar("xxyy") == "x*xy*y")
            print(pairStar("aaaa") == "a*a*a*a")

            print("endX")
            print(endX("xxre") == "rexx")
            print(endX("xxhixx") == "hixxxx")
            print(endX("xhixhix") == "hihixxx")

            print("countPairs")
            print(countPairs("axa") == 1)
            print(countPairs("axax") == 2)
            print(countPairs("axbx") == 1)

            print("countAbc")
            print(countAbc("abc") == 1)
            print(countAbc("abcxxabc") == 2)
            print(countAbc("abaxxaba") == 2)

            print("count11")
            print(count11("11abc11") == 2)
            print(count11("abc11x11x11") == 3)
            print(count11("111") == 1)

            print("stringClean")
            print(stringClean("yyzzza") == "yza")
            print(stringClean("abbbcdd") == "abcd")
            print(stringClean("Hello") == "Helo")

            print("countHi2")
            print(countHi2("ahixhi") == 1)
            print(countHi2("ahibhi") == 2)
            print(countHi2("xhixhi") == 0)

            print("parenBit")
            print(parenBit("xyz(abc)123") == "(abc)")
            print(parenBit("x(hello)") == "(hello)")
            print(parenBit("(xy)1") == "(xy)")

            print("nestParen")
            print(nestParen("(())") == True)
            print(nestParen("((()))") == True)
            print(nestParen("(((x))") == False)

            print("strCount")
            print(strCount("catcowcat", "cat") == 2)
            print(strCount("catcowcat", "cow") == 1)
            print(strCount("catcowcat", "dog") == 0)

            print("strCopies")
            print(strCopies("catcowcat", "cat", 2) == True)
            print(strCopies("catcowcat", "cow", 2) == False)
            print(strCopies("catcowcat", "cow", 1) == True)

            print("strDist")
            print(strDist("catcowcat", "cat") == 9)
            print(strDist("catcowcat", "cow") == 3)
            print(strDist("cccatcowcatxx", "cat") == 9)
