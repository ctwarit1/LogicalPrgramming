"""
YouTube offers different playback speed options for users.
This allows users to increase or decrease the speed of the
 video content. Given the actual duration and playback
 speed of the video, calculate the playback duration of the video.
Examples
playback_duration("00:30:00", 2) ➞ "00:15:00"
playback_duration("01:20:00", 1.5) ➞ "00:53:20"
playback_duration("51:20:09", 0.5) ➞ "102:40:18"
Notes
Both durations will be in hh:mm:ss format.
Playback speed will be up to one decimal place only.
Time units are expected to be truncated/floored.
"""


def playback_duration(time, speed):
    in_list = time.split(":")
    hours_sec = int(in_list[0]) * 3600
    minutes_sec = int(in_list[1]) * 60
    sec = int(in_list[2])

    tot_sec = hours_sec + minutes_sec + sec
    calc_time = tot_sec / speed
    rem = calc_time % 60

    in_list[2] = round(rem)
    in_list[1] = round(calc_time // 60)

    if in_list[1] > 60:

        in_list[0] = round(calc_time // 3600)
        in_list[1] = round(calc_time % 3600) // 60
        in_list[2] = round(rem)

    else:

        in_list[0] = 00

    print(f"{in_list[0]}:{in_list[1]}:{in_list[2]}")


playback_duration("00:30:00", 2)
playback_duration("01:20:00", 1.5)
playback_duration("51:20:09", 0.5)
