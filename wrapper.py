import asyncio
from asyncio.subprocess import PIPE
from typing import Generator


async def read_lines(stream: asyncio.StreamReader) -> str:
    lines = ""
    while True:
        try:
            line = await asyncio.wait_for(stream.readline(), timeout=0.1)
        except asyncio.TimeoutError:
            break

        if not line:
            break
        lines += line.decode()
    return lines


async def interact_with_process() -> Generator[str, str, None]:
    # Start the subprocess
    process = await asyncio.create_subprocess_exec(
        "python", "./game.py", stdin=PIPE, stdout=PIPE
    )

    stdout = await read_lines(process.stdout)
    # Initial output from the subprocess

    try:
        # Await the next input from the caller
        user_input = yield stdout
        while True:
            if process.returncode is not None or user_input == "STOP":
                break
    
            # Write the user's input to the subprocess stdin
            process.stdin.write((user_input + "\n").encode())   
            await process.stdin.drain()

            # Read the output from subprocess stdout and yield it
            user_input = yield await read_lines(process.stdout)
    finally:
        if process.returncode is None:
            process.kill()
        

async def run_game():
    gen = interact_with_process()
    print(await gen.asend(None), end="")  # Start the generator

    while True:
        user_input = input()
        try:
            line = await gen.asend(user_input)
        except StopAsyncIteration:
            break
        else:
            print(line, end="")


# Entry point of the script
if __name__ == "__main__":
    asyncio.run(run_game())
