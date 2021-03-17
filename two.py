import requests
import re
from bs4 import BeautifulSoup
# Gettin the page by Request-modal
page = requests.get("https://faradars.org/")
# Parsing the page by BS
page_content = BeautifulSoup(page.content, 'html.parser')
# Using BS methods to get the required Tag
home_page = page_content.find(class_="home")
# Using Select method to get The Class
all_cards = home_page.select(".course-card")
print(len(all_cards))
# Declaring
text_of_card = ''
name_raw = []
name_clean = ''
final_name_list = []
flag_text = 0
# for Loop
for course_name in all_cards:
    # Getting and Sanitizing the text for any text-name
    text_of_card = course_name.find(class_='show-text-card').get_text()
    name_raw = re.split("\s", text_of_card)
    name_raw = [aaa for aaa in name_raw if aaa != '']
    for xx in name_raw:
        name_clean += ' ' + xx
    # Entering the clean-name into the final list
    final_name_list.append(name_clean)
    name_clean = ''
    # Breaking
    flag_text += 1
    if flag_text == 12:
        break


for x in final_name_list:
    print('QQQQQQQQQQQQQQQQQQQQQQQ')
    print(x)