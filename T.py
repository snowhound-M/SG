from telethon import TelegramClient, events
from telethon.tl.custom import Button

# Replace these with your own values
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# Create the client and connect
client = TelegramClient('bot_session', api_id, api_hash)

# Define a simple command handler
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
# Create an inline button
button = Button.inline("Add me to your chat!", b"add_me")
await event.reply(
"Hey there! My name is Rose - I'm here to help you manage your groups! "
"Use /help to find out more about how to use me to my full potential.\n\n"
"Join my news channel to get information on all the latest updates.\n\n"
"Use the /privacy command to view the privacy policy, and interact with your data.",
buttons=[button]
)

@client.on(events.NewMessage(pattern='/privacy'))
async def privacy(event):
await event.reply("Here is the privacy policy...\n[Details about privacy]")

@client.on(events.CallbackQuery(data=b'add_me'))
async def on_button_click(event):
# Handle the button click here
await event.answer("Thank you for your interest! To add me to your group, please use the link below:\n"
"[Add me to your group](https://t.me/your_bot_username?startgroup=start)",
alert=True)

@client.on(events.NewMessage(pattern='/help'))
async def help(event):
# Define buttons for each row
buttons = [
[Button.inline("Admin", b"admin_info"), Button.inline("Antiflood", b"antiflood_info"), Button.inline("AntiRaid", b"antiraid_info")],
[Button.inline("Approval", b"approval_info"), Button.inline("Bans", b"bans_info"), Button.inline("Blocklists", b"blocklists_info")],
[Button.inline("CAPTCHA", b"captcha_info"), Button.inline("Clean Commands", b"clean_commands_info"), Button.inline("Clean Service", b"clean_service_info")],
[Button.inline("Connections", b"connections_info"), Button.inline("Disabling", b"disabling_info"), Button.inline("Federations", b"federations_info")],
[Button.inline("Filters", b"filters_info"), Button.inline("Formatting", b"filters_formatting"), Button.inline("Greetings", b"btn5_3")],
[Button.inline("Button 6-1", b"btn6_1"), Button.inline("Button 6-2", b"btn6_2"), Button.inline("Button 6-3", b"btn6_3")],
[Button.inline("Button 7-1", b"btn7_1"), Button.inline("Button 7-2", b"btn7_2"), Button.inline("Button 7-3", b"btn7_3")],
[Button.inline("Button 8-1", b"btn8_1"), Button.inline("Button 8-2", b"btn8_2"), Button.inline("Button 8-3", b"btn8_3")],
[Button.inline("Button 9-1", b"btn9_1"), Button.inline("Button 9-2", b"btn9_2"), Button.inline("Button 9-3", b"btn9_3")],
[Button.inline("Button 10-1", b"btn10_1")]  # Last row with only one button
]

await event.reply(
"Help\n\n"
"Hey! My name is Rose. I am a group management bot, here to help you get around and keep the order in your groups!\n"
"I have lots of handy features, such as flood control, a warning system, a note keeping system, and even predetermined replies on certain keywords.\n\n"
"Helpful commands:\n"
"- /start: Starts me! You've probably already used this.\n"
"- /help: Sends this message; I'll tell you more about myself!\n"
"- /donate: Gives you info on how to support me and my creator.\n\n"
"If you have any bugs or questions on how to use me, have a look at my website, or head to @RoseSupportChannel.\n"
"All commands can be used with the following: / !",
buttons=buttons
)

