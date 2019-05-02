"""Download Google Slides."""
import time
from typing import Text

from absl import app
from absl import flags
from selenium.webdriver.chrome.webdriver import WebDriver

from tool import chromedriver
from tool import xte

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'url', None,
    'The URL of the Google slides, in presentation mode.')

flags.DEFINE_integer(
    'num_of_pages', 1,
    'Download this number of pages.')

flags.DEFINE_integer(
    'wait_for_navigation_bar_to_disappear_sec', 10,
    'Wait for this long to navigation bar to disappear.')

flags.DEFINE_float(
    'wait_between_pages_sec', 1.0,
    'How long to wait between moving to next pages.')


class Fetcher:

    def __init__(
            self,
            manager: chromedriver.ChromeDriverManager,
            xte_client: xte.Xte):
        self._manager = manager
        self._xte = xte_client

    def take_screen_shots(
            self,
            url: Text,
            number_of_pages: int,
            file_prefix: Text,
    ) -> None:
        """Takes a screen shot of a single page.

        Args:
            url: the page to take screen shot for.
            number_of_pages: number of pages to take screenshots for.
            file_prefix: the prefix of files to save as.
        """

        def take_screen_shot_action(driver: WebDriver) -> None:
            """Takes a screen shot."""
            driver.get(url)
            time.sleep(FLAGS.wait_for_navigation_bar_to_disappear_sec)

            for page_idx in range(number_of_pages):
                driver.get_screenshot_as_file('%s_%03d.png' % (file_prefix, page_idx))
                self._xte.Run(['key Right'])
                time.sleep(FLAGS.wait_between_pages_sec)

        self._manager.Do(take_screen_shot_action)


def main(_):
    fetcher = Fetcher(
        chromedriver.ChromeDriverManager(),
        xte.Xte())
    fetcher.take_screen_shots(FLAGS.url, FLAGS.num_of_pages, 'data/screenshot')


if __name__ == '__main__':
    app.run(main)
