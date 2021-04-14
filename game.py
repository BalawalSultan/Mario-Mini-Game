from sense_emu import SenseHat
from player import Player
from time import sleep
from boss import Boss
import util

sense = SenseHat()

y = [255,255,0] # the path will be made of yellow dots
x = [0,0,0] # black

b1 = [255,0,0] # the boss will be a red dot
b2 = [0,255,0] # the boss2 will be a green dot
b3 = [128,0,0] # the boss3 will be a brown dot

player_dot = [0,0,255] # The player will be a blue dot

p = [255, 255, 255] # The princess

# The three bosses that the player must defeat
bowser = Boss("Bowser", 20, 3, 3, 3)
cackletta = Boss("Cackletta", 40, 7, 5, 4)
bowletta = Boss("Bowletta", 62, 11, 3, 7)

mario = Player() # Player object

isPrincessSave = False # The condition to win the game is if the princess is saved
 
# this list will act as a map
game_map = [
  y,y,x,x,x,x,x,x,
  x,y,x,x,x,x,x,x,
  x,y,x,x,x,x,x,x,
  x,y,y,b1,y,y,x,x,
  x,x,x,x,x,b2,x,x,
  x,y,y,y,y,y,x,x,
  x,y,x,x,x,x,x,x,
  x,y,y,b3,y,y,y,p
]

util.intro() # plays intro sequence
sleep(1)

util.playAudioFile("music/map_music.mp3",-1) # plays map music

while not isPrincessSave:
    sense.set_pixels(game_map)
    sense.set_pixel(mario.x, mario.y, player_dot)

    for event in sense.stick.get_events():
        if event.action == "pressed":

            if event.direction == "left" and mario.x > 0: # condition to move left
                mario.x -= 1

            if event.direction == "right" and mario.x < 7: # condition to move right
                mario.x += 1

            if event.direction == "up" and mario.y > 0: # condition to move up
                mario.y -= 1

            if event.direction == "down" and mario.y < 7: # condition to move down
                mario.y += 1

        current_position = sense.get_pixel(mario.x, mario.y)

        if current_position == x:
            mario.x = 0
            mario.y = 0

        elif util.checkPosition(mario, bowser) and bowser.isAlive():

            util.playAudioFileNoInterruption("music/enemy_encounter.mp3")
            util.bowser()
            result = util.fight(mario, bowser, sense)
            if(result):
                game_map[27] = y # removes the boss from the map
            else:
                bowser = Boss("Bowser", 20, 3, 3, 3) # reset boss stats
                mario = Player() # resets the player position and stats
            
            util.playAudioFile("music/map_music.mp3",-1) # plays map music

        elif util.checkPosition(mario, cackletta) and cackletta.isAlive():

            util.playAudioFileNoInterruption("music/enemy_encounter.mp3")
            util.cackletta()
            result = util.fight(mario, cackletta, sense)
            if(result):
                game_map[37] = y # removes the boss from the map
            else:
                cackletta = Boss("Cackletta", 40, 7, 5, 4) # reset boss stats
                mario = Player() # resets the player position and stats
            
            util.playAudioFile("music/map_music.mp3",-1) # plays map music

        elif util.checkPosition(mario, bowletta) and bowletta.isAlive():

            util.playAudioFileNoInterruption("music/enemy_encounter.mp3")
            util.bowletta()
            result = util.fight(mario, bowletta, sense)
            if(result):
                game_map[59] = y # removes the boss from the map
            else:
                bowletta = Boss("Bowletta", 62, 11, 3, 7) # reset boss stats
                mario = Player() # resets the player position and stats

            util.playAudioFile("music/map_music.mp3",-1) # plays map music
            
        elif mario.x == 7 and mario.y == 7:
            isPrincessSave = True
            break

    sleep(0.2)

sense.show_letter("Y")
sleep(0.4)
sense.show_letter("O")
sleep(0.4)
sense.show_letter("U")
sleep(0.4)

sense.show_message("WON!!")
util.credits()
