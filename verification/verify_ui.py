from playwright.sync_api import sync_playwright, expect
import time
import os

def verify_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            # Wait for server to start
            print("Waiting for server...")
            time.sleep(15)
            print("Navigating...")
            page.goto("http://localhost:5173")

            # Check for new buttons
            print("Checking buttons...")
            expect(page.get_by_text("Noise", exact=True)).to_be_visible()
            expect(page.get_by_text("Crowd", exact=True)).to_be_visible()
            expect(page.get_by_text("Water Leak", exact=True)).to_be_visible()
            expect(page.get_by_text("Accessibility", exact=True)).to_be_visible()

            # Click one to see if it navigates
            print("Clicking Noise button...")
            page.get_by_text("Noise", exact=True).click()
            expect(page).to_have_url("http://localhost:5173/noise")
            expect(page.get_by_role("heading", name="Noise Detector")).to_be_visible()

            # Screenshot
            if not os.path.exists("verification"):
                os.makedirs("verification")
            page.screenshot(path="verification/ui_verification.png")
            print("UI Verified Successfully")

        except Exception as e:
            print(f"UI Verification Failed: {e}")
            if not os.path.exists("verification"):
                os.makedirs("verification")
            page.screenshot(path="verification/ui_failure.png")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_ui()
