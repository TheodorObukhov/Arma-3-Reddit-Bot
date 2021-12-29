**INSTALLATION**
Download all the files. Open terminal with C:/path/to/requirements.txt. Run `pip install -r requirements.txt`

**Example Format(THIS IS NOT A RECRUITMENT SCHEME, LITERALLY JUST AN EXAMPLE):**
_title_ = "[A3][Recruiting][Semi-Serious Milsim][US][New Players Welcome] Task Force Orion"

_First paragraph_ = "Other info: Founded in 2020, Task Force Orion strives in bringing a realistic yet fun milsim experience to its members. 
We provide training to each member so they can improve and move up in their field. 
TFO runs a multitude of different operations and trainings, ranging from basic assaults and squad/platoon 
tactics to assisting foreign governments and conducting special operations."

_Second Paragraph_= "Unit Requirements: Must have legal copy of Arma 3, must have Teamspeak 3, 
must have a microphone and be able to speak proficient English, and must be 15 years or older. 
Exceptions can be made as long as you can show a level of maturity."

_Group Name_ = "Group: Task Force Orion"

_Group Style_ = "Play Style: Semi-Serious Milsim"

_Primary Language_ = "Main Language: English"

_Op Times_ = "Operation Times: 7pm EST Wednesday & Saturday"

_Op Type_ = "Operation Type: Campaign"

_Discord link_ = "Discord: https://discord.gg/DQUzjX3Uny"

**Final Output:**
https://www.reddit.com/r/FindAUnit/comments/q3kog6/a3recruitingsemiserious_milsimusnew_players/


You can work with the formatting but it's mainly how its posted right there. The indentations is the only real defining variable so you'll always have 7 indentations. I don't have any plans on adding more formats at the moment. This is a format that I've used and looks clean and professional from my point of view. If you'd like another, feel free to modify the source code.

If you have any suggestions on how to improve on the code or anything you'd like to see added, feel free to post a comment on github. This is just a little project for a friend and his server but I'll try to keep it updated. 

On the note of bugs, I personally haven't found any yet but if you do just post something on github.

**HOW TO USE:**
The base poster works very simply. You launch it, it takes your username and password to reddit, logs in as that user, goes and posts on r/FindaUnit. It adds all necessary flairs. What you put in for each section is what it will post. If you'd like to see the format it will post in, above there is an example with a link to post made by the bot. 

There are four main buttons to focus on: Loop Process, Run Headless, Use Last Inputs, and Employ Discord Bot:

_Loop Process_: Keeps the program running. It will make a post, and it will wait for the next correct day/hour to post. It will always post at 10am on these days: [1, 4, 7, 9, 12, 14, 16, 18, 20, 22, 24, 27]

_Run Headless_: This is very good to pair with Loop Process. Essentially it configures the chromedriver to run without opening its own screen and showing you everything, which can be annoying 24/7. If you're concerned as to what it will do, you can run it in terminal and it will print out what it does.

_Use Last Inputs_: This button pulls from the database to which your last entries have been logged into and inserts into the entry boxes. You can modify them or if they are satisfactory, you can simply press "Go".

_Employ Discord Bot_: If you'd like to have the link posted on discord so the rest of your server can go and upvote it, you can do so with this. If you have your own discord bot, you can input the token, the server to which it'll connect to, the channel id you'd like it to post to, and the message. The format for the message is = [Message + " " + link]. If you do not have a discord bot but would like to use this feature, feel free to make your own in the tutorial with this link: https://discordpy.readthedocs.io/en/stable/discord.html. Remember, all you really need to do is make the bot, copy the token, and invite it into your own server. The scripting is taken care of.
