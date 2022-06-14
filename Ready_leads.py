from playwright.sync_api import sync_playwright, TimeoutError
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
today = date.today()+timedelta(1)
past = (date.today()-timedelta(days=120))
end_date = today.strftime("%b %d, %Y")
start_date = past.strftime("%b %d, %Y")
uname = ''
pwd = ''
with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True, slow_mo=50, timeout=0)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
#    uname = input("Enter Username: ")
#    pwd = input("Enter Password: ")
    page.goto('https://leadgen.zifftech.com/reporting/LeadCap.aspx')
    page.fill('input#ctl00_m_UserName', uname)
    page.fill('input#ctl00_m_Password', pwd)
    page.dispatch_event("input#ctl00_m_LoginButton", "click")
    page.click('span[class=multiselect-selected-text]')
    #page.uncheck('input[value="7"]')
    page.check('input[value="9"]')
    page.click('text=Campaign Type')
    page.select_option("select#ctl00_m_ddlStatus", value='0')
    #page.select_option("select#ddlAgency", value='9996')
    page.select_option("select#ddlAgency", value='0')
    page.click('text=None selected')
    page.check('input[value="all"]')
    page.fill('input#ctl00_m_txtStartDate', start_date)
    page.fill('input#ctl00_m_txtEndDate', end_date)
    page.check('input#ctl00_m_chkIncludeLeadGroupsInExport')
    #page.click('input[value="Run"]')
    with page.expect_download() as download_info:
        page.click('text=Export to CSV')
    download = download_info.value
    path = download.path()
    download.save_as('RTD.xlsx')
print("Saved")    
