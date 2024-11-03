# for each row down the cells value will only be added to its two children j, j+ 1
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(rowIndex):
            new_row = [0] * (len(result) + 1)
            for j in range(len(result)):
                new_row[j] += result[j]
                new_row[j + 1] += result[j]
            
            result = new_row
        
        return result

