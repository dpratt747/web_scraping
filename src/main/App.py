from src.request.URequest import URequest
from src.methods.UsefulMethods import UsefulMethods


class App:

    def __init__(self):
        pass

    @staticmethod
    def run():
        endpoint = 'new-look-vouchers'
        domain = 'https://www.vouchercloud.com'
        url = create_url(domain, endpoint)
        # url = f'https://www.vouchercloud.com/{endpoint}'
        souped_page = URequest.create_soup_page(url)
        results = []

        content = souped_page.find_all("div", {"class": "content"})
        layout = UsefulMethods.find_all_by_class_and_dom(content, "div", "layout")
        container = UsefulMethods.find_all_by_class_and_dom(layout, "div", "container")
        layout_content = UsefulMethods.find_all_by_class_and_dom(container, "main", "layout-content")
        section_tile_list = UsefulMethods.find_all_by_class_and_dom(layout_content, "div", "section-tile-list")
        tile_list = UsefulMethods.find_all_by_class_and_dom(section_tile_list, "div", "tile-list")
        offer_tile_list_content = UsefulMethods.find_all_by_class_and_dom(tile_list, "div", "tile-list-content")
        offer_tile_list_footer = UsefulMethods.find_all_by_class_and_dom(tile_list, "div", "tile-list-footer")

        for (offer, offer_footer) in zip(offer_tile_list_content, offer_tile_list_footer):
            # initialise dictionary where scrapped information should be persisted
            offer_info = {}
            h2 = UsefulMethods.find_all_by_class_and_dom(offer, "h2", "tile-list-title")
            title = UsefulMethods.find_one_by_class_and_dom(h2, "span", "hover-over")
            description = UsefulMethods.find_one_by_class_and_dom(h2, "span", "tile-text")
            expiration = UsefulMethods.find_one_by_class_and_dom(offer_footer, "span", "tile-expires")
            analytics_link = UsefulMethods.find_one_by_class_and_dom(offer_footer, "a", "tile-redeem")

            offer_info["title"] = title.text
            offer_info["description"] = description.text
            offer_info["expiration"] = expiration.text
            offer_info["link"] = create_url(domain, analytics_link["href"])

            # add offer to final results table
            results.append(offer_info)


def create_url(url: str, endpoint: str):
    return f'{url}/{endpoint}'


def main():
        App.run()


if __name__ == '__main__':
        main()
