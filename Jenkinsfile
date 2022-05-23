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
                stage("try and catch"){
                    try{
                        sh "exit 1"
                    } catch (err) {
                       catchError(message: "Some test failed", buildResult: 'UNSTABLE', stageResult: 'UNSTABLE')
                    }
                }
            }
        }
    }
}