@client.on(events.CallbackQuery(data=b'admin_info'))
async def admin_info(event):
await event.answer("Sending admin information...", alert=True)
await event.edit(
"Admin\n\n"
"Make it easy to promote and demote users with the admin module!\n\n"
"Admin commands:\n"
"- /promote <reply/username/mention/userid>: Promote a user.\n"
"- /demote <reply/username/mention/userid>: Demote a user.\n"
"- /adminlist: List the admins in the current chat.\n"
"- /admincache: Update the admin cache, to take into account new admins/admin permissions.\n"
"- /anonadmin <yes/no/on/off>: Allow anonymous admins to use all commands without checking their permissions. Not recommended.\n"
"- /adminerror <yes/no/on/off>: Send error messages when normal users use admin commands. Default: on.\n\n"
"Sometimes, you promote or demote an admin manually, and Rose doesn't realize it immediately. This is because to avoid spamming Telegram servers, admin status is cached locally.\n"
"This means that you sometimes have to wait a few minutes for admin rights to update. If you want to update them immediately, you can use the /admincache command; that'll force Rose to check who the admins are again.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'antiflood_info'))
async def antiflood_info(event):
await event.answer("Sending antiflood information...", alert=True)
await event.edit(
"Antiflood\n\n"
"You know how sometimes, people join, send 100 messages, and ruin your chat? With antiflood, that happens no more!\n\n"
"Antiflood allows you to take action on users that send more than x messages in a row. Actions are: ban/mute/kick/tban/tmute\n\n"
"Admin commands:\n"
"- /flood: Get the current antiflood settings\n"
"- /setflood <number/off/no>: Set the number of consecutive messages to trigger antiflood. Set to '0', 'off', or 'no' to disable.\n"
"- /setfloodtimer <count> <duration>: Set the number of messages and time required for timed antiflood to take action on a user. Set to just 'off' or 'no' to disable.\n"
"- /floodmode <action type>: Choose which action to take on a user who has been flooding. Possible actions: ban/mute/kick/tban/tmute\n"
"- /clearflood <yes/no/on/off>: Whether to delete the messages that triggered the flood.\n\n"
"Examples:\n"

"- Set antiflood to trigger after 7 messages:\n"
"  -> /setflood 7\n\n"
"- Disable antiflood:\n"
"  -> /setflood off\n\n"
"- Set timed antiflood to trigger after 10 messages in 30 seconds:\n"
"  -> /setfloodtimer 10 30s\n\n"
"- Disable timed antiflood:\n"
"  -> /setfloodtimer off\n\n"
"- Set the antiflood action to mute:\n"
"  -> /floodmode mute\n\n"
"- Set the antiflood action to a 3-day ban:\n"
"  -> /floodmode tban 3d",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'antiraid_info'))
async def antiraid_info(event):
await event.answer("Sending antiraid information...", alert=True)
await event.edit(
"AntiRaid\n\n"
"Some people on Telegram find it entertaining to 'raid' chats. During a raid, hundreds of users join a chat to spam.\n\n"
"The antiraid module allows you to quickly stop anyone from joining when such a raid is happening.\n"
"All new joins will be temporarily banned for the next few hours, allowing you to wait out the spam attack until the trolls stop.\n\n"
"Admin commands:\n"
"- /antiraid <optional time/off/no>: Toggle antiraid. All new joins will be temporarily banned for the next few hours.\n"
"- /raidtime <time>: View or set the desired antiraid duration. Default 6h.\n"
"- /raidactiontime <time>: View or set the time for antiraid to tempban users for. Default 1h.\n"
"- /autoantiraid <number/off/no>: Set the number of joins per minute after which to enable automatic antiraid. Set to '0', 'off', or 'no' to disable.\n\n"
"Examples:\n"
"- Enable antiraid for 3 hours:\n"
"  -> /antiraid 3h\n\n"
"- Disable antiraid:\n"
"  -> /antiraid off\n\n"
"- Automatically enable antiraid if over 15 users join in under a minute:\n"
"  -> /autoantiraid 15\n\n"
"- Disable automatic antiraid:\n"
"  -> /autoantiraid off",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'approval_info'))
async def approval_info(event):
await event.answer("Sending approval information...", alert=True)
await event.edit(
"Approval\n\n"
"Sometimes, you might trust a user not to send unwanted content.\n"
"Maybe not enough to make them admin, but you might be ok with locks, blocklists, and antiflood not applying to them.\n\n"
"That's what approvals are for - approve of trustworthy users to allow them to send content without restrictions.\n\n"
"User commands:\n"
"- /approval: Check a user's approval status in this chat.\n\n"
"Admin commands:\n"
"- /approve: Approve of a user. Locks, blocklists, and antiflood won't apply to them anymore.\n"
"- /unapprove: Unapprove of a user. They will now be subject to locks, blocklists, and antiflood again.\n"
"- /approved: List all approved users.\n"
"- /unapproveall: Unapprove ALL users in a chat. This cannot be undone.\n\n",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'bans_info'))
async def bans_info(event):
await event.answer("Sending bans information...", alert=True)
await event.edit(
"Bans\n\n"
"Some people need to be publicly banned; spammers, annoyances, or just trolls.\n\n"
"This module allows you to do that easily, by exposing some common actions, so everyone will see!\n\n"

"User commands:\n"
"- /kickme: Users that use this, kick themselves.\n\n" "Admin commands:\n" "- /ban: Ban a user.\n" "- /dban: Ban a user by reply, and delete their message.\n" "- /sban: Silently ban a user, and delete your message.\n" "- /tban: Temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.\n" "- /unban: Unban a user.\n" "- /mute: Mute a user.\n" "- /dmute: Mute a user by reply, and delete their message.\n" "- /smute: Silently mute a user, and delete your message.\n" "- /tmute: Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.\n" "- /unmute: Unmute a user.\n" "- /kick: Kick a user.\n" "- /dkick: Kick a user by reply, and delete their message.\n" "- /skick: Silently kick a user, and delete your message\n\n" "Examples:\n" "- Mute a user for two hours.\n" "  -> /tmute @username 2h",
buttons=[[Button.inline("Back", b"help_back")]] )

