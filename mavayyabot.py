
import discord
import random
import os
from keep_online import keep_alive
import time


intents = discord.Intents.default()
intents.members = True
intents.emojis=True
intents.reactions=True

client=discord.Client(intents=intents)

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
    "ass\n",
    " ass"
  ]

  for i in bad_words:
    if i in mess or i.upper() in mess:
      await message.channel.send(f"yenti ra {username}, yemitaa maatalu?")
  
  #displays the avatar
  if mess == "-avatar":
    await message.channel.send(message.author.avatar_url)
  
  if mess == "-insult killjoy":
    await message.channel.send("యే రా killjoy, బెవర్సే గా ఉన్నావంటే ఊర్కే టైంపాస్ చేయడమేనా? పనికొచ్చే పనులు ఏమన్నా చెయ్యచ్చు కదా? అన్నీ సగం నాలేడ్జి పనులు...")

  if mess == "-remind killjoy to sleep":
    await message.channel.send("orey killjoy, panduko po ra mundhu!")

  if mess == "-remind killjoy to come online":
    await message.channel.send("orey killjoy, pandukundi chalu, online ra ra!")
  
  admin=["admin","admeen","aadmin","yadmin","mod"]

  for i in admin:
    if i in mess and "make" in mess:
      await message.channel.send("Provide aadhar card, 10th class participation certificate, 2 passport size photos, then mod exam pass ga... Then interview pass ga... Internship ippistha.")
      break


  #so that bot wouldn't summon itself
  if message.author==client.user:
    return




#welcome message when a member joins
@client.event
async def on_member_join(member):
  time.sleep(1)
  channel = client.get_channel(890388908813213727)
  await channel.send(f"Yem maa {member.mention} bavunnava..? Ye pusthakam chaduvtunnav e madya..?")

'''@client.event
async def on_message_delete(message):
  time.sleep(5)
  botspam=client.get_channel(876497595441229824)
  await botspam.send("ye ra, nee thappulanni ila lokaniki thelikunda daachestunnava?")'''


@client.event
async def on_reaction_add(reaction, user):
  hall_of_fame=client.get_channel(911854338803109929)
  
  if reaction.emoji=="⭐" and reaction.count==1:

    mess=reaction.message.content
    user=reaction.message.author

    pop=discord.Embed(title=f"{mess}",color=user.color)
    pop.set_author(name=f"{user}")

    await hall_of_fame.send(embed=pop)
    




#keeping the bot online
my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)

