class script(object):   
    HELP_TXT = """π·π΄π {}\nπ·π΄ππ΄ πΈπ πΌπ π·π΄π»πΏ π²πΎπΌπΌπ°π½π³π."""

    ABOUT_TXT = """<b>β¬ πΌπ π½π°πΌπ΄: {}
β¬ π²ππ΄π°ππΎπ: <a href=https://t.me/FILESHAREBOTUSERS>AML UPDATES</a>
</b>"""

    SOURCE_TXT = """Till now not published """

    FILE_TXT = """Just files storee"""
    
    OWNER_TXT = """β― π²ππ΄π°ππΎπ: <a href=https://t.me/filesharebotusers>AML UPDATES</a>
Contact Owner for more details through:-"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and α©αα©α­  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>

β’ <code>/g_filter off</code> use this commoand + on/off in your group to control global filter in your group"""
   
    BUTTON_TXT = """Help: <b>Buttons</b>

-this bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:xxxxxxxxxxxx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """
βΊβΊ /set_template - ππ΄π π²ππππΎπΌ πΈπΌπ³π± ππ΄πΌπΏπ»π°ππ΄ π΅πΎπ π°πππΎ π΅πΈπ»ππ΄π. 
βΊβΊ /get_template - πΆπ΄π π²ππππ΄π½π πΈπΌπ³π± ππ΄πΌπΏπ»π°ππ΄ πΎπ΅ π°πππΎ π΅πΈπ»ππ΄π.
"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b>Ι΄α΄α΄α΄:</b>
<code>TΚΙͺs Mα΄α΄α΄Κα΄ OΙ΄ΚΚ Wα΄Κα΄s Fα΄Κ MΚ Aα΄α΄ΙͺΙ΄s</code>

π <u><b>Basic Command</b></u>
β’ /logs - <code>α΄α΄ Ι’α΄α΄ α΄Κα΄ Κα΄α΄α΄Ι΄α΄ α΄ΚΚα΄Κκ±</code>
β’ /stats - <code>α΄α΄ Ι’α΄α΄ κ±α΄α΄α΄α΄κ± α΄κ° κ°ΙͺΚα΄κ± ΙͺΙ΄ α΄Κ.</code>

ποΈ <u><b>Database & Server Command</b></u>
β’ /status - <code>α΄α΄ Ι’α΄α΄ sα΄α΄α΄α΄s α΄? sα΄Κα΄ α΄Κ</code>
β’ /stats - <code>α΄α΄ Ι’α΄α΄ α΄α΄α΄α΄α΄Κα΄κ±α΄ κ±α΄α΄α΄α΄κ±</code>
β’ /delete - <code>α΄α΄ α΄α΄Κα΄α΄α΄ α΄ κ±α΄α΄α΄Ιͺκ°Ιͺα΄ κ°ΙͺΚα΄ κ°Κα΄α΄ α΄Κ.</code>
β’ /deleteall - <code>α΄α΄ α΄α΄Κα΄α΄α΄ α΄ΚΚ κ°ΙͺΚα΄s κ°Κα΄α΄ α΄Κ.</code>
β’ /users - <code>α΄α΄ Ι’α΄α΄ ΚΙͺκ±α΄ α΄κ° α΄Κ α΄κ±α΄Κκ± α΄Ι΄α΄ Ιͺα΄κ±.</code>
β’ /chats - <code>α΄α΄ Ι’α΄α΄ ΚΙͺκ±α΄ α΄κ° α΄Κ α΄Κα΄α΄κ± α΄Ι΄α΄ Ιͺα΄κ±</code>
β’ /channel - <code>α΄α΄ Ι’α΄α΄ ΚΙͺκ±α΄ α΄κ° α΄α΄α΄α΄Κ α΄α΄Ι΄Ι΄α΄α΄α΄α΄α΄ α΄Κα΄Ι΄Ι΄α΄Κκ±</code>"""

    US_CHAT_TXT = """<b>Ι΄α΄α΄α΄:</b>
