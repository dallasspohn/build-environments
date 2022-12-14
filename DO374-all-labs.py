import os
import yaml

chapters = ["ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8", "ch9"]

ch1 = ["develop-navigator", "develop-git", "develop-practices", "develop-review"]
ch2 = [
    "manage-reusing",
    "manage-finding",
    "manage-selecting",
    "lab start manage-review",
]
ch3 = ["controller-playbooks", "controller-review"]
ch4 = ["config-ansible", "config-navigator", "config-review"]
ch5 = ["inventory-dynamic", "inventory-yaml", "inventory-variables", "inventory-review"]
ch6 = ["task-escalation", "task-execution", "task-tagging", "task-speed", "task-review"]
ch7 = ["data-filters", "data-lookups", "data-loops", "data-netfilters", "data-review"]
ch8 = ["update-delegation", "update-parallelism", "update-management", "update-review"]
ch9 = [
    "create-writing",
    "",
    "builder-custom",
    "builder-validate",
    "builder-use",
    "builder-review",
]
ch10 = ["review-cr1", "review-cr2", "review-cr3"]


AAP22 = [
    "develop-navigator",
    "develop-git",
    "develop-practices",
    "develop-review",
    "manage-reusing",
    "manage-finding",
    "manage-selecting",
    "controller-playbooks",
    "controller-review",
    "config-ansible",
    "config-navigator",
    "inventory-dynamic",
    "inventory-yaml",
    "inventory-variables",
    "inventory-review",
    "task-escalation",
    "task-execution",
    "task-tagging",
    "task-speed",
    "data-filters",
    "data-lookups",
    "data-loops",
    "data-netfilters",
    "data-review",
    "update-delegation",
    "update-parallelism",
    "update-management",
    "create-writing",
    "builder-custom",
    "builder-validate",
    "builder-use",
]  # builder-review

lab_name = "This lab is "


def ch1():
    for c1 in ch1:
        print(lab_name, c1)
        os.system("lab start " + c1)
        os.system("lab finish " + c1)


def ch2():
    for c2 in ch2:
        print(lab_name, c2)
        os.system("lab start " + c2)
        os.system("lab finish " + c2)


def ch3():
    for c3 in ch3:
        print(lab_name, c3)
        os.system("lab start " + c3)
        os.system("lab finish " + c3)


def ch4():
    for c4 in ch4:
        print(lab_name, c4)
        os.system("lab start " + c4)
        os.system("lab finish " + c4)


def ch5():
    for c5 in ch5:
        print(lab_name, c5)
        os.system("lab start " + c5)
        os.system("lab finish " + c5)


def ch6():
    for c6 in ch6:
        print(lab_name, c6)
        os.system("lab start " + c6)
        os.system("lab finish " + c6)


def ch7():
    for c7 in ch7:
        print(lab_name, c7)
        os.system("lab start " + c7)
        os.system("lab finish " + c7)


def ch8():
    for c8 in ch8:
        print(lab_name, c8)
        os.system("lab start " + c8)
        os.system("lab finish " + c8)


def ch9():
    for c9 in ch9:
        print(lab_name, c9)
        os.system("lab start " + c9)
        os.system("lab finish " + c9)


def ch10():
    for c10 in ch10:
        print(lab_name, c10)
        os.system("lab start " + c10)
        os.system("lab finish " + c10)


def ch11():
    for c11 in ch11:
        print(lab_name, c11)
        os.system("lab start " + c11)
        os.system("lab finish " + c11)


def ch12():
    for c12 in ch12:
        print(lab_name, c12)
        os.system("lab start " + c12)
        os.system("lab finish " + c12)


# with open("lab-scripts.yml", 'r') as stream:
#    out = yaml.load(stream)
#    print(out["scripts"]["chapter"])

def aap_all():
    for lab in AAP22:
        print(lab_name, lab)
        os.system("lab start " + lab)
        os.system("lab finish " + lab) 

aap_all()

#ch1()
