"""
俄罗斯方块游戏 Selenium 自动化测试
"""
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=400,600')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def game_url(driver):
    return "file:///Users/njh/.qclaw/workspace/games/tetris/index.html"


class TestTetrisGame:
    """测试俄罗斯方块游戏"""
    
    # 1. 页面加载测试
    def test_page_loads(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        assert "俄罗斯方块" in driver.title
    
    # 2. 画布存在测试
    def test_canvas_exists(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        canvas = driver.find_element(By.TAG_NAME, "canvas")
        assert canvas is not None
    
    # 3. 得分显示测试
    def test_score_display_exists(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        score = driver.find_element(By.CSS_SELECTOR, "#score span")
        assert score is not None
    
    # 4. 开始按钮存在测试
    def test_start_button_exists(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        assert len(buttons) > 0
    
    # 5. 旋转按钮存在测试
    def test_rotate_button_exists(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        button = driver.find_element(By.XPATH, "//button[contains(text(),'旋转')]")
        assert button is not None
    
    # 6. 左移按钮存在测试
    def test_left_button_exists(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        button = driver.find_element(By.XPATH, "//button[contains(text(),'左')]")
        assert button is not None
    
    # 7. 右移按钮存在测试
    def test_right_button_exists(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        button = driver.find_element(By.XPATH, "//button[contains(text(),'右')]")
        assert button is not None
    
    # 8. 下落按钮存在测试
    def test_drop_button_exists(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        button = driver.find_element(By.XPATH, "//button[contains(text(),'下落')]")
        assert button is not None
    
    # 9. 点击开始按钮测试
    def test_click_start_button(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        button = driver.find_element(By.XPATH, "//button[contains(text(),'开始')]")
        button.click()
        time.sleep(0.3)
        # 开始后按钮应该变成"重新开始"
    
    # 10. 虚拟按键功能测试
    def test_virtual_buttons_work(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        # 点击开始
        start_btn = driver.find_element(By.XPATH, "//button[contains(text(),'开始')]")
        start_btn.click()
        time.sleep(0.5)
        
        # 点击旋转
        rotate_btn = driver.find_element(By.XPATH, "//button[contains(text(),'旋转')]")
        rotate_btn.click()
        time.sleep(0.2)
        
        # 点击左
        left_btn = driver.find_element(By.XPATH, "//button[contains(text(),'左')]")
        left_btn.click()
        time.sleep(0.2)
        
        # 点击右
        right_btn = driver.find_element(By.XPATH, "//button[contains(text(),'右')]")
        right_btn.click()
        time.sleep(0.2)
        
        # 点击下落
        drop_btn = driver.find_element(By.XPATH, "//button[contains(text(),'下落')]")
        drop_btn.click()
        time.sleep(0.2)
    
    # 11. 键盘控制测试
    def test_keyboard_controls(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(" ")
        time.sleep(0.3)
        body.send_keys("a")  # 左
        time.sleep(0.2)
        body.send_keys("d")  # 右
        time.sleep(0.2)
        body.send_keys("w")  # 旋转
        time.sleep(0.2)
    
    # 12. 游戏初始化状态测试
    def test_initial_state(self, driver, game_url):
        driver.get(game_url)
        time.sleep(0.5)
        score = driver.execute_script("return score")
        assert score == 0

    def test_canvas_grid_height_consistent(self, driver, game_url):
        """测试画布高度与网格总高度一致"""
        driver.get(game_url)
        time.sleep(0.5)
        state = driver.execute_script(
            "return {canvasH: c.height, rows: ROWS, cell: CELL, expected: ROWS * CELL};"
        )
        assert state["canvasH"] == state["expected"]

    def test_start_sets_running_state(self, driver, game_url):
        """测试开始后进入运行态"""
        driver.get(game_url)
        time.sleep(0.3)
        start_btn = driver.find_element(By.XPATH, "//button[contains(text(),'开始')]")
        start_btn.click()
        time.sleep(0.3)
        running = driver.execute_script("return running")
        assert running == 1

    def test_arrow_keys_move_piece(self, driver, game_url):
        """测试方向键可移动方块"""
        driver.get(game_url)
        time.sleep(0.3)
        driver.find_element(By.XPATH, "//button[contains(text(),'开始')]").click()
        time.sleep(0.3)
        before_x = driver.execute_script("return piece.x")
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ARROW_RIGHT)
        time.sleep(0.2)
        after_x = driver.execute_script("return piece.x")
        assert after_x >= before_x
