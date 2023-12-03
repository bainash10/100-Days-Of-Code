# regular expression wont be used for basic programs
# Used to make the programming easier for long codes
import re #built in module

pattern = r"[A-Z]+yclone" #checks A-Z any character that is in Capital Letters, + is one or more occurances
text = '''
In meteorology, a cyclone is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.[5] Mesocyclones, tornadoes, and dust devils lie within the smaller mesoscale.[6] Upper level cyclones can exist without the presence of a surface low, and can pinch off from the base of the tropical upper tropospheric trough during the summer months in the Northern Hemisphere. Dyclones Cyclones have also been seen on extraterrestrial planets, such as Mars, Jupiter, and Neptune.[7][8] Cyclogenesis is the process of cyclone formation and intensification.[9] Extratropical cyclones begin as waves in large regions of enhanced mid-latitude temperature contrasts called baroclinic zones. These zones contract and form weather fronts as the cyclonic circulation closes and intensifies. Later in their life cycle, extratropical cyclones occlude as cold air masses undercut the warmer air and become cold core systems. A cyclone's track is guided over the course of its 2 to 6 day life cycle by the steering flow of the subtropical jet stream.
'''

match=re.search(pattern,text) #it will check the pattern in the above text for single occurance
print("------------------------")
match1= re.finditer(pattern,text) #it will check every pattern
print(match)

for match in match1:
    # print(match.span())
    print(match) 

    # type of match.span() is tuple


#Metacharacters in regular expression
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
''' ?   Matches zero or one occurrence.'''
# |   Means OR (Matches with any of the characters
#     separated by it.
''' *   Any number of occurrences (including 0 occurrences)'''
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs