from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import string


# how to extract all text contents from html

def main():
    wanted_tags = ['a', 'p', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    strainer = SoupStrainer(wanted_tags)

    with open('docs_python_org.html', encoding='utf-8') as f:
        # soup = BeautifulSoup(f, 'html.parser')
        strained_soup = BeautifulSoup(f, 'html.parser', parse_only=strainer)

    # strainer filters some unuseful tags from html
    for st in strained_soup.stripped_strings:
        print(repr(st))

    # body = soup.html.body

    # best practice to extract text contents
    # the problem is, it returns also unnecessary text data e.g. script text
    # for st in body.stripped_strings:
    #     print(repr(st))

    # this way is bad, repeatedly returns same strings from different levels of tree
    # looping body.children is better, but still returns too many empty lines

    # for child in body.descendants:
    #     try:
    #         text = child.get_text().strip()
    #         print(text)
    #     except AttributeError:
    #         # print(f'{type(child)} has no attribute "get_text"')
    #         pass

    # with open('stepik_courses.csv', 'a', newline='', encoding='utf-8') as csv_file:
    #     my_writer = csv.writer(csv_file)
    #     my_writer.writerow([course_id, course_title, course_link, authors, course_students])


if __name__ == '__main__':
    main()
