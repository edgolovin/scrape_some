from scrapy import Selector


def main():
    with open('courses_list.html') as f:
        html = f.read()

    sel = Selector(text=html)

    course_list = sel.xpath('//ol')
    print(course_list.extract())


if __name__ == '__main__':
    main()
