from playwright.sync_api import sync_playwright, TimeoutError
from datetime import datetime, date, timedelta
import time
import copy
import pyperclip
today = date.today()
start_date = today.strftime("%Y-%m-1")
with sync_playwright() as sync:
    browser = sync.chromium.launch(channel='chrome', headless=False, slow_mo=50, timeout=0)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.set_default_timeout(0)
    page.goto('https://teamob.zdpm.us/bi_report/dashboard', timeout=0)
    page.fill('input#IndexUsername', '')
    page.fill('input#IndexPassword', '')
    #page.pause()
    #page.check('input[value="1"]')
    page.click('text=Remember me')    
    page.click('button[type=button]')
    page.goto('https://teamob.zdpm.us/bi_report/dashboard')
    time.sleep(1)
    page.click('input#date_range_bi')
    print("Waiting for Page to load...")
    page.click('text=This month')
    time.sleep(60)
    #page.click('text=Yesterday')
    #col-sm-6 col-md-6 col-xs-12 col-lg-6 custom_field_104
    for i in range(7):
        page.locator(f":nth-match(:text('Export'), {i})")
        print(f'Locator {i} found!')
    with page.expect_download(timeout=0) as download_info:
        page.locator(":nth-match(:text('Export'), 3)").click()
    download = download_info.value
    path = download.path()
    download.save_as('TeamOB_Performance.csv')
    print("TeamOB_Performance File saved")
    print("Plese wait while downloading Incident Report...")
    #page.goto('https://teamob.zdpm.us/timesheets/app_incidents')
    
    page.goto('https://teamob.zdpm.us/timesheets/app_incidents')
    page.locator("input#TimesheetFromdate").click()
    time.sleep(1)
    #page.click("td.day >> nth = 0")
    #page.click("td[text='1']")
    #page.dispatch_event("")
    pyperclip.copy(start_date)
    page.keyboard.press("Control+KeyV")
    time.sleep(1)
    page.locator("button#btn_go")
    page.click("button#btn_go")
    page.is_visible('div.btn-toolbar pull-right   hidden-print')
    #page.locator('text=Actions').wait_for(timeout=0)
    time.sleep(1)
    page.click('text=Actions')
    #page.locator('text=Export')
    #page.click('text=Export')
    time.sleep(1)
    with page.expect_download(timeout=0) as download_info:
        page.locator('text=Export').click()
    download = download_info.value
    path = download.path()
    download.save_as('TeamOB_Incident.csv')
    print("TeamOB_Incident File saved")
    page.pause()
