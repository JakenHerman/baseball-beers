from matplotlib import pyplot as plt
import pandas as pd

# read data from CSV into local variable
data = pd.read_csv('MLBBeerPrices.csv', skipinitialspace=True, sep=',')

# select beers specifically from Astros
astros_beers = data[data.Nickname == 'Astros']

# create a plot within a three-plot canvas in the first position
# that shows the trend of Beer prices at MMP from 2013-2018
plt.subplot(3, 1, 1)
plt.title('Price of Beer at MMP (USD)')
plt.xlabel('Year')
plt.ylabel('Price (USD)')
plt.plot(astros_beers.Year, astros_beers.Price)

# create a plot within a three-plot canvas in the second position
# that shows the trend of Beer prices per Ounce at MMP from 2013-2018
plt.subplot(3, 1, 3)
plt.title('Price of Beer per Ounce at MMP (USD)')
plt.xlabel('Year')
plt.ylabel('PPO')
plt.plot(astros_beers.Year, astros_beers['Price per Ounce'])
plt.show()
