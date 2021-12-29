def botInfoCreate(cur):
    cur.execute('''CREATE TABLE "botInfo" (
	"token"	TEXT,
	"serverID"	INTEGER,
	"channelID"	INTEGER,
	"message"	TEXT,
	"link"	TEXT
    );
    ''')

def inputMemoryCreate(cur):
    cur.execute('''
    CREATE TABLE "inputMemory" (
	"username"	TEXT,
	"password"	TEXT,
	"title"	TEXT,
	"firstpara"	TEXT,
	"secondpara"	TEXT,
	"groupname"	TEXT,
	"groupstyle"	TEXT,
	"language"	TEXT,
	"optime"	TEXT,
	"optype"	TEXT,
	"discord"	TEXT
    );
    ''')