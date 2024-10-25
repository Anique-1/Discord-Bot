#import the libaries
import discord
from discord.ext import commands
import random


#inlitize the command structure
intents = discord.Intents.all()
intents.message_content=True
intents.emojis_and_stickers=True
client= commands.Bot(command_prefix="!", intents=intents)


#start the main Event
@client.event
async def on_ready():
    print("The Bot is Ready For use!")
    print("--------------------------")



#Hello Command Run this commmand write "!hello" 
@client.command()
async def Hello(ctx):
    monospace=f"``{"!Menu"}``"
    membed=discord.Embed(title="Welcome ❤️",description=f'{ctx.author.mention} Hello there! \n\n 👉How are you?We hope you are well!\n    ≿━━━━༺❀༻━━━━≾   \n ···· ☆ Visit The Menu ↓ \n\n      🔐 Write   {monospace}   to See Menu ✴', color=discord.Color.dark_orange())
    await ctx.send(embed=membed)

#Menu Command Run This Commmand write "!Menu"
@client.command()
async def Menu(ctx):
    bold48=f'**{"Character Name"}**'
    monospace=f"``{"![Character Name]"}``"
    aembed=discord.Embed(title="Card Menu ", description=f'{bold48} \n ---------------- \n 🔹 Taemin \n 🔸 Jongseob \n 🔹 Seoyeon \n 🔸 Joohyoung \n 🔹 Taeyeon \n 🔸 Leo \n 🔹 Hanbin \n 🔸 Rie \n 🔹 Sunwoo \n 🔸 Peniel \n 🔹 Chaesol \n 🔸 Yuri \n 🔹 Bae \n 🔸 Minzy \n 🔹 Riina \n 🔸 Yue \n 🔹 Hoya \n 🔸 Yuki \n 🔹 Baekseung \n 🔸 Yujin \n 🔹 Chaewon \n 🔸 Jiheon \n 🔹 Jisung \n 🔸 Taesan \n ---------------- \n  👉🏻 Write Character Name: {monospace} to claim Card! ', color=discord.Color.dark_red())
    await ctx.send(embed=aembed)




#BAE Character FLOW
@client.command()
async def Bae(ctx):
    monospace = f"``{"!claim [code]"}``"
    bold=f'**{"NMIXX Bae"}**'
    myembed=discord.Embed(title='Card Spawn',description=f'A new {bold} --⭐has been spawned.\n  Use {monospace} to claim it!',color=discord.Color.dark_gold())
    myembed.set_image(url="https://i.imgur.com/q5pnSDT.png")
    initial_message = await ctx.send(embed=myembed)

    # Wait for the user's input
    def check(a):
        return a.author == ctx.author and a.channel == ctx.channel

    user_input = await client.wait_for('message', check=check)

    # Expected code
    expected_code = "!claim RMSL"

    # Delete the initial message
    await initial_message.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input.content == expected_code:
        # Send a new embedded message for correct input
        bold1=f'**{"NMIXX Bae"}**'
        success_embed = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold1} -- ⭐card. \n\n Issue #{random_digits}', color=discord.Color.dark_orange())
        await ctx.send(embed=success_embed)



#BAEKSEUNG Character FLOW
@client.command()
async def Baekseung(ctx):
    monospace1 = f"``{"!claim [code]"}``"
    bold2=f'**{"EPEX Baekseung"}**'
    embed1=discord.Embed(title='Card Spawn',description=f'A new {bold2} --⭐has been spawned.\n  Use {monospace1} to claim it!',color=discord.Color.blurple())
    embed1.set_image(url="https://i.imgur.com/zsJH6vH.png")
    initial_message1 = await ctx.send(embed=embed1)

    # Wait for the user's input
    def check(b):
        return b.author == ctx.author and b.channel == ctx.channel

    user_input1 = await client.wait_for('message', check=check)

    # Expected code
    expected_code1 = "!claim WKFD"

    # Delete the initial message
    await initial_message1.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits1 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input1.content == expected_code1:
        # Send a new embedded message for correct input
        bold3=f'**{"EPEX Baekseung"}**'
        success_embed1 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold3} -- ⭐card. \n\n Issue #{random_digits1}', color=discord.Color.brand_green())
        await ctx.send(embed=success_embed1)



