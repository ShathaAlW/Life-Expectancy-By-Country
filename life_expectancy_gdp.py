import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("country_data.csv")


# Quartiles of life expectency
life_expectancy = data['Life Expectancy']
life_expectancy_quartiles = np.quantile(life_expectancy,[0.25, 0.5, 0.75])
print("life expectancy quartiles of all countries:")
print(life_expectancy_quartiles)


# Splitting data by GDP into low and high GDP countries
gdp = data['GDP']
median_gdp = np.quantile(gdp, 0.5)
print(median_gdp)
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] >= median_gdp]


# how the life expectancy of low and high gdp groups compare to each other
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])
print("life expectancy quartiles of low GDP countries:")
print(low_gdp_quartiles)

high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.5, 0.75])
print("life expectancy quartiles of high GDP countries:")
print(high_gdp_quartiles)

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP", color= 'r')
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.title('The impact of GDP on life expectancy')
plt.xlabel('life expectancy')
plt.legend()
plt.show()
