import os
import sys
import discord
import re, json
import html
import datetime

from discord.ext import commands
from bs4 import BeautifulSoup
from urlbreak import get_item, skill_info
import urllib.request
import urllib.parse
from urllib.parse import urlencode
from paginator import Pages

###-- Invitation Link --###
#https://discordapp.com/api/oauth2/authorize?client_id=441691408630546443&scope=bot&permissions=0

bot = commands.Bot(command_prefix='!popo ', description='just another popolion bot', pm_help = True)

bot.remove_command("help")


VERSION='0.0.1'
CHANGELOG="""
```md
[Changelog](version: 0.0.1)
```
```md
# Change:
* Fix:
    - Birth of Popo
```
"""

db = {'servers': {}}

def get_first_text_channel(server):
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            return channel
    return None


###-- prep --###
@bot.event
async def on_ready():
    # global db

    # __location__ = os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # if os.path.isfile(os.path.join(__location__, 'db.json')):
    #     with open(os.path.join(__location__, 'db.json')) as f:
    #         db = json.loads(f.read())

    # for server in bot.servers:
    #     if server.id not in db['servers'].keys() or (server.id in db['servers'].keys() and db['servers'][server.id] != VERSION):
    #         # channel = get_first_text_channel(server)

    #         # if channel is not None:
    #         #     await bot.send_message(channel, CHANGELOG)

    #         for channel in server.channels:
    #             if channel.type == discord.ChannelType.text:
    #                 try:
    #                     await bot.send_message(channel, CHANGELOG)
    #                     break
    #                 except discord.errors.Forbidden:
    #                     continue
    #                     break

    #         db['servers'][server.id] = VERSION

    # with open(os.path.join(__location__, 'db.json'), 'w') as f:
    #     json.dump(db, f, indent=4)

	activity = discord.Game(name="!popo help")
	await client.change_presence(status=discord.Status("online"), activity=activity)


    print('========================================')
    print('            Are you ready popo?!        ')
    print('----------------------------------------')
    print('----------------------------------------')
    print("smmmmmmmmmmmmoddyssydhyddddmddmmmmmmmmms")
    print("smmmmmmmsdmddhd++++/+hh+//+ydmmmmmmmmmms")
    print("smmmmmmdsho//+yy++osoyo++ooohddmmmmmmmms")
    print("smmmmmmmms+s+:oyo/-...-:+s.-y//smmmmmmms")
    print("smmmmmmmmhsso+/````````...+ss++/ymmmmmms")
    print("smmmmmds//+sy.syh:`:+..dyy.+s++sdmmmmmms")
    print("smmmmmy++++s/`o+++.+h:o/+o.`sso+odmmmmms")
    print("smmmmmdssssh......:ss/``...`oso+/ymmmmms")
    print("smmmmmmd+/+y/..````.:.````.:hsoosdhhhhms")
    print("smmmmmmd++++so/-........-/os++sdmmmmmmms")
    print("smmmmmmmdysysoosooo+/++oys+++++dmmmmmmms")
    print("smmmmmmmmmmd+++++sy++++++dsssydhhhhhhhho")
    print("smmmmmmmmmmmdhyyy+ssoooss/.../mmmmmmmmms")
    print("smmmmmmmmmmmmmmmd-.-:::.:-:-`ymmmmmmmmms")
    print("smmmmmmmmmmmmddddy:mdmd-yhhyoddddddddddo")
    print("+yyyyyyyyyyyyyyyyyyyyyyyy:/yyoooooooooo/")
    print('----------------------------------------')
    print('----------------------------------------')


