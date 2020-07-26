
# elm <user.text>:
#   "<"
#   insert(user.text)
#   ">"
#   key("enter")
# elm <user.text>:
#   user.react_create_element(user.text)

# action(user.react_create_element):
#   "hello2"

# boo: "ysa"

<user.create_element> [over]: insert(create_element)

react: insert("import React from 'react';")
styled: insert("import styled from 'styled-components';")

<user.default_import>: insert(default_import)

up: insert('../')

# todo: Move these to their own Talon file
save: key('cmd s')
console:
  insert('console.log();')
  key('left left')

