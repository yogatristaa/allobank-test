provider "kubernetes" {
  config_path = "~/.kube/config"
  
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

resource "helm_release" "postgresql" {
  name       = "postgresql"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql"
  version    = "15.5.14" 
  namespace  = "postgresql"
  create_namespace = true
  values = [
    <<EOF
postgresqlPassword: "password"
postgresqlDatabase: "airflow"
EOF
  ]
}

resource "helm_release" "airflow" {
  name       = "airflow"
  repository = "https://airflow.apache.org"
  chart      = "airflow"
  namespace  = "airflow"
  create_namespace = true
  timeout    = 600

  values = [
    file("values.yaml")
  ]
}
