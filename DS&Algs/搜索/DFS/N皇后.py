class NQueens:
    '''N皇后问题'''
    def __init__(self, N):
        self.N = N
        self.solutions = []
        self.current_state = []
        self.solution_count = 0

    def __valid(self, i, j):
        '''检查位置是否有效'''
        for x, y in self.current_state:
            if j == y or i + j == x + y or i - j == x - y:
                return False
        return True
    
    def __dfs(self, n):
        '''递归回溯求解'''
        if n == self.N:
            self.solutions.append(self.current_state[:])
            self.solution_count += 1
            return
        for m in range(self.N):
            if self.__valid(n, m):
                self.current_state.append((n, m))
                self.__dfs(n + 1)
                self.current_state.pop()

    def solve(self):
        '''求解N皇后问题'''
        self.__dfs(0)
        if self.solution_count == 0:
            raise ValueError("No solution")

    def get_solutions(self):
        '''返回解集'''
        return self.solutions
    
    def get_solution_count(self):
        '''返回解的数量'''
        return self.solution_count
    
    def print_solutions(self, max_display=4):
        '''打印部分解'''
        for solution in self.solutions[:max_display]:
            board = [['.' for _ in range(self.N)] for _ in range(self.N)]
            for x, y in solution:
                board[x][y] = 'Q'
            for row in board:
                print(' '.join(row))
            print()


Q = NQueens(8)
Q.solve()
solutions = Q.get_solutions()
counts = Q.get_solution_count()


Q.print_solutions()
print(f"解的总数：{counts}")