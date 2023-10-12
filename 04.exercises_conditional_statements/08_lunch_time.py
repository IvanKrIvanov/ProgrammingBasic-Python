import math

serial_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
rest_time = break_length / 4
watch_time = break_length - lunch_time - rest_time

if watch_time >= episode_length:
    free_time = math.ceil(watch_time - episode_length)
    print(f"You have enough time to watch {serial_name} and left with {free_time} minutes free time.")
else:
    needed_time = math.ceil(episode_length - watch_time)
    print(f"You don't have enough time to watch {serial_name}, you need {needed_time} more minutes.")
