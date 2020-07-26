from talon import cron, ctrl, ui, Module, Context, actions, noise, settings, imgui, app
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
import subprocess
import os
import pathlib

mod = Module()
ctx = Context()


# @mod.action_class
# class Actions:
#     def react_create_element(text: str):
#         """Create a react element"""
#         print('debug fos')
#         'hello'
@mod.capture
def create_element(m) -> str:
    "Formats the text and returns a string"

@ctx.capture(rule='elm <user.text>')
def create_element(m):
    print('debug fos')
    print(m.text)
    m.text


# @ctx.action_class('react')
# class react_actions:
#     def language():
#         result = ""

#         #print("code.language: " + result)
#         return result
