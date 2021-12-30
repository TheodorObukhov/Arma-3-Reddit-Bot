#bot.py
import discord
from discord import message
from dotenv import load_dotenv
import datetime
import sqlite3

#client
client = discord.Client()
load_dotenv()
conn = sqlite3.connect(r"PosterDB")
cur = conn.cursor()

#SQL pull
selectquery = '''
Select * from botInfo
'''
cur.execute(selectquery)
records = cur.fetchall()
for row in records:
    token = row[0]
    guild = row[1]
    channelID = row[2]
    messageSent = row[3]
    link = row[4]

#time
now = datetime.datetime.now()
nowDay = '{:02d}'.format(now.day)
nowHour = '{:02d}'.format(now.hour)
nowDayInt = int(nowDay)
nowHourInt = int(nowHour)

#Posting
@client.event
async def on_ready():
    print(f'{client.user} is connect to the following guild:\n')
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(channelID)
    await channel.send(str(messageSent) + ' ' + str(link))
client.run(token)
