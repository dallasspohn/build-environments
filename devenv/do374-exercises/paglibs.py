import pyautogui as pag
import time
from Color import *

sku = "do467"


def serverexit():
    """Exit from root user"""
    pag.typewrite("exit")
    et()
    pag.typewrite("exit")
    et()


def et():
    """Press Enter"""
    pag.press("enter")


def setnoai():
    """Stops the stepping in VIM when pasting."""
    pag.press("esc")
    pag.typewrite(":")
    pag.typewrite(':set indentexpr=""')
    et()


def vc():
    """Write to and close VIM."""
    pag.press("esc")
    pag.press(":")
    pag.typewrite("wq")
    et()


def pwst():
    """Student as password"""
    pag.typewrite(["s", "t", "u", "d", "e", "n", "t"])
    et()


def pwrh():
    """redhat as password"""
    pag.typewrite(["r", "e", "d", "h", "a", "t"])
    et()


def labrefresh():
    """Lab Refresh"""
    pag.typewrite("lab --refresh")
    et()
    pag.typewrite(["s", "t", "u", "d", "e", "n", "t"])
    et()


def workstation():
    """SSH to workstation from home"""
    pag.typewrite("ssh aap101_workstation")
    et()


def exit1():
    pag.typewrite("logout")
    et()
    time.sleep(5)


def installrpm():
    pag.typewrite(
        "sudo yum remove -y $(rpm -qa | grep res294); sudo yum install $(ls | grep foundation | tail -1)"
    )
    et()
    time.sleep(4)
    pag.typewrite("y")
    et()


# def rootServera():
#     pag.typewrite('ssh admin@servera')
#     et()
#     pag.typewrite('sudo -i')
#     et()
#
# def rootServerc():
#     pag.typewrite('ssh admin@serverc')
#     et()
#     pag.typewrite('sudo -i')
#     et()
# def student():
#     pag.typewrite(['s', 't', 'u', 'd', 'e', 'n', 't'])
#     et()


def source():
    pag.typewrite("python3 -m venv venv")
    et()
    pag.typewrite("source venv/bin/activate")
    et()


def ansibleRunner():
    ### ANSIBLE RUNNER
    pag.typewrite("git clone https://github.com/ansible/ansible-runner.git")
    et()
    pag.typewrite("cd ansible-runner")
    et()
    pag.typewrite("git checkout release_2.0")
    et()
    pag.typewrite("pip install .")
    et()
    time.sleep(10)
    # pag.typewrite('unhash ansible-runner')
    # et()
    pag.typewrite("cd ~")
    et()


def ansibleBuilder():
    ### ANSIBLE BUILDER
    pag.typewrite("git clone https://github.com/ansible/ansible-builder.git")
    et()
    pag.typewrite("cd ansible-builder")
    et()
    pag.typewrite("git checkout devel")
    et()
    pag.typewrite("pip install .")
    et()
    time.sleep(10)
    # pag.typewrite('unhash ansible-builder')
    # et()
    pag.typewrite("cd ~")
    et()


def ansibleNavigator():
    ### ANSIBLE NAVIGATOR
    pag.typewrite("git clone https://github.com/ansible/ansible-navigator.git")
    et()
    pag.typewrite("cd ansible-navigator")
    et()
    pag.typewrite("pip install .")
    et()
    time.sleep(10)
    # pag.typewrite('unhash ansible-navigator')
    # et()
    pag.typewrite("cd ~")
    et()


def installRPM():
    pag.typewrite("cd /home/dallas/dev/RES294/classroom")
    et()
    pag.typewrite("make clean; make")
    et()
    time.sleep(4)
    pag.typewrite("rsync *.rpm res294_classroom:")
    et()
    time.sleep(20)
    pag.typewrite("ssh res294_classroom")
    et()
    installrpm()
    exit1()


def source():
    pag.typewrite("source ~/.venv/bin/activate")


def et():
    """Press Enter"""
    pag.press("enter")


def source_ansible():
    """Set environment to run ansible 2.11"""
    # os.system('python -m venv ~/.ansible-2.11')
    # os.system('source ~/.ansible-2.11/bin/activate')
    pag.typewrite("source ~/.ansible-2.11/bin/activate")
    et()


