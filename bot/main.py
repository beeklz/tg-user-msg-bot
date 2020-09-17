from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep


app = Client("my_account")


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    """Command .type adds typing effect for a message."""
    text = msg_original = msg.text.split(".type ", maxsplit=1)[1]
    result = ""
    typing_symbol = "_"

    while(result != msg_original):
        try:
            msg.edit(result + typing_symbol)
            sleep(0.02)  # 20 ms

            result += text[0]
            text = text[1:]

            msg.edit(result)
            sleep(0.02)

        except FloodWait as e:
            sleep(e.x)


if __name__ == "__main__":
    app.run()
