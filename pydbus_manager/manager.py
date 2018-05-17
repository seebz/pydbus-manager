from gi.repository import Gio

from pydbus import Variant
from pydbus.auto_names import *
from pydbus.generic import signal
from pydbus.proxy_property import ProxyProperty

class ManagerMixin(object):
	InterfacesAdded = signal()
	InterfacesRemoved = signal()

	def GetManagedObjects(self):
		pass
		# TODO