#CHAESOL Character FLOW
@client.command()
async def Chaesol(ctx):
    monospace2 = f"``{"!claim [code]"}``"
    bold4=f'**{"Cignature Chaesol"}**'
    embed2=discord.Embed(title='Card Spawn',description=f'A new {bold4} --⭐has been spawned.\n  Use {monospace2} to claim it!',color=discord.Color.dark_grey())
    embed2.set_image(url="https://i.imgur.com/mHLSrfX.png")
    initial_message2 = await ctx.send(embed=embed2)

    # Wait for the user's input
    def check(c):
        return c.author == ctx.author and c.channel == ctx.channel

    user_input2 = await client.wait_for('message', check=check)

    # Expected code
    expected_code2 = "!claim HAVJ"

    # Delete the initial message
    await initial_message2.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits2 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input2.content == expected_code2:
        # Send a new embedded message for correct input
        bold5=f'**{"Cignature Chaesol"}**'
        success_embed2 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold5} -- ⭐card. \n\n Issue #{random_digits2}', color=discord.Color.dark_red())
        await ctx.send(embed=success_embed2)


#CHAEWON Character FLOW
@client.command()
async def Chaewon(ctx):
    monospace3 = f"``{"!claim [code]"}``"
    bold6=f'**{"IZ*ONE Chaewon"}**'
    embed3=discord.Embed(title='Card Spawn',description=f'A new {bold6} --⭐has been spawned.\n  Use {monospace3} to claim it!',color=discord.Color.dark_purple())
    embed3.set_image(url="https://i.imgur.com/TtpP6F6.png")
    initial_message3 = await ctx.send(embed=embed3)

    # Wait for the user's input
    def check(d):
        return d.author == ctx.author and d.channel == ctx.channel

    user_input3 = await client.wait_for('message', check=check)

    # Expected code
    expected_code3 = "!claim FOMG"

    # Delete the initial message
    await initial_message3.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits3 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input3.content == expected_code3:
        # Send a new embedded message for correct input
        bold7=f'**{"IZ*ONE Chaewon"}**'
        success_embed3 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold7} -- ⭐card. \n\n Issue #{random_digits3}', color=discord.Color.dark_orange())
        await ctx.send(embed=success_embed3)



#HOYA Character FLOW
@client.command()
async def Hoya(ctx):
    monospace4 = f"``{"!claim [code]"}``"
    bold8=f'**{"INFINITE Hoya"}**'
    embed4=discord.Embed(title='Card Spawn',description=f'A new {bold8} --⭐has been spawned.\n  Use {monospace4} to claim it!',color=discord.Color.dark_magenta())
    embed4.set_image(url="https://i.imgur.com/EDcI2ZI.png")
    initial_message4 = await ctx.send(embed=embed4)

    # Wait for the user's input
    def check(e):
        return e.author == ctx.author and e.channel == ctx.channel

    user_input4 = await client.wait_for('message', check=check)

    # Expected code
    expected_code4 = "!claim SEJP"

    # Delete the initial message
    await initial_message4.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits4 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input4.content == expected_code4:
        # Send a new embedded message for correct input
        bold9=f'**{"INFINITE Hoya"}**'
        success_embed4 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold9} -- ⭐card. \n\n Issue #{random_digits4}', color=discord.Color.dark_gold())
        await ctx.send(embed=success_embed4)

#JIHEON Character FLOW
@client.command()
async def Jiheon(ctx):
    monospace5 = f"``{"!claim [code]"}``"
    bold10=f'**{"Fromis_9 Jiheon"}**'
    embed5=discord.Embed(title='Card Spawn',description=f'A new {bold10} --⭐has been spawned.\n  Use {monospace5} to claim it!',color=discord.Color.dark_grey())
    embed5.set_image(url="https://i.imgur.com/8eYE7Wd.png")
    initial_message5 = await ctx.send(embed=embed5)

    # Wait for the user's input
    def check(f):
        return f.author == ctx.author and f.channel == ctx.channel

    user_input5 = await client.wait_for('message', check=check)

    # Expected code
    expected_code5 = "!claim NLAJ"

    # Delete the initial message
    await initial_message5.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits5 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input5.content == expected_code5:
        # Send a new embedded message for correct input
        bold11=f'**{"Fromis_9 Jiheon"}**'
        success_embed5 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold11} -- ⭐card. \n\n Issue #{random_digits5}', color=discord.Color.dark_magenta())
        await ctx.send(embed=success_embed5)



