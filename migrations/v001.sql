BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "botInfo" (
	"token"	TEXT NOT NULL,
	"serverID"	INTEGER NOT NULL,
	"channelID"	INTEGER NOT NULL,
	"message"	TEXT NOT NULL,
	"link"	TEXT
);
CREATE TABLE IF NOT EXISTS "inputMemory" (
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
COMMIT;
