Reliance Netconnect Broadband+ on Linux
#######################################
:date: 2010-11-26 02:38
:tags: reliance, linux, broadband

-  It works. Make sure while purchasing you inform them that you use Linux
-  It’s fast and reliable in Pashan, Pune area
-  Below config worked for me on Ubuntu 9.10 AND 10.04
-  There are Linux drivers on the CD but I could not get it working on Ubuntu 9.10.
-  For activation, I had to use Windows :(

::

    sudo apt-get install usb-modeswitch wvdial

    vi /etc/wvdial
    
    [Dialer Defaults]
    Phone = #777
    Password =
    Username =
    Baud = 460800
    Stupid Mode = 1
    New PPPD = 1
    Tonline = 0
    Init1 = ATZ
    Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0
    Modem Type = Analog Modem
    Baud = 460800
    Modem = /dev/ttyUSB0
    ISDN = 0
