# -*- coding: utf-8 -*-

import discord
import random
import datetime
from discord.ext import commands, tasks
import os
import json
#import keep_alive
import math
import asyncio
import async_timeout
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
#from easy_pil import Editor, load_image_async, Font
from discord.utils import get


client = commands.Bot(command_prefix="$", intents=discord.Intents.all(), activity = discord.Activity(type=discord.ActivityType.playing, name="$help"))

@client.event
async def on_ready():
  print("bot is ready")

#filtered words
filtered_words = ["forehead"]


# flags
flagnames = {
  "ad": "Andorra",
    "ae": "United Arab Emirates",
    "af": "Afghanistan",
    "ag": "Antigua and Barbuda",
    "ai": "Anguilla",
    "al": "Albania",
    "am": "Armenia",
    "ao": "Angola",
    "aq": "Antarctica",
    "ar": "Argentina",
    "as": "American Samoa",
    "at": "Austria",
    "au": "Australia",
    "aw": "Aruba",
    "ax": "Aland Islands",
    "az": "Azerbaijan",
    "ba": "Bosnia and Herzegovina",
    "bb": "Barbados",
    "bd": "Bangladesh",
    "be": "Belgium",
    "bf": "Burkina Faso",
    "bg": "Bulgaria",
    "bh": "Bahrain",
    "bi": "Burundi",
    "bj": "Benin",
    "bl": "Saint Barthelemy",
    "bm": "Bermuda",
    "bn": "Brunei",
    "bo": "Bolivia",
    "bq": "Caribbean Netherlands",
    "br": "Brazil",
    "bs": "Bahamas",
    "bt": "Bhutan",
    "bv": "Bouvet Island",
    "bw": "Botswana",
    "by": "Belarus",
    "bz": "Belize",
    "ca": "Canada",
    "cc": "Cocos Islands",
    "cd": "DR Congo",
    "cf": "Central African Republic",
    "cg": "Republic of the Congo",
    "ch": "Switzerland",
    "ci": "Ivory Coast",
    "ck": "Cook Islands",
    "cl": "Chile",
    "cm": "Cameroon",
    "cn": "China",
    "co": "Colombia",
    "cr": "Costa Rica",
    "cu": "Cuba",
    "cv": "Cape Verde",
    "cw": "Curacao",
    "cx": "Christmas Island",
    "cy": "Cyprus",
    "cz": "Czechia",
    "de": "Germany",
    "dj": "Djibouti",
    "dk": "Denmark",
    "dm": "Dominica",
    "do": "Dominican Republic",
    "dz": "Algeria",
    "ec": "Ecuador",
    "ee": "Estonia",
    "eg": "Egypt",
    "eh": "Western Sahara",
    "er": "Eritrea",
    "es": "Spain",
    "et": "Ethiopia",
    "fi": "Finland",
    "fj": "Fiji",
    "fk": "Falkland Islands",
    "fm": "Micronesia",
    "fo": "Faroe Islands",
    "fr": "France",
    "ga": "Gabon",
    "gb": "United Kingdom",
    "gd": "Grenada",
    "ge": "Georgia",
    "gf": "French Guiana",
    "gg": "Guernsey",
    "gh": "Ghana",
    "gi": "Gibraltar",
    "gl": "Greenland",
    "gm": "Gambia",
    "gn": "Guinea",
    "gp": "Guadeloupe",
    "gq": "Equatorial Guinea",
    "gr": "Greece",
    "gs": "South Georgia",
    "gt": "Guatemala",
    "gu": "Guam",
    "gw": "Guinea-Bissau",
    "gy": "Guyana",
    "hk": "Hong Kong",
    "hm": "Heard Island and McDonald Islands",
    "hn": "Honduras",
    "hr": "Croatia",
    "ht": "Haiti",
    "hu": "Hungary",
    "id": "Indonesia",
    "ie": "Ireland",
    "il": "Israel",
    "im": "Isle of Man",
    "in": "India",
    "io": "British Indian Ocean Territory",
    "iq": "Iraq",
    "ir": "Iran",
    "is": "Iceland",
    "it": "Italy",
    "je": "Jersey",
    "jm": "Jamaica",
    "jo": "Jordan",
    "jp": "Japan",
    "ke": "Kenya",
    "kg": "Kyrgyzstan",
    "kh": "Cambodia",
    "ki": "Kiribati",
    "km": "Comoros",
    "kn": "Saint Kitts and Nevis",
    "kp": "North Korea",
    "kr": "South Korea",
    "kw": "Kuwait",
    "ky": "Cayman Islands",
    "kz": "Kazakhstan",
    "la": "Laos",
    "lb": "Lebanon",
    "lc": "Saint Lucia",
    "li": "Liechtenstein",
    "lk": "Sri Lanka",
    "lr": "Liberia",
    "ls": "Lesotho",
    "lt": "Lithuania",
    "lu": "Luxembourg",
    "lv": "Latvia",
    "ly": "Libya",
    "ma": "Morocco",
    "mc": "Monaco",
    "md": "Moldova",
    "me": "Montenegro",
    "mf": "Saint Martin",
    "mg": "Madagascar",
    "mh": "Marshall Islands",
    "mk": "North Macedonia",
    "ml": "Mali",
    "mm": "Myanmar",
    "mn": "Mongolia",
    "mo": "Macau",
    "mp": "Northern Mariana Islands",
    "mq": "Martinique",
    "mr": "Mauritania",
    "ms": "Montserrat",
    "mt": "Malta",
    "mu": "Mauritius",
    "mv": "Maldives",
    "mw": "Malawi",
    "mx": "Mexico",
    "my": "Malaysia",
    "mz": "Mozambique",
    "na": "Namibia",
    "nc": "New Caledonia",
    "ne": "Niger",
    "nf": "Norfolk Island",
    "ng": "Nigeria",
    "ni": "Nicaragua",
    "nl": "Netherlands",
    "no": "Norway",
    "np": "Nepal",
    "nr": "Nauru",
    "nu": "Niue",
    "nz": "New Zealand",
    "om": "Oman",
    "pa": "Panama",
    "pe": "Peru",
    "pf": "French Polynesia",
    "pg": "Papua New Guinea",
    "ph": "Philippines",
    "pk": "Pakistan",
    "pl": "Poland",
    "pm": "Saint Pierre and Miquelon",
    "pn": "Pitcairn Islands",
    "pr": "Puerto Rico",
    "ps": "Palestine",
    "pt": "Portugal",
    "pw": "Palau",
    "py": "Paraguay",
    "qa": "Qatar",
    "re": "Reunion",
    "ro": "Romania",
    "rs": "Serbia",
    "ru": "Russia",
    "rw": "Rwanda",
    "sa": "Saudi Arabia",
    "sb": "Solomon Islands",
    "sc": "Seychelles",
    "sd": "Sudan",
    "se": "Sweden",
    "sg": "Singapore",
    "sh": "Saint Helena, Ascension and Tristan da Cunha",
    "si": "Slovenia",
    "sj": "Svalbard and Jan Mayen",
    "sk": "Slovakia",
    "sl": "Sierra Leone",
    "sm": "San Marino",
    "sn": "Senegal",
    "so": "Somalia",
    "sr": "Suriname",
    "ss": "South Sudan",
    "st": "Sao Tome and Principe",
    "sv": "El Salvador",
    "sx": "Sint Maarten",
    "sy": "Syria",
    "sz": "Eswatini",
    "tc": "Turks and Caicos Islands",
    "td": "Chad",
    "tf": "French Southern and Antarctic Lands",
    "tg": "Togo",
    "th": "Thailand",
    "tj": "Tajikistan",
    "tk": "Tokelau",
    "tl": "Timor-Leste",
    "tm": "Turkmenistan",
    "tn": "Tunisia",
    "to": "Tonga",
    "tr": "Turkey",
    "tt": "Trinidad and Tobago",
    "tv": "Tuvalu",
    "tw": "Taiwan",
    "tz": "Tanzania",
    "ua": "Ukraine",
    "ug": "Uganda",
    "us": "United States",
    "uy": "Uruguay",
    "uz": "Uzbekistan",
    "va": "Vatican City",
    "vc": "Saint Vincent and the Grenadines",
    "ve": "Venezuela",
    "vg": "British Virgin Islands",
    "vi": "United States Virgin Islands",
    "vn": "Vietnam",
    "vu": "Vanuatu",
    "wf": "Wallis and Futuna",
    "ws": "Samoa",
    "xk": "Kosovo",
    "ye": "Yemen",
    "yt": "Mayotte",
    "za": "South Africa",
    "zm": "Zambia",
    "zw": "Zimbabwe"
}

