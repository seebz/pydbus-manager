#!/usr/bin/env python
from __future__ import print_function

from gi.repository import GLib
from pydbus import SessionBus
from pydbus_manager import Manager

bus = SessionBus()
proxy = bus.get("org.example.MyApp", "/")["org.freedesktop.DBus.ObjectManager"]

proxy.InterfacesAdded.connect(lambda *args: print("InterfacesAdded:", *args))
proxy.InterfacesRemoved.connect(lambda *args: print("InterfacesRemoved:", *args))

GLib.MainLoop().run()
