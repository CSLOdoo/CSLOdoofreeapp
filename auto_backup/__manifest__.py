# -- encoding: utf-8 --
##############################################################################
#
#    Cloud Science Labs
#    Copyright (C) 2024 (https://www.cloudsciencelabs.com/)
#
##############################################################################

{
    "name": "CSL Database Backup",
    "summary": "Backups database",
    "version": "17.0.0.0.0",
    "author": "Cloud Science Labs",
    "license": "AGPL-3",
    "website": "https://www.cloudsciencelabs.com/",
    "category": "Tools",
    "depends": ["mail"],
    "data": [
        "data/ir_cron.xml",
        "data/mail_message_subtype.xml",
        "security/ir.model.access.csv",
        "view/db_backup_view.xml",
    ],
    "installable": True,
    "external_dependencies": {"python": ["pysftp"]},
}