###-- on server join --###
@bot.event
async def on_server_join(server):

    ##-- send msg to the server owner --##
    owner = server.owner

    welcome = """
_`Hello there!`_

Nice to meet you, I am popo!!
I'm a simple Tree of Savior Discord bot that can help you and your community find and gather information regarding ToS.

Here, I am request permission to stay in your server.
- popo
    """
    await bot.send_message(owner, welcome)

    ##-- send msg to the 1st text channel on the server --##
    chch = server.channels

    spawn = """
```css
"When you meet someone for the first time, that's not the whole book. That's just the first page."
```
Gao! I'm **popo!**

I am a simple bot that aims to help Tree of Savior players find information related to ToS.
Use `!popo help` to find out more commands.
Alright Boys, popo at your service!! :sunglasses:
================================================================
    """
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            try:
                await bot.send_message(channel, spawn)
                break
            except discord.errors.Forbidden:
                continue
                break


###-- help --###
@bot.command(pass_context=True, aliases=['halp'])
async def help(ctx):

    halpme = """

**[popo Help]**
```md
<prefix : !popo>
<format : prefix command>
    e.g : !popo<space>commands
```
**[List of commands:]**
```md
# help /halp:
  this message

# hello:
  greets the bot

# news:
  get latest news/updates from Tree of Savior official website

# ping:
  ping the bot

# ktest:
  get link for ktest version of tos.neet

# update / updates:
  get link for latest datamined file(s)

# planner:
  get link for class/build planner

# inv / invite:
  get my invitation link

# lv / leveling:
  get link for leveling guide (reddit)

# rank:
  get class build rankings (based on itos official website)

# explo:
  get link for explorer's gimmick & new collections guide (made by TerminalEssence and friends)

# get / item:
  - get item info
  command: get "item name"
  < e.g. : !popo get solmiki >
  /* important: now you can search any item(s) information *

# skill:
  - get skill info
  command: skill "class name"
  < e.g. : !popo skill diev >
  /* you may use class name abbreviation/alias (e.g. sr, pd, diev etc.) *
```
    """

    await bot.whisper(halpme)
    # await bot.send_message(ctx.message.author, halpme)
    # await bot.send_message(ctx.message.author, content=halpme)


###-- hello --###
@bot.command(pass_context=True)
async def hello():
    me = """
Hello, I am **Popolion**

I'm a simple discord bot born to help Tree of Savior's Discord community members find info about items, skills, ~~maps~~ and etc.
I am created by the desire of my creator to obtain basic information regarding ToS items or skills without having to open the browser.
"""
    await bot.say(me)

###-- who --###
@bot.command()
async def who():
    await bot.say("Full-fledged Hero!!")

###-- ping --###
@bot.command()
async def ping(*args):
    await bot.say(":ping_pong: Pong!")

###-- die --###
@bot.command(hidden=True, no_pm=True)
async def die():
    sys.exit(0)

###-- ktest --###
@bot.command()
async def ktest():
    await bot.say("**[Let's see the future!!]**\n" + "https://tos-ktest.neet.tv/")

###-- update --###
@bot.command(aliases=['updates'])
async def update():
    await bot.say("**[Check what is new!!]**\n" + "https://tos.neet.tv/changes")

###-- planner --###
@bot.command()
async def planner():
    await bot.say("**[Plan your character build!!]**\n" + "https://tos.neet.tv/skill-planner")

###-- gimmick --###
@bot.command()
async def explo():
     await bot.say("**[Explorer's Gimmick & New Collections Guide]**\n[*credits : TerminalEssence & Friends*]\n\n" + "https://docs.google.com/document/d/1ihOzgxe8SrV8aRwYq1xMUwiTvsTNHGibJ6yBXFATaTg/edit?usp=sharing")

###-- leveling --###
# @bot.command(aliases=['leveling'])
# async def lv():
#     await bot.say("**[Leveling Guide]**\n[based on shion@inven.co.kr]\n\n" + "https://www.reddit.com/r/treeofsavior/comments/8bg0mb/updated_levelling_guide/")

