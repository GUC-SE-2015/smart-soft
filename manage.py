#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "syntax_solutions.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _

if "notification" in settings.INSTALLED_APPS:
    from pinax.notifications.models import NoticeType

    def create_notice_types(app, created_models, verbosity, **kwargs):
        NoticeType.create("create_follow_request", _("Follow Reqquest"), _("you have received a follow request"))
        NoticeType.create("accept", _("Acceptance Received"), _("follow request is accepted"))

    signals.post_syncdb.connect(create_notice_types, sender=NoticeType)
else:
    print "Skipping creation of NoticeTypes as notification app not found"