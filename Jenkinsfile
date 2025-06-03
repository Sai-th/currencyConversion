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
        }
        stage('Package') {
            steps {
                sh 'echo "Packaging application..."'
                sh 'tar -czf conversion_app.tar.gz *'
            }
        }
        stage('Run') {
            steps {
                sh 'python conversion_app.py & sleep 10' // start app in background and allow time to initialize
            }
        }
    }
}
