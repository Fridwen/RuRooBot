import discord, asyncio, os, random, re, youtube_dl, requests
from random import choice
from discord.ext import commands
from bs4 import BeautifulSoup
game = discord.Game("냥!")
client = discord.Client(status=discord.Status.online, activity=game)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
TOKEN = os.environ.get('BOT_TOKEN')
@client.event
async def on_message(message):
    if message.content == "!안녕":
        await message.channel.send(f"{message.author.mention}님 안녕하다냥")

    if message.content == "!주사위":
        await message.channel.send(f"{message.author.mention} 범위를 입력해달라냥 ex) !주사위 6")

    if message.content.startswith("!주사위 ") :
        number = message.content.replace("!주사위 ", "")
        check_number = number.isdigit()

        if check_number == True:
            Randnumber = random.randint(1,int(number))
            msg = await message.channel.send(f"{message.author.mention} 주사위를 굴려 {Randnumber}이(가) 나왔다냥 (범위 1 ~ {number})")
        else:
            await message.channel.send(f"{message.author.mention} 올바른 값을 입력해달라냥")

    if message.content.startswith("!경기 "):
        member = list(message.content.replace("!경기 ", "").split())
        teamA = []
        teamB = []

        while len(member) > 0:
            memberA = choice(member)
            teamA.append(memberA)
            member.remove(memberA)
            memberB = choice(member)
            teamB.append(memberB)
            member.remove(memberB)

        embed = discord.Embed(title="**자리 배정**", color=0x0303000)
        embed.add_field(name="1팀", value=teamA, inline=True)
        embed.add_field(name="2팀", value=teamB, inline=True)
        await message.channel.send(embed=embed)
    
    if message.content.startswith("!범석대 "):
        member = list(message.content.replace("!범석대 ", "").split())
        teamA = []
        teamB = []

        while len(member) > 0:
            memberA = choice(member)
            teamA.append(memberA)
            member.remove(memberA)
            memberB = choice(member)
            teamB.append(memberB)
            member.remove(memberB)

        embed = discord.Embed(title="**범석대 조 편성**", color=0x0303000)
        embed.add_field(name="A조", value=teamA, inline=True)
        embed.add_field(name="B조", value=teamB, inline=True)
        await message.channel.send(embed=embed)
    
    if message.content == "!명령어":
        if message.author.dm_channel:
            embed = discord.Embed(title = "[루루봇 명령어]", color = discord.Color.dark_blue())
            embed.add_field(name = "**★ 주사위**", value = "- !주사위 (정수) - 1 부터 해당 정수의 범위로 랜덤한 값을 추출한다냥", inline = False)
            embed.add_field(name = "**★ 경기**", value = "- !경기 (이름) (이름) (이름) (이름)... - 짝수개의 값을 넣으면 랜덤하게 두 팀으로 나눠준다냥 ", inline = False)
            embed.add_field(name = "**★ 안녕**", value = "- !안녕 - 인사를 해준다냥", inline = False)
            embed.add_field(name = "**★ 이리와**", value = "- !이리와 - 음성 채널에 들어온다냥", inline = False)
            embed.add_field(name = "**★ 저리가**", value = "- !저리가 - 음성 채널에서 나간다냥", inline = False)
            embed.add_field(name = "**★ 전적검색**", value = "- !전적검색 (이름) - (이름) 플레이어의 롤 전적을 검색해준다냥", inline = False)
            embed.set_author(name = "루루봇", icon_url = "https://cdn.discordapp.com/attachments/916751424686260276/916756875981238272/69e5983b355aff34.jpg")
            user_id ='686565060826366004'
            embed.add_field(name = "\n★ 문의", value = f"<@{user_id}>", inline = False)
            await message.author.dm_channel.send(embed=embed)

        elif message.author.dm_channel is None:
            channel = await message.author.create_dm()
            embed = discord.Embed(title = "[루루봇 명령어]", color = discord.Color.dark_blue())
            embed.add_field(name = "**★ 주사위**", value = "- !주사위 (정수) - 1 부터 해당 정수의 범위로 랜덤한 값을 추출한다냥", inline = False)
            embed.add_field(name = "**★ 경기**", value = "- !경기 (이름) (이름) (이름) (이름)... - 짝수개의 값을 넣으면 랜덤하게 두 팀으로 나눠준다냥 ", inline = False)
            embed.add_field(name = "**★ 안녕**", value = "- !안녕 - 인사를 해준다냥", inline = False)
            embed.add_field(name = "**★ 이리와**", value = "- !이리와 - 음성 채널에 들어온다냥", inline = False)
            embed.add_field(name = "**★ 저리가**", value = "- !저리가 - 음성 채널에서 나간다냥", inline = False)
            embed.add_field(name = "**★ 전적검색**", value = "- !전적검색 (이름) - (이름) 플레이어의 롤 전적을 검색해준다냥", inline = False)
            embed.set_author(name = "루루봇", icon_url = "https://cdn.discordapp.com/attachments/916751424686260276/916756875981238272/69e5983b355aff34.jpg")
            user_id ='686565060826366004'
            embed.add_field(name = "\n★ 문의", value = f"<@{user_id}>", inline = False)
            await channel.send(embed=embed)
    
    
    if message.content.startswith("!이리와"):
        user = message.author
        vc = user.voice.channel
        bot = client.get_user('916623193010229278')
        voice= discord.utils.get(client.voice_clients, guild=message.guild)
        if voice == None:
            await vc.connect()
            await message.channel.send("음성 채널에 들어왔다냥")

    if message.content == "!저리가":
        for voc in client.voice_clients:
            if voc.guild == message.guild:
                voice1 = voc
        await voice1.disconnect()
        await message.channel.send("음성 채널에서 나갔다냥")

    if message.content.startswith("!전적검색 "):
        user = message.content.replace("!전적검색 ", "")
        data1 = requests.get(f'https://www.op.gg/summoners/kr/{user}',headers=headers)
        soup = BeautifulSoup(data1.text, 'html.parser')
        tier = soup.find("div", class_="tier-rank")
        lp = soup.find("span", class_="lp")
        winlose = soup.find("span", class_="win-lose")
        lgname = soup.find("div", class_="league-name")
        if tier == None:
            img = "https://ww.namu.la/s/452135c0507972ac84a1280a7830b665310aa8897090d235be7017e96a666979de058d542893689518a700f8631b368c86467ce37b7d9235e24e61de3e67704c9ede04b4174b9edec93590008ae22984"
            gumki = soup.find("div", class_="unranked").get_text()
            embedstat = discord.Embed(title=user + "님의 전적 정보", description="", color=0x62c1cc)
            embedstat.set_thumbnail(url=img)
            embedstat.add_field(name="티어 정보", value="`" + "0 lp" + " | " + "Unranked" + "`", inline=False)
            embedstat.set_footer(text="솔로랭크 > 자유랭크 > 언랭의 우선도로 전적이 출력된다냥")
            await message.channel.send(embed=embedstat)
        else:
            img = "https://ww.namu.la/s/452135c0507972ac84a1280a7830b665310aa8897090d235be7017e96a666979de058d542893689518a700f8631b368c86467ce37b7d9235e24e61de3e67704c9ede04b4174b9edec93590008ae22984"
            tier = tier.get_text()
            lp = lp.get_text()
            winlose = winlose.get_text()
            # lgname = lgname.get_text()
            print(tier)
            print(lp)
            winlose = winlose.replace("Win Rate", "승률")
            winlose = winlose.replace("W", "승")
            winlose = winlose.replace("L", "패 | ")
            if "iron" in tier:
                tier = tier.replace("iron", "아이언")
            if "bronze" in tier:
                tier = tier.replace("bronze", "브론즈")
            if "silver" in tier:
                tier = tier.replace("silver", "실버")
            if "gold" in tier:
                tier = tier.replace("gold", "골드")
            if "platinum" in tier:
                tier = tier.replace("platinum", "플래티넘")
            if "diamond" in tier:
                tier = tier.replace("diamond", "다이아몬드")
            if "master" in tier:
                tier = tier.replace("master", "마스터")
            if "grandmaster" in tier:
                tier = tier.replace("grandmaster", "그랜드마스터")
            if "challenger" in tier:
                tier = tier.replace("challenger", "챌린저")
            print(winlose)
            embedstat = discord.Embed(title=user + "님의 전적 정보다냥", description="", color=0x62c1cc)
            embedstat.set_thumbnail(url=img)
            embedstat.add_field(name="티어 정보", value="`" + lp + " | " + tier + "`", inline=False)
            embedstat.add_field(name="승률", value="`" + winlose + "`", inline=False)
            embedstat.set_footer(text="솔로랭크 > 자유랭크 > 언랭의 우선도로 전적이 출력된다냥")
            await message.channel.send(embed=embedstat)


client.run(TOKEN)