flagemoji = {
  "AD": "🇦🇩",
  "AE": "🇦🇪",
  "AF": "🇦🇫",
  "AG": "🇦🇬", 
  "AI": "🇦🇮", 
  "AL": "🇦🇱", 
  "AM": "🇦🇲", 
  "AO": "🇦🇴", 
  "AQ": "🇦🇶", 
  "AR": "🇦🇷",
  "AS": "🇦🇸", 
  "AT": "🇦🇹", 
  "AU": "🇦🇺", 
  "AW": "🇦🇼", 
  "AX": "🇦🇽", 
  "AZ": "🇦🇿", 
  "BA": "🇧🇦", 
  "BB": "🇧🇧", 
  "BD": "🇧🇩", 
  "BE": "🇧🇪", 
  "BF": "🇧🇫", 
  "BG": "🇧🇬", 
  "BH": "🇧🇭", 
  "BI": "🇧🇮", 
  "BJ": "🇧🇯", 
  "BL": "🇧🇱", 
  "BM": "🇧🇲",
  "BN": "🇧🇳", 
  "BO": "🇧🇴", 
  "BQ": "🇧🇶", 
  "BR": "🇧🇷", 
  "BS": "🇧🇸", 
  "BT": "🇧🇹", 
  "BV": "🇧🇻", "BW": "🇧🇼", "BY": "🇧🇾", "BZ": "🇧🇿", "CA": "🇨🇦", "CC": "🇨🇨", "CD": "🇨🇩", "CF": "🇨🇫", "CG": "🇨🇬", "CH": "🇨🇭", "CI": "🇨🇮", "CK": "🇨🇰", "CL": "🇨🇱", "CM": "🇨🇲", "CN": "🇨🇳", "CO": "🇨🇴", "CR": "🇨🇷", "CU": "🇨🇺", "CV": "🇨🇻", "CW": "🇨🇼", "CX": "🇨🇽", "CY": "🇨🇾", "CZ": "🇨🇿", "DE": "🇩🇪", "DJ": "🇩🇯", "DK": "🇩🇰", "DM": "🇩🇲", "DO": "🇩🇴", "DZ": "🇩🇿", "EC": "🇪🇨", "EE": "🇪🇪", "EG": "🇪🇬", "EH": "🇪🇭", "ER": "🇪🇷", "ES": "🇪🇸", "ET": "🇪🇹", "FI": "🇫🇮", "FJ": "🇫🇯", "FK": "🇫🇰", "FM": "🇫🇲", "FO": "🇫🇴", "FR": "🇫🇷", "GA": "🇬🇦", "GB": "🇬🇧", "GD": "🇬🇩", "GE": "🇬🇪", "GF": "🇬🇫", "GG": "🇬🇬", "GH": "🇬🇭", "GI": "🇬🇮", "GL": "🇬🇱", "GM": "🇬🇲", "GN": "🇬🇳", "GP": "🇬🇵", "GQ": "🇬🇶", "GR": "🇬🇷", "GS": "🇬🇸", "GT": "🇬🇹", "GU": "🇬🇺", "GW": "🇬🇼", "GY": "🇬🇾", "HK": "🇭🇰", "HM": "🇭🇲", "HN": "🇭🇳", "HR": "🇭🇷", "HT": "🇭🇹", "HU": "🇭🇺", "ID": "🇮🇩", "IE": "🇮🇪", "IL": "🇮🇱", "IM": "🇮🇲", "IN": "🇮🇳", "IO": "🇮🇴", "IQ": "🇮🇶", "IR": "🇮🇷", "IS": "🇮🇸", "IT": "🇮🇹", "JE": "🇯🇪", "JM": "🇯🇲", "JO": "🇯🇴", "JP": "🇯🇵", "KE": "🇰🇪", "KG": "🇰🇬", "KH": "🇰🇭", "KI": "🇰🇮", "KM": "🇰🇲", "KN": "🇰🇳", "KP": "🇰🇵", "KR": "🇰🇷", "KW": "🇰🇼", "KY": "🇰🇾", "KZ": "🇰🇿", "LA": "🇱🇦", "LB": "🇱🇧", "LC": "🇱🇨", "LI": "🇱🇮", "LK": "🇱🇰", "LR": "🇱🇷", "LS": "🇱🇸", "LT": "🇱🇹", "LU": "🇱🇺", "LV": "🇱🇻", "LY": "🇱🇾", "MA": "🇲🇦", "MC": "🇲🇨", "MD": "🇲🇩", "ME": "🇲🇪", "MF": "🇲🇫", "MG": "🇲🇬", "MH": "🇲🇭", "MK": "🇲🇰", "ML": "🇲🇱", "MM": "🇲🇲", "MN": "🇲🇳", "MO": "🇲🇴", "MP": "🇲🇵", "MQ": "🇲🇶", "MR": "🇲🇷", "MS": "🇲🇸", "MT": "🇲🇹", "MU": "🇲🇺", "MV": "🇲🇻", "MW": "🇲🇼", "MX": "🇲🇽", "MY": "🇲🇾", "MZ": "🇲🇿", "NA": "🇳🇦", "NC": "🇳🇨", "NE": "🇳🇪", "NF": "🇳🇫", "NG": "🇳🇬", "NI": "🇳🇮", "NL": "🇳🇱", "NO": "🇳🇴", "NP": "🇳🇵", "NR": "🇳🇷", "NU": "🇳🇺", "NZ": "🇳🇿", "OM": "🇴🇲", "PA": "🇵🇦", "PE": "🇵🇪", "PF": "🇵🇫", "PG": "🇵🇬", "PH": "🇵🇭", "PK": "🇵🇰", "PL": "🇵🇱", "PM": "🇵🇲", "PN": "🇵🇳", "PR": "🇵🇷", "PS": "🇵🇸", "PT": "🇵🇹", "PW": "🇵🇼", "PY": "🇵🇾", "QA": "🇶🇦", "RE": "🇷🇪", "RO": "🇷🇴", "RS": "🇷🇸", "RU": "🇷🇺", "RW": "🇷🇼", "SA": "🇸🇦", "SB": "🇸🇧", "SC": "🇸🇨", "SD": "🇸🇩", "SE": "🇸🇪", "SG": "🇸🇬", "SH": "🇸🇭", "SI": "🇸🇮", "SJ": "🇸🇯", "SK": "🇸🇰", "SL": "🇸🇱", "SM": "🇸🇲", "SN": "🇸🇳", "SO": "🇸🇴", "SR": "🇸🇷", "SS": "🇸🇸", "ST": "🇸🇹", "SV": "🇸🇻", "SX": "🇸🇽", "SY": "🇸🇾", "SZ": "🇸🇿", "TC": "🇹🇨", "TD": "🇹🇩", "TF": "🇹🇫", "TG": "🇹🇬", "TH": "🇹🇭", "TJ": "🇹🇯", "TK": "🇹🇰", "TL": "🇹🇱", "TM": "🇹🇲", "TN": "🇹🇳", "TO": "🇹🇴", "TR": "🇹🇷", "TT": "🇹🇹", "TV": "🇹🇻", "TW": "🇹🇼", "TZ": "🇹🇿", "UA": "🇺🇦", "UG": "🇺🇬", "US": "🇺🇸", "UY": "🇺🇾", "UZ": "🇺🇿", "VA": "🇻🇦", "VC": "🇻🇨", "VE": "🇻🇪", "VG": "🇻🇬", "VI": "🇻🇮", "VN": "🇻🇳", "VU": "🇻🇺", "WF": "🇼🇫", "WS": "🇼🇸", "XK": "🇽🇰", "YE": "🇾🇪", "YT": "🇾🇹", "ZA": "🇿🇦", "ZM": "🇿🇲", "ZW": "🇿🇼"
}