#JISUNG Character FLOW
@client.command()
async def Jisung(ctx):
    monospace6 = f"``{"!claim [code]"}``"
    bold12=f'**{"NCT Dream Jisung"}**'
    embed6=discord.Embed(title='Card Spawn',description=f'A new {bold12} --⭐has been spawned.\n  Use {monospace6} to claim it!',color=discord.Color.dark_gold())
    embed6.set_image(url="https://i.imgur.com/D5ZbFiT.png")
    initial_message6 = await ctx.send(embed=embed6)

    # Wait for the user's input
    def check(g):
        return g.author == ctx.author and g.channel == ctx.channel

    user_input6 = await client.wait_for('message', check=check)

    # Expected code
    expected_code6 = "!claim OMJF"

    # Delete the initial message
    await initial_message6.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits6 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input6.content == expected_code6:
        # Send a new embedded message for correct input
        bold13=f'**{"NCT Dream Jisung"}**'
        success_embed6 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold13} -- ⭐card. \n\n Issue #{random_digits6}', color=discord.Color.dark_blue())
        await ctx.send(embed=success_embed6)



#JONGSEOB Character FLOW
@client.command()
async def Jongseob(ctx):
    monospace7 = f"``{"!claim [code]"}``"
    bold14=f'**{"P1Harmony Jongseob"}**'
    embed7=discord.Embed(title='Card Spawn',description=f'A new {bold14} --⭐has been spawned.\n  Use {monospace7} to claim it!',color=discord.Color.brand_green())
    embed7.set_image(url="https://i.imgur.com/xQO6KHF.png")
    initial_message7 = await ctx.send(embed=embed7)

    # Wait for the user's input
    def check(h):
        return h.author == ctx.author and h.channel == ctx.channel

    user_input7 = await client.wait_for('message', check=check)

    # Expected code
    expected_code7 = "!claim KKGD"

    # Delete the initial message
    await initial_message7.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits7 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input7.content == expected_code7:
        # Send a new embedded message for correct input
        bold15=f'**{"P1Harmony Jongseob"}**'
        success_embed7 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold15} -- ⭐card. \n\n Issue #{random_digits7}', color=discord.Color.dark_magenta())
        await ctx.send(embed=success_embed7)


#JOOHYOUNG Character FLOW
@client.command()
async def Joohyoung(ctx):
    monospace8 = f"``{"!claim [code]"}``"
    bold16=f'**{"NINE.i Joohyoung"}**'
    embed8=discord.Embed(title='Card Spawn',description=f'A new {bold16} --⭐has been spawned.\n  Use {monospace8} to claim it!',color=discord.Color.dark_red())
    embed8.set_image(url="https://i.imgur.com/nPKUnvS.png")
    initial_message8 = await ctx.send(embed=embed8)

    # Wait for the user's input
    def check(i):
        return i.author == ctx.author and i.channel == ctx.channel

    user_input8 = await client.wait_for('message', check=check)

    # Expected code
    expected_code8 = "!claim TRNG"

    # Delete the initial message
    await initial_message8.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits8 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input8.content == expected_code8:
        # Send a new embedded message for correct input
        bold17=f'**{"NINE.i Joohyoung"}**'
        success_embed8 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold17} -- ⭐card. \n\n Issue #{random_digits8}', color=discord.Color.pink())
        await ctx.send(embed=success_embed8)


