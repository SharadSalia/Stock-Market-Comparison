import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import plotly.graph_objects as go

def main_menu():
    print('WELCOME TO MAIN MENU')
    print('HERE ARE THE STOCK DATA OF 4 COMPANIES')
    print('[1] Skechers')
    print('[2] Tesla')
    print('[3] Apple')
    print('HERE YOU CAN CHECK EVERY DETAIL OF STOCK DATA ABOUT THESE 3 COMPANIES')
    print('WE HAVE TAKEN OPEN PRICE , CLOSE PRICE , HIGH PRICE ,AND LOW PRICE OF ALL 3 COMPANIES')
    print('OPEN PRICE : Price when Stock Market Opens ') 
    print('CLOSE PRICE : Price when Stock Market Closed')
    print('HIGH PRICE : Highest price on that particular day')
    print('LOW PRICE : Lowest price on that particular day')
    print('THIS DATA IS FROM PAST 10 YRS [QUATERLY]')
    print('DOWN HERE YOU HAVE OPTIONS TO SEE THEIR STOCK DATA') 
    print('Read Data From File In Different Way')
    print('1. Read CSV files')
    print('==========================================') 
    print('Data Visualization')
    print('2. Line Chart') 
    print('3. Bar Chart')
    print('4. Scatter Chart')
    print('5. Pie Chart')
    print('6. Histogram')
    print('7. Candlestick Chart') 
    print('==========================================')
    print('Apply the manipulation in the records of CSV file')
    print('8. Sorting the data as per your choice')
    print('9. Read Top to Bottom records from file as per requirement')
    print('10. Read specific columns')
    print('==========================================')
    print('HERE ARE OPTIONS FROM 1 TO 10 PRESENTING DIFFERENT FORMS OF GRAPH & DATA SORTING OF OUR STOCK DATA')
#================================================================================= #==============================================================================
def Read_CSV():
    print('Press 1 Read csv file of Skechers.Inc') 
    print('Press 2 Read csv file of Tesla.Inc') 
    print('Press 3 Read csv file of Apple.Inc')
############################################################### 
op = (int(input("enter your choice")))
def Skechers_csv():
    print("reading data from csv file ") 
    df=pd.read_csv("E:\Sharad\Skechers.csv",index_col=0) 
    print(df)
################################################################ 
def Tesla_csv():
    print("reading data from csv file ") 
    df=pd.read_csv("E:\Sharad\Tesla.csv",index_col=0) 
    print(df)
################################################################ 
def Apple_csv():
    print("reading data from csv file ")
    df=pd.read_csv("E:\Sharad\Apple.csv",index_col=0)
    print(df) 
###############################################################
if op==1: Skechers_csv()
elif op==2: Tesla_csv()
elif op==3: Apple_csv()
#================================================================================= 
#=================================================================================
def Line_Chart(): 
    df=pd.read_csv("E:\Sharad\SKX.csv") 
    dt=df["Date"]
    ops=df["Open [S]"]
    his=df["High [S]"]
    los=df["Open [S]"]
    cls=df["Close [S]"]
    opt=df["Open [T]"]
    hit=df["High [T]"]
    lot=df["Low [T]"]
    clt=df["Close [T]"]
    opa=df["Open [A]"]
    hia=df["High [A]"]
    loa=df["Low [A]"]
    cla=df["Close [A]"] 
    plt.xlabel("Dates") 
    plt.xticks(rotation="vertical")
    print('''Select specific line chart as given below:
Press 1 to print the Stock data of Skechers.Inc
Press 2 to print the Stock data of Tesla.Inc
Press 3 to print the Stock data of Apple.Inc
Press 4 to compare the Stock data of Skechers & Tesla 
Press 5 to compare the Stock data of Skechers & Apple Press 6 to compare the Stock data of Tesla & Apple Press 7 to comapre the stock data of All 3 Companies
''')
    op = (int(input("enter your choice")))
