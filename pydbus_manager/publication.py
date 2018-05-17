
NODE_INFO = """
<node>
	<interface name="org.freedesktop.DBus.ObjectManager">
		<method name="GetManagedObjects">
			<arg type="a{oa{sa{sv}}}" name="object_paths_interfaces_and_properties" direction="out"/>
		</method>
		<signal name="InterfacesAdded">
			<arg type="o" name="object_path"/>
			<arg type="a{sa{sv}}" name="interfaces_and_properties"/>
		</signal>
		<signal name="InterfacesRemoved">
			<arg type="o" name="object_path"/>
			<arg type="as" name="interfaces"/>
		</signal>
	</interface>
</node>
"""

class PublicationMixin(object):
	__slots__ = ()

	def publish(self):
		"""Expose itself on the bus."""
		bus = self.bus
		bus_name = self.bus_name
		path = self.path

		node_info = [NODE_INFO]  # TODO: add child xml interface from doc

		publication = bus.publish(bus_name, (path, self, node_info))
		return publication