countrynames = list(flagnames.values())
flags = list(flagemoji.values())

@client.listen()
async def on_message(message):
  if message.author == client.user:
    return
  if message.author.bot:
    return
  if "party time" in message.content:
    emoji = '<a:swag:1005202356088098876>'
    await message.add_reaction(emoji)
  if "funky" in message.content:
    emoji = '<a:party:1005206123101561035>'
    await message.add_reaction(emoji)
  if message.content.lower() == "heheha":
    emoji = '<a:heheha:1005705172611235881>'
    await message.add_reaction(emoji)
  if "i count money" in message.content.lower():
    await message.channel.send(file=discord.File(r'ICOUNTMONEYICOUNTMONEYICOUNTMONEYICOUNTMONEYICOUNTMONEY.txt'))
    await message.channel.send("https://i1.sndcdn.com/artworks-Ey3W1K16JIdkbjZE-OQrNhQ-t500x500.jpg")
  #filtered words
  for word in filtered_words:
    if word in message.content:
      await message.delete()
  #await client.process_commands(message)
  #the actual stuf
  with open("user.json", "r") as f:
    u = json.load(f)
  if str(message.author.id) not in u:
    u[str(message.author.id)] = {}
    u[str(message.author.id)]["xp"] = 0
    u[str(message.author.id)]["level"] = 1
    with open("user.json", "w") as f:
      json.dump(u, f, indent=4)
  else:
    next_level = math.floor(((math.sqrt((2 * u[str(message.author.id)]["xp"]) + 30625) / 50) - 2.5) + 1)
  
    xp = random.randint(250, 750)
    u[str(message.author.id)]["xp"] += xp
    u[str(message.author.id)]["level"] = (math.sqrt((2 * u[str(message.author.id)]["xp"]) + 30625) / 50) - 2.5
  
    
    # print(next_level)
    # print(math.floor((math.sqrt((2 * u[str(message.author.id)]["xp"]) + 30625) / 50) - 2.5))
    if math.floor((math.sqrt((2 * u[str(message.author.id)]["xp"]) + 30625) / 50) - 2.5) == next_level:
      await message.channel.send(f"{message.author.mention} you leveled up to level {next_level}")
  
    with open("user.json", "w") as f:
      json.dump(u, f, indent=4)
  
  # await client.process_commands(message)

