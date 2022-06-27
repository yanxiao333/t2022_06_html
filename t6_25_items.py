from requests_html import HTMLSession
from copyheaders import headers_raw_to_dict

url = ''
str = b'''

'''


class Session(object):

    def __init__(self):
        self.session = HTMLSession()
        self.headers = headers_raw_to_dict(str)

    def main():
        pass


if __name__ == '__main':
    ss = Session()
    ss.main()
