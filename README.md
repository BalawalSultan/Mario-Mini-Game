# Mario Mini Game

## Brief introduction

In this game Mario must save the princess that has been kidnapped by Bowser and his friends.
Mario must use the [SenseHat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) joystick to move on the map, but be careful not to fall of the yellow path or you will start from the beginning of the map. Mario must fight three boss battles before being able to save the princess, each boss will say something to Mario when he meets them using [google text to speech](https://cloud.google.com/text-to-speech). During each boss battle Mario can see his health on the [SenseHat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) LED matrix  and also the health of the boss, but only when the boss gets hit, and must decide on wether to heal himself or attack the boss. The bosses follow the rules so they will wait for Mario to finish his turn before attacking him. After each boss battle Mario will get stronger and recive two healing potions. After defeating all the bosses Mario reach the princess and the game will be over. All throughout the game there will be background music playing using [pygame](https://www.pygame.org/wiki/about).

## Technologies used in the project

In this project I used:
* [Raspberry SenseHat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)
to display the map and handle player movement.
* [google text to speech](https://cloud.google.com/text-to-speech) to say cheesy lines such as 
 `My new country has no need for old superstars! It will do just fine with only one: the Great Bowletta!!!`
* [pygame](https://www.pygame.org/wiki/about) to play background music