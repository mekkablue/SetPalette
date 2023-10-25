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

	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': u'Set Palette',
			'de': u'Formatsatz-Palette',
		})
		self.dialogName = self.name
		self.loadNib('IBdialog', __file__)
	
	@objc.python_method
	def start(self):
		pass

	@objc.IBAction
	def setStylisticSet_(self, sender):
		editTab = Glyphs.font.currentTab
		if editTab:
			setNumber = int(sender.title())
			featureTag = "ss%02i" % setNumber
			setPref = 'com.mekkablue.SetPalette.%s' % featureTag
			if Glyphs.defaults[setPref]:
				self.activateFeature(featureTag, editTab)
			else:
				self.deactivateFeature(featureTag, editTab)
			self.updateTab(editTab)
	
	@objc.IBAction
	def allOn_(self, sender):
		for i in range(20):
			setNumber = "%02i" % (i + 1)
			featureTag = "ss%s" % setNumber
			Glyphs.defaults["com.mekkablue.SetPalette.%s" % featureTag] = 1
		self.updateFeatures()
	
	@objc.IBAction
	def allOff_(self, sender):
		for i in range(20):
			setNumber = "%02i" % (i + 1)
			featureTag = "ss%s" % setNumber
			Glyphs.defaults["com.mekkablue.SetPalette.%s" % featureTag] = 0
		self.updateFeatures()
	
	@objc.IBAction
	def applySets_(self, sender):
		self.updateFeatures()
	
	@objc.python_method
	def updateFeatures(self):
		font = Glyphs.font
		editTab = font.currentTab
		if editTab:
			for i in range(20):
				setNumber = "%02i" % (i+1)
				featureTag = "ss%s" % setNumber
				if Glyphs.defaults["com.mekkablue.SetPalette.%s" % featureTag] == 0:
					self.deactivateFeature(featureTag, editTab)
				else:
					self.activateFeature(featureTag, editTab)
			self.updateTab(editTab)
	
	@objc.python_method
	def updateTab(self, editTab):
		editTab.graphicView().reflow()
		editTab.graphicView().layoutManager().updateActiveLayer()
		editTab._updateFeaturePopup()
		editTab.updatePreview()
	
	@objc.python_method
	def activateFeature(self, featureTag, editTab):
		try:
			if not featureTag in editTab.features:
				editTab.features.append(featureTag)
			return True

		except Exception as e:
			print(e)
			print(traceback.format_exc())
			return False
	
	@objc.python_method
	def deactivateFeature(self, featureTag, editTab):
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
