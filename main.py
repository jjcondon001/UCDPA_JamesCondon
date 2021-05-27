#Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import sum

#Read in the csv file
games = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv", index_col=0)

#Drop the games with missing values
games = games.dropna()

#Sort games by year
games = games.sort_values("Year_of_Release")

#Convert Year from floats to ints
games["Year_of_Release"] = games["Year_of_Release"].astype(int)

#Reduce games to after 2000
games = games[games["Year_of_Release"] >= 2000]

#Print the games DataFrame
#print(games.loc[:, "Platform":"Year_of_Release"])

#Change style
sns.set_style("whitegrid")

#A variable for the age ratings in order
ratings_order = ["E", "E10+", "T", "M", "AO", "RP"]

#Plot global sales by age rating
age = sns.catplot(data = games,
                  y = "Global_Sales",
                  x = "Rating",
                  kind = "bar",
                  order = ratings_order)

#Annotate the plot
age.fig.suptitle("Sales of Each Age Rating Group")
age.set(xlabel = "Age Ratings",
        ylabel = "Sales in Millions")

#Save the global sales plot
age.savefig("Age_Global_Sales.png")

#Create a 2x2 subplot
fig, ax = plt.subplots(2, 2, figsize = (8, 9.5))

#A function to plot the sales by region
def plot_sales(axis, sales, colour, country):
    sns.barplot(ax = axis,
                data = games,
                x = "Rating",
                y = sales,
                estimator = sum,
                order = ratings_order,
                color = colour,
                ci = None)
    axis.set_xlabel("Age Rating")
    axis.set_ylabel("Sales in Millions")
    axis.set_title("Sales in " + country, color = colour)

#Ploting the regional sales
plot_sales(ax[0, 0], "NA_Sales", "red", "North America")
plot_sales(ax[0, 1], "EU_Sales", "blue", "Europe")
plot_sales(ax[1, 0], "JP_Sales", "green", "Japan")
plot_sales(ax[1, 1], "Other_Sales", "purple", "Other Countries")

#Save regional sales figure
fig.savefig("Sales by Region.png")

#Convert the User Score column to a float
games["User_Score"] = games["User_Score"].astype(float)

#Create plot to compare user vs critic score
fig2, ax2 = plt.subplots(1, 2, figsize = (12, 6))

#Create regression plots for user vs critic score
#Plot User scores vs sales
sns.regplot(ax = ax2[0],
            data = games,
            x = "User_Score",
            y = "Global_Sales",
            scatter_kws = {"color":"red", "alpha":0.2},
            line_kws = {"color":"black", "alpha":1})
ax2[0].set_xlabel("Average User Scores by Metacritic Subscribers")
ax2[0].set_ylabel("Sales in Millions")
#Plot critic scores vs sales
sns.regplot(ax = ax2[1],
            data = games,
            x = "Critic_Score",
            y = "Global_Sales",
            scatter_kws = {"color":"green", "alpha":0.2},
            line_kws = {"color":"black", "alpha":1})
ax2[1].set_xlabel("Average Score on Metacritic by Professional Critics")
ax2[1].set_ylabel("Sales in Millions")
#Add titles
fig2.suptitle("How Sales are Affected by User Scores vs Critic Scores")

#Save the sales vs scores graph
fig2.savefig("Critic v User score")

#Create separate dataframes for individual genres
shooter = games[games["Genre"] == "Shooter"]
platformer = games[games["Genre"] == "Platform"]
sport = games[games["Genre"] == "Sports"]
sim = games[games["Genre"] == "Simulation"]
#Merge the different genre dataframes
frames = [shooter, platformer, sport, sim]
genre_df = pd.concat(frames)

#plot a line plot for the genres
genre_graph = sns.catplot(data = genre_df,
                          x = "Year_of_Release",
                          y = "Global_Sales",
                          kind = "point",
                          ci = None,
                          hue = "Genre",
                          alpha = 0.8,
                          estimator = sum)

genre_graph.fig.suptitle("Sales in Various Genres from 2000-2016")
genre_graph.set(xlabel = "Year of Release",
                ylabel = "Average Sales of Games in Millions")
genre_graph.set_xticklabels(rotation = 45)

#Save the genre sales graph
genre_graph.savefig("Sales by Genre.png")

#Display plots
plt.show()