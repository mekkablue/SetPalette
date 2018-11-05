# encoding: utf-8

###########################################################################################################
#
#
#	Palette Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Palette
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class SetPalette (PalettePlugin):
	
	dialog = objc.IBOutlet()
	
	ss01field = objc.IBOutlet()
	ss02field = objc.IBOutlet()
	ss03field = objc.IBOutlet()
	ss04field = objc.IBOutlet()
	ss05field = objc.IBOutlet()
	ss06field = objc.IBOutlet()
	ss07field = objc.IBOutlet()
	ss08field = objc.IBOutlet()
	ss09field = objc.IBOutlet()
	ss10field = objc.IBOutlet()
	ss11field = objc.IBOutlet()
	ss12field = objc.IBOutlet()
	ss13field = objc.IBOutlet()
	ss14field = objc.IBOutlet()
	ss15field = objc.IBOutlet()
	ss16field = objc.IBOutlet()
	ss17field = objc.IBOutlet()
	ss18field = objc.IBOutlet()
	ss19field = objc.IBOutlet()
	ss20field = objc.IBOutlet()
	
	allOnButton = objc.IBOutlet()
	allOffButton = objc.IBOutlet()
	reapplyButton = objc.IBOutlet()
	
	def settings(self):
		self.name = Glyphs.localize({
			'en': u'Set Palette',
			'de': u'Formatsatz-Palette'
		})
		self.dialogName = self.name
		# Load .nib dialog (without .extension)
		
		Glyphs.registerDefaults({
			"com.mekkablue.SetPalette.ss01": 0,
			"com.mekkablue.SetPalette.ss02": 0,
			"com.mekkablue.SetPalette.ss03": 0,
			"com.mekkablue.SetPalette.ss04": 0,
			"com.mekkablue.SetPalette.ss05": 0,
			"com.mekkablue.SetPalette.ss06": 0,
			"com.mekkablue.SetPalette.ss07": 0,
			"com.mekkablue.SetPalette.ss08": 0,
			"com.mekkablue.SetPalette.ss09": 0,
			"com.mekkablue.SetPalette.ss10": 0,
			"com.mekkablue.SetPalette.ss11": 0,
			"com.mekkablue.SetPalette.ss12": 0,
			"com.mekkablue.SetPalette.ss13": 0,
			"com.mekkablue.SetPalette.ss14": 0,
			"com.mekkablue.SetPalette.ss15": 0,
			"com.mekkablue.SetPalette.ss16": 0,
			"com.mekkablue.SetPalette.ss17": 0,
			"com.mekkablue.SetPalette.ss18": 0,
			"com.mekkablue.SetPalette.ss19": 0,
			"com.mekkablue.SetPalette.ss20": 0,
		})
		
		self.loadNib('IBdialog', __file__)
	
	def start(self):
		self.ss01field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss01"])
		self.ss02field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss02"])
		self.ss03field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss03"])
		self.ss04field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss04"])
		self.ss05field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss05"])
		self.ss06field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss06"])
		self.ss07field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss07"])
		self.ss08field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss08"])
		self.ss09field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss09"])
		self.ss10field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss10"])
		self.ss11field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss11"])
		self.ss12field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss12"])
		self.ss13field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss13"])
		self.ss14field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss14"])
		self.ss15field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss15"])
		self.ss16field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss16"])
		self.ss17field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss17"])
		self.ss18field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss18"])
		self.ss19field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss19"])
		self.ss20field.setIntValue_(Glyphs.defaults["com.mekkablue.SetPalette.ss20"])

		# Adding a callback for the 'GSUpdateInterface' event
		#Glyphs.addCallback(self.update, UPDATEINTERFACE)
	
	def __del__(self):
		#Glyphs.removeCallback(self.update)
		pass

	def update( self, sender ):
		# Extract font from sender
		font = sender.object()

		# Update the palette
		if font.currentTab:
			for i in range(1,21):
				setNumber = "%02i" % i
				featureTag = "ss%s" % setNumber
				if featureTag in font.currentTab.selectedFeatures():
					pass
					# turn on checkboxes in palette
				else:
					pass
					# turn off checkboxes in palette
	
	# Action triggered by UI
	@objc.IBAction
	def setStylisticSet_( self, sender ):
		if Glyphs.font.currentTab:
			setNumber = int(sender.title())
			featureTag = "ss%02i" % setNumber
			# Store value coming in from dialog
			setPref = 'com.mekkablue.SetPalette.%s' % featureTag
			Glyphs.defaults[setPref] = sender.intValue()
			if Glyphs.defaults[setPref]:
				self.activateFeature(featureTag, Glyphs.font.currentTab)
			else:
				self.deactivateFeature(featureTag, Glyphs.font.currentTab)
			# Trigger redraw
			# self.update(sender)
	
	@objc.IBAction
	def allOn_( self, sender ):
		for i in range(1,21):
			setNumber = "%02i" % i
			featureTag = "ss%s" % setNumber
			Glyphs.defaults["com.mekkablue.SetPalette.%s"%featureTag] = 1
			eval("self.%sfield"%featureTag).setIntValue_(1)
			self.updateFeatures()
	
	@objc.IBAction
	def allOff_( self, sender ):
		for i in range(1,21):
			setNumber = "%02i" % i
			featureTag = "ss%s" % setNumber
			Glyphs.defaults["com.mekkablue.SetPalette.%s"%featureTag] = 0
			eval("self.%sfield"%featureTag).setIntValue_(0)
			self.updateFeatures()
	
	@objc.IBAction
	def applySets_( self, sender ):
		self.updateFeatures()
	
	def updateFeatures(self):
		font = Glyphs.font
		if font.currentTab:
			for i in range(1,21):
				setNumber = "%02i" % i
				featureTag = "ss%s" % setNumber
				if Glyphs.defaults["com.mekkablue.SetPalette.%s"%featureTag] == 0:
					self.deactivateFeature(featureTag, font.currentTab)
				else:
					self.activateFeature(featureTag, font.currentTab)
	
	def updateTab( self, editTab ):
		editTab.graphicView().reflow()
		editTab.graphicView().layoutManager().updateActiveLayer()
		editTab._updateFeaturePopup()
		editTab.updatePreview()
	
	def activateFeature( self, featureTag, editTab ):
		try:
			if not featureTag in editTab.selectedFeatures():
				editTab.selectedFeatures().append(featureTag)
			self.updateTab(editTab)
			return True

		except Exception, e:
			print e
			print traceback.format_exc()
			return False
			
	def deactivateFeature( self, featureTag, editTab ):
		try:
			if featureTag in editTab.selectedFeatures():
				editTab.selectedFeatures().remove(featureTag)
			self.updateTab(editTab)
			return True

		except Exception, e:
			print e
			print traceback.format_exc()
			return False
	
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	
	# Temporary Fix
	# Sort ID for compatibility with v919:
	_sortID = 0
	def setSortID_(self, id):
		try:
			self._sortID = id
		except Exception as e:
			self.logToConsole( "setSortID_: %s" % str(e) )
	def sortID(self):
		return self._sortID
	