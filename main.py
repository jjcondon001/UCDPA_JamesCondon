#Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read in the csv file
games = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv", index_col=0)

#Drop the games with missing values
games = games.dropna()

#Sort games by year
games = games.sort_values("Year_of_Release")

#Reduce games to after 2000
games = games[games["Year_of_Release"] >= 2000]

#Print the games DataFrame
#print(games.loc[:, "Platform":"Year_of_Release"])

sns.catplot(data = games,
            y = "Global_Sales",
            x = "Rating",
            kind = "bar")

plt.show()