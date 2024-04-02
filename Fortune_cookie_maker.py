import random

Random_thingss = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]

def fortune():
  random_fortune = random.randint(0, len(Random_thingss) - 1)

  if random_fortune == 0:
    Random_things = Random_thingss[0]
  elif random_fortune == 1:
    Random_things = Random_thingss[1]
  elif random_fortune == 2:
    Random_things = Random_thingss[2]
  elif random_fortune == 3:
    Random_things = Random_thingss[3]
  elif random_fortune == 4:
    Random_things = Random_thingss[4]
  elif random_fortune == 5:
    Random_things = Random_thingss[5]
  elif random_fortune == 6:
    Random_things = Random_thingss[6]
  elif random_fortune == 7:
    Random_things = Random_thingss[7]
  elif random_fortune == 8:
    Random_things = Random_thingss[8]
  else:
    Random_things = 'Error'

  print(Random_things)

fortune()
fortune()
fortune()