from discordwebhook import Discord

def discordNotify(url, message):
    discord = Discord(url=url)
    discord.post(content=message)
