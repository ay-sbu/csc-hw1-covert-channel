# Covert Channel (C2) by Timing Channel

Simple sample for attack by transferring data to a receiver by 
Timing Covert Channel. Sender send a nice message but also a 
hidden message that is hide in bit time interval sendings and 
we call this timing intervals that makes zeros and ones Covert
Channel!

## Run

1. first run `ayreceiver.py`:
```shell
python3 ayreceiver.py
```
2. then run `aysender.py`:
```shell
python3 aysender.py
```
3. see results in 2 sides!

> nice message   = '- I love you!'

> hidden message = '- I hack you!'
