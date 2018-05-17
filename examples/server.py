#!/usr/bin/env python

from gi.repository import GLib
from pydbus import SessionBus
from pydbus_manager import Manager
from example import Example


bus = SessionBus()
manager = Manager(bus, "org.example.MyApp", "/")

child = Example()

print("register")
# bus.register_object("/org/example/MyApp/child", child, None)
x = manager.register_object("/org/example/MyApp/child", child, None)
print("registered")

print("...........")

# objects = manager.GetManagedObjects()
# print(objects)

print("unregister")
x.unregister()
print("unregistered")

GLib.MainLoop().run()
