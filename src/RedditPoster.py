#Reddit Poster
import datetime
import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
from migrate import *
#global params
window = tk.Tk()
webPage = ("https://old.reddit.com/r/FindAUnit/") 
now = datetime.datetime.now()
nowDay = '{:02d}'.format(now.day)
nowHour = '{:02d}'.format(now.hour)
nowDayInt = int(nowDay)
nowHourInt = int(nowHour)
secondsInHour = 60 * 60  
secondsInDay = 24 * secondsInHour
days = [1, 4, 7, 9, 12, 14, 16, 18, 20, 22, 24, 27]
hour = 10

#SQLITE3 connection
conn = sqlite3.connect(r"PosterDB")
cur = conn.cursor()

cur.execute(''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name='botInfo' ''')
if cur.fetchone()[0]==0:
    botInfoCreate(cur)
conn.commit()

cur.execute(''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name='inputMemory' ''')
if cur.fetchone()[0]==0:
    inputMemoryCreate(cur)
conn.commit()

#Selenium Actions
class driverVars:
    def get_time(self) -> str: #Time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def WebLaunch(self, user, passW, headless): #Main webdriver launch
        options = Options()
        if headless == True:
            options.headless = True
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            self.driver.get(webPage)
        else:
            options.headless = False
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            self.driver.get(webPage)

        while True:
            try:
                self.driver.find_element(By.XPATH,'//*[@id="login_login-main"]/input[2]')
                break
            except NoSuchElementException:
                print("Cannot find element. Trying again.")
                time.sleep(1)
        username = self.driver.find_element(By.XPATH,'//*[@id="login_login-main"]/input[2]') 
        ActionChains(self.driver).move_to_element(username).click(username).send_keys(user).perform() #Username input
        password = self.driver.find_element(By.XPATH, '//*[@id="login_login-main"]/input[3]')
        ActionChains(self.driver).reset_actions()
        ActionChains(self.driver).move_to_element(password).click(password).send_keys(passW).perform() #Password input
        signin = self.driver.find_element(By.XPATH,'//*[@id="login_login-main"]/div[4]/button').click() #Sign in
        print("Signed In.")

    def post_loop(self, title, mainStatement, secondStatement, groupStatement, styleStatement, languageStatement, opTimes, opType, discord):
        while True:
            try:
                self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div/a')
                break
            except NoSuchElementException:
                print("Cannot find element. Trying again.")
                time.sleep(1)

        def click(path, keys=[]):
            btn = self.driver.find_element(By.XPATH, path)
            clickAction = ActionChains(self.driver).move_to_element(btn).click(btn)
            withKeys = clickAction.send_keys(*keys) if keys else clickAction
            withKeys.perform()
            ActionChains(self.driver).reset_actions()
            
        click('/html/body/div[3]/div[2]/div/div/a') #Finds and clicks on 'Post' button
        click('//*[@id="newlink"]/ul/li[2]/a') # Finds and click on 'text' button
        click('//*[@id="title-field"]/div/textarea', [title]) # Finds, clicks on, and sends keys to Title field
        click(
            '//*[@id="text-field"]/div/div/div/div[1]/textarea',
            [
                groupStatement,
                Keys.ENTER,
                Keys.ENTER,
                styleStatement,
                Keys.ENTER,
                Keys.ENTER,
                languageStatement,
                Keys.ENTER,
                Keys.ENTER,
                opTimes,
                Keys.ENTER,
                Keys.ENTER,
                opType,
                Keys.ENTER,
                Keys.ENTER,
                mainStatement,
                Keys.ENTER,
                Keys.ENTER,
                secondStatement,
                Keys.ENTER,
                Keys.ENTER,
                discord
            ]
        ) # Finds, clicks on, and sends keys to main field
        click('//*[@id="flair-field"]/div/div/button') # Finds button to open 'flair' option fields

        ActionChains(self.driver).send_keys(Keys.END).perform()
        ActionChains(self.driver).reset_actions()

        while True:
            try:
                self.driver.find_element(By.XPATH,'//*[@id="acf7f706-2050-11e6-9d2c-0e78d0cc7a07"]')
                break
            except NoSuchElementException:
                print("Cannot find element. Trying again.")
                time.sleep(1)

        click('//*[@id="acf7f706-2050-11e6-9d2c-0e78d0cc7a07"]') # Finds correct flair and selects it
        click('//*[@id="newlink-flair-dropdown"]/form/button') # Applies the flair
        click('//*[@id="newlink"]/div[4]/button') # Submits the new post

        while True: 
            try:
                self.driver.find_element(By.XPATH,'//*[@id="shortlink-text"]')
                break
            except NoSuchElementException:
                print("Cannot find element. Trying again.")
                time.sleep(1)
        element = self.driver.find_element(By.XPATH,'//*[@id="shortlink-text"]')
        redditLink = element.get_attribute('value')
        print("Success! Posted","\n" "Day:",nowDay,"\n" "Hour:",nowHour,"\n" "link:", redditLink)

        linkUpdate = '''Update botInfo set link=?'''
        cur.execute(linkUpdate, (redditLink,)) #Updates SQL Database with new link
        conn.commit()

