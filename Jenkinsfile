
pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'mycalc add 100 50' 
                sh 'pytest -v'
            }
        }
    }
}
