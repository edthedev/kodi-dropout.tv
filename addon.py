# Kodi modules
import xbmc
import xbmcaddon
import xbmcgui

# Python modules
import platform
import os.path
import subprocess
import json

# Getting constants
__addon__ = xbmcaddon.Addon('program.launcher.chrome')
__addonId__ = __addon__.getAddonInfo('id')
__addonName__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')

subprocess.run(
    [sys.executable, '-m', 'pip', 'install', 'robotframework-SeleniumLibrary'])

# Method to print logs on a standard way
def log(message, level=xbmc.LOGNOTICE):
    xbmc.log('[%s:v%s] %s' % (__addonId__, __version__, message.encode('utf-8')), level)
# end of log

# Starting the Addon
log("Starting " + __addonName__)

launch = ["robot", "dropout.robot"]

# Var to hold current display sleep timer
displayoff = ""

# Var to hold current computer sleep timer
shutdowntime = ""

if __addon__.getSetting('powersaving') == "true":
    log("Turning off powersavings")
    displayoff = str(json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"powermanagement.displaysoff"},"id":1}'))["result"]["value"])
    log("Current display off time: " + displayoff)
    shutdowntime = str(json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettingValue", "params":{"setting":"powermanagement.shutdowntime"},"id":1}'))["result"]["value"])
    log("Current shutdown time: " + shutdowntime)
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.displaysoff","value":0},"id":1}')
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.shutdowntime","value":0},"id":1}')
if __addon__.getSetting('workaround') == "true":
    log("Applying workaround for windows stacking order")
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method": "Input.ExecuteAction", "params": {"action":"togglefullscreen"},"id":1}')

subprocess.call(launch)

if __addon__.getSetting('powersaving') == "true":
    log("Returning powersaving settings to inital value")
    # Before reenabling powersavings, send Down key to Kodi to wake up. Otherwise computer goes to sleep as soon as parameter is set
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Input.Down","id":1}')
    
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.displaysoff","value":'+displayoff+'},"id":1}')
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"powermanagement.shutdowntime","value":'+shutdowntime+'},"id":1}')
if __addon__.getSetting('workaround') == "true":
    log("Removing workaround for windows stacking order")
    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method": "Input.ExecuteAction", "params": {"action":"togglefullscreen"},"id":1}')
