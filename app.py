import random as rand
import time
while True:
    print(rand.randint(1,6))
    time.sleep(1)
    if keyboard.is_pressed('enter'):
        break
