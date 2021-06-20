import os
import subprocess

form_list = [i for i in os.listdir() if i.endswith('.ui')]
form_list = ['.'.join(i.split('.')[:-1]) for i in form_list]

for form in form_list:
    subprocess.run([
        'pyuic5',
        '{}.ui'.format(form),
        '-o',
        '{}.py'.format(form)
        ])
    print('rebuilt {}'.format(form))
