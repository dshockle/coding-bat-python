import sys

class PythonRecursion_1(object:
        '''
        Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. 
        Compute the result recursively (without loops). 

        factorial(1) -> 1
        factorial(2) -> 2
        factorial(3) -> 6
        '''
        def factorial(int n)
        
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        

        '''        
        We have a number of bunnies and each bunny has two big floppy ears. We want to compute the 
        total number of ears across all the bunnies recursively (without loops or multiplication). 

        bunnyEars(0) -> 0
        bunnyEars(1) -> 2
        bunnyEars(2) -> 4
        '''
        def bunnyEars(int bunnies):
            if bunnies == 0:
                return 0
            elif bunnies == 1:
                return 2
            else:
                return 2 + bunnyEars(bunnies - 1)

        

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
        def fibonacci(int n):
            if n == 0):
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)
        

        '''        
        We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the 
        normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a 
        raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without 
        loops or multiplication). 

        bunnyEars2(0) -> 0
        bunnyEars2(1) -> 2
        bunnyEars2(2) -> 5
        '''
        def bunnyEars2(int bunnies):
            if bunnies == 0:
                return 0
            elif bunnies == 1:
                return 2
            else:
                return 3 - bunnies % 2 + bunnyEars(bunnies - 1)
        

        '''
        We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, 
        the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the 
        total number of blocks in such a triangle with the given number of rows. 

        triangle(0) -> 0
        triangle(1) -> 1
        triangle(2) -> 3
        '''
        def triangle(int rows):
            if rows == 0:
                return 0
            elif rows == 1:
                return 1
            else:
                return rows + triangle(rows - 1)
        

        '''        
        Given a non-negative int n, return the sum of its digits recursively (no loops).

        sumDigits(126) -> 9
        sumDigits(49) -> 13
        sumDigits(12) -> 3
'''
        def sumDigits(int n):
            if n == 0:
                return 0
            else:
                return n % 10 + sumDigits(n / 10)
        

        '''        
        Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for 
        example 717 yields 2. (no loops). 

        count7(717) -> 2
        count7(7) -> 1
        count7(123) -> 0
        '''
        def count7(int n):
            if n == 0)
                return 0
            elif n % 10 == 7)
                return 1 + count7(n / 10)
            else
                return count7(n / 10)
        

        '''        
        Given a non-negative int n, compute recursively (no loops) the count of the occurrences 
        of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, 
        so 8818 yields 4. 

        count8(8) -> 1
        count8(818) -> 2
        count8(8818) -> 4
        '''
        def count8(int n):
            if n == 0:
                return 0
            elif n % 10 == 8:
                if n / 10) % 10 == 8:
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
        def powerN(int baseNum, int pow):
            if pow == 0:
                return 1
            elif pow == 1:
                return baseNum
            else:
                return baseNum * powerN(baseNum, pow - 1)
        


        '''
        Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string. 

        countX("xxhixx") -> 4
        countX("xhixhix") -> 3
        countX("hi") -> 0

            '''
        def countX(string str):
            if len(str) == 0:
                return 0
            elif str[0] == 'x':
                return 1 + countX(str.Substring(1))
            else:
                return countX(str.Substring(1))
        


        '''
        Given a string, compute recursively (no loops) the number of times lowercase "hi" appears 
        in the string. 

        countHi("xxhixx") -> 1
        countHi("xhixhix") -> 2
        countHi("hi") -> 1
        '''
        def countHi(string str):
            if len(str) < 2:
                return 0
            elif str.Substring(0, 2).Equals("hi")):
                return 1 + countHi(str.Substring(1))
            else:
                return countHi(str.Substring(1))
        

        '''
        Given a string, compute recursively (no loops) a new string where all the lowercase 'x' 
        chars have been changed to 'y' chars. 

        changeXY("codex") -> "codey"
        changeXY("xxhixx") -> "yyhiyy"
        changeXY("xhixhix") -> "yhiyhiy"
        '''
        def changeXY(string str):
            if len(str) == 0:
                return ""
            elif str[0] == 'x':
                return "y" + changeXY(str.Substring(1))
            else:
                return str[0] + changeXY(str.Substring(1))

        

        '''
        Given a string, compute recursively (no loops) a new string where all appearances of "pi" 
        have been replaced by "3.14". 

        changePi("xpix") -> "x3.14x"
        changePi("pipi") -> "3.143.14"
        changePi("pip") -> "3.14p"
        '''
        def changePi(string str):
            if len(str) < 2:
                return str
            elif str.Substring(0, 2).Equals("pi")):
                return "3.14" + changePi(str.Substring(2))
            else:
                return str.Substring(0,1) + changePi(str.Substring(1))
        

        '''        
        Given a string, compute recursively a new string where all the 'x' chars have been removed.

        noX("xaxb") -> "ab"
        noX("abc") -> "abc"
        noX("xx") -> ""
        '''
        def noX(string str):
            if len(str) < 1:
                return str
            elif str[0] == 'x':
                return noX(str.Substring(1))
            else:
                return str[0] + noX(str.Substring(1))
        

        '''
        Given an array of ints, compute recursively if the array contains a 6. We'll use the 
        convention of considering only the part of the array that begins at the given index. 
        In this way, a recursive call can pass index+1 to move down the array. The initial 
        call will pass in index as 0. 

        array6(1, 6, 4, 0) -> true
        array6(1, 4, 0) -> false
        array6(6, 0) -> true
        '''
        def bool array6(int[] nums, int index)
            if nums.Length == 0:
                return false
            elif nums.Length <= index:
                return false
            elif nums[index] == 6:
                return true
            else:
                return array6(nums, index + 1)
        

        '''
        Given an array of ints, compute recursively the number of times that the value 11 appears 
        in the array. We'll use the convention of considering only the part of the array that begins 
        at the given index. In this way, a recursive call can pass index+1 to move down the array. 
        The initial call will pass in index as 0. 

        array11(1, 2, 11, 0) -> 1
        array11(11, 11, 0) -> 2
        array11(1, 2, 3, 4, 0) -> 0
        '''
        def array11(int[] nums, int index):
            if nums.Length == 0 || nums.Length <= index:
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

        array220(1, 2, 20, 0) -> true
        array220(3, 30, 0) -> true
        array220(3, 0) -> false
        '''
        def bool array220(int[] nums, int index):
            if nums.Length < 2:
                return false
            elif nums[index] * 10 == nums[index + 1]:
                return true
            else:
                return array220(nums, index + 1)
        

        '''
        Given a string, compute recursively a new string where all the adjacent chars are now separated 
        by a "*". 

        allStar("hello") -> "h*e*l*l*o"
        allStar("abc") -> "a*b*c"
        allStar("ab") -> "a*b"
        '''

        def allStar(string str):
            if string.IsNullOrEmpty(str) || len(str) == 1:
                return str
            else:
                return str[0] + "*" + allStar(str.Substring(1))
        

        '''
        Given a string, compute recursively a new string where identical chars that are adjacent in 
        the original string are separated from each other by a "*". 

        pairStar("hello") -> "hel*lo"
        pairStar("xxyy") -> "x*xy*y"
        pairStar("aaaa") -> "a*a*a*a"
        '''
        def pairStar(string str):
            if string.IsNullOrEmpty(str) || len(str) == 1:
                return str
            elif str[0] == str[1]:
                return str[0] + "*" + pairStar(str.Substring(1))
            else:
                return str[0] + pairStar(str.Substring(1))

        

        '''
        Given a string, compute recursively a new string where all the lowercase 'x' chars have been 
        moved to the end of the string. 

        endX("xxre") -> "rexx"
        endX("xxhixx") -> "hixxxx"
        endX("xhixhix") -> "hihixxx"
        '''
        def endX(string str):
            if string.IsNullOrEmpty(str):
                return str
            elif str[0] == 'x'):
                return endX(str.Substring(1)) + 'x'
            else:
                return str[0] + endX(str.Substring(1))
        

        '''
        We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" 
        the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. 
        Recursively compute the number of pairs in the given string. 

        countPairs("axa") -> 1
        countPairs("axax") -> 2
        countPairs("axbx") -> 1
        '''
        def countPairs(string str):
            if string.IsNullOrEmpty(str) || len(str) < 3):
                return 0
            elif str[0] == str[2]):
                return 1 + countPairs(str.Substring(1))
            else:
                return countPairs(str.Substring(1))
        


        '''        
        Count recursively the total number of "abc" and "aba" substrings that appear in the given string. 

        countAbc("abc") -> 1
        countAbc("abcxxabc") -> 2
        countAbc("abaxxaba") -> 2
        '''
        def countAbc(string str):
            if string.IsNullOrEmpty(str) || len(str) < 3):
                return 0
            elif str.Substring(0,3).Equals("abc") || str.Substring(0,3).Equals("aba")):
                return 1 + countAbc(str.Substring(1))
            else:
                return countAbc(str.Substring(1))
        

        '''
        Given a string, compute recursively (no loops) the number of "11" substrings in the string. 
        The "11" substrings should not overlap. 

        count11("11abc11") -> 2
        count11("abc11x11x11") -> 3
        count11("111") -> 1
        '''
        def count11(string str)
        
            if string.IsNullOrEmpty(str) || len(str) < 2)
                return 0
            elif str.Substring(0, 2).Equals("11"))
                return 1 + count11(str.Substring(2))
            else
                return count11(str.Substring(1))
        

        '''
        Given a string, return recursively a "cleaned" string where adjacent chars that are the same 
        have been reduced to a single char. So "yyzzza" yields "yza". 

        stringClean("yyzzza") -> "yza"
        stringClean("abbbcdd") -> "abcd"
        stringClean("Hello") -> "Helo"
        '''
        def stringClean(string str):
            if string.IsNullOrEmpty(str) || len(str) < 2):
                return str
            elif str[0] == str[1]):
                return stringClean(str.Substring(1))
            else:
                return str[0] + stringClean(str.Substring(1))
        

        '''
        Given a string, compute recursively the number of times lowercase "hi" appears in the string, 
        however do not count "hi" that have an 'x' immedately before them. 

        countHi2("ahixhi") -> 1
        countHi2("ahibhi") -> 2
        countHi2("xhixhi") -> 0
        '''
        def countHi2(string str):
            if string.IsNullOrEmpty(str) || len(str) < 2):
                return 0
            elif len(str) == 2):
                if str.Equals("hi")):
                    return 1
                else:
                    return 0
            elif str[0] == 'x'):
                return countHi2(str.Substring(2))
            elif str.Substring(0,2).Equals("hi")):
                return 1 + countHi2(str.Substring(2))
            else:
                return countHi2(str.Substring(1))
        

        '''
        Given a string that contains a single pair of parenthesis, compute recursively a new string 
        made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)". 

        parenBit("xyz(abc)123") -> "(abc)"
        parenBit("x(hello)") -> "(hello)"
        parenBit("(xy)1") -> "(xy)"
        '''
        def parenBit(string str):
            if string.IsNullOrEmpty(str) || len(str) < 2):
                return ""
            elif str[0] == '(' && str[len(str) - 1] == ')'):
                return str
            elif str[0] == '('):
                return parenBit(str.Substring(0, len(str) - 1)):
            elif str[len(str) - 1] == ')'):
                return parenBit(str.Substring(1))
            else:
                return parenBit(str.Substring(1, len(str) - 1))
        

        '''
        Given a string, return true if it is a nesting of zero or more pairs of parenthesis, 
        like "(())" or "((()))". Suggestion: check the first and last chars, and then recur 
        on what's inside them.

        nestParen("(())") -> true
        nestParen("((()))") -> true
        nestParen("(((x))") -> false
        nestParen("((())") -> false
        nestParen("((()()") -> false
        nestParen("()") -> true
        nestParen("") -> true
        nestParen("(yy)") -> false
        nestParen("(())") -> true
        nestParen("(((y))") -> false
        nestParen("((y)))") -> false
        nestParen("((()))") -> true
        nestParen("(())))") -> false
        nestParen("((yy())))") -> false
        nestParen("(((())))") -> true
        '''
        def bool nestParen(string str):
            if string.IsNullOrEmpty(str)):
                return true
            elif len(str) == 1):
                return false
            else:
                char start = str[0]
                char end = str[len(str) - 1]

                if start != '(' || end != ')'):
                    return false
                else:
                    return nestParen(str.Substring(1, len(str) - 2))
            
        

        '''        
        Given a string and a non-empty substring sub, compute recursively the number of times that 
        sub appears in the string, without the sub strings overlapping. 

        strCount("catcowcat", "cat") -> 2
        strCount("catcowcat", "cow") -> 1
        strCount("catcowcat", "dog") -> 0
        '''
        def strCount(string str, string sub):
            if string.IsNullOrEmpty(str) || string.IsNullOrEmpty(sub)):
                return 0
            elif len(str) < len(sub)):
                return 0
            elif str.Substring(0, len(sub)).Equals(sub)):
                return 1 + strCount(str.Substring(len(sub)), sub)
            else:
                return strCount(str.Substring(1), sub)
        


        '''
        Given a string and a non-empty substring sub, compute recursively if at least n copies of 
        sub appear in the string somewhere, possibly with overlapping. N will be non-negative. 

        strCopies("catcowcat", "cat", 2) -> true
        strCopies("catcowcat", "cow", 2) -> false
        strCopies("catcowcat", "cow", 1) -> true
        '''
        def bool strCopies(string str, string sub, int n):
            if n == 0:
                return true
            elif string.IsNullOrEmpty(str) || string.IsNullOrEmpty(sub):
                return false
            elif len(str) < len(sub):
                return false
            elif str.Substring(0, len(sub)).Equals(sub):
                return strCopies(str.Substring(len(sub)), sub, n - 1)
            else:
                return strCopies(str.Substring(1), sub, n)
        

        '''      
        Given a string and a non-empty substring sub, compute recursively the largest substring 
        which starts and ends with sub and return its length. 

        strDist("catcowcat", "cat") -> 9
        strDist("catcowcat", "cow") -> 3
        strDist("cccatcowcatxx", "cat") -> 9
        '''
        def strDist(string str, string sub):
            if string.IsNullOrEmpty(str) || string.IsNullOrEmpty(sub):
                return 0
            elif len(str) < len(sub):
                return 0
            elif str.Substring(0, len(sub)).Equals(sub) && str.Substring(len(str) - len(sub)).Equals(sub):
                return len(str)
            elif str.Substring(0, len(sub)).Equals(sub):
                return strDist(str.Substring(0, len(str) - 1), sub)
            elif str.Substring(len(str) - len(sub)).Equals(sub):
                return strDist(str.Substring(1), sub)
            else 
                return strDist(str.Substring(1, len(str) - 1), sub)
        


            Console.WriteLine("factorial")
            Console.WriteLine(factorial(1) == 1)
            Console.WriteLine(factorial(2) == 2)
            Console.WriteLine(factorial(3) == 6)

            Console.WriteLine("bunnyEars")
            Console.WriteLine(bunnyEars(0) == 0)
            Console.WriteLine(bunnyEars(1) == 2)
            Console.WriteLine(bunnyEars(2) == 4)

            Console.WriteLine("fibonacci")
            Console.WriteLine(fibonacci(0) == 0)
            Console.WriteLine(fibonacci(1) == 1)
            Console.WriteLine(fibonacci(2) == 1)

            Console.WriteLine("bunnyEars2")
            Console.WriteLine(bunnyEars2(0) == 0)
            Console.WriteLine(bunnyEars2(1) == 2)
            Console.WriteLine(bunnyEars2(2) == 5)

            Console.WriteLine("triangle")
            Console.WriteLine(triangle(0) == 0)
            Console.WriteLine(triangle(1) == 1)
            Console.WriteLine(triangle(2) == 3)

            Console.WriteLine("sumDigits")
            Console.WriteLine(sumDigits(126) == 9)
            Console.WriteLine(sumDigits(49) == 13)
            Console.WriteLine(sumDigits(12) == 3)

            Console.WriteLine("count7")
            Console.WriteLine(count7(717) == 2)
            Console.WriteLine(count7(7) == 1)
            Console.WriteLine(count7(123) == 0)

            Console.WriteLine("count8")
            Console.WriteLine(count8(8) == 1)
            Console.WriteLine(count8(818) == 2)
            Console.WriteLine(count8(8818) == 4)

            Console.WriteLine("powerN")
            Console.WriteLine(powerN(3, 1) == 3)
            Console.WriteLine(powerN(3, 2) == 9)
            Console.WriteLine(powerN(3, 3) == 27)

            Console.WriteLine("countX")
            Console.WriteLine(countX("xxhixx") == 4)
            Console.WriteLine(countX("xhixhix") == 3)
            Console.WriteLine(countX("hi") == 0)

            Console.WriteLine("countHi")
            Console.WriteLine(countHi("xxhixx") == 1)
            Console.WriteLine(countHi("xhixhix") == 2)
            Console.WriteLine(countHi("hi") == 1)

            Console.WriteLine("changeXY")
            Console.WriteLine(changeXY("codex") == "codey")
            Console.WriteLine(changeXY("xxhixx") == "yyhiyy")
            Console.WriteLine(changeXY("xhixhix") == "yhiyhiy")

            Console.WriteLine("changePi")
            Console.WriteLine(changePi("xpix") == "x3.14x")
            Console.WriteLine(changePi("pipi") == "3.143.14")
            Console.WriteLine(changePi("pip") == "3.14p")

            Console.WriteLine("noX")
            Console.WriteLine(noX("xaxb") == "ab")
            Console.WriteLine(noX("abc") == "abc")
            Console.WriteLine(noX("xx") == "")

            Console.WriteLine("array6")
            Console.WriteLine(array6(new int[]  1, 6, 4, 0) == true)
            Console.WriteLine(array6(new int[]  1, 4, 0) == false)
            Console.WriteLine(array6(new int[]  6 , 0) == true)

            Console.WriteLine("array11")
            Console.WriteLine(array11(new int[]  1, 2, 11, 0) == 1)
            Console.WriteLine(array11(new int[]  11, 11, 0) == 2)
            Console.WriteLine(array11(new int[]  1, 2, 3, 4, 0) == 0)

            Console.WriteLine("array220")
            Console.WriteLine(array220(new int[]  1, 2, 20, 0) == true)
            Console.WriteLine(array220(new int[]  3, 30, 0) == true)
            Console.WriteLine(array220(new int[]  3 , 0) == false)

            Console.WriteLine("allStar")
            Console.WriteLine(allStar("hello") == "h*e*l*l*o")
            Console.WriteLine(allStar("abc") == "a*b*c")
            Console.WriteLine(allStar("ab") == "a*b")

            Console.WriteLine("pairStar")
            Console.WriteLine(pairStar("hello") == "hel*lo")
            Console.WriteLine(pairStar("xxyy") == "x*xy*y")
            Console.WriteLine(pairStar("aaaa") == "a*a*a*a")

            Console.WriteLine("endX")
            Console.WriteLine(endX("xxre") == "rexx")
            Console.WriteLine(endX("xxhixx") == "hixxxx")
            Console.WriteLine(endX("xhixhix") == "hihixxx")

            Console.WriteLine("countPairs")
            Console.WriteLine(countPairs("axa") == 1)
            Console.WriteLine(countPairs("axax") == 2)
            Console.WriteLine(countPairs("axbx") == 1)

            Console.WriteLine("countAbc")
            Console.WriteLine(countAbc("abc") == 1)
            Console.WriteLine(countAbc("abcxxabc") == 2)
            Console.WriteLine(countAbc("abaxxaba") == 2)

            Console.WriteLine("count11")
            Console.WriteLine(count11("11abc11") == 2)
            Console.WriteLine(count11("abc11x11x11") == 3)
            Console.WriteLine(count11("111") == 1)

            Console.WriteLine("stringClean")
            Console.WriteLine(stringClean("yyzzza") == "yza")
            Console.WriteLine(stringClean("abbbcdd") == "abcd")
            Console.WriteLine(stringClean("Hello") == "Helo")

            Console.WriteLine("countHi2")
            Console.WriteLine(countHi2("ahixhi") == 1)
            Console.WriteLine(countHi2("ahibhi") == 2)
            Console.WriteLine(countHi2("xhixhi") == 0)

            Console.WriteLine("parenBit")
            Console.WriteLine(parenBit("xyz(abc)123") == "(abc)")
            Console.WriteLine(parenBit("x(hello)") == "(hello)")
            Console.WriteLine(parenBit("(xy)1") == "(xy)")

            Console.WriteLine("nestParen")
            Console.WriteLine(nestParen("(())") == true)
            Console.WriteLine(nestParen("((()))") == true)
            Console.WriteLine(nestParen("(((x))") == false)

            Console.WriteLine("strCount")
            Console.WriteLine(strCount("catcowcat", "cat") == 2)
            Console.WriteLine(strCount("catcowcat", "cow") == 1)
            Console.WriteLine(strCount("catcowcat", "dog") == 0)

            Console.WriteLine("strCopies")
            Console.WriteLine(strCopies("catcowcat", "cat", 2) == true)
            Console.WriteLine(strCopies("catcowcat", "cow", 2) == false)
            Console.WriteLine(strCopies("catcowcat", "cow", 1) == true)

            Console.WriteLine("strDist")
            Console.WriteLine(strDist("catcowcat", "cat") == 9)
            Console.WriteLine(strDist("catcowcat", "cow") == 3)
            Console.WriteLine(strDist("cccatcowcatxx", "cat") == 9)
