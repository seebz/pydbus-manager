from pydbus.generic import signal

class Example(object):
	"""
	<node>
		<interface name='net.lew21.pydbus.TutorialExample'>
			<method name='EchoString'>
				<arg type='s' name='a' direction='in'/>
				<arg type='s' name='response' direction='out'/>
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
