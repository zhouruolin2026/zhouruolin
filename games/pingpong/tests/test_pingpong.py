"""
乒乓球游戏 Selenium 自动化测试
"""
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    """创建浏览器驱动"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def game_url(driver):
    """游戏页面 URL"""
    return "file:///Users/njh/.qclaw/workspace/games/pingpong/index.html"


class TestPingpongGame:
    """测试乒乓球游戏"""
    
    def test_page_loads(self, driver, game_url):
        """测试页面加载"""
        driver.get(game_url)
        assert "乒乓球" in driver.title
    
    def test_canvas_exists(self, driver, game_url):
        """测试画布存在"""
        driver.get(game_url)
        canvas = driver.find_element(By.TAG_NAME, "canvas")
        assert canvas is not None
    
    def test_start_button_exists(self, driver, game_url):
        """测试开始按钮存在"""
        driver.get(game_url)
        start_btn = driver.find_element(By.ID, "gameBtn")
        assert start_btn.text == "开始"
    
    def test_click_start_button(self, driver, game_url):
        """测试点击开始按钮"""
        driver.get(game_url)
        start_btn = driver.find_element(By.ID, "gameBtn")
        start_btn.click()
        # 按钮应该变成"暂停"
        assert start_btn.text == "暂停"
    
    def test_click_pause_button(self, driver, game_url):
        """测试点击暂停按钮"""
        driver.get(game_url)
        # 先开始
        start_btn = driver.find_element(By.ID, "gameBtn")
        start_btn.click()
        time.sleep(0.5)
        # 再暂停
        start_btn.click()
        # 按钮应该变成"继续"
        assert start_btn.text == "继续"
    
    def test_click_resume_button(self, driver, game_url):
        """测试点击继续按钮"""
        driver.get(game_url)
        start_btn = driver.find_element(By.ID, "gameBtn")
        # 开始
        start_btn.click()
        time.sleep(0.5)
        # 暂停
        start_btn.click()
        time.sleep(0.5)
        # 继续
        start_btn.click()
        # 按钮应该变回"暂停"
        assert start_btn.text == "暂停"
    
    def test_restart_button_exists(self, driver, game_url):
        """测试重置按钮存在"""
        driver.get(game_url)
        restart_btn = driver.find_element(By.XPATH, "//button[contains(text(),'重置')]")
        assert restart_btn is not None
    
    def test_click_restart_button(self, driver, game_url):
        """测试点击重置按钮"""
        driver.get(game_url)
        restart_btn = driver.find_element(By.XPATH, "//button[contains(text(),'重置')]")
        
        # 先开始游戏
        start_btn = driver.find_element(By.ID, "gameBtn")
        start_btn.click()
        time.sleep(0.5)
        
        # 重置
        restart_btn.click()
        time.sleep(0.3)
        
        # 开始按钮应该变回"开始"
        start_btn = driver.find_element(By.ID, "gameBtn")
        assert start_btn.text == "开始"
    
    def test_keyboard_controls(self, driver, game_url):
        """测试键盘控制"""
        driver.get(game_url)
        
        # 按空格开始
        driver.find_element(By.TAG_NAME, "body").send_keys(" ")
        time.sleep(0.3)
        
        start_btn = driver.find_element(By.ID, "gameBtn")
        assert start_btn.text == "暂停"

    def test_restart_resets_runtime_state(self, driver, game_url):
        """测试重置后关键运行状态被恢复"""
        driver.get(game_url)
        start_btn = driver.find_element(By.ID, "gameBtn")
        start_btn.click()
        time.sleep(0.3)

        restart_btn = driver.find_element(By.XPATH, "//button[contains(text(),'重置')]")
        restart_btn.click()
        time.sleep(0.3)

        state = driver.execute_script("return {running, paused, x, y, score}")
        assert state["running"] == 0
        assert state["paused"] == 0
        assert state["x"] == 150
        assert state["y"] == 200
        assert state["score"] == 0
