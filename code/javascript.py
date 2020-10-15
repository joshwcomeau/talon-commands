from talon import cron, ctrl, ui, Module, Context, actions, noise, settings, imgui, app
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
import subprocess
import os
import pathlib

mod = Module()
ctx = Context()

# @mod.capture
# def if_statement(m) -> str:
#     "Scaffolding for an `if` statement"


# ##### CONTEXT
# @ctx.capture(rule='if statement')
# def create_image(m):
#     return '<img alt="" src="" />'
