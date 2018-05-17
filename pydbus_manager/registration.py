from gi.repository import Gio
from pydbus import Variant

class RegistrationMixin:
	__slots__ = ()

	def register_object(self, path, object, node_info):
		"""Register object on the bus."""
		manager = self

		def at_init():
			proxy = manager.get(path)

			xml = proxy["org.freedesktop.DBus.Introspectable"].Introspect()
			node_info = Gio.DBusNodeInfo.new_for_xml(xml)
			interfaces = node_info.interfaces

			interfaces_and_properties = {}
			for iface in interfaces:
				interfaces_and_properties[iface.name] = {}

				for prop in iface.properties:
					try:
						value = getattr(object, prop.name)
						variant = Variant(prop.signature, value)

						interfaces_and_properties[iface.name][prop.name] = variant
					except:
						pass

			manager.InterfacesAdded(path, interfaces_and_properties)

		def at_exit():
			proxy = manager.get(path)
			interfaces = [base.__name__ for base in type(proxy).__bases__]

			manager.InterfacesRemoved(path, interfaces)

		registration = manager.bus.register_object(path, object, node_info)
		registration._at_exit(at_exit)

		at_init()

		return registration
