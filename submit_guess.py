#!/usr/bin/env python3
import requests
import getpass

BASE_URL = "https://9n52ntmq97.execute-api.us-east-1.amazonaws.com/prod"
REQUEST_URL = "{base_url}/guess".format(base_url=BASE_URL)
WRONG = {
    "Arizona Cardinals": 1,
    "Atlanta Falcons": 2,
    "Baltimore Ravens": 3,
    "BearReport.com": 4,
    "BreakingBurgundy.com": 5,
    "Buffalo Bills": 6,
    "Carolina Panthers": 7,
    "Chicago Bears": 8,
    "Cincinnati Bengals": 9,
    "Cleveland Browns": 10,
    "CowboysHQ.com": 11,
    "Dallas Cowboys": 12,
    "Denver Broncos": 13,
    "Detroit Lions": 14,
    "DolphinsReport.com": 15,
    "Green Bay Packers": 16,
    "Houston Texans": 17,
    "Indianapolis Colts": 18,
    "Jacksonville Jaguars": 19,
    "JaguarsForever.com": 20,
    "Kansas City Chiefs": 21,
    "Los Angeles Chargers": 22,
    "Los Angeles Rams": 23,
    "Miami Dolphins": 24,
    "MileHighHuddle.com": 25,
    "Minnesota Vikings": 26,
    "New England Patriots": 27,
    "New Orleans Saints": 28,
    "New York Giants": 29,
    "New York Jets": 30,
    "Oakland Raiders": 31,
    "PackerReport.com": 32,
    "PatriotsInsider.com": 33,
    "Philadelphia Eagles": 34,
    "Pittsburgh Steelers": 35,
    "San Francisco 49ers": 36,
    "Seattle Seahawks": 37,
    "StateoftheTexans.com": 38,
    "SteelCityInsider.net": 39,
    "Tampa Bay Buccaneers": 40,
    "Tennessee Titans": 41,
    "TheGiantsBeat.com": 42,
    "theOBR.com": 43,
    "VikingUpdate.com": 44,
    "Washington Redskins": 45,
}


def submit_request(guess, username):
    print("Submitting guess!")
    resp = requests.post(REQUEST_URL, json={
        "results": guess,
        "username": username
    })
    print(resp.text)


if __name__ == '__main__':
    submit_request(WRONG, getpass.getuser())
