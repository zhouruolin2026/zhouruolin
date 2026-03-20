"""
2048 游戏逻辑
"""
import random
from typing import List


class Game2048:
    def __init__(self, size: int = 4):
        self.size = size
        self.board: List[List[int]] = [[0] * size for _ in range(size)]
        self.score = 0
        self.game_over = False
        self.add_number()
        self.add_number()
    
    def add_number(self):
        """在空位随机添加 2 或 4"""
        empty = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    empty.append((i, j))
        if empty:
            i, j = random.choice(empty)
            self.board[i][j] = 2 if random.random() < 0.9 else 4
    
    def slide(self, row: List[int]) -> List[int]:
        """滑动并合并一行"""
        # 去除0
        non_zero = [x for x in row if x != 0]
        # 合并相邻相同元素
        for i in range(len(non_zero) - 1):
            if non_zero[i] == non_zero[i + 1]:
                non_zero[i] *= 2
                self.score += non_zero[i]
                non_zero[i + 1] = 0
        # 再次去除0
        non_zero = [x for x in non_zero if x != 0]
        # 补0
        while len(non_zero) < self.size:
            non_zero.append(0)
        return non_zero
    
    def transpose(self, board: List[List[int]]) -> List[List[int]]:
        """矩阵转置"""
        return [list(row) for row in zip(*board)]
    
    def move_left(self):
        """向左移动"""
        for i in range(self.size):
            self.board[i] = self.slide(self.board[i])
    
    def move_right(self):
        """向右移动"""
        for i in range(self.size):
            self.board[i] = self.slide(self.board[i][::-1])[::-1]
    
    def move_up(self):
        """向上移动"""
        self.board = self.transpose(self.board)
        self.move_left()
        self.board = self.transpose(self.board)
    
    def move_down(self):
        """向下移动"""
        self.board = self.transpose(self.board)
        self.move_right()
        self.board = self.transpose(self.board)
    
    def is_game_over(self) -> bool:
        """检查游戏是否结束"""
        # 有空位
        for row in self.board:
            if 0 in row:
                return False
        # 有相邻相同元素
        for i in range(self.size):
            for j in range(self.size):
                if i < self.size - 1 and self.board[i][j] == self.board[i + 1][j]:
                    return False
                if j < self.size - 1 and self.board[i][j] == self.board[i][j + 1]:
                    return False
        return True
    
    def get_state(self):
        """获取游戏状态"""
        return {
            'board': self.board,
            'score': self.score,
            'game_over': self.is_game_over()
        }


# 供测试使用的函数
def slide(board: List[List[int]]) -> List[List[int]]:
    """滑动所有行向左"""
    game = Game2048()
    game.board = board
    result = []
    for row in board:
        result.append(game.slide(row[:]))
    return result


def transpose(board: List[List[int]]) -> List[List[int]]:
    """矩阵转置"""
    return [list(row) for row in zip(*board)]


if __name__ == '__main__':
    game = Game2048()
    print("2048 游戏")
    print("使用 WASL/方向键移动，R 重新开始")
    
    import os
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        # 打印棋盘
        print(f"得分: {game.score}\n")
        for row in game.board:
            print(' '.join(str(x) if x != 0 else '.' for x in row).center(20))
        print()
        
        if game.is_game_over():
            print("游戏结束!")
            break
        
        key = input("方向 (WASD): ").upper()
        old_board = [row[:] for row in game.board]
        
        if key == 'W':
            game.move_up()
        elif key == 'S':
            game.move_down()
        elif key == 'A':
            game.move_left()
        elif key == 'D':
            game.move_right()
        elif key == 'R':
            game = Game2048()
            continue
        
        # 如果板子有变化，添加新数字
        if game.board != old_board:
            game.add_number()
