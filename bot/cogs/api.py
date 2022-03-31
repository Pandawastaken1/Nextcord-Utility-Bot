import os, nextcord, dotenv
from aiohttp import ClientSession
from nextcord.ext import commands, tasks

dotenv.load_dotenv()

class API(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.joke_api_key = os.getenv("JOKE_API")

    @commands.command(
        name="dadjoke",
        description="Send a dad joke!",
        aliases=['dadjokes']
    )
    async def dadjoke(self, ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': self.joke_api_key
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")


def setup(bot):
    bot.add_cog(API(bot))