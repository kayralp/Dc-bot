import tkinter as tk
import discord
import random

window = tk.Tk()
window.title("Guessing Game")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def yaziTura():
    result = random.choice([True, False])
    return result

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('sans'):
        user_guess = message.content.split()[1].lower() if len(message.content.split()) > 1 else ''
        result = yaziTura()
        if user_guess == 'doğru' and result == True:
            response = "Tebrikler!Doğru cevap doğruydu."
        elif user_guess == 'yanlış' and result == False:
            response = "Tebrikler !Doğru cevap yanlıştı."
        else:
            response = f"Üzgünüm, yanlış tahmin ettin. Cevap {result}."
        await message.author.send(response, delete_after=5.0)

client.run('')

window.mainloop()
