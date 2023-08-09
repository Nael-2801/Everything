# -*- coding: utf-8 -*-
import controlTypes
import appModuleHandler
import addonHandler
import scriptHandler
import api
import ui
from logHandler import log
import wx
import gui
import config
addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):
	def event_gainFocus(self, obj, nextHandler):
		if obj.role == controlTypes.Role.LIST and obj.windowClassName == 'SysListView32':
			if obj.firstChild != controlTypes.Role.LISTITEM:
				obj.name = _("No result found")
		if obj.role == controlTypes.Role.LISTITEM and obj.windowClassName == 'SysListView32':
			#get the value of all columns
			self.column = [config.conf["everything"]["column1"]],config.conf["everything"["column2"],config.conf["everything"]["column3"]]
			self.sayColumn=config.conf["everything"]["sayColumn"]
			o=obj.firstChild
			listChildren=[]
			while o:
				#add the value of column on the listChildren variable
				listChildren.append(o.name)
				o=o.next
			newobj= listChildren[0]+"; "
			count=0
			#Arrange the order of column display
			for order in self.column:
				if order == 'path':
					if self.sayColumn:
						newobj=newobj+_("Path: ")
					newobj = newobj+listChildren[1]
					count=count+1
				elif order == 'size':
					if self.sayColumn:
						newobj=newobj+_("Size: ")
					newobj = newobj+listChildren[2]
					count=count+1
				elif order == 'date':
					if self.sayColumn:
						newobj=newobj+_("Date: ")
					newobj = newobj+listChildren[3]
					count=count+1
				if count < 3:
					newobj=newobj+"; "
			obj.name = newobj
		nextHandler()

	@scriptHandler.script(gesture="kb:control+shift+o",description=_("""Open the settings panel of the Everything extension"""),category="Everything")
	def script_openFile(self, gesture):
		import globalPlugins.everything.settings_gui as settings_gui
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.settingsDialogs.NVDASettingsDialog, settings_gui.Everything)

