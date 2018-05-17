
class RegistrationMixin:
	__slots__ = ()

	def register_object(self, path, object, node_info):
		"""Register object on the bus."""
		bus = self.bus
		bus_name = self.bus_name

		registration = bus.register_object(path, object, node_info)

		def at_init():
			print("at_init()")
			proxy = self.get(path)
			# TODO
		at_init()

		def at_exit():
			print("at_exit()")
			proxy = self.get(path)
			interfaces = [base.__name__ for base in type(proxy).__bases__]
			self.InterfacesRemoved(path, interfaces)

		registration._at_exit(at_exit)

		return registration
