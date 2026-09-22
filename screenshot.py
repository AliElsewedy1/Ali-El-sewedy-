from playwright.sync_api import Page, expect, sync_playwright

def verify_navbar(page: Page):
    page.goto("http://localhost:8080")
    # Wait for the header to be visible
    page.wait_for_selector(".dynamic-header")

    # Wait a tiny bit for render
    page.wait_for_timeout(1000)

    # Screenshot the initial wide state
    page.screenshot(path="unscrolled_1200.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Set a wide viewport to test desktop media queries
        page = browser.new_page(viewport={"width": 1600, "height": 900})
        try:
            verify_navbar(page)
        finally:
            browser.close()
