from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup


class URequest:

    def __init__(self):
        pass

    @staticmethod
    def create_soup_page(url):
        page_soup = None
        u_client = None

        try:
            u_client = uReq(url)
            page_html = u_client.read()
            page_soup = bsoup(page_html, "html.parser")
            print(page_soup)
        except Exception as e:
            print(e)
        finally:
            u_client.close()

        return page_soup