#GUI App + Main logic
class MyWindow:
    def botInfoUpdate(self):
        updatequery = '''Update botInfo set token=?, serverID=?,channelID=?,message=?'''
        coloumn_vals = (self.botToken1.get(), self.botGuild1.get(), self.botChannel1.get(), self.botMessage1.get())
        cur.execute(updatequery, coloumn_vals)
        conn.commit()

    def botPost(self): #Bot poster
        from bot import on_ready
        on_ready()
        print("Link posted.")

    def postLooper(self): #Looping function for posting
        while True:
            if nowDayInt in days & nowHourInt == hour:
                driverVars.post_loop(self, self.Title, self.firstPara, self.secondPara, self.groupName, self.groupStyle, self.language, self.opTimes, self.opTypes, self.discord)
                time.sleep(secondsInDay - 1)
            else:
                print("Sleeping. Current time:", driverVars.get_time(self))
                time.sleep(secondsInHour)

    def UseLast(self):
        def entryUseLast(self):
            self.UpdateBotInfoFunc = True
            try:    #SQL grabber (Database -> GUI)
                sql = '''
                select * from inputMemory
                '''
                cur.execute(sql)
                records = cur.fetchall()
                for row in records:
                    Username = row[0]
                    password = row[1]
                    Title = row[2]
                    firstPara = row[3]
                    secondPara = row[4]
                    groupName = row[5]
                    groupStyle = row[6]
                    language = row[7]
                    opTimes = row[8]
                    opTypes = row[9]
                    discord = row[10]

                    self.usrName1.insert(0, Username)
                    self.passW1.insert(0, password)
                    self.title1.insert(0, Title)
                    self.frstP1.insert(0, firstPara)
                    self.scndP1.insert(0, secondPara)
                    self.grpN1.insert(0, groupName)
                    self.grpSty1.insert(0, groupStyle)
                    self.lng1.insert(0, language)
                    self.opTime1.insert(0, opTimes)
                    self.opType1.insert(0, opTypes)
                    self.discord1.insert(0, discord)
            except sqlite3.Error as error:
                print("Failed to pull.")

        def entryUseLastBot(self):
            try:
                sql = '''
                select * from botInfo
                '''
                cur.execute(sql)
                records = cur.fetchall()
                for row in records:
                    token = row[0]
                    server = row[1]
                    channel = row[2]
                    message = row[3]

                    self.botToken1.insert(0, token)
                    self.botGuild1.insert(0, server)
                    self.botChannel1.insert(0, channel)
                    self.botMessage1.insert(0, message)
            except sqlite3.Error as error:
                print("Failed to pull.")
        entryUseLast(self)
        if self.OnandOffBot.get() == 1:
            entryUseLastBot(self)
        else:
            exit

    def updateTask(self, conn, task): #SQL updater (GUI->Database)
        sql = '''
        UPDATE inputMemory
        SET username=?,
            password=?,
            title=?,
            firstpara=?,
            secondpara=?,
            groupname=?, 
            groupstyle=?, 
            language=?, 
            optime=?, 
            optype=?,
            discord=?
        '''
        cur.execute(sql, task)
        conn.commit()

    def updateTaskBot(self, conn, task):
        sqlBot = '''
        UPDATE botInfo
        SET token=?,
            serverID=?,
            channelID=?,
            message=?
        '''
        cur.execute(sqlBot, task)
        conn.commit()

    def goFunction(self): #Main Logic

        self.Username = self.usrName1.get()
        self.password = self.passW1.get()
        self.Title = self.title1.get()
        self.firstPara = self.frstP1.get()
        self.secondPara = self.scndP1.get()
        self.groupName = self.grpN1.get()
        self.groupStyle = self.grpSty1.get()
        self.language = self.lng1.get()
        self.opTimes = self.opTime1.get()
        self.opTypes = self.opType1.get()
        self.discord = self.discord1.get()

        self.token = self.botToken1.get()
        self.server = self.botGuild1.get()
        self.botChannel = self.botChannel1.get()
        self.message = self.botMessage1.get()
        if self.UpdateBotInfoFunc:
            self.botInfoUpdate()

        with conn: #Updates the SQL database with the new info
            self.updateTask(conn, (self.Username, self.password, self.Title, self.firstPara, self.secondPara, self.groupName, self.groupStyle, self.language, self.opTimes, self.opTypes, self.discord))
            self.updateTaskBot(conn, (self.token, self.server, self.botChannel, self.message))

        if self.runHeadless.get() == 1: #guess bro
            headlessMode = True
        else:
            headlessMode = False

        if self.OnandOffBot.get() == 1:
            if self.repeatScript.get() == 1:
                driverVars.WebLaunch(self, self.Username, self.password, headlessMode)
                if nowDayInt != days or nowHourInt != hour:
                    driverVars.post_loop(self, self.Title, self.firstPara, self.secondPara, self.groupName, self.groupStyle, self.language, self.opTimes, self.opTypes, self.discord)
                self.botPost()
                self.postLooper()     
            else:
                driverVars.WebLaunch(self, self.Username, self.password, headlessMode)
                driverVars.post_loop(self, self.Title, self.firstPara, self.secondPara, self.groupName, self.groupStyle, self.language, self.opTimes, self.opTypes, self.discord)
                self.botPost()
        else:
            if self.repeatScript.get() == 1:
                driverVars.WebLaunch(self, self.Username, self.password, headlessMode)
                if nowDayInt != days or nowHourInt != hour:
                    driverVars.post_loop(self, self.Title, self.firstPara, self.secondPara, self.groupName, self.groupStyle, self.language, self.opTimes, self.opTypes, self.discord)
                self.postLooper()     
            else:
                driverVars.WebLaunch(self, self.Username, self.password, headlessMode)
                driverVars.post_loop(self, self.Title, self.firstPara, self.secondPara, self.groupName, self.groupStyle, self.language, self.opTimes, self.opTypes, self.discord)

    def enableDisable(self): #Bot Enable/Disable
        if self.OnandOffBot.get() == 1:
            self.botToken1.configure(state='normal')
            self.botGuild1.configure(state='normal')
            self.botChannel1.configure(state='normal')
            self.botMessage1.configure(state='normal')
        else:
            self.botToken1.configure(state='disabled')
            self.botGuild1.configure(state='disabled')
            self.botChannel1.configure(state='disabled')
            self.botMessage1.configure(state='disabled')

    def __init__(self, win): #GUI
        self.UpdateBotInfoFunc = False

        lbl = tk.Label(window, text="Please fill out the following fields").grid(row=1, column=1)
        #basic inputs
        self.usrNameLbl = tk.Label(window, text="Username:").grid(row=2, column=1)
        self.usrName1 = tk.Entry(window, width= 25)
        self.usrName1.grid(row=3, column=1)

        self.passWLbl = tk.Label(window, text="Password:").grid(row=4, column=1)
        self.passW1 = tk.Entry(window, width= 25)
        self.passW1.grid(row=5, column=1)

        self.titleLbl = tk.Label(window, text="Input Title:").grid(row=6, column=1)
        self.title1 = tk.Entry(window, width= 25)
        self.title1.grid(row=7,column=1)

        self.frstPLbl = tk.Label(window, text="Input First Paragraph:").grid(row=8, column=1)
        self.frstP1 = tk.Entry(window, width= 25)
        self.frstP1.grid(row=9, column=1)

        self.scndPLbl = tk.Label(window, text="Input Second Paragraph:").grid(row=10, column=1)
        self.scndP1 = tk.Entry(window, width= 25)
        self.scndP1.grid(row=11, column=1)

        self.grpNLbl = tk.Label(window, text="Input Group Name:").grid(row=12, column=1)
        self.grpN1 = tk.Entry(window, width= 25)
        self.grpN1.grid(row=13, column=1)

        self.grpStyLbl = tk.Label(window, text="Input Group Style:").grid(row=14, column=1)
        self.grpSty1 = tk.Entry(window, width= 25)
        self.grpSty1.grid(row=15, column=1)

        self.lngLbl = tk.Label(window, text="Input Primary Language:").grid(row=16, column=1)
        self.lng1 = tk.Entry(window, width= 25)
        self.lng1.grid(row=17, column=1)

        self.opTimeLbl = tk.Label(window, text="Input Op Times:").grid(row=18, column=1)
        self.opTime1 = tk.Entry(window, width= 25)
        self.opTime1.grid(row=19, column=1)

        self.opTypeLbl = tk.Label(window, text="Input Op Type:").grid(row=20, column=1)
        self.opType1 = tk.Entry(window, width= 25)
        self.opType1.grid(row=21, column=1)

        self.discordlbl = tk.Label(window, text="Discord Link:").grid(row=22, column=1)
        self.discord1 = tk.Entry(window, width=25)
        self.discord1.grid(row=23, column=1)

        #repeat button
        self.repeatScript = tk.IntVar()
        tk.Checkbutton(window, text="Loop Process?", variable=self.repeatScript).grid(row=24, column=1)
        #Headless
        self.runHeadless = tk.IntVar()
        tk.Checkbutton(window, text="Run Headless?", variable=self.runHeadless).grid(row=25, column=1)

        #Use last inputs
        tk.Button(window, text="Use last inputs?", command=self.UseLast).grid(row=26, column=1)
        #go button
        tk.Button(window, text="Go", command=self.goFunction).grid(row=27, column=1)

        #bot controls
        self.OnandOffBot = tk.IntVar()
        tk.Checkbutton(window, text="Employ Discord Bot?", variable=self.OnandOffBot, command= self.enableDisable).grid(row=1, column=2)

        self.botTokenLbl = tk.Label(window, text="Bot Token:").grid(row=2, column=2)
        self.botToken1 = tk.Entry(window, width= 25, state='disabled')
        self.botToken1.grid(row=3,column=2)

        self.botGuildLbl = tk.Label(window, text="Server ID:").grid(row=4, column=2)
        self.botGuild1 = tk.Entry(window,width=25, state='disabled')
        self.botGuild1.grid(row=5, column=2)

        self.botChannelLbl = tk.Label(window, text="Channel ID:").grid(row=6, column=2)
        self.botChannel1 = tk.Entry(window, width=25, state='disabled')
        self.botChannel1.grid(row=7, column=2)

        self.botMessageLbl = tk.Label(window, text="Message Posted:").grid(row=8, column=2)
        self.botMessage1 = tk.Entry(window, width=25, state='disabled')
        self.botMessage1.grid(row=9,column=2)

MyWin= MyWindow(window)
window.title("Reddit Poster")
window.geometry("500x600")
window.mainloop()

#TO DO: Run GUI in different thread to avoid freezing