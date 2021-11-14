import discord
import random
import os
from keep_online import keep_alive

intents = discord.Intents.default()
intents.members = True
intents.emojis=True

client=discord.Client(intents=intents)

hg2g={
  "killjoy":0,
  "seegana":0,
  "ayaan":0,
  "debugger":0
}

@client.event
async def on_message(message):

 

  username=str(message.author).split("#")[0]
  mess=message.content

  #general mavayya phrases
  mavayya_maatalu=[
  f"entira {username} chusi kuda chudanattu velthunav...bagunava?",
  "manushulu manchollu ra, manashi antene manchodu!",
  "oka samanyudiga emi ivagalamu ra e samajaniki prema tho kudina oka kutumbam thappa...",
  "nuvvu, ee server nadipevallu, ee server ni abhimaaninche vallu, andaru baagundali ra!",
  "chakkaga oka navvu navvithe, meeku baguntundi, naku baaguntundi :grin:",
  "https://tenor.com/view/smile-prakash-raj-gif-reactions-mahesh-babu-gif-19508343",
  "aa bhagavantudni mana gurinchi korukovalsina avasaram em ledu ra... ala korukunte pakkodi gurinchi korukuvali :pray:",
  f"bhagavantudaa, nijayiti ga brathike {username} ni chiru navvu nunchi dooram cheyyaku...",
  f"yera {username} ela unnav, bagunnava?",
  "mee andarini ila server lo chutunte, entha haayi ga undho...",
  f"yera {username} , bhojanam chesava?",
  f"ఏరా {username}, నీ లిస్ట్ లో నుండి తీసేశావా నన్ను?",
  f"ఒరేయి {username}, దేవుణ్ణి ఏం కోరుకున్నావు రా?",
  f"అరేయి {username}, దాటగలిగే కష్టాల్నీనీ, ఆ కష్టాల్ని దాటే ధైర్యాన్నీ ఇవ్వమని దేవుణ్ణి అడగరా!"

  ]

  mavayya=["mavayya","Mavayya"]
  for i in mavayya:
    if i in mess:
	    await message.channel.send(random.choice(mavayya_maatalu))


  #list of cuss words
  bad_words=[
    "lauda",
    "modda",
    "sulli",
    "gudha",
    "dengey",
    "munda",
    "kutha",
    "lawda",
    "lowda",
    "puku",
    " ass ",
    "ass\n"
  ]

  for i in bad_words:
    if i in mess:
      await message.channel.send(f"yenti ra {username}, yemitaa maatalu?")

  if mess=="-react":
    emoji="wholesomemavayya"
    mess.add_reaction(emoji)
  
  #displays the avatar
  if mess == "-avatar":
    await message.channel.send(message.author.avatar_url)

  if mess == "-update hg2g":

    await message.channel.send("ye ra, yenno chapter varaku?")

    async def on_message(message):

      if str(message.author).split("#")[0]=="KILLJOY":
        hg2g["killjoy"]=int(message.content)
      if str(message.author).split("#")[0]=="psychedelicpoops":
        hg2g["seegana"]=int(message.content)
      if str(message.author).split("#")[0]=="Ayaan":
        hg2g["ayaan"]=int(message.content)
      if str(message.author).split("#")[0]=="debugger":
        hg2g["debugger"]=int(message.content)
    
  if mess == f"-progress {username}":
      if username=="KILLJOY":
        await message.channel.send(hg2g["killjoy"])
      if username=="psychedelicpoops":
        await message.channel.send(hg2g["seegana"])
      if username=="Ayaan":
        await message.channel.send(hg2g["ayaan"])
      if username=="debugger":
        await message.channel.send(hg2g["debugger"])

  #so that bot wouldn't summon itself
  if message.author==client.user:
    return


#welcome message when a member joins
@client.event
async def on_member_join(member):
  channel = client.get_channel(890388908813213727)
  await channel.send(f"Yem maa {member.mention} bavunnava..? Ye pusthakam chaduvtunnav e madya..?")

 
#keeping the bot online
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)
