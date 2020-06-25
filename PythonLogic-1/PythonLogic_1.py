import sys

class PythonLogic_1(object):

        '''
        Given three ints, a b c, return True if two or more of them have the same 
        rightmost digit. The ints are non-negative.

        lastDigit(23, 19, 13) -> True
        lastDigit(23, 19, 12) -> False
        lastDigit(23, 19, 3) -> True        
        '''
        def lastDigit(ld1, ld2, ld3):
            lastDigit1 = ld1%10
            lastDigit2 = ld2%10
            lastDigit3 = ld3%10
            return lastDigit1 == lastDigit2 or lastDigit1 == lastDigit3 or lastDigit2 == lastDigit3

        '''
        Given three ints, a b c, return True if two or more of them have the same 
        rightmost digit. The ints are non-negative.

        lastDigit2(23, 19, 13) -> True
        lastDigit2(23, 19, 12) -> False
        lastDigit2(23, 19, 3) -> True        
        '''
        def lastDigit2(*args):
            ld2Set = set()
            for arg in args:
                ld2digit = arg % 10
                if ld2digit in ld2Set:
                    return True
                else:
                    ld2Set.add(ld2digit)
            return False

        '''
        Given three ints, a b c, return True if one of them is 10 or more less than 
        one of the others. 

        lessBy10(1, 7, 11) -> True
        lessBy10(1, 7, 10) -> False
        lessBy10(11, 1, 7) -> True        
        '''
        def lessBy10(lbtA, lbtB, lbtC):
            lbtAB = abs(lbtA - lbtB)
            lbtAC = abs(lbtA - lbtC)
            lbtBC = abs(lbtB - lbtC)
            return max(lbtAB, max(lbtAC, lbtBC)) >= 10

        '''
        Given three ints, a b c, return True if one of them is 10 or more less than 
        one of the others. 

        lessBy102(1, 7, 11) -> True
        lessBy102(1, 7, 10) -> False
        lessBy102(11, 1, 7) -> True        
        '''
        def lessBy102(*args):
            return max(args) - min(args) >= 10


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
        def maxMod5(mm5A, mm5B):
            if mm5A == mm5B:
                return 0
            elif mm5A % 5 == mm5B % 5:
                return min(mm5A, mm5B)
            else:
                return max(mm5A, mm5B)

        

        '''
        You have a red lottery ticket showing ints a, b, and c, each of which 
        is 0, 1, or 2. If they are all the value 2, the result is 10. Otherwise 
        if they are all the same, the result is 5. Otherwise so long as both 
        b and c are different from a, the result is 1. Otherwise the result is 0. 

        redTicket(2, 2, 2) -> 10
        redTicket(2, 2, 1) -> 0
        redTicket(0, 0, 0) -> 5        
        '''
        def redTicket(rtA, rtB, rtC):
            if rtA == 2 and rtB == 2 and rtC == 2:
                return 10
            elif rtA == rtB == rtC:
                return 5
            elif rtA != rtB and rtA != rtC:
                return 1
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
        def greenTicket(gtA, gtB, gtC):
            if gtA != gtB and gtA != gtC and gtB != gtC:
                return 0
            elif gtA == gtB == gtC:
                return 20
            else:
                return 10

        '''
        You have a green lottery ticket, with ints a, b, and c on it. 
        If the numbers are all different from each other, the result is 0. 
        If all of the numbers are the same, the result is 20. 
        If two of the numbers are the same, the result is 10. 

        greenTicket2(1, 2, 3) -> 0
        greenTicket2(2, 2, 2) -> 20
        greenTicket2(1, 1, 2) -> 10        
        '''
        def greenTicket2(*args):
            gtSet = set(args)
            gtCount = len(gtSet)
            if gtCount == 3:
                return 0
            elif gtCount == 2:
                return 10
            else:
                return 20


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
        def blueTicket(btA, btB, btC):
            btAB = btA + btB
            btAC = btA + btC
            btBC = btB + btC

            if btAB == 10 or btAB == 10 or btBC == 10:
                return 10
            elif btAB - btAC == 10 or btAB - btBC == 10:
                return 5
            else:
                return 0


        '''
        Given two ints, each in the range 10..99, return True if there is 
        a digit that appears in both numbers, such as the 2 in 12 and 23.

        shareDigit(90, 0) -> True
        shareDigit(12, 23) -> False
        shareDigit(12, 34) -> False        
        '''
        def shareDigit(sd1, sd2):
            sdSet = set()

            while True:
                sdSet.add(sd1%10)
                sd1 //= 10
                if sd1 == 0:
                    break
            
            while True:
                if sd2%10 in sdSet:
                    return True
                sd2 //= 10
                if sd2 == 0:
                    break

            return False

        '''
        Given two ints, each in the range 10..99, return True if there is 
        a digit that appears in both numbers, such as the 2 in 12 and 23.

        shareDigit2(90, 0) -> True
        shareDigit2(12, 23) -> False
        shareDigit2(12, 34) -> False        
        '''
        def shareDigit2(sd21, sd22):
            sd21Str = str(sd21)
            sd22Str = str(sd22)
            for ch in sd21Str:
                if ch in sd22Str:
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
        def sumLimit(sl1, sl2):
            slSum = sl1 + sl2
            slMax = max(sl1, sl2)
            slSumStr = str(abs(slSum))
            slMaxStr = str(abs(slMax))
            if len(slSumStr) == len(slMaxStr):
                return slSum
            else:
                return slMax



        print("lastDigit")
        print(lastDigit(23, 19, 13) ==  True)
        print(lastDigit(23, 19, 12) == False)
        print(lastDigit(23, 19, 3) == True)    

        print("lastDigit2")
        print(lastDigit2(23, 19, 13) ==  True)
        print(lastDigit2(23, 19, 12) == False)
        print(lastDigit2(23, 19, 3) == True)    

        print("lessBy10")
        print(lessBy10(1, 7, 11) == True)
        print(lessBy10(1, 7, 10) == False)
        print(lessBy10(11, 1, 7) == True)     

        print("lessBy102")
        print(lessBy102(1, 7, 11) == True)
        print(lessBy102(1, 7, 10) == False)
        print(lessBy102(11, 1, 7) == True)     

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

        print("greenTicket2")
        print(greenTicket2(1, 2, 3) == 0)
        print(greenTicket2(2, 2, 2) == 20)
        print(greenTicket2(1, 1, 2) == 10)     
        
        print("blueTicket")
        print(blueTicket(14, 1, 4) == 5)
        print(blueTicket(9, 1, 0) == 10)
        print(blueTicket(9, 2, 0) == 0)

        print("shareDigit")
        print(shareDigit(90, 0) == True)
        print(shareDigit(12, 23) == True)
        print(shareDigit(12, 34) == False)

        print("shareDigit2")
        print(shareDigit2(90, 0) == True)
        print(shareDigit2(12, 23) == True)
        print(shareDigit2(12, 34) == False)
            
        print("sumLimit")
        print(sumLimit(-12, 3) == -9)
        print(sumLimit(2, 3) == 5)
        print(sumLimit(8, 3) == 8)