# ML Pipeline with Airflow, Kubernetes, and Docker

This project demonstrates an end-to-end **ML training pipeline** orchestrated using **Apache Airflow**, executed in **Kubernetes (Minikube)** using Dockerized training jobs. It serves as a lightweight, local MLOps environment that can scale to cloud services like AWS EKS and SageMaker.

---

## Features

- Dockerized Python-based ML training job  
- Apache Airflow DAG using `KubernetesPodOperator`  
- Runs in a local Minikube cluster  
- Logs captured inside Airflow UI  
- Easily extendable to preprocessing, deployment, and MLflow logging  
- Future migration path to AWS (EKS, S3, SageMaker)  

---

## Project Structure

```
ml-airflow-k8s-pipeline/
├── dags/
│   └── train_in_k8s.py             # Airflow DAG to run training in Kubernetes
├── docker/
│   └── train.py                    # Simple Python ML training script
├── Dockerfile                      # Docker image for training job
├── build_ml_training_image.sh     # Script to build image inside Minikube
├── README.md                       # This file
```

---

## Setup Instructions

### Prerequisites

- Python ≥ 3.8  
- Docker  
- Minikube  
- Apache Airflow (Docker Compose)  
- Kubectl  

---

### Start Minikube

```bash
minikube start
```

---

### Build Docker Image in Minikube

```bash
eval $(minikube docker-env)
./build_ml_training_image.sh
```

---

### Set Up Airflow

```bash
cd airflow  # or wherever your Airflow project is
docker compose up airflow-init
docker compose up
```

Make sure the DAG `train_model_in_minikube` appears in the Airflow UI at [http://localhost:8080](http://localhost:8080)

---

### Trigger the DAG

- Go to the Airflow UI  
- Enable and trigger `train_model_in_minikube`  
- Monitor pod logs within Airflow or via terminal:

```bash
kubectl get pods
kubectl logs <pod-name>
```

---

## Sample Output

```text
Starting training job...
Training epoch 1/5
Training epoch 2/5
...
Training complete!
```

---

## 🌐 Roadmap

- [ ] Add data preprocessing step  
- [ ] Integrate MLflow for experiment tracking  
- [ ] Push model artifacts to S3  
- [ ] Deploy model using Flask/FastAPI on EKS  

---

## Contributing

Feel free to fork the repo, improve workflows, or use it in your own projects.

---

## License

This project is open-source under the MIT License.

---

## Author

**Manish Kumar**  
AI Engineer | MLOps Enthusiast  
[LinkedIn](https://linkedin.com) • [GitHub](https://github.com)
