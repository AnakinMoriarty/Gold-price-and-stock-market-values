import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('GoldDatabase.db')
cur = conn.cursor()

date_list = []
values = []
average_values = []
list_of_date = []
list_of_price = []


def calculating_average(name, year):
    i = 0
    max = 2017 - year
    while i <= max:
        cur.execute(f"SELECT High FROM '{name}' WHERE Date LIKE '%{year}%'")
        for element in cur.fetchall():
            values.append(sum(element))
        date_list.append(year)
        avg = sum(values) / len(values)
        average_values.append(avg)
        values.clear()
        year = year + 1
        i = i + 1

# Comparing avg gold values per year to avg stock prices of top companies and ticking 2007-2009 crisis, and 2005 soared

def plotting_annual_data(name, year, scaling, value1=None, value2=None, value3=None):
    i = 0
    max = 2017 - year
    while i <= max:
        cur.execute(f'SELECT Price FROM annualdata WHERE Date LIKE "%{year}%"')
        for element in cur.fetchall():
            scaling_value = sum(element) / scaling
            list_of_price.append(scaling_value)
        list_of_date.append(year)
        year = year + 1
        i = i + 1
    if name != "ubsgroup":
        plt.plot(list_of_date, list_of_price, color="red") # annual data
        plt.plot(date_list, average_values, color="green")
        plt.annotate('2007 crisis start', xytext=(2007, average_values[-11] + value1)  ,xy=(2007, average_values[-11]), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
        plt.annotate('2009 crisis end', xytext=(2009, average_values[-9] + value2)  ,xy=(2009, average_values[-9]), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
        plt.annotate('2016 stocks soared', xytext=(2016, average_values[-2] + value3)  ,xy=(2016, average_values[-2]), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
        plt.xlabel("Date")
        plt.ylabel("Values")
        plt.grid()
        plt.title(f"{name} stock data comparing to gold value")
        plt.show()
    else:
        plt.plot(list_of_date, list_of_price, color="red") # annual data
        plt.plot(date_list, average_values, color="green")
        plt.grid()
        plt.title("UBS Group stock data comparing to gold value")
        plt.xlabel("Date")
        plt.ylabel("Values")
        plt.annotate('2016 stocks soared', xytext=(2016, average_values[-2] + value3)  ,xy=(2016, average_values[-2]), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
        plt.show()
    list_of_price.clear()
    list_of_date.clear()
    date_list.clear()
    values.clear()
    average_values.clear()


calculating_average('hsbc', 1999)
plotting_annual_data('HSBC', 1999, 17, 10, 50, -9)

calculating_average('barclays', 2005)
plotting_annual_data('Barclays', 2005, 20, 5, 6, 9)

calculating_average('citigroup', 1970)
plotting_annual_data('Citigroup', 1970, 7, -50, 50, 30)

calculating_average('bankofamerica', 1986)
plotting_annual_data('Bank of America Merril Lynch', 1986, 20, 5, 6, 11)

calculating_average('creditsuisse', 2005)
plotting_annual_data('Creditsuisse', 2005, 20, 5, 6, 9)

calculating_average('deutschebank', 2005)
plotting_annual_data('Deutsche Bank AG', 2005, 17, -20, 6, 15)

calculating_average('goldmansachsgroup', 1999)
plotting_annual_data('Goldman Sachs Group', 1999, 17, 5, 30, -13)

calculating_average('jpmorgan', 1970)
plotting_annual_data('JP Morgan', 1970, 17, 5, -10, -12)

calculating_average('morganstanley', 2005)
plotting_annual_data('Morgan Stanley', 2005, 17, 5, 6, -9)

calculating_average('ubsgroup', 2014)
plotting_annual_data('ubsgroup', 2014, 17, value3=5)
