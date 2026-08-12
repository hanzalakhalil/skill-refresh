"""
Selenium Refresher — locators + waits
=======================================
Uses two public, made-for-testing pages, so nothing here scrapes
a real site or breaks anyone's ToS.

Setup (run in your activated venv):
    pip install selenium webdriver-manager
    python selenium_exercises.py

webdriver-manager auto-downloads the right ChromeDriver version,
so you don't need to manage driver binaries by hand.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


# ---------------------------------------------------------------
# PART 1 — LOCATORS
# Page: Selenium's own test form (built for exactly this purpose)
# ---------------------------------------------------------------
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# TODO 1.1: Find the text input by its `name` attribute ("my-text")
# and type "hello world" into it.
# text_input = driver.find_element(By.NAME, "my-text")
# text_input.send_keys("hello world")

text_input = driver.find_element(By.NAME, "my-text")
text_input.send_keys("hello  world")


# TODO 1.2: Find the dropdown (By.NAME, "my-select") and select
# the option with visible text "Two".
# Hint: from selenium.webdriver.support.ui import Select
# dropdown = ...
# Select(dropdown).select_by_visible_text("Two")
dropdown = driver.find_element(By.NAME, "my-select")
Select(dropdown).select_by_visible_text("Two")

# TODO 1.3: Find the checkbox by CSS selector (input[name='my-check'])
# and click it.
# checkbox = ...
checkbox = driver.find_elements(By.CSS_SELECTOR, "input[name='my-check']")
checkbox[0].click()
checkbox[1].click()

# TODO 1.4: Find the submit button by its CSS selector
# (button[type='submit']) — don't click yet, just locate it and
# print its visible text.
# submit_btn = ...
# print(submit_btn.text)

submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print(submit_btn.text)


# ---------------------------------------------------------------
# PART 2 — EXPLICIT WAITS
# Page: the-internet's dynamic loading example (content appears
# after a delay — classic case where waits matter)
# ---------------------------------------------------------------
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# TODO 2.1: Click the "Start" button (By.CSS_SELECTOR, "#start button")
driver.find_element(By.CSS_SELECTOR,"#start button").click()

# TODO 2.2: The text only appears after ~5 seconds and the element
# is hidden until then. Use WebDriverWait + expected_conditions to
# wait until the element with id="finish" is VISIBLE, then print
# its text. This is the core skill — no time.sleep() allowed.
# finish_text = wait.until(
#     EC.visibility_of_element_located((By.ID, "finish"))
# )
# print(finish_text.text)

finish_text = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
print(finish_text.text)


# ---------------------------------------------------------------
# PART 3 — STRETCH: dynamic_loading/2 is trickier — the element
# EXISTS in the DOM the whole time but is only *populated* after
# the delay, which behaves differently. Try adapting your wait
# condition and see what breaks if you reuse the same approach.
# ---------------------------------------------------------------
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.find_element(By.CSS_SELECTOR,"#start button").click()

finish2_text = wait.until(EC.presence_of_element_located((By.ID, "finish")))
print(finish2_text.text)


driver.quit()
