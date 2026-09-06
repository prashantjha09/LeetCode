class Solution:
    def reverse(self, x: int) -> int:
        ten_multiple = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]
        count = 0
        positive = True
        if x==0:
            return x
        if x < 0 :
            positive = False
            x = (-1)*x
        while True:
            i =  x//ten_multiple[count]
            if 9>= i >= 1:
                break
            count+=1


        output = 0
        while count >= 0:
            output = output + (x%10)*ten_multiple[count]
            x = x//10
            count-=1
        print(output)
        # return output if positive else -1*output

        if not positive:
            output = -output

        if output < -2**31 or output > 2**31 - 1:
            return 0
        return output


