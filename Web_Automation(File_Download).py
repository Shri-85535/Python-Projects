from playwright.sync_api import sync_playwright, TimeoutError
from bs4 import BeautifulSoup
import time
uname = '****'
pwd = '****'
camps = int(input("Number of Campaigns: "))
camps1  = camps
pages = 0
while camps1 > 0:
    pages+= 1
    camps1-= 100
print(f"Total {pages} Pages!")
total_href = []
with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False, slow_mo=500, timeout=0)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    #page.set_viewport_size({"width": 1200, "height": 650})
    page.goto('https://xxx')
    page.click('button#consent-accept')
    page.fill('input#username', uname)
    time.sleep(0.50)
    page.click('text=Next')
    page.fill('input#password', pwd)
    time.sleep(0.50)
    page.click('span[class=mat-button-wrapper]')
    MFA = str(input("Enter Code: "))
    page.fill('input#mfa_code', MFA)
    #page.pause()
    print("Logged In")
    page.click('span[class=mat-button-wrapper]')
    page.click('text=View')
    page.dispatch_event("mat-select#mat-select-2", "click")
    time.sleep(0.50)
    page.dispatch_event("mat-option#mat-option-7", "click")
    #page.click('path[d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"]')
    print("Extracting Links")
    #page.keyboard.press("Control+Alt+ArrowRight")
    #page.pause()
    for i in range(pages-1):
        time.sleep(10)
        html = page.inner_html('.cvtr-theme1', timeout=0)
        soup = BeautifulSoup(html, 'html.parser')
        hrefs = page.eval_on_selector_all("a[href^='https://xxx/']","elements => elements.map(element => element.href)")
        for links in hrefs:
            l = links.strip()
            total_href.append(l)
        page.click('path[d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"]', timeout=0)
        i = 1
    for h in hrefs:
        
        #time.sleep(3)
        if i == 1:
            page.goto(h)
            #page.dispatch_event("div.walkme-action-openMenu-0 wm-blue-btn wm-template-main-bg wm-main-border-bottom-darker wm-action-text-color wm-main-bg-hover", "click")
            #page.dispatch_event('text=VIEW', "click")
            #page.click('div[class="wm-close-button walkme-x-button]', timeout=2000)
            #page.dispatch_event('div[class="wm-close-button walkme-x-button"]', "click", timeout=0)
            
            page.keyboard.press("Escape")
            i -= 1
        page.goto(h)
        time.sleep(0.50)
        #page.click('text=VIEW', timeout=200, force=False)
        #page.dispatch_event("input#campaign_leads_export_filter_5", "click")
        page.check('input#campaign_leads_export_filter_5', timeout=0)
        page.dispatch_event("button#export_leads_terms_modal", "click")
        page.check('input#campaign_leads_export_acceptTerms', timeout=0)
        page.click('text="Export Leads"')
        time.sleep(2.5)
        page.goto('https://xxx')
        time.sleep(2.5)
        page.click('text="Download"')
        page.check('input#export-download-acceptTerms', timeout=0)
        with page.expect_download() as download_info:        
            page.click('a#exportDownloadLink')
        download = download_info.value
        path = download.path()
        download.save_as(download.suggested_filename)
        print(f'Please wait...', end="\r")
