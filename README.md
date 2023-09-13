# AIRFLOW-TRIAL-1
HOW TO INSTALL APACHE-AIRFLOW

```bash
choco install kubernetes-helm: This command is likely used on a Windows system with Chocolatey package manager to install Helm, a package manager for Kubernetes.

helm list: This command lists Helm releases that are currently installed on your Kubernetes cluster.

git clone https://github.com/KamarulAdha/AIRFLOW-TRIAL-1.git: This command clones a Git repository named "AIRFLOW-TRIAL-1" from GitHub.

helm repo add apache-airflow https://airflow.apache.org: This command adds the Apache Airflow Helm repository to your Helm configuration, allowing you to install Apache Airflow using Helm charts.

helm list: This command lists Helm releases again, possibly to check if the Apache Airflow Helm repository has been successfully added.

kubectl getall: There is a typo in this command; it should be kubectl get all. This command lists all Kubernetes resources in the current namespace.

kubectl describe pod service/airflow-postgresql: This command attempts to describe a Kubernetes pod named "airflow-postgresql" in the "service" namespace. The syntax should be corrected to kubectl describe pod airflow-postgresql.

kubectl describe pod airflow-postgresql: This command describes the Kubernetes pod named "airflow-postgresql," providing detailed information about its configuration and status.

helm delete airflow: This command deletes a Helm release named "airflow" from the Kubernetes cluster.

kubectl get all -n kube-system: This command lists all Kubernetes resources in the "kube-system" namespace. This is typically used to view system-level resources.

kubectl logs deployment.apps/ebs-csi-controller: This command retrieves the logs of a Kubernetes deployment named "ebs-csi-controller."

kubectl logs deployment.apps/ebs-csi-controller -n kube-system: This command retrieves the logs of a Kubernetes deployment named "ebs-csi-controller" in the "kube-system" namespace.

helm upgrade airflow apache-airflow/airflow -f values.yaml --install: This command upgrades or installs the "airflow" Helm release from the "apache-airflow" Helm repository using the configuration specified in the "values.yaml" file.

kubectl get all: This command lists all Kubernetes resources in the current namespace after the Helm upgrade or installation.

kubectl port-forward service/airflow-webserver 8081:8080: This command sets up port forwarding, allowing you to access the Kubernetes service named "airflow-webserver" on port 8081 on your local machine, which will be forwarded to port 8080 on the Kubernetes cluster. This is commonly used to access web interfaces or services running in Kubernetes locally.
```

