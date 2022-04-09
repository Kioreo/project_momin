import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0056&date=20220403"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')

movies = soup.select('body > div > div.sect-showtimes > ul > li')

def get_timeTable(movie):
    tuples = []
    timeTables = movie.select('div > .type-hall > .info-timetable > ul > li')
    for timeTable in timeTables:
        time = timeTable.select_one('em').get_text()
        seat = timeTable.select_one('span.').get_text()
        tuple = (time, seat)
        tuples.append(tuple)
    return tuples

for movie in movies:
    title = movie.select_one('div > div.info-movie > a > strong').get_text().strip()
    timeTable = get_timeTable(movie)
    print(title, timeTable, '\n')

