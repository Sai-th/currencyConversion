# Jenkinsfile
pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }
    triggers {
        cron('@daily')
        pollSCM('H * * * *') // Check for git changes every hour
    }
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/YOUR_USERNAME/currency_converter.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Package') {
            steps {
                sh 'echo "Packaging application..."'
            }
        }
        stage('End'){
            steps{
                sh 'echo "###########---------Build completed succesfully!!---------###########'
            }
        }
    }
}