##-- leveling (2) --###
@bot.command(pass_context=True, aliases=['leveling'])
async def lv(ctx):
    pages = [
"***Lvl 1 ~ 50:***\n\nStart off by going straight to Klaipeda town and speaking with the event notice board to pick up your new/returning player bonus package. Then return and complete all the main(yellow/gold) quests from **West Siauliai Woods** all the way to **East Siauliai Woods**. You can then complete the main quest chains from **Miner's Village > Crystal Mines > Strautas Gorge > Gele Plateau > Nefritas Cliff > Tenet Garden**. Once you have enough silver to get Blessing and Sacrament buffs from pardoners in Klaipeda town(usually about 1600 silver is enough), you will want to get the buffs whenever you want to level. Make sure you refresh your buffs if they run out by purchasing them again in town. Once you arrive at Tenet Garden you can kill the mobs above the goddess statue there, they are plentiful and have fast respawn times. You will also need to go inside Tenet Church B1 and complete the entire main questline there until Tenet Church 2f in order to acquire the Seal of Space quest item. As a side note; when you reach lvl 40, go to the **Wings of Vivora** NPC in Klaipeda Town to receive the Kedora Merchant Alliance Support Selection Boxes. These Gear boxes contain lvl 40 gear for you to use until a higher level.",
"***Lvl 50 ~ 100:***\n\nOnce you are lvl 50, you will be able to attempt the lvl 50 leveling dungeon in Klaipeda town, be sure to use your megaphones brought from the TP store using free daily tp to shout for people to queue up for it or join a guild so that it is easier to find parties. You can also solo the dungeon by making an empty party and selecting the enter now option at the dungeon npc. After you complete your lvl 50 dungeon runs up to the daily limit cap, proceed to complete the main quest chain at **Veja Ravine, Vieta Gorge, Cobalt Forest, Septyini Glen**. At the end of the Septyini Glen quest chain, Goddess Saule will warp you to Rukas Plateau. You can speak with **Historian Rexipher** there to start another main quest chain to do, which will take you all the way to King's Plateau, Zachariel Crossroads and Royal Mausoleum 1f - 5f. Similar to the previous level bracket; when you reach lvl 75, go to the **Wings of Vivora** NPC in Klaipeda Town to receive the Kedora Merchant Alliance Support Selection Boxes.",
"***Lvl 100 ~ 220:***\n\nGo to **Fedimian** and pick up the Goddess Gabija questline which takes you to Fedimian Suburbs. Following the quest line will bring you to Mage Tower1f-5f in which you will want to finish the main quest chain there. If you are under level 121 at this point, then feel free to go to **Main Building** and finish the main quest chains there leading to Sanctuary, or you can do the lvl 120 leveling dungeon in towns if the day has reset. At level 121+, you can make your way to **Aqueduct Bridge Area** and start the main quest chain there. It will bring you into the Demon Prison maps in which you can follow the entire questchain until Demon Prison District 5. Once you have done so, you may choose to return to Demon Prison District 2 and kill the mobs there if you wish, since they are plentiful and respawn quickly. You will also want to try the Challenge Mode feature(lvl 100+) around maps of your level. After you are finished with the Demon Prison maps, go to Dina Bee Farm and follow the main quest chain starting there until its completion at Spring Light Woods. You should be aiming to be lvl 171+ at this point, if you need additional levels, remember to 100% explore the previous maps for exp cards redeemed at the **Wings of Vivora** NPC. When you are lvl 171+, go to Inner Enceinte Dristrict and start main quest line there from **Amanda Grave Robbers** Amanda. This quest chain will lead you all the way to Fortress Battlegrounds and you should be at least lvl 220+ at the end of it. As usual, remember to pick up the Kedora Merchant Alliance Support Selection Boxes for level 120 and 170 gear after reaching those levels.",
"***Lvl 220 ~ 310:***\n\nGo to **Elgos Monastery Annex** and complete the main quest chain there that leads you to Elgos Monastery Main Building. After completing those two maps, go to **Kalejimas Visiting Room** and start to complete the main quests in that area. You can actually follow the entire quest route from **Kalejimas Visiting Room > Storage > Solitary Cells > Workshop > Investigation Room**, killing all the monsters you encounter on the way. Remember to keep up with your daily dungeon runs of the appropriate level(lvl 200 and 270) and Challenge mode entries. After you finish with the Kalejimas full quest line, you should be around level 260+ if you have used your EXP cards along with the Episode rewards. Make your way to **Khonot Forest** and find Kupole Medena in order to start a main quest chain. This quest chain will bring you from Stalcite Tehvrin Cave 1f all the way to Stalcite Tehvrin Cave 5f. At the end of this tedious quest chain, you should be at lvl 310+.",
"***Lvl 310 ~ 350:***\n\nStart off with speaking to **Neringa** at **Nobeer Forest** to initiate a main quest chain. It will lead you to **Sausis Room 9** and continues onwards to conclude at Valandis Room 91. This quest chain should complete Episode 9 for you and you should be level 350+ at the end of it. Remember to pick up your new Kedora boxes for levels 315 and 350 when you can.",
"***Lvl Lvl 350 ~ 390:***\n\nMove to **Barynwell 85 Waters** and complete the main quests there. This will initiate a main quest chain that brings you to **Barynwell 86 Waters, Barynwell 87 Waters, Astral Tower 1F, Astral Tower 4F, Astral Tower 12F, Astral Tower 20F and Astral Tower 21F**. Finish up those maps and then go and do the main quests at **Outer Wall District 11, Inner Wall District 10, Outer Wall District 13, Outer Wall District 14 and Outer wall District 15**. Once you are done with that, travel to **Fedimian** and speak with **Pajauta** for a main quest chain that ends with providing you lvl 380 Kedora gear and a Pajauta Card. Proceed onwards to **Northern Parias Forest** and speak with **Kupole Astra** to begin a new main quest chain, this one will lead onto **Central Parias Forest** and conclude at **Southern Parias Forest**. At the end of this, you should be lvl 393+. Remember to keep up with your daily challenge modes.",
"***Lvl 390 ~ 450:***\n\nSpeak with **Neringa** at Orsha for a main quest chain that ends with providing you with lvl 400 Kedora gear boxes and a Neringa Card. After completing that quest chain, find **Kupole Maya** in **Frienel Memorial** to begin your Episode 12 quests. It will lead you to **West Jungers Road, Vienibe Shelter, Tvirtumas Fortress, Skalda Outskirts, Rinksmas Ruins** and ends at **Path of Desition**. You will also want to speak with **Receptionist Ramda** in **Klaipeda** town for the repeatable defeat x amount of monster quests for each of the new EP 12 maps. Once you are level 400+, you can also attempt the lvl 400 leveling dungeon in towns. At this point in the game, you should be doing daily dungeons, daily challenge modes, field grinding in EP12 maps or in Outer Wall Sewers to supplement your leveling process until you reach the lvl 450 cap. If you not able to see the quests at some of the EP12 maps, it means your level is too low and you will want to grind exp until you are able to do so. The game provides you with many free exp boosting items, so it is good to take advantage of that when you are grinding or doing challenge modes.",
    ]

    for index, page in enumerate(pages):
        pages[index] = page

    pages = Pages(bot, message=ctx.message, entries=pages, per_page=1, with_number=False)
    await pages.paginate()

