# Here we have used two modules whose knowledge has been acquired from online resources #

import webbrowser
from easygui import *

class Google_items:
    def __init__(self,name,mobile_no,what_to_search):
        self.name=name
        self.mobile_no = mobile_no
        self.what_to_search = what_to_search

    def Google(self):
        webbrowser.open("https://www.google.co.in/search?q="+self.what_to_search)
    def Youtube(self):
        webbrowser.open("https://www.youtube.com/results?search_query=" + self.what_to_search)
    def IIITD(self):
        webbrowser.open("https://iiitd.ac.in/search/node/"+ self.what_to_search)
    def Maps(self):
        webbrowser.open("https://www.google.com/maps/dir//"+self.what_to_search)
    def GoogleMeet(self):
        webbrowser.open("https://meet.google.com/"+ self.what_to_search +"?pli=1&authuser=0")

class MarketPlaces:
    def __init__(self,name,mobile_no,what_to_search):
        self.name=name
        self.mobile_no = mobile_no
        self.what_to_search = what_to_search

    def Amazon(self):
        webbrowser.open("https://www.amazon.in/s?k=" + self.what_to_search +"&crid=2IEZEG8TDC0OP&sprefix="+self.what_to_search+"%2Caps%2C205&ref=nb_sb_noss")
    def Flipkart(self):
        webbrowser.open("https://www.flipkart.com/search?q=" + self.what_to_search + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    def Meesho(self):
        webbrowser.open("https://meesho.com/search?q="+ self.what_to_search + "&searchType=manual&searchIdentifier=text_search")
    def Bigbasket(self):
        webbrowser.open("https://www.bigbasket.com/ps/?q=" + self.what_to_search)

class Other:
    def __init__(self,name,mobile_no,what_to_search=""):
        self.name=name
        self.mobile_no = mobile_no
        self.what_to_search = what_to_search

    def Weather(self):
        webbrowser.open("https://www.accuweather.com/en/search-locations?query=" + self.what_to_search)
    def News(self):
        webbrowser.open("https://economictimes.indiatimes.com/")
    def TicTacToe(self):
        webbrowser.open("https://playtictactoe.org/")
    def Snake(self):
        webbrowser.open("https://snake.googlemaps.com/")


Message = "Information Box"
Words_shown = "WELCOME TO THE CLICKABLE INTERFACE OF EASY SEARCH"
msg = msgbox(Words_shown, Message)

question = "Enter the following details"
title = "Personal Data Collector"
input11 = ["Name", "Mobile no."]
default11 = []
output = multenterbox(question, title, input11, default11)

Items = "Select the type of operation which you want to perform"
Initial_values = ["Google","Marketplaces","Other"]
output1 = choicebox(Items,choices=Initial_values)
if output1=="Google":
    msg = "Select the web service you want to search on"
    Items1 = ["Google","Youtube","IIITD","Maps","Google Meet"]
    output2 = choicebox(msg, choices = Items1)
    if output2=="Google":
        text1 = "Welcome to Google Search"
        title1 = "Required search"
        input1 = ["What do you want to search"]
        initial1 = []
        output3 = multenterbox(text1, title1, input1, initial1)
        output3 = [i for i in output3]
        a = ""
        for i in output3:
            a+=f"{i}+"
        a = a[:-1]
        obj = Google_items(output[0],output[1],a)
        obj.Google()

    elif output2=="Youtube":
        text2 = "Welcome to YouTube"
        title2 = "Required search"
        input2 = ["What do you want to search"]
        initial2 = []
        output4 = multenterbox(text2, title2, input2, initial2)
        output4 = [i for i in output4]
        a = ""
        for i in output4:
            a+=f"{i}%20"
        a = a[:-3]
        obj = Google_items(output[0],output[1],a)
        obj.Youtube()

    elif output2=="IIITD":
        text3 = "Welcome to IIITD portal"
        title3 = "Required search"
        input3 = ["What do you want to search"]
        initial3 = []
        output5 = multenterbox(text3, title3, input3, initial3)
        output5 = [i for i in output5]
        a = ""
        for i in output5:
            a+=f"{i}%20"
        a = a[:-3]
        obj = Google_items(output[0],output[1],a)
        obj.IIITD()

    elif output2=="Maps":
        text3 = "Welcome to Google Maps"
        title3 = "Required search"
        input3 = ["Enter the location"]
        initial3 = []
        output5 = multenterbox(text3, title3, input3, initial3)
        output5 = [i for i in output5]
        a = ""
        for i in output5:
            a+=f"{i}%20"
        a = a[:-3]
        obj = Google_items(output[0],output[1],a)
        obj.Maps()
        
    elif output2=="Google Meet":
        text3 = "Welcom to Google Meet"
        title3 = "Required search"
        input3 = ["Enter the meet code"]
        initial3 = []
        output5 = multenterbox(text3, title3, input3, initial3)
        output5 = [i for i in output5]
        a = ""
        for i in output5:
            a+=f"{i}-"
        a = a[:-1]
        obj = Google_items(output[0],output[1],a)
        obj.GoogleMeet()

elif output1=="Marketplaces":
    msg = "Select the Marketplace you want to search on"
    Items1 = ["Amazon","Flipkart","Meesho","Bigbasket"]
    output2 = choicebox(msg, choices = Items1)
    if output2=="Amazon":
        text1 = "Welcome to Amazon"
        title1 = "Required search"
        input1 = ["Item name"]
        initial1 = []
        output3 = multenterbox(text1, title1, input1, initial1)
        output3 = [i for i in output3]
        a = ""
        for i in output3:
            a+=f"{i}+"
        a = a[:-1]
        obj = MarketPlaces(output[0],output[1],a)
        obj.Amazon()

    elif output2=="Flipkart":
        text2 = "Welcome to Flipkart"
        title2 = "Required search"
        input2 = ["Item name"]
        initial2 = []
        output4 = multenterbox(text2, title2, input2, initial2)
        output4 = [i for i in output4]
        a = ""
        for i in output4:
            a+=f"{i}%20"
        a = a[:-3]
        obj = MarketPlaces(output[0],output[1],a)
        obj.Flipkart()

    elif output2=="Meesho":
        text3 = "Welcome to Meesho"
        title3 = "Required search"
        input3 = ["Item name"]
        initial3 = []
        output5 = multenterbox(text3, title3, input3, initial3)
        output5 = [i for i in output5]
        a = ""
        for i in output5:
            a+=f"{i}%20"
        a = a[:-3]
        obj = MarketPlaces(output[0],output[1],a)
        obj.Meesho()
    
    elif output2=="Bigbasket":
        text4 = "Welcome to Bigbasket"
        title4 = "Required search"
        input4 = ["Item name"]
        initial4 = []
        output56 = multenterbox(text4, title4, input4, initial4)
        output56 = [i for i in output56]
        a = ""
        for i in output56:
            a+=f"{i}%20"
        a = a[:-3]
        obj = MarketPlaces(output[0],output[1],a)
        obj.Bigbasket()

elif output1=="Other":
    msg = "Select one of the following options"
    Items1 = ["Weather","News","TicTacToe","SnakeGame"]
    output2 = choicebox(msg, choices = Items1)
    if output2 == "Weather":
        text1 = "Enter the place whose weather you want to search"
        title1 = "Required search"
        input1 = ["Place name"]
        initial1 = []
        output3 = multenterbox(text1, title1, input1, initial1)
        output3 = [i for i in output3]
        a = ""
        for i in output3:
            a+=f"{i}+"
        a = a[:-1]
        obj = Other(output[0],output[1],a)
        obj.Weather()
    elif output2 == "News":
        obj = Other(output[0],output[1])
        obj.News()
    elif output2 == "TicTacToe":
        obj = Other(output[0],output[1])
        obj.TicTacToe()
    elif output2 == "SnakeGame":
        obj = Other(output[0],output[1])
        obj.Snake()