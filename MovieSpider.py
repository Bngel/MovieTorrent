import requests
from bs4 import BeautifulSoup
from urllib import parse
import pyperclip
from PyQt5.QtCore import pyqtSignal,QThread
from PyQt5 import QtWidgets

class MovieSpider(QThread):
    finishSignal = pyqtSignal(str)

    def __init__(self,movie):
        super(MovieSpider,self).__init__()
        self.base_url = 'http://s.ygdy8.com'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        }
        self.cookie = {
            'Cookie': 'PHPSESSID=73057044b31d8bf035e11159c701355d'
        }
        self.mov = movie

    def get_url(self):
        source = parse.quote(self.mov.MovieInput.text().encode('gb2312'))
        url = self.base_url +'/plus/so1.php?typeid=1&keyword='+source
        response = requests.get(url,headers=self.header,cookies=self.cookie)
        response.encoding='gb2312'
        soup = BeautifulSoup(response.text,'html.parser')
        return soup

    def url_parser(self):
        try:
            self.mov.MovieList.clear()
            valid = True
            if len(self.mov.MovieInput.text().encode()) < 3:
                self.mov.State.setText('请输入3个字节以上电影名.')
                valid = False
            if valid == True:
                self.mov.State.setText('正在搜索电影:' + self.mov.MovieInput.text() + '...')
                soup = self.get_url()
                # print(soup)
                self.torrent_url = []
                flag = True
                while flag == True:
                    # print(soup)
                    movie_list = soup.find('div', {'class': 'co_content8'}).find_all('table')
                    next_page = ''
                    try:
                        next_page = movie_list[-1].find_all('a')[-2].text
                    except IndexError as ie:
                        flag = False
                    # print(next_page)
                    if flag == True:
                        movies = movie_list[:-1]
                    else:
                        movies = movie_list
                    if next_page != '下一页':
                        flag = False
                    for movie in movies:
                        movies_url = self.base_url + movie.find('a').get('href')
                        print(movies_url)
                        html = requests.get(movies_url, headers=self.header, cookies=self.cookie)
                        html.encoding = 'gb2312'
                        soups = BeautifulSoup(html.text, 'html.parser')
                        torrent = soups.find('div', {'class', 'co_content8'}).find('td', {'bgcolor': '#fdfddf'}).find('a').get('href')
                        self.torrent_url.append(torrent)
                        self.mov.MovieList.addItem(movie.find('a').text)
                    if flag == True:
                        url = self.base_url + movie_list[-1].find_all('td')[-2].find('a').get('href')
                        response = requests.get(url, headers=self.header, cookies=self.cookie)
                        response.encoding = 'gb2312'
                        soup = BeautifulSoup(response.text, 'html.parser')
                self.mov.State.setText('双击以复制磁力链接')
        except AttributeError as ae:
            self.url_parser()

    def run(self):
        self.url_parser()
        self.finishSignal.emit('Finish')

    def clip_url(self):
        index = self.mov.MovieList.currentRow()
        print(index)
        pyperclip.copy(self.torrent_url[index])
        msg = QtWidgets.QMessageBox()
        msg.information(self.mov, "提示:", "磁力链接已复制到剪贴板", msg.Ok,msg.Ok)


'''
    def url_parser(self):
        try:
            self.mov.MovieList.clear()
            self.mov.MovieList.setDisabled(True)
            valid = True
            if len(self.mov.MovieInput.text().encode()) < 3:
                self.mov.State.setText('请输入3个字节以上电影名.')
                valid = False
            if valid == True:
                self.mov.State.setText('正在搜索电影:' + self.mov.MovieInput.text() + '...')
                soup = self.get_url()
                # print(soup)
                movie_url = []
                flag = True
                while flag == True:
                    # print(soup)
                    movie_list = soup.find('div', {'class': 'co_content8'}).find_all('table')
                    next_page = ''
                    try:
                        next_page = movie_list[-1].find_all('a')[-2].text
                    except IndexError as ie:
                        flag = False
                    # print(next_page)
                    if next_page != '下一页':
                        flag = False
                    for movie in movie_list[:-1]:
                        self.mov.MovieList.addItem(movie.find('a').text)
                        movie_url.append(self.base_url + movie.find('a').get('href'))
                    if flag == True:
                        url = self.base_url + movie_list[-1].find_all('td')[-2].find('a').get('href')
                        response = requests.get(url, headers=self.header, cookies=self.cookie)
                        response.encoding = 'gb2312'
                        soup = BeautifulSoup(response.text, 'html.parser')
                self.mov.State.setText('搜索完毕 正在导入磁力链接...')
                self.torrent_url = []
                for page in movie_url:
                    html = requests.get(page, headers=self.header, cookies=self.cookie)
                    html.encoding = 'gb2312'
                    soup = BeautifulSoup(html.text, 'html.parser')
                    torrent = soup.find('div', {'class', 'co_content8'}).find_all('td', {'bgcolor': '#fdfddf'})
                    for tdtor in torrent:
                        self.torrent_url.append(tdtor.find('a').get('href'))
                # print(self.torrent_url)
                self.mov.State.setText('导入完毕 双击以复制磁力链接')
                self.mov.MovieList.setEnabled(True)
        except AttributeError as ae:
            self.url_parser()
'''