# DS5111_FALL2023_SW2_Lab

1. What did you have to do to get make to work?
\\ 
I reused my environment from the last lab, so I already had make installed on the ubuntu server. But if I didn't I would have had to have called sudo apt update and then sudo apt install make. The first to update apt, and then the second to install make.

2. Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)
  The virtual environment was not created successfully because ensurepip is not available.  On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.
apt install python3.10-venv
  
I ran the command that was indicated from the error message to resolve the error. It would have been a lot of googling to figure out that error without the clear error message.

3. Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;
  
Make interprets each line as it's own command line call. With the commands on seperate lines the install and python call would be run without going into the virtual environment. So your python setup would not be based on the version and packages we installed, but instead what you have in the standard locations on your machine.

5. As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?
  
The job would not run, becasue make would recognize there is a run file that exists. If we wanted to fix this we could a .PHONY: run
  
This would ensure that command runs regardless of whether a file exists with that name or not.

7. The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?
  
This line sys.path.append(".") line adds the current directory to the list of directories Python will look to to find modules. Without this we would not be able to import the clockdeco_param. To use sys.path.append we have to first import the sys module, which is what import sys does.
