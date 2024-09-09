import discord

# YOUR TOKEN DISCORD
token = ""

# Message à envoyer aux amis
message = '''
discord.gg/black-gold
'''

client = discord.Client()

# Event
@client.event
async def on_connect():
    user_messaged = 0  # User counter

    # friend loop
    for user in client.user.friends:
        try:
            # Send message to every friend
            await user.send(message)
            print(f"message sent to : {user.name}")
            user_messaged += 1 
        except Exception as e:
            print(f"error {user.name}: {str(e)}")
            pass
    
    # Displaying the total number of users
    print(f"\n\n\n{user_messaged} message sent")

client.run(token, bot=False)
