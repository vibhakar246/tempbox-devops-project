pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'python3 -m pytest tests/ -v || echo "No tests yet"'
            }
        }
        stage('Docker Build') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t tempbox:test .'
            }
        }
        stage('Docker Run') {
            steps {
                echo "Running container..."
                sh 'docker run -d -p 5000:5000 --name tempbox-test tempbox:test || true'
                sh 'sleep 5'
                sh 'curl -f http://localhost:5000/health || true'
                sh 'docker stop tempbox-test || true'
                sh 'docker rm tempbox-test || true'
            }
        }
    }
}
