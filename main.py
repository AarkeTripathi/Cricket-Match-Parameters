from selenium import webdriver
from selenium.webdriver.common.by import By





# Scraping the Cricket Line Guru app
path='chromedriver-win64/chromedriver.exe'
driver=webdriver.Chrome(path)
url='https://www.cricketlineguru.com/cricket-schedule/upcoming/all'
driver.get(url)




# Scraping all matches
apps=driver.find_element(By.TAG_NAME,"app-schedule")
table=apps.find_element(By.TAG_NAME,'table')
matches=table.find_elements(By.TAG_NAME,'tr')
schedule=[match.text.split('\n') for match in matches[1:]]
schedule=[{match[0]:match[1:]} for match in schedule]




# Function to obtain the list of matches scheduled on the input date
def match_list(date):
    for game in schedule:
        if date_inp in game.keys():
            list_of_matches=game[date_inp][::4]
            list_of_matches=[i.split('  ')[0] for i in list_of_matches]
            break
    return list_of_matches




# Function to obtain the parameters of the match
def match_info(match):
    # Directing to the page containing info about the match
    element=driver.find_element(By.LINK_TEXT,match)
    driver.get(element.get_attribute('href'))


    # Getting the team names
    params=driver.find_elements(By.TAG_NAME,'strong')
    params=[param.text for param in params]
    team1=params[6]
    team2=params[7]


    # Deriving all the ueful odds of the match
    info=driver.find_elements(By.TAG_NAME,'div')
    info=[c.text for c in info]
    use_info=info[2].split('\n')


    city=use_info[use_info.index('City:')+1]
    weather=use_info[use_info.index('Weather:')+1]
    temperature=use_info[use_info.index('Temperature:')+1]
    rain=use_info[use_info.index('Rain Forecast:')+1]
    humid=use_info[use_info.index('Humid:')+1]


    return team1,team2,city,weather,temperature,rain,humid




# Taking the date of match as input
date_inp = 'Mon, 30 Oct 2023'     #sample input


# List of all matches on that day
list_of_matches = match_list(date_inp)


# This input will be taken by the user through drop down menu containing matches on the date input by user
match_inp = list_of_matches[1]        #sample input


# Obtaining the parameters of the match
team1, team2, city, weather, temperature, rain, humid = match_info(match_inp)


print(f'The match is between {team1} vs {team2}', '\nCity: ', city, '\nWeather: ', weather, '\nTemperature: ', temperature, '\nRain probability: ', rain, '\nHumidity: ', humid)