#LEO Character FLOW
@client.command()
async def Leo(ctx):
    monospace9 = f"``{"!claim [code]"}``"
    bold18=f'**{"VIXX Leo"}**'
    embed9=discord.Embed(title='Card Spawn',description=f'A new {bold18} --⭐has been spawned.\n  Use {monospace9} to claim it!',color=discord.Color.dark_blue())
    embed9.set_image(url="https://i.imgur.com/DsiHuXw.png")
    initial_message9 = await ctx.send(embed=embed9)

    # Wait for the user's input
    def check(j):
        return j.author == ctx.author and j.channel == ctx.channel

    user_input9 = await client.wait_for('message', check=check)

    # Expected code
    expected_code9 = "!claim AVJC"

    # Delete the initial message
    await initial_message9.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits9 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input9.content == expected_code9:
        # Send a new embedded message for correct input
        bold19=f'**{"VIXX Leo"}**'
        success_embed9 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold19} -- ⭐card. \n\n Issue #{random_digits9}', color=discord.Color.dark_green())
        await ctx.send(embed=success_embed9)




#MINZY Character FLOW
@client.command()
async def Minzy(ctx):
    monospace10 = f"``{"!claim [code]"}``"
    bold20=f'**{"2NE1 Minzy"}**'
    embed10=discord.Embed(title='Card Spawn',description=f'A new {bold20} --⭐has been spawned.\n  Use {monospace10} to claim it!',color=discord.Color.dark_gold())
    embed10.set_image(url="https://i.imgur.com/xYo42LX.png")
    initial_message10 = await ctx.send(embed=embed10)

    # Wait for the user's input
    def check(k):
        return k.author == ctx.author and k.channel == ctx.channel

    user_input10 = await client.wait_for('message', check=check)

    # Expected code
    expected_code10 = "!claim UXSY"

    # Delete the initial message
    await initial_message10.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits10 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input10.content == expected_code10:
        # Send a new embedded message for correct input
        bold21=f'**{"2NE1 Minzy"}**'
        success_embed10 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold21} -- ⭐card. \n\n Issue #{random_digits10}', color=discord.Color.dark_grey())
        await ctx.send(embed=success_embed10)


#PARK HANBIN Character FLOW
@client.command()
async def Hanbin(ctx):
    monospace11 = f"``{"!claim [code]"}``"
    bold22=f'**{"EVNNE Park Hanbin"}**'
    embed11=discord.Embed(title='Card Spawn',description=f'A new {bold22} --⭐has been spawned.\n  Use {monospace11} to claim it!',color=discord.Color.brand_green())
    embed11.set_image(url="https://i.imgur.com/AxBTYj8.png")
    initial_message11 = await ctx.send(embed=embed11)

    # Wait for the user's input
    def check(l):
        return l.author == ctx.author and l.channel == ctx.channel

    user_input11 = await client.wait_for('message', check=check)

    # Expected code
    expected_code11 = "!claim GFRB"

    # Delete the initial message
    await initial_message11.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits11 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input11.content == expected_code11:
        # Send a new embedded message for correct input
        bold23=f'**{"EVNNE Park Hanbin"}**'
        success_embed11 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold23} -- ⭐card. \n\n Issue #{random_digits11}', color=discord.Color.dark_orange())
        await ctx.send(embed=success_embed11)




#PENIEL Character FLOW
@client.command()
async def Peniel(ctx):
    monospace12 = f"``{"!claim [code]"}``"
    bold24=f'**{"BTOB Peniel"}**'
    embed12=discord.Embed(title='Card Spawn',description=f'A new {bold24} --⭐has been spawned.\n  Use {monospace12} to claim it!',color=discord.Color.brand_red())
    embed12.set_image(url="https://i.imgur.com/x1eU9OV.png")
    initial_message12 = await ctx.send(embed=embed12)

    # Wait for the user's input
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    user_input12 = await client.wait_for('message', check=check)

    # Expected code
    expected_code12 = "!claim MGRO"

    # Delete the initial message
    await initial_message12.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits12 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input12.content == expected_code12:
        # Send a new embedded message for correct input
        bold25=f'**{"BTOB Peniel"}**'
        success_embed12 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold25} -- ⭐card. \n\n Issue #{random_digits12}', color=discord.Color.darker_grey())
        await ctx.send(embed=success_embed12)





