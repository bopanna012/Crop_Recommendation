from playwright.sync_api import sync_playwright

URL = "http://localhost:8501"
SHOT = "streamlit_screenshot.png"
TIMEOUT = 60000

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL, timeout=TIMEOUT)
    # Allow app JS to render
    page.wait_for_timeout(2000)
    found = False
    try:
        # look for part of the title text
        page.wait_for_selector("text=Smart Crop Recommendation", timeout=10000)
        found = True
    except Exception:
        found = False
    page.screenshot(path=SHOT, full_page=True)
    print(f"SCREENSHOT:{SHOT}")
    print(f"FOUND_TEXT:{found}")
    browser.close()