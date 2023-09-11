class utils:

    def reversed(self, num):
        returnNum = None
        returnStr = ""
        if isinstance(num,int):
            if (num < 0):
                num = abs(num)
                returnStr+=("-")
            numString = str(num)
            returnStr+=(numString[::-1])
            returnNum = int(returnStr)
        return returnNum
        
    def formatter(self, num):
        returnBin = None
        returnOct = None
        if isinstance(num,int):
            returnBin = bin(num)
            returnOct = oct(num)
        return returnBin, returnOct