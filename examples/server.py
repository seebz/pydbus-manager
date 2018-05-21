#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import GLib
from pydbus import SessionBus
from pydbus.generic import signal
from pydbus_manager import Manager


# child class
class Example(object):
	"""
	<node>
		<interface name="net.lew21.pydbus.TutorialExample">
			<method name="EchoString">
				<arg type="s" name="a" direction="in"/>
				<arg type="s" name="response" direction="out"/>
			</method>
			<property name="SomeProperty" type="s" access="readwrite">
				<annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
			</property>
		</interface>
	</node>
	"""

	def EchoString(self, s):
		"""returns whatever is passed to it"""
		return s

	def __init__(self):
		self._someProperty = "initial value"

	@property
	def SomeProperty(self):
		return self._someProperty

	@SomeProperty.setter
	def SomeProperty(self, value):
		self._someProperty = value
		self.PropertiesChanged("net.lew21.pydbus.TutorialExample", {"SomeProperty": self.SomeProperty}, [])

	PropertiesChanged = signal()

# get the session bus
bus = SessionBus()

# init & publish our manager to the bus
manager = Manager(bus, "org.example.MyApp")

# register two children
registration1 = manager.register_object("/org/example/MyApp/child1", Example(), None)
registration2 = manager.register_object("/org/example/MyApp/child2", Example(), None)

# list all managed objects
reply = manager.GetManagedObjects()
print(reply)

# unregister the first child
registration1.unregister()

# list all managed objects
reply = manager.GetManagedObjects()
print(reply)

# the loop
GLib.MainLoop().run()
