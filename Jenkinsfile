pipeline {
    agent { label 'vm1-agent' }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Deploy to RKE2 Kubernetes') {
            steps {
                sh '''
                  pwd
                  ls
                  ls k8s
                  kubectl apply -f k8s/deployment.yaml
                  kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo 'Notes Microservice deployed successfully via CloudBees CI'
        }
    }
}