###-- invite --###
@bot.command(aliases=['invite'])
async def inv():
    invt = "https://discordapp.com/api/oauth2/authorize?client_id=441691408630546443&scope=bot&permissions=0"
    await bot.say("**[Use this link to invite me to your server.]**\n\n" + invt)

###-- ranking --###
@bot.command(aliases=['rankings'])
async def rank():
    await bot.say("**[The most popular TOS class builds of all time]**\n[Update periodically]\n\n" + "https://treeofsavior.com/page/class/ranking.php")

###-- get / item --###
def get_choice(r):
    return (r.content.isdigit() and int(r.content) >= 1 and int(r.content) <= len(result_search))

@bot.command(pass_context=True, aliases=['item'], no_pm=True)
async def get(ctx, *name):

    await bot.send_typing(ctx.channel)

    # get keyword #
    name = '+'.join(name)

    r = urllib.request.urlopen('https://tos.neet.tv/items?name=' + name + '&f=1').read()
    soup = BeautifulSoup(r, 'html.parser')
    result_table = soup.find('table', {"class": 'results-table'}).find('tbody').find_all('tr')

    item_names = []
    item_types = []
    item_links = []
    result_search = ''
    res_len = len(result_table)
    start = 0
    end = 7

    for no, row in enumerate(result_table[start:end], start=0):
        columns = row.find_all('td')
        item_links.append(columns[1].find('a').get('href'))
        item_names.append(columns[2].string)
        item_types.append(columns[3].string)

        result_search += str(no + 1) + '. ' + columns[2].get_text() + ' - [' + columns[3].get_text() + ']' + '\n'


    # send search result - multiple choice #
    msg = await bot.say(content=ctx.message.author.mention + "\n**Please choose one by giving its number**,\n_type `next` or `>` to display more result._" + "```" + str(result_search) + "```" + "\n")


    # waiting for response from user #
    while True:
        choice = await bot.wait_for_message(timeout=30.0, author=ctx.message.author)

        if choice is None:
            await bot.say('_**too slow...**_   **(╯°□°）╯︵ ┻━┻**')
            break

        elif choice.content == 'next' or choice.content == '>':

                    start += 7
                    end += 7
                    result_search = ""
                    for no, row in enumerate(result_table[start:end], start=start):
                        columns = row.find_all('td')
                        item_links.append(columns[1].find('a').get('href'))
                        item_names.append(columns[2].string)
                        item_types.append(columns[3].string)

                        result_search += str(no + 1) + '. ' + columns[2].get_text() + ' - [' + columns[3].get_text() + ']' + '\n'

                    await bot.delete_message(msg)

                    msg = await bot.say(content=ctx.message.author.mention + "\n**Please choose one by giving its number**,\n_type `next` or `>` to display more result._" + "```" + str(result_search) + "```" + "\n")


    # send search result - embed #
        elif choice.content.isdigit() and int(choice.content) >= 1 and int(choice.content) <= len(result_search):
            choice_number = int(choice.content)
            embed = get_item('https://tos.neet.tv' + item_links[choice_number - 1])

            # await bot.delete_message(choice)
            await bot.delete_message(msg)
            # await bot.delete_message(ctx.message)

            await bot.say(content=ctx.message.author.mention + "\n**This is your search result!**\n_Click the item name to see more info on your browser._", embed=embed)
            break

