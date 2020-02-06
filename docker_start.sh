#!/bin/sh

docker run -it --rm -p 8089:8089 -e TARGET_URL=http://localhost:80  -v ~/workdir/locust_test/locustfile.py:/locustfile.py  locustio/locust:latest sh
