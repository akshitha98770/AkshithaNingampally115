def spiralOrder(matrix: List[List[int]]) -> List[int]:
        top,bottom=0,len(matrix)-1 
        left,right=0,len(matrix[0])-1
        res=[]
        while top<=bottom and left<=right:
            #left to right
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top+=1 
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right-=1 
            if top<=bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom-=1
            if left<=right:
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                left+=1 
        return res
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))

def transpose(matrix: List[List[int]]) -> List[List[int]]:
        rows,col=len(matrix),len(matrix[0])
        res=[[0]*rows for _ in range(col)]
        for r in range(rows):
            for c in range(col):
                res[c][r]=matrix[r][c]
        return res
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))