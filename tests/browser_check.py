from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent.parent
SCREENSHOTS = ROOT / "tests" / "screenshots"
SCREENSHOTS.mkdir(parents=True, exist_ok=True)


def check_page(page, name: str) -> None:
    runtime_errors = []
    page.on("pageerror", lambda error: runtime_errors.append(str(error)))
    page.goto("http://127.0.0.1:4173", wait_until="networkidle")
    page.locator("#service-grid .service-card").first.wait_for()

    assert page.locator("#service-grid .service-card").count() == 7
    assert page.locator("#legal .document-card").count() == 2
    assert page.locator("h1").inner_text() == "讓自己成為最溫暖的陽光"
    assert page.evaluate(
        "document.documentElement.scrollWidth <= document.documentElement.clientWidth"
    ), f"Horizontal overflow detected on {name}"

    images = page.locator("img")
    for index in range(images.count()):
        images.nth(index).scroll_into_view_if_needed()
        page.wait_for_timeout(80)
    failed_images = page.locator("img").evaluate_all(
        "images => images.filter(image => !image.complete || image.naturalWidth === 0)"
        ".map(image => image.getAttribute('src'))"
    )
    assert not failed_images, f"Images failed to load on {name}: {failed_images}"

    if name == "desktop":
        page.get_by_role("button", name="EN").click()
        assert page.locator("h1").inner_text() == "Be the Sunshine That Warms Every Heart."
        assert page.locator("footer").inner_text().count(
            "Buddhist Tzuen Children’s Welfare Foundation"
        ) == 1
        assert page.locator("#service-grid .service-card").count() == 7
        page.reload(wait_until="networkidle")
        assert page.locator("h1").inner_text() == "Be the Sunshine That Warms Every Heart."
        page.get_by_role("button", name="中文").click()
    else:
        menu = page.locator(".menu-button")
        menu.click()
        assert menu.get_attribute("aria-expanded") == "true"
        assert page.locator("#site-nav").evaluate(
            "element => element.classList.contains('is-open')"
        )
        page.locator("#site-nav a").first.click()
        assert menu.get_attribute("aria-expanded") == "false"

    page.screenshot(path=str(SCREENSHOTS / f"tzuen-{name}.png"), full_page=True)
    assert not runtime_errors, f"Runtime errors on {name}: {runtime_errors}"


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    desktop = browser.new_page(viewport={"width": 1440, "height": 1000})
    check_page(desktop, "desktop")
    desktop.close()

    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    check_page(mobile, "mobile")
    mobile.close()
    browser.close()

print("Browser checks passed for desktop and mobile.")
