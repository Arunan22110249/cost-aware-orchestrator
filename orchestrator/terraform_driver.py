import json, subprocess

def write_tfvars(path, variables):
    with open(path, 'w') as f:
        json.dump(variables, f, indent=2)

def terraform_plan(tfdir):
    subprocess.run(['terraform','init','-input=false'], cwd=tfdir, check=True)
    subprocess.run(['terraform','plan','-out','plan.tfout','-input=false'], cwd=tfdir, check=True)
    return 'plan.tfout'

def terraform_apply(tfdir):
    subprocess.run(['terraform','apply','-auto-approve','plan.tfout'], cwd=tfdir, check=True)
