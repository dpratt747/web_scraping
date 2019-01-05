from src.request.URequest import URequest


class App:

    def __init__(self):
        pass

    @staticmethod
    def run():
        limit = 5
        search_results = []
        search_results_as_soup = []
        titles = []
        for i in range(limit):
            url = f'https://store.steampowered.com/search/?specials=${i}'
            souped_page = URequest.create_soup_page(url)
            search_results.extend(souped_page.find_all("a", {"class": "search_result_row"}))

        for results in search_results:
            soup_results = URequest.html_to_soup(results)
            title = soup_results.find("span", {"class": "title"}).string
            search_results_as_soup.append(soup_results)
            titles.append(title)


def main():
    App.run()


if __name__ == '__main__':
        main()
