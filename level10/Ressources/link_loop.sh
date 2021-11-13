#!/bin/bash

while true; do
	touch /tmp/link
	ln -s -f /home/user/level10/token /tmp/link
	rm /tmp/link
done