#checking level
@client.command()
async def level(ctx, member: discord.Member = None):
  with open("user.json", "r") as f:
    u = json.load(f)

  if member == None:
    level = str(u[str(ctx.author.id)]["level"])
    next_level = float(level)+1
    dot = level.find(".")
    twodec = math.floor(100 - int(level[dot+1:dot+3]))
    #threedec = math.floor(100 - int(level[dot+3]))
    await ctx.send(f"you are level {math.floor(float(level))}\n{twodec} xp to level {math.floor(float(next_level))}")
  else:
    level = str(u[str(member.id)]["level"])
    next_level = float(level)+1
    dot = level.find(".")
    twodec = math.floor(100 - int(level[dot+1:dot+3]))
    #threedec = 100 - int(level[dot+3])
    await ctx.send(f"{member.mention} is level {math.floor(float(level))}\n{twodec} xp to level {math.floor(float(next_level))}")


#purge command
@client.command(aliases=['p'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=0):
  await ctx.channel.purge(limit=amount)


#kick command
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="no reason provided."):
  try:
    await member.send("you have been kicked from the server. reason provided: " + reason)
  except:
    await ctx.send(member.mention + " has been kicked from the server. reason: " + reason)
  await member.kick(reason=reason)

#invite
@client.command(aliases=['i'])
@commands.has_permissions(kick_members=True)
async def invite(ctx, user):
  user = await client.fetch_user("USER_ID")
  try:
    await user.send("https://discord.gg/tzA6PrNRK6")
  except:
    await ctx.send("the user has their DM settings closed.")

