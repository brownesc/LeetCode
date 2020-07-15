"""
https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# 124
# 995
#-----
# 1119
"""
This algorithm makes use of the normal addition that we're used to on paper. 
"""
def addStrings(num1,num2):
    index1 = len(num1)-1
    index2 = len(num2)-1
    output = []
    carry = 0

    while index1>=0 or index2>=0:
        if index1>=0:
            x1=ord(num1[index1])-ord('0')
        else:
            x1=0
        if index2>=0:
            x2 = ord(num2[index2])-ord('0')
        else:
            x2=0
        
        val= (x1+x2+carry)%10
        carry=(x1+x2+carry)//10
        output.append(val)
        index1-=1
        index2-=1
    if carry>0:
        output.append(carry)
    return "".join(str(x) for x in output[::-1])
print(addStrings("99","99"))