import pandas as pd
import matplotlib.pyplot as plt

# Reading data from excel

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

list_of_companies = [bankofamerica_data, barclays_data, citigroup_data, creditsuisse_data, deutschebank_data,
                     goldmansachsgroup_data, hsbc_data, morganstanley_data, ubsgroup_data]
list_of_company_names = ["Bank on America Merril Lynch", "Barclays", "Citigroup", "Credit Suisse", "Deutsche Bank AG",
                         "Goldman Sachs Group", "HSBC", "Morgan Stanley", "UBS Group"]

# Plotting graph for every stock market company

def normal_graph(name, number):
    name.plot(x='Date', y='High', color='blue')
    plt.title(list_of_company_names[number])
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

i = 0
for name in list_of_companies:
    normal_graph(name, i)
    i = i + 1
