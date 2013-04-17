Configuring your ubuntu for faster internet access
##################################################
:date: 2011-02-04 15:57
:tags: linux, squid, dnsmasq, proxy

While there is a lot already written here my quick howto 

.. code:: bash

    $ sudo bash
    # apt-get install dnsmasq squid
    # echo "listen-address=127.0.0.1" >> /etc/dnsmasq.conf
    # echo "no-dhcp-interface=" >> /etc/dnsmasq.conf
    # vi /etc/dhcp3/dhclient.conf 
    # # ^ uncomment line #prepend domain-name-servers 127.0.0.1;
    # vi /etc/resolv.conf  # Add nameserver 127.0.0.1 
    # /etc/init.d/dnsmasq restart
    # vi /etc/squid/squid.conf 
    
    http_port 3128
    visible_hostname localhost
    
    acl all src 0.0.0.0/0.0.0.0
    
    cache_effective_user proxy
    cache_effective_group proxy
    
    http_access allow all
    icp_access allow all
    
    positive_dns_ttl 1 month
    negative_dns_ttl 1 minute
    httpd_accel_port 80
    httpd_accel_with_proxy on
    httpd_accel_uses_host_header on
    
    cache_dir ufs /cache 400 16 256
    cache_store_log none         
    
    
    # mkdir /cache # I have this dir on reizerfs partition
    # chown proxy.proxy /cache
    
    # /etc/init.d/squid restart

Configure your browser to use 127.0.0.1:8080.
Also read detailed dnsmasq setup article
http://ubuntu.wordpress.com/2006/08/02/local-dns-cache-for-faster-browsing/
