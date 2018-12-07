# -*- coding: utf-8 -*-
from bs4 import *
import csv
import re
import requests


def cut_link(nws_link_list, count):
    how_cut = len(nws_link_list) - count
    real_cut = how_cut + 1
    for i in range(len(nws_link_list) - 1, len(nws_link_list) - real_cut, -1):
        del (nws_link_list[i])
    return nws_link_list


def check_count(nws_link_list, page_link_list, count, loop_count):
    html_soup = get_html(page_link_list[loop_count])
    for k in html_soup.find_all('a', {'class': '_sp_each_url'}):
        if k.text == '네이버뉴스':
            nws_link_list.append(k.get('href'))
        if len(nws_link_list) == count:
            break
    return nws_link_list


def get_html(url):
    response_html = requests.get(url).text
    soup = BeautifulSoup(response_html, 'html.parser')
    return soup


def get_count():
    count = int(input('기사 개수?(10단위로 입력) : '))
    if count % 10 != 0:
        print('10 단위로 입력해주세요!!!')
        get_count()
    return count


def main():
    keyword = input("검색하실 단어를 입력하세요 : ")
    count = get_count()
    url1 = 'http://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + keyword
    print(url1)
    html_soup = get_html(url1)
    page_link_list = []
    nws_link_list = []

    for k in html_soup.find_all('a', {'class': '_sp_each_url'}):
        if k.text == '네이버뉴스':
            # print(k.get('href'))
            nws_link_list.append(k.get('href'))

    for j in html_soup.find_all('a', {'href': re.compile('cluster_rank=')}):
        # print(j.get('href'))
        string = str(j.get('href'))
        string = string.replace(string[0:2], 'http://')
        # print(string)
        page_link_list.append(string)

    # print(len(nws_link_list))

    if len(nws_link_list) > count:
        nws_link_list = cut_link(nws_link_list, count)
    loop_count = 0
    while len(nws_link_list) < count:
        nws_link_list = check_count(nws_link_list, page_link_list, count, loop_count)
        loop_count += 1

    print('지금부터 시간이 걸릴수 있습니다. 느긋하게 기다려 주세요..')
    titles = get_titles(nws_link_list)
    contents = get_contents(nws_link_list)

    print('기사 개수 : ' + str(len(nws_link_list)))
    # print(len(page_link_list))
    # print(len(titles))
    # print(len(contents))

    print(nws_link_list)

    outfile = open('naver.csv', 'w', encoding='utf-8')
    write_outfile = csv.writer(outfile)
    header = ["기사 제목", '기사 내용']
    write_outfile.writerow(header)
    for i in range(0, len(contents)):
        list_article = [titles[i], contents[i]]
        write_outfile.writerow(list_article)

    outfile.close()


def get_contents(some_list):
    r = []
    count = 1
    for i in some_list:
        if i[7:13] == 'sports':
            soup = get_html(i)
            article_body = soup.find('div', id='wrap')
            article_body = str(article_body)
            article_body = re.sub('<!--.+?-->', '', article_body, 0, re.I | re.S)
            article_body = re.sub('/\*.+?\*/', '', article_body, 0, re.I | re.S)
            article_body = re.sub('<.+?>', '', article_body, 0, re.I | re.S)
            article_body = re.sub('.+?본문 프린트', '', article_body, 0, re.I | re.S)
            article_body = re.sub('좋아요.+?webncc', '', article_body, 0, re.I | re.S)
            print('기사 ' + str(count) + ' 개 완료!')
            count += 1
            r.append(article_body)
        else:
            soup = get_html(i)
            article_body = soup.find('div', id='wrap')
            article_body = str(article_body)
            article_body = re.sub('<!--.+?-->', '', article_body, 0, re.I | re.S)
            article_body = re.sub('/\*.+?\*/', '', article_body, 0, re.I | re.S)
            article_body = re.sub('<.+?>', '', article_body, 0, re.I | re.S)
            article_body = re.sub('.+?// flash 오류를 우회하기 위한 함수 추가', '', article_body, 0, re.I | re.S)
            article_body = re.sub('좋아요.+?\(\'data-useragent\',navigator.userAgent\);', '', article_body, 0, re.I | re.S)
            article_body = re.sub('function.+?back\(\) {}', '', article_body, 0, re.I | re.S)
            article_body = re.sub('메인 메뉴로 바로가기.+?인쇄하기', '', article_body, 0, re.I | re.S)
            article_body = re.sub('좋아요.+?모바일 버전으로 보기', '', article_body, 0, re.I | re.S)
            print('기사 ' + str(count) + ' 개 완료!')
            count += 1
            r.append(article_body)
    return r


def get_titles(some_list):
    r = []
    for i in some_list:
        soup = get_html(i)
        article_title = soup.title.text
        r.append(article_title)
    return r


main()
