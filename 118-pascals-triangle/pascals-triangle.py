class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1,numRows):
            opt = output[-1]
            rows_answer=[1]
            j = 0
            k = 1
            while j <= k < len(opt):
                rows_answer.append(opt[j]+opt[k])            
                j+=1
                k+=1 
            rows_answer.append(1)
            output.append(rows_answer)   
        return  output     




        
        
        