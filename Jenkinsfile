pipeline{
    agent{
        label 'jenkins-node-intern'
    }
    stages{
        stage("setup docker agent"){
            agent {
                docker {
                    label 'jenkins-node-intern'
                    image 'nexus.tkhtechnology.com/amd64/chrome_python:latest'
                    registryUrl 'https://nexus.tkhtechnology.com'
                    registryCredentialsId 'jenkins_office365_account'
                    args '-u root:root'
                    reuseNode true
                }
            }
            environment{
                scannerHome = tool 'SonarQube'
                SONARQUBE_TOKEN =
            }
            stages{
                stage("Sonarqube analysis"){
                    steps{
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=${SONARQUBE_TOKEN}"
                }

                    }
                }
                stage("install dependencies"){
                    steps{
                        sh """
                        pip install pipenv
                        pipenv install
                        """
                    }
                }
                stage("run test"){
                    steps{
                        script{
                            warnError(message:"Some tests failed"){
                                sh "pipenv run pytest --headless"
                            }
                        }
                    }
                }
            }
        }
    }
}