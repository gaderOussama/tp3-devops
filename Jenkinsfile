pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/gaderOussama/tp3-devops.git'
            }
        }

        stage('Run .NET tests') {
            steps {
                dir('dotnet-app.Tests') {
                    bat 'dotnet test'
                }
            }
        }

        stage('Run Python tests') {
            steps {
                dir('python-app') {
                    bat 'python -m unittest'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished !!!'
        }
    }
}
