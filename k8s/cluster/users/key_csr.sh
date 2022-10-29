#!/bin/bash
openssl genrsa -out junior.key 2048 \
&& openssl req -new -key junior.key -out junior.csr -subj "/CN=junior@team.in/O=junior" \
&& openssl genrsa -out senior.key 2048 \
&& openssl req -new -key senior.key -out senior.csr -subj "/CN=senior@team.in/O=senior" \


