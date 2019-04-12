
pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'pytest /app/test_calc.py'
            }
        }
    }
}
