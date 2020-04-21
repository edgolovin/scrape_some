from scrapy import Selector


def main():
    with open('courses_list.html', encoding='utf-8') as f:
        sel = Selector(text=f.read())

    course_list = sel.xpath('//ol')
    print(course_list.extract())


if __name__ == '__main__':
    main()
