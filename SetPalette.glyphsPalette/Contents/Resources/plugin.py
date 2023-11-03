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
	prefID = "com_mekkablue_SetPalette"

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
	def featureTag(self, featureIdx):
		return f"ss{featureIdx:02}"

	@objc.python_method
	def prefKey(self, featureIdx):
		return self.prefID + "_" + self.featureTag(featureIdx)

	@objc.python_method
	def getPref(self, featureIdx):
		prefKey = self.prefKey(featureIdx)
		return Glyphs.defaults[prefKey]

	@objc.python_method
	def setPref(self, featureIdx, value):
		prefKey = self.prefKey(featureIdx)
		Glyphs.defaults[prefKey] = value

	@objc.python_method
	def start(self):
		pass

	@objc.IBAction
	def setStylisticSet_(self, sender):
		editTab = Glyphs.font.currentTab
		if editTab:
			setNumber = int(sender.title())
			featureTag = self.featureTag(setNumber)
			if self.getPref(setNumber):
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
	def switchAll(self, onOff=1):
		for i in range(21):
			self.setPref(i, onOff)
		self.updateFeatures()

	@objc.IBAction
	def applySets_(self, sender):
		self.updateFeatures()

	@objc.python_method
	def updateFeatures(self):
		font = Glyphs.font
		editTab = font.currentTab
		if editTab:
			for i in range(21):
				featureTag = self.featureTag(i)
				if self.getPref(i) == 0:
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
