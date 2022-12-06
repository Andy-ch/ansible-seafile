#!/usr/bin/env python
#
# {{ ansible_managed }}

import check_init_admin
import os
import sys
import subprocess

def main():
    
    subprocess.call(["{{ seafile_installation_path }}/seafile.sh", "start"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if len(sys.argv) == 3:
        if check_init_admin.need_create_admin():
            check_init_admin.create_admin(sys.argv[1],sys.argv[2])
        else:
            print "changed=False"
        sys.exit(0)
    else:
        print
        print "Usage: init_admin.py <username> <password>"
        print 
        sys.exit(1)


if __name__ == '__main__':
    
    try:
        main()
    except KeyboardInterrupt:
        print '\n\n\n'
        print 'Aborted.'
        print
        sys.exit(1)
    except Exception, e:
        print
        print 'Error happened during creating seafile admin:'
        print e
        print
        sys.exit(1)
