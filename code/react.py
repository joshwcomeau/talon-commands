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
def create_closed_element(m) -> str:
    "Creates a react element"

@mod.capture
def create_native_element(m) -> str:
    "Creates a react element (lower case)"

@mod.capture
def create_image(m) -> str:
    "Creates a react <img> element"

@mod.capture
def create_styled_component(m) -> str:
    "Creates a new styled component"
@mod.capture
def create_styled_wrapper(m) -> str:
    "Creates a new styled Wrapper"

@mod.capture
def create_function_component(m) -> str:
    "Creates a new react function component"

@mod.capture
def default_import(m) -> str:
    "Import a default export"

@mod.capture
def component_import(m) -> str:
    "Import a react component"

@mod.capture
def hook_import(m) -> str:
    "Import a react hook"

@mod.capture
def text_attribute(m) -> str:
    "Add jsx attribute with double quotes"

@mod.capture
def squiggly_attribute(m) -> str:
    "Add jsx attribute with squiggly brackets"

@mod.capture
def state_hook(m) -> str:
    "Create a react state hook"
@mod.capture
def rough_hook(m) -> str:
    "Create a react ref hook"


@mod.capture(rule='(<user.vocabulary> | <phrase> | <user.text>)+')
def var(m) -> str:
    return m

@mod.capture(rule='(<user.vocabulary> | <phrase>)+')
def package(m) -> str:
    return m



# Context Stuff
@ctx.capture(rule='elm image')
def create_image(m):
    return '<img alt="" src="" />'

@ctx.capture(rule='elm <user.text>')
def create_element(m):
    return '<' + actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE') + '>'

@ctx.capture(rule='closed elm <user.text>')
def create_closed_element(m):
    return '<' + actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE') + '  />'

@ctx.capture(rule='elm native <user.html_elements>')
def create_native_element(m):
    return '<' + actions.user.formatted_text(m.html_elements, 'PRIVATE_CAMEL_CASE') + '>'

@ctx.capture(rule='styled <user.html_elements> <user.text>')
def create_styled_component(m):
    component_name = actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE')
    return f'const {component_name} = styled.{m.html_elements}``'

@ctx.capture(rule='styled wrapper <user.text>')
def create_styled_component(m):
    component_name = actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE')
    return f'const {component_name} = styled()``'

@ctx.capture(rule='function component <user.text>')
def create_function_component(m):
    component_name = actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE')
    return f'function {component_name}({{}}) {{}}'

@ctx.capture(rule='import <user.var> from <user.package>')
def default_import(m):
    return f'import {m.var} from \'{m.package}\';'

@ctx.capture(rule='import component <user.text>')
def component_import(m):
    component_name = actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE')
    return f'import {component_name} from \'@components/{component_name}\';'

@ctx.capture(rule='import hook <user.text>')
def component_import(m):
    hook_name = actions.user.formatted_text(m.text, 'PRIVATE_CAMEL_CASE')
    filename =  actions.user.formatted_text(m.text, 'DASH_SEPARATED') + '.hook'
    return f'import {hook_name} from \'@hooks/{filename}\';'

@ctx.capture(rule='text attribute <user.text>')
def text_attribute(m):
    attribute_name = actions.user.formatted_text(m.text, 'PRIVATE_CAMEL_CASE')
    return f'{attribute_name}=""'

@ctx.capture(rule='squiggly attribute <user.text>')
def squiggly_attribute(m):
    attribute_name = actions.user.formatted_text(m.text, 'PRIVATE_CAMEL_CASE')
    return f'{attribute_name}={{}}'

@ctx.capture(rule='state hook <user.text>')
def state_hook(m):
    state_name = actions.user.formatted_text(m.text, 'PRIVATE_CAMEL_CASE')
    setter_name = 'set' + actions.user.formatted_text(m.text, 'PUBLIC_CAMEL_CASE')
    return f'const [{state_name}, {setter_name}] = React.useState();'

@ctx.capture(rule='rough hook <user.text>')
def rough_hook(m):
    state_name = actions.user.formatted_text(m.text, 'PRIVATE_CAMEL_CASE')
    return f'const {state_name}Ref = React.useRef();'


mod.list('html_elements', desc='list of all HTML elements')




ctx.lists['user.html_elements'] = {
  'div': 'div',
  'span': 'span',
  'section': 'section',
  'header': 'header',
  'footer': 'footer',
  'article': 'article',
  'aside': 'aside',
  'main': 'main',
  'break': 'br',
  'list': 'ul',
  'ordered list': 'ol',
  'list item': 'li',
  'a': 'a',
  'anchor': 'a',
  'image': 'img',
  'pe': 'p',
  'paragraph': 'p',
  'heading one': 'h1',
  'heading two': 'h2',
  'heading three': 'h3',
  'heading four': 'h4',
  'heading five': 'h5',
  'heading six': 'h6',
  'form': 'form',
  'input': 'input',
  'button': 'button',
  'text area': 'textarea',
  'select': 'select',
  'label': 'label',
  'details': 'details',
  'strong': 'strong',
  'am': 'em',
  'emphasis': 'em',
  'title': 'title',
  'table': 'table',
  'table body': 'tbody',
  'table head': 'thead',
'table row': 'tr',
'table heading': 'th',
'table cell': 'td'
}