<code>TΚΙͺs Mα΄α΄α΄Κα΄ OΙ΄ΚΚ Wα΄Κα΄s Fα΄Κ MΚ Aα΄α΄ΙͺΙ΄s</code>

π― <u><b>Chat & User</b></u>
β’ /broadcast - <code>α΄α΄ ΚΚα΄α΄α΄α΄α΄κ±α΄ α΄ α΄α΄κ±κ±α΄Ι’α΄ α΄α΄ α΄ΚΚ α΄κ±α΄Κκ±</code>
β’ /group_broadcast - <code>α΄α΄ ΚΚα΄α΄α΄α΄α΄sα΄ α΄ α΄α΄ssα΄Ι’α΄ α΄α΄ α΄ΚΚ α΄α΄Ι΄Ι΄α΄α΄α΄α΄α΄ Ι’Κα΄α΄α΄s</code>
β’ /leave  - <code>α΄α΄ Κα΄α΄α΄ α΄ κ°Κα΄α΄ α΄ α΄Κα΄α΄.</code>
β’ /disable  -  <code>α΄α΄ α΄Ιͺκ±α΄ΚΚα΄ α΄ α΄Κα΄α΄.</code>
β’ /invite - <code>Tα΄ Ι’α΄α΄ α΄Κα΄ ΙͺΙ΄α΄ Ιͺα΄α΄ ΚΙͺΙ΄α΄ α΄? α΄Ι΄Κ α΄Κα΄α΄ α΄‘Κα΄Κα΄ α΄Κα΄ Κα΄α΄ Ιͺs α΄α΄α΄ΙͺΙ΄.</code>
β’ /ban_user  - <code>α΄α΄ Κα΄Ι΄ α΄ α΄κ±α΄Κ.</code>
β’ /unban_user  - <code>α΄α΄ α΄Ι΄Κα΄Ι΄ α΄ α΄κ±α΄Κ.</code>
β’ /restart - <code>Tα΄ Rα΄sα΄α΄Κα΄ α΄ Bα΄α΄</code>
β’ /usend - <code>Tα΄ Sα΄Ι΄α΄ α΄ Mα΄ssΙ’α΄α΄ α΄α΄ Pα΄Κα΄Ιͺα΄α΄Κα΄Κ Usα΄Κ</code>
β’ /gsend - <code>Tα΄ Sα΄Ι΄α΄ α΄ Mα΄ssα΄Ι’α΄ α΄α΄ Pα΄Κα΄Ιͺα΄α΄Κα΄Κ CΚα΄α΄</code>"""

    G_FIL_TXT = """<b>Ι΄α΄α΄α΄:</b>
<code>TΚΙͺs Mα΄α΄α΄Κα΄ OΙ΄ΚΚ Wα΄Κα΄s Fα΄Κ MΚ Aα΄α΄ΙͺΙ΄s</code>

π₯ <u><b>Adv Global Filter </b></u>
β’ /gfilter - <code>α΄α΄ α΄α΄α΄ Ι’Κα΄Κα΄Κ ?ΙͺΚα΄α΄Κs</code>
β’ /gfilters - <code>α΄α΄ α΄ Ιͺα΄α΄‘ ΚΙͺsα΄ α΄? α΄ΚΚ Ι’Κα΄Κα΄Κ ?ΙͺΚα΄α΄Κs<code>
β’ /delg - <code>α΄α΄ α΄α΄Κα΄α΄α΄ α΄ sα΄α΄α΄Ιͺ?Ιͺα΄ Ι’Κα΄Κα΄Κ ?ΙͺΚα΄α΄Κ</code>
β’ /delallg - <code>α΄α΄ α΄α΄Κα΄α΄α΄ α΄ΚΚ Ι’Κα΄Κα΄Κ κ°ΙͺΚα΄α΄Κκ±</code>
"""

    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
   
    ZOMBIES_TXT = """π·π΄π»πΏ ππΎπ ππΎ πΊπΈπ²πΊ πππ΄ππ

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
β’ /inkick - command with required arguments and i will kick members from group.
β’ /instatus - to check current status of chat member from group.
β’ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
β’ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
β’ /dkick - to kick deleted accounts."""

    IMAGE_TXT = """Not an editor π"""

    RESTRIC_TXT = """β€ πππ₯π©: Mα΄α΄α΄ π«

