name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.4 # inches to cm
weight = 180.0 * 0.45 # lbs to kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d cm tall." % height
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
