from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Function to wait for an element to be clickable
def wait_for_element(driver, by, value, timeout=10):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

# Launching the browser
driver = webdriver.Chrome()

# Maximizing the browser window
driver.maximize_window()

# Navigating to YouTube
driver.get("https://www.youtube.com")

# Feature 1: Searching for a video
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Conestoga Waterloo")
search_box.send_keys(Keys.RETURN)
time.sleep(8)  # Wait for search results to load

# Feature 2: Clicking on the first video
first_video = wait_for_element(driver, By.CSS_SELECTOR, "#contents ytd-video-renderer")
first_video.click()
time.sleep(8)  # Wait for video to load

# Feature 3: Pausing the video
video_player = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
video_player.click()
time.sleep(5)  # Wait for the video to pause

# Feature 4: Seeking the video
video_player.click()  # Resume video
time.sleep(5)  # Wait for the video to play
seek_bar = driver.find_element(By.CSS_SELECTOR, ".ytp-scrubber-container")
webdriver.ActionChains(driver).click_and_hold(seek_bar).move_by_offset(50, 0).release().perform()
time.sleep(8)  # Wait for the seek operation

# Feature 6: Liking the video
like_button = driver.find_element(By.CSS_SELECTOR, ".ytd-toggle-button-renderer")
like_button.click()
time.sleep(8)  # Wait for like to register

# Feature 7: Disliking the video
dislike_button = driver.find_element(By.CSS_SELECTOR, ".ytd-toggle-button-renderer")
dislike_button.click()
time.sleep(8)  # Wait for dislike to register

# Feature 8: Subscribing to the channel
subscribe_button = driver.find_element(By.CSS_SELECTOR, ".ytd-subscribe-button-renderer")
subscribe_button.click()
time.sleep(8)  # Wait for subscription to register

# Feature 9: Navigating to the home page
home_button = driver.find_element(By.CSS_SELECTOR, "#logo-icon-container")
home_button.click()
time.sleep(8)  # Wait for home page to load

# Feature 10: Checking trending videos
trending_button = driver.find_element(By.CSS_SELECTOR, "#endpoint[title='Trending']")
trending_button.click()
time.sleep(8)  # Wait for trending page to load

# Closing the browser
driver.quit()