pipeline {
    agent any

    environment {
        IMAGE_NAME = 'golu009/jenkins_ci'  // You can change the image name if needed
    }

    triggers {
        githubPush() // 🔥 THIS enables GitHub webhook triggers
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/manish-bagdwal1/Jenkins_CI.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_cred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh """
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $IMAGE_NAME:latest
                    """
                }
            }
        }
    }
}
