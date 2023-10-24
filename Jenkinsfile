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
    post('email-notify'){
        always{
            // 提交邮件通知
            emailext body: '${FILE,path="data/email_template.html"}',
            subject: "jobName:${env.JOB_BASE_NAME},result:${currentBuild.currentResult},name:${self_jobname}",
            to: '1074256248@qq.com'
            // 展示allure报告
            allure includeProperties: false,
            jdk: 'JAVA17_HOME',
            report: 'report/allure-report',
            results: [[path: 'report/xml']]
        }
    }

}