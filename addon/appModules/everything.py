# -*- coding: utf-8 -*-
import controlTypes
import appModuleHandler
import os
import addonHandler
import scriptHandler
import api
import ui
from logHandler import log
addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		self.file = os.getenv('APPDATA')+"/nvda/everything.ini"
		if not os.path.exists(self.file):
			createFile = open(self.file, "w")
			createFile.write(_("""#This file allows organizing the display of columns in Everything.
# Move the variables @path @size @date to organize the column display. Please make sure to separate each element with a space.\n""")+
"""lines = @date @size @path\n"""+
_("""# The following line enables the announcement of column names in Everything.
# Write False after the equal sign to disable it or True to enable it. Please note that the capitalization is important.\n""")+
"sayColumn=True")
			createFile.close()
		self.readConfigFile(self.file)
	
	def event_gainFocus(self, obj, nextHandler):
		if obj.role == controlTypes.Role.LISTITEM and obj.windowClassName == 'SysListView32':
			#get the value of all columns
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
				if order == '@path':
					if self.sayColumn:
						newobj=newobj+_("Path: ")
					newobj = newobj+listChildren[1]
					count=count+1
				elif order == '@size':
					if self.sayColumn:
						newobj=newobj+_("Size: ")
					newobj = newobj+listChildren[2]
					count=count+1
				elif order == '@date':
					if self.sayColumn:
						newobj=newobj+_("Date: ")
					newobj = newobj+listChildren[3]
					count=count+1
				if count < 3:
					newobj=newobj+"; "
			obj.name = newobj
		nextHandler()

	@scriptHandler.script(gesture="kb:control+shift+o",description=_("""Open the configuration file of the Everything extension"""),category="Everything")
	def script_openFile(self, gesture):
		openConfigFile()

	@scriptHandler.script(gesture="kb:control+shift+R",description=_("""Reload the configuration file of the Everything extension"""),category="Everything")
	def script_fileConfig(self, gesture):
		self.readConfigFile(self.file)
		ui.message(_("Reloaded configuration."))
	
	def getTextFile(self, searchText, cutSpace=True):
		for l in self.lines:
			if l.startswith(searchText):
				result = l.split("=")[1]
				if cutSpace:
					result = result.split(" ")
				if result[0] == '':
					del result[0]
		return result

	def readConfigFile(self, file):
		read = open(file, 'r')
		self.lines = read.readlines()
		read.close()
		self.column = self.getTextFile("lines")
		self.column[-1] = self.column[-1].replace("\n","")
		self.sayColumn = eval(self.getTextFile("sayColumn", cutSpace=False))

def openConfigFile():
	configFile = api.config.getUserDefaultConfigPath()+"\\everything.ini"
	startProgramMaximized (r"C:\Windows\System32\notepad.exe", configFile)


def startProgramMaximized(exePath, exeParams=""):
	import subprocess
	SW_MAXIMIZE = 3
	info = subprocess.STARTUPINFO()
	info.dwFlags = subprocess.STARTF_USESHOWWINDOW
	info.wShowWindow = SW_MAXIMIZE
	if exeParams != "":
		exePath += " " + exeParams 
	subprocess.Popen(exePath, startupinfo=info)

