def countNegatives(grid: List[List[int]]) -> int:
        a=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    a+=1
        return a
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))

def countNegative(grid: List[List[int]]) -> int:
        a=0
        r,c=len(grid),len(grid[0])
        for rr in range(r):
            for cc in range(c):
                if grid[rr][cc]<0:
                    a+=(c-cc)
                    break 
        return a
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegative(grid))

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for j in range(len(i)):
                i[j]=1-i[j]
        return image
image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))