@client.on(events.CallbackQuery(data=b'blocklists_info'))
async def blocklists_info(event):
await event.answer("Sending blocklists information...", alert=True)
await event.edit(
"Blocklists\n\n"
"Want to stop people asking stupid questions? Or ban anyone saying censored words? Blocklists is the module for you!\n\n"
"From blocking rude words, filenames/extensions, to specific emoji, everything is possible.\n\n"
"Admin commands:\n"
"- /addblocklist <blocklist trigger> <reason>: Add a blocklist trigger. You can blocklist an entire sentence by putting it in 'quotes'.\n"
"- /rmblocklist <blocklist trigger>: Remove a blocklist trigger.\n"
"- /unblocklistall: Remove all blocklist triggers - chat creator only.\n"
"- /blocklist: List all blocklisted items.\n"
"- /blocklistmode <blocklist mode>: Set the desired action to take when someone says a blocklisted item. Available: nothing/ban/mute/kick/warn/tban/tmute.\n"
"- /blocklistdelete <yes/no/on/off>: Set whether blocklisted messages should be deleted. Default: on.\n"
"- /setblocklistreason <reason>: Set the default blocklist reason to warn people with.\n"
"- /resetblocklistreason: Reset the default blocklist reason to default - nothing.\n\n"
"Top tip:\n"
"Blocklists allow you to use some modifiers to match 'unknown' characters. For example, you can use the ? character to match a single occurrence of any non-whitespace character.\n"
"You could also use the * modifier, which matches any number of any character. If you want to blocklist URLs, this will allow you to match the full thing. It matches every character except spaces. This is cool if you want to block, for example, URL shorteners.",
buttons=[
[Button.inline("Blocklist Command Examples", b"blocklist_examples")],
[Button.inline("Back", b"help_back")]
]
)

@client.on(events.CallbackQuery(data=b'blocklist_examples'))
async def blocklist_examples(event):
await event.answer("Sending blocklist command examples...", alert=True)
await event.edit(
"Blocklist Command Examples\n\n"
"If you're still curious as to how blocklists work, here are some examples you can copy.\n\n"
"Example blocklist commands:\n"
"- Automatically warn users who say blocklisted words:\n"
"  -> /blocklistmode warn\n\n"
"- Override the blocklist mode for a single filter. Users that say 'boo' will get muted for 6 hours, instead of the blocklist action:\n"

"  -> /addblocklist boo Don't scare the ghosts! {tmute 6h}\n\n"
"- Add a full sentence to the blocklist. This would delete any message containing 'the admins suck':\n"
"  -> /addblocklist \"the admins suck\" Respect your admins!\n\n"
"- Add multiple blocklist entries at once by separating wrapping in brackets, and separating with commas:\n"
"  -> /addblocklist (hi, hey, hello) Stop saying hello!\n\n"
"- Stop any bit.ly links using the * shortcut to match any character:\n"
"  -> /addblocklist \"bit.ly/*\" We dont like shorteners!\n\n"
"- Stop any bit.ly links followed by exactly three characters, to catch bit.ly/hey, but not bit.ly/abcd:\n"
"  -> /addblocklist \"bit.ly/???\" We dont like 3 letter shorteners!\n\n"
"- Stop people sending zip files, by blocklisting file:*.zip:\n"
"  -> /addblocklist \"file:*.zip\" zip files are not allowed here.\n\n"
"- Stop people using the @gif inline bot by adding inline:@gif:\n"
"  -> /addblocklist \"inline:@gif\" The gif bot is not allowed here.\n\n"
"- Stop people forwarding from a channel by adding forward:@channelusername:\n"
"  -> /addblocklist \"forward:@botnews\" The bot news channel is not allowed here.\n\n"
"- Stop any 🖕 emoji, or any stickers related to it:\n"
"  -> /addblocklist 🖕 This emoji is not allowed here.\n\n"
"- To blocklist a stickerpack, simply reply to a sticker with your addblocklist command:\n"
"  -> (replying to a sticker) /addblocklist\n\n"
"- To stop a single blocklist item from deleting messages:\n"
"  -> /addblocklist test {nodel} {warn} No talking about tests here, don't do it again!\n\n"
"- If you've disabled blocklist deletion, but you want to configure some items to still delete:\n"
"  -> /addblocklist boop {del} {ban} No b words here!", buttons=[[Button.inline("Back", b"help_back")]] )

