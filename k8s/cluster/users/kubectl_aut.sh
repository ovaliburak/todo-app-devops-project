#!/bin/bash
kubectl certificate approve junior \
&& kubectl certificate approve senior \
&& kubectl get csr junior -o jsonpath='{.status.certificate}' | base64 -d >> junior.crt \
&& kubectl get csr senior -o jsonpath='{.status.certificate}' | base64 -d >> senior.crt \
&& kubectl config set-credentials junior@team.in --client-certificate=junior.crt --client-key=junior.key \
&& kubectl config set-credentials senior@team.in --client-certificate=senior.crt --client-key=senior.key \
&& kubectl config set-context junior-ctx --cluster=minikube --user=junior@team.in \
&& kubectl config set-context senior-ctx --cluster=minikube --user=senior@team.in 