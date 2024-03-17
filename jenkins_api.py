import jenkins
import csv


def list_jobs(jenkins_url,jenkins_user,jenkins_pass):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    Jobs=server.get_jobs()
    list_of_jobs=[]
    for i in Jobs:
        list_of_jobs.append([i['name'], i['url'], i.get('color')])
    return list_of_jobs

def startJobs():
    pass
    

#list_jobs('http://54.172.51.138:8080','devops','devops')

def jenkins_csv_file(my_list):
    with open("jenkins_inventory.csv", 'w',newline='') as j:
        pen = csv.writer(j)
        header=['JOBS_NAME', 'JOB_URL', 'JOB_LAST_BUILD_STATUS']
        pen.writerow(header)
        for item in my_list:
            pen.writerow(item)
    j.close
            
#jenkins_csv_file(list_jobs('http://54.172.51.138:8080','devops','devops'))
jenkins_jobs =list_jobs('http://54.172.51.138:8080','devops','devops')
jenkins_csv_file(jenkins_jobs)

