#!/usr/bin/env python

from pydbus import SessionBus

# get the session bus
bus = SessionBus()

# get the manager
the_manager = bus.get("org.example.MyApp")["org.freedesktop.DBus.ObjectManager"]

# list all managed objects
reply = the_manager.GetManagedObjects()
print(reply)

# get a managed object
the_child = bus.get("org.example.MyApp", "/org/example/MyApp/child2")

# call the methods and print the results
reply = the_child.EchoString("test 123")
print(reply)

# read the property and print the results
reply = the_child.SomeProperty
print(reply)
