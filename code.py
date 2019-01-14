# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data) 
 
# Code starts here
#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
def deliveries_count(data=data):
    count = 0
    innings_delivered = data["innings"][0]["1st innings"]["deliveries"]
    for m, x in enumerate(innings_delivered):
        dict = innings_delivered[m]
        for key,value in dict.items():
            if dict[key]["batsman"] == "SC Ganguly":
                count = count + 1
    return count
deliveries_count()

#  Who was man of the match and how many runs did he scored ?


#  Which batsman played in the first inning?
def first_batsman(data):
    name = data['innings'][0]['1st innings']['deliveries'][0]
    return (name["0.1"]["batsman"])
first_batsman(data)


# Which batsman had the most no. of sixes in first inning ?


# Find the names of all players that got bowled out in the second innings.
def bowled_out(data=data):
    bowled_players = []
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        for deli_num in delivery:
            if 'wicket' in delivery[deli_num] and delivery[deli_num]['wicket']['kind']=='bowled':
                bowled_players.append(delivery[deli_num]['batsman'])

    return bowled_players
bowled_out()


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
def extras_runs(data=data):
    Innings_1  , Innings_2 = 0 , 0
    deliveries1 = data ['innings'][0]["1st innings"]['deliveries']
    for delivery in deliveries1:
        for deli_num, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    Innings_1 += delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                    Innings_1 += delivery_info['extras']['legbyes']
                
    deliveries2 = data ['innings'][1]["2nd innings"]['deliveries']
    for delivery in deliveries2:
        for deli_num, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    Innings_2 += delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                    Innings_2 += delivery_info['extras']['legbyes']


    print("Total no in innings_2: ",Innings_2)
    print("Total no in innings_1: ",Innings_1)
    difference = Innings_2 - Innings_1
    return difference
extras_runs()



# Code ends here


