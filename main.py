import discord

# YOUR TOKEN DISCORD
token = ""

# Message à envoyer aux amis
message = '''
discord.gg/hackteur
'''

client = discord.Client()

@client.event
async def on_connect():
    user_messaged = 0  # User counter

    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"message sent to : {user.name}")
            user_messaged += 1 
        except Exception as e:
            print(f"error {user.name}: {str(e)}")
            pass
    
    print(f"\n\n\n{user_messaged} message sent")

client.run(token, bot=False)
