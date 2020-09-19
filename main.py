from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

class Bot:
    def __init__(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver = Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.last_post = None

    def login(self):
        self.driver.get('https://facebook.com')
        sleep(1)
        email_input = self.driver.find_element_by_css_selector('input#email')
        password_input = self.driver.find_element_by_css_selector('input#pass')
        email_input.send_keys('trd.ayoub2004@gmail.com')
        password_input.send_keys('ayoubtrd0.')
        password_input.send_keys(Keys.RETURN)
        sleep(4)

    def watch(self, page_url, callback):
        self.driver.get(page_url)
        sleep(3)
        try:
            current_post = self.driver.find_element_by_css_selector('[role="article"] .rq0escxv.l9j0dhe7.du4w35lb.hybvsw6c.ue3kfks5.pw54ja7n.uo3d90p7.l82x9zwi.ni8dbmo4.stjgntxs.k4urcfbm.sbcfpzgs')
        except:
            current_post = self.driver.find_element_by_css_selector('blockquote')

        current_post = current_post.get_attribute('textContent')
        print(self.last_post)
        print(current_post)
        if self.last_post is None or self.last_post == current_post:
            self.last_post = current_post

        else:
            callback()
            self.last_post = current_post
        sleep(8)
        self.watch(page_url, callback)

    def share_post(self, contacts):
        print('sharing post')
        sleep(1)
        #share_btn = self.driver.find_element_by_css_selector('[aria-label="Send this to friends or post it on your timeline."]')
        #share_btn.click()
        self.driver.execute_script("""
            document.querySelector('[aria-label="Send this to friends or post it on your timeline."]').click()
        """)
        sleep(4)
        #share = self.driver.find_elements_by_css_selector('.pybr56ya.f10w8fjw [data-visualcompletion="ignore-dynamic"][style="padding-left: 8px; padding-right: 8px;"]')[3]
        #share.click()
        self.driver.execute_script("""
            document.querySelectorAll('.pybr56ya.f10w8fjw [data-visualcompletion="ignore-dynamic"][style="padding-left: 8px; padding-right: 8px;"]')[3].click()
        """)
        sleep(2)
        search_input = self.driver.find_element_by_css_selector('[aria-label="Search for people and groups"]')
        for contact in contacts:
            search_input.clear()
            search_input.send_keys(contact)
            sleep(1.5)
            try:
                send_btn = self.driver.find_element_by_css_selector('.muag1w35.b20td4e0 [aria-label="Send"]')
                send_btn.click()
                sleep(1)
            except:
                print('failed to get send btn')


bot = Bot()
bot.login()
bot.watch(
    'https://www.facebook.com/AmzaziSaaidOfficiel/',
    lambda: bot.share_post(['Ayoub Taouarda', 'Fridoga Manilla'])
)
