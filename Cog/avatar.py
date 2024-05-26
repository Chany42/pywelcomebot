import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='avatar', help='Belirtilen kullanıcının avatarını gösterir')
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        await ctx.send(member.avatar_url)

def setup(bot):
    bot.add_cog(Avatar(bot))
