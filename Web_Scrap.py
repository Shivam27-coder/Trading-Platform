import os
#os.system("python -m pip install mysql.connector")
#os.system("python -m pip install requests")
#os.system("python -m pip install bs4")
#os.system("python -m pip install pyautogui")
#os.system("python -m pip install BeautifulSoup")
from tkinter import messagebox
import mysql.connector
from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
def gold():
    url = "https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF"
    response = requests.get(url)
    soup = BeautifulSoup(response, "html.parser")
    price = soup.find("fin-streamer", {"data-field": "regularMarketPrice","data-test":"qsp-price"})
    val=soup.find("span", class_="C($positiveColor)")
    #price=price.replace(",","")
    #val=val.replace(",","")
    return price,val

def silver():
    url = "https://finance.yahoo.com/quote/SI%3DF?p=SI%3DF"
    response = requests.get(url)
    soup = BeautifulSoup(response, "html.parser")
    price = soup.find("fin-streamer", {"data-field": "regularMarketPrice","data-test":"qsp-price"})
    val=soup.find("span", class_="C($positiveColor)")
    price=price.replace(",","")
    val=val.replace(",","")
    return price,val

def bitcoin():
    url = "https://coinranking.com/coin/Qwsogvtv82FCd+bitcoin-btc"
    response = requests.get(url)
    soup = BeautifulSoup(response, "html.parser")
    price = soup.find("div", class_="hero-coin__price")
    price=price.replace('\n          $ ','')
    price=price.replace('\n','')
    price=price.replace("'","")
    price=price.replace("        ","")
    price=price.replace(",","")
    return price

def etherum():
    url = "https://coinranking.com/coin/razxDUgYGNAdQ+ethereum-eth"
    response = requests.get(url)
    soup = BeautifulSoup(response, "html.parser")
    price = soup.find("div", class_="hero-coin__price")
    price=price.replace('\n          $ ','')
    price=price.replace('\n','')
    price=price.replace("'","")
    price=price.replace("        ","")
    price=price.replace(",","")
    return price

def tether():
    url = "https://coinranking.com/coin/HIVsRcGKkPFtW+tetherusd-usdt"
    response = requests.get(url)
    soup = BeautifulSoup(response, "html.parser")
    price = soup.find("div", class_="hero-coin__price")
    price=price.replace('\n          $ ','')
    price=price.replace('\n','')
    price=price.replace("'","")
    price=price.replace("        ","")
    price=price.replace(",","")
    return price

