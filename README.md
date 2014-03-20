#Navi-Notify
## Ryan Hunter

Ever tried to get someones attention but they had headphones on? Navi notify is the solution!! Once installed, you can send remote "notifications" that pump the annoying nagging of Navi right into their ear!

http://www.youtube.com/watch?v=0sZ0Yn16Dgg

##Installation

Simply install the egg (sudo python setup.py install) and execute "start-navi"

NOTE: this requires pygame, which at least on ubuntu, is MUCH easier to install from the package repo vs pip (apt-get install python-pygame_
to notify, simply call notify <hostname> from any other machine (you have to install this on the client as well).

There is also a basic directory, you can call notify <name> and it the client will attempt to lookup the persons computer.