#ban command
@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="no reason provided."):
  try:
    await member.send("you have been banned from the server. reason provided: " + reason)
  except:
    await ctx.send(member.mention + " has been banned from the server. reason: " + reason)
    await member.ban(reason=reason)


#unban command
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_disc = member.split('#')
  for banned_entry in banned_users:
    user = banned_entry.user
    if (user.name, user.discriminator) == (member_name, member_disc):
        await ctx.guild.unban(user)
        await ctx.send(member_name + " has been unbanned!")
        return
  await ctx.send("member was not found")


#muting
@client.command(aliases=['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx, member: discord.Member):
  muted_role = ctx.guild.get_role(840992112631611433)
  await member.add_roles(muted_role)
  await ctx.send(member.mention + " has been muted.")


#unmuting
@client.command(aliases=['um'])
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member: discord.Member):
  muted_role = ctx.guild.get_role(840992112631611433)
  await member.remove_roles(muted_role)
  await ctx.send(member.mention + " has been unmuted.")


#error handling
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
      author = ctx.author
      await ctx.send(author.mention + ", you can't do that!")
  elif isinstance(error, commands.MissingRequiredArgument):
      author = ctx.author
      await ctx.send(author.mention +
       ", please enter all the required arguments.")
  else:
    raise error


#whois
@client.command(aliases=['user', 'info'])
async def whois(ctx, member: discord.Member = None):
  if member == None:
    embed = discord.Embed(title=ctx.author.name, description=ctx.author.mention)
    embed.add_field(name="ID:", value=ctx.author.id, inline=True)
    embed.add_field(name="account created:", value=datetime.datetime.strftime(ctx.author.created_at, "%a %b %-d %X %p %Y"), inline=True)
    embed.add_field(name="joined server at:", value=datetime.datetime.strftime(ctx.author.joined_at, "%a %b %-d %X %p %Y"), inline=True)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(icon_url=ctx.author.avatar.url, text=f"requested by {ctx.author.name}")
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title=member.name, description=member.mention)
    embed.add_field(name="ID:", value=member.id, inline=True)
    embed.add_field(name="account created:",
        value=datetime.datetime.strftime(member.created_at, "%a %b %-d %X %p %Y"),
        inline=True)
    embed.add_field(name="joined server at:",
        value=datetime.datetime.strftime(member.joined_at, "%a %b %-d %X %p %Y"),
        inline=True)
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(icon_url=ctx.author.avatar.url,
         text=f"requested by {ctx.author.name}")
    await ctx.send(embed=embed)

