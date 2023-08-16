# Class for scraping ebay
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from ebay_scraper.ebay_report import EbayReport

test_listings = [
    "Dean & Tyler Patch Collar Nylon Collar with Removable Patches",
    "Dog Shocker Collar Large Medium Small Mode Ultrasonic Electric Training G5 ✅",
    "Touchdog Caliber Pet Dog Leash and Collar Brown Small",
    "Nite Ize NiteHowl LED Mini Dog Collar Rechargeable Size Small Free S&H",
    "Nightmare Before Christmas ZERO, Dog Collar",
    "SportDOG 100 Yard Trainer Stubborn Dog Remote Collar Yard Training YT-100S New",
    "Vsezund GE-G21 Remote Control Rechargeable Waterproof Dog Training Collar",
    "Aweec Wireless Dog Fence 2-in-1 Remote Training Collar System",
    "SportDOG 100 Yard Trainer Stubborn Dog Remote Collar Yard Training YT-100S",
]


class Ebay(webdriver.Chrome):
    # Constructor Function
    # if using mac set driver_path=r"./chromedriver_mac64"
    # if using windows set driver_path=r"./chromedriver_win32"
    def __init__(self, driver_path=r"./chromedriver_win32"):
        self.driver_path = driver_path
        os.environ["PATH"] = self.driver_path
        super(Ebay, self).__init__()
        self.implicitly_wait(15)

    # Launching Function
    def launch(self, url):
        self.get(url)

    # Display categories that can be searched for
    def display_categories(self):
        category_selector = self.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat")
        category_elements = category_selector.find_elements(By.TAG_NAME, "option")
        categories = []
        for cat in category_elements:
            categories.append(cat.get_attribute("innerHTML").strip())
        print(categories)

    """
    # Search Function
    This function allows a user to search for a specific category
    While the function automatically applies specific filters to ensure 
    correct results
    """

    def search(self, category="Sporting Goods", keywords="Dog Collars"):
        # Choosing category
        # This block selects a specific category
        """
        category = category.lower().title()
        category_select = self.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat")
        category_select.click()
        category_el = category_select.find_element(
            By.CSS_SELECTOR, f'option[text="{category}"]'
        )
        category_el.click()
        """

        # Enter keywords in search
        keyword_el = self.find_element(By.ID, "_nkw")
        keyword_el.send_keys(keywords)

        # Under Section "Search Including"
        # Select "Sold Items"
        # This will automatically click Completed items
        sold_items_el = self.find_element(By.ID, "s0-1-17-5[1]-[2]-LH_Sold")
        sold_items_el.click()

        """
        # Selecting only new items
        new_items_el = self.find_element(By.ID, "s0-1-17-6[4]-[0]-LH_ItemCondition")
        new_items_el.click()
        """

        # Sort by list view
        # And show 240 results per page
        view_select_el = self.find_element(By.ID, "s0-1-17-8[9]-1[1]-_dmd")
        view_select_el.click()
        list_el = view_select_el.find_element(
            By.CSS_SELECTOR, 'option[text="List View"]'
        )
        list_el.click()

        num_results = self.find_element(By.ID, "s0-1-17-8[9]-1[2]-_ipg")
        num_results.click()
        num_240 = num_results.find_element(By.CSS_SELECTOR, 'option[text="240"]')
        num_240.click()

        # Search button
        # Starts search for listings
        search_btn = self.find_element(
            By.CSS_SELECTOR, 'button[_sp="p4433449.m150127.l158973"]'
        )

        search_btn.click()

    # Select subcategory function
    def select_subcategory(self):
        pass

    # get report
    def get_report(self, keywords):
        listings = []
        for _ in range(10):
            listing_box_el = self.find_element(By.ID, "srp-river-results")
            listings += EbayReport(listing_box_el).get_listings()
            next_btn = self.find_element(
                By.CSS_SELECTOR, 'a[aria-label="Go to next search page"]'
            )
            next_btn.click()

        report = EbayReport.create_unique_listings(listings)
        EbayReport.create_sheet(report, keywords)

    """
        total = 0
        highest = 0
        for key, value in report.items():
            print(key, ": \t", value)
            print("\n")
            total += value

            if value > highest:
                highest = value

        print(total)
        print(highest)
    """

    # this is a simple tester method
    def test(self):
        report = EbayReport.create_unique_listings(test_listings)

        total = 0
        highest = 0
        for key, value in report.items():
            print(key, ": \t", value)
            print("\n")
            total += value

            if value > highest:
                highest = value

        print(total)
        print(highest)
