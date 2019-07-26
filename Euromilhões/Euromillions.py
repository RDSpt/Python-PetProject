import requests
from datetime import datetime
import collections
import matplotlib.pyplot as plt
import numpy as np

def draw_bar_chart(data):

    index = np.arange(len(data))
    plt.bar(index, data.values())
    plt.xlabel('Number')
    plt.ylabel('No of Occurence')
    plt.xticks(index, data.keys())
    plt.show()


if __name__ == '__main__':
    r = requests.get('https://nunofcguerreiro.com/api-euromillions-json?result=all')
    r = r.json()
    allDrawns = r['drawns']
    print(allDrawns)
    toDealData = []
    for i in allDrawns:
        date_str = i['date']
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        if date.year > 2016:
            toDealData.append(i)
#     New Rules Data
    ballCounter = collections.Counter()
    starCounter = collections.Counter()
    for i in toDealData:
        # Count all balls
        balls = i['balls'].split(' ')
        for ball in balls:
            ballCounter[ball] += 1
        # Count all stars
        stars = i['stars'].split(' ')
        for star in stars:
            starCounter[star] +=1
    draw_bar_chart(ballCounter)
    draw_bar_chart(starCounter)
    sortedBalls = ballCounter.most_common()
    sortedStars = starCounter.most_common()
    print(sortedBalls)
    print(sortedStars)

