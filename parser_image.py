from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException

from config import USER_AGENT
from helper import Helper


class ParserItemInfo(Helper):
    def __init__(self,source_file=''):
        # Initialize Firefox options
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("general.useragent.override",
                                    USER_AGENT)  # Set custom user agent to avoid detection as a bot
        self.options.set_preference("dom.webdriver.enabled", False)  # Disable WebDriver detection
        self.options.set_preference("intl.accept_languages", 'en-us')  # Set language WebDriver
        self.options.set_preference("dom.webnotifications.enabled", False)  # Disable WebDriver notifications

        self.service = Service(executable_path='GeckoDriver/geckodriver.exe')  # Path to WebDriver

        self.driver = webdriver.Firefox(service=self.service,
                                        options=self.options)  # Create a new instance of the Firefox WebDriver with the specified options

        self.source_file = source_file

        self.iter_by_item()

    def xpath_exists(self, xpath):
        """Checks if an element with the given XPath exists on the page.

        Args:
            xpath (str): The XPath of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            # Attempt to find the element by XPath
            self.driver.find_element(By.XPATH, xpath)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def id_exists(self, element_id):
        """Checks if an element with the given ID exists on the page.

        Args:
            element_id (str): The ID of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            # Attempt to find the element by XPath
            self.driver.find_element(By.ID, element_id)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def class_exists(self, class_name):
        """Checks if an element with the given class name exists on the page.

        Args:
            class_name (str): The class name of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            # Attempt to find the element by class name
            self.driver.find_element(By.CLASS_NAME, class_name)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def tag_exists(self, tag_name):
        """Checks if an element with the given class name exists on the page.

        Args:
            tag_name (str): The tag name of the element to check.

        Returns:
            bool: True if the element exists, False otherwise.
        """
        try:
            # Attempt to find the element by tag name
            self.driver.find_element(By.TAG_NAME, tag_name)
            exist = True
        except NoSuchElementException:
            # If NoSuchElementException is raised, the element does not exist
            exist = False
        return exist

    def send_by_url(self, url):
        """
        Navigates to the specified URL using the web driver.

        Args:
            url (str): The URL to navigate to.

        Raises:
            WebDriverException: If there is an issue with navigating to the URL.
        """
        # Use the web driver to open the specified URL
        self.driver.get(url=url)



    def iter_by_item(self):
        with open(file=self.source_file, mode='r') as file:
            source = file.read()
            for url in source.split():
                self.random_pause_code(start=1, stop=4)
                self.send_by_url(url=url)
                self.get_image()


    def get_image(self):
        self.random_pause_code(start=1, stop=4)

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.TAG_NAME, 'img'))

        try:
            if self.tag_exists(tag_name='img'):
                self.driver.find_element(By.TAG_NAME, 'img').click()
                self.random_pause_code(start=1, stop=2)
                image_link = self.driver.find_element(By.TAG_NAME, 'img').get_attribute('src')


                self.crate_file(
                    filename=f"{self.source_file.split('/')[0]}/{self.source_file.split('/')[0]}_image_link.txt",
                    mode='a',
                    data=image_link
                )

        except NoSuchElementException:
            self.close_driver()

    def close_driver(self):
        """Close the WebDriver instance and quits the browser.

        This method closes the current window and terminates the WebDriver session.
        """
        self.driver.close()  # Close the current window
        self.driver.quit()  # Quit the WebDriver session and close all associated windows


def main():
    return ParserItemInfo(
        source_file='girl/girl_image_page_links.txt'
    )


if __name__ == '__main__':
    main()
