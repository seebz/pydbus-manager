from pydbus.subscription import Subscription

class SubscriptionMixin(object):
	__slots__ = ()
	SubscriptionFlags = Subscription.Flags

	def subscribe(self, iface=None, signal=None, object=None, arg0=None, flags=0, signal_fired=None):
		"""Subscribes to matching signals."""
		bus = self.bus
		sender = self.bus_name

		subscription = bus.subscribe(sender, iface, signal, object, arg0, flags, signal_fired)
		return subscription
