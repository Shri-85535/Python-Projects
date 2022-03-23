from playwright.sync_api import sync_playwright, TimeoutError
from bs4 import BeautifulSoup
import openpyxl as openpyxl
import time
book = openpyxl.load_workbook('Leads.xlsx')
sheet = book.active
UDF_01_Answer = "Test String"
UDF_02_Answer = "Test String"
UDF_03_Answer = "Test String"
UDF_04_Answer = "Test String"
i = 2
num_of_records = int(input("How many records? "))

for a in range(num_of_records):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False, slow_mo=1000, timeout=0)
        page=browser.new_page()
        page.goto('https://***')
        FirstName = sheet[f'A{i}']
        LastName = sheet[f'B{i}']
        Email = sheet[f'C{i}']
        Phone = sheet[f'D{i}']
        Comp_name = sheet[f'E{i}']
        Dep = sheet[f'F{i}']
        Role = sheet[f'G{i}']
        Country = sheet[f'H{i}']
        Tagged_asset = sheet[f'I{i}']
        VID = sheet[f'J{i}']
        page.fill('input#C_FirstName', f'{FirstName.value}')
        page.fill('input#C_LastName', f'{LastName.value}')
        page.fill('input#C_EmailAddress', f'{Email.value}')
        page.fill('input#C_BusPhone', f'{Phone.value}')
        page.fill('input#C_Company', f'{Comp_name.value}')
        page.select_option("select", value=f'{Dep.value}')
        time.sleep(1)
        page.select_option("select#C_Job_Role11", label=f'Role.value', value=f'{Role.value}')
        page.select_option("select#C_Country", label=f'Country.value', value=f'{Country.value}')
        if UDF_01_Answer == Tagged_asset.value:
            page.select_option("select#UDF_01_Answer", value='Yes')
        else:
            page.select_option("select#UDF_01_Answer", value='No')
        if UDF_02_Answer == Tagged_asset.value:
            page.select_option("select#UDF_02_Answer", value='Yes')
        else:
            page.select_option("select#UDF_02_Answer", value='No')
        if UDF_03_Answer == Tagged_asset.value:
            page.select_option("select#UDF_03_Answer", value='Yes')
        else:
            page.select_option("select#UDF_03_Answer", value='No')
        if UDF_04_Answer == Tagged_asset.value:
            page.select_option("select#UDF_04_Answer", value='Yes')
        else:
            page.select_option("select#UDF_04_Answer", value='No')
        page.check('text=Notify me about products, services, and events.')
        #page.pause()
        page.locator("text=Continue").wait_for(timeout=0)
        page.click('text=Continue')
        #page.pause()
        page.is_visible('div.col-sm-12 text-muted')
        html = page.inner_html('#verificationId', timeout=0)
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        sheet.cell(row=i, column=10).value = soup.__str__()
        i+=1
book.save('Leads.xlsx')
