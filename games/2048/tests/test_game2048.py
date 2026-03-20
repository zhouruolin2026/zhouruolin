"""
2048 游戏逻辑测试
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from game2048 import Game2048, slide, transpose


class TestGame2048:
    """测试 2048 游戏逻辑"""
    
    def test_initial_state(self):
        """测试初始状态"""
        game = Game2048()
        assert game.score == 0
        # 初始有两个数字
        count = sum(1 for row in game.board for cell in row if cell != 0)
        assert count == 2
    
    def test_add_number(self):
        """测试添加数字"""
        game = Game2048()
        game.board = [[0] * 4 for _ in range(4)]
        game.add_number()
        count = sum(1 for row in game.board for cell in row if cell != 0)
        assert count == 1
    
    def test_slide_left(self):
        """测试向左滑动"""
        board = [
            [2, 2, 0, 0],
            [4, 0, 4, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        result = slide(board)
        assert result[0] == [4, 0, 0, 0]  # 2,2 -> 4
        assert result[1] == [8, 0, 0, 0]  # 4,4 -> 8
        assert result[2] == [2, 0, 0, 0]  # 2
    
    def test_transpose(self):
        """测试矩阵转置"""
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        result = transpose(board)
        assert result[0] == [1, 5, 9, 13]
        assert result[1] == [2, 6, 10, 14]
        assert result[3] == [4, 8, 12, 16]
    
    def test_move_left(self):
        """测试向左移动"""
        game = Game2048()
        game.board = [
            [2, 2, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        game.move_left()
        assert game.board[0] == [4, 4, 0, 0]
    
    def test_move_right(self):
        """测试向右移动"""
        game = Game2048()
        game.board = [
            [2, 2, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        game.move_right()
        assert game.board[0] == [0, 0, 4, 4]
    
    def test_move_up(self):
        """测试向上移动"""
        game = Game2048()
        game.board = [
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        game.move_up()
        assert game.board[0][0] == 4
    
    def test_move_down(self):
        """测试向下移动"""
        game = Game2048()
        game.board = [
            [2, 0, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        game.move_down()
        assert game.board[3][0] == 4
    
    def test_game_over_full_board(self):
        """测试游戏结束（满盘）"""
        game = Game2048()
        game.board = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [512, 1024, 2048, 2],
            [4, 8, 16, 32]
        ]
        assert game.is_game_over() is True
    
    def test_game_not_over(self):
        """测试游戏未结束"""
        game = Game2048()
        game.board = [
            [2, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        assert game.is_game_over() is False
    
    def test_get_state(self):
        """测试获取状态"""
        game = Game2048()
        state = game.get_state()
        assert 'board' in state
        assert 'score' in state
        assert 'game_over' in state
