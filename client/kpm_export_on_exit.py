import king_phisher.client.plugins as plugins
import king_phisher.client.gui_utilities as gui_utilities

class Plugin(plugins.ClientPlugin):
	authors = ['Spencer McIntyre']
	classifiers = ['Plugin :: Client :: Tool :: Data Management']
	title = 'Save KPM On Exit'
	description = 'Prompt to save the message data as a KPM file when King Phisher exits.'
	homepage = 'https://github.com/securestate/king-phisher-plugins'
	version = '1.0.1'
	def initialize(self):
		if self.application.rpc is None:
			self.signal_connect('server-connected', self.signal_server_connected)
		else:
			self.signal_connect('exit-confirm', self.signal_exit_confirm)
		return True

	def signal_exit_confirm(self, app):
		response = gui_utilities.show_dialog_yes_no(
			'Save KPM File?',
			app.get_active_window(),
			'Save the current message configuration to a KPM file?'
		)
		if not response:
			return
		mailer_tab = app.main_window.tabs['mailer']
		mailer_tab.export_message_data()

	def signal_server_connected(self, app):
		self.signal_connect('exit-confirm', self.signal_exit_confirm)
