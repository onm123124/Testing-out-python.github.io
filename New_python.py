<<<<<<< HEAD
from ast import Str
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
import turtle
=======
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
>>>>>>> f31eddd3fe19a4a91878692d0885a55e84d01245

aturtle=turtle

