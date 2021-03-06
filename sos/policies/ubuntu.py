from __future__ import with_statement

import os

from sos.plugins import UbuntuPlugin, DebianPlugin, IndependentPlugin
from sos.policies.debian import DebianPolicy

class UbuntuPolicy(DebianPolicy):
    distro = "Ubuntu"
    vendor = "Ubuntu"
    vendor_url = "http://www.ubuntu.com/"

    def __init__(self):
        super(UbuntuPolicy, self).__init__()
        self.valid_subclasses = [DebianPlugin, UbuntuPlugin]

    @classmethod
    def check(self):
        """This method checks to see if we are running on Ubuntu.
           It returns True or False."""
        try:
            with open('/etc/lsb-release', 'r') as fp:
                return "Ubuntu" in fp.read()
        except:
            return False
