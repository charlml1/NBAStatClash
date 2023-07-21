# NBAStatClash

## Introduction
NBAStatClash is a website dedicated to comparing the stats of NBA players from the 2022-2023 regular season. The primary aim is to assist fantasy basketball enthusiasts in drafting players for the upcoming 2023-2024 season. To cater to different fantasy leagues, there are two separate webpages—one focused on points leagues and the other on category leagues. The main reason I created this website was to work on my web development skills and to learn Django.

## Screenshots
#### Categories Page
Here is how the website looks for comparing players in category leagues. Simply select the two players you wish to compare and click "Submit" to view the results. First, you'll see both players' overall stats for the 2022-2023 regular season. Then, those stats will be compared across each of the nine main categories. The winner of each category is shown in parentheses after each stat.
![Screenshot (75)](https://github.com/charlml1/NBAStatClash/assets/44219118/72ae2f64-98e9-4a74-a212-6007f5b3bb39)

#### Points Page
Here is the webpage for comparing players in points leagues. Because there are tons of different ways to weight each category, the user can adjust the weights according to their specific league settings.
![Screenshot (77)](https://github.com/charlml1/NBAStatClash/assets/44219118/dff8e0ce-1196-4b42-a771-b84c7ba92136)

Once you've submitted the players you want to compare, the results will begin just like the categories page, displaying both players' regular season stats. However, the final comparison takes a different route, showcasing the average fantasy points scored by each player per game played. This fantasy point total is calculated using the user-defined weights for each stat in the Points Scoring System. 
![Screenshot (76)](https://github.com/charlml1/NBAStatClash/assets/44219118/efcfee99-2413-4108-8df9-05b8d2acae99)

## Technologies Used
Python - version 3.10.2

Django - version 4.2.2

## Launch
To run the program, there is a requirements.txt file which has all the packages that this project depends on. If you don't know what a requirements.txt file is or how to use it, [this website](https://learnpython.com/blog/python-requirements-file/) gives a quick guide on it and how to install packages using it.
