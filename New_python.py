import discord
from ast import Strfrom 
from cgi import parse_header
from ctypes import py_object
from tkinter import*
from queue import PriorityQueue
from re import A, X
from sqlite3 import adapt
from telnetlib import theNULL
from tkinter.tix import ButtonBox
from tkinter.ttk import Button
from typing import no_type_check
from html import __all__
from profile import Profile
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')


