from playwright.sync_api import sync_playwright, TimeoutError
from bs4 import BeautifulSoup
import openpyxl as openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
with sync_playwright()as p:
    browser = p.chromium.launch(headless=True, slow_mo=50, timeout=0)
    page = browser.new_page()
    print("Opening Browser...")
    print("Redirecting to Partner Portal!")
    page.goto('')
    page.fill('input#login__email', '')
    page.fill('input#login__password', '')
    page.click('button[type=submit]')
    print("Logged In...")
    page.locator("text=My Programs").wait_for(timeout=0)
    print("Extracting labels...")
    page.select_option("select", label="All")
#    new_selector = 'id=name-fruit'
#    page.wait_for_selector(new_selector)
#    handle = page.query_selector(new_selector)
    html = page.inner_html('#app', timeout=0)
    soup = BeautifulSoup(html, 'html.parser')
    print("parsing..")
    print("Please wait..")

    total_href = page.eval_on_selector_all("a[href^='/out-task/program-partners/']","elements => elements.map(element => element.href)")
    i=1
    for s in total_href:
        page.goto(s)
        page.locator("text=Delivery Schedule").wait_for(timeout=0)
        html = page.inner_html('#app', timeout=0)
        i_soup = BeautifulSoup(html, 'html.parser')
        CID = BeautifulSoup(html, 'html.parser').find('span', {'class': 'text-info'}).text.strip()
        Campaign_ID = CID[1:9]
        Campaign_ID.__str__()
    #    print("",Campaign_ID)

        Lead_Result = []
        Lead_Status = ['Submitted', 'Pending Review', 'Accepted', 'Upload Errors', 'Rejections', 'Returns']
        for a in i_soup.find_all('h1', {'class': 'mb-2'}):
            b = a.text.strip()
            Lead_Result.append(b)
        Final_status = dict(zip(Lead_Status,Lead_Result))
    #    print(Final_status)
        sheet.cell(row=i+1, column=1).value = (Campaign_ID, Final_status.__str__()).__str__()
        i = i+1
wb.save('NameFile.xlsx')
print("File Saved")
