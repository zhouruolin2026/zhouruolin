"""
跳跳鸟游戏 Selenium 自动化测试
"""
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """创建浏览器驱动"""
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
    """游戏页面 URL"""
    return "file:///Users/njh/.qclaw/workspace/games/flappy/index.html"


class TestFlappyBirdGame:
    """测试跳跳鸟游戏"""
    
    def test_page_loads(self, driver, game_url):
        """测试页面加载"""
        driver.get(game_url)
        time.sleep(0.5)
        assert "跳跳鸟" in driver.title
    
    def test_canvas_exists(self, driver, game_url):
        """测试画布存在"""
        driver.get(game_url)
        time.sleep(0.5)
        canvas = driver.find_element(By.TAG_NAME, "canvas")
        assert canvas is not None
    
    def test_button_exists(self, driver, game_url):
        """测试按钮存在"""
        driver.get(game_url)
        time.sleep(1)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        assert len(buttons) > 0
    
    def test_button_has_id(self, driver, game_url):
        """测试按钮有正确的ID"""
        driver.get(game_url)
        time.sleep(1)
        button = driver.find_element(By.ID, "startBtn")
        assert button is not None
    
    def test_initial_button_text(self, driver, game_url):
        """测试初始按钮文字"""
        driver.get(game_url)
        time.sleep(1)
        button = driver.find_element(By.ID, "startBtn")
        text = button.text
        # 初始应该是"开始"
        assert text == "开始" or text == "重新开始"
