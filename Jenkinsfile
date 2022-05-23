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
            stages{
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
                        sh """
                        test=$(pipenv run pytest --headless)
                        if [$test == 1]
                        then
                            echo "0"
                        """
                    }
                }
            }
        }
    }
}