# -*- coding: utf-8 -*-

from __future__ import print_function

from gi.repository import Gio
from pydbus import Variant
from pydbus.generic import signal

class RegistrationMixin:
	_objects = {}

	InterfacesAdded = signal()
	InterfacesRemoved = signal()

	def _add_object(self, path, object_):
		self._objects[path] = object_

		interfaces_and_properties = self._get_interfaces_and_properties(path)
		self.InterfacesAdded(path, interfaces_and_properties)

	def _remove_object(self, path, object_):
		object_ = self._objects.pop(path)
		proxy = self.get(path)

		interfaces = [base.__name__ for base in type(proxy).__bases__]
		self.InterfacesRemoved(path, interfaces)

	def _get_interfaces_and_properties(self, path):
		object_ = self._objects[path]
		proxy = self.get(path)

		xml = proxy["org.freedesktop.DBus.Introspectable"].Introspect()
		node_info = Gio.DBusNodeInfo.new_for_xml(xml)
		interfaces = node_info.interfaces

		interfaces_and_properties = {}
		for iface in interfaces:
			interfaces_and_properties[iface.name] = {}

			for prop in iface.properties:
				try:
					value = getattr(object_, prop.name)
					variant = Variant(prop.signature, value)

					interfaces_and_properties[iface.name][prop.name] = variant
				except:
					pass

		return interfaces_and_properties

	def register_object(self, path, object_, node_info):
		"""Register object on the bus."""
		manager = self
		bus = self.bus

		registration = bus.register_object(path, object_, node_info)

		# signals
		manager._add_object(path, object_)
		registration._at_exit(lambda *args: manager._remove_object(path, object_))

		return registration

	def GetManagedObjects(self):
		"""Implementation of org.freedesktop.DBus.ObjectManager.GetManagedObjects()"""
		object_paths_interfaces_and_properties = {}

		for path, object_ in self._objects.items():
			object_paths_interfaces_and_properties[path] = self._get_interfaces_and_properties(path)

		return object_paths_interfaces_and_properties
