from bs4 import BeautifulSoup
import string


def main():
    with open('docs_python_org.html', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    body = soup.html.body.children

    for child in body:
        try:
            text = child.get_text().strip()
            print(text)
        except AttributeError:
            print(f'{type(child)} has no attribute "get_text"')

    # with open('stepik_courses.csv', 'a', newline='', encoding='utf-8') as csv_file:
    #     my_writer = csv.writer(csv_file)
    #     my_writer.writerow([course_id, course_title, course_link, authors, course_students])


if __name__ == '__main__':
    main()
