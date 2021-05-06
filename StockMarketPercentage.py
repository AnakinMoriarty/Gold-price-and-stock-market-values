import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('GoldDatabase.db')
cur = conn.cursor()

list_of_dats = []
list_of_percentage = []
list_of_price = []
less_than_zero = []
zero_zero = []
zero_to_twenty = []
twenty_to_fourthy = []
fourthy_to_sixty = []
sixty_to_eighty = []
eighty_and_more = []
official_list_of_percentage = []

# Calculating percentage value for each year for top stock market companies and showing how they are distribute

def percentage(name, year):
    i = 0
    max = 2017 - year
    while i <= max:
        list_of_dats.append(year)
        cur.execute(f"SELECT Date, High FROM '{name}' WHERE Date LIKE '%{year}%'")
        for row in cur.fetchall():
            list_of_price.append(row[1])
        year = year + 1
        i = i + 1
        list_of_percentage.append(list_of_price[0])
        list_of_percentage.append(list_of_price[-1])
        list_of_price.clear()


def calculating_percentage(name):
    i = 0
    j = 1
    while j <= len(list_of_percentage):
        percent = ((list_of_percentage[j] - list_of_percentage[i]) / list_of_percentage[i]) * 100
        official_list_of_percentage.append(percent)
        i = i + 2
        j = j + 2
    plt.plot(list_of_dats, official_list_of_percentage, "o")
    plt.grid()
    plt.title(f"{name}")
    plt.show()


def distribution_of_values(name):
    for element in official_list_of_percentage:
        if element > 0 and element <= 20:
            zero_to_twenty.append(element)
        elif element == 0:
            zero_zero.append(element)
        elif element < 0:
            less_than_zero.append(element)
        elif element > 20 and element <= 40:
            twenty_to_fourthy.append(element)
        elif element > 40 and element <= 60:
            fourthy_to_sixty.append(element)
        elif element > 60 and element <= 80:
            sixty_to_eighty.append(element)
        elif element > 80:
            eighty_and_more.append(element)
    zero = len(less_than_zero)
    zero_zers = len(zero_zero)
    first = len(zero_to_twenty)
    second = len(twenty_to_fourthy)
    third = len(fourthy_to_sixty)
    forth = len(sixty_to_eighty)
    fifth = len(eighty_and_more)
    zero1 = str("-100% to -1%")
    zero_zers1 = str("0%")
    first1 = str("1% to 20%")
    second1 = str("21% to 40%")
    third1 = str("41% to 60%")
    fourth1 = str("61% to 80%")
    fifth1 = str("81% and more")
    plt.bar(zero1, zero)
    plt.bar(zero_zers1, zero_zers)
    plt.bar(first1, first)
    plt.bar(second1, second)
    plt.bar(third1, third)
    plt.bar(fourth1, forth)
    plt.bar(fifth1, fifth)
    plt.title(f"{name} distribution of values")
    plt.grid()
    plt.show()
    list_of_dats.clear()
    list_of_percentage.clear()
    list_of_price.clear()
    less_than_zero.clear()
    zero_zero.clear()
    zero_to_twenty.clear()
    twenty_to_fourthy.clear()
    fourthy_to_sixty.clear()
    sixty_to_eighty.clear()
    eighty_and_more.clear()
    official_list_of_percentage.clear()


percentage('hsbc', 1999)
calculating_percentage('HSBC percentage')
distribution_of_values('HSBC')

percentage('barclays', 2005)
calculating_percentage('Barclays percentage')
distribution_of_values("Barclays")

percentage('citigroup', 1970)
calculating_percentage('Citigroup percentage')
distribution_of_values("Citigroup")

percentage('bankofamerica', 1986)
calculating_percentage('Bank of America Merril Lynch percentage')
distribution_of_values("Bank of America Merril Lynch")

percentage('creditsuisse', 2005)
calculating_percentage('Credit Suisse percentage')
distribution_of_values("Credit Suisse")

percentage('deutschebank', 2005)
calculating_percentage('Deutsche Bank AG percentage')
distribution_of_values("Deutsche Bank AG")

percentage('goldmansachsgroup', 1999)
calculating_percentage('Goldman Sachs Group percentage')
distribution_of_values("Goldman Sachs Group")

percentage('jpmorgan', 1970)
calculating_percentage('JP Morgan percentage')
distribution_of_values("JP Morgan")

percentage('morganstanley', 2005)
calculating_percentage('Morgan Stanley percentage')
distribution_of_values("Morgan Stanley")

percentage('ubsgroup', 2014)
calculating_percentage('UBS Group percentage')
distribution_of_values("UBS Group")
