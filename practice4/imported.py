from typing import Dict
from import_this import RACE_DATA
import datetime

def get_place(racer_place):
    return racer_place[1].get('FinishedPlace')

sorted_data = sorted(RACE_DATA.items(), key=get_place)

for racer_id, racer_info in sorted_data[:3]:
    if racer_info['FinishedPlace'] == 1:
        print(f"Выиграл - {racer_info['RacerName']}, поздравляем!")
    print("Имя гонщика:", racer_info['RacerName'])
    print("Название команды:", racer_info['RacerTeam'])
    print("Занятое место:", racer_info['FinishedPlace'])
    print("Время заезда (HMS): ", str(datetime.timedelta(seconds=(racer_info['FinishedTimeSeconds']))))
    print()


