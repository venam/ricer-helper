#!/usr/bin/env python
import Outputer
import JsonInfoReader
import State
import random

out = Outputer.Outputer()
state = State.State()
info = JsonInfoReader.JsonInfoReader("info.json")
state.addSelect("Bootloader")
state.addComment("Bootloader","I use a magenta... blah blah")
state.addSelect("Window manager")
state.addComment("Window manager", "2bwm ftw")
state.addSelect("GUI")
state.addComment("GUI", "gtk theme: a modified version of flatstudio that can be found here\nhttp://example.com")
out.output(random.choice(out.getAvailable()),state,info, "savedOutputTest")

