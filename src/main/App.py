from src.request.URequest import URequest


class App:

    def __init__(self):
        pass

    @staticmethod
    def run():
        url = 'https://store.steampowered.com/search/?specials=1'
        URequest.create_soup_page(url)


def main():
    App.run()


if __name__ == '__main__':
        main()
