# pkg-prime_server
RPM packaging of prime_server for Sailfish 

To get the sources, run `download.sh`

To build and install:

```
export SFARCH=armv7hl
mb2 -t SailfishOS-$SFARCH -s ../rpm/prime_server.spec build
sb2 -t SailfishOS-$SFARCH -m sdk-install -R rpm -i <INSERT-PATH>/prime_server*$SFARCH.rpm
```

