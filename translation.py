from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} , 

`I'am a url to telegram file or media uploader bot with permanent thumbnail support`.

👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://telegram.me/BX_Botz)
"""
    HELP_TEXT = """
<b><u>Link to Media or File</u></b>
➠ Send a link for upload to telegram file or media.

<b><u>Set Thumbnail</u></b>
➠ Send a photo to make it as permanent thumbnail.

<b><u>Deleting Thumbnail</u></b>
➠ Send /delthumb to deleting thumbnail.

<b><u>Show Thumbnail</u></b>
➠ Send /showthumb to view custom thumbnail.

Made With ❤ By @BX_Botz
"""
    ABOUT_TEXT = """
- **Bot :** `URL Uploader`
- **Creator :** [ᴍʜᴅ ᴍᴜꜰᴀᴢ](https://telegram.me/Mufaz123)
- **Channel :** [ʙx ʙᴏᴛᴢ](https://telegram.me/BX_Botz)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://t.me/nokiyirunnoippokitum)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/BX_Botz'),
        InlineKeyboardButton('👥Support Group', url='https://telegram.me/BxSupport')
        ],[
        InlineKeyboardButton('⚙️Help', callback_data='help'),
        InlineKeyboardButton('🔰About', callback_data='about')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data='home'),
        InlineKeyboardButton('🔰About', callback_data='about')
        ],[
        InlineKeyboardButton('🔒Close', callback_data='close'),
        InlineKeyboardButton('⚜️ Share ⚜️', url='tg://msg?text=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%20%0AToday%20I%20Just%20Found%20out%20An%20Nice%20And%20Poweful%20URL%20Uploader%20Bot%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Bot%20Link%20%3A%20%40BxUploaderV2Bot')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data='home'),
        InlineKeyboardButton('⚙️Help', callback_data='help')
        ],[
        InlineKeyboardButton('🔒Close', callback_data='close'),
        InlineKeyboardButton('⚜️ Share ⚜️', url='tg://msg?text=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%20%0AToday%20I%20Just%20Found%20out%20An%20Nice%20And%20Poweful%20URL%20Uploader%20Bot%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Bot%20Link%20%3A%20%40BxUploaderV2Bot')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>Downloading To My server Please Wait...</code>"    
    UPLOAD_START = "<code>Uploading into Telegram...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @BX_Botz"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
