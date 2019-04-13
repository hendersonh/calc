
pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'echo "$(mycalc sub 100 50)"' 
                sh 'pytest -v'
            }
        }
    }
}
