# provisioning/kickstarts

Create your [kickstart](http://fedoraproject.org/wiki/Anaconda/Kickstart) files for automated/unattended
RHEL/CentOS 6.x &amp; 7.x installations.

> **NOTE**: For the network interfaces, the old naming convention is used. Which makes the network
> interfaces end up with names *eth0*, *eth1*, etc.


## Quick-Start

 1. Create your specific `variables` file out of the template
 2. Run `ks_build.py`, selecting one of the CentOS templates, as below:
    ~~~
    $ ../tools/ks_build.py -v variables-webServer1.tmpl centos6.tmpl > centos6_webServer1.ks
    ~~~
 3. Copy the kickstart file on a floppy-disk (image) as `ks.cfg`
 4. Add the floppy-disk on you server
 5. Boot from the related (CentOS 6.x or 7.x) ISO, using the below boot parameters:
    + RHEL 6.x: `ks=floppy`
    + RHEL 7.x: `net.ifnames=0 biosdevname=0 ks=hd:fd0:/ks.cfg`


## References

 - [RHEL 7 Kickstart Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/chap-kickstart-installations)
 - [RHEL 6 Kickstart Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Installation_Guide/s1-kickstart2-options.html)
 - [Cheetah Users' Guide](http://www.cheetahtemplate.org/docs/users_guide_html)
