import globalPluginHandler
import config
import scriptHandler
import gui
import addonHandler
from .consts import addonInfos

addonHandler.initTranslation()

confspecs = {
	"nbWeek": "integer(default=60)",
	"autoUpdate": "boolean(default=True)",
	"updateEveryStart": "boolean(default=False)",
	"column1": "string(default=date)",
	"column2": "string(default=size)",
	"column3": "string(default=path)",
	"sayColumn": "boolean(default=True)",
}

config.conf.spec[addonInfos['name']] = confspecs
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__ (self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		gui.NVDASettingsDialog.categoryClasses.append(settings_gui.Everything)
	
	def terminate(self):
		super().terminate()
		gui.NVDASettingsDialog.categoryClasses.remove(settings_gui.Everything) 

from . import settings_gui