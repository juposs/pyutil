ldap = {
    "match_attribute": "userPrincipalName",
    "dn": "OU=OrgUnit,DC=example,DC=org",
    "server": "example.org",
    "port": 636
}

mail = {
    "server": "mailserver.example.org",
    "port": 25,
    "sendfile": "False",
    "filepath": "None",
    "sender": "no-reply@example.org",
    "password": "None",
}

logger = {
    "logfile_path": "./myutil.log",
    "maxBytes": 0,
    "backupCount": 10,
}
