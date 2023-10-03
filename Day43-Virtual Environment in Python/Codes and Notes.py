#useful when working on projects that have conflicting package versions or package that are not compatible with each other

#Create a virtual environment
#python -m venv myenv  --> myvenv is folder name and can be any name

#Activate the virtual environment (Mac/Linux)
# source myenv/bin/activate

#Activate the virtual environment (windows)
# myenv\Scripts\activate.bat -->if cmd
# myenv\Scripts\activate.ps1  --> if powershell

#Deactivate virtual env
#deactivate

#to see the installed package in the virtual env
# pip freeze

#to see the installed package in the virtual env in txt file
# pip freeze > requirements.txt

#Install the packages installed in requirements.txt
# pip install -r requirements.txt

