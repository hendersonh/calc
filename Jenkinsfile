
pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'pytest test_calc.py'
            }
        }
    }
}
