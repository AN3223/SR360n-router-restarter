# SR360n-router-restarter
A script for automatically restarting the SR360n SmartRG router based on how long your internet is down. This does not work for other routers.
## How does it work?
It restarts the router through the admin control panel on 192.168.1.1, and it will only do so if the internet has been down 40% of the time in the last 15 minutes. You must have Selenium for Python installed with the Chrome driver ready to go.
## What can I customize?
The password for the router and the length of the timer are both easily accessible variables. Default password is "admin", just like the router, and default timer is 15 minutes. You can also change the IP or domain to ping by modifying how the ping() function is called from main().
