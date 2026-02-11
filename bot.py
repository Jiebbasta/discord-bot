import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

teams = {
    "Kangaroo 🦘": """### [__**Kangaroo**__](https://op.gg/it/lol/multisearch/euw?summoners=Jiebbasta%231512%2Cchimeminister%23roam%2Cdlwlrma0715%23LJE%2CValkyriaX%23fury%2C恨比爱长久%23CHN%2CPRIDE%23XIII%2Csimocat06%23EUW)
- **Eddifier/Yuno** *(chimeminister/PRIDE)* <:Top:1471188682613719232>
- **Jiebbasta** <:Jungle:1471188589617479690>
- **Tronix** *(dlwlrma0715)* <:Mid:1471188659545051156>
- **Iuty** *(恨比爱长久)* <:Bot:1471188539717849109>
- **Nina/Simocat** *(ValkyriaX)* <:Support:1471188624207904900>""",

    "Raccoons 🦝": """### [__**Raccoons**__](https://op.gg/it/lol/multisearch/euw?summoners=Ethan%23nooob%2CC0STA%236432%2CLoganniere0366%23PRTS%2Craguzzo2%23EUW%2Cgaru%235573)
- **Loganniere** <:Top:1471188682613719232>
- **Garu** <:Jungle:1471188589617479690>
- **Raguzzo** <:Mid:1471188659545051156>
- **Costa** <:ADC:965006363677835274>
- **Ethan** <:Support:729065102321385566>""",

    "Dolphins 🐬": """### [__**Dolphins**__](https://op.gg/it/lol/multisearch/euw?summoners=PSICOPATICO%23SANGU%2CGadix1900%23ITALY%2CSkrall09%23EUW%2Cniekas%23goat%2Cthevoicessaymeow%23meow)
- **Skrall** <:Top:1471188682613719232>
- **Gadix** <:Jungle:1471188589617479690>
- **Kerrel** *(TheVoicesSayMeow)* <:Mid:1471188659545051156>
- **Nebbia** *(PSICOPATICO)* <:ADC:965006363677835274>
- **Niekas** <:Support:729065102321385566>""",

    "Caimans 🐊": """### [__**Caimans**__](https://op.gg/it/lol/multisearch/euw?summoners=caimanosudatoII%23EUW%2CWaxflight%23EUW%2CLemonBuck%23EUW%2CBl00DK1lleR%23EUW)
- *Assente* <:Top:1471188682613719232>
- **Thomas** *(caimanosudatoII)* <:Jungle:1471188589617479690>
- **Waxflight** <:Mid:1471188659545051156>
- **Gabox** *(Bl00DK1lleR)* <:ADC:965006363677835274>
- **Ale** *(LemonBuck)* <:Support:729065102321385566>""",

    "Octopus 🐙": """### [__**Octopus**__](https://op.gg/it/lol/multisearch/euw?summoners=판드레+바루스+원챔%23777%2COphiocordyceps98%23ANT%2CPocketcat%23kat%2Cmotivationless%23shiva%2CW+J+K+Long%23EUW)
- **Carletto** *(motivationless)* <:Top:1471188682613719232>
- **MastroMisciu** *(W J K Long)* <:Jungle:1471188589617479690>
- **Pandre** *(판드레 바루스 원챔)* <:Mid:1471188659545051156>
- **Ren** *(Pocketcat)* <:ADC:965006363677835274>
- **Smilmito** *(Ophiocordyceps)* <:Support:729065102321385566>""",

    "Phoenix 🐦‍🔥": """### [__**Phoenix**__](https://op.gg/it/lol/multisearch/euw?summoners=buckati%23ITAS%2CPlsPeelMe%23adc%2CSheolded%23ITAS%2CTheFaKeKeria%23chill%2CSinonJason204%230069)
- **Buckati** <:Top:1471188682613719232>
- **Pablitos** *(Sheolded)* <:Jungle:1471188589617479690>
- **Darius** *(TheFakeKeria)* <:Mid:1471188659545051156>
- **MrY/Darius** *(PlsPeelMe/TheFakeKeria)* <:ADC:965006363677835274>
- **Sinon/Darius** *(TheFakeKeria)* <:Support:729065102321385566>""",

    "Bulls 🐂": """### [__**Bulls**__](https://op.gg/it/lol/multisearch/euw?summoners=babybroccol%23CKM%2CSCIPPO%231819%2CARANDLE9%23CKM%2CZore%23zore%2CLelou+Pendragon%23EUW%2C+il+devastatore%23eup%2C)
- **Sysma** *(babybroccol)* <:Top:1471188682613719232>
- **Scippo** <:Jungle:1471188589617479690>
- **Zore/Davide** *(Il Devastatore)* <:Mid:1471188659545051156>
- **Genfryx/Zore** *(Lelou Pendragon)* <:ADC:965006363677835274>
- **Arandle** <:Support:729065102321385566>""",

    "Foxes 🦊": """### [__**Foxes**__](https://op.gg/it/lol/multisearch/euw?summoners=baulo%23euw%2Csuperzilvietta%23EUW%2CBiankoniglio%23pdpm%2CSoulTaxCollector%23GVN%2CReira%23ITA%2Cdarkroxas1998%23euw)
- **Roxas** <:Top:1471188682613719232>
- **Bianco** *(Biankoniglio)* <:Jungle:1471188589617479690>
- **SoulTax/Reira/Baulo** <:Mid:1471188659545051156>
- **Silvia** *(superzilvietta)* <:ADC:965006363677835274>
- **Bianco/SoulTax/Baulo** *(Biankoniglio)* <:Support:729065102321385566>""",

    "Centaurs 🐎": """### [__**Centaurs**__](https://op.gg/it/lol/multisearch/euw?summoners=ShαdΘw%23suuus%2C+Kørø+Sensei%23EUW%2C+motivationless%23shiva%2C+CHRISTIAN+DIORE%23EUW%2C+AK47stylish%23EUW%2C)
- **Kina** *(Kørø Sensei)* <:Top:1471188682613719232>
- **Carletto** *(motivationless)* <:Jungle:1471188589617479690>
- **Sirim** *(AK47stylish)* <:Mid:1471188659545051156>
- **Shadow** <:ADC:965006363677835274>
- **StillingLove** *(CHRISTIAN DIORE)* <:Support:729065102321385566>""",

    "Bats 🦇": """### [__**Bats**__](https://op.gg/it/lol/multisearch/euw?summoners=VitoMargarito%239640%2Cfreddy15153%23EUW%2CCappelloDiPaglia%23ONP%2CLadyB0506%23euw%2CJoyBoy%23Luch%C3%AC)
- **VitoMargarito** <:Top:1471188682613719232>
- **Barbarossa** *(CappelloDiPaglia)* <:Jungle:1471188589617479690>
- **JoyBoy** <:Mid:1471188659545051156>
- **Lady** <:ADC:965006363677835274>
- **Freddy** <:Support:729065102321385566>"""
}

class TeamMenu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label=name, description=f"Visualizza {name}")
            for name in teams.keys()
        ]
        super().__init__(placeholder="Seleziona un team...", options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(teams[self.values[0]], ephemeral=True)

class TeamView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(TeamMenu())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot online: {bot.user}")

@bot.tree.command(name="teams", description="Mostra i team con menu a tendina")
async def teams_cmd(interaction: discord.Interaction):
    await interaction.response.send_message("🔽 **Seleziona un team:**", view=TeamView(), ephemeral=True)

import os
bot.run(os.getenv("DISCORD_TOKEN"))
