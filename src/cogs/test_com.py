"""
A collection of test commands for debugging

Should be disabled in prod
"""

from discord.ext import commands


class Test(commands.Cog):
    """Test commands for debugging"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def user_id(self, ctx):
        print(ctx.author.id)

    @commands.command()
    async def test_get_user(self, ctx):
        Id = ctx.author.id
        user = self.bot.get_user(Id)
        if user:
            print(user.id),
        else:
            print("failed")

    @commands.command()
    async def members(self, ctx):
        for u in self.bot.get_all_members():
            print(u.id)


def register(bot: commands.Bot):
    bot.add_cog(Test(bot))
