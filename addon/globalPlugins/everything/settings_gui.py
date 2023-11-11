import wx
import gui
try:
	from gui.settingsDialogs import SettingsPanel
except ImportError:
	from gui import SettingsPanel
import config
import ui
import addonHandler
from logHandler import log

addonHandler.initTranslation()

class Everything(SettingsPanel):
	title = "Everything"
	column=(
		# Translator: A list option in the parameter panel
		("date", _("Date")),
		# Translator: A list option in the parameter panel
		("size", _("Size")),
		# Translator: A list option in the parameter panel
		("path", _("Path")),
	)
	
	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		generalGroupSizer = wx.StaticBoxSizer(wx.VERTICAL, self, label=_("General"))
		generalGroupBox = generalGroupSizer.GetStaticBox()
		generalGroup = gui.guiHelper.BoxSizerHelper(self, sizer=generalGroupSizer)
		sHelper.addItem(generalGroup)

		self.sayColumn = generalGroup.addItem(
			wx.CheckBox(generalGroupBox, 
			# Translator: Checkbox label in parameter panel
			label=_("Announce column names"))
		)
		self.sayColumn.SetValue(config.conf["everything"]["sayColumn"])

		listChoice = [name for setting, name in self.column]

		self.list1 = generalGroup.addLabeledControl(
			# Translator: List name in parameter panel
			_("Choose the &first information to be displayed in the results list"),
			wx.Choice,
			choices=listChoice
		)
		for index, (setting, name) in enumerate(self.column):
			if setting == config.conf["everything"]["column1"]:
				self.list1.SetSelection(index)
				break
			else:
				self.list1.SetSelection(0)

		self.list2 = generalGroup.addLabeledControl(
			# Translator: List name in parameter panel
			_("Choose the &second information to display in the results list"),
			wx.Choice,
			choices=listChoice
		)
		for index, (setting, name) in enumerate(self.column):
			if setting == config.conf["everything"]["column2"]:
				self.list2.SetSelection(index)
				break
			else:
				self.list2.SetSelection(0)

		self.list3 = generalGroup.addLabeledControl(
			# Translator: List name in parameter panel
			_("Choose the &third information to display in the results list"),
			wx.Choice,
			choices=listChoice
		)
		for index, (setting, name) in enumerate(self.column):
			if setting == config.conf["everything"]["column3"]:
				self.list3.SetSelection(index)
				break
			else:
				self.list3.SetSelection(0)
	
		self.reset = generalGroup.addItem(
			wx.Button(generalGroupBox,
			# Translator: Button label in parameter panel
			label=_("&Return to default settings")
			)
		)
		self.reset.Bind(wx.EVT_BUTTON, self.on_reset)
	
	def on_reset(self, evt):
		self.list1.SetSelection(0)
		self.list2.SetSelection(1)
		self.list3.SetSelection(2)
		self.sayColumn.SetValue(True)
		# Translator: Message says when you click on the return to default settings button in the settings panel
		ui.message(_("Settings reset to default"))

	def onSave(self):
		valu1 = self.list1.GetSelection()
		valu2 = self.list2.GetSelection()
		valu3 = self.list3.GetSelection()
		if valu1 == valu2 or valu1 == valu3 or valu2 == valu3:
			gui.messageBox(
				# Translator: Text displayed in error window after parameter validation
				_("You have selected the same element several times in the display organization. You only need to select an element once in the column display."), 
				# Translator: Title of error window after parameter validation
				_("Display selection error"), wx.OK|wx.ICON_ERROR)
		else:
			config.conf["everything"]["column1"] = self.column[valu1][0]
			config.conf["everything"]["column2"] = self.column[valu2][0]
			config.conf["everything"]["column3"] = self.column[valu3][0]
		config.conf["everything"]["sayColumn"] = self.sayColumn.GetValue()