##-- eol --##


### get skill ###
@bot.command(pass_context=True, no_pm=True)
async def skill(ctx, *job):

    await bot.send_typing(ctx.channel)

    # get keyword #
    __location__ = os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'classes2.json')) as f:
    # with open('classes2.json') as f:
        content = f.read()

    tos_classes2 = json.loads(content)

    for tos_class in tos_classes2:
        tos_class['regex'] = re.compile(tos_class['regex'], re.IGNORECASE)

    response = "\nNot Found\n"

    keyword = ' '.join(job)

    for tos_class in tos_classes2:
        if tos_class['regex'].match(keyword):
            code, name = tos_class['code'], tos_class['name']
            # print('Founded?: ' + name + " :" + code)
            break

    jobs = code

    r = urllib.request.urlopen('https://tos.neet.tv/skills?cls=' + jobs + '&f=1').read()
    soup = BeautifulSoup(r, 'html.parser')
    result_table = soup.find('table', {"class": 'results-table'}).find('tbody').find_all('tr')

    skill_names = []
    skill_types = []
    skill_links = []
    result_search = ''
    skill_res = ''
    res_len = len(result_table)

    for no, row in enumerate(result_table):
        columns = row.find_all('td')
        skill_links.append(columns[1].find('a').get('href'))
        skill_names.append(columns[2].string)
        skill_types.append(columns[3].string)

        result_search += str(no + 1) + '. ' + columns[2].get_text() + ' - [' + columns[3].get_text() + ']' + ' ------ ' + columns[1].find('a').get('href') + '\n'
        skill_res += str(no + 1) + '. ' + columns[2].string + '\n'

    # send search result - multiple choice #
    msg = await bot.say(content=ctx.message.author.mention + "\n**Please choose one by giving its number:**" + "```" + (skill_res) + "```" + "\n")

    # waiting for response from user #
    while True:
        choice = await bot.wait_for_message(timeout=30.0, author=ctx.message.author)

        if choice is None:
            await bot.say('_**too slow...**_   **(╯°□°）╯︵ ┻━┻**')
            break

    # send search result - embed #
        elif choice.content.isdigit() and int(choice.content) >= 1 and int(choice.content) <= len(result_search):
            choice = int(choice.content)
            items = skill_info('https://tos.neet.tv' + skill_links[choice - 1])

            embed = discord.Embed(colour=discord.Colour(0xD2EE8A), description=items['description'], timestamp=datetime.datetime.now())

            # embed.set_image(url="https://tos.neet.tv/images/equip/icon_item_shirts_acolyte_silver.png")
            embed.set_thumbnail(url=items['thumbnail'])

            embed.set_author(name=items['title'], url='https://tos.neet.tv' + skill_links[choice - 1], icon_url="http://bestonlinegamesreview.com/wp-content/uploads/2016/04/p1_2006411_5eae6fd9.png")

            embed.set_footer(text="tos.neet.tv", icon_url="https://tos.neet.tv/images/hairacc/hairacc_80_fez.png")

            sklinfo = '```' + '\n'.join(["{:<15}: {}".format(*item) for item in items['adin'].items()]) + '```'

            embed.add_field(name="Skill Info", value=sklinfo, inline=True)

            if len(items['attribs']) > 0:
                sklatrb = '```' +'\n\n'.join(["{}\n{}".format(*item.values()) for item in items['attribs']]) + '```'
                embed.add_field(name="Attributes", value=sklatrb, inline=False)

            await bot.delete_message(msg)

            await bot.say(content=ctx.message.author.mention + "\n**This is your search result!**\n_Click the skill name to see more info on your browser._", embed=embed)

            break

