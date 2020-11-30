TOKEN = 'YOUR TOKEN HERE'


import colorama, time, os
import discord, asyncio, re

from discord.ext import commands, tasks
from colorama import *

colorama.init()

IP_REGEX = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
NITRO_REGEX = r'discord\.gift\/(.*)'
TOKEN_REGEX = r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}'
PASTEBIN_REGEX = r'pastebin\.com\/\w{8}|pastebin\.com\/raw\/\w{8}'
DOXBIN_REGEX = r'https:\/\/doxbin\.org\/upload\/[a-zA-Z0-9]+'

REGEXS = {
    'IP': IP_REGEX,
    'Nitro': NITRO_REGEX,
    'Token': TOKEN_REGEX,
    'Pastebin': PASTEBIN_REGEX
}

VERSION = 1.0
AUTHOR = 'badaboum#6183'
PREFIX = 'eeeeeeee;d;ed;e'

BANNER = f'''\x1b[2J
{Fore.CYAN}╦ ╦╔═╗  ╔═╗╦═╗╔╦╗╦ ╦  ╔═╗╦╔╗╔╦╔═╗╔═╗╦═╗   {Fore.RED}.{Fore.WHITE} | {Fore.RED}.
{Fore.CYAN}║ ║╚═╗  ╠═╣╠╦╝║║║╚╦╝  ╚═╗║║║║║╠═╝║╣ ╠╦╝ {Fore.WHITE}-(- {Fore.RED}+{Fore.WHITE} -)-
{Fore.MAGENTA}╚═╝╚═╝  ╩ ╩╩╚═╩ ╩ ╩   ╚═╝╩╝╚╝╩╩  ╚═╝╩╚═   {Fore.RED}'{Fore.WHITE} | {Fore.RED}'{Fore.WHITE}
{Fore.GREEN}version {VERSION} {Fore.BLACK}{Style.BRIGHT}-{Fore.GREEN}{Style.NORMAL} by {AUTHOR}
'''

def get_time():
    return time.strftime("%H:%M:%S")

def print_info(message):
    size = os.get_terminal_size().columns + 9
    string = f'{Fore.CYAN}[info]{Fore.WHITE} {message}'
    time_string = get_time()
    print(string + (' ' * (size - (len(string) + len(time_string)))) + time_string)


def print_success(message):
    size = os.get_terminal_size().columns + 9
    string = f'{Fore.GREEN}[success]{Fore.WHITE} {message}'
    time_string = get_time()
    print(string + (' ' * (size - (len(string) + len(time_string)))) + time_string)

def print_failed(message):
    size = os.get_terminal_size().columns + 9
    string = f'{Fore.RED}[failed]{Fore.WHITE} {message}'
    time_string = get_time()
    print(string + (' ' * (size - (len(string) + len(time_string)))) + time_string)

def print_loading(message):
    size = os.get_terminal_size().columns + 9
    string = f'{Fore.CYAN}[loading]{Fore.WHITE} {message}'
    time_string = get_time()
    print(string + (' ' * (size - (len(string) + len(time_string)))) + time_string)

def claim_nitro(code): # 
    print_loading(f'trying to claim \'{code}\'')

    r = str(requests.post(
        f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
        headers={'Authorization': TOKEN},
    ).text).lower()

    if 'this gift has been redeemed already.' in r:
        print_failed('someone got it before us :(')

    elif 'subscription_plan' in r:
        print_success('got it! *ST0NKS*')

    elif 'unknown gift code' in r:
        print_failed('unknown gift code')
    else:
        print_failed('bruh')



print(BANNER)

snipe = commands.Bot(
    description='US Army Sniper',
    command_prefix=PREFIX,
    self_bot=True
)

@snipe.event
async def on_connect():
    snipe.user.name 
    print_success(f'logged in as {snipe.user.name}#{snipe.user.discriminator}')
    print_info('ready to snipe !')

@snipe.event
async def on_message(message):
    message_content = message.content
    message_author = f'{message.author.name}#{message.author.discriminator}'

    ips = re.findall(IP_REGEX, message_content)
    tokens = re.findall(TOKEN_REGEX, message_content)
    pastebins = re.findall(PASTEBIN_REGEX, message_content)
    nitros = re.findall(NITRO_REGEX, message_content)
    doxs = re.findall(DOXBIN_REGEX, message_content)


    if len(doxs) != 0:
        for dox in doxs:
            print_success(f'dox: {dox}')
            print(' ' * (len('[success]') + 1) + f'→ guild name \'{message.guild.name}\'')
            print(' ' * (len('[success]') + 1) + f'→ channel name \'{message.channel.name}\'')       
            print()     

    if len(nitros) != 0:
        for nitro in nitros:
            print_success(f'nitro: discord.gift/{nitro}')
            print(' ' * (len('[success]') + 1) + f'→ guild name \'{message.guild.name}\'')
            print(' ' * (len('[success]') + 1) + f'→ channel name \'{message.channel.name}\'')            
            claim_nitro(nitro)
            print()

    if len(pastebins) != 0:
        for pastebin in pastebins:
            print_success(f'pastebin: {pastebin}')
            print(' ' * (len('[success]') + 1) + f'→ guild name \'{message.guild.name}\'')
            print(' ' * (len('[success]') + 1) + f'→ channel name \'{message.channel.name}\'')            
            print()

    if len(ips) != 0:
        for ip in ips:
            print_success(f'ip address: {ip}')
            print(' ' * (len('[success]') + 1) + f'→ guild name \'{message.guild.name}\'')
            print(' ' * (len('[success]') + 1) + f'→ channel name \'{message.channel.name}\'')       
            print()     

    if len(tokens) != 0:
        for token in tokens:
            print_success(f'token: {token}')
            print(' ' * (len('[success]') + 1) + f'→ guild name \'{message.guild.name}\'')
            print(' ' * (len('[success]') + 1) + f'→ channel name \'{message.channel.name}\'')      
            print()      


    # giveaways, inspired from alucard selfbot src
    if 'giveaway' in message_content.lower():
        if int(message.author.id) == 294882584201003009:
            try:    
                await message.add_reaction("🎉")
            except discord.errors.Forbidden:
                pass
            print_success('reacted to giveaway')
            print(' ' * (len('[success]') + 1) + f'→ guild name \'{message.guild.name}\'')
            print(' ' * (len('[success]') + 1) + f'→ channel name \'{message.channel.name}\'')
            print()

    if f'congratulations <@{snipe.user.id}>' in message_content.lower():
        if int(message.author.id) == 294882584201003009:    
            print_success('giveaway won!')
            print(' ' * (len('[success]') + 1) + f'→ guild name \'{message.guild.name}\'')
            print(' ' * (len('[success]') + 1) + f'→ channel name \'{message.channel.name}\'')
            print()

    if TOKEN in message_content:
        for x in range(10):
            print_info('SOMEONE GOT YOUR TOKEN!!!!!!!!!!!')
            print()


snipe.run(
    TOKEN,
    bot=False,
    reconnect=True
)