from playwright.async_api import async_playwright
import json
import asyncio
from datetime import date
from pathlib import Path
import os
from dateutil.relativedelta import relativedelta as delta

folder = Path(__file__).resolve().parent
creds = folder / "creds.txt"
qldt = folder / "qldt"
slink = folder / "slink"


def enter_creds():
    usr = input("Enter QLDT username: ") 
    pwd = input("Enter QLDT password: ")    # pass

    with open(creds,"w") as f:
        f.write(f"{usr}\n{pwd}\n")

async def get_api():

    # Auth
    usr,pwd = "",""
    while True:
        try:
            usr,pwd = open(creds,"r").read().split("\n")
            break
        except Exception as error:
            print("Error, re-enter credentials", error)
            enter_creds()




    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=True,timeout=None)
        page = await browser.new_page()

        # QLDT
        try:
            print("QLDT: Fetching...")

            await page.goto("https://qldt.ptit.edu.vn")

            #log in & expect calendar API
            async with page.expect_response("**/api/sch/w-locdstkbtuanusertheohocky") as response:
                await page.locator('input[name="username"]').fill(usr)
                await page.locator('input[name="password"]').fill(pwd)
                await page.get_by_role("button",name="Đăng nhập",exact=True).click()

            #parse api
            calendar_api = await response.value
            calendar_data = await calendar_api.json()

            #write onto calendar_data.json
            calendar_json = json.dumps(calendar_data)
            with open(qldt/"qldt_calendar.json","w") as f:
                f.write(str(calendar_json))
            
            print("QLDT fetched successfully.")
        except Exception as error:
            print("QLDT failed to fetch:", error)


        await browser.close()

def main():
    try:
        if not os.path.exists(qldt):
            os.mkdir(qldt)
        if creds.exists() == False:
            enter_creds()
        asyncio.run(get_api())
        return "extraction success"
    except Exception as error:
        return f"extraction failed: {error}"
    
if __name__ == "__main__":
    main()
    print("Works")