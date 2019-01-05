from urllib.request import urlopen as urequest
from bs4 import BeautifulSoup as bSoup


class URequest:

    def __init__(self):
        pass

    @staticmethod
    def html_to_soup(html: object):
        to_convert = None

        if type(html) != bSoup:
            to_convert = str(html)

        return bSoup(to_convert, "html.parser")

    @staticmethod
    def create_soup_page(url: str):
        page_soup = None
        u_client = None

        try:
            u_client = urequest(url)
            page_html = u_client.read()
            page_soup = URequest.html_to_soup(page_html)
        except Exception as e:
            print(e)
        finally:
            u_client.close()

        return page_soup
