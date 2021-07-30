'''Problem : 01 Matrix '''

#CODE :

class Solution(object):
    def updateMatrix(self, matrix):
        def setDistance(i, j, dis):
            if i<0 or i>=M:
                return False
            if j<0 or j>=N:
                return False
            if opt[i][j]!=-1:
                return False 
            opt[i][j] = dis
            return True

        M, N = len(matrix), len(matrix[0])
        opt = [[-1]*N for _ in range(M)]
        dis = 0
        count = 0

        for i in range(M):
            for j in range(N):
                if matrix[i][j]==0:
                    count+=1
                    opt[i][j] = 0

        while count<M*N:
            for i in range(M):
                for j in range(N):
                    if opt[i][j]==dis:
                        if setDistance(i+1, j, dis+1): count+=1
                        if setDistance(i-1, j, dis+1): count+=1
                        if setDistance(i, j+1, dis+1): count+=1
                        if setDistance(i, j-1, dis+1): count+=1
            dis+=1
        return opt