#minion image generator
minionGeneratorImgs = [   'https://i.imgur.com/NQrJL5r.jpeg',
  'https://imgur.com/a/SeqPULf.jpeg',     'https://i.pinimg.com/originals/e1/3d/e0/e13de00443cede6743ae6be14632dcf9.jpg',                    'https://i.pinimg.com/originals/8f/e2/d4/8fe2d41f9e14bca2128627156e847a91.jpg',
  'https://www.cartoonbrew.com/wp-content/uploads/2022/06/Minions-1-150x150.jpg',
  'https://www.cartoonbrew.com/wp-content/uploads/2022/07/minions_riseofgru_bo-150x150.jpg', 'https://i.pinimg.com/736x/c4/8c/24/c48c248c161d8994705646671b8ed8d3.jpg', 'https://i.pinimg.com/550x/f5/6e/23/f56e235046740d159b710ff4daf972bc.jpg', 'https://i.pinimg.com/originals/4b/00/b8/4b00b8ac5f3d44aa272f3e8eea5e1e97.jpg', 'https://static.wikia.nocookie.net/despicableme/images/9/93/Whaaat.jpg/revision/latest/scale-to-width-down/250?cb=20130706041544',
  'https://redefined.s3.us-east-2.amazonaws.com/wp-content/uploads/2020/02/05141935/minions_screenshot-585x585.jpg', 'https://i.pinimg.com/originals/22/66/1c/22661c4c8fcc6e0c7f50f28217d20f4d.jpg'
]


@client.command()
async def minion(ctx):
  #embed = discord.Embed(color=discord.Colour.yellow())
  num = random.randint(0, len(minionGeneratorImgs)-1)
  random_link = minionGeneratorImgs[num]
  #embed.set_image(url=random_link)
  #await ctx.send(embed=embed)
  await ctx.send(random_link)

#I COUNT MONEY
#@client.command()
#async def swag(ctx):
  #await ctx.send(file=discord.File(r'stuff/b.mp3'))

#compliment feature
compliments = ['you are very cool', "you're awesome", "you are insane at game pigeon", "you are amazing", "youre very dripy", "you are cooler than otto the minion", "you = 😎😎😎😎🥶"]
  
@client.command()
async def compliment(ctx, member: discord.Member):
  if member.id == 708076224366248017:
    await ctx.send(f"{member.mention} you are the absolute greatest person in the entire world and you are so amazing and great at everything")
  else:
    num = random.randint(0, len(compliments)-1)
    random_compliment = compliments[num]
    await ctx.send(f"{member.mention}, {random_compliment}")

#avatar
@client.command()
async def avatar(ctx, member : discord.Member = None):
  if member == None:
    url=ctx.author.avatar.url
    await ctx.send(url)
  else:
    url=member.avatar.url
    await ctx.send(url)

# spiffy bot hacked
@client.command()
async def say(ctx, *, msg):
  if msg == "@everyone":
    await ctx.send('no')
  else:
    await ctx.send(msg)

# KING BOB
@client.command()
async def bob(ctx):
  await ctx.send(file=discord.File(r'stuff/kingbob.mp4'))

# poll
@client.command()
async def poll(ctx, *, message):
  #if len(options) <= 1:
            #await ctx.channel.send('you need more than one option to make a poll!')
            #return
  #if len(options) > 10:
    #await ctx.channel.send('you cannot make a poll with more than 10 options!')
    #return
  #if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
    #reactions = ['✅', '❌']
  #else:
    #reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
  emb = discord.Embed(title=" poll ", description=f"{message}")
  msg = await ctx.channel.send(embed=emb)
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')