#RIE Character FLOW
@client.command()
async def Rie(ctx):
    monospace13 = f"``{"!claim [code]"}``"
    bold26=f'**{"OnlyOneOf Rie"}**'
    embed13=discord.Embed(title='Card Spawn',description=f'A new {bold26} --⭐has been spawned.\n  Use {monospace13} to claim it!',color=discord.Color.dark_magenta())
    embed13.set_image(url="https://i.imgur.com/NSQy9ga.png")
    initial_message13 = await ctx.send(embed=embed13)

    # Wait for the user's input
    def check(n):
        return n.author == ctx.author and n.channel == ctx.channel

    user_input13 = await client.wait_for('message', check=check)

    # Expected code
    expected_code13 = "!claim FFSE"

    # Delete the initial message
    await initial_message13.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits13 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input13.content == expected_code13:
        # Send a new embedded message for correct input
        bold27=f'**{"OnlyOneOf Rie"}**'
        success_embed13 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold27} -- ⭐card. \n\n Issue #{random_digits13}', color=discord.Color.brand_red())
        await ctx.send(embed=success_embed13)




#RIINA Character FLOW
@client.command()
async def Riina(ctx):
    monospace14 = f"``{"!claim [code]"}``"
    bold28=f'**{"H1-KEY Riina"}**'
    embed14=discord.Embed(title='Card Spawn',description=f'A new {bold28} --⭐has been spawned.\n  Use {monospace14} to claim it!',color=discord.Color.dark_gold())
    embed14.set_image(url="https://i.imgur.com/pEOGGL7.png")
    initial_message14 = await ctx.send(embed=embed14)

    # Wait for the user's input
    def check(o):
        return o.author == ctx.author and o.channel == ctx.channel

    user_input14 = await client.wait_for('message', check=check)

    # Expected code
    expected_code14 = "!claim MUYE"

    # Delete the initial message
    await initial_message14.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits14 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input14.content == expected_code14:
        # Send a new embedded message for correct input
        bold29=f'**{"H1-KEY Riina"}**'
        success_embed14 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold29} -- ⭐card. \n\n Issue #{random_digits14}', color=discord.Color.dark_magenta())
        await ctx.send(embed=success_embed14)



#SEOYEON Character FLOW
@client.command()
async def Seoyeon(ctx):
    monospace15 = f"``{"!claim [code]"}``"
    bold30=f'**{"CSR Seoyeon"}**'
    embed15=discord.Embed(title='Card Spawn',description=f'A new {bold30} --⭐has been spawned.\n  Use {monospace15} to claim it!',color=discord.Color.blurple())
    embed15.set_image(url="https://i.imgur.com/xaBTx8B.png")
    initial_message15 = await ctx.send(embed=embed15)

    # Wait for the user's input
    def check(p):
        return p.author == ctx.author and p.channel == ctx.channel

    user_input15 = await client.wait_for('message', check=check)

    # Expected code
    expected_code15 = "!claim ATBW"

    # Delete the initial message
    await initial_message15.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits15 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input15.content == expected_code15:
        # Send a new embedded message for correct input
        bold31=f'**{"CSR Seoyeon"}**'
        success_embed15 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold31} -- ⭐card. \n\n Issue #{random_digits15}', color=discord.Color.dark_green())
        await ctx.send(embed=success_embed15)




#SUNWOO Character FLOW
@client.command()
async def Sunwoo(ctx):
    monospace16 = f"``{"!claim [code]"}``"
    bold32=f'**{"The Boyz Sunwoo"}**'
    embed16=discord.Embed(title='Card Spawn',description=f'A new {bold32} --⭐has been spawned.\n  Use {monospace16} to claim it!',color=discord.Color.brand_green())
    embed16.set_image(url="https://i.imgur.com/Gq8mAJi.png")
    initial_message16 = await ctx.send(embed=embed16)

    # Wait for the user's input
    def check(q):
        return q.author == ctx.author and q.channel == ctx.channel

    user_input16 = await client.wait_for('message', check=check)

    # Expected code
    expected_code16 = "!claim BAVV"

    # Delete the initial message
    await initial_message16.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits16 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input16.content == expected_code16:
        # Send a new embedded message for correct input
        bold33=f'**{"The Boyz Sunwoo"}**'
        success_embed16 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold33} -- ⭐card. \n\n Issue #{random_digits16}', color=discord.Color.blue())
        await ctx.send(embed=success_embed16)




