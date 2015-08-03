from lxml import html
from lxml import etree
import requests
import json

class person:
  def __init__(self):
    netId = "test_id"
    department = "test"
    floor = "-1"

def get_data(url, xpath):
  page = requests.get(url)
  tree = html.fromstring(page.text)
  return tree.xpath(xpath)

def get_data_from_html(xpath, html):
  parser = etree.HTMLParser()
  tree = etree.parse(html, parser)
  return tree.xpath(xpath)

def main():
  # list of all cs faculty
  faculty = {}

  # xpath to get the illinois id of all faculty
  xpath_faculty_list_name = '//*[@class="extDirectoryPerson"]/div[3]/div[5]/a/text()'
  xpath_faculty_room = '//*[@class="extDirectoryPerson"]/div[3]/div[3]/text()'

  illinois_id = get_data_from_html(xpath_faculty_list_name, "cs-faculty.html")
  floor_addr = get_data_from_html(xpath_faculty_room, "cs-faculty.html")

  # Loop to reduce all email ids to just net id and add to dict
  count = 0
  for item in illinois_id:
    temp = person()
    temp.netId = item[:-13]
    temp.floor = floor_addr[count]
    temp.floor = temp.floor[0]
    temp.department = ["te"]
    faculty[temp.netId] = temp # add to dict
    count = count + 1

  research = ["architecture", "artificial", "bioinformatics", "database","graphics",
  "programming-languages","scientific","systems","theory"]

  url = "https://cs.illinois.edu/directory/profile/"
  url_list = ["https://cs.illinois.edu/research/research-areas/architecture-compilers-and-parallel-computing",
  "https://cs.illinois.edu/research/research-areas/artificial-intelligence",
  "https://cs.illinois.edu/research/research-areas/bioinformatics-computational-biology",
  "https://cs.illinois.edu/research/research-areas/database-information-systems",
  "https://cs.illinois.edu/research/research-areas/graphics-visualization-and-hci",
  "https://cs.illinois.edu/research/research-areas/programming-languages-formal-methods-software-engineering",
  "https://cs.illinois.edu/research/research-areas/scientific-computing",
  "https://cs.illinois.edu/research/research-areas/systems-and-networking",
  "https://cs.illinois.edu/research/research-areas/theory-algorithms"]

  xpath_list = ['//*[@id="node-526"]/div/table/tbody/tr/td[1]/a/@href',
  '//*[@id="node-529"]/div/table/tbody/tr/td[1]/a/@href',
  '//*[@id="node-534"]/div/table/tbody/tr/td[1]/a/@href',
  '//*[@id="node-531"]/div/table/tbody/tr/td[1]/a/@href',
  '//*[@id="node-532"]/div/table[2]/tbody/tr/td[1]/a/@href',
  '//*[@id="node-530"]/div/table/tbody/tr/td[1]/a/@href',
  '//*[@id="node-533"]/div/table[2]/tbody/tr/td[1]/a/@href',
  '//*[@id="node-527"]/div/table/tbody/tr/td[1]/a/@href',
  '//*[@id="node-528"]/div/table/tbody/tr/td[1]/a/@href']

  count = 0
  for x in range(0,9):
    temp = get_data(url_list[x], xpath_list[x])
    for y in temp:
      tempId = y[42:]
      if tempId in faculty:
        if "te" in faculty[tempId].department:
          faculty[tempId].department = [research[x]]
        else:
          faculty[tempId].department.append(research[x])

if __name__ == "__main__":
    main()
