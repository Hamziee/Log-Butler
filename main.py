from dotenv import load_dotenv
load_dotenv()
token = os.getenv('token')

import selfcord

bot = selfcord.Bot(prefixes=["$#$"])

@bot.on("ready")
async def ready(time):
    print(f"Connected To {bot.user} \nStartup took {time:0.2f} seconds")

@bot.on("message")
async def stuff(message):
    print(f"[GUILD ID: {message.guild.id}] | [AUTHOR: {message.author.id} - {message.author}] = {message.content}")

bot.run(token)