demodb=mysql.connector.connect(host='localhost',user='root',passwd='shivam1shivam')
democursor=demodb.cursor()
democursor.execute("create database if not exists trading")
demodb.commit()
demodb=mysql.connector.connect(host='localhost',user='root',passwd='shivam1shivam',database='trading')
democursor=demodb.cursor()
democursor.execute("""create table if not exists users
(name varchar(30),
clientid varchar(30),
userid varchar(30),
password varchar(30),
acc_cr varchar(30))""")
demodb.commit()
democursor.execute("""create table if not exists moneyinfo
(clientid varchar(30),cash varchar(30))""")
demodb.commit()
def moneyin(cid):
    c=Tk()
    c.title("Add or Remove Money")
    c.state('zoomed')
    c.configure(bg="black")
    c.iconbitmap('Py_ICO.ico')
    def win_cl0():
            c.destroy()
    b=Button(c,text='<Exit',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
    l=Label(c,text='',bg='black').pack(padx=0,pady=0)
    l=Label(c,text='Add or Take Money',bg='black',fg='white',font="LUCIDA 20 bold").pack(padx=0,pady=0)
    l=Label(c,text='',bg='black').pack(padx=0,pady=0)
    
    def deposit():
        d=Tk()
        d.title("Deposit Money")
        d.state('zoomed')
        d.configure(bg="black")
        d.iconbitmap('Py_ICO.ico')
        l=Label(d,text='',bg='black').pack(padx=0,pady=0)
        def win_cl0():
            d.destroy()
        b=Button(d,text='<Exit',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
        l=Label(d,text='Deposit Money',bg='black',fg='white',font="LUCIDA 20 bold").pack(padx=0,pady=0)
        l=Label(d,text='',bg='black').pack(padx=0,pady=0)
        amt=StringVar(d)
        def depmon():
            amt1=amt.get()
            amt1=float(amt1)
            democursor.execute("select cash from moneyinfo where clientid='"+cid+"'")
            bal=0
            for i in democursor:
                bal+=float(i[0])
            final_bal=str(amt1+bal)
            democursor.execute("update moneyinfo set cash='"+final_bal+"' where clientid='"+cid+"'")
            demodb.commit()
            d.destroy()
            l=Label(c,text='Money Deposited Successfully',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
        l=Label(d,text="Amount : ",bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=200)
        l=Entry(d,textvariable=amt,bg='white',font='LUCIDA 13 bold').place(x=730,y=200)
        b=Button(d,text="Deposit Money",bg='white',fg='black',activebackground='white',command=depmon,font='LUCIDA 13 bold').place(x=850,y=320)
    def withdraw():
        d=Tk()
        d.title("Withdraw Money")
        d.state('zoomed')
        d.configure(bg="black")
        d.iconbitmap('Py_ICO.ico')
        def win_cl0():
            d.destroy()
        b=Button(d,text='<Exit',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
        l=Label(d,text='',bg='black').pack(padx=0,pady=0)
        l=Label(d,text='Withdraw Money',bg='black',fg='white',font="LUCIDA 20 bold").pack(padx=0,pady=0)
        l=Label(d,text='',bg='black').pack(padx=0,pady=0)
        amt=StringVar(d)
        def witmon():
            amt1=amt.get()
            try:
                amt1=float(amt1)
                democursor.execute("select cash from moneyinfo where clientid='"+cid+"'")
                for i in democursor:
                    bal=float(i[0])
                if bal<amt1:
                    l=Label(d,text='Not Enough Balance',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
                else:
                    final_bal=str(bal-amt1)
                    democursor.execute("update moneyinfo set cash='"+final_bal+"' where clientid='"+cid+"'")
                    demodb.commit()
                    d.destroy()
                    l=Label(c,text='Money Withdrawn Successfully',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
            except:
                l=Label(d,text='Invalid Amount Entered',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
        l=Label(d,text="Amount : ",bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=200)
        l=Entry(d,textvariable=amt,bg='white',font='LUCIDA 13 bold').place(x=730,y=200)
        b=Button(d,text="Withdraw Money",bg='white',fg='black',activebackground='white',command=witmon,font='LUCIDA 13 bold').place(x=850,y=320)
    l=Label(c,text='Choose One Of The Below Option',bg='black',fg='red',font="LUCIDA 20 bold").pack(padx=0,pady=0)
    b=Button(c,text="Deposit Money",bg='white',fg='black',command=deposit,font='LUCIDA 15 bold').place(x=400,y=300)
    b=Button(c,text="Withdraw Money",bg='white',fg='black',command=withdraw,font='LUCIDA 15 bold').place(x=900,y=300)
def logsin(user,pas):
    demodb=mysql.connector.connect(host='localhost',user='root',passwd='shivam1shivam',database='trading')
    democursor=demodb.cursor()
    democursor.execute("select name from users where userid='"+user+"' and password='"+pas+"'")
    for i in democursor:
        names=str(i[0])
    b=Tk()
    b.title("Welcome to Trading Platform")
    b.state('zoomed')
    b.configure(bg="black")
    b.iconbitmap('Py_ICO.ico')
    def invest1():
        gold_p,gold_v=gold()
        silver_p,silver_v=silver()
        bit_p=bitcoin()
        etherum_p=etherum()
        tether_p=tether()
        bit_v='-'
        tether_v='-'
        etherum_v='-'
        h=Tk()
        h.title("Invest")
        h.state('zoomed')
        h.configure(bg="black")
        h.iconbitmap('Py_ICO.ico')
        l=Label(h,text='',bg='black').pack(padx=0,pady=0)
        democursor.execute("select cash from moneyinfo where clientid='"+user+"'")
        for i in democursor:
            curr_bal1=str(i[0])
        l=Label(h,text='Current Balance '+curr_bal1,bg='black',fg='green',font="LUCIDA 17 bold").place(x=632,y=60)
        def win_cl0():
            h.destroy()
        l=Button(h,text='< Back',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
        l=Label(h,text='Select From Below Options',bg='black',fg='white',font='LUCIDA 25 bold').pack(padx=0,pady=0)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=150)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=100)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=350)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=250)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=450)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=650)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=550)
        l=Label(h,text="Name",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=130)
        l=Label(h,text="Price(in USD)",bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=130)
        l=Label(h,text="Value",bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=130)
        l=Label(h,text="Buy/Sell",bg="black",fg='white',font='LUCIDA 15 bold').place(x=1200,y=130)
        l=Label(h,text="Gold",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=200)
        def refresh():
            democursor.execute("select cash from moneyinfo where clientid='"+user+"'")
            for i in democursor:
                curr_bal1=str(i[0])
            l=Label(h,text='Current Balance '+curr_bal1,bg='black',fg='green',font="LUCIDA 17 bold").place(x=632,y=60)
        l=Button(h,text='Refresh',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=refresh,bg='black',fg='white',font='LUCIDA 10').place(x=1450,y=10)
        
        l=Label(h,text="Silver",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=300)
        l=Label(h,text="Bitcoin",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=400)
        l=Label(h,text="Ethereum",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=500)
        l=Label(h,text="Tether USD",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=600)
        l=Label(h,text=gold_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=200)
        l=Label(h,text=silver_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=300)
        l=Label(h,text=bit_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=400)
        l=Label(h,text=etherum_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=500)
        l=Label(h,text=tether_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=600)
        l=Label(h,text=gold_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=200)
        l=Label(h,text=silver_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=300)
        l=Label(h,text=bit_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=400)
        l=Label(h,text=etherum_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=500)
        l=Label(h,text=tether_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=600)
        def buy_stock(x,j):
            k=Tk()
            k.title(j)
            k.state('zoomed')
            k.configure(bg="black")
            k.iconbitmap('Py_ICO.ico')
            def win_cl0():
                k.destroy()
            l=Button(k,text='< Back',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
            if x==1:
                prices=gold_p
            elif x==2:
                prices=silver_p
            elif x==3:
                prices=bit_p
            elif x==4:
                prices=etherum_p
            else:
                prices=tether_p
            l=Label(k,text='',bg='black').pack(padx=0,pady=0)
            l=Label(k,text="Please Enter Quantity to Buy : ",bg='black',fg='white',font='LUCIDA 25 bold').pack(padx=0,pady=0)
            amount_to_buy=StringVar(k)
            def buy_final():
                amt2=amount_to_buy.get()
                amt2=float(amt2)
                total_due=float(prices)*amt2
                democursor=demodb.cursor()
                democursor.execute("select cash from moneyinfo where clientid='"+user+"'")
                for i in democursor:
                    avail_bal=float(i[0])
                if avail_bal<total_due:
                    l=Label(k,text='Not Enough Balance',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
                else:
                    o=Tk()
                    o.geometry("900x200")
                    o.configure(bg='white')
                    o.title("Confirm & Pay")
                    o.iconbitmap('Py_ICO.ico')
                    
                    tick=IntVar(o)
                    def conf_pay():
                        o.destroy()
                        k.destroy()
                        num_entry=1
                        date_to=datetime.today().strftime('%Y-%m-%d')
                        avail_bal1=avail_bal-total_due
                        l=Label(h,text="                                                                                                                ",bg='black',fg='green',font='LUCIDA 16 bold').place(x=100,y=700)
                        l=Label(h,text="Successfully Bought "+j+" of Worth "+str(total_due),bg='black',fg='red',font='LUCIDA 16 bold').place(x=100,y=700)
                        democursor.execute("select count(*) from buy_"+user)
                        for i in democursor:
                            num_entry+=int(i[0])
                        democursor.execute("insert into buy_"+user+" values(%s,%s,%s,%s,%s)",(str(num_entry),str(amt2),str(j),str(total_due),str(date_to)))
                        demodb.commit()
                        democursor.execute("insert into buy_"+user+"_h values(%s,%s,%s,%s,%s)",(str(num_entry),str(amt2),str(j),str(total_due),str(date_to)))
                        demodb.commit()
                        democursor.execute("update moneyinfo set cash='"+str(avail_bal1)+"' where clientid='"+user+"'")
                        demodb.commit()
                    def next_pro():
                        tick1=tick.get()
                        if tick1==0:
                            b=Label(o,text="       ",bg='white',font='LUCIDA 34').place(x=400,y=50)
                        else:
                            b=Button(o,text="Proceed",bg='white',borderwidth=1,activebackground='white',relief='solid',command=conf_pay,font='LUCIDA 15').place(x=400,y=50)
                    b=Checkbutton(o,text="Are You Sure You Want to Buy "+j+" Worth of "+str(total_due),bg='white',activebackground='white',command=next_pro,variable=tick,onvalue=1,offvalue=0,font="LUCIDA 15").pack(padx=0,pady=0)        
                    b=Label(o,text='',bg='white',font='LUCIDA 15').pack(padx=0,pady=0)
            l=Label(k,text="Quantity to Buy : ",bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=200)
            l=Entry(k,textvariable=amount_to_buy,bg='white',font='LUCIDA 13 bold').place(x=770,y=200)
            b=Button(k,text="Buy",bg='white',fg='black',activebackground='white',command=buy_final,font='LUCIDA 13 bold').place(x=850,y=320)

        def gold_b():
            x=1
            j="Gold"
            buy_stock(x,j)
        def silver_b():
            x=2
            j="Silver"
            buy_stock(x,j)
        def bit_b():
            x=3
            j="Bitcoin"
            buy_stock(x,j)
        def ether_b():
            x=4
            j="Ethereum"
            buy_stock(x,j)
        def tether_b():
            x=5
            j="Tether USD"
            buy_stock(x,j)
        def sell_stock(x,j):
            k=Tk()
            k.geometry("1200x200")
            k.configure(bg='white')
            k.title("Confirm & Pay")
            k.iconbitmap('Py_ICO.ico')
            def win_cl0():
                k.destroy()
            if x==1:
                prices=gold_p
            elif x==2:
                prices=silver_p
            elif x==3:
                prices=bit_p
            elif x==4:
                prices=etherum_p
            else:
                prices=tether_p
            democursor.execute("select qty from buy_"+user+" where name='"+j+"'")
            for i in democursor:
                qty_to_sell=float(i[0])
            democursor.execute("select money from buy_"+user+" where name='"+j+"'")
            for i in democursor:
                bought_price=float(i[0])
            curr_price=float(prices)*qty_to_sell
            l=Button(k,text='< Back',borderwidth=0,relief='solid',activebackground='white',activeforeground='black',command=win_cl0,bg='white',fg='black',font='LUCIDA 10').place(x=0,y=0)
            tick=IntVar(k)
            def conf_pay():
                k.destroy()
                num_entry=1
                l=Label(h,text="                                                                                                                ",bg='black',fg='green',font='LUCIDA 16 bold').place(x=100,y=700)
                democursor.execute("select cash from moneyinfo where clientid='"+user+"'")
                for i in democursor:
                    avail_bal=float(i[0])
                date_to=datetime.today().strftime('%Y-%m-%d')
                avail_bal1=avail_bal+curr_price
                profits=curr_price-bought_price
                if profits>=0:
                    l=Label(h,text="Successfully Sold "+j+" of Worth "+str(curr_price)+" with Profit of "+str(profits),bg='black',fg='green',font='LUCIDA 16 bold').place(x=100,y=700)
                else:
                    l=Label(h,text="Successfully Sold "+j+" of Worth "+str(curr_price)+" with Loss of "+str(profits),bg='black',fg='red',font='LUCIDA 16 bold').place(x=100,y=700)
                democursor.execute("select count(*) from buy_"+user)
                for i in democursor:
                    num_entry+=int(i[0])
                democursor.execute("insert into sell_"+user+" values(%s,%s,%s,%s,%s,%s,%s)",(str(num_entry),str(qty_to_sell),str(j),str(bought_price),str(curr_price),str(profits),str(date_to)))
                demodb.commit()
                democursor.execute("update moneyinfo set cash='"+str(avail_bal1)+"' where clientid='"+user+"'")
                demodb.commit()
                democursor.execute("delete from buy_"+user+" where name='"+j+"' and qty='"+str(qty_to_sell)+"'")
                demodb.commit()
            def next_pro():
                tick1=tick.get()
                if tick1==0:
                    b=Label(k,text="       ",bg='white',font='LUCIDA 34').place(x=400,y=50)
                else:
                    b=Button(k,text="Proceed",bg='white',borderwidth=1,activebackground='white',relief='solid',command=conf_pay,font='LUCIDA 15').place(x=400,y=50)
            
            b=Checkbutton(k,text="Are You Sure You Want to Sell "+j+" Now Worth of "+str(curr_price)+" And You Bought at "+str(bought_price),bg='white',activebackground='white',command=next_pro,variable=tick,onvalue=1,offvalue=0,font="LUCIDA 15").pack(padx=0,pady=0)        
            b=Label(k,text='',bg='white',font='LUCIDA 15').pack(padx=0,pady=0)
        def gold_s():
            x=1
            j="Gold"
            qty_to=''
            democursor.execute("select qty from buy_"+user+" where name='"+j+"'")
            for i in democursor:
                qty_to+=str(i[0])
            if qty_to=='':
                l=Label(h,text="You Don't Have any "+j+" to Sell",bg='black',fg='red',font='LUCIDA 16 bold').place(x=100,y=700)
            else:
                sell_stock(x,j )
        def silver_s():
            x=2
            j="Silver"
            qty_to=''
            democursor.execute("select qty from buy_"+user+" where name='"+j+"'")
            for i in democursor:
                qty_to+=str(i[0])
            if qty_to=='':
                l=Label(h,text="You Don't Have any "+j+" to Sell",bg='black',fg='red',font='LUCIDA 16 bold').place(x=100,y=700)
            else:
                sell_stock(x,j )
        def bit_s():
            x=3
            j="Bitcoin"
            qty_to=''
            democursor.execute("select qty from buy_"+user+" where name='"+j+"'")
            for i in democursor:
                qty_to+=str(i[0])
            if qty_to=='':
                l=Label(h,text="You Don't Have any "+j+" to Sell",bg='black',fg='red',font='LUCIDA 16 bold').place(x=100,y=700)
            else:
                sell_stock(x,j )
        def ether_s():
            x=4
            j="Ethereum"
            qty_to=''
            democursor.execute("select qty from buy_"+user+" where name='"+j+"'")
            for i in democursor:
                qty_to+=str(i[0])
            if qty_to=='':
                l=Label(h,text="You Don't Have any "+j+" to Sell",bg='black',fg='red',font='LUCIDA 16 bold').place(x=100,y=700)
            else:
                sell_stock(x,j )
        def tether_s():
            x=5
            j="Tether USD"
            qty_to=''
            democursor.execute("select qty from buy_"+user+" where name='"+j+"'")
            for i in democursor:
                qty_to+=str(i[0])
            if qty_to=='':
                l=Label(h,text="You Don't Have any "+j+" to Sell",bg='black',fg='red',font='LUCIDA 16 bold').place(x=100,y=700)
            else:
                sell_stock(x,j )
        l=Button(h,text="Buy",bg='black',fg='green',borderwidth=0,activebackground='black',command=gold_b,activeforeground='green',font=('Arial',15,'underline')).place(x=1150,y=200)
        l=Button(h,text="Sell",bg='black',fg='red',borderwidth=0,activebackground='black',activeforeground='red',command=gold_s,font=('Arial',15,'underline')).place(x=1250,y=200)
        l=Button(h,text="Buy",bg='black',fg='green',borderwidth=0,activebackground='black',command=silver_b,activeforeground='green',font=('Arial',15,'underline')).place(x=1150,y=300)
        l=Button(h,text="Sell",bg='black',fg='red',borderwidth=0,activebackground='black',activeforeground='red',command=silver_s,font=('Arial',15,'underline')).place(x=1250,y=300)
        l=Button(h,text="Buy",bg='black',fg='green',borderwidth=0,activebackground='black',command=bit_b,activeforeground='green',font=('Arial',15,'underline')).place(x=1150,y=400)
        l=Button(h,text="Sell",bg='black',fg='red',borderwidth=0,activebackground='black',activeforeground='red',command=bit_s,font=('Arial',15,'underline')).place(x=1250,y=400)
        l=Button(h,text="Buy",bg='black',fg='green',borderwidth=0,activebackground='black',command=ether_b,activeforeground='green',font=('Arial',15,'underline')).place(x=1150,y=500)
        l=Button(h,text="Sell",bg='black',fg='red',borderwidth=0,activebackground='black',activeforeground='red',command=ether_s,font=('Arial',15,'underline')).place(x=1250,y=500)
        l=Button(h,text="Buy",bg='black',fg='green',borderwidth=0,activebackground='black',command=tether_b,activeforeground='green',font=('Arial',15,'underline')).place(x=1150,y=600)
        l=Button(h,text="Sell",bg='black',fg='red',borderwidth=0,activebackground='black',activeforeground='red',command=tether_s,font=('Arial',15,'underline')).place(x=1250,y=600)
        h.mainloop()
    def portfolio_viewing():
        gold_p,gold_v=gold()
        silver_p,silver_v=silver()
        bit_p=bitcoin()
        etherum_p=etherum()
        tether_p=tether()
        bit_v='-'
        tether_v='-'
        etherum_v='-'
        h=Tk()
        h.title("Portfolio Viewing")
        h.state('zoomed')
        h.configure(bg="black")
        h.iconbitmap('Py_ICO.ico')
        l=Label(h,text='',bg='black').pack(padx=0,pady=0)
        def win_cl0():
            h.destroy()
        l=Button(h,text='< Back',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
        l=Label(h,text='Select From Below Options',bg='black',fg='white',font='LUCIDA 25 bold').pack(padx=0,pady=0)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=150)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=100)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=350)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=250)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=450)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=650)
        l=Label(h,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=550)
        l=Label(h,text="Name",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=130)
        l=Label(h,text="Price(in USD)",bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=130)
        l=Label(h,text="Value",bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=130)
        l=Label(h,text="Gold",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=200)
        l=Label(h,text="Silver",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=300)
        l=Label(h,text="Bitcoin",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=400)
        l=Label(h,text="Ethereum",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=500)
        l=Label(h,text="Tether USD",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=600)
        l=Label(h,text=gold_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=200)
        l=Label(h,text=silver_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=300)
        l=Label(h,text=bit_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=400)
        l=Label(h,text=etherum_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=500)
        l=Label(h,text=tether_p,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=600)
        l=Label(h,text=gold_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=200)
        l=Label(h,text=silver_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=300)
        l=Label(h,text=bit_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=400)
        l=Label(h,text=etherum_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=500)
        l=Label(h,text=tether_v,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=600)
        h.mainloop()
    l=Label(b,text='',bg='black').pack(padx=0,pady=0)
    def moneyins():
        moneyin(user)
    def win_cl0():
        b.destroy()
    l=Button(b,text='< Back',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
    def refresh():
        curr_bal1=''
        democursor.execute("select cash from moneyinfo where clientid='"+user+"'")
        for i in democursor:
            curr_bal1+=str(i[0])
        l=Label(b,text='Current Balance '+curr_bal1,bg='black',fg='green',font="LUCIDA 17 bold").place(x=632,y=60)
    l=Button(b,text='Refresh',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=refresh,bg='black',fg='white',font='LUCIDA 10').place(x=1450,y=10)
    l=Label(b,text='Welcome '+names,bg='black',fg='white',font="LUCIDA 20 bold").pack(padx=0,pady=0)
    democursor.execute("select cash from moneyinfo where clientid='"+user+"'")
    curr_bal1=''
    for i in democursor:
        curr_bal1+=str(i[0])
    def bought_history():
        democursor.execute("select count(*) from buy_"+user)
        for i in democursor:
            total_len=int(i[0])
        s=Tk()
        def win_cl0():
            s.destroy()
        b=Button(s,text='<Exit',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)

        s.title("Buying History")
        s.state('zoomed')
        s.configure(bg="black")
        s.iconbitmap('Py_ICO.ico')
        l=Label(s,text='',bg='black').pack(padx=0,pady=0)
        l=Label(s,text='Buying History',bg='black',fg='white',font="LUCIDA 20 bold").pack(padx=0,pady=0)
        l=Label(s,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=100)
        l=Label(s,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=150)
        l=Label(s,text="Name",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=130)
        l=Label(s,text="Price(in USD)",bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=130)
        l=Label(s,text="Quantity",bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=130)
        l=Label(s,text="Date",bg="black",fg='white',font='LUCIDA 15 bold').place(x=1200,y=130)
        place_x=0
        for i in range(total_len):
            democursor.execute("select name,money,qty,date from buy_"+user+"_h where num='"+str(i+1)+"'")
            for j in democursor:
                name12=j[0]
                price12=j[1]
                qtye12=j[2]
                dates123=j[3]
            num_pl=i*50
            l=Label(s,text=name12,bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=200+num_pl)
            l=Label(s,text=price12,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=200+num_pl)
            l=Label(s,text=qtye12,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=200+num_pl)
            l=Label(s,text=dates123,bg="black",fg='white',font='LUCIDA 15 bold').place(x=1200,y=200+num_pl)
        s.mainloop()
    def selling_history():
        democursor=demodb.cursor()
        democursor.execute("select count(*) from sell_"+user)
        for i in democursor:
            total_len=int(i[0])
        s=Tk()
        def win_cl0():
            s.destroy()
        b=Button(s,text='<Exit',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)

        s.title("Buying History")
        s.state('zoomed')
        s.configure(bg="black")
        s.iconbitmap('Py_ICO.ico')
        l=Label(s,text='',bg='black').pack(padx=0,pady=0)
        l=Label(s,text='Selling History',bg='black',fg='white',font="LUCIDA 20 bold").pack(padx=0,pady=0)
        l=Label(s,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=100)
        l=Label(s,text='________________________________________________________________________________________________________________________________________________________________________________________________________',bg='black',fg='white',font="LUCIDA 15 bold").place(x=0,y=150)
        l=Label(s,text="Name",bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=130)
        l=Label(s,text="Price(in USD)",bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=130)
        l=Label(s,text="Quantity",bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=130)
        l=Label(s,text="Sell Price",bg="black",fg='white',font='LUCIDA 15 bold').place(x=1200,y=130)
        place_x=0
        democursor=demodb.cursor()
        for i in range(total_len):
            democursor.execute("select name,bought_price,qty,sell_price from sell_"+user+" where num='"+str(i+1)+"'")
            for j in democursor:
                name12s=j[0]
                price12s=j[1]
                qtye12s=j[2]
                dates123s=j[3]
                num_pl=i*50
                l=Label(s,text=name12s,bg="black",fg='white',font='LUCIDA 15 bold').place(x=100,y=200+num_pl)
                l=Label(s,text=price12s,bg="black",fg='white',font='LUCIDA 15 bold').place(x=400,y=200+num_pl)
                l=Label(s,text=qtye12s,bg="black",fg='white',font='LUCIDA 15 bold').place(x=800,y=200+num_pl)
                l=Label(s,text=dates123s,bg="black",fg='white',font='LUCIDA 15 bold').place(x=1200,y=200+num_pl)
        s.mainloop()
    l=Label(b,text='Current Balance '+curr_bal1,bg='black',fg='green',font="LUCIDA 17 bold").pack(padx=0,pady=0)
    l=Label(b,text="Choose From Below Options :",bg='black',fg='red',font="LUCIDA 25 bold").place(x=100,y=150)
    l=Button(b,text='Invest',bg='black',fg='white',activebackground='black',activeforeground='blue',command=invest1,borderwidth=0,font=("LUCIDA","20","underline","bold")).place(x=150,y=250)
    l=Button(b,text='Portfolio Viewing',activebackground='black',activeforeground='blue',fg='white',bg='black',borderwidth=0,command=portfolio_viewing,font="LUCIDA 20 bold underline").place(x=150,y=350)
    l=Button(b,text='Money In/Out',activebackground='black',activeforeground='blue',fg='white',bg='black',command=moneyins,borderwidth=0,font="LUCIDA 20 bold underline").place(x=150,y=450)
    l=Button(b,text='',activebackground='white',activeforeground='black',bg='white',borderwidth=1,font="LUCIDA 20 bold",height=9,width=15).place(x=1200,y=100)
    l=Button(b,text='',activebackground='black',activeforeground='white',bg='black',borderwidth=1,font="LUCIDA 20 bold",height=8,width=14).place(x=1206,y=115)
    l=Label(b,text="History",bg='black',fg='red',font="LUCIDA 15 bold underline").place(x=1280,y=130)
    l=Button(b,text='Bought History',activebackground='black',activeforeground='blue',fg='white',bg='black',borderwidth=0,command=bought_history,font="LUCIDA 15 bold underline").place(x=1250,y=180)
    l=Button(b,text='Selling History',activebackground='black',activeforeground='blue',fg='white',bg='black',borderwidth=0,command=selling_history,font="LUCIDA 15 bold underline").place(x=1250,y=230)
    b.mainloop()
y=Tk()
y.title("Welcome To Trading Platform")
y.state('zoomed')
y.configure(bg="black")
y.iconbitmap('Py_ICO.ico')
l=Label(y,text='',bg='black').pack(padx=0,pady=0)
l=Label(y,text="Online Trading Platform",bg='black',fg='white',font='LUCIDA 25 bold').pack(padx=0,pady=0)
l=Label(y,text='',bg='black').pack(padx=0,pady=0)
l=Label(y,text='',bg='black').pack(padx=0,pady=0)
l=Label(y,text='',bg='black').pack(padx=0,pady=0)
b=Button(y,text='',height=27,width=54,activebackground='white',bg='white').pack(padx=0,pady=0)
b=Button(y,text='',height=26,width=53,activebackground='black',bg='black').place(x=577,y=134)
l=Label(y,text="Login -",bg='black',fg='white',font='LUCIDA 15 bold').place(x=730,y=150)
user=StringVar(y)
pas=StringVar(y)
l=Label(y,text='Username : ',bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=200)
l=Label(y,text='Password : ',bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=240)
e=Entry(y,textvariable=user,font='LUCIDA 13 bold').place(x=730,y=200)
e=Entry(y,textvariable=pas,show='*',font='LUCIDA 13 bold').place(x=730,y=240)
def create(name,pasw):
    num=1
    cl="C"
    date_to=datetime.today().strftime('%Y-%m-%d')
    democursor.execute("select count(*) from users")
    for i in democursor:
        num+=int(i[0])
    if num<10:
        clientid=cl+"00"+str(num)
    elif num>9 and num<100:
        clientid=cl+"0"+str(num)
    else:
        clientid=cl+str(num)
    democursor.execute("insert into users values(%s,%s,%s,%s,%s)",(name,clientid,clientid,pasw,str(date_to)))
    demodb.commit()
    money_now=0
    democursor.execute("insert into moneyinfo values(%s,%s)",(clientid,money_now))
    demodb.commit()
    democursor.execute("create table buy_"+clientid+" (num varchar(30),qty varchar(30),name varchar(30),money varchar(30),date varchar(30))")
    demodb.commit()
    democursor.execute("create table buy_"+clientid+"_h (num varchar(30),qty varchar(30),name varchar(30),money varchar(30),date varchar(30))")
    demodb.commit()
    democursor.execute("create table sell_"+clientid+" (num varchar(30),qty varchar(30),name varchar(30),bought_price varchar(30),sell_price varchar(30),profit varchar(30),date varchar(30))")
    demodb.commit()
def open_new():
    a=Tk()
    a.title("Open New Account")
    a.state('zoomed')
    a.configure(bg="black")
    a.iconbitmap('Py_ICO.ico')
    def win_cl1():
        a.destroy()
    b=Button(a,text='< Back To Login',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl1,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
    name=StringVar(a)
    password_set=StringVar(a)
    repassword_set=StringVar(a)
    l=Label(a,text='',bg='black').pack(padx=0,pady=0)
    l=Label(a,text='Create New Account',bg='black',fg='white',font="LUCIDA 20 bold").pack(padx=0,pady=0)
    l=Label(a,text='',bg='black').pack(padx=0,pady=0)
    l=Label(a,text='',bg='black').pack(padx=0,pady=0)
    l=Label(a,text='',bg='black').pack(padx=0,pady=0)
    l=Label(a,text='',bg='black').pack(padx=0,pady=0)
    b=Button(a,text='',height=27,width=54,activebackground='white',bg='white').pack(padx=0,pady=0)
    b=Button(a,text='',height=26,width=53,activebackground='black',bg='black').place(x=577,y=150)
    l=Label(a,text="Enter Following Details - ",bg='black',fg='white',font='LUCIDA 15 bold').place(x=630,y=160)
    l=Label(a,text='Name : ',bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=210)
    l=Label(a,text='Password : ',bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=250)
    l=Label(a,text='Re-Password : ',bg='black',fg='white',font='LUCIDA 13 bold').place(x=600,y=290)
    e=Entry(a,textvariable=name,font='LUCIDA 13 bold').place(x=730,y=210)
    e=Entry(a,textvariable=password_set,show='*',font='LUCIDA 13 bold').place(x=730,y=250)
    e=Entry(a,textvariable=repassword_set,show='*',font='LUCIDA 13 bold').place(x=730,y=290)
    def cr():
        name1=name.get()
        pas1=password_set.get()
        repas1=repassword_set.get()
        if name=='':
            l=Label(a,text='Invalid Name',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
        elif pas1!=repas1:
            l=Label(a,text='Passwords Does Not Match',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
        else:
            if len(pas1)>6:
                num=1
                cl="C"
                democursor.execute("select count(*) from users")
                for i in democursor:
                    num+=int(i[0])
                if num<10:
                    clientid=cl+"00"+str(num)
                elif num>9 and num<100:
                    clientid=cl+"0"+str(num)
                else:
                    clientid=cl+str(num)
                l=Label(a,text='Account Created Successfully',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
                l=Label(a,text='Now Please Exit This Page And Continue To Login',bg='black',fg='red',font='LUCIDA 16 bold').place(x=550,y=680)
                l=Label(a,text="Your Username is : "+clientid,bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=640)
                create(name1,pas1)
            else:
                l=Label(a,text='Password is Too Short',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
    b=Button(a,text="Create Account",bg='white',fg='black',activebackground='white',command=cr,font='LUCIDA 13 bold').place(x=750,y=360)
    a.mainloop()
def login():
    userin=user.get()
    pasin=pas.get()
    if userin=='':
        l=Label(y,text='Invalid Username or Password',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)  
    else:
        in_v=''
        democursor.execute("select password from users where userid='"+userin+"'")
        for i in democursor:
            in_v+=i[0]
        if in_v==pasin:
            l=Label(y,text='Successfull Login',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)
            logsin(userin,pasin)
        else:
            l=Label(y,text='Invalid Username or Password',bg='black',width=25,fg='red',font='LUCIDA 16 bold').place(x=620,y=600)        
b=Button(y,text="Login",bg='white',fg='black',activebackground='white',command=login,font='LUCIDA 13 bold').place(x=850,y=320)
def win_cl0():
    y.destroy()
b=Button(y,text='<Exit',borderwidth=0,relief='solid',activebackground='black',activeforeground='white',command=win_cl0,bg='black',fg='white',font='LUCIDA 10').place(x=0,y=0)
b=Button(y,text="Open Account",bg='white',fg='black',width=25,activebackground='white',command=open_new,font='LUCIDA 13 bold').place(x=640,y=400)
y.mainloop()
