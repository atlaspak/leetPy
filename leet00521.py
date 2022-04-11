class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        result = [] * N
        que = []
        
        for i in range(N):
            inner = []
            for j in range(M):
                if mat[i][j] == 0:
                    inner.append(0)
                    que.append((i,j))
                else:
                    inner.append(200001)
            result.append(inner)
        
        while que:
            i,j = que.pop(0)
            cur = result[i][j]
            if(i - 1 >= 0) and (cur < result[i-1][j]):
                result[i-1][j] = cur + 1
                que.append((i-1,j))
            if(i + 1 < N) and (cur < result[i+1][j]):
                result[i+1][j] = cur + 1
                que.append((i+1,j))
            if(j - 1 >= 0) and (cur < result[i][j-1]):
                result[i][j-1] = cur + 1
                que.append((i,j-1))
            if(j + 1 < M) and (cur < result[i][j+1]):
                result[i][j+1] = cur + 1
                que.append((i,j+1))
        return result
