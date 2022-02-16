class Backpack:

    def __init__(self, a, c, b):
        self.size = a
        self.value = c
        self.bSize = b
        self.matrix = [[-1 for x in range(b+1)] for j in range(len(a)+1)]

    def dynamic(self, n, b):
        if n == 0 or b == 0:
            self.matrix[n][b] = 0
            return 0
        elif self.matrix[n][b] != -1:
            return self.matrix[n][b]
        elif self.size[n-1] <= b:
            self.matrix[n][b] = max(self.value[n-1] + self.dynamic(n-1, b - self.size[n-1]), self.dynamic(n-1, b))
            return self.matrix[n][b]
        else:
            self.matrix[n][b] = self.dynamic(n - 1, b)
            return self.matrix[n][b]
        
    def greedy(self, n, b):
        result = []
        size = 0
        res = 0

        for x in range(n):
            temp = [self.value[x], self.size[x], (self.value[x] / self.size[x])]
            result.append(temp)
        result = sorted(result, key = lambda x: x[2], reverse = True)
        for i in range(n):
            if size + result[i][1] <= b:
                size += result[i][1]
                res += result[i][0]
        return res


if __name__ == '__main__':

    with open('test.txt', 'r') as f:
        data=[]
        for line in f:
            line=line.split('\n')
            for l in line:
                res=[]
                mark=l.split(' ')
                for m in mark:
                    if m.isnumeric():
                        res.append(m)
                if len(res)>0:
                    data.append([ int(x) for x in res ])

    n = data[0][0]
    a = data[1]
    c = data[2]
    b = data[3][0]
    s = Backpack(a, c, b)

    print("dynamic: "+ str(s.dynamic(n, b)))
    print(" greedy: "+ str(s.greedy(n, b)))


