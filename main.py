import os
import dotenv
import discord
from responses import get_response

# retrieve discord token
dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# inital bot setup
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

# message functionality
async def send_message(message: discord.Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# bot starup handling
@client.event
async def on_ready() -> None:
    print('GMCD is now online and at your service!')

# incoming message handling
@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
        
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

@client.event
async def on_member_join(member):
    channel = client.get_channel(1202511857370275881)
    embed=discord.Embed(title="Welcome!",description=f"How's it going, {member.mention}?")
    await channel.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1203983556607610901:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, name='Member')
        elif payload.emoji.name == '🟢':
            role = discord.utils.get(guild.roles, name='Events')
        elif payload.emoji.name == '🟠':
            role = discord.utils.get(guild.roles, name='Competing')
        else:
            role = None
            print(payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("role added!")
            else:
                print("memeber not found :(")
        else:
            print("role not found :(")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1203983556607610901:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, name='Member')
        elif payload.emoji.name == '🟢':
            role = discord.utils.get(guild.roles, name='Events')
        elif payload.emoji.name == '🟠':
            role = discord.utils.get(guild.roles, name='Competing')
        else:
            role = None
            print(payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("role added!")
            else:
                print("memeber not found :(")
        else:
            print("role not found :(")

# main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
