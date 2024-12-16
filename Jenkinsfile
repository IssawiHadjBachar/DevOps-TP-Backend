pipeline {
  agent any

  stages {
    stage('Clone Repository') {
      steps {
        git url: 'https://github.com/IssawiHadjBachar/DevOps-TP-Backend.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t issawi/backend:latest .'
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
          sh 'echo "$DOCKER_TOKEN" | docker login -u issawi --password-stdin'
          sh 'docker push issawi/backend:latest'
        }
      }
    }
  }
}