import os

addon = os.path.join(os.path.dirname(__file__), "..", "..") 
addonInfos = addonHandler.Addon(addon).manifest
