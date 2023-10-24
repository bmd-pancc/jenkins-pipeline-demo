pipeline{
    agent any
    environment{
        self_jobname = '流水线项目'
    }
    stages{
        stage("api_auto_test"){
            steps{
                bat 'python run_all.py'
            }
        }
    }
    post{
        always{
            // One or more steps need to be included within each condition's block.
            emailext body: '${FILE,path="data/email_template.html"}',
            subject: "jobName:${env.JOB_BASE_NAME},result:${currentBuild.currentResult},name:${self_jobname}",
            to: '1074256248@qq.com'
        }
    }

}