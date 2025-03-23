from db_man import *
from bot_task_commands import *

import os
from dotenv import load_dotenv
load_dotenv(override=True)

TOKEN = os.environ.get("DISCORD_TOKEN")

import discord
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", help_command= None, intents=intents)

def get_user_by_id(user_id: int) -> discord.user:
    guild = bot.get_guild()

@bot.event
async def on_ready():
    print(f"bot is ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("hello cânim")
    await bot.process_commands(message)


@bot.command("add_task")
async def add_task(ctx, *task):
    task = " ".join([word for word in task if not word.startswith("<")])
    if not check_user(ctx.author.id):   # Checking if user is privilege
        await ctx.send("You are not allowed to assign a task")
        return
    if not ctx.message.mentions:
        await ctx.send("You have to mention someone to assign task")
    user2assign_task = ctx.message.mentions[0]
    print("add task öncesi")
    add_task_db(ctx.author.id, user2assign_task.id, task)
    print("add task sonrası")
    await ctx.send(f"{task} assigned to {user2assign_task.name} ✅")

@bot.command("delete_task")
async def delete_task(ctx, task_id):
    if not check_user(ctx.message.author.id):
        await ctx.send("You cannot delete a task")
        return
    delete_task_db(int(task_id))
    await ctx.send("task is removed❌")

@bot.command("complete_task")
async def complete_task(ctx, task_id): # to assign task completed, you must be assigned it at first
    task = execute_query(
        "SELECT * FROM task WHERE id = ?",
        (task_id,)
    )
    task_given_by = task[0]
    if not ctx.author.id == task_given_by[1]:
        await ctx.send("this task is not assigned by you")
        return
    complete_task_db(task_id)

@bot.command("show_tasks")
async def show_tasks(ctx):
    result = get_all_tasks_db()
    await ctx.send(result)


@bot.command("add_user")
async def add_user(ctx):    # only admin can add a new user with privilege to assign task
    admin_id = os.environ.get("ADMIN_ID")
    if not ctx.author.id == int(admin_id):
        await ctx.send("You're not allowed to do this")
        return
    user2assign_privilege = ctx.message.mentions[0]
    add_user_db(user2assign_privilege.id ,user2assign_privilege.name)
    await ctx.send(f"{user2assign_privilege.name} can assign tasks now")

if not check_db():
    init_db()
bot.run(TOKEN)