import sys

class PythonLogic_1(object):

        '''
        Given three ints, a b c, return True if two or more of them have the same 
        rightmost digit. The ints are non-negative.

        lastDigit(23, 19, 13) -> True
        lastDigit(23, 19, 12) -> False
        lastDigit(23, 19, 3) -> True        
        '''
        def lastDigit(values):
            digits = []
            for val in values:
                if digits.Contains(val % 10):
                    return True
                else:
                    digits.Add(val % 10)
            return False
        

        '''
        Given three ints, a b c, return True if one of them is 10 or more less than 
        one of the others. 

        lessBy10(1, 7, 11) -> True
        lessBy10(1, 7, 10) -> False
        lessBy10(11, 1, 7) -> True        
        '''
        def lessBy10(values):
            for val in values:
                if values.Contains(val - 10) or values.Contains(val + 10):
                    return True
            return False
        


        '''
            Return the sum of two 6-sided dice rolls, each in the range 1..6. 
            However, if noDoubles is True, if the two dice show the same value, 
            increment one die to the next value, wrapping around to 1 if its value was 6. 

            withoutDoubles(2, 3, True) -> 5
            withoutDoubles(3, 3, True) -> 7
            withoutDoubles(3, 3, False) -> 6        
        '''
        def withoutDoubles(die1, die2, noDoubles):
            if noDoubles and (die1 == die2):
                if die1 == 6:
                    die1 = 1
                else:
                    die1 += 1

            return die1 + die2
        

        '''
        Given two int values, return whichever value is larger. 
        However if the two values have the same remainder when divided by 5, 
        then the return the smaller value. However, in all cases, if the two 
        values are the same, return 0.

        maxMod5(25, 15) -> 15
        maxMod5(6, 2) -> 6
        maxMod5(3, 3) -> 0        
        '''
        def maxMod5(values):
            vals = ()
            mods = ()
 
            for val in values:
                 vals.Add(val)
                 mods.Add(val % 5)
            
            if vals.Count < 2:
                return 0
            elif mods.Count < 2:
                return vals.Min()
            else:
                return vals.Max()

        

        '''
        You have a red lottery ticket showing ints a, b, and c, each of which 
        is 0, 1, or 2. If they are all the value 2, the result is 10. Otherwise 
        if they are all the same, the result is 5. Otherwise so long as both 
        b and c are different from a, the result is 1. Otherwise the result is 0. 

        redTicket(2, 2, 2) -> 10
        redTicket(2, 2, 1) -> 0
        redTicket(0, 0, 0) -> 5        
        '''
        def redTicket(values):
            vals = ()
            values.add(values)
            if vals.Count == 1:
                if vals.Contains(2):
                    return 10
                else:
                    return 5
            else:
                return 0
        

        '''
        You have a green lottery ticket, with ints a, b, and c on it. 
        If the numbers are all different from each other, the result is 0. 
        If all of the numbers are the same, the result is 20. 
        If two of the numbers are the same, the result is 10. 

        greenTicket(1, 2, 3) -> 0
        greenTicket(2, 2, 2) -> 20
        greenTicket(1, 1, 2) -> 10        
        '''
        def greenTicket(values):
            allSame = True
            allDifferent = True

            for i in range (0, len(values)):
                for j in range(i+1, len(values)):
                    if values[i] != values[j]:
                        allSame = False
                    if values[i] == values[j]:
                        allDifferent = False
            
            if allSame:
                return 20
            elif allDifferent:
                return 0
            else:
                return 10
        

        '''
        You have a blue lottery ticket, with ints a, b, and c on it. 
        This makes three pairs, which we'll call ab, bc, and ac. 
        Consider the sum of the numbers in each pair. 
        If any pair sums to exactly 10, the result is 10. 
        Otherwise if the ab sum is exactly 10 more than either bc or ac sums, 
        the result is 5. Otherwise the result is 0. 

        blueTicket(9, 1, 0) -> 10
        blueTicket(9, 2, 0) -> 0
        blueTicket(14, 1, 4) -> 5        
        '''
        def blueTicket(values):
            pairs = ()

            for i in range(0, len(values)):
                for j in range(0, len(values)):
                    if i != j:
                        pair = values[i] + values[j]
                        if pair == 10:
                            return 10
                        elif pairs.Contains(pair - 10):
                            return 5
                        elif pairs.Contains(pair + 10):
                            return 5
                        else:
                            pairs.Add(pair)
            
            return 0
        

        '''
        Given two ints, each in the range 10..99, return True if there is 
        a digit that appears in both numbers, such as the 2 in 12 and 23.

        shareDigit(12, 23) -> True
        shareDigit(12, 34) -> False
        shareDigit(12, 44) -> False        
        '''
        def shareDigit(values):
            List<HashSet<int>> list = new List<HashSet<int>>()

            for i in range(0, len(values)):
                digits = ()

                if values[i] == 0:
                    digits.Add(values[i])
                else:
                    while values[i] != 0:
                        digits.Add(values[i] % 10)
                        values[i] /= 10

                list.append(digits)
            

            for i in range (0, list.Count-1):
                for j in range(i+1, list.Count)::
                    for n in list[i]:
                        if list[j].Contains(n):
                            return True

            return False
        

        '''
        Calculate the sum and the maximum of the passed-in values. 
        If the sum and maximum have the same number of digits then 
        return the sum, otherwise return the maximum.

        sumLimit(2, 3) -> 5
        sumLimit(8, 3) -> 8
        sumLimit(-12, 3) -> -9       
        '''
        def sumLimit(values):
            sum = values.Sum()
            max = values.Max()
            sumDigits = Math.Abs(sum).ToString().Length
            maxDigits = Math.Abs(max).ToString().Length
            return sumDigits == maxDigits


    print("lastDigit")
    print(lastDigit(23, 19, 13) ==  True)
    print(lastDigit(23, 19, 12) == False)
    print(lastDigit(23, 19, 3) == True)    

    print("lessBy10")
    print(lessBy10(1, 7, 11) == True)
    print(lessBy10(1, 7, 10) == False)
    print(lessBy10(11, 1, 7) == True)     

    print("withoutDoubles")
    print(withoutDoubles(6, 6, True) == 7)
    print(withoutDoubles(2, 3, True) == 5)
    print(withoutDoubles(3, 3, True) == 7)
    print(withoutDoubles(3, 3, False) == 6)       

    print("maxMod5")
    print(maxMod5(25, 15) == 15)
    print(maxMod5(6, 2) == 6)
    print(maxMod5(3, 3) == 0)      

    print("redTicket")
    print(redTicket(2, 2, 2) == 10)
    print(redTicket(2, 2, 1) == 0)
    print(redTicket(0, 0, 0) == 5)      

    print("greenTicket")
    print(greenTicket(1, 2, 3) == 0)
    print(greenTicket(2, 2, 2) == 20)
    print(greenTicket(1, 1, 2) == 10)      
            
    print("blueTicket")
    print(blueTicket(14, 1, 4) == 5)
    print(blueTicket(9, 1, 0) == 10)
    print(blueTicket(9, 2, 0) == 0)

    print("shareDigit")
    print(shareDigit(12, 34, 56, 78, 90, 0) == True)
    print(shareDigit(12, 23) == True)
    print(shareDigit(12, 34) == False)
    print(shareDigit(12, 44) == False)      
            
    print("sumLimit")
    print(sumLimit(-12, 3) == -9)
    print(sumLimit(2, 3) == 5)
    print(sumLimit(8, 3) == 8)