#####################################################################
def Skechers(): 
    print(""" Select specific line chart as given below
    Press 1 to for graph of date and opening stock price 
    Press 2 to for graph of date and closing stock price 
    Press 3 to for graph of date and maximum stock price 
    Press 4 to for graph of date and lowest stock price """)
    op=(int(input("enter your choice"))) 
    if op==1:
        plt.plot(dt,ops,label="opening stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,ops,colors='skyblue',alpha=0.4) 
    elif op==2:
        plt.plot(dt,cls,label="closing stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,cls,colors='skyblue',alpha=0.4) 
    elif op==3:
        plt.plot(dt,his,label="Highest stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,his,colors='skyblue',alpha=0.4) 
    elif op==4:
        plt.plot(dt,los,label="lowest stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,los,colors='skyblue',alpha=0.4) 
    else:
        print("Enter valid input")

    plt.ylabel("Stock Value (in $)") 
    plt.title("Skechers Stock Data") 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
################################################################### 
def Tesla():
    print("""Select specific line chart as given below
    Press 1 to for graph of date and opening stock price 
    Press 2 to for graph of date and closing stock price 
    Press 3 to for graph of date and maximum stock price 
    Press 4 to for graph of date and lowest stock price """)
    op=int(input("enter your choice")) 
    if op==1:
        plt.plot(dt,opt,label="opening stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,opt,colors='skyblue',alpha=0.4) 
    elif op==2:
        plt.plot(dt,clt,label="closing stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,clt,colors='skyblue',alpha=0.4)
    elif op==3:
        plt.plot(dt,hit,label="Highest stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,hit,colors='skyblue',alpha=0.4) 
    elif op==4:
        plt.plot(dt,lot,label="lowest stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,lot,colors='skyblue',alpha=0.4) 
    else:
        print("Enter valid input") 
    
    plt.ylabel("Stock Value (in $)") 
    plt.title("Tesla Stock Data") 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
################################################################################## ## 
def Apple():
    print("""Select specific line chart as given below
    Press 1 to for graph of date and opening stock price 
    Press 2 to for graph of date and closing stock price 
    Press 3 to for graph of date and maximum stock price 
    Press 4 to for graph of date and lowest stock price """)
    op=(int(input("enter your choice"))) 
    if op==1:
        plt.plot(dt,opa,label="opening stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,opa,colors='skyblue',alpha=0.4) 
    elif op==2:
        plt.plot(dt,cla,label="closing stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,cla,colors='skyblue',alpha=0.4)
    elif op==3:
        plt.plot(dt,hia,label="Highest stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,hia,colors='skyblue',alpha=0.4) 
    elif op==4:
        plt.plot(dt,loa,label="lowest stock value",marker='*',markeredgecolor='g',markerfacecolor='c')
        plt.stackplot(dt,loa,colors='skyblue',alpha=0.4) 
    else:
        print("Enter valid input") 
        
    plt.title("Apple Stock Data") 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show() 
####################################################################### 
def Skechers_Tesla():
    print("Here is The comparison of highest stock data of Skechers and Tesla") 
    plt.plot(dt,his,'b',label="[Skechers]",marker='*',markeredgecolor='g',markerfacecolor='c') 
    plt.stackplot(dt,his,colors='skyblue',alpha=0.4) 
    plt.plot(dt,hit,'g',label="[Tesla]",marker='o',markeredgecolor='c',markerfacecolor='g') 
    plt.stackplot(dt,hit,colors='k',alpha=0.4)
    plt.ylabel("Highest Stock Value (in $)") 
    plt.title("Skechers v/s Tesla Stock Data") 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
####################################################################### 
def Skechers_Apple():
    print("Here is The comparison of highest stock data of Skechers and Apple") 
    plt.plot(dt,his,'b',label="[Skechers]",marker='*',markeredgecolor='g',markerfacecolor='c') 
    plt.stackplot(dt,his,colors='skyblue',alpha=0.4)
    plt.plot(dt,hia,'g',label="[Apple]",marker='o',markeredgecolor='c',markerfacecolor='g') 
    plt.stackplot(dt,hia,colors='k',alpha=0.4)
    plt.ylabel("Highest Stock Value (in $)")
    plt.title("Skechers v/s Apple Stock Data")
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
################################################################################## 
def Tesla_Apple():
    print("Here is The comparison of highest stock data of Tesla and Apple") 
    plt.plot(dt,hit,'b',label="[Tesla]",marker='*',markeredgecolor='g',markerfacecolor='c') 
    plt.stackplot(dt,hit,colors='skyblue',alpha=0.4) 
    plt.plot(dt,hia,'g',label="[Apple]",marker='o',markeredgecolor='c',markerfacecolor='g') 
    plt.stackplot(dt,hia,colors='k',alpha=0.4)
    plt.ylabel("Highest Stock Value (in $)") 
    plt.title("Tesla v/s Apple Stock Data") 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
################################################################################## 
def S_T_A():
    print("Here is The comparison of highest stock data of Skechers, Tesla and Apple") 
    plt.plot(dt,his,'b',label="[Skechers]")
    plt.plot(dt,hit,'g',label="[Tesla]")
    plt.plot(dt,hia,'y',label="[Apple]")
    plt.ylabel("Highest Stock Value (in $)") 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
################################################################################## 
if op==1:
    Skechers() 
elif op==2:
    Tesla() 
elif op==3:
    Apple() 
elif op==4:
    Skechers_Tesla() 
elif op==5:
    Skechers_Apple() 
elif op==6:
    Tesla_Apple() 
elif op==7:
    S_T_A() 
else:
    print("enter valid input")
#================================================================================= 
#================================================================================= 
def Bar_Chart() :
    df=pd.read_csv("E:\Sharad\SKX.csv") 
    dt=df["Date"]
    ops=df["Open [S]"]
    his=df["High [S]"]
    los=df["Open [S]"] 
    cls=df["Close [S]"] 
    opt=df["Open [T]"] 
    hit=df["High [T]"] 
    lot=df["Low [T]"] 
    clt=df["Close [T]"] 
    opa=df["Open [A]"]
    hia=df["High [A]"] 
    loa=df["Low [A]"] 
    cla=df["Close [A]"] 
    plt.xlabel("dates") 
    plt.xticks(rotation="vertical") 
    print('''
Select specific line chart as given below:
Press 1 to print the Stock data of Skechers.Inc
Press 2 to print the Stock data of Tesla.Inc
Press 3 to print the Stock data of Apple.Inc
Press 4 to compare the Stock data of Skechers & Tesla Press 5 to compare the Stock data of Skechers & Apple Press 6 to compare the Stock data of Tesla & Apple Press 7 to compare the stock data of all four companies
    ''')
    op = (int(input("enter your choice")))
################################################################################## 
def Skechers():
    print("""Select specific Bar Charts as given below
    Press 1 for graph of date and opening stock price 
    Press 2 for graph of date and closing stock price 
    Press 3 for graph of date and maximum stock price 
    Press 4 for graph of date and lowest stock price 
    """)
    sk=(int(input("Enter your choice"))) 
    plt.title("Skechers Stock Value") 
    plt.grid(color='grey',alpha=0.3) 
    ind=np.arange(len(dt))
    width=0.25 
    if sk==1:
        plt.bar(dt,ops)
        plt.ylabel("Opening stock value(($))") 
    elif sk==2:
        plt.bar(dt,cls)
        plt.ylabel("Closing stock value($)") 
    elif sk==3:
        plt.bar(dt,his)
        plt.ylabel("Higest stock value($)") 
    elif sk ==4:
        plt.bar(dt,los)
        plt.ylabel("Lowest stock value($)") 
    else:
        print("Enter valid input")
    plt.show()
################################################################################## 
def Tesla():
    print("""
Select specific Bar Charts as given below Press 1 for Opening stock price
Press 2 for Closing stock price
Press 3 for Maximum stock price
Press 4 for Lowest stock price
    """)
    te=(int(input("Enter your choice"))) 
    plt.grid(color='grey',alpha=0.3) 
    ind=np.arange(len(dt))
    width=0.25
    plt.title("Tesla Stock Value")
    if te==1:
        plt.bar(dt,opt)
        plt.ylabel("Opening stock value($)") 
    elif te==2:
        plt.bar(dt,clt)
        plt.ylabel("Closing stock value($)") 
    elif te==3:
        plt.bar(dt,hit)
        plt.ylabel("Higest stock value($)") 
    elif te ==4:
        plt.bar(dt,lot)
        plt.ylabel("Lowest stock value($)") 
    else:
        print("Enter valid input")
    plt.show()
################################################################################ 
def Apple():
    print("""
Select specific Bar Charts as given below Press 1 for Opening stock price
Press 2 for Closing stock price
Press 3 for Maximum stock price
Press 4 for Lowest stock price
    """)
    ap=(int(input("Enter your choice"))) 
    plt.title("Apple Stock Value") 
    plt.grid(color='grey',alpha=0.3)
    ind=np.arange(len(dt)) 
    width=0.25
    if ap==1:
        plt.bar(dt,opa)
        plt.ylabel("Opening stock value($)") 
    elif ap==2:
        plt.bar(dt,cla)
        plt.ylabel("Closing stock value($)") 
    elif ap==3:
        plt.bar(dt,hia)
        plt.ylabel("Higest stock value($)") 
    elif ap==4:
        plt.bar(dt,loa)
        plt.ylabel("Lowest stock value($)") 
    else:
        print("Enter valid input")
    plt.show()
################################################################################## 
def Skechers_Tesla():
    ind=np.arange(len(dt))
    width=0.5
    print("Here is The comparison of highest stock data of Skechers and Tesla")
    plt.ylabel("Stock value($)") 
    plt.title("Skechers and Tesla Stock Comparison") 
    plt.grid(color='grey',alpha=0.3)
    plt.xticks(ind,dt) 
    plt.title("Maximun stock value")
    plt.bar(ind,his,width,label='Skechers') 
    plt.bar(ind+0.5,hit,width,label='Tesla') 
    plt.legend()
    plt.show()
################################################################################## 
def Skechers_Apple():
    ind=np.arange(len(dt))
    width=0.5
    print("Here is The comparison of highest stock data of Skechers and Apple") 
    plt.ylabel("Stock value($)")
    plt.title("Skechers and Apple Stock Comparison") 
    plt.grid(color='grey',alpha=0.3)
    plt.title("Maximun stock value") 
    plt.bar(ind,his,width,label='Skechers') 
    plt.bar(ind+0.5,hia,width,label='Apple') 
    plt.legend()
    plt.xticks(ind,dt) 
    plt.show()
################################################################################## 
def Tesla_Apple():
    ind=np.arange(len(dt))
    width=0.5
    print("Here is The comparison of highest stock data of Apple and Tesla")
    plt.ylabel("stock value($)")
    plt.title("Tesla and Apple Stock Comparison") 
    plt.grid(color='grey',alpha=0.3)
    plt.title("Maximun stock value") 
    plt.bar(ind,hit,width,label='Tesla') 
    plt.bar(ind+0.5,hia,width,label='Apple')
    plt.legend() 
    plt.xticks(ind,dt) 
    plt.show()
################################################################################## 
def S_T_A():
    ind=np.arange(len(dt))
    print("Here is The comparison of highest stock data of Skechers, Apple and Tesla")
    plt.ylabel("Stock values")
    width=0.3
    plt.title("Maximum stock value($)")
    plt.bar(ind,his,width,label='Skechers') 
    plt.bar(ind+0.33,hit,width,label='Tesla') 
    plt.bar(ind+0.33,hia,width,label='Apple') 
    plt.legend()
    plt.xticks(ind,dt)
    plt.show() 
#########################################################################
if op==1: 
    Skechers()
elif op==2: 
    Tesla() 
elif op==3:
    Apple() 
elif op==4:
    Skechers_Tesla() 
elif op==5:
    Skechers_Apple() 
elif op==6:
    Tesla_Apple() 
elif op==7:
    S_T_A()
else:
    print("Enter valid input")
#========================================================================= 
#========================================================================= 
def Scatter_Chart():
    df=pd.read_csv('E:\Sharad\SKX.csv') 
    dt=df["Date"]
    ops=df["Open [S]"]
    his=df["High [S]"]
    los=df["Open [S]"] 
    cls=df["Close [S]"] 
    opt=df["Open [T]"] 
    hit=df["High [T]"] 
    lot=df["Low [T]"] 
    clt=df["Close [T]"] 
    opa=df["Open [A]"] 
    hia=df["High [A]"] 
    loa=df["Low [A]"] 
    cla=df["Close [A]"] 
    print('''
Select specific Scatter chart as given below:
Press 1 to print the Stock data of Skechers.Inc
Press 2 to print the Stock data of Tesla.Inc
Press 3 to print the Stock data of Apple.Inc
Press 4 to compare the stock data of all three companies 
    ''')
    op = (int(input("enter your choice: "))) 
############################################################################
def Skechers(): 
    print("""Select specific Scatter chart as given below
    Press 1 to for comparison graph of opening stock price 
    Press 2 to for comparison graph of closing stock price 
    Press 3 to for comparison graph of maximum stock price 
    Press 4 to for comparison graph of lowest stock price 
    """)
    sk=(int(input("enter your choice: "))) 
    if sk==1:
        plt.scatter(dt,ops,color='c',label='Opening Stock Value') 
    elif sk==2:
        plt.scatter(dt,cls,color='c',label='Closing Stock Value') 
    elif sk==3:
        plt.scatter(dt,his,color='c',label='Highest Stock Value') 
    elif sk==4:
        plt.scatter(dt,los,color='c',label='Lowest Stock Value') 
    plt.xticks(rotation='vertical')
    plt.xlabel('Date')
    plt.ylabel('Stock Value (in $)')
    plt.title('Skechers Stock Value') 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
################################################################################ 
def Tesla():
    print("""Select specific Scatter chart as given below
    Press 1 to for comparison graph of opening stock price 
    Press 2 to for comparison graph of closing stock price 
    Press 3 to for comparison graph of maximum stock price 
    Press 4 to for comparison graph of lowest stock price
    """)
    sk=(int(input("enter your choice: ")))
    if sk==1:
        plt.scatter(dt,opt,color='c',label='Opening Stock Value')
    elif sk==2:
        plt.scatter(dt,clt,color='c',label='Closing Stock Value')
    elif sk==3:
        plt.scatter(dt,hit,color='c',label='Highest Stock Value')
    elif sk==4:
        plt.scatter(dt,lot,color='c',label='Lowest Stock Value')
    plt.xticks(rotation='vertical') 
    plt.xlabel('Date') 
    plt.ylabel('Stock Value (in $)') 
    plt.title('Tesla Stock Value') 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show() 
##########################################################################
def Apple(): 
    print("""Select specific Scatter chart as given below
    Press 1 to for comparison graph of opening stock price 
    Press 2 to for comparison graph of closing stock price 
    Press 3 to for comparison graph of maximum stock price 
    Press 4 to for comparison graph of lowest stock price 
    """)
    sk=(int(input("enter your choice: "))) 
    if sk==1:
        plt.scatter(dt,opa,color='c',label='Opening Stock Value') 
    elif sk==2:
        plt.scatter(dt,cla,color='c',label='Closing Stock Value') 
    elif sk==3:
        plt.scatter(dt,hia,color='c',label='Highest Stock Value') 
    elif sk==4:
        plt.scatter(dt,loa,color='c',label='Lowest Stock Value') 
    plt.xticks(rotation='vertical')
    plt.xlabel('Date')
    plt.ylabel('Stock Value (in $)')
    plt.title('Apple Stock Value') 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show()
########################################################################## 
def S_T_A():
    print("Here is The comparison of highest stock data of Skechers, Apple and Tesla") 
    plt.scatter(dt,his,color='c',label='Opening Stock [S]') 
    plt.scatter(dt,hit,color='r',label='Opening Stock [T]') 
    plt.scatter(dt,hia,color='m',label='Highest Stock [A]')
    plt.xticks(rotation='vertical')
    plt.xlabel('Date')
    plt.ylabel('Stock Value (in $)')
    plt.title('Skechers v/s Tesla v/s Apple Stock Value') 
    plt.grid(color='grey',alpha=0.3)
    plt.legend()
    plt.show() 
##########################################################################
if op==1: 
    Skechers()
elif op==2: 
    Tesla() 
elif op==3:
    Apple()
elif op==4: 
    S_T_A()
else:
    print("Enter valid input")
#======================================================================= 
#======================================================================= 
def Pie_Chart():
    df=pd.read_csv("E:\Sharad\SKX3.csv") 
    dt=df["Date"]
    ops=df["Open [S]"]
    his=df["High [S]"]
    los=df["Open [S]"] 
    cls=df["Close [S]"] 
    opt=df["Open [T]"] 
    hit=df["High [T]"] 
    lot=df["Low [T]"] 
    clt=df["Close [T]"] 
    opa=df["Open [A]"] 
    hia=df["High [A]"] 
    loa=df["Low [A]"] 
    cla=df["Close [A]"]
    print('''Select specific Pie chart as given below:
    Press 1 to print the Stock data of Skechers.Inc 
    Press 2 to print the Stock data of Tesla.Inc 
    Press 3 to print the Stock data of Apple.Inc
    ''')
    op=int(input('Enter your choice: '))
##########################################################################
def Skechers(): 
    print('''
    Press 1 to print the Piechart of date vs opening stocks 
    Press 2 to print the Piechrt of date vs closing stocks 
    Press 3 to print the Piechart of date vs maximun stocks 
    Press 4 to print the Piechart of date vs minimun stocks 
    ''')
    op=int(input('Enter your choice: ')) 
    if op==1:
        plt.title("Date wise opening stocks of Skechers") 
        plt.pie(ops,labels=dt,autopct='%1.2f%%') 
    elif op==2:
        plt.title("Date wise closing stocks of Skechers") 
        plt.pie(cls,labels=dt,autopct='%1.2f%%') 
    elif op==3:
        plt.title("Date wise highest stocks of Skechers") 
        plt.pie(his,labels=dt,autopct='%1.2f%%') 
    elif op==4:
        plt.title("Date wise lowest of Skechers") 
        plt.pie(los,labels=dt,autopct='%1.2f%%') 
    else:
        print("enter valid input")
    plt.show()
########################################################################## 
def Tesla():
    print('''
    Press 1 to print the Piechart of date vs opening stocks 
    Press 2 to print the Piechrt of date vs closing stocks
    Press 3 to print the Piechart of date vs maximun stocks 
    Press 4 to print the Piechart of date vs minimun stocks ''')
    op=int(input('Enter your choice: ')) 
    if op==1:
        plt.title("Date wise opening stocks of Tesla") 
        plt.pie(opt,labels=dt,autopct='%1.2f%%')
    elif op==2:
        plt.title("Date wise closing stocks of Tesla") 
        plt.pie(clt,labels=dt,autopct='%1.2f%%') 
    elif op==3:
        plt.title("Date wise highest stocks of Tesla") 
        plt.pie(hit,labels=dt,autopct='%1.2f%%') 
    elif op==4:
        plt.title("Date wise lowest stocks of Tesla") 
        plt.pie(lot,labels=dt,autopct='%1.2f%%') 
    else:
        print("enter valid input")
    plt.show()
########################################################################## 
def Apple():
    print('''
    Press 1 to print the Piechart of date vs opening stocks 
    Press 2 to print the Piechrt of date vs closing stocks 
    Press 3 to print the Piechart of date vs maximun stocks 
    Press 4 to print the Piechart of date vs minimun stocks 
    ''')
    op=int(input('Enter your choice: '))
    if op==1:
        plt.title("Date wise opening stocks of Apple") 
        plt.pie(opa,labels=dt,autopct='%1.2f%%') 
    elif op==2:
        plt.title("Date wise closing stocks of Apple") 
        plt.pie(cla,labels=dt,autopct='%1.2f%%') 
    elif op==3:
        plt.title("Date wise highest stocks of Apple") 
        plt.pie(hia,labels=dt,autopct='%1.2f%%') 
    elif op==4:
        plt.title("Date wise lowest stocks of Apple") 
        plt.pie(loa,labels=dt,autopct='%1.2f%%') 
    else:
        print("enter valid input")
    plt.show()
########################################################################## 
if op==1:
    Skechers() 
elif op==2:
    Tesla() 
elif op==3:
    Apple() 
else:
    print("Enter valid input") 
#======================================================================= 
# #======================================================================= 
def Histogram():
    df=pd.read_csv('E:\Sharad\SKX.csv')
    dt=df["Date"]
    ops=df["Open [S]"] 
    his=df["High [S]"] 
    los=df["Open [S]"] 
    cls=df["Close [S]"] 
    opt=df["Open [T]"] 
    hit=df["High [T]"]
    lot=df["Low [T]"] 
    clt=df["Close [T]"] 
    opa=df["Open [A]"] 
    hia=df["High [A]"] 
    loa=df["Low [A]"] 
    cla=df["Close [A]"] 
    plt.ylabel("number of states") 
    print('''Select specific Histogram as given below: 
    Press 1 to make Histogram for Skechers.Inc 
    Press 2 to make Histogram for Tesla.Inc 
    Press 3 to make Histogram for Apple.Inc
    ''')
    op=int(input("enter your choice"))
############################################################################### 
def Skechers():
    print('''
    Press 1 to make Histogram of Opening Stock price [S] 
    Press 2 to make Histogram of Closing Stock price [S] 
    Press 3 to make Histogram of Highest Stock price [S] 
    Press 4 to make Histogram of Lowest Stock price [S] 
    ''')
    skc=int(input("enter your choice: ")) 
    if skc==1:
        plt.hist(ops,bins=[0,5,10,15,20,25,30,35,40,45,50],edgecolor='green',label='Opening Stock Value')
        plt.xticks([0,5,10,15,20,25,30,35,40,45,50],rotation="vertical")
        plt.yticks([0,2,4,6,8,10]) 
    elif skc==2:
        plt.hist(cls,bins=[0,5,10,15,20,25,30,35,40,45,50],edgecolor='green',label='Closing Stock Value')
        plt.xticks([0,5,10,15,20,25,30,35,40,45,50],rotation="vertical")
        plt.yticks([1,2,3,4,5,6,7,8,9,10]) 
    elif skc==3:
        plt.hist(his,bins=[0,5,10,15,20,25,30,35,40,45,50],edgecolor='green',label='Highest Stock Value')
        plt.xticks([0,5,10,15,20,25,30,35,40,45,50],rotation='vertical')
        plt.yticks([1,2,3,4,5,6,7,8,9,10]) 
    elif skc==4:
        plt.hist(los,bins=[0,5,10,15,20,25,30,35,40,45,50],edgecolor='green',label='Lowest Stock Value')
        plt.xticks([0,5,10,15,20,25,30,35,40,45,50],rotation='vertical')
        plt.yticks([1,2,3,4,5,6,7,8,9,10]) 
    plt.xlabel("Stocks Value (in $)") 
    plt.ylabel('No. of Stock value') 
    plt.title('Skechers.Inc Stocks Data') 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show() 
#################################################################################
def Tesla(): 
    print('''
    Press 1 to make Histogram of Opening Stock price [T] 
    Press 2 to make Histogram of Closing Stock price [T] 
    Press 3 to make Histogram of Highest Stock price [T] 
    Press 4 to make Histogram of Lowest Stock price [T]
    ''')
    ts=int(input("enter your choice: ")) 
    if ts==1:
        plt.hist(opt,bins=[0,100,200,300,400,500,600],edgecolor='green',label='Opening Stock Value') 
        plt.xticks([0,100,200,300,400,500,600],rotation="vertical")
        plt.yticks([0,10,20,30,40,50])
    elif ts==2:
        plt.hist(clt,bins=[0,100,200,300,400,500],edgecolor='green',label='Closing Stock Value') 
        plt.xticks([0,100,200,300,400,500],rotation="vertical")
        plt.yticks([0,10,20,30,40,50])
    elif ts==3:
        plt.hist(hit,bins=[0,100,200,300,400,500,600],edgecolor='green',label='Highest Stock Value') 
        plt.xticks([0,100,200,300,400,500,600],rotation='vertical')
        plt.yticks([0,10,20,30,40,50])
    elif ts==4:
        plt.hist(lot,bins=[0,100,200,300,400],edgecolor='green',label='Lowest Stock Value') 
        plt.xticks([0,100,200,300,400],rotation='vertical')
        plt.yticks([0,10,20,30,40,50])
    plt.xlabel("Stocks Value (in $)") 
    plt.ylabel('No. of Stock value') 
    plt.title('Tesla.Inc Stocks Data') 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show() 
##################################################################################
def Apple(): 
    print('''
    Press 1 to make Histogram of Opening Stock price [A] 
    Press 2 to make Histogram of Closing Stock price [A] 
    Press 3 to make Histogram of Highest Stock price [A] 
    Press 4 to make Histogram of Lowest Stock price [A]
    ''')
    ap=int(input("enter your choice: ")) 
    if ap==1:
        plt.hist(opa,bins=[0,20,40,60,80,100,120,140],edgecolor='green',label='Opening Stock Value') 
        plt.xticks([0,20,40,60,80,100,120,140],rotation="vertical")
        plt.yticks([0,5,10,15,20])
    elif ap==2:
        plt.hist(cla,bins=[0,20,40,60,80,100,120],edgecolor='green',label='Closing Stock Value') 
        plt.xticks([0,20,40,60,80,100,120],rotation="vertical")
        plt.yticks([0,5,10,15,20])
    elif ap==3:
        plt.hist(hia,bins=[0,20,40,60,80,100,120,140],edgecolor='green',label='Highest Stock Value') 
        plt.xticks([0,20,40,60,80,100,120,140],rotation='vertical')
        plt.yticks([0,5,10,15,20])
    elif ap==4:
        plt.hist(loa,bins=[0,20,40,60,80,100,120],edgecolor='green',label='Lowest Stock Value') 
        plt.xticks([0,20,40,60,80,100,120],rotation='vertical')
        plt.yticks([0,5,10,15,20])
    plt.xlabel("Stocks Value (in $)") 
    plt.ylabel('No. of Stock value') 
    plt.title('Apple.Inc Stocks Data') 
    plt.grid(color='grey',alpha=0.3) 
    plt.legend()
    plt.show() 
##################################################################################
if op==1: 
    Skechers()
elif op==2: 
    Tesla() 
elif op==3:
    Apple()
else:
    print("Enter Valid Input")
#=========================================================================== 
#=========================================================================== 
def Candlestick_Chart():
    df=pd.read_csv('E:\Sharad\Stocks.csv') 
    dt=df["Date"]
    ops=df["Open [S]"]
    his=df["High [S]"]
    os=df["Open [S]"]
    cls=df["Close [S]"]
    opt=df["Open [T]"]
    hit=df["High [T]"]
    lot=df["Low [T]"]
    clt=df["Close [T]"]
    opa=df["Open [A]"]
    hia=df["High [A]"]
    loa=df["Low [A]"]
    cla=df["Close [A]"]
    print("press 1 for Skechers") 
    print("press 2 for Tesla") 
    print("press 3 for Apple") 
    op=int(input("enter your choice"))
################################################################################# 
def Skechers():
    fig = go.Figure(data=[go.Candlestick (x=dt,open=ops,high=his,low=los,close=cls)])
    fig.update_layout(title='Skechers stock data', yaxis_title='Stock data (in $)',
    xaxis_title='Date',xaxis_rangeslider_visible=False) 
    fig.show()
################################################################################# 
def Tesla():
    fig = go.Figure(data=[go.Candlestick (x=dt,open=opt,high=hit,low=lot,close=clt)])
    fig.update_layout(title='Tesla stock data', yaxis_title='Stock data (in $)',
    xaxis_title='Date',xaxis_rangeslider_visible=False) 
    fig.show()
################################################################################# 
def Apple():
    fig = go.Figure(data=[go.Candlestick (x=dt,open=opa,high=hia,low=loa,close=cla)])
    fig.update_layout(title='Apple stock data', yaxis_title='Stock data (in $)',
    xaxis_title='Date',xaxis_rangeslider_visible=False) 
    fig.show()
################################################################################# 
if op==1:
    Skechers() 
elif op==2:
    Tesla() 
elif op==3:
    Apple() 
#=========================================================================== 
#=========================================================================== 
def Data_Sorting():
    df=pd.read_csv("E:\Sharad\SKX.csv",index_col=0) 
    print('''
    Press 1 to arrange the record as per the Date 
    Press 2 to arrange the record as per the Open[S] 
    Press 3 to arrange the record as per the Close[S]
    Press 4 to arrange the record as per the High[S] 
    Press 5 to arrange the record as per the Low[S] 
    Press 6 to arrange the record as per the Open[T] 
    Press 7 to arrange the record as per the Close[T] 
    Press 8 to arrange the record as per the High[T] 
    Press 9 to arrange the record as per the Low[T] 
    Press 10 to arrange the record as per the Open[A] 
    Press 11 to arrange the record as per the Close[A] 
    Press 12 to arrange the record as per the High[A] 
    Press 13 to arrange the record as per the Low[A] ''')
    op=int(input("enter your choice")) 
    if op==1:
        df.sort_values(["Date"],inplace=True)
    elif op==2:
        df.sort_values(["Open [S]"],inplace=True)
    elif op==3:
        df.sort_values(["Close [S]"],inplace=True)
    elif op==4:
        df.sort_values(["High [S]"],inplace=True)
    elif op==5:
        df.sort_values(["Low [S]"],inplace=True)
    elif op==6:
        df.sort_values(["Open [T]"],inplace=True)
    elif op==7:
        df.sort_values(["Close [T]"],inplace=True) 
    elif op==8:
        df.sort_values(["High [T]"],inplace=True)
    elif op==9:
        df.sort_values(["Low [T]"],inplace=True)
    elif op==10:
        df.sort_values(["Open [A]"],inplace=True)
    elif op==11:
        df.sort_values(["Close [A]"],inplace=True)
    elif op==12:
        df.sort_values(["High [A]"],inplace=True)
    elif op==13:
        df.sort_values(["Low [A]"],inplace=True)
    else:
        print("enter valid input") 
    print(df)
#===================================================================== 
#===================================================================== 
def Top_Bottom_Selected_Records():
    df=pd.read_csv("E:\Sharad\SKX.csv",index_col=0) 
    top=int(input("how many records to display from top: ")) 
    print('First',top,'records')
    print(df.head(top))
    bottom=int(input("how many records to display from bottom: ")) 
    print('Last',top,'records')
    print(df.tail(bottom)) 
#===================================================================== 
#===================================================================== 
def Specific_Col():
    print('Reading Specific column from CSV file')
    print("""
    Press 1 to print date and opening stock data of Skechers 
    Press 2 to print date and closing stock data of Skechers 
    Press 3 to print date and highest stock data of Skechers 
    Press 4 to print date and lowest stock data of Skechers 
    Press 5 to print date and opening stock data of Tesla 
    Press 6 to print date and closing stock data of Tesla 
    Press 7 to print date and highest stock data of Tesla 
    Press 8 to print date and lowest stock data of Tesla 
    Press 9 to print date and opening stock data of Apple 
    Press 10 to print date and closing stock data of Apple 
    Press 11 to print date and highest stock data of Apple 
    Press 12 to print date and lowest stock data of Apple """)
    op =int(input("enter your choice:")) 
    print('Reading Specific column from CSV file')
    df1=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Open [S]'],index_col=0) 
    df2=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Close [S]'],index_col=0) 
    df3=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','High [S]'],index_col=0) 
    df4=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Low [S]'],index_col=0) 
    df5=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Open [T]'],index_col=0) 
    df6=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Close [T]'],index_col=0) 
    df7=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','High [T]'],index_col=0) 
    df8=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Low [T]'],index_col=0) 
    df9=pd.read_csv("E:\ip\stocks.csv",usecols=['Date','Open [A]'],index_col=0) 
    df10=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Close [A]'],index_col=0)
    df11=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','High [A]'],index_col=0) 
    df12=pd.read_csv("E:\Sharad\SKX.csv",usecols=['Date','Low [A]'],index_col=0)
    if op ==1: 
        print(df1)
    elif op==2: 
        print(df2)
    elif op==3: 
        print(df3)
    elif op==4: 
        print(df4)
    elif op==5: 
        print(df5)
    elif op==6: 
        print(df6)
    elif op==7: 
        print(df7)
    elif op==8: 
        print(df8)
    elif op==9: 
        print(df9)
    elif op==9: 
        print(df10)
    elif op==11: 
        print(df11)
    elif op==12: 
        print(df12)
    else:
        print("Enter valid input")
#===================================================================== 
#===================================================================== 
main_menu()

opt=(int(input('ENTER YOUR CHOICE FROM 1 TO 12 = '))) 
if opt==1:
    Read_CSV() 
elif opt==2:
    Line_Chart() 
elif opt==3:
    Bar_Chart() 
elif opt==4:
    Scatter_Chart() 
elif opt==5:
    Pie_Chart() 
elif opt==6:
    Histogram() 
elif opt==7:
    Candlestick_Chart() 
elif opt==8:
    Data_Sorting() 
elif opt==9:
    Top_Bottom_Selected_Records() 
elif opt==10:
    Specific_Col() 
else:
    print("Enter valid input")