#flag modes
@client.command()
async def modes(ctx):
  embed = discord.Embed(title = "what mode would you like to play?", description="1️⃣: singleplayer \n 2️⃣: multiplayer \n 3️⃣: practice")
  msg = await ctx.channel.send(embed=embed)
  await msg.add_reaction('1️⃣')
  await msg.add_reaction('2️⃣')
  await msg.add_reaction('3️⃣')
  def check(reaction, user):
    return str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣'] and user != client.user and user == ctx.author and reaction.message == msg
  try:
    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
  except asyncio.TimeoutError:
    await ctx.channel.send("timed out")
    return
  else:
    count = 0
    if str(reaction.emoji) == '1️⃣':
      global numbcorrect
      numbcorrect = 0
      global count1
      count1 = 0
      for i in range(1, 11):
        num1 = random.randint(0, len(countrynames)-1)
        country = countrynames[num1]
        flag = flags[num1]
        await ctx.send(f"**round {i} out of 10: **")
        await ctx.send(flag)
        countrylower = [each_string.lower() for each_string in countrynames]
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel
        global cor
        cor = False
        try:
          async with async_timeout.timeout(12):
            while True:
              msg = await client.wait_for("message", check=check)
              if msg.content.lower() == country.lower():
                await msg.add_reaction('✅')
                cor = True
                numbcorrect += 1
                await asyncio.sleep(12-count1)
                continue
              elif msg.content.lower() != country.lower():
                pass
        except asyncio.TimeoutError:
          if cor == True:
            continue
          else:
            await ctx.send(f"the correct answer was **{country}**.")
            continue
      results1 = discord.Embed(title="game ended", description=f"**final score** \n {numbcorrect} - {ctx.author.name}")
      await ctx.send(embed=results1)
    elif str(reaction.emoji) == '2️⃣':
      global count2
      count2 = 0
      await ctx.send(f"{ctx.author.mention}, please @ the users you would like to play the multiplayer game with, or type `everyone` for anyone to be able to play!")
      check = lambda m:m.author == ctx.author and m.channel == ctx.channel
      playmode = await client.wait_for("message", check=check, timeout=20.0)
      try:
        if playmode.content.lower() == "everyone":
          scoredict = {}
          for i in range(1, 11):
            num1 = random.randint(0, len(countrynames)-1)
            country = countrynames[num1]
            flag = flags[num1]
            await ctx.send(f"**round {i} out of 10: **")
            await ctx.send(flag)
            countrylower = [each_string.lower() for each_string in countrynames]
            check = lambda m: m.channel == ctx.channel
            await asyncio.sleep(1)
            global core
            core = False
            try:
              async with async_timeout.timeout(12):
                while True:
                  msg = await client.wait_for("message", check=check)
                  if msg.content.lower() == country.lower():
                    await msg.add_reaction('✅')
                    if ctx.author.name in scoredict:
                      scoredict2[ctx.author.name] += 1
                    else:
                      scoredict[ctx.author.name] = 0
                      scoredict[ctx.author.name] += 1
                    core = True
                    await asyncio.sleep(10-count2)
                    continue
                  if msg.content.lower() in countrylower and msg.content.lower() != country.lower():
                      await msg.add_reaction('❌')
                  elif msg.content.lower() != country.lower():
                    pass
            except asyncio.TimeoutError:
              if core == True:
                continue
              else:
                await ctx.send(f"the correct answer was **{country}**.")
                continue
          scores2 = ''
          for key, value in scoredict2.items():
            scores2 += f"{key} - {value}"
          results3 = discord.Embed(title="game finished", description=f"**final scores** \n {scores2}")
          await ctx.send(embed=results3)
        else:
          scoredict2 = {}
          for i in range(1, 11):
            num1 = random.randint(0, len(countrynames)-1)
            country = countrynames[num1]
            flag = flags[num1]
            await ctx.send(f"**round {i} out of 10: **")
            await ctx.send(flag)
            countrylower = [each_string.lower() for each_string in countrynames]
            check = lambda m: m.author in playmode.mentions or m.author == ctx.author and m.channel == ctx.channel
            await asyncio.sleep(1)
            global corec
            corec = False
            try:
              async with async_timeout.timeout(12):
                while True:
                  msg = await client.wait_for("message", check=check)
                  if msg.content.lower() == country.lower():
                    await msg.add_reaction('✅')
                    if ctx.author.name in scoredict2:
                      scoredict2[ctx.author.name] += 1
                    else:
                      scoredict2[ctx.author.name] = 0
                      scoredict2[ctx.author.name] += 1
                    corec = True
                    await asyncio.sleep(10-count2)
                    continue
                  if msg.content.lower() in countrylower and msg.content.lower() != country.lower():
                      await msg.add_reaction('❌')
                  elif msg.content.lower() != country.lower():
                    pass
            except asyncio.TimeoutError:
              if corec == True:
                continue
              else:
                await ctx.send(f"the correct answer was **{country}**.")
                continue
          scores = ''
          for key, value in scoredict2.items():
            scores += f"{key} - {value}"
          results3 = discord.Embed(title="game finished", description=f"**final scores** \n {scores}")
          await ctx.send(embed=results3)
      except asyncio.TimeoutError:
        await ctx.send("timed out")

    elif str(reaction.emoji) == '3️⃣':
      global var 
      var = 2
      global streak
      streak = 0
      global numcorrect
      numcorrect = 0 
      global totalplayed
      totalplayed = 0
      streaks = []
      await ctx.send(f"{ctx.author.mention}, your flag practice is starting. type `flag` to send a flag and begin!")
      while var == 2:
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel
        mesa = await client.wait_for("message", check=check)
        if mesa.content.lower() == "stop":
          streaks.append(streak)
          if streaks:
            beststreak = max(streaks)
          else:
            beststreak = 0
          results = discord.Embed(title="practice ended", description=f"\n **your stats** \n highest streak: `{beststreak}` \n total number correct: `{numcorrect}` \n total played: `{totalplayed}` \n")
          results.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
          await ctx.send(embed=results)
          var = 0
          return var
        elif mesa.content.lower() == "flag":
          totalplayed += 1 
          num1 = random.randint(0, len(countrynames)-1)
          country = countrynames[num1]
          flag = flags[num1]
          await ctx.send(flag)
          answer = [country]
          countrylower = [each_string.lower() for each_string in countrynames]
          check = lambda m: m.author == ctx.author and m.channel == ctx.channel
          while True:
            try:
              msg = await client.wait_for("message", check=check, timeout=100.0)
              if msg.content.lower() in countrylower and msg.content.lower() != country.lower():
                streaks.append(streak)
                streak = 0
                await msg.add_reaction('❌')
              if msg.content.lower() == country.lower():
                numcorrect += 1
                streak += 1
                await msg.add_reaction('✅')
                #check = lambda m: m.author == ctx.author and m.channel == ctx.channel
                #mesat = await client.wait_for("message", check=check)
                #if msg.content.lower() == "stop":
                  #await ctx.send("stopped")
                  #var = 0
                  #return var
                #else:
                break
              elif msg.content.lower() == "answer":
                streaks.append(streak)
                streak = 0
                await ctx.send(f"the correct answer is **{answer[0]}**.")
                answer.clear()
                #check = lambda m: m.author == ctx.author and m.channel == ctx.channel
                #mesaw = await client.wait_for("message", check=check)
                #if mesaw.content.lower() == "stop":
                  #await ctx.send("stopped")
                  #var = 0
                  #return var
                #else:
                break
              elif msg.content.lower() == "stop":
                streaks.append(streak)
                if streaks:
                  beststreak = max(streaks)
                else:
                  beststreak = 0
                results = discord.Embed(title="practice ended", description=f"\n **your stats** \n highest streak: `{beststreak}` \n total number correct: `{numcorrect}` \n total played: `{totalplayed}` \n")
                results.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
                await ctx.send(embed=results)
                var = 0
                return var 
            except asyncio.TimeoutError:
              streaks.append(streak)
              if streaks:
                beststreak = max(streaks)
              else:
                beststreak = 0
              results = discord.Embed(title="practice ended due to inactivity", description=f"\n **your stats** \n highest streak: `{beststreak}` \n total number correct: `{numcorrect}` \n total played: `{totalplayed}` \n")
              results.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
              await ctx.send(embed=results)
              var = 0
              return var
    else:
      pass


