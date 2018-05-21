#!/usr/bin/env python
from __future__ import print_function

from gi.repository import GLib
from pydbus import SessionBus
from pydbus_manager import Manager

# get the session bus
bus = SessionBus()

# get the manager
the_manager = bus.get("org.example.MyApp")["org.freedesktop.DBus.ObjectManager"]

# subscribe to signals
the_manager.InterfacesAdded.connect(lambda *args: print("InterfacesAdded:", *args))
the_manager.InterfacesRemoved.connect(lambda *args: print("InterfacesRemoved:", *args))

# the loop
GLib.MainLoop().run()
