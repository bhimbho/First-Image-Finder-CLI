from bs4 import BeautifulSoup
import os, click
from random import randint
from selenium import webdriver
from urllib.request import urlretrieve



def search_string(query):
    driver = webdriver.Chrome("c://chromedriver")
    driver.get("https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch")
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    mydivs = soup.findAll("img", {"class": "rg_i"})
    return mydivs[0]["src"]


def save_image(link):
    print(f'found {len(link)} images')
    print('===Start downloading...===')

    try:
        os.mkdir('downloads')
    except FileExistsError:
        pass
        count = 0
    src = link
    try:
        if src != None:
            src = str(src)
            count = randint(1, 2000)
            urlretrieve(src, os.path.join('downloads', 'image' + str(count) + '.jpg'))
            print('==== Image Download and Stored in Downloads Folder =====')
        else:
            raise TypeError
    except TypeError:
        print('fail')

@click.command()
@click.option('--search', '-s', default="fish", help='Enter search value')
def main(search):

    link = search_string(search)
    save_image(link)


if __name__ == '__main__':
    main()