def clean_and_add():
    """Clean the Known Hosts file."""
    # os.system('ssh-add /home/dspohn/.ssh/instructor_key')
    # os.system('python3 /home/dspohn/bin/clean_known_hosts.py')
    pag.typewrite("python3 /home/dallas/bin/clean_known_hosts.py")
    et()
    # pag.typewrite('ssh-add /home/dspohn/.ssh/instructor_key')
    # et()


# def query_ip_sku():
#     global sku, ip
#     # sku = 'res294'#input("What is the classroom SKU? ")
#     #sku = pag.prompt("What is the sku of the course? ").upper()
#     # sku = input("What is the sku of the classroom.")
#     ip = pag.prompt("What is the last octaive of the IP? ")
#     pag.alert("Will move back to terminal window")

# time.sleep(2)

# def query_ip_sku():
#     global sku, ip
#     ip = input("What is the last octaive of the IP? ")
#     pag.alert("Will move back to terminal window")
#     time.sleep(2)


def change_to_drive():
    """Change to RES294 /classroom/ansible-playbooks-novello drive"""
    # os.chdir('/home/dspohn/development/RES294/classroom/research/playbooks')
    # os.chdir('/home/dspohn/development/RES294/classroom/ansible-playbooks-novello/')
    pag.typewrite("cd /home/dallas/dev/RES294/classroom/ansible-playbooks-novello/")
    et()


def update_galaxy():
    """Update ansible-galaxy requirements"""
    # os.system('ansible-galaxy install -r requirements.yml --force ')
    pag.typewrite("ansible-galaxy install -r requirements.yml --force ")
    et()


def run_playbook(sku, ip):
    # print(os.listdir())
    # os.system('ansible-playbook add_lab_env_ssh_config.yml -e classroom_external_ip=150.239.52.'+ip+' -e classroom_ssh_key_path=~/.ssh/instructor_key')
    #    os.system('ansible-playbook dle.heat_templates.update_local_ssh_config.yml -e course_sku='+sku+' -e classroom_external_ip=150.239.52.'+ip+' -e classroom_ssh_key_path=~/.ssh/instructor_key')
    pag.typewrite(
        "ansible-playbook dle.heat_templates.update_local_ssh_config.yml -e course_sku="
        + sku
        + " -e classroom_external_ip=150.239.52."
        + ip
        + " -e classroom_ssh_key_path=~/.ssh/instructor_key"
    )
    et()


def bob():
    print("Bob")


### Run with different SKU
# os.system('ansible-playbook add_lab_env_ssh_config.yml -e classroom_external_ip=150.239.52.'+ip+' -e sku='+sku+' -e classroom_ssh_key_path=~/.ssh/instructor_key')


### THEN RUN to provision classroom env.
# ansible-playbook 140_register-sat.yml -i ../research/playbooks/inventory.laptop


def flow_into_rpm_build():
    pag.typewrite(
        "cd /home/dallas/.config/JetBrains/PyCharmCE2021.1/scratches/AAP-Research"
    )
    et()
    pag.typewrite("python3 rpm-RES294.py")
    et()


def source_ansible():
    """Set environment to run ansible 2.11"""
    pag.typewrite("source ~/.ansible-2.11/bin/activate")
    et()


def source_dynolabs():
    pag.typewrite("source ~/.venv/labs/bin/activate")
    et()


def et():
    """Press Enter"""
    pag.press("enter")


def password_local():
    """My local password"""
    pag.typewrite(["!", "d", "!", "g", "P", "y", "t", "h", "0", "n"])
    et()


def password_student():
    """My local password"""
    pag.typewrite(["s", "t", "u", "d", "e", "n", "t"])
    et()


def clean_and_add():
    """Clean the Known Hosts file."""
    pag.typewrite("python3 /home/dallas/bin/clean_known_hosts.py")
    et()


def change_to_drive():

    """Change to RES294 /classroom/ansible-playbooks-novello drive"""
    pag.typewrite(
        "cd /home/dallas/dev/" + sku.upper() + "/classroom/ansible-playbooks-novello/"
    )
    et()