#####


### get news - official website ###
@bot.command(pass_context=True, no_pm=True)
async def news(ctx):

    await bot.send_typing(ctx.channel)

    r = urllib.request.urlopen('https://treeofsavior.com/page/news/').read()
    soup = BeautifulSoup(r, 'html.parser')
    resnews = soup.find(id= 'news_box_wrap').find_all('div', {"class": 'news_box'}, limit = 7)


    news_list = ""
    for n, news in enumerate(resnews, start=1):
        title = news.find('h3').get_text()
        link = 'https://treeofsavior.com' + news.find('a').get('href')

        news_list +=  "{}. [{}]({})\n".format(str(n), title, link)

    embed = discord.Embed(colour=discord.Colour(0x1abc9c), description="[All](https://treeofsavior.com/page/news/?n=1) | [Event](https://treeofsavior.com/page/news/?c=33&n=1) | [Patch Notes](https://treeofsavior.com/page/news/?c=3&n=1) | [Dev's Blog](https://treeofsavior.com/page/news/?c=31&n=1) | [Known Issues](https://treeofsavior.com/page/news/?c=32&n=1)", timestamp=datetime.datetime.now())

    embed.set_thumbnail(url="https://treeofsavior.com/img/common/logo.png")
    embed.set_author(name="Tree Of Savior News & Update", url="https://treeofsavior.com/page/news/", icon_url="http://bestonlinegamesreview.com/wp-content/uploads/2016/04/p1_2006411_5eae6fd9.png")
    embed.set_footer(text="tree of savior - a buggy mmorpg")

    nlist = "".join(news_list)# for item in news_list
    embed.add_field(name="Patch Notes & News", value=nlist, inline = False)

    await bot.say(embed=embed)


bot.run(os.environ['BOT_TOKEN'])
