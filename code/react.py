from talon import cron, ctrl, ui, Module, Context, actions, noise, settings, imgui, app
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
import subprocess
import os
import pathlib

mod = Module()
ctx = Context()



@mod.capture(rule='({user.html_elements})')
def html_elements(m) -> str:
    return m.html_elements

@mod.capture
def create_element(m) -> str:
    "Creates a react element"

@mod.capture
def create_image(m) -> str:
    "Creates a react <img> element"

@mod.capture
def create_styled_component(m) -> str:
    "Creates a new styled component"

@mod.capture
def css_attribute(m) -> str:
    "Adds a css attribute"


@mod.capture
def default_import(m) -> str:
    "Import a default export"

@mod.capture(rule='(<user.vocabulary> | <phrase> | <user.text>)+')
def var(m) -> str:
    return m

@mod.capture(rule='(<user.vocabulary> | <phrase>)+')
def package(m) -> str:
    return m

@mod.capture(rule='<user.text>')
def attribute_key(m) -> str:
    return m
@mod.capture(rule='<user.text>')
def attribute_value(m) -> str:
    return m


@ctx.capture(rule='elm image')
def create_image(m):
    return '<img alt="" src="" />'

@ctx.capture(rule='elm <user.text>')
def create_element(m):
    return '<' + actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE') + '>'

@ctx.capture(rule='styled <user.html_elements> <user.text>')
def create_styled_component(m):
    component_name = actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE')
    return f'const {component_name} = styled.{m.html_elements}``'

@ctx.capture(rule='cat <user.attribute_key> <user.attribute_value>')
def css_attribute(m):
    key = actions.user.formatted_text(m.attribute_key, 'DASH_SEPARATED')
    return f'{key}: {m.attribute_value}'

@ctx.capture(rule='import <user.var> from <user.package>')
def default_import(m):
    print('import test')
    print(m.var)
    print(m.package)
    # print(m.package)
    return f'import {m.var} from \'{m.package}\';'

mod.list('html_elements', desc='list of all HTML elements')




ctx.lists['user.html_elements'] = {
  'div': 'div',
  'span': 'span',
  'section': 'section',
  'article': 'article',
  'aside': 'aside',
  'break': 'br',
  'list': 'ul',
  'ordered list': 'ol',
  'list item': 'li',
  'a': 'a',
  'image': 'img',
  'pe': 'p',
  'heading one': 'h1',
  'heading two': 'h2',
  'heading three': 'h3',
  'heading four': 'h4',
  'heading five': 'h5',
  'heading six': 'h6',
}
