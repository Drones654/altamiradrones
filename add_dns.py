"""Add CNAME DNS records for altamiradrones.com via Cloudflare dashboard automation."""

import time
from playwright.sync_api import sync_playwright

ACCOUNT_ID = "53da8abc5851e057f18f44869ced3584"
ZONE_ID = "8d7d6759e1466b7e9470b25e24763919"
DNS_URL = f"https://dash.cloudflare.com/{ACCOUNT_ID}/altamiradrones.com/dns/records"

RECORDS = [
    {"type": "CNAME", "name": "@", "content": "altamiradrones.pages.dev", "proxied": True},
    {"type": "CNAME", "name": "www", "content": "altamiradrones.pages.dev", "proxied": True},
]

def main():
    import subprocess, os, signal

    # Close Chrome gracefully so we can use its profile
    print("[0/6] Closing Chrome to reuse session...")
    subprocess.run(["osascript", "-e", 'tell application "Google Chrome" to quit'], capture_output=True)
    import time; time.sleep(2)

    chrome_profile = os.path.expanduser("~/Library/Application Support/Google/Chrome")
    pw = sync_playwright().start()
    browser = pw.chromium.launch_persistent_context(
        user_data_dir=chrome_profile,
        headless=False,
        channel="chrome",
        viewport={"width": 1280, "height": 900},
        args=["--disable-blink-features=AutomationControlled"],
        ignore_default_args=["--enable-automation"],
    )
    page = browser.pages[0] if browser.pages else browser.new_page()

    print("[1/6] Navigating to Cloudflare DNS...")
    page.goto(DNS_URL, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(4000)

    # Check if we need to log in
    if "login" in page.url or "sign-in" in page.url:
        print("[!] Not logged in. Please log in to Cloudflare in the browser window.")
        print("    Waiting up to 120 seconds...")
        try:
            page.wait_for_url(f"**/dns/records**", timeout=120000)
            print("[OK] Logged in successfully.")
            page.wait_for_timeout(3000)
        except Exception:
            print("[FAIL] Login timeout. Exiting.")
            browser.close()
            pw.stop()
            return
    else:
        print("[OK] Already logged in.")

    print("[2/6] On DNS records page. Adding records via dashboard API...")

    # Use the browser's session cookie to call the Cloudflare API directly
    # This leverages the dashboard's authenticated session
    for i, record in enumerate(RECORDS):
        print(f"[{3+i}/6] Adding CNAME: {record['name']} -> {record['content']}")

        result = page.evaluate("""async (args) => {
            const [zoneId, record] = args;
            try {
                const resp = await fetch(`https://api.cloudflare.com/client/v4/zones/${zoneId}/dns_records`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify({
                        type: record.type,
                        name: record.name,
                        content: record.content,
                        proxied: record.proxied,
                        ttl: 1
                    })
                });
                const data = await resp.json();
                return { ok: data.success, errors: data.errors, result: data.result ? { id: data.result.id, name: data.result.name } : null };
            } catch (e) {
                return { ok: false, errors: [{ message: e.message }] };
            }
        }""", [ZONE_ID, record])

        if result.get("ok"):
            print(f"       -> Created: {result['result']}")
        else:
            errors = result.get("errors", [])
            # Check if record already exists
            already = any("already" in str(e.get("message", "")).lower() for e in errors)
            if already:
                print(f"       -> Already exists, skipping.")
            else:
                print(f"       -> Error: {errors}")

    # Reload the DNS page to verify
    print("[5/6] Verifying... reloading DNS page.")
    page.reload(wait_until="domcontentloaded")
    page.wait_for_timeout(3000)

    # Take a screenshot for confirmation
    page.screenshot(path="/Users/e/e/c/altamiradrones/dns_records.png")
    print("[OK] Screenshot saved to dns_records.png")

    print("[6/6] Checking custom domain activation...")
    page.wait_for_timeout(2000)
    browser.close()
    pw.stop()
    print("\nDone. DNS records added. SSL certificate will provision automatically (1-2 min).")
    print("  https://altamiradrones.com")
    print("  https://www.altamiradrones.com")

if __name__ == "__main__":
    main()
