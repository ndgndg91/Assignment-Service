# -*- coding: utf-8 -*-
import re


def main():
    regex = re.compile(r'[a-zA-Z0-9]+')

    f = open("Article.txt", 'rt', encoding='UTF8')
    text = f.read()
    text = text.replace('- ', '')
    text = text.replace('-', '')
    text = text.replace('\n', '')
    # print(text)

    wordss = text.split()
    words = regex.findall(str(wordss))
    word_counts = dict()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print('"' + word + '"' + '  shows', str(count) + ' times')

    max_cnt, max_word = max(zip(word_counts.values(), word_counts.keys()))
    print('The most frequent word is ' + '"' + max_word + '".')

    f2 = open("Word.txt", 'wt', encoding="UTF-8")
    for word in word_counts.keys():
        f2.write(word + '\r\n')
    f.close()
    f2.close()


if __name__ == '__main__':
    main()
