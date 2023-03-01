[![BACKUP EAGLE Logo](https://images.schmitz-rz-consult.de/github/logo_backupeagle.png)](https://www.schmitz-rz-consult.de/de/)

# BACKUP EAGLE® REST API python examples
BACKUP EAGLE® REST API examples for python.

## About BACKUP EAGLE®
BACKUP EAGLE® is a reporting and monitoring solution that monitors and documents your entire backup environment without any additional manual effort.

BACKUP EAGLE® supports various backup systems such as IBM Spectrum Protect, IBM Spectrum Protect Plus, Veeam, DELL EMC NetWorker, IBM BRMS, Microsoft Azure Backup, SEP sesam, Rubrik, dsmISI MAGS, dsmISI Storage, dsmISI Veeam, Oracle RMAN, UC4 / CA Automatic Workload, BMC Control-M, DELL EMC Data Domain, IBM Tape Library, DELL EMC Isilon, DELL EMC PowerProtect Data Manager, Commvault, Cohesity, VMware vCenter and others.

The dashboard provides you with all the essential information on the status of your backup environment in a clear and concise manner. You can see at a glance whether there is still enough storage capacity, whether the backups have run reliably or whether there have been problems during a backup.

For more information visit <a href="https://www.schmitz-rz-consult.de/" target="_blank">www.schmitz-rz-consult.de</a>.

## Content

Here are the assignments of the individual topics to the sample folders:

| Topic                              | Folder                             |
| ---------------------------------- | ---------------------------------- |
| Backup & restore results           | backup_and_restore_results         |
| Connection test to the REST API    | connection_test                    |
| Import of backup results           | import_backup_results              |
| Mail management                    | mail_management                    |
| Nodes, Clients, VMs                | nodes_clients_vms                  |
| Projects & schedules               | projects_and_schedules             |
| Report management                  | report_management                  |
| RMAN catalog management            | rman_catalog_management            |
| Server and device group management | server_and_device_group_management |
| Server & devices                   | server_devices                     |
| User defined group management      | user_defined_group_management      |
| User management                    | user_management                    |
| XML, log & csv upload              | xml_log_csv_upload                 |

## Usage

### Windows

#### Requirements

Install the last version of Python from here: <a href="https://www.python.org/downloads/windows/" target="_blank">www.python.org/downloads/windows/</a>.

#### Example usage

Open a new command prompt and insert:

```console
py .\mail_management\queryMailRecipients.py --host="192.168.0.1" --user="admin" --password="admin" --pretty-print=True
```

### Linux

#### Requirements

Install the last version of Python via console:

```console
sudo apt-get update
sudo apt-get install python3.10
```

:warning: Please look for current version on <a href="https://www.python.org/downloads/" target="_blank">www.python.org/downloads/</a> and replace it in the command above

#### Example usage

Write in the terminal:

```console
python .\mail_management\queryMailRecipients.py --host="192.168.0.1" --user="admin" --password="admin" --pretty-print=True
```

---

## Copyright

Visit <a href="https://www.schmitz-rz-consult.de/" target="_blank">www.schmitz-rz-consult.de</a> for more information.

[![SRZC Logo](https://images.schmitz-rz-consult.de/github/logo_srzc.png)](https://www.schmitz-rz-consult.de/)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/schmitz-rz-consult-gmbh/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/backupeagle)
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/backupeagle/)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/user/BACKUPEAGLE)
