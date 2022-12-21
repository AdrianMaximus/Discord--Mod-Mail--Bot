import discord, asyncio, time, datetime
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import has_permissions
import os
import openai

bot = commands.Bot(
  command_prefix='?',
  case_insensitive=False,
  description=None,
  intents=discord.Intents.all(),
  help_command=None
)   

@bot.event
async def on_message(message):
  try:
    gd = await bot.fetch_guild(paste your guild id here with brackets)
    category1 = bot.get_channel(paste your category id here with brackets) 

    #### TICKET CLOSE FUNCTION ####
    if message.channel in category1.channels and message.channel.id != (paste ur log channel id without brackets) and message.author.id != (paste your bot id wihtout brackets) and message.content == '?close':
      category = bot.get_channel(paste your category id here with brackets) 
      ch = await bot.fetch_channel(paste your log channel id here with brackets)
      id = message.channel.topic
      usr = await bot.fetch_user(id)

      await message.channel.send('CLOSING TICKET ...')
      await usr.send(f"**Greetings {usr.name}**\n```Your Ticket has been closed by our moderation team. If you want to contact us again , message in this channel once again. Note that, we don't accept any sort of trolling.```\n**Thank you**")
      embed = discord.Embed(title='TICKET CLOSED', description=f'Ticket created by {usr.name} is closed by {message.author.name}', color = 0xFF0000)
      await ch.send(embed=embed)
      await asyncio.sleep(6)
      await usr.send(embed=embed)
      await message.channel.delete()

      #### MODERATOR REPLY FUNCTION ####
      if message.channel in category1.channels and message.channel.id != (paste ur log channel id without brackets)  and message.author.id != (paste your bot id wihtout brackets) and message.content != '?close':

        usrid = message.channel.topic
      usr = await bot.fetch_user(usrid)
      
      if message.content == None:
        msg = 'None'
      else:
        msg = message.content
            
      embed6 = discord.Embed(title='Message from TEAM 💬', description=f'{msg}')
      await usr.send(embed=embed6)
      urls=[]
      for att in message.attachments:
          urls.append(att.url)
      embed7 = discord.Embed(title='Attachmet 🔗',color = 0x75E6DA)
      embed7.set_image(url=f'{urls[0]}')
      await usr.send(embed=embed7)

      if message.channel.type == discord.ChannelType.private:
        if message.author.id != (paste your bot id wihtout brackets) :

          #### CHECKING IF USER HAS ALREADY CREATED A TICKET ####
          topics = []
          a = 'b'
          
          for x in category1.channels:
            topics.append(x.topic)
            a = x.id
            
          if f'{message.author.id}' in topics:
            chnl = await bot.fetch_channel(a)
            if message.content == None:
              msg = 'None'
            else:
              msg = message.content
            embed3 = discord.Embed(title='Message 💬', description=f'{msg}')
            await chnl.send(embed=embed3)
            urls=[]
            for att in message.attachments:
               urls.append(att.url)
            embed4 = discord.Embed(title='Attachmet 🔗',color = 0x75E6DA)
            embed4.set_image(url=f'{urls[0]}')
            await chnl.send(embed=embed4)
            
        else:
           ### CREATING TEXT CHANNEL ###
          m1 = await gd.create_text_channel(f'{message.author.name}', category=category1, topic=f'{message.author.id}')

          ### SENDING USER A DM ###
          embed1 = discord.Embed(title=f'Greetings {message.author.name}', description='```New ticket has been created for you , send your messages in my DM, which will be sent to our Moderation team and we will respond you soon.\n\nNote the following things:\n1) Animated emotes wont be visible to mods.\n2) If you have to send images send one by one\n3) Make sure you dont send nsfw content or swear during the course of help.\n4) You cannot close a ticket since, there might be a chance of reopening your ticket .\n5) Be respectful and follow discord TOS ```\n**Thank you**', color=0x00FF00)
      
          await message.author.send(embed=embed1)


          ### SEND TICKET CHANNEL A REMOTE MESSAGE FOR CLOSE ETC ###

          embed2 = discord.Embed(title='TICKET CREATED', description='Hey Mods 🔴\n```New ticket created,\nRemember that whatever you send in this channel henceforth will be sent to the user who created the ticket. Kindly Maintain the server Decorum .```\n**Thank you**', color=0xFF0000)

          timestamp = datetime.datetime.now()  
          embed5 = discord.Embed(color=0xF1C0B9)
          embed5.add_field(name='**USER INFORMATION**', value=f'```USER NAME - {message.author.name}\n\nUSER ACCOUNT AGE - {round((time.time() - message.author.created_at.timestamp())/86400)} days\n\nTIME OF CREATION - {timestamp.strftime(r"%I:%M %p") } ```')
      
          await m1.send(embed=embed2)
          await m1.send(embed=embed5)


          ### BOT LOGS ### WHERE THE LOGGINGS WILL TAKE PLACE 
              
          ch = await bot.fetch_channel(paste your log channel id with brackets)
              
          embed=discord.Embed(title='TICKET CREATED',description=f'New ticket created by user {message.author.name}, [CLICK ME](https://discord.com/channels/{gd.id}/{m1.id}) to access ticket', color =0x00FF00)
              
          await ch.send(embed=embed)

  except Exception as e:
    print(e)



@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"Hi"))
  print(f"Logged in as {bot.user.name}")

keep_alive()


bot.run(os.environ['BOT KEY'])
