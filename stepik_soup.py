from bs4 import BeautifulSoup
import csv


def main():
    with open('courses_list.html', encoding='utf-8') as f:  # if use file.mhtml, markup being parsed very messy
        soup = BeautifulSoup(f, 'html.parser')

    courses_tag = soup.find('ol')  # in our case single 'ol' exists in the file

    li_tags_list = []  # all courses listed in 'li' tags

    for li in courses_tag.contents:
        if li.name == 'li':
            li_tags_list.append(li)

    for li in li_tags_list:
        course_id = li['id']
        course_title = ''
        course_link = ''
        authors = {}
        course_students = ''
        for t in li.descendants:
            if t.name == 'a' and 'course-widget__title-link' in t['class']:
                course_link = t['href']
                course_title = t.text.strip()
            elif t.name == 'a' and 'course-widget__author-link' in t['class']:
                authors[t['href']] = t.text.strip()
            elif t.name == 'div' and 'course-promo-widget__stats-item' in t['class']:
                course_students = t.text.strip()
        with open('stepik_courses.csv', 'a', newline='', encoding='utf-8') as csv_file:
            my_writer = csv.writer(csv_file)
            my_writer.writerow([course_id, course_title, course_link, authors, course_students])


if __name__ == '__main__':
    main()
