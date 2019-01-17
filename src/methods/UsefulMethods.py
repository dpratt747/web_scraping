from src.request.URequest import URequest


class UsefulMethods:

    def __init__(self):
        pass

    @staticmethod
    def find_all_by_class_and_dom(html, dom: str, class_name: str):
        souped_html = URequest.html_to_soup(html)
        return souped_html.find_all(dom, {"class": class_name})

    @staticmethod
    def find_one_by_class_and_dom(html, dom: str, class_name: str):
        souped_html = URequest.html_to_soup(html)
        return souped_html.find(dom, {"class": class_name})
