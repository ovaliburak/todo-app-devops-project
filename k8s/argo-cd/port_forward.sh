kubectl port-forward \
    --namespace argocd \
    svc/argocd-server 8000:443
Forwarding from 127.0.0.1:8000 -> 8080
Forwarding from [::1]:8000 -> 8080