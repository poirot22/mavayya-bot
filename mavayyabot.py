import discord
import random
import os
from keep_online import keep_alive



intents = discord.Intents.default()
intents.members = True

client=discord.Client(intents=intents)


@client.event
async def on_message(message):

  username=str(message.author).split("#")[0]
  mess=message.content

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
  f"yera {username} , bhojanam chesava?"
  ]

  mavayya=["mavayya","Mavayya"]
  for i in mavayya:
    if i in mess:
	    await message.channel.send(random.choice(mavayya_maatalu))

  bad_words=[
    "dengey",
    "lauda",
    "modda",
    "sulli",
    "gudha",
    "dengey",
    "munda",
    "kutha",
    "lawda",
    "lowda",
    "puku"
  ]

  for i in bad_words:
    if i in mess:
      await message.channel.send(f"yenti ra {username}, yemitaa maatalu?")
  
  if message.author==client.user:
    return
  

@client.event
async def on_member_join(member):

  welcome=[
    f"ye ra {member.mention}, ela unnav? em book chaduvutunnav ee madhya?",
    f"ha ha, ye ra {member.mention}, nuvvu kuda ochesava ikkadiki? ochi manchi pane chesavu le ra, em chaduvutunnav?",
  ]
  channel = client.get_channel(890388908813213727)
  await channel.send(f"Yem maa {member.mention} bavunnava..? Ye pusthakam chaduvtunnav e madya..?")
 

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)