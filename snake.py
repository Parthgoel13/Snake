import pygame
import sys
import time
import random

class Snake():
	def __init__(self):
		self.position = [100,50]
		self.body = [[100,50],[90,50],[80,50]]
		self.direction = "Right"
		self.changeDirTo3 = self.direction

	def changeDirTo(self,dir):
		if dir == "Right" and  self.direction != "Left":
			self.direction = "Right"
		if dir == "Left" and  self.direction != "Right":
			self.direction = "Left"
		if dir == "Up" and  self.direction != "Down":
			self.direction = "Up"
		if dir == "Down" and self.direction != "Up":
			self.direction = "Down"

	def move(self,foodPos):
		if self.direction == "Right":
			self.position[0] += 10
		if self.direction == "Left":
			self.position[0] -= 10
		if self.direction == "Up":
			self.position[1] += 10
		if self.direction == "Down":
			self.position[1] -= 10
		self.body.insert(0,list(self.position))
		if abs(self.position[0] - foodPos[0])<8 and abs(self.position[1] - foodPos[1])<8:
			return 1
		else:
			self.body.pop()
			return 0

	def checkCollision(self):
		if self.position[0] > 490 or self.position[0] < 0:
			return 1
		elif self.position[1] > 490 or self.position[1] < 0:
			return 1 
		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1
		return 0

	def getHeadPos(self):
		return self.position

	def getbody(self):
		return self.body

class FoodSpawner():
	def __init__(self):
		self.position = [random.randrange(1,500),random.randrange(1,500)]
		self.isFoodOnScreen = True

	def foodSpawn(self):
		if self.isFoodOnScreen == False:
			self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
			self.isFoodOnScreen = True
		return self.position

	def setFoodOnScreen(self,ToF):
		self.isFoodOnScreen = ToF

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("My Snake Game")
fps = pygame.time.Clock()

score = 0

Snake = Snake()
FoodSpawner = FoodSpawner()

def gameOver():
	pygame.quit()
	sys.exit()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver();
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				Snake.changeDirTo('Right')
			if event.key == pygame.K_LEFT:
				Snake.changeDirTo('Left')
			if event.key == pygame.K_DOWN:
				Snake.changeDirTo('Up')
			if event.key ==  pygame.K_UP:
				Snake.changeDirTo('Down')
	foodPos = FoodSpawner.foodSpawn()
	if (Snake.move(foodPos)==1):
		score += 1
		FoodSpawner.isFoodOnScreen = False


	window = pygame.display.set_mode((500,500))
	for pos in Snake.getbody():
		pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
	pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],10,10))
	if (Snake.checkCollision()==1):
		gameOver()
	pygame.display.set_caption("Parth's Snake Game| Score : " + str(score))
	pygame.display.flip()
	fps.tick(15)


