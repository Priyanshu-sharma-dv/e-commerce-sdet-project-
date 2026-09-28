pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build Test Image') { steps { sh 'docker build -f Dockerfile.test -t ecommerce-sdet-tests:ci .' } }
    stage('Lint') { steps { sh 'docker run --rm ecommerce-sdet-tests:ci ruff check .' } }
    stage('Type Check') { steps { sh 'docker run --rm ecommerce-sdet-tests:ci pyright' } }
    stage('Start Environment') { steps { sh 'docker compose -f docker-compose.ci.yml up -d db app' } }
    stage('Parallel Tests') { steps { sh 'docker compose -f docker-compose.ci.yml run --rm playwright pytest -n auto --junitxml=test-results.xml --cov=app --cov=api_clients --cov=database --cov-report=xml' } }
    stage('Security') { steps { sh 'docker run --network host -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t http://127.0.0.1:8000 -r zap-report.html || true' } }
  }
  post {
    always {
      sh 'docker compose -f docker-compose.ci.yml down -v || true'
      archiveArtifacts artifacts: 'test-results.xml,coverage.xml,zap-report.html,reports/**,allure-results/**', allowEmptyArchive: true
      junit testResults: 'test-results.xml', allowEmptyResults: true
    }
  }
}
