#######################################################################################################
#
# Python Example - Delete role
# (C) Schmitz RZ Consult GmbH - BACKUP EAGLE
#
# Example usage:
# python deleteRole.py --host="192.168.0.1" --user="admin" --password="admin" --role-id="2"
#
# For more information see BACKUP EAGLE REST API documentation
#
#######################################################################################################

from optparse import OptionParser
import sys
import requests

parser = OptionParser()
parser.add_option("--host", dest="host", help="BACKUP EAGLE host, (example: 192.168.0.1)")
parser.add_option("--user", dest="username", help="BACKUP EAGLE username")
parser.add_option("--password", dest="password", help="BACKUP EAGLE password")
parser.add_option("--role-id", dest="roleId", help="Id of the role.")
parser.add_option("--verify-ssl", dest="verifySSL", default=False, help="Yerify SSL certificate of connection (default: false)")

(options, args) = parser.parse_args()

def validate_input():
    if(options.username is None or options.password is None or options.host is None or options.roleId is None):
        print("Invalid input, use -h or --help for help")
        sys.exit(2)

def main():
    session = requests.Session()
    session.auth = (options.username, options.password)

    url = "https://" + options.host + ":10987/api/rest/security/role/" + options.roleId
    r = session.delete(url, verify=options.verifySSL)
    print(r.text)

validate_input()
main()