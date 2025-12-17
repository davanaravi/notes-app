pipeline {
    agent { label 'vm1-agent' }

    stages {
        stage('Deploy to RKE2 Kubernetes') {
            steps {
                sh '''
                  whoami
                  hostname
                  kubectl get nodes
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
