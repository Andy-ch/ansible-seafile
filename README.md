# Seafile server

An Ansible playbook that installs a Seafile fileserver for Ubuntu.

## Usage

    ansible-playbook main.yml

## Role Variables

See [roles/seafile/defaults/main.yml](https://github.com/Andy-ch/ansible-seafile/blob/master/roles/seafile/defaults/main.yml)

## Init database

When is `seafile_create_database` set to True, database is initialized after it's created.
To initialize manualy use extra vars:
 
   ansible-playbook main.yml --extra-vars '{"seafile_init_database": true}'

## Misc

Sometimes you need to restart memcached, when assets not loading properly.

   service memcached restart

## Dependencies

None

# License

BSD

# Author Information

Originally created by [netzwirt](https://github.com/netzwirt).