@client.on(events.CallbackQuery(data=b'captcha_info'))
async def captcha_info(event):
await event.answer("Sending CAPTCHA information...", alert=True)
await event.edit(
"CAPTCHA\n\n"
"Some chats get a lot of users joining just to spam. This could be because they're trolls, or part of a spam network.\n"
"To slow them down, you could try enabling CAPTCHAs. New users joining your chat will be required to complete a test to confirm that they're real people.\n\n"
"Admin commands:\n"
"- /captcha <yes/no/on/off>: All users that join will need to solve a CAPTCHA. This proves they aren't a bot! If you use join requests, the CAPTCHA will be sent in PM.\n"
"- /captchamode <button/math/text/text2>: Choose which CAPTCHA type to use for your chat.\n"
"- /captcharules <yes/no/on/off>: Require new users accept the rules before being able to speak in the chat.\n"
"- /captchatime <Xw/d/h/m>: Unmute new users after X time. If a user hasn't solved the CAPTCHA yet, they get automatically unmuted after this period.\n"
"- /captchakick <yes/no/on/off>: Kick users that haven't solved the CAPTCHA. In the case of JoinRequests, users will be dismissed.\n"
"- /captchakicktime <Xw/d/h/m>: Set the time after which to kick CAPTCHA'd users.\n"
"- /setcaptchatext <text>: Customise the CAPTCHA button.\n"
"- /resetcaptchatext: Reset the CAPTCHA button to the default text.\n\n"

"Examples:\n"
"- Enable CAPTCHAs\n"
"  -> /captcha on\n\n"
"- Change the CAPTCHA mode to text.\n"
"  -> /captchamode text\n\n"
"- Enable CAPTCHA rules, forcing users to read the rules before being allowed to speak.\n"
"  -> /captcharules on\n\n"
"- Disable captcha time; users will stay muted until they solve the captcha.\n"
"  -> /captchatime off\n\n"
"NOTE:\n"
"For CAPTCHAs to be enabled, you MUST have enabled welcome messages. If you disable welcome messages, CAPTCHAs will also stop.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'clean_commands_info'))
async def clean_commands_info(event):
await event.answer("Sending Clean Commands information...", alert=True)
await event.edit(
"Clean Commands\n\n"
"Keep your chat clean by cleaning up commands from both users and admins!\n"
"This module allows you to delete certain command categories, for both users and admins, to ensure your chat is kept clean.\n"
"For example, you might choose to delete all user commands; this will stop users from accidentally pressing on blue-text commands in other people's messages.\n\n"
"Available options are:\n"
"- all: Delete ALL commands sent to the group.\n"
"- admin: Delete any admin-only commands sent to the group (e.g., /ban, /mute, or any settings changes).\n"
"- user: Delete any user commands sent to the group (e.g., /id, /info, or /get). These commands will also be cleaned when admins use them.\n"
"- other: Delete any commands which aren't recognized as being valid Rose commands.\n\n"
"Admin commands:\n"
"- /cleancommand <type>: Select which command types to delete.\n"
"- /keepcommand <type>: Select which command types to stop deleting.\n"
"- /cleancommandtypes: List the different command types which can be cleaned.\n\n"
"Examples:\n"
"- Delete all commands, but still respond to them:\n"
"  -> /cleancommand all\n\n"
"- Delete all user commands (but still respond), as well as commands for other bots:\n"
"  -> /cleancommand user other\n\n"
"- Stop deleting all commands:\n"
"  -> /keepcommand all\n\n"
"Note:\n"
"If you are looking to stop your users from using any commands altogether, and don't want Rose to reply to them, have a look at the locks module instead. You may also want to set up log channels, to track the settings changes that your admins are making!",
buttons=[
[Button.inline("Locks", b"locks_info"), Button.inline("Log Channels", b"log_channels_info")],
[Button.inline("Back", b"help_back")]
]
)

@client.on(events.CallbackQuery(data=b'locks_info'))
async def locks_info(event):
await event.answer("Sending Locks information...", alert=True)
await event.edit(
"Locks\n\n"
"Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!\n"
"The locks module allows you to lock away some common items in the Telegram world; the bot will automatically delete them!\n\n"
"Admin commands:\n"
"- /lock <item(s)>: Lock one or more items. Now, only admins can use this type!\n"
"- /unlock <item(s)>: Unlock one or more items. Everyone can use this type again!\n"
"- /locks: List currently locked items.\n"
"- /lockwarns <yes/no/on/off>: Enabled or disable whether a user should be warned when using a locked item.\n"
"- /locktypes: Show the list of all lockable items.\n"
"- /allowlist <url/id/command/@username(s)>: Allowlist a URL, group ID, channel @, bot @, command, or stickerpack link to stop them being deleted by URL, forward, invitelink, inline, command, externalreply, anonchannel, and sticker locks. Separate these with a space to add multiple items at once. If no arguments are given, returns the current allowlist.\n"
"- /rmallowlist <url/id/@channelname(s)>: Remove an item from the allowlist - url, invitelink, and forward locking will now take effect on messages containing it again. Separate with a space to remove multiple items.\n"
"- /rmallowlistall: Remove all allowlisted items.\n\n",
buttons=[
[Button.inline("Example Commands", b"locks_examples"), Button.inline("Lock Descriptions", b"locks_descriptions")],
[Button.inline("Back", b"help_back")]
]
)

@client.on(events.CallbackQuery(data=b'locks_examples'))
async def locks_examples(event):
await event.answer("Sending Locks Examples...", alert=True)
await event.edit(
"Example Commands\n\n"
"Locks are a powerful tool, with lots of different options. So here are a few examples to get you started and familiar on how exactly to use them.\n\n"
"Examples:\n"
"- Stop all users from sending stickers with:\n"
"  -> /lock sticker\n\n"
"- You can lock/unlock multiple items by chaining them:\n"
"  -> /lock sticker photo gif video\n\n"
"- Want a harsher punishment for certain actions? Set a custom lock action for it! You must separate the types from your reason with ###:\n"
"  -> /lock invitelink ### no promoting other chats {ban}\n\n"
"- Reset the custom lock action and reason for a single item:\n"
"  -> /lock emoji ###\n\n"
"- Reset all custom lock actions and reasons; remember to unlock again after:\n"
"  -> /lock all ###\n\n"
"- List all locks at once:\n"
"  -> /locks list\n\n"
"- To allow forwards from a specific channel, eg @RoseSupport, you can allowlist it. You can also use the ID, or invitelink:\n"
"  -> /allowlist @RoseSupport",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'locks_descriptions'))
async def locks_descriptions(event):
await event.answer("Sending Lock Descriptions...", alert=True)
await event.edit(
"Lock Descriptions\n\n"
"There are lots of different locks, and some of them might not be super clear; this section aims to explain each kind of lock.\n\n"
"Types:\n"
"- all: All messages.\n"
"- album: Photos or documents sent as albums.\n"
"- anonchannel: Messages sent through anonymous channels.\n"
"- audio: Audio media messages.\n"
"- bot: Anyone adding bots. Note: bots (like Rose) cannot see other bots.\n"
"- button: Messages which contain buttons.\n"
"- command: Messages which start with a Telegram command (e.g., /start).\n"
"- comment: Messages sent by users that are commenting in the linked channel, yet aren't members of the group.\n"
"- contact: Contact media messages.\n"
"- document: Document media messages. This includes photos/videos sent uncompressed.\n"
"- email: Messages which contain emails (as defined by Telegram).\n"
"- emoji: Messages containing any kind of emoji.\n"
"- emojicustom: Messages containing custom Telegram emoji.\n"
"- emojigame: Telegram mini games like dice, bowling, or darts.\n"
"- emojionly: Messages which contain only emoji, and no other text.\n"
"- externalreply: Replies to messages from other chats.\n"
"- forward: Forwarded messages.\n"
"- forwardbot: Messages where the original sender is a bot.\n"
"- forwardchannel: Messages where the original sender is a channel.\n"
"- forwarduser: Messages where the original sender is a user.\n"
"- game: Bot API game messages.\n"
"- gif: GIF media messages.\n"
"- inline: Messages sent through inline bots, like @gif or @pic.\n"
"- invitelink: Messages containing private and public links to groups or channels.\n"
"- location: Location messages.\n"
"- phone: Messages which contain phone numbers (as defined by Telegram).\n"
"- photo: Messages containing a photo.\n"
"- poll: Poll messages.\n"
"- rtl: Messages which contain right-to-left characters. E.g., Arabic, Farsi, Hebrew, etc.\n"
"- spoiler: Messages containing Telegram spoiler entities.\n"
"- sticker: All sticker types.\n" "- stickeranimated: Animated stickers (including premium).\n"
"- stickerpremium: Premium stickers.\n"
"- story: Messages containing user stories.\n"
"- text: Messages which contain text, including media captions.\n"
"- url: Messages which contain website links (as defined by Telegram).\n"
"- video: Video media messages.\n"
"- videonote: Videonote media messages.\n"
"- voice: Voice messages.",
buttons=[[Button.inline("Back", b"help_back")]] )

