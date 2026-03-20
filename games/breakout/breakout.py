"""
打砖块游戏逻辑
"""
import random


class BreakoutGame:
    def __init__(self, width=300, height=400):
        self.width = width
        self.height = height
        self.reset()
    
    def reset(self):
        """重置游戏"""
        self.ball_x = self.width / 2
        self.ball_y = 350
        self.ball_dx = 3
        self.ball_dy = -3
        self.ball_r = 8
        self.paddle_width = 80
        self.paddle_height = 10
        self.paddle_x = (self.width - self.paddle_width) / 2
        self.paddle_y = self.height - 15
        self.score = 0
        self.running = False
        self.bricks = self.create_bricks()
    
    def create_bricks(self):
        """创建砖块"""
        bricks = []
        rows = 5
        cols = 6
        brick_width = 45
        brick_height = 20
        colors = ['#f44336', '#ff9800', '#ffeb3b', '#4caf50', '#2196f3']
        
        for row in range(rows):
            for col in range(cols):
                bricks.append({
                    'x': col * 50 + 5,
                    'y': row * 25 + 5,
                    'width': brick_width,
                    'height': brick_height,
                    'color': colors[row],
                    'active': True
                })
        return bricks
    
    def move_paddle(self, dx):
        """移动挡板"""
        self.paddle_x += dx
        # 边界检测
        if self.paddle_x < 0:
            self.paddle_x = 0
        if self.paddle_x > self.width - self.paddle_width:
            self.paddle_x = self.width - self.paddle_width
    
    def move_ball(self):
        """移动球"""
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy
        
        # 左右墙壁碰撞
        if self.ball_x - self.ball_r < 0 or self.ball_x + self.ball_r > self.width:
            self.ball_dx = -self.ball_dx
        
        # 顶部墙壁碰撞
        if self.ball_y - self.ball_r < 0:
            self.ball_dy = -self.ball_dy
        
        # 挡板碰撞
        if (self.ball_y + self.ball_r > self.paddle_y and
            self.ball_x > self.paddle_x and
            self.ball_x < self.paddle_x + self.paddle_width):
            self.ball_dy = -abs(self.ball_dy)
            # 根据击打位置改变角度
            hit_pos = (self.ball_x - self.paddle_x) / self.paddle_width
            self.ball_dx = (hit_pos - 0.5) * 10
        
        # 底部出界
        if self.ball_y - self.ball_r > self.height:
            self.running = False
            return False
        
        return True
    
    def check_brick_collision(self):
        """检查砖块碰撞"""
        for brick in self.bricks:
            if not brick['active']:
                continue
            
            if (self.ball_x + self.ball_r > brick['x'] and
                self.ball_x - self.ball_r < brick['x'] + brick['width'] and
                self.ball_y + self.ball_r > brick['y'] and
                self.ball_y - self.ball_r < brick['y'] + brick['height']):
                
                brick['active'] = False
                self.score += 10
                
                # 简单反弹
                self.ball_dy = -self.ball_dy
                return True
        
        return False
    
    def step(self):
        """游戏一步"""
        if not self.running:
            return
        
        if not self.move_ball():
            return
        
        self.check_brick_collision()
        
        # 检查是否所有砖块都被打掉
        if all(not brick['active'] for brick in self.bricks):
            self.bricks = self.create_bricks()
            self.score += 100  # 通关奖励
    
    def get_state(self):
        """获取游戏状态"""
        return {
            'ball_x': self.ball_x,
            'ball_y': self.ball_y,
            'ball_dx': self.ball_dx,
            'ball_dy': self.ball_dy,
            'paddle_x': self.paddle_x,
            'score': self.score,
            'running': self.running,
            'bricks': [{'x': b['x'], 'y': b['y'], 'w': b['width'], 'h': b['height'], 'c': b['color'], 'a': b['active']} for b in self.bricks]
        }


if __name__ == '__main__':
    game = BreakoutGame()
    print("打砖块游戏")
    print("按左右方向键移动挡板")
    
    while True:
        state = game.get_state()
        print(f"\n得分: {state['score']}")
        print(f"球位置: ({state['ball_x']:.0f}, {state['ball_y']:.0f})")
        print(f"挡板位置: {state['paddle_x']:.0f}")
        print(f"运行状态: {state['running']}")
        
        if not state['running']:
            cmd = input("输入命令 (s=开始, r=重置, q=退出): ").lower()
            if cmd == 's':
                game.running = True
            elif cmd == 'r':
                game.reset()
            elif cmd == 'q':
                break
        else:
            game.step()
            cmd = input("方向 (l=左, r=右, q=退出): ").lower()
            if cmd == 'l':
                game.move_paddle(-20)
            elif cmd == 'r':
                game.move_paddle(20)
            elif cmd == 'q':
                break
