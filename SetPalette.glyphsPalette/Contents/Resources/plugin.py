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
	prefID = "com.mekkablue.SetPalette"
	
	dialog = objc.IBOutlet()

	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'Set Palette',
			'de': 'Formatsatz-Palette',
		})
		self.dialogName = self.name
		self.loadNib('IBdialog', __file__)
	
	@objc.python_method
	def domain(self, prefName):
		prefName = prefName.strip().strip(".")
		return self.prefID + "." + prefName.strip()
	
	@objc.python_method
	def pref(self, prefName):
		prefDomain = self.domain(prefName)
		return Glyphs.defaults[prefDomain]
	
	@objc.python_method
	def start(self):
		pass

	@objc.IBAction
	def setStylisticSet_(self, sender):
		editTab = Glyphs.font.currentTab
		if editTab:
			setNumber = int(sender.title())
			featureTag = self.ssXX(setNumber)
			setPref = self.domain(featureTag)
			if Glyphs.defaults[setPref]:
				self.activateFeature(featureTag, editTab)
			else:
				self.deactivateFeature(featureTag, editTab)
			self.updateTab(editTab)
	
	@objc.IBAction
	def allOn_(self, sender):
		self.switchAll(onOff=1)
	
	@objc.IBAction
	def allOff_(self, sender):
		self.switchAll(onOff=0)
	
	@objc.python_method
	def ssXX(self, setNumber):
		return f"ss{setNumber:02}"
	
	@objc.python_method
	def switchAll(self, onOff=1):
		for i in range(20):
			featureTag = self.ssXX(i+1)
			Glyphs.defaults[self.domain(featureTag)] = onOff
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
				featureTag = self.ssXX(i+1)
				value = self.pref(featureTag)
				if value == 0:
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
