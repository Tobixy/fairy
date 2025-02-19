import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "27007231")) #optional
API_HASH = getenv("API_HASH", "ba3dcfb8a5b282263f50f438200fb35c") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5443243540").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID") or 5715764478)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "6080624164").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "1715348447").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "5633133204").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "5657257558").split()))

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://mex:rex@cluster7.jrzowqz.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6103019135:AAHsZsIcBkueu7CAm1BMUp7C3976U5J97Js")
BOT_WORKERS = int(getenv("BOT_WORKERS", "1"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001566281443").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personalacces
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "fairy") 
REPO_URL = getenv("REPO_URL", "https://github.com/Malik22222/fairy")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001849819947"))
CHANNEL = int(getenv("CHANNEL", "-1001849819947"))
SESSION1 = getenv("SESSION1","BQCN3swKrFxETNV8SyWvUHfFDMPMDLHVPsLdc4q57S9e8zGkmGaI7MPmLyo3wCTlhjLiUlPVrXOGY_M4HB0SD0HqKKgaeG6pr5E0xtIaZ1153di5AtLXrjEyQBKUJqno5Gn0qzyO3Grv_ydcbZMt29oC44mqgWGk6wzK96Eu6a3TBJdDKXxGeBK4r2em5UKM8_jZdFprXwmYsvJNcREn-cwssCqlRKnJQC7W96jaWI5BzIrkn38ZGsbracBLhRBkN1frrcZwPzQEaKNmCIbZ_7qlfY_acv0xl24NIq7neqbIJsgA6MIdOmLB6ROS5Th57KpdZ-FSe5NA-aTBSc_1xvKKAAAAAVtWnrgA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
