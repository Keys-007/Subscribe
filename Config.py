import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(1068256093)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1461108175:AAF_MvI_qUhu30uY1Pcg1sXmx-7FNFa5Zxs"
    DATABASE_URL = "postgres://usuvepwsspsiqd:74a8ccf19a01e24081bd36b2405ca5994d58dd18125ecdabaf7bd9d339abe450@ec2-34-202-65-210.compute-1.amazonaws.com:5432/db0oji77o48nhr"
    APP_ID = "1859011"
    API_HASH = "e9b27b0efdbf11a12d82cf769487023f"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1068256093)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @viperadnan**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
