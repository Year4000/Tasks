#! /usr/bin/python

import os, sys, subprocess


''' Run a command '''
def runCmd(cmd):
    subprocess.call(cmd,  shell=True)


''' Import a task from the tasks folder '''
def importTask(name):
    try:
        with open('tasks/{}.py'.format(name)) as file_task:
            exec(''.join(file_task.readlines()))
    except IOError as error:
        print('There is no task by: {}'.format(arg))


# Make sure there are tasks to run
if len(sys.argv) <= 1:
    print('You must give a task name as the argument(s).')
    sys.exit(1)
# Process the rest of the tasks
else:
    for arg in sys.argv[1:]:
        importTask(arg)
