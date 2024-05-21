#!/usr/bin/env python3
import asyncio
from collections import defaultdict
import discord
import re
from wrapper import interact_with_process
from typing import AsyncGenerator
import logging
import shutil

bot = discord.Bot(
    intents=discord.Intents.none()
    | discord.Intents.message_content
    | discord.Intents.guild_messages
)

all_state = defaultdict(str)

CYCY = 1168452148049231934
EITIFRIE = 804393955533914142
MOON = 955864224092012644
RES = 459147358463197185
ADMINS = {CYCY, EITIFRIE, MOON, RES}


async def run_git_pull() -> str:
    process = await asyncio.create_subprocess_exec(
        "git",
        "pull",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd="repository",
    )

    stdout, stderr = await process.communicate()
    shutil.copy("repository/game.py", "game.py")
    await asyncio.create_subprocess_shell("./listPlayers.sh > ./listPlayers.txt")

    if stderr:
        logging.error(stderr)

    return stdout.decode().strip()


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

    if "listakinator" in text:
        with open("listPlayers.txt") as f:
            players = f.read().replace("\n", ", ")
        await message.reply(players)
        return

    user = message.author.id
    if "updategame" in text:
        if user in ADMINS:
            status = await run_git_pull()
            await message.reply("Checked for updates.\n" + status)
        else:
            await message.reply("You are not an admin.")
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
    logger.info("Started")


bot.run("TOKEN")
