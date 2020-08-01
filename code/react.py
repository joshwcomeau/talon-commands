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

@mod.capture
def create_image(m) -> str:
    "Formats the text and returns a string"


@mod.capture
def default_import(m) -> str:
    "Import a default export"

@mod.capture(rule='(<user.vocabulary> | <phrase>)+')
def var(m) -> str:
    return m

@mod.capture(rule='(<user.vocabulary> | <phrase>)+')
def package(m) -> str:
    return m


@ctx.capture(rule='elm image')
def create_image(m):
    return '<img alt="" src="" />'

@ctx.capture(rule='elm <user.text>')
def create_element(m):
    return '<' + m.text

@ctx.capture(rule='import <user.var> from <user.package>')
def default_import(m):
    print('import test')
    print(m.var)
    print(m.package)
    # print(m.package)
    return f'import {m.var} from \'{m.package}\';'


# @ctx.action_class('react')
# class react_actions:
#     def language():
#         result = ""

#         #print("code.language: " + result)
#         return result
