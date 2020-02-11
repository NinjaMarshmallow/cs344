from lab1.gps import gps
import logging
# Jason Klaassen CS344 Lab 1
# The Raspberry Pi configuration problem
# In order to enable wifi as an entry point to the pi
# you need to configure the network settings, then reboot the pi
# So the end state has the pi both running with wifi ready to go, but
# requires the advanced technique of erasing the progress of the goal
# of having the pi booted in order to reach the finish state that the
# GPS cannot figure out. To be fair this stumped many a CS300 student
# including myself for some time.
problem = {
    "start": ["pi is booted", "wifi disabled","network unconfigured"],
    "finish": ["pi is booted", "wifi enabled", "network configured"],
    "ops": [
    {
        "action": "sudo configure network",
        "preconds": ["pi is booted", "network unconfigured"],
        "add": ["network configured"],
        "delete": ["network unconfigured"]
    },
    {
        "action": "sudo halt",
        "preconds": ["pi is booted"],
        "add": ["pi is off"],
        "delete": ["pi is booted"]
    },
    {
        "action": "reset wifi adapter",
        "preconds": ["pi is off", "network configured"],
        "add" : ["wifi enabled"],
        "delete": ["wifi disabled"]
    },
    {
        "action": "press power button",
        "preconds": ["pi is off"],
        "add": ["pi is booted"],
        "delete": ["pi is off"]
    },

    ]
}

def main():
    start = problem['start']
    finish = problem['finish']
    ops = problem['ops']
    logging.basicConfig(level=logging.DEBUG)
    # The GPS cannot solve this raspberry pi configuration problem because
    # it does not allow for a goal condition to be undone
    # in order to complete both that goal and a second goal condition
    # Thus it returns a NoneType object
    for action in gps(start, finish, ops):
        print(action)

if __name__ == '__main__':
    main()