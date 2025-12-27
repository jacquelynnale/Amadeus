import xbmcaddon

import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
CUSTOM_ART = os.path.join(PATH, 'resources', 'amadeus_art')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = '[COLOR blue]Amadeus Wizard[/COLOR]'
BUILDERNAME = '[COLOR blue]Amadeus Wizard Team[/COLOR]'
EXCLUDES = [ADDON_ID]
# Text File with build info in it
BUILDFILE = 'https://raw.githubusercontent.com/jacquelynnale/Amadeus/main/wizard/assets/build.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = 'http://'

#########################################################
# Amadeus Wizard - Custom Settings
BUILD_SKIN_SWITCH_IMAGE_URL = 'https://raw.githubusercontent.com/jacquelynnale/Amadeus/main/wizard/assets/skin_switch.png'
# Auto Quick Updates
QUICK_UPDATE_NOTIFICATION_URL = 'https://raw.githubusercontent.com/jacquelynnale/Amadeus/main/wizard/assets/quick_update.txt'
# Auto Android/Windows Update - Disabled for now
LATEST_WINDOWS_VERSION_TEXT_FILE = 'http://'
WINDOWS_DOWNLOAD_URL = 'http://'
WINDOWS_INSTALLATION_PATH = "C:\\Amadeus Wizard"
LATEST_APK_VERSION_TEXT_FILE = 'http://'
APK_DOWNLOAD_URL = 'http://'
APK_PACKAGE_ID = 'org.xbmc.amadeuswizard'
APK_DOWNLOADER_CODE = '000000'
APK_DOWNLOADER_CODE_IMAGE_URL = 'http://'
#########################################################

# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = ''
YOUTUBEFILE = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'http://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'wizard.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
SPACER = '='

# Theme Colors
COLOR1 = 'blue'
COLOR2 = 'gold'
COLOR_LIMEGREEN = 'limegreen'
COLOR_YELLOW = 'yellow'
COLOR_WHITE = 'white'
# Primary menu items
THEME1 = u'[COLOR {color1}][B]Amadeus Wizard[/B][/COLOR] - [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Build Names
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# LIMEGREEN Alternate items
THEME_LIMEGREEN = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR_LIMEGREEN)
# YELLOW Alternate items
THEME_YELLOW = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR_YELLOW)
# Current Build Header
THEME4 = u'[COLOR {color1}]Current Build:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# White text theme
THEME6 = u'[COLOR {COLOR_WHITE}]{{}}[/COLOR]'.format(COLOR_WHITE=COLOR_WHITE)

# Message for Contact Page
HIDECONTACT = 'Yes'
CONTACT = 'Thank you for choosing Amadeus Wizard'
CONTACTICON = os.path.join(ART, 'qricon.png')
CONTACTFANART = 'http://'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
AUTOUPDATE = 'Yes'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
AUTOINSTALL = 'Yes'
REPOID = 'repository.amadeuswizard'
REPOADDONXML = 'https://raw.githubusercontent.com/jacquelynnale/Amadeus/main/addons.xml'
REPOZIPURL = 'https://raw.githubusercontent.com/jacquelynnale/Amadeus/main/zips/repository.amadeuswizard/'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
ENABLE = 'Yes'
NOTIFICATION = 'https://raw.githubusercontent.com/jacquelynnale/Amadeus/main/wizard/assets/notification.txt'
HEADERTYPE = 'Text'
FONTHEADER = 'Font14'
HEADERMESSAGE = 'Amadeus Wizard'
HEADERIMAGE = 'http://'
FONTSETTINGS = 'Font13'
BACKGROUND = 'http://'
#########################################################
