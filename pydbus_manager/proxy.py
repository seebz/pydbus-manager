# -*- coding: utf-8 -*-

class ProxyMixin(object):
	__slots__ = ()

	def get(self, object_path=None, **kwargs):
		"""Get a managed object."""
		bus = self.bus
		bus_name = self.bus_name

		composite_object = bus.get(bus_name, object_path, **kwargs)
		return composite_object
