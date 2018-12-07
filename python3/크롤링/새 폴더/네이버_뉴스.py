# url = 'http://news.naver.com/main/f  54search/search.nhn?query=%BC%AD%C1%F8%BC%F6'
# url = 'http://news.naver.com/main/search/search.nhn?query=%BC%AD%C1%F8%BC%F6&st=news.all&q_enc=EUC-KR&r_enc=UTF-8&r_format=xml&rp=none&sm=all.basic&ic=all&ie=MS949&so=rel.dsc&detail=0&pd=1&r_cluster2_start=1&r_cluster2_display=10&start=1&display=5&page=2'

# http://news.naver.com/main/search/search.nhn?
# refresh=
# &so=rel.dsc
# &stPhoto=
# &stPaper=
# &stRelease=
# &ie=MS949
# &detail=0
# &rcsection=
# &query=%BE%CB%B6%F3%BA%E4
# &x=0
# &y=0
# &sm=all.basic
# &pd=1
# &startDate=
# &endDate=


import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

import time
import os

from app import *
from datetime import datetime

import re

d_url = 'http://news.naver.com/main/search/search.nhn?ie=utf8&query='
headers = {"User-Agent": "Mozilla/5.0", "referer": "http://m.naver.com"}

isLastPage = False


# def checkLastPage(soup):


def fetch_list(url, options):
    url += '&page=' + str(options['page'])
    # print(url)
    # return
    soup = read_to_soup(url, headers)

    n_links = soup.find_all('a', class_='go_naver')

    links = [tag['href'] for tag in n_links]

    _next = soup.find('a', class_='next')

    if not _next:
        isLastPage = True

    return links


def get_redirect_link_reqeust(_url):
    url = re.sub('\'', '', _url.group())

    isNaver = re.match('http://news.naver', url)
    print('REDIRECT URL: ' + url)
    print("############################################")
    print(isNaver)
    if not isNaver:
        return False

    return read_to_soup(url, headers)


def fetch_detail(url):
    soup = read_to_soup(url, headers)

    script = soup.find('script').get_text(strip=True)
    isURL = script = soup.find('script').get_text(strip=True)
    isURL = re.search("http://.+'", isURL)

    if isURL:
        soup = get_redirect_link_reqeust(isURL)
        if not soup:
            return False

    body = soup.find(id='articleBodyContents')
    title = soup.find(id='articleTitle').get_text(strip=True)

    if body.a:
        body.a.extract()

    return {
        'title': title,
        'body': body.get_text(strip=True)
    }


def fetch_start():
    query = input_query()
    # query = input("검색할 문자열을 입력하세요: ")
    _max = input_count()
    path = input_save_path()
    f = save_file(path)

    w_count = 1
    isBreak = False
    isFirstLoop = True
    isNaver = True
    page = 1

    options = {
        'page': page
    }

    while True:
        if w_count > 1:
            if isBreak:
                break
            else:
                if isLastPage:
                    break

                if isNaver:
                    delay_random()

                options['page'] += 1
        else:
            if not isFirstLoop:
                options['page'] += 1

        _URL = d_url + query
        _list = fetch_list(_URL, options)

        # print(_list)

        for link in _list:
            try:
                if w_count == 1:
                    delay_random()
                else:
                    if isNaver:
                        pass
                    else:
                        delay_random()
                print("MAIN URL: " + link)
                detail = fetch_detail(link)
                if not detail:
                    print("네이버 뉴스가 아닙니다.")
                    isNaver = False
                    continue

                isNaver = True

                separation(f)

                file_write(f, '제목 : ' + detail['title'])
                file_write(f, '뉴스내용 : ' + detail['body'])

                separation(f)

                if w_count == _max:
                    isBreak = True
                    break
                else:
                    w_count += 1
                    delay_random()

            except:
                print("크롤링 할 수 없는 페이지입니다.")
                continue

        if isFirstLoop:
            isFirstLoop = False

        if isBreak:
            break

    print("총 " + str(w_count) + "건 추출에 성공하였습니다.")
    f.close()


fetch_start()
