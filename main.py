
"""
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
print(f"TOKEN lu : {TOKEN}")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class PochiBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=1427718161884774450
        )

    async def setup_hook(self):
        await self.tree.sync()
        print("Les commandes slash sont synchronisées")

bot = PochiBot()

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.tree.command(name="mood", description="Vérifie si ton Pochi est en forme")
async def mood(interaction: discord.Interaction):
    await interaction.response.send_message("Ton Pochi est en pleine forme !")

bot.run(TOKEN)


PROJET EN PYTHON (OBSOLETE)


"""



