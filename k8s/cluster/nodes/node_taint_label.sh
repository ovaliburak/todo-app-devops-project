#!/bin/bash
node1=$(kubectl get no -o jsonpath="{.items[1].metadata.name}") \
&& node2=$(kubectl get no -o jsonpath="{.items[2].metadata.name}") \
&& node3=$(kubectl get no -o jsonpath="{.items[3].metadata.name}") \
&& kubectl taint node $node1 tier=prod:NoSchedule \
&& kubectl taint node $node1 service=django:NoSchedule \
&& kubectl taint node $node2 tier=prod:NoSchedule \
&& kubectl taint node $node2 service=nodejs:NoSchedule \
&& kubectl taint node $node3 tier=prod:NoSchedule \
&& kubectl label node $node1 tier=prod \
&& kubectl label node $node2 tier=prod \
&& kubectl label node $node3 tier=prod
