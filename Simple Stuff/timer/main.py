#TODO 
# Improve user validation
# Better error messages


import time
import math


def check_input(value):
    if value == "":
        return 0
    try:
        val = int(value)
        if val < 0:
            return None
        return val
    except ValueError:
        return None


def set_timer():
    print("Setting the timer")
    total_timer_in_seconds = 0
    while True:
        # TODO Improve so the user doesn't have to keep entering numbers if the previous was valid
        # TODO Small validation helper (prompt_till_valid)
        hours = input("How many hours: ")
        hours = check_input(hours)
        if hours is None:
            print("Invalid Entry")
            continue

        minutes = input("How many minutes: ")
        minutes = check_input(minutes)
        if minutes is None:
            print("Invalid Entry")
            continue

        seconds = input("How many seconds: ")
        seconds = check_input(seconds)
        if seconds is None:
            print("Invalid Entry")
            continue

        total_timer_in_seconds = (hours * 3600) + (minutes * 60) + seconds
        break
    return total_timer_in_seconds

def seconds_to_h_m_s_mod(total_timer_in_seconds):
    hours = total_timer_in_seconds // 3600
    minutes = (total_timer_in_seconds % 3600) // 60
    seconds = (total_timer_in_seconds % 60)
    print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")

def seconds_to_h_m_s_subtract(total_timer_in_seconds):
    remaining = total_timer_in_seconds
    hours = remaining // 3600
    remaining -= (hours*3600)
    minutes = remaining // 60
    remaining -= (minutes * 60)
    seconds = remaining
    print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")

def start_timer(time_value):
    start_time = time.monotonic()
    now = start_time
    deadline = start_time + time_value
    last_whole = time_value
    while now < deadline:
        now = time.monotonic()
        time.sleep(0.01)
        remaining = max(0, deadline - now)
        whole = math.floor(remaining)
        if whole != last_whole:
            last_whole = whole
            seconds_to_h_m_s_mod(last_whole)


def main():
    time_value = set_timer()
    seconds_to_h_m_s_mod(time_value)
    start_timer(time_value)


if __name__ == "__main__":
    main()
