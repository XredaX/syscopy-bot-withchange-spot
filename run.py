from telegram import *
from telegram.ext import *
from database import user
import re
from configs import Config

print("start")
admins = ['1807268933', '646510124', '5403740273', '1826751444']
answer = 9999
sessionString = ""
target = ""
name = ""
share = ""
formatS = ""
name1 = ""
botUsername = "@SessionStringGeneratorZBot"
token = Config.BOT_TOKEN

def start(update, context):
    try:
        if str(update.message.chat_id) in admins:
            keyboard = [[KeyboardButton("🔗 ربط الحساب"), KeyboardButton("🔗 ربط القناة")], [KeyboardButton("✏️ التعديل"), KeyboardButton("🗑 الحذف")], [KeyboardButton("🔰 قائمة القنوات")]]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            update.message.reply_text('*👋 مرحبا بك عزيزي الأدمن  *`'+update.effective_user.full_name+'`*\n\nيمكنك الإختيار من القائمة الموجودة في الأسفل 👇*', parse_mode="Markdown", reply_markup=reply_markup)
    except :
        pass

def handlmsg(update, context):
    if str(update.message.chat_id) in admins:
        global sessionString, answer, target, name, share, formatS, name1

        if update.message.text == "⛔️ إلغاء" or update.message.text == "📋 العودة للقائمة الرئيسية":
            try:
                keyboard = [[KeyboardButton("🔗 ربط الحساب"), KeyboardButton("🔗 ربط القناة")], [KeyboardButton("✏️ التعديل"), KeyboardButton("🗑 الحذف")], [KeyboardButton("🔰 قائمة القنوات")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text('*👋 مرحبا بك عزيزي الأدمن  *`'+update.effective_user.full_name+'`*\n\nيمكنك الإختيار من القائمة الموجودة في الأسفل 👇*', parse_mode="Markdown", reply_markup=reply_markup)
                answer = 9999
            except:
                answer = 9999
                pass

        if update.message.text == "🔗 ربط الحساب":
            try:
                keyboard = [[KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                chat_id = update.message.chat_id
                document = open('sessionS.jpg', 'rb')
                context.bot.send_photo(chat_id, document, '*🤖 قم بالدخول لهذا البوت 👇🏻 '+botUsername+'\n\n💎 إتبع التعليمات التالية:\n\n1️⃣ قم بالدخول للبوت\n2️⃣ إضغط على الزر  *`Telethon`*\n3️⃣ أرسل هذا الأمر *`/skip`*\n4️⃣ أرسل الرقم الذي تريد النسخ به, مع رمز الدولة\n5️⃣ ستتوصل بكود التأكيد, أرسله بالطريقة التي تظهر في الصورة فالبوت\n6️⃣ في حالة كنت مفعل خاصية التأكيد الثنائي, سيطلب منك الكود أدخله\n7️⃣ سيرسل لك البوت رمز, قم بضغط عليه, سيتم نسخه\n8️⃣ عد هنا, للبوت الخاص بالنسخ و أرسل الرمز\n\n⚠️ يفضل إستعمال حساب لا يحتوي على أي معلومات خاصة أو مهمة* ⚠️', parse_mode="Markdown", reply_markup=reply_markup)
                answer = 0
            except:
                answer = 9999
                pass

        if answer == 1:
            try:
                sessionString = str(update.message.text)
                keyboard = [[KeyboardButton("✅ تأكيد")],[KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("*❔ هل أنت متأكد, في حالة كان الرمز خاطئ فلن يتم النسخ بطريقة صحيحة*", parse_mode= "Markdown", reply_markup=reply_markup)
            except:
                answer = 9999
                pass

        if answer == 2 and update.message.text == "✅ تأكيد":
            try:
                data = user.findsession(collection = "sessions", Owenr=str(update.message.chat_id))
                if int(data[1])>0:
                    user.editsession(collection = "sessions", Owenr=str(update.message.chat_id), Session=sessionString)
                else:
                    user.addsession(collection = "sessions", Owenr=str(update.message.chat_id), Session=sessionString)
                keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("✅ *تم حفظ الإتصال بنجاح*", parse_mode="Markdown", reply_markup=reply_markup)
            except:
                answer = 9999

        if update.message.text == "🔗 ربط القناة":
            try:
                keyboard = [[KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                chat_id = update.message.chat_id
                document = open('copylink.jpg', 'rb')
                context.bot.send_photo(chat_id, document, "*⚡️ قم بنسخ رابط اي منشور سبق وتم نشره فالقناة لي تريد تاخد منها التوصيات, ثم أرسله هنا*", parse_mode="Markdown", reply_markup=reply_markup)
                answer = 5
            except:
                answer = 9999
                pass

        if answer == 6:
            try:
                target = str(update.message.text)
                listy = re.findall('[0-9]+', str(target))
                target = listy[0]
                update.message.reply_text("*❔ إسم القناة لي تريد تنسخ منها*", parse_mode= "Markdown")
            except:
                update.message.reply_text("*🙁 الرابط الذي أرسلته غير صحيح, جرب مرة أخرى*", parse_mode= "Markdown")
                answer = 5

        if answer == 7:
            try:
                name = str(update.message.text)
                chat_id = update.message.chat_id
                document = open('copylink.jpg', 'rb')
                context.bot.send_photo(chat_id, document, "*⚡️ قم بنسخ رابط اي منشور سبق وتم نشره فالقناة لي تريد تنشر فيها التوصيات, ثم أرسله هنا*", parse_mode="Markdown")
            except:
                answer = 9999

        if answer == 8:
            try:
                share = str(update.message.text)
                listy = re.findall('[0-9]+', str(share))
                share = listy[0]
                chat_id = update.message.chat_id
                document = open('formarsignal.jpg', 'rb')
                context.bot.send_photo(chat_id, document, "*📶 قم بإرسال شكل التوصية لي تريده يتم نشره عندك فالقناة, بالتباع التعليمات التالية:\n\n*`📍قم بالستعمال coin في مكان إسم العملة.\n\n📍قم بالستعمال entry1 في مكان نقطة الدخول الأولى.\n\n📍قم بالستعمال entry2 في مكان نقطة الدخول الثانية.\n\n📍قم بالستعمال target1 في مكان الهذف الأول, نفس الشيء بالنسبة للهذف الثاني target2 والتالث target3, على حسب عدد الأهذاف فالتوصية الأصلية.\n\n📍قم بالستعمال stop في مكان الستوب لوز.`", parse_mode="Markdown")
            except:
                update.message.reply_text("*🙁 الرابط الذي أرسلته غير صحيح, جرب مرة أخرى*", parse_mode= "Markdown")
                answer = 7

        if answer == 9:
            try:
                formatS = str(update.message.text)
                condition = ["coin", "entry1", "target1", "stop"]
                a = 0
                for c in condition:
                    if re.search(c, formatS):
                        pass
                    else:
                        a += 1
                        break
                if a <= 0:
                    keyboard = [[KeyboardButton("✅ تأكيد")],[KeyboardButton("⛔️ إلغاء")]]
                    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                    update.message.reply_text("*❔ هل أنت متأكد, من أنك تريد إضافة هذه القناة*", parse_mode= "Markdown", reply_markup=reply_markup)
                else:
                    chat_id = update.message.chat_id
                    document = open('formarsignal.jpg', 'rb')
                    context.bot.send_photo(chat_id, document, "*📶 قم بإرسال شكل التوصية لي تريده يتم نشره عندك فالقناة, بالتباع التعليمات التالية:\n\n*`📍قم بالستعمال coin في مكان إسم العملة.\n\n📍قم بالستعمال entry1 في مكان نقطة الدخول الأولى.\n\n📍قم بالستعمال entry2 في مكان نقطة الدخول الثانية.\n\n📍قم بالستعمال target1 في مكان الهذف الأول, نفس الشيء بالنسبة للهذف الثاني target2 والتالث target3, على حسب عدد الأهذاف فالتوصية الأصلية.\n\n📍قم بالستعمال stop في مكان الستوب لوز.`", parse_mode="Markdown")
                    answer = 8
            except:
                answer = 9999

        if answer == 10 and update.message.text == "✅ تأكيد":
            try:
                user.addchannel(collection="channels1", Owenr=str(update.message.chat_id), target=target, name=name, share=share, formatS=formatS)
                keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("✅ *تم حفظ القناة بنجاح*", parse_mode="Markdown", reply_markup=reply_markup)
            except:
                answer = 9999

        if update.message.text == "✏️ التعديل" or update.message.text == "🗑 الحذف":
            try:
                data = user.findsession(collection = "channels1", Owenr=str(update.message.chat_id))
                if int(data[1])>0:
                    buttons = []
                    buttons.append([KeyboardButton("⛔️ إلغاء")])
                    for mb in data[0]:
                        buttons.append([KeyboardButton(mb["name"])])
                    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
                    update.message.reply_text("*📃 إختر إسم القناة من القائمة أسفله*", parse_mode="Markdown", reply_markup=keyboard)
                    if update.message.text == "✏️ التعديل":
                        answer = 14
                    else:
                        answer = 39
                else:
                    keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                    update.message.reply_text("*⚠️ لم تقم بإضافة أي قناة بعد*", parse_mode="Markdown", reply_markup=reply_markup)
                    answer = 9999
            except:
                answer = 9999

        if answer == 15:
            try:
                name = str(update.message.text)
                name1 = name
                data = user.findsession(collection = "channels1", Owenr=str(update.message.chat_id))
                lists = []
                keyboard = [[KeyboardButton("✏️ تعديل شكل التوصية الخاصة بك")], [KeyboardButton("✏️ تغيير القناة لي تريد ينشر فيها")], [KeyboardButton("✏️ تعديل القناة المنسوخ منها")], [KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                for mb in data[0]:
                    lists.append(mb["name"])
                if name in lists:
                        update.message.reply_text("*📋 إختر من القائمة أسفله, الشيء الذي تريد تغييره*", parse_mode="Markdown", reply_markup=reply_markup)
                else:
                    update.message.reply_text("*🙁 يبدو أنك أدخلت إسم غير موجود في قاعدة البيانات, جرب مرة أخرى*", parse_mode="Markdown")
                    answer = 14
            except:
                answer = 9999

        if update.message.text == "✏️ تعديل شكل التوصية الخاصة بك":
            try:
                chat_id = update.message.chat_id
                document = open('formarsignal.jpg', 'rb')
                context.bot.send_photo(chat_id, document, "*📶 قم بإرسال شكل التوصية لي تريده يتم نشره عندك فالقناة, بالتباع التعليمات التالية:\n\n*`📍قم بالستعمال coin في مكان إسم العملة.\n\n📍قم بالستعمال entry1 في مكان نقطة الدخول الأولى.\n\n📍قم بالستعمال entry2 في مكان نقطة الدخول الثانية.\n\n📍قم بالستعمال target1 في مكان الهذف الأول, نفس الشيء بالنسبة للهذف الثاني target2 والتالث target3, على حسب عدد الأهذاف فالتوصية الأصلية.\n\n📍قم بالستعمال stop في مكان الستوب لوز.`", parse_mode="Markdown")
                answer = 20
            except:
                answer = 9999

        if answer == 21:
            try:
                formatS = str(update.message.text)
                condition = ["coin", "entry1", "target1", "stop"]
                a = 0
                for c in condition:
                    if re.search(c, formatS):
                        pass
                    else:
                        a += 1
                        break
                if a <= 0:
                    keyboard = [[KeyboardButton("✅ تأكيد")],[KeyboardButton("⛔️ إلغاء")]]
                    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                    update.message.reply_text("*❔ هل أنت متأكد, من أنك تريد التعديل على شكل الصفقة*", parse_mode= "Markdown", reply_markup=reply_markup)
                else:
                    chat_id = update.message.chat_id
                    document = open('formarsignal.jpg', 'rb')
                    context.bot.send_photo(chat_id, document, "*📶 قم بإرسال شكل التوصية لي تريده يتم نشره عندك فالقناة, بالتباع التعليمات التالية:\n\n*`📍قم بالستعمال coin في مكان إسم العملة.\n\n📍قم بالستعمال entry1 في مكان نقطة الدخول الأولى.\n\n📍قم بالستعمال entry2 في مكان نقطة الدخول الثانية.\n\n📍قم بالستعمال target1 في مكان الهذف الأول, نفس الشيء بالنسبة للهذف الثاني target2 والتالث target3, على حسب عدد الأهذاف فالتوصية الأصلية.\n\n📍قم بالستعمال stop في مكان الستوب لوز.`", parse_mode="Markdown")
                    answer = 20
            except:
                answer = 9999
       
        if answer == 22 and update.message.text == "✅ تأكيد":
            try:
                user.updatechannel1(collection="channels1", Owenr=str(update.message.chat_id), formatS=formatS, name=name)
                keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("✅ *تم التعديل بنجاح*", parse_mode="Markdown", reply_markup=reply_markup)
            except:
                answer = 9999
        
        if update.message.text == "✏️ تعديل القناة المنسوخ منها":
            try:
                keyboard = [[KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                chat_id = update.message.chat_id
                document = open('copylink.jpg', 'rb')
                context.bot.send_photo(chat_id, document, "*⚡️ قم بنسخ رابط اي منشور سبق وتم نشره فالقناة لي تريد تاخد منها التوصيات, ثم أرسله هنا*", parse_mode="Markdown", reply_markup=reply_markup)
                answer = 25
            except:
                answer = 9999
     
        if answer == 26:
            try:
                target = str(update.message.text)
                listy = re.findall('[0-9]+', str(target))
                target = listy[0]
                update.message.reply_text("*❔ إسم القناة لي تريد تنسخ منها*", parse_mode= "Markdown")
            except:
                update.message.reply_text("*🙁 الرابط الذي أرسلته غير صحيح, جرب مرة أخرى*", parse_mode= "Markdown")
                answer = 25

        if answer == 27:
            try:
                name = str(update.message.text)
                keyboard = [[KeyboardButton("✅ تأكيد")],[KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("*❔ هل أنت متأكد, من أنك تريد التعديل*", parse_mode= "Markdown", reply_markup=reply_markup)
            except:
                answer = 9999

        if answer == 28 and update.message.text == "✅ تأكيد":
            try:
                user.updatechannel2(collection="channels1", Owenr=str(update.message.chat_id), target=target, name=name, name1=name1)
                keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("✅ *تم التعديل بنجاح*", parse_mode="Markdown", reply_markup=reply_markup)
            except:
                answer = 9999

        if update.message.text == "✏️ تغيير القناة لي تريد ينشر فيها":
            try:
                chat_id = update.message.chat_id
                document = open('copylink.jpg', 'rb')
                context.bot.send_photo(chat_id, document, "*⚡️ قم بنسخ رابط اي منشور سبق وتم نشره فالقناة لي تريد تنشر فيها التوصيات, ثم أرسله هنا*", parse_mode="Markdown")
                answer = 30
            except:
                answer = 9999

        if answer == 31:
            try:
                share = str(update.message.text)
                listy = re.findall('[0-9]+', str(share))
                share = listy[0]
                keyboard = [[KeyboardButton("✅ تأكيد")],[KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("*❔ هل أنت متأكد, من أنك تريد التعديل*", parse_mode= "Markdown", reply_markup=reply_markup)
            except:
                update.message.reply_text("*🙁 الرابط الذي أرسلته غير صحيح, جرب مرة أخرى*", parse_mode= "Markdown")
                answer = 30
        
        if answer == 32 and update.message.text == "✅ تأكيد":
            try:
                user.updatechannel3(collection="channels1", Owenr=str(update.message.chat_id), share=share, name1=name1)
                keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("✅ *تم التعديل بنجاح*", parse_mode="Markdown", reply_markup=reply_markup)
            except:
                answer = 9999
        
        if answer == 40:
            try:
                name = str(update.message.text)
                keyboard = [[KeyboardButton("✅ تأكيد")],[KeyboardButton("⛔️ إلغاء")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("*❔ هل أنت متأكد, من أنك تريد الحذف*", parse_mode= "Markdown", reply_markup=reply_markup)
            except:
                update.message.reply_text("*🙁 الرابط الذي أرسلته غير صحيح, جرب مرة أخرى*", parse_mode= "Markdown")
                answer = 9999

        if answer == 41 and update.message.text == "✅ تأكيد":
            try:
                user.deletechannel(collection="channels1", Owenr=str(update.message.chat_id), name1=name)
                keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                update.message.reply_text("✅ *تم الحذف بنجاح*", parse_mode="Markdown", reply_markup=reply_markup)
            except:
                answer = 9999

        if update.message.text == "🔰 قائمة القنوات":
            try:
                keyboard = [[KeyboardButton("📋 العودة للقائمة الرئيسية")]]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                members = user.findsession(collection = "channels1", Owenr=str(update.message.chat_id))
                li = []
                if int(members[1])>0:
                    for mb in members[0]:
                        name = mb["name"]
                        li.append(name)
                    update.message.reply_text("*📍 لائحة بأسماء القنوات لي يتم النسخ منها: \n\n*`"+str(*li)+"`", parse_mode="Markdown", reply_markup=reply_markup)
                else:
                    update.message.reply_text("*⚠️ لم تقم بإضافة أي قناة بعد*", parse_mode="Markdown", reply_markup=reply_markup)
                    answer = 9999
            except:
                answer = 9999
                
        answer += 1

updater = Updater(token, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, handlmsg))
updater.start_polling()
updater.idle()
