from discord.ext import commands
import discord
import requests
import time


bot = commands.Bot(command_prefix='/',
                   description='Get Bus Notifcations from NextBus API')

@bot.command(pass_context=True)
async def start(ctx):
    if ctx.message.channel.is_private:
        await bot.say("""Hello!\nI'm a Discord Bot that can give you bus time notifications!\nLet's start!\nUse /add to add a notification!""")
    else:
        await bot.say("Sorry, I can't help you here. Please PM me!")


@bot.command(pass_context=True)
async def add(ctx):
    await bot.say('Which Bus System do you use?')

    system_choice = await bot.wait_for_message(
        author=ctx.message.author, timeout=300)
    if not system_choice:
        await bot.say('Bot timed out and closed the connection.')
        return
    found_busses = []

    for bus in requests.get('http://webservices.nextbus.com/service/publicJSONFeed?command=agencyList').json()['agency']:
        for attribute in bus:
            if system_choice.content.lower() in bus[attribute].lower():
                found_busses.append(bus)
                break

    await bot.say('I found {} bus system(s) matching your search.'.format(len(found_busses)))

    if len(found_busses) != 0:
        await bot.say('\n'.join('%s - %s' % t for t in zip(range(1, len(found_busses) + 2), [d['title'] for d in found_busses])))
        await bot.say('Choose a bus system by number.')
        choice = await bot.wait_for_message(
            author=ctx.message.author, timeout=300)
        if not choice.content:
            await bot.say('Bot timed out and closed the connection.')
        try:
            bus_system = found_busses[int(choice.content) - 1]
            await bot.say('You selected {}!'.format(bus_system['title']))
        except Exception:
            await bot.say("That's not a valid choice.")
            return

        await bot.say('Which Line do you use?')

        line_choice = await bot.wait_for_message(
            author=ctx.message.author, timeout=300)

        if not line_choice:
            await bot.say('Bot timed out and closed the connection.')
            return

        lines = requests.get(
            'http://webservices.nextbus.com/service/publicJSONFeed?command=routeList&a={}'.format(bus_system['tag'])).json()['route']
        found_lines = []

        for line in lines:
            if line_choice.content.upper() in line['tag']:
                found_lines.append(line)

        await bot.say('I found {} line(s) matching your search.'.format(len(found_lines)))

        if len(found_lines) != 0:
            await bot.say('\n'.join('%s - %s' % t for t in zip(range(1, len(found_lines) + 1), [d['title'] for d in found_lines])))

            await bot.say('Choose a line by number.')
            choice = await bot.wait_for_message(
                author=ctx.message.author, timeout=300)

            if not choice:
                await bot.say('Bot timed out and closed the connection.')
                return
            try:
                line = found_lines[int(choice.content) - 1]
                await bot.say('You selected {}!'.format(line['title']))
            except Exception:
                await bot.say("That's not a valid choice.")
                return

            await bot.say("When should I give you a notification?\nFor Example:\n'6 30' = 6:30 AM\n'16 30' = 4:30 AM")
            time_choice = await bot.wait_for_message(
                author=ctx.message.author, timeout=300)

            if not time_choice:
                await bot.say('Bot timed out and closed the connection.')
                return


@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('TOKEN')
