import discord
import responces

TOKEN = 'MTE5MTY0NzM2NzMyMjE1MzAwMA.GBks-w.on91B2RCmJbIJm4QojYR9DQT6fKDcv7TGh2jLc'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


async def send_message(channel_id, message):
    try:
        channel = client.get_channel(channel_id)
        if channel:
            await channel.send(message)
    except Exception as e:
        print(e, " HELP")


def run_discord_bot():

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}'.format())
        channelID = 929288419908153394
        user_id = 342830408800534529  # Replace with the actual User ID of Izokia
        msg = f'<@{user_id}> Check the stream you got a shiny!'  # Mention the user by their ID
        await send_message(channelID, msg)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

    client.run(TOKEN)
