import pygame
import sys
import time
import random

class Snake():
	def __init__(self):
	self.position = [100,50]
	self.body = [[100,50],[90,50],[80,50]]
	self.direction = "Right"
	self.changeDirTo = self.direction

	def 