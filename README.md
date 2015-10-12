# provisioning

Scripts &amp; Tools for Physical or Virtual Server Provisioning.


## Build CentOS/RHEL 6.x Kickstart

Edit the `variables` file and run `build_ks.sh` with the kickstart template:
~~~
$ ../tools/build_ks.sh centos6.tml
~~~


## TODOs

 - use `variables` file as parameter for build script
 - centos6: Disable IPv6 as an option 
 - centos6: Add hostname on `/etc/hosts`


## References

 - [RHEL 6 Kickstart Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Installation_Guide/s1-kickstart2-options.html)
