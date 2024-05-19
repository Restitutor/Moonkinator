#!/home/onfim/no_sync/TTS/venv/bin/python
#!/usr/bin/env python3
from collections import defaultdict
import discord
import re
from wrapper import interact_with_process
from typing import AsyncGenerator
import logging

bot = discord.Bot(
    intents=discord.Intents.none()
    | discord.Intents.message_content
    | discord.Intents.guild_messages
)

all_state = defaultdict(str)


async def play(state: AsyncGenerator, text: str) -> tuple[str, AsyncGenerator]:
    if text == "start":
        new_state = interact_with_process("./game.py")
        output = await new_state.asend(None)
    else:
        output = await state.asend(text)
        new_state = state

    return output.strip(), new_state


@bot.event
async def on_message(message):
    # Limit to people in guilds
    if message.author.bot or type(message.author) is not discord.member.Member:
        return

    # Remove non letters
    text = re.sub(r"[^a-z]+", "", message.clean_content.lower())
    user = message.author.id

    if "listakinator" in text:
        with open('listPlayers.txt') as f:
            players = f.read().replace('\n', ', ')
        await message.reply(players)
        return

    if text not in {"yes", "no", "start"}:
        return

    if user not in all_state and text != "start":
        return

    try:
        output, all_state[user] = await play(all_state[user], text)
    except StopAsyncIteration:
        del all_state[user]
    except Exception as e:
        logging.exception(e)  # Invalid response. Skip.
    else:
        if not output:
            output = "You found a bug! Tell Res and Moon"
            del all_state[user]
        await message.reply(output)


@bot.event
async def on_ready():
    print("Started")
