import os
import pyautogui as pag
from paglibs import *
#List = open("labs.txt").readlines()
#print(List)
pag.alert("Make sure you are on workstation then click ok")
time.sleep(4)
#labs = ['lab start install-installation', 'lab start install-configuration', 'lab start org-user', 'lab start org-team', 'lab start org-hub', 'lab start org-review', 'lab start host-inventory', 'lab start host-credential', 'lab start host-review', 'lab start provision-project', 'lab start provision-job', 'lab start provision-review', 'lab start job-facts', 'lab start job-survey', 'lab start job-notification', 'lab start job-review', 'lab start workflow-template', 'lab start workflow-approval', 'lab start workflow-review', 'lab start advinventory-static', 'lab start advinventory-dynamic', 'lab start advinventory-smart', 'lab start advinventory-review', 'lab start api-controller', 'lab start cicd-controller', 'lab start api-review', 'lab start admin-troubleshoot', 'lab start admin-recovery']
xlabs = ['lab start install-configuration', 'lab start org-user', 'lab start org-team', 'lab start org-hub', 'lab start org-review', 'lab start host-inventory', 'lab start host-credential', 'lab start host-review', 'lab start provision-project', 'lab start provision-job', 'lab start provision-review', 'lab start job-facts', 'lab start job-survey', 'lab start job-notification', 'lab start job-review', 'lab start workflow-template', 'lab start workflow-approval', 'lab start workflow-review', 'lab start advinventory-static', 'lab start advinventory-dynamic', 'lab start advinventory-smart', 'lab start advinventory-review', 'lab start api-controller', 'lab start cicd-controller', 'lab start api-review', 'lab start admin-troubleshoot', 'lab start admin-recovery']


for l in xlabs:
    pag.typewrite("time " + l)
    et()
    time.sleep(40)