@client.on(events.CallbackQuery(data=b'log_channels_info'))
async def log_channels_info(event):
await event.answer("Sending Log Channels information...", alert=True)
await event.edit(
"Log Channels\n\n"
"Recent actions are nice, but they don't help you log every action taken by the bot. This is why you need log channels!\n"
"Log channels can help you keep track of exactly what the other admins are doing. Bans, Mutes, warns, notes - everything can be moderated.\n\n"
"Setting a log channel is done by the following steps:\n"
" - Add Rose to your channel, as an admin. This is done via the \"add administrators\" tab.\n"
" - Send /setlog to your channel.\n"
" - Forward the /setlog command to the group you wish to be logged.\n"
" - Congrats! all done :)\n\n"
"Admin commands:\n"
"- /logchannel: Get the name of the current log channel.\n"
"- /setlog: Set the log channel for the current chat.\n"
"- /unsetlog: Unset the log channel for the current chat.\n"

"- /log <category>: Enable a log category - actions of that type will now be logged.\n"
"- /nolog <category>: Disable a log category - actions of that type will no longer be logged.\n"
"- /logcategories: List all supported categories, with information on what they refer to.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'clean_service_info'))
async def clean_service_info(event):
await event.answer("Sending Clean Service information...", alert=True)
await event.edit(
"**Clean Service**\n\n"
"Cleanup automated Telegram service messages! The available categories are:\n"
"- **all**: All service messages.\n"
"- **join**: When a new user joins, or is added. eg: 'X joined the chat'\n"
"- **leave**: When a user leaves, or is removed. eg: 'X left the chat'\n"
"- **other**: Miscellaneous items; such as chat boosts, successful Telegram payments, proximity alerts, webapp messages, or message auto-deletion changes.\n"
"- **photo**: When chat photos or chat backgrounds are changed.\n"
"- **pin**: When a new message is pinned. eg: 'X pinned a message'\n"
"- **title**: When chat or topic titles are changed.\n"
"- **videochat**: When a video chat action occurs - eg starting, ending, scheduling, or adding members to the call.\n\n"
"**Admin commands:**\n"
"- `/cleanservice <type/yes/no/on/off>`: Select which service messages to delete.\n"
"- `/keepservice <type>`: Select which service messages to stop deleting.\n"
"- `/nocleanservice <type>`: (same as `/keepservice`)\n"
"- `/cleanservicetypes`: List all the available service messages, with a brief explanation.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'connections_info'))
async def connections_info(event):
await event.answer("Sending Connections information...", alert=True)
await event.edit(
"**Connections**\n\n"
"Sometimes, you just want to add some notes and filters to a group chat, but you don't want everyone to see; This is where connections come in...\n\n"
"This allows you to connect to a chat's database and add things to it without the chat knowing about it! For obvious reasons, you need to be an admin to add things; but any member can view your data. (banned/kicked users can't!)\n\n"
"**Admin commands:**\n"
"- `/connect <chatid/username>`: Connect to the specified chat, allowing you to view/edit contents.\n"
"- `/disconnect`: Disconnect from the current chat.\n"
"- `/reconnect`: Reconnect to the previously connected chat.\n"
"- `/connection`: See information about the currently connected chat.\n\n"
"You can retrieve the chat id by using the `/id` command in your chat. Don't be surprised if the id is negative; all supergroups have negative ids.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'disabling_info'))
async def disabling_info(event):
await event.answer("Sending Disabling information...", alert=True)
await event.edit(
"**Disabling**\n\n"
"Not everyone wants every feature that Rose offers. Some commands are best left unused; to avoid spam and abuse.\n\n"
"This allows you to disable some commonly used commands, so no one can use them. It'll also allow you to autodelete them, stopping people from bluetexting.\n\n"
"**Admin commands:**\n"
"- `/disable <commandname>`: Stop users from using `commandname` in this group.\n"
"- `/enable <commandname>`: Allow users to use `commandname` in this group.\n"
"- `/disableable`: List all disableable commands.\n"
"- `/disabledel <yes/no/on/off>`: Delete disabled commands when used by non-admins.\n"
"- `/disableadmin <yes/no/on/off>`: Stop admins from using disabled commands too.\n"
"- `/disabled`: List the disabled commands in this chat.\n\n"
"**Examples:**\n"
"- Stop people from using the info command:\n"
"  `/disable info`\n"
"- Enable the info command (e.g., undo a disable):\n"
"  `/enable info`\n"
"- Disable all commands listed in the `/disableable`:\n"
"  `/disable all`\n"
"- Delete disabled commands that get used:\n"
"  `/disabledel on`\n"
"- Make sure that disabled commands are also disabled for admins:\n"
"  `/disableadmin on`\n\n"
"**Note:**\n"
"By default, disabling a command only disables it for non-admins. To stop admins from using disabled commands too, check the `/disableadmin` toggle.\n"
"Disabled commands are still accessible through the `/connect` feature.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'federations_info'))
async def federations_info(event):
await event.answer("Sending Federations information...", alert=True)
await event.edit(
"**Federations**\n\n"
"Ah, group management. It's all fun and games, until you start getting spammers in, and you need to ban them. Then you need to start banning more, and more, and it gets painful.\n"
"But then you have multiple groups, and you don't want these spammers in any of your groups - how can you deal? Do you have to ban them manually, in all your groups?\n\n"
"No more! With federations, you can make a ban in one chat overlap to all your other chats.\n"
"You can even appoint federation admins, so that your trustworthiest admins can ban across all the chats that you want to protect.\n\n"
"Choose an option below:",
buttons=[
[Button.inline("Fed Admin Commands", b"fed_admin_commands"), Button.inline("Federation Owner Commands", b"fed_owner_commands")],
[Button.inline("User Commands", b"user_commands")],
[Button.inline("Back", b"help_back")]
]
)

@client.on(events.CallbackQuery(data=b'fed_admin_commands'))
async def fed_admin_commands(event):
await event.answer("Sending Fed Admin Commands information...", alert=True)
await event.edit(
"**Fed Admin Commands**\n\n"
"The following is the list of all fed admin commands. To run these, you have to be a federation admin in the current federation.\n\n"
"**Commands:**\n"
"- `/fban`: Bans a user from the current chat's federation\n"
"- `/unfban`: Unbans a user from the current chat's federation\n"
"- `/feddemoteme <fedID>`: Demote yourself from a fed.\n"
"- `/myfeds`: List all feds you are an admin in.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'fed_owner_commands'))
async def fed_owner_commands(event):
await event.answer("Sending Fed Owner Commands information...", alert=True)
await event.edit(
"**Federation Owner Commands**\n\n"
"These are the list of available fed owner commands. To run these, you have to own the current federation.\n\n"
"**Owner Commands:**\n"
"- `/newfed <fedname>`: Creates a new federation with the given name. Only one federation per user.\n"
"- `/renamefed <fedname>`: Rename your federation.\n"
"- `/delfed`: Deletes your federation, and any information related to it. Will not unban any banned users.\n"
"- `/fedtransfer <reply/username/mention/userid>`: Transfer your federation to another user.\n"
"- `/fedpromote`: Promote a user to fedadmin in your fed. To avoid unwanted fedadmin, the user will get a message to confirm this.\n"
"- `/feddemote`: Demote a federation admin in your fed.\n"
"- `/fednotif <yes/no/on/off>`: Whether or not to receive PM notifications of every fed action.\n"
"- `/fedreason <yes/no/on/off>`: Whether or not fedbans should require a reason.\n"
"- `/subfed <FedId>`: Subscribe your federation to another. Users banned in the subscribed fed will also be banned in this one.\n"
"- `/unsubfed <FedId>`: Unsubscribes your federation from another. Bans from the other fed will no longer take effect.\n"
"- `/fedexport <csv/minicsv/json/human>`: Get the list of currently banned users. Default output is CSV.\n"
"- `/fedimport <overwrite/keep> <csv/minicsv/json/human>`: Import a list of banned users.\n"
"- `/setfedlog`: Sets the current chat as the federation log. All federation events will be logged here.\n"
"- `/unsetfedlog`: Unset the federation log. Events will no longer be logged.\n"
"- `/setfedlang`: Change the language of the federation log. Note: This does not change the language of Rose's replies to fed commands, only the log channel.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'user_commands'))
async def user_commands(event):
await event.answer("Sending User Commands information...", alert=True)
await event.edit(
"**User Commands**\n\n"
"These commands do not require you to be admin of a federation. These commands are for general commands, such as looking up information on a fed, or checking a user's fbans.\n\n"
"**Commands:**\n"
"- `/fedinfo <FedID>`: Information about a federation.\n"
"- `/fedadmins <FedID>`: List the admins in a federation.\n"
"- `/fedsubs <FedID>`: List all federations your federation is subscribed to.\n"
"- `/joinfed <FedID>`: Join the current chat to a federation. A chat can only join one federation. Chat owners only.\n"
"- `/leavefed`: Leave the current federation. Only chat owners can do this.\n"
"- `/fedstat`: List all the federations that you have been banned in.\n"
"- `/fedstat <user ID>`: List all the federations that a user has been banned in.\n"
"- `/fedstat <FedID>`: Gives information about your ban in a federation.\n"
"- `/fedstat <user ID> <FedID>`: Gives information about a user's ban in a federation.\n"
"- `/chatfed`: Information about the federation the current chat is in.\n"
"- `/quietfed <yes/no/on/off>`: Whether or not to send ban notifications when fedbanned users join the chat.",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'filters_info'))
async def filters_info(event):
await event.answer("Sending Filters information...", alert=True)
await event.edit(
"**Filters**\n\n"
"Make your chat more lively with filters; The bot will reply to certain words!\n"
"Filters are case insensitive; every time someone says your trigger words, Rose will reply with something else! Filters can also be used to create your own commands, if desired.\n\n"
"**Commands:**\n"
"- `/filter <trigger> <reply>`: Every time someone says \"trigger\", the bot will reply with \"reply\". For multiple word filters, quote the trigger.\n"
"- `/filters`: List all chat filters.\n"
"- `/stop <trigger>`: Stop the bot from replying to \"trigger\".\n"
"- `/stopall`: Stop ALL filters in the current chat. This cannot be undone.\n\n"
"Choose an option below:",
buttons=[
[Button.inline("Example Usage", b"filters_example_usage"), Button.inline("Formatting", b"filters_formatting")],
[Button.inline("Back", b"help_back")]
]
)

@client.on(events.CallbackQuery(data=b'filters_example_usage'))
async def filters_example_usage(event):
await event.answer("Sending Example Usage information...", alert=True)
await event.edit(
"**Example Usage**\n\n"
"Filters can seem quite complicated; so here are some examples, so you can get some inspiration.\n\n"
"**Examples:**\n"
"- Set a filter:\n-> /filter hello Hello there! How are you?\n\n"
"- Set a filter which uses the user's name through fillings:\n-> /filter hello Hello there {first}! How are you?\n\n"
"- Set a filter on a sentence:\n-> /filter \"hello friend\" Hello back! Long time no see!\n\n"
"- Set multiple filters at once by separating wrapping in brackets, and separating with commas:\n-> /filter (hi, hey, hello, \"hi there\") Hello back! Long time no see!\n\n"
"- Set a filter that can only be used by admins:\n-> /filter \"trigger\" This filter wont happen if a normal user says it {admin}\n\n"
"- Or, set a filter that can only be used by users:\n-> /filter \"trigger\" Admins won't trigger this {user}\n\n"
"- If an admin wants to force a {user} filter to reply:\n-> trigger force\n\n"
"- To get the unformatted version of a filter, to copy and edit it, simply say the trigger followed by the keyword \"noformat\":\n-> trigger noformat\n\n"
"- To save a \"protected\" filter, which cant be forwarded:\n-> /filter \"example\" This filter cant be forwarded {protect}\n\n"
"- If you want the filter to reply to the person you replied to, instead of you:\n-> /filter \"magic\" Watch out for wizards! {replytag}\n\n"
"- To save a file, image, gif, or any other attachment, simply reply to file with:\n-> /filter trigger\n\n"
"- To set a filter which replies with a random answer from a preset list:\n-> /filter test\nAnswer one\n%%%\nAnswer two\n\n"
"- To set a filter which gives a different reply to admins users, you can mix permission fillings with random contents:\n-> /filter test\nOnly admins see this {admin}\n%%%\nOnly users see this {user}",
buttons=[
[Button.inline("Fillings", b"filters_fillings")],
[Button.inline("Back", b"help_back")]
]
)

@client.on(events.CallbackQuery(data=b'filters_fillings'))
async def filters_fillings(event):
await event.answer("Sending Fillings information...", alert=True)
await event.edit(
"**Fillings**\n\n"
"You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the welcome message, or mention them in a filter!\n\n"
"**Supported fillings:**\n"
"- `{first}`: The user's first name.\n"
"- `{last}`: The user's last name.\n"
"- `{fullname}`: The user's full name.\n"
"- `{username}`: The user's username. If they don't have one, mentions the user instead.\n"
"- `{mention}`: Mentions the user with their firstname.\n"
"- `{id}`: The user's ID.\n"
"- `{chatname}`: The chat's name.\n"
"- `{rules}`: Create a button to the chat's rules.\n"
"- `{preview}`: Enables link previews for this message. Useful when using links to Instant View pages.\n"
"- `{preview:top}`: Shows the link preview for this message ABOVE the message text.\n"
"- `{nonotif}`: Disables the notification for this message.\n"
"- `{protect}`: Stop this message from being forwarded, or screenshotted.\n"
"- `{mediaspoiler}`: Marks the message photo/video/animation as being a spoiler.\n\n"
"**Example usages:**\n"
"- Save a filter using the user's name:\n-> /filter test {first} triggered this filter.\n\n"
"- Add a rules button to a note:\n-> /save info Press the button to read the chat rules! {rules}\n\n"
"- Mention a user in the welcome message:\n-> /setwelcome Welcome {mention} to {chatname}!",
buttons=[[Button.inline("Back", b"help_back")]]
)

@client.on(events.CallbackQuery(data=b'filters_formatting'))
async def filters_formatting(event)
await event.answer("Sending Formatting information...", alert=True)
await event.edit(
"**Formatting**\n\n"
"Rose supports a large number of formatting options to make your messages more expressive. Take a look!",
buttons=[
[Button.inline("Markdown Formatting", b"formatting_markdown"), Button.inline("Fillings", b"filters_fillings")],
[Button.inline("Random Content", b"formatting_random_content"), Button.inline("Buttons", b"formatting_buttons")],
[Button.inline("Back", b"help_back")]
]
)


@client.on(events.CallbackQuery(data=b'help_back'))
async def help_back(event):
await help(event)
