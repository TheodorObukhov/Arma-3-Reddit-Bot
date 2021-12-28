Example Format:
title = "[A3][Recruiting][Semi-Serious Milsim][US][New Players Welcome] Task Force Orion"

First paragraph = "Other info: Founded in 2020, Task Force Orion strives in bringing a realistic yet fun milsim experience to its members. 
We provide training to each member so they can improve and move up in their field. 
TFO runs a multitude of different operations and trainings, ranging from basic assaults and squad/platoon 
tactics to assisting foreign governments and conducting special operations."

Second Paragraph = "Unit Requirements: Must have legal copy of Arma 3, must have Teamspeak 3, 
must have a microphone and be able to speak proficient English, and must be 15 years or older. 
Exceptions can be made as long as you can show a level of maturity."

Group Name = "Group: Task Force Orion"

Group Style = "Play Style: Semi-Serious Milsim"

Primary Language = "Main Language: English"

Op Times = "Operation Times: 7pm EST Wednesday & Saturday"

Op Type = "Operation Type: Campaign"

Discord link = "Discord: https://discord.gg/DQUzjX3Uny"

Final Output:
https://www.reddit.com/r/FindAUnit/comments/q3kog6/a3recruitingsemiserious_milsimusnew_players/


You can work with the formatting but it's mainly how its posted right there. The indentations is the only real defining variable so you'll always have 7 indentations. I don't have any plans on adding more formats, but over time maybe I'll think about it a bit. This is a format that I've used and looks clean and professional from my point of view. If you'd like another, source code is right there. 

If you have any suggestions on how to improve on the code or anything you'd like to see added, feel free to post a comment on github. This is just a little project for a friend and his server but I'll try to keep it updated. 

On the note of bugs, I personally haven't found any yet but if you do just post something on github.

HOW TO USE:
The base poster works very simply. You launch it, it takes your username and password to reddit, logs in as that user, goes and posts on r/FindaUnit. It adds all necessary flairs. What you put in for each section is what it will post. If you'd like to see the format it will post in, above there is an example with a link to post made by the bot. 

This may not work right now, but if it does, in the GUI for the poster, there should also be a section for a discord bot. If you have a personal discord bot and it is in your server, you can put in the token for the bot, the server id, the channel you want to post in, and what you want the bot to say. The format is [link] #Whatever text you input#. This way everytime the bot posts, it will automatically notify your discord so people can go and upvote it.


FOR PEOPLE GOING INTO SOURCE CODE:
All of the time sleeps are NECESSARY. Otherwise the website itself doesn't have time to react and you'll get an error that crashes the process. I don't have a "try again x amount of times" function and I can't be fucked at the moment. Might delete this later.
