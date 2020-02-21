from bs4 import BeautifulSoup
import re


def main():
    with open('courses_list.html', encoding='utf-8') as f:  # if use file.mhtml, markup being parsed very messy
        soup = BeautifulSoup(f, 'html.parser')
    # ol = soup.find_all('ol', attrs={'class': re.compile('course-list')})
    ol = soup.find('ol')  # works fine also, because in our case single 'ol' exists in the file
    print(type(ol))

    li_list = ol.contents
    print(type(li_list[2]))
    for i in li_list:
        if i.name == 'li':
            print(i.attrs)
    # for child in ol.children:
    #     print(child)
    #     # print(type(child))
    #     print('*'*88)


if __name__ == '__main__':
    main()
