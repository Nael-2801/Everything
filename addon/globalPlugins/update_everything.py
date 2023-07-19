import core
import os
import urllib.request
import addonHandler
import globalPluginHandler
import gui
import wx
import datetime
import scriptHandler
from logHandler import log
import config
import globalVars
import ui
addonHandler.initTranslation()

baseDir = os.path.dirname(__file__) 
addon = os.path.join(baseDir, "..") 
addonInfos = addonHandler.Addon(addon).manifest

confSpecs = {
	"nbWeek": "integer(default=60)",
	"autoUpdate": "boolean(default=True)",
	"updateEveryStart": "boolean(default=False)",
}
config.conf.spec[addonInfos["name"]] = confSpecs
time=datetime.datetime.now()
week= int(time.strftime("%W"))

def updateAvailable():
	title = _("Update of %s version %s") %(addonInfos["summary"], oversion)
	msg = _("%s version %s is available. Would you like to update now? You can see the new features by clicking on the help button in the add-on manager.") %(addonInfos["summary"], oversion)
	res = gui.messageBox(msg, title, wx.YES_NO|wx.ICON_ERROR)
	if res == wx.YES:
		installupdate()
	else:
		config.conf[addonInfos["name"]]["nbWeek"] = week

def installupdate():
	temp=os.environ.get('TEMP')
	file=temp + "\\"+addonInfos["name"]+"_" + oversion + ".nvda-addon"
	url=f"https://module.nael-accessvision.com/addons/addons/"+addonInfos["name"]+"/"+addonInfos["name"]+"-{oversion}.nvda-addon"
	urllib.request.urlretrieve(url, file)
	curAddons = []
	for addon in addonHandler.getAvailableAddons():
		curAddons.append(addon)
	bundle = addonHandler.AddonBundle(file)
	prevAddon = None
	bundleName = bundle.manifest['name']
	for addon in curAddons:
		if not addon.isPendingRemove and bundleName == addon.manifest["name"]:
			prevAddon = addon
			break
	if prevAddon:
		prevAddon.requestRemove()
	addonHandler.installAddonBundle(bundle)
	os.remove(file)
	config.conf[addonInfos["name"]]["nbWeek"] = week
	core.restart()

def verifUpdate(gesture=False):
	global oversion
	version = addonInfos["version"]
	rversion = urllib.request.urlopen("https://module.nael-accessvision.com/addons/addons/"+addonInfos["name"]+"/version_"+addonInfos["name"]+".txt")
	tversion = rversion.read().decode()
	oversion=tversion.replace("\n", "")
	if version != oversion:
		wx.CallAfter(updateAvailable)
	else:
		if gesture:
			ui.message(_("No update is available."))

def Param(param,message):
	if not config.conf[addonInfos["name"]][param]:
		config.conf[addonInfos["name"]][param]= True
		ui.message(_("%s is enabled.") %(message))
	else:
		config.conf[addonInfos["name"]][param] = False
		ui.message(_("%s is disabled.") %(message))

if not globalVars.appArgs.secure and config.conf[addonInfos["name"]]["autoUpdate"] and (config.conf[addonInfos["name"]]["nbWeek"] != week or config.conf[addonInfos["name"]]["updateEveryStart"]):
	verifUpdate()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@scriptHandler.script(description=addonInfos["summary"]+_(""": checks for module updates manually"""),category=addonInfos["summary"])
	def script_gestureUpdate(self, gesture):
		verifUpdate(True)
	
	@scriptHandler.script(description=addonInfos["summary"]+_(""": enable/disable automatic update checking"""),category=addonInfos["summary"])
	def script_autoUpdate(self, gesture):
		Param("autoUpdate",_("Automatic update"))