#TAEMIN Character FLOW
@client.command()
async def Taemin(ctx):
    monospace17 = f"``{"!claim [code]"}``"
    bold34=f'**{"Shinee Taemin"}**'
    embed17=discord.Embed(title='Card Spawn',description=f'A new {bold34} --⭐has been spawned.\n  Use {monospace17} to claim it!',color=discord.Color.dark_magenta())
    embed17.set_image(url="https://i.imgur.com/7UYjUaN.png")
    initial_message17 = await ctx.send(embed=embed17)

    # Wait for the user's input
    def check(r):
        return r.author == ctx.author and r.channel == ctx.channel

    user_input17 = await client.wait_for('message', check=check)

    # Expected code
    expected_code17 = "!claim DVNR"

    # Delete the initial message
    await initial_message17.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits17 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input17.content == expected_code17:
        # Send a new embedded message for correct input
        bold35=f'**{"Shinee Taemin"}**'
        success_embed17 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold35} -- ⭐card. \n\n Issue #{random_digits17}', color=discord.Color.dark_gold())
        await ctx.send(embed=success_embed17)




#TAESAN Character FLOW
@client.command()
async def Taesan(ctx):
    monospace18 = f"``{"!claim [code]"}``"
    bold36=f'**{"BOYNEXTDOOR Taesan"}**'
    embed18=discord.Embed(title='Card Spawn',description=f'A new {bold36} --⭐has been spawned.\n  Use {monospace18} to claim it!',color=discord.Color.dark_grey())
    embed18.set_image(url="https://i.imgur.com/WpdpsvC.png")
    initial_message18 = await ctx.send(embed=embed18)

    # Wait for the user's input
    def check(s):
        return s.author == ctx.author and s.channel == ctx.channel

    user_input18 = await client.wait_for('message', check=check)

    # Expected code
    expected_code18 = "!claim XESE"

    # Delete the initial message
    await initial_message18.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits18 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input18.content == expected_code18:
        # Send a new embedded message for correct input
        bold37=f'**{"BOYNEXTDOOR Taesan"}**'
        success_embed18 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold37} -- ⭐card. \n\n Issue #{random_digits18}', color=discord.Color.dark_purple())
        await ctx.send(embed=success_embed18)



#TAEYEON Character FLOW
@client.command()
async def Taeyeon(ctx):
    monospace19 = f"``{"!claim [code]"}``"
    bold38=f'**{"GOT The Beat Taeyeon"}**'
    embed19=discord.Embed(title='Card Spawn',description=f'A new {bold38} --⭐has been spawned.\n  Use {monospace19} to claim it!',color=discord.Color.dark_green())
    embed19.set_image(url="https://i.imgur.com/j8sIJrU.png")
    initial_message19 = await ctx.send(embed=embed19)

    # Wait for the user's input
    def check(t):
        return t.author == ctx.author and t.channel == ctx.channel

    user_input19 = await client.wait_for('message', check=check)

    # Expected code
    expected_code19 = "!claim OGHR"

    # Delete the initial message
    await initial_message19.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits19 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input19.content == expected_code19:
        # Send a new embedded message for correct input
        bold39=f'**{"GOT The Beat Taeyeon"}**'
        success_embed19 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold39} -- ⭐card. \n\n Issue #{random_digits19}', color=discord.Color.blurple())
        await ctx.send(embed=success_embed19)




#YUE Character FLOW
@client.command()
async def Yue(ctx):
    monospace20 = f"``{"!claim [code]"}``"
    bold40=f'**{"LAPILLUS Yue"}**'
    embed20=discord.Embed(title='Card Spawn',description=f'A new {bold40} --⭐has been spawned.\n  Use {monospace20} to claim it!',color=discord.Color.dark_gold())
    embed20.set_image(url="https://i.imgur.com/djeV2Pi.png")
    initial_message20 = await ctx.send(embed=embed20)

    # Wait for the user's input
    def check(u):
        return u.author == ctx.author and u.channel == ctx.channel

    user_input20 = await client.wait_for('message', check=check)

    # Expected code
    expected_code20 = "!claim UEBG"

    # Delete the initial message
    await initial_message20.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits20 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input20.content == expected_code20:
        # Send a new embedded message for correct input
        bold41=f'**{"LAPILLUS Yue"}**'
        success_embed20 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold41} -- ⭐card. \n\n Issue #{random_digits20}', color=discord.Color.dark_blue())
        await ctx.send(embed=success_embed20)




