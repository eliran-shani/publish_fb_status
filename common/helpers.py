import os
import time
import urllib.request as request
from diffimg import diff
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

first_time = True


def set_first_time_false():
    """ Sets the Golbal variable 'first_time' to False
    """
    global first_time
    first_time = False


def get_root_path() -> str:
    """

    :return: The root folder path
    """
    relative_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(relative_path)


def get_attachment_path():
    """

    :return: The attachments folder path
    """
    return "{root}/{attachments}/".format(root=get_root_path(), attachments="attachments")


def get_downloads_path():
    """

    :return: The downloads folder path
    """
    directory = "{root}/{downloads}/".format(root=get_root_path(), downloads="downloads")
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory


def find_element_by_test_id(driver: webdriver, test_id: str) -> WebElement:
    """

    :param driver: a webdriver object
    :param test_id: a string the represents an element's data-testid
    :return: a WebElement given a string
    """
    try:
        return driver.find_element_by_css_selector('[data-testid="{id}"]'.format(id=test_id))
    except NoSuchElementException:
        print("NoSuchElement: {}".format(test_id))


def click_status(driver: webdriver) -> WebElement:
    """

    :param driver: a webdriver object
    :return: a WebElement of the status component
    """
    if first_time:
        set_first_time_false()
        composer = driver.find_element_by_id("pagelet_composer")
        return composer.find_element_by_tag_name("textarea")
    else:
        return find_element_by_test_id(driver, "status-attachment-mentions-input")


def click_post_button(driver: webdriver):
    """ Click on the post button

    :param driver: a webdriver object
    """
    find_element_by_test_id(driver, "react-composer-post-button").click()


def add_status_text(driver: webdriver, text: str, publish: bool = False):
    """

    :param driver: a webdriver object
    :param text: a string to update the status component
    :param publish: a boolean flag. in case of True, click on the post button.
    """
    status_element = click_status(driver)
    status_element.send_keys(text)
    if publish:
        click_post_button(driver)


def add_status_image(driver: webdriver, image: str, publish: bool = False):
    """

    :param driver: a webdriver object
    :param image: a string of an image path
    :param publish: a boolean flag. in case of True, click on the post button.

    """
    image_path = "{attachments}{image}".format(attachments=get_attachment_path(), image=image)
    click_status(driver)
    upload_button = find_element_by_test_id(driver, "media-sprout")
    upload_button.send_keys(image_path)
    image_element = find_element_by_test_id(driver, "media-attachment-photo")

    assert image == image_element.find_element_by_tag_name("img").get_attribute("alt"), \
        "The image was not uploaded as expected"

    if publish:
        click_post_button(driver)


def read_image(url: str) -> bytes:
    """

    :param url: a url string of an image
    :return: bytes of the response
    """
    with request.urlopen(url) as response:
        return response.read()


def compare_images(image1: str, image2: str):
    """

    :param image1: a string to the first image path
    :param image2: a string to the second image path

    """
    image_ratio_diff = diff(image1, image2, delete_diff_file=True)

    assert image_ratio_diff < 0.01, "There is an image ratio difference of {}% between the images". \
        format(image_ratio_diff)


def verify_status_posted(driver: webdriver, text: str = None, image: str = None):
    """

    :param driver: a webdriver object
    :param text: a text to verify in the status component
    :param image: an image to verify in the status component

    """
    # wait for the status to upload
    time.sleep(2)

    news_feed = find_element_by_test_id(driver, "newsFeedStream")

    if text is not None:
        assert text in news_feed.text, \
            "{text} was not posted as expected".format(text=text)

    if image is not None:
        img_src = news_feed.find_element_by_css_selector(".uiScaledImageContainer > img").get_attribute("src")
        downloaded_image_path = get_downloads_path() + "downloaded_image.jpg"
        with open(downloaded_image_path, 'wb') as f:
            f.write(read_image(img_src))

        compare_images(downloaded_image_path, get_attachment_path() + image)
