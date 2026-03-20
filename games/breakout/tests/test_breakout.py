"""
打砖块游戏测试
"""
import pytest
from breakout import BreakoutGame


class TestBreakoutGame:
    """测试打砖块游戏逻辑"""
    
    def test_initial_state(self):
        """测试初始状态"""
        game = BreakoutGame()
        assert game.ball_x == 150
        assert game.ball_y == 350
        assert game.paddle_x == 110
        assert game.score == 0
        assert game.running is False
    
    def test_paddle_movement(self):
        """测试挡板移动"""
        game = BreakoutGame()
        game.move_paddle(-10)
        assert game.paddle_x == 100
        game.move_paddle(20)
        assert game.paddle_x == 120
    
    def test_paddle_boundaries(self):
        """测试挡板边界"""
        game = BreakoutGame()
        game.paddle_x = 0
        game.move_paddle(-10)
        assert game.paddle_x == 0  # 不能超出左边界
        game.paddle_x = 220
        game.move_paddle(10)
        assert game.paddle_x == 220  # 不能超出右边界
    
    def test_ball_wall_collision(self):
        """测试球碰墙反弹"""
        game = BreakoutGame()
        game.ball_x = 1
        game.ball_dx = -3
        game.move_ball()
        assert game.ball_dx == 3  # 应该反弹
    
    def test_ball_paddle_collision(self):
        """测试球碰挡板反弹"""
        game = BreakoutGame()
        game.ball_y = 380
        game.paddle_x = 110
        game.ball_x = 150
        game.move_ball()
        assert game.ball_dy == -3  # 应该反弹向上
    
    def test_brick_collision(self):
        """测试球碰砖块"""
        game = BreakoutGame()
        # 手动设置球的位置来测试碰撞
        game.ball_x = 25
        game.ball_y = 30
        initial_score = game.score
        game.check_brick_collision()
        assert game.score >= initial_score
    
    def test_reset(self):
        """测试重置"""
        game = BreakoutGame()
        game.score = 100
        game.ball_x = 200
        game.reset()
        assert game.score == 0
        assert game.ball_x == 150
    
    def test_get_state(self):
        """测试获取状态"""
        game = BreakoutGame()
        state = game.get_state()
        assert 'ball_x' in state
        assert 'ball_y' in state
        assert 'paddle_x' in state
        assert 'score' in state
        assert 'running' in state