# flag ref
@client.command()
async def flagof(ctx, *, country):
  if country == "minion":
    await ctx.send("https://preview.redd.it/hcbkuvokc9y11.png?auto=webp&s=25a6bf5e20e992201f197db8b8d7fa69024f97b0")
  else:
    countrykeylist = list(flagnames.keys())
    countrylist = list(flagnames.values())
    for i in range (len(countrylist)):
      countrylist[i] = countrylist[i].lower()
    country1 = countrylist.index(country)
    countrycode = countrykeylist[country1]
    await ctx.reply(flagemoji[countrycode.upper()])

# feedback
@client.command()
async def feedback(ctx, *, feedback):
  user = client.get_user(708076224366248017)
  await user.send(f"feedback from {ctx.author.mention}: {feedback}")
  await ctx.send(f"{ctx.author.mention}, your feedback has been received. thank you!")

# mass shut down
@client.command()
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
  await ctx.send('shutting down...')
  await exit()

# minion img manipulation
@client.command()
async def makeminion(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author
  minion = Image.open("Images/makeminion.jpg")
  asset = user.avatar.with_size(128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((175, 175))
  minion.paste(pfp, (65,100))
  minion.save("Images/newminion.jpg")
  await ctx.send(file = discord.File("Images/newminion.jpg"))

# megamind
@client.command()
async def megamind(ctx, *, words):
  megamind = Image.open("Images/megamind.png")
  width,height = megamind.size
  font = ImageFont.truetype("impact.ttf", 80)
  draw = ImageDraw.Draw(megamind)
  text = words
  w = draw.textlength(text, font=font)
  h = 80
  draw.text(((megamind.width-w)/2, 20), text, (255,255,255), font=font)
  megamind.save("Images/newmegamind.png")
  await ctx.send(file = discord.File("Images/newmegamind.png"))

# calculator
@client.command(aliases=['calc'])
async def calculate(ctx, *, expression):
  try:
    result = eval(expression)
    await ctx.send(result)
  except Exception as e:
    await ctx.send('Invalid expression!')

# reminders
@client.command()
async def remind(ctx, time_minutes, *, reminder_text):
  time_minutes = float(time_minutes)
  await asyncio.sleep(time_minutes * 60)
  await ctx.send(f'{ctx.author.mention}: {reminder_text}')

TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
