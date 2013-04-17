Qemu networking setup
#####################
:date: 2009-02-16 11:25
:tags: vde, qemu, tap, networking

::

    ------------        ----------
    |           |      |  Guest  |
    | Host  ----+------+-----    |
    |      |    | Hub  |     |   |
    |      |tap0|      |tap1 |   |
    |      |-----+-----+-----|   |
    | eth0      |      |         |
    |   |       |      |         |
    ----+-------       ----------
     |
    (Internet)
    
    Host
    * Add a hub
    # vde_switch  -x -d -tap tap0 -tap tap1
    * Assign ip to host's nic
    # ifconfig tap0 192.168.1.1
    * Setup ip forwarding
    Modify /etc/sysctl.conf
    net.ipv4.ip_forward=1
    * Setup masquerading
    # iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
    * Fire qemu
    # vdeqemu -m 1024 -localtime /vm//jos_8.04_01/jos_8.04_01.img
    
    Guest
    # ifconfig eth0 192.168.1.2
    # route add default gw 192.168.1.1
    # vi /etc/resolv.com
    # ping google.com
