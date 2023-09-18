# DS5111_FALL2023_SW2_Lab

**1.** What did you have to do to get make to work?

I reused my environment from the last lab, so I already had make installed on the ubuntu server. But if I didn't I would have had to have called sudo apt update and then sudo apt install make. The first to update apt, and then the second to install make.

**2.** Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)
The virtual environment was not created successfully because ensurepip is not available.  On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.
apt install python3.10-venv
    
I ran the command that was indicated from the error message to resolve the error. It would have been a lot of googling to figure out that error without the clear error message.

**3.** Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a ;
  
Make interprets each line as it's own command line call. With the commands on seperate lines the install and python call would be run without going into the virtual environment. So your python setup would not be based on the version and packages we installed, but instead what you have in the standard locations on your machine.

**5.** As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this?
  
The job would not run, becasue make would recognize there is a run file that exists. If we wanted to fix this we could a .PHONY: run
  
This would ensure that command runs regardless of whether a file exists with that name or not.

**7.** The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?
  
This line sys.path.append(".") line adds the current directory to the list of directories Python will look to to find modules. Without this we would not be able to import the clockdeco_param. To use sys.path.append we have to first import the sys module, which is what import sys does.

**8.** Execute sudo apt install tree, and use that application to print out the file and directory structure, just as it is shown in this document at the top. You will have to look up in the reading, or google it in stackoverflow, what flag you need to exclude the 'env' directory. No need to cut and paste the structure, just include the full line you used to get it working.

tree -I env

**9.** Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in __pycache__ folders. What is the meaning of the **/* ?

This is as wildcard used to represent any file path from the working directory to the __pychache__ directories. It allows gitignore to ignore them even if they are in a subdirectory of our current working directory. 

**10.**

Adding versions to requirements.txt

**11.** In the sample code from the book, why does the line if __name__=="__main__": allow the script to run if called directly, but not otherwise? What's going on there?

This returns true only if the current file is the one that we called directly the command line. It won't return true if that file was used for importing a module or something similar. __name__ is the name of the current file, "__main__" is the name of the file called from the command line.

**12.** You would not see the print below the if __name__... line if you do an import of the file. You would see both if calling the file directly. Thsi is becasue the __name__... lien only returns true if the file is called directly.