def update_galaxy():
    """Update ansible-galaxy requirements"""
    pag.typewrite("ansible-galaxy install -r requirements.yml --force ")
    et()


def run_playbook(sku, ip):
    pag.typewrite(
        "ansible-playbook dle.heat_templates.update_local_ssh_config.yml -e course_sku="
        + sku
        + " -e classroom_external_ip=150.239.52."
        + ip
        + " -e classroom_ssh_key_path=~/.ssh/instructor_key"
    )
    et()
    time.sleep(4)


def makeCurriculum():
    """Make Necessary directory and pull SKEW to it"""
    pag.typewrite("mkdir dev")
    et()
    pag.typewrite("cd dev")
    et()
    pag.typewrite("git clone git@github.com:RedHatTraining/DO374.git")
    et()
   # time.sleep(4)
    # pag.typewrite("git clone git@github.com:RedHatTraining/DO447.git")
    # et()
    time.sleep(4)
    pag.typewrite("git clone https://github.com/dallasspohn/build-environments.git")
    et()
    time.sleep(4)
#    pag.typewrite("git clone git@github.com:RedHatTraining/pcommit-config.git")
#    et()
#    time.sleep(4)
#    pag.typewrite("git clone git@github.com:RedHatTraining/flamel-container.git")
#    et()
#    time.sleep(4)


def convert_forwardx11():
    pag.typewrite(
        "find /home/dallas/.ssh/config.d/ -type f -exec sed -i 's/ForwardX11 no/ForwardX11 yes/g' {} \;"
    )
    et()


def sendAwayConfigs():
    pag.typewrite("scp /home/dallas/.ssh/config.d/50_* dallas@alpine:.ssh/config.d/")
    et()
    # pag.typewrite('scp /home/dallas/.ssh/config.d/50_* dspohn@dspohn:.ssh/config.d/')
    # et()


def install_pcommit():
    pag.typewrite("cd /home/student/dev/pcommit-config")
    et()
    pag.typewrite("./install_precommit.sh")
    et()
    time.sleep(5)


def run_build_dev_env():
    pag.typewrite("cd /home/student/dev/build-environments")
    et()
    pag.typewrite("time ansible-playbook deploydev.yml")
    et()
    time.sleep(1)
    password_student()
    #pag.typewrite("student")
    et()


def build_vale():
    pag.typewrite("cd ~/.config")
    et()
    pag.typewrite("git clone git@github.com:dallasspohn/vale.git")
    et()
    time.sleep(3)


def youCompleteMe_build():
    pag.typewrite("cd ~/.vim/bundle/YouCompleteMe")
    et()
    pag.typewrite("sudo dnf install cmake gcc-c++ make python3-devel")
    et()
    password_student()


def install_exa():
    pag.typewrite(
        "sudo unzip /home/student/dev/build-dev-environment/devenv/files/bashprompt/exa.zip -d /usr/local/"
    )
    et()
    password_student()
    #pag.typewrite("sudo cp /usr/local/bin/bin/exa /usr/local/bin/")
    #et()


def install_starship():
    pag.typewrite("curl -sS https://starship.rs/install.sh | sh")
    et()
    time.sleep(1)
    pag.typewrite("y")
    et()
    password_student()
    et()
    time.sleep(4)
    pag.typewrite('eval "$(starship init bash)"')
    et()

def finish_icon():
    print(
       Base.WARNING,Base.BOLD,Formatting.Blink, """     (     (        )  (    (        )      (
     )\ )  )\ )  ( /(  )\ ) )\ )  ( /(      )\ )
    (()/( (()/(  )\())(()/((()/(  )\()) (  (()/(
     /(_)) /(_))((_)\  /(_))/(_))((_)\  )\  /(_))
    (_))_|(_))   _((_)(_)) (_))   _((_)((_)(_))_
    | |_  |_ _| | \| ||_ _|/ __| | || || __||   \\
    | __|  | |  | .` | | | \__ \ | __ || _| | |) |
    |_|   |___| |_|\_||___||___/ |_||_||___||___/ """, Base.END
    )
