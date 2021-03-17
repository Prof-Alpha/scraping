import requests
import re
from bs4 import BeautifulSoup

page = requests.get("https://faradars.org/")
page_content = BeautifulSoup(page.content, 'html.parser')

home_page = page_content.find(class_="home")
all_cards = home_page.select(".course-card")
print(len(all_cards))
text_of_card = all_cards[0].find(class_='show-text-card').get_text()


# Declaring Final [ Name , Price]
final_name_price = []
# Declaring flag
for_flag = 0
# for-Loop in-order-to Extract   ['Course_Name', Price]
for xx in all_cards:
    course_name_raw = xx.find(class_='show-text-card').get_text()
    course_price_raw = xx.find(class_='card-footer').get_text()
    # Sanitizing The Prices And Turning it To a List
    '''  Price Sanitizing 1/2    '''
    # The output is a List of Digits
    course_price_raw_list = re.findall("\d", course_price_raw)
    course_price = ''
    for price_digits in course_price_raw_list:
        course_price += price_digits
    # Entering the name and price into The Final List
    course_list = []
    course_list.append(course_price)
    '''  Text Sanitizing 2/2   '''
    # Output is a List for re.split()
    name_raw = re.split("\s", course_name_raw)
    # Eliminating The empty characters from The List Above
    # Output is Something Like: ['aaaa', 'bbbb', 'cccc']
    name_raw = [aaa for aaa in name_raw if aaa != '']
    # Concatinating the List members
    name_clean = ''
    for xx in name_raw:
        name_clean += ' ' + xx
    # Entering the clean-name into the final list
    course_list.append(name_clean)
    name_clean = ''
    '''  End  2/2   '''
    # Entering New Course name-price into the final list
    final_name_price.append(course_list)
    for_flag += 1
    if for_flag == 12:
        break

print(final_name_price)
# price_one is Modified
'''
# for Loop on First 12 New Courses To Get The Prices
for_flag = 0
# declare an empty list
price_list_new_courses = []
# declare an empty list to Store The final Daily Prices
daily_price_list = []
# for Loop on All Daily New Courses
for new_courses in price_one:
    # Sanitizing The Prices And Turning it To a List
    price_list = re.findall("\d", new_courses.get_text())
    # Converting Price list To a String
    final_price = ''
    for xx in price_list:
        final_price += xx
    # Adding The Price to The Final-Price List
    daily_price_list.append(final_price)
    # Break if is Not New Course
    j_flag += 1
    if j_flag == 12:
        break

# Printing The Daily Prices
print(daily_price_list)

# Perspective   ('Name', Price)
'''