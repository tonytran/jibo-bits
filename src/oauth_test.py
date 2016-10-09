import requests
import webbrowser
import base64
import json
import datetime
import time

with open('keys.txt', 'r') as infile:

    AUTH = infile.readline().strip('\n')


def get_profile_data():
    r2 = requests.get(
        url = 'https://api.fitbit.com/1/user/37T8GV/profile.json',
        headers  = {

        'Authorization':"Bearer"+AUTH,
        'Accept-Header': 'en_US'
        }
    )

    r2 = r2.json()
    with open('./profile_data.json', 'w+') as outfile:
        json.dump(r2, outfile)
def get_profile_data2():
    r2 = requests.get(
        url = 'https://api.fitbit.com/1/user/37T8GV/profile.json',
        headers  = {

        'Authorization':"Bearer"+AUTH,
        'Accept-Header': 'en_US'
        }
    )

    r2 = r2.json()
    with open('./profile_data2.json', 'w+') as outfile:
        json.dump(r2, outfile)

def get_current_date():
    date = datetime.datetime.now()
    return date.day, date.month, date.year
def make_request():
    #webbrowser.open('https://www.fitbit.com/oauth2/authorize?client_id=2282D5&response_type=token&scope=activity%20sleep&prompt=consent')
    #get_sleep_data()
    #get_weight_data()
    #get_hr_data()
    get_activity_data()
    get_profile_data2()
    get_profile_data()
    '''
    compare steps to step goals
    '''


    with open('./daily_activity.json') as data_file:
        daily_activity = json.load(data_file)

    steps_to_complete = int(daily_activity['goals']['steps']) - 10500#int(daily_activity['summary']['steps'])
    if steps_to_complete < 0:
        print("Congrats you're ", abs(steps_to_complete), " steps over your step goal.")
    else:
        print("You need ", steps_to_complete, " to complete your goal of ", daily_activity['goals']['steps'], " for the day.")
    #calories_to_consume =
    #calories_to_lose =


    '''
    calculate how much sleep user got recently (1d), compare against sleep goals
    minutesAsleep
    minDuration

    '''
    with open('./sleep_log_2016-10-8.json') as data_file:
        sleep_activity = json.load(data_file)
    #minutes_to_sleep
    #print("You slept for ", '{:02d}:{:02d}'.format(*divmod(int(sleep_activity['sleep'][0]['minutesAsleep']), 60)), " yesterday.")



def get_activity_data():
    r2 = requests.get(
        url = 'https://api.fitbit.com/1/user/37T8GV/activities/date/today.json',
        headers  = {

        'Authorization':"Bearer"+AUTH,
        'Accept-Header': 'en_US'
        }
    )

    r2 = r2.json()


    with open ('./daily_activity.json', 'w+') as outfile:
        json.dump(r2, outfile)

def get_sleep_data():
    r2 = requests.get(
        url = 'https://api.fitbit.com/1/user/37T8GV/sleep/goal.json',
        headers  = {
        'Authorization':"Bearer"+AUTH,
        'Accept-Header': 'en_US'
        }
    )
    #print(r2.status_code)
    r2 = r2.json()


    with open ('./sleep_goals.json', 'w+') as outfile:
        json.dump(r2, outfile)

    #print(r2)
    currdate = get_current_date()
    currdate = str(currdate[2]) + '-' + str(currdate[1]) + '-' +str(currdate[0])


    r3 = requests.get(
        url = "https://api.fitbit.com/1/user/37T8GV/sleep/date/2016-10-8.json",
        headers  = {
        'Authorization':"Bearer"+AUTH,
        'Accept-Header': 'en_US'
             }
    )
    r3 = r3.json()
    #print(r3)
    with open ('./sleep_log_'+str(currdate)+'.json', 'w+') as outfile:
        json.dump(r3, outfile)


def get_hr_data():
    r2 = requests.get(
        url = 'https://api.fitbit.com/1/user/37T8GV/activities/heart/date/today/1d.json',
        headers  = {
        'Authorization':"Bearer"+AUTH,
        'Accept-Header': 'en_US'
        }
    )
    r2 = r2.json()
    with open('./hr_data.json', 'w+') as outfile:
        json.dump(r2, outfile)


def get_weight_data():
    r2 = requests.get(
        url = 'https://api.fitbit.com/1/user/37T8GV/body/log/weight/goal.json',
        headers  = {

        'Authorization':"Bearer"+AUTH,
        'Accept-Header': 'en_US'
        }
    )
    weight = r2.json()

    with open('./weight.json', 'w') as outfile:
        json.dump(weight,outfile)
    outfile.close()
make_request()