#YUJIN Character FLOW
@client.command()
async def Yujin(ctx):
    monospace21 = f"``{"!claim [code]"}``"
    bold42=f'**{"ZB1 Han Yu Jin"}**'
    embed21=discord.Embed(title='Card Spawn',description=f'A new {bold42} --⭐has been spawned.\n  Use {monospace21} to claim it!',color=discord.Color.dark_grey())
    embed21.set_image(url="https://i.imgur.com/OPrQTXk.png")
    initial_message21 = await ctx.send(embed=embed21)

    # Wait for the user's input
    def check(v):
        return v.author == ctx.author and v.channel == ctx.channel

    user_input21 = await client.wait_for('message', check=check)

    # Expected code
    expected_code21 = "!claim RNYG"

    # Delete the initial message
    await initial_message21.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits21 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input21.content == expected_code21:
        # Send a new embedded message for correct input
        bold43=f'**{"ZB1 Han Yu Jin"}**'
        success_embed21 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold43} -- ⭐card. \n\n Issue #{random_digits21}', color=discord.Color.dark_magenta())
        await ctx.send(embed=success_embed21)





#YUKI Character FLOW
@client.command()
async def Yuki(ctx):
    monospace22 = f"``{"!claim [code]"}``"
    bold44=f'**{"PURPLE KISS Yuki"}**'
    embed22=discord.Embed(title='Card Spawn',description=f'A new {bold44} --⭐has been spawned.\n  Use {monospace22} to claim it!',color=discord.Color.dark_purple())
    embed22.set_image(url="https://i.imgur.com/xBVvuzq.png")
    initial_message22 = await ctx.send(embed=embed22)

    # Wait for the user's input
    def check(w):
        return w.author == ctx.author and w.channel == ctx.channel

    user_input22 = await client.wait_for('message', check=check)

    # Expected code
    expected_code22 = "!claim IITA"

    # Delete the initial message
    await initial_message22.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits22 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input22.content == expected_code22:
        # Send a new embedded message for correct input
        bold45=f'**{"PURPLE KISS Yuki"}**'
        success_embed22 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold45} -- ⭐card. \n\n Issue #{random_digits22}', color=discord.Color.dark_blue())
        await ctx.send(embed=success_embed22)



#YURI Character FLOW
@client.command()
async def Yuri(ctx):
    monospace23 = f"``{"!claim [code]"}``"
    bold46=f'**{"IZ*ONE Yuri"}**'
    embed23=discord.Embed(title='Card Spawn',description=f'A new {bold46} --⭐has been spawned.\n  Use {monospace23} to claim it!',color=discord.Color.dark_magenta())
    embed23.set_image(url="https://i.imgur.com/WcgkBvq.png")
    initial_message23 = await ctx.send(embed=embed23)

    # Wait for the user's input
    def check(x):
        return x.author == ctx.author and x.channel == ctx.channel

    user_input23 = await client.wait_for('message', check=check)

    # Expected code
    expected_code23 = "!claim RESD"

    # Delete the initial message
    await initial_message23.delete()
    #program generate number
    def generate_random_digits():
        digits = []
        for _ in range(4):
            digit = random.randint(0, 9)
            digits.append(str(digit))
        return ''.join(digits)
    random_digits23 = generate_random_digits()

    # Check if the user's input matches the expected code
    if user_input23.content == expected_code23:
        # Send a new embedded message for correct input
        bold47=f'**{"IZ*ONE Yuri"}**'
        success_embed23 = discord.Embed(title=f'{ctx.author.name}',description=f'{ctx.author.mention} has claimed the {bold47} -- ⭐card. \n\n Issue #{random_digits23}', color=discord.Color.dark_orange())
        await ctx.send(embed=success_embed23)




client.run("Enter the API")







