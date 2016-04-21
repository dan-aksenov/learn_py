from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
 
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
         
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out last scene
        current_scene.enter()
           
class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
 
class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invided your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put in in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapoons Armory when"
	print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapoon to blast you."

        action = raw_input("> ")
        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire in at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "Your aim. You laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costure his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer, you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgt nebhag gur ubhfr, fur fvgf ne bhaq fur ubhfr."
            print "The Gothon stomps, tries not to laugh, then bursts out laughing and can't move."
            print "While he's laughing you run up adn shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'       
class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):


    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()  
