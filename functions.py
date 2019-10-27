import requests
from bs4 import BeautifulSoup
import os


def access_dontpad(dontpad):
    link = requests.get(dontpad)
    soup = BeautifulSoup(link.text, "html.parser")
    text = soup.find('textarea')
    return text


# def access_sub_dontpad(dontpad):
#      link = requests.get(dontpad)
#     soup = BeautifulSoup(link.text, 'html.parser')
#     sub_list = soup.find_all('a')
#     # for links in soup.find_all('a'):
#     #     print(links.prettify())
#     # return sub_list


def download_dontpad(dontpad):
    text = access_dontpad(dontpad)
    buffer = open("buffer.txt", "w+")
    buffer.write(text)
    buffer.close()


def edit_dontpad(dontpad):
    download_dontpad(dontpad)

    os.system("vim buffer.txt")

    with open('buffer.txt', 'r') as myfile:
        text = myfile.read()
    data = {'text': text}
    requests.post(url=dontpad, data=data)


# def delete_dontpad()


def main():
    endereco = input()
    # download_dontpad("http://dontpad.com/"+endereco+"/")
    # edit_dontpad("http://dontpad.com/"+endereco+"/")
    # download_dontpad_links("http://dontpad.com/"+endereco+"/")
    exit()


main()