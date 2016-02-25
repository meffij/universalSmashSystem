import pygame
import collections

print "Joystick Test"

pygame.init()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print joysticks

j = joysticks[0]
print j.get_init()
print j.get_id()

j.init()

print j.get_init()
print j.get_id()
print j.get_numaxes()
a = [set() for axis in range(j.get_numaxes())]
print j.get_numbuttons()
# b = [set() for button in range(j.get_numbuttons())]

while True:
	e = pygame.event.get()
	# if len(e) != 0:
		# print len(e)
	for event in e:
		if event.type == pygame.JOYBUTTONDOWN:
			n = event.joy
			for axis in range(j.get_numaxes()):
				print len(a[axis]) 
			# for button in range(j.get_numbuttons()):
				# print j.get_button(button)
			print '\n'
		if event.type == pygame.JOYAXISMOTION:
			n = event.axis
			a[n].add(event.value)
