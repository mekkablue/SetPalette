# encoding: utf-8
from __future__ import division, print_function, unicode_literals

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
import traceback

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
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': u'Set Palette',
			'de': u'Formatsatz-Palette'
		})
		self.dialogName = self.name
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
	
	@objc.python_method
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

	@objc.IBAction
	def setStylisticSet_( self, sender ):
		editTab = Glyphs.font.currentTab
		if editTab:
			setNumber = int(sender.title())
			featureTag = "ss%02i" % setNumber
			# Store value coming in from dialog
			setPref = 'com.mekkablue.SetPalette.%s' % featureTag
			Glyphs.defaults[setPref] = sender.intValue()
			if Glyphs.defaults[setPref]:
				self.activateFeature(featureTag, editTab)
			else:
				self.deactivateFeature(featureTag, editTab)
			self.updateTab(editTab)
	
	@objc.IBAction
	def allOn_( self, sender ):
		for i in range(20):
			setNumber = "%02i" % (i+1)
			featureTag = "ss%s" % setNumber
			Glyphs.defaults["com.mekkablue.SetPalette.%s"%featureTag] = 1
			eval("self.%sfield"%featureTag).setIntValue_(1)
		self.updateFeatures()
	
	@objc.IBAction
	def allOff_( self, sender ):
		for i in range(20):
			setNumber = "%02i" % (i+1)
			featureTag = "ss%s" % setNumber
			Glyphs.defaults["com.mekkablue.SetPalette.%s"%featureTag] = 0
			eval("self.%sfield"%featureTag).setIntValue_(0)
		self.updateFeatures()
	
	@objc.IBAction
	def applySets_( self, sender ):
		self.updateFeatures()
	
	@objc.python_method
	def updateFeatures(self):
		font = Glyphs.font
		editTab = font.currentTab
		if editTab:
			for i in range(20):
				setNumber = "%02i" % (i+1)
				featureTag = "ss%s" % setNumber
				if Glyphs.defaults["com.mekkablue.SetPalette.%s"%featureTag] == 0:
					self.deactivateFeature(featureTag, editTab)
				else:
					self.activateFeature(featureTag, editTab)
			self.updateTab(editTab)
	
	@objc.python_method
	def updateTab( self, editTab ):
		editTab.graphicView().reflow()
		editTab.graphicView().layoutManager().updateActiveLayer()
		editTab._updateFeaturePopup()
		editTab.updatePreview()
	
	@objc.python_method
	def activateFeature( self, featureTag, editTab ):
		try:
			if not featureTag in editTab.features:
				editTab.features.append(featureTag)
			return True

		except Exception as e:
			print(e)
			print(traceback.format_exc())
			return False
	
	@objc.python_method
	def deactivateFeature( self, featureTag, editTab ):
		try:
			if featureTag in editTab.features:
				editTab.features.remove(featureTag)
			return True

		except Exception as e:
			print(e)
			print(traceback.format_exc())
			return False
	
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
