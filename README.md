# React-Node-Django DevOps Project

## General Info 
The application is a simple to-do application. This app is used for my Devops learning process.

React and Nginx are used on the frontend.

Django Rest Framework-Gunicorn and Node are used on the backend. Since I do not have much knowledge on the node side, I cannot give a detailed explanation.

Postgresql is preferred as database.

## Usage

I'm trying to combine what I've learned for the CI-CD process. I will advance this project using different devops tools. Minicube and docker-compose are used under this single repo. Its purpose is to run the project locally. Each service is kept under different repo for a complete CI-CD process. Links to other repos will be shared.

### Running application with docker-compose

Make sure these ports are empty as they are used on the Nginx and Postgresql default ports (80 and 5432).

```
git clone https://github.com/ovaliburak/todo-app-devops-project.git
cd todo-app-devops-project/
docker-compose up -d --build
```

We can now access the application from local. It is running on Node 5000 port, Django running on 8000 port. React is served by Nginx with port 80.

### Running application in k8s

Namespace

```
kubectl apply -f k8s/cluster/namespaces .
```

Optional user and authentication. Run in order

```
cd k8s/cluster
./users/key_csr.sh
```

Let's paste the two commands in CertificateSigningRequest.txt into the terminal respectively

```
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: junior
spec:
  groups:
  - system:authenticated
  request: $(cat junior.csr | base64 | tr -d "\n")
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF

---

cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: senior
spec:
  groups:
  - system:authenticated
  request: $(cat senior.csr | base64 | tr -d "\n")
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF
```

Authorize users.

```
kubectl apply -f authentication/. 
```


Enable Nginx ingress for Minikube

```
minikube addons enable ingress
```
--- 

Creating taint and label for nodes
If you include this part, you will need to uncomment the comment lines in the deployment.yaml files.

```
./nodes/node_taint_label.sh
```

--- 

To deploy the production side. The test side is similar.
Postgresql

```
cd k8s/db/prod
kubectl apply -f .
```
Node js 
```
cd k8s/server/server-node/prod
kubectl apply -f .
```
Django
```
cd k8s/server/server-django/prod
kubectl apply -f .
```
Nginx Ingress - React

```
cd k8s/client_nginx/prod
kubectl apply -f .
```
You can change the host information in client-web-ingress.yaml. For linux you will need to map this information to the ingress ip in /etc/hosts.



