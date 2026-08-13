#1572 traditional
def diagonalSum(mat: List[List[int]]) -> int:
        a=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    a+=mat[i][j]
                if i+j==len(mat)-1:
                    a+=mat[i][j]
        if len(mat)%2==0:
            return a
        else:
            return a-mat[len(mat)//2][len(mat)//2]
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))
#another method 
def diagonalSums(mat: List[List[int]]) -> int:
        a=0
        n=len(mat)
        for i in range(n):
            a+=mat[i][i]+mat[i][n-i-1]
        if n%2==1:
            return a-mat[n//2][n//2]
        return a
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSums(mat))
#498
def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
        r, c = len(mat), len(mat[0])
        res = []
        
        for d in range(r + c - 1):
            di = []
            rr = 0 if d < c else d - c + 1
            cc = d if d < c else c - 1
            while rr < r and cc >= 0:
                di.append(mat[rr][cc])
                rr += 1
                cc -= 1  
            if d % 2 == 0:
                di.reverse()    
            res.extend(di)  
        return res
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(mat))
#1380