πππππ πππ πππ ππππππππ π πππππ πππππ πππ πππ ππ ππππππ πππππ πππππ ππππ πππππππππππ’.

βͺ/ban: π³π π»πΊπ πΊ πππΎπ πΏπππ πππΎ πππππ.
βͺ/unban: π³π πππ»πΊπ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tban: π³π ππΎπππππΊππππ π»πΊπ πΊ πππΎπ.
βͺ/mute: π³π ππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/unmute: π³π ππππππΎ πΊ πππΎπ ππ πππΎ πππππ.
βͺ/tmute: π³π ππΎπππππΊππππ ππππΎ πΊ πππΎπ.

β€ π­πππΎ:
πΆππππΎ πππππ /tmute ππ /tban πππ ππππππ½ πππΎπΌππΏπ πππΎ ππππΎ πππππ.

βπ€ππΊππππΎ: /ππ»πΊπ 2π½ ππ /πππππΎ 2π½.
πΈππ πΌπΊπ πππΎ ππΊπππΎπ: π/π/π½. 
 β’ π = ππππππΎπ
 β’ π = πππππ
 β’ π½ = π½πΊππ"""


    PIN_TXT ="""<b>PIN MODULE</b>
<b>πΏπΈπ½ π° πΌπ΄πππ°πΆπ΄../</b>

<b>π°π»π» ππ·π΄ πΏπΈπ½ ππ΄πΏπ»π°ππ΄π³ π²πΎπΌπΌπ°π½π³π π²π°π½ π±π΄ π΅πΎππ½π³ π·π΄ππ΄::</b>

<b>ππ²πΎπΌπΌπ°π½π³π π°π½π³ πππ°πΆπ΄π</b>

β /pin :- ππΎ πΏπΈπ½ ππ·π΄ πΌπ΄πππ°πΆπ΄ πΎπ½ ππΎππ π²π·π°ππ
β /unpin :- ππΎ ππ½πΏπΈπ½ ππ·π΄ π²ππππ΄π΄π½π πΏπΈπ½π½π΄π³ πΌπ΄ππ°π°πΆπ΄"""

    PASTE_TXT = """Not made 4 u"""

    TTS_TXT = """."""

    PINGS_TXT ="""<b>π Ping:</b>

Helps you to know your ping πΆπΌββοΈ

<b>Commands:</b>

β’ /alive - To check you are alive.
β’ /ping - To get your ping.
<b>πΉUsageπΉ :</b>

β’ This commands can be used in pms and groups
β’ This commands can be used buy everyone in the groups and bots pm
β’ Share us for more features"""

    TELE_TXT = """."""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""

    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

β /purge :- Delete All Messages From The Replied To Message, To The Current Message"""

    CREATOR_REQUIRED = """β<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """π? Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """β<b>ΰ΄ΰ΄¨ΰ΅ΰ΄¨ΰ΅ Admin ΰ΄ΰ΄ΰ΅ΰ΄ΰ΄€ΰ΅ΰ΄€ ΰ΄Έΰ΅ΰ΄₯ΰ΄²ΰ΄€ΰ΅ΰ΄€ΰ΅ ΰ΄ΰ΄Ύΰ΅» ΰ΄¨ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΄Ώΰ΄²ΰ΅ΰ΄² ΰ΄ͺΰ΅ΰ΄ΰ΅ΰ΄΅ΰ΄Ύ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ΰ΄ΰ΄ͺΰ΅ΰ΄ͺΰ΅ ΰ΄ΰ΄²ΰ΅ΰ΄²ΰ΄Ύΰ΄ ΰ΄ΰ΄ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅ΰ΄?ΰ΄Ύΰ΄±ΰ΅ΰ΄±ΰ΄Ώ ΰ΄€ΰ΄°ΰ΄Ύΰ΄...</b>"""
      
    CARB_TXT = """."""
    FOND_TXT = """."""

    SHARE_TXT = """."""



    


    
