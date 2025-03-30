pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sirvaiys/diabetes-jenkins'  // You can change the image name if needed
    }

    triggers {
        githubPush() // 🔥 THIS enables GitHub webhook triggers
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh """
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $IMAGE_NAME:latest
                    """
                }
            }
        }
    }
}
