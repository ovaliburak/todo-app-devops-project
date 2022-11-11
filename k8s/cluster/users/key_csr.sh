#!/bin/bash
openssl genrsa -out sample.key 2048 \
&& openssl req -new -key sample.key -out sample.csr -subj "/CN=sample@team.in/O=sample" \
&& openssl genrsa -out senior.key 2048 \
&& openssl req -new -key senior.key -out senior.csr -subj "/CN=senior@team.in/O=senior" \


