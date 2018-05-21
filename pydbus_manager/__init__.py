# -*- coding: utf-8 -*-

__all__ = ["Manager"]

from pydbus.auto_names import *

from .proxy import ProxyMixin
from .publication import PublicationMixin
from .registration import RegistrationMixin
from .subscription import SubscriptionMixin

class Manager(ProxyMixin, SubscriptionMixin, RegistrationMixin, PublicationMixin):

	def __init__(self, bus, bus_name, path=None, publish=True):
		bus_name = auto_bus_name(bus_name)
		path = auto_object_path(bus_name, path)

		self._bus = bus
		self._bus_name = bus_name
		self._path = path

		if publish:
			self.publish()

	@property
	def bus(self):
		return self._bus

	@property
	def bus_name(self):
		return self._bus_name

	@property
	def path(self):
		return self._path
