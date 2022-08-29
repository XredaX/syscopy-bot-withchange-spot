from telethon import TelegramClient, events
from telethon.sessions import StringSession
import re
from ticker_rules import rules
from configs import Config
from database import user
import os

print("start")
# admin = Config.ADMIN_ID
admin = '646510124'
api_id = '14607067'
api_hash = '70733cc9c675ed296a399e0a82a9b8d9'
datasession = user.findsession(collection = "sessions", Owenr=str(admin))
string = datasession[0][0]['Session']
client = TelegramClient(StringSession(string), api_id, api_hash)


@client.on(events.NewMessage)
async def handlmsg(event):
     try:
        datasession = user.findsession(collection = "sessions", Owenr=str(admin))
        string1 = datasession[0][0]['Session']

        if str(string1) == str(string):
            targets = []
            share = ''
            formatS = ''
            chat_id = event.chat_id
            msg = event.raw_text
            msg = msg.upper()
            res = msg.split()
            coin = ""
            datachannel = user.specifiChannel(collection = "channels1", Owenr=str(admin), target=str(chat_id))
            if datachannel[1]>0:
                    for i in datachannel[0]:
                            share = i["share"]
                            formatS = i["formatS"]
                            listy = re.findall("\d+\.\d+", str(msg))
                            try:
                                index = res.index('SHORT')
                                listy.sort(reverse=True)
                            except:
                                listy.sort()
                            if len(listy) >= 4:
                                for r in res:
                                    cleanString = re.sub('\W+','', r).upper()
                                    if re.search("USDT", cleanString):
                                        for t in rules:
                                            if cleanString == t:
                                                coin = cleanString
                                        break
                                    else:
                                        cleanString = cleanString+"USDT"
                                        for t in rules:
                                            if cleanString == t:
                                                coin = cleanString
                            share = str(share)
                            if coin != "":
                                coin = coin[:-4]
                                if re.search("coin", formatS):
                                    formatS = formatS.replace("coin", coin+" / USDT")
                                
                                if re.search('entry1', formatS):
                                    formatS = formatS.replace('entry1', listy[1])

                                if re.search('entry2', formatS):
                                    formatS = formatS.replace('entry2', listy[2])
                                    for i in range(1 ,15):
                                        try:
                                            target = 'target'+str(i)
                                            if re.search(target, formatS):
                                                formatS = formatS.replace(target, listy[i+2])
                                            else:
                                                break
                                        except:
                                            pass
                                else:
                                    for i in range(1 ,15):
                                        try:
                                            target = 'target'+str(i)
                                            if re.search(target, formatS):
                                                formatS = formatS.replace(target, listy[i+2])
                                            else:
                                                break
                                        except:
                                            pass


                                if re.search("stop", formatS):
                                    formatS = formatS.replace("stop", listy[0])

                                await client.send_message(int(share), formatS)

        else:
            os.system("python copymsg.py")
     except:
         pass

client.start()
client.run_until_disconnected()
