import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# Connecting to database

conn = sqlite3.connect("GoldDatabase.db")
cur = conn.cursor()

# Reading stock data from excel

bankofamerica_data = pd.read_excel("BankOfAmericaMerrilLynch.xlsx")
barclays_data = pd.read_excel("Barclays.xlsx")
citigroup_data = pd.read_excel("Citigroup.xlsx")
creditsuisse_data = pd.read_excel("CreditSuisse.xlsx")
deutschebank_data = pd.read_excel("DeutscheBankAG.xlsx")
goldmansachsgroup_data = pd.read_excel("GoldmanSachsGroup.xlsx")
hsbc_data = pd.read_excel("HSBC.xlsx")
jpmorgan_data = pd.read_excel("JPMorgan.xlsx")
morganstanley_data = pd.read_excel("MorganStanley.xlsx")
ubsgroup_data = pd.read_excel("UBSgroup.xlsx")


data_lista_avg = []
values_avg = []
less_than_zero = []
zero_zero = []
zero_to_twenty = []
twenty_to_fourthy = []
fourthy_to_sixty = []
sixty_to_eighty = []
eighty_and_more = []
data_lista_max = []
values_max = []
data_list_min = []
value_min = []
list_of_date = []
list_of_price = []
list_of_dats = []
list_of_percentage = []
list_of_price = []
official_list_of_percentage = []

# Calculating average price value for each year (for gold)
def avrage_value_per_year(year):
    i = 0
    while i <= 70:
        cur.execute(f'SELECT Date, AVG(Price) FROM monthlydata WHERE Date LIKE "%{year}%"')
        for row in cur.fetchall():
            data_lista_avg.append(year)
            values_avg.append(row[1])
            i = i + 1
            year = year + 1

# Def to check max price value for each year (for gold)
def max_value_per_year(year):
    i = 0
    while i <= 70:
        cur.execute(f'SELECT Date, MAX(Price) FROM monthlydata WHERE Date LIKE "%{year}%"')
        for row in cur.fetchall():
            data_lista_max.append(year)
            values_max.append(row[1])
            i = i + 1
            year = year + 1

# Def to check the smallest price value for each year (for gold)
def min_value_per_year(year):
    i = 0
    while i <= 70:
        cur.execute(f'SELECT Date, MIN(Price) FROM monthlydata WHERE Date LIKE "%{year}%"')
        for row in cur.fetchall():
            data_list_min.append(year)
            value_min.append(row[1])
            i = i + 1
            year = year + 1

# Def to check top ten price values for monthly data (for gold)
def top_ten_monthly():
    cur.execute("SELECT Date, Price FROM monthlydata ORDER BY Price DESC")
    print(cur.fetchmany(10))
    cur.execute("SELECT Date, Price FROM monthlydata ORDER BY Price DESC")
    for row in cur.fetchmany(10):
        list_of_date.append(row[0])
        list_of_price.append(row[1])
    plt.plot(list_of_date, list_of_price)
    plt.title("Top ten gold price monthly ever")
    plt.grid()
    plt.show()
    list_of_date.clear()
    list_of_price.clear()

# Def to check top ten price values for annual data (for gold)
def top_ten_annualy():
    cur.execute("SELECT Date, Price FROM annualdata ORDER BY Price DESC")
    print(cur.fetchmany(10))
    cur.execute("SELECT Date, Price FROM annualdata ORDER BY Price DESC")
    for row in cur.fetchmany(10):
        list_of_date.append(row[0])
        list_of_price.append(row[1])
    plt.plot(list_of_date, list_of_price)
    plt.title("Top ten annual gold price ever")
    plt.grid()
    plt.show()
    list_of_date.clear()
    list_of_price.clear()

# Def to check ten smallest price values for monthly data (for gold)
def top_ten_smallest_monthly():
    cur.execute("SELECT Date, Price FROM monthlydata ORDER BY Price ASC")
    print(cur.fetchmany(10))
    cur.execute("SELECT Date, Price FROM monthlydata ORDER BY Price ASC")
    for row in cur.fetchmany(10):
        list_of_date.append(row[0])
        list_of_price.append(row[1])
    plt.plot(list_of_date, list_of_price)
    plt.title("Top ten smallests gold values monthly ever")
    plt.grid()
    plt.show()
    list_of_date.clear()
    list_of_price.clear()

# Def to check ten smallest price values for annualy data (for gold)
def top_ten_smallest_annualy():
    cur.execute("SELECT * FROM annualdata ORDER BY Price")
    print(cur.fetchmany(10))
    cur.execute("SELECT Date, Price FROM annualdata ORDER BY Price ASC")
    for row in cur.fetchmany(10):
        list_of_date.append(row[0])
        list_of_price.append(row[1])
    plt.plot(list_of_date, list_of_price)
    plt.title("Top ten smallests annual gold values ever")
    plt.grid()
    plt.show()
    list_of_date.clear()
    list_of_price.clear()

# Possibilitie to choose one year and plott dates and prices for this year (for gold)
def graph_for_one_year(data):
    cur.execute(f'SELECT Date, Price FROM monthlydata WHERE Date LIKE "%{data}%"')
    for row in cur.fetchall():
        list_of_date.append(row[0])
        list_of_price.append(row[1])
    plt.bar(list_of_date, list_of_price)
    plt.title(f"Graph for monthly price for {data}")
    plt.grid()
    plt.show()
    list_of_date.clear()
    list_of_price.clear()


# graph_for_amayw_years("1950")

# Plotting graph for all years and prices (for gold)
def graph_for_all():
    cur.execute('SELECT Date, Price FROM annualdata')
    for row in cur.fetchall():
        list_of_date.append(row[0])
        list_of_price.append(row[1])
    plt.plot(list_of_date, list_of_price)
    plt.grid()
    plt.title("Graph for all years")
    plt.show()
    list_of_date.clear()
    list_of_price.clear()

# Prepering data to calculating percentage 
def percentage(data):
    i = 0
    while i <= 70:
        list_of_dats.append(data)
        cur.execute(f"SELECT Date, Price FROM monthlydata WHERE Date LIKE '%{data}%'")
        for row in cur.fetchall():
            list_of_price.append(row[1])
        data = data + 1
        i = i + 1
        list_of_percentage.append(list_of_price[0])
        list_of_percentage.append(list_of_price[-1])
        list_of_price.clear()

# Calculating percentage value for each year (gold value)
def calculating_percentage_per_year():
    i = 0
    j = 1
    while j <= 141:
        percentage = ((list_of_percentage[j] - list_of_percentage[i]) / list_of_percentage[i]) * 100
        official_list_of_percentage.append(percentage)
        i = i + 2
        j = j + 2

# Distribution of gold values
def distribution_of_values():
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
    zero1 = str("-26% to -1%")
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
    plt.title("Distribution of values")
    plt.grid()
    plt.show()


avrage_value_per_year(1950)
max_value_per_year(1950)
min_value_per_year(1950)
plt.plot(data_lista_avg, values_avg, "r", label="Average values")
plt.grid()
plt.MaxNLocator(20)
plt.xlabel("Years")
plt.ylabel("Gold price (USD)")
plt.title("Comparing the average gold price, minimum gold price and maximum gold price")
plt.legend(loc="upper left")
plt.show()
percentage(1950)
calculating_percentage_per_year()
plt.plot(list_of_dats, official_list_of_percentage)
plt.grid()
plt.title("Graph for percentage values for gold")
plt.show()
top_ten_annualy()
top_ten_monthly()
top_ten_smallest_monthly()
top_ten_smallest_annualy()
# graph for one year optionally
