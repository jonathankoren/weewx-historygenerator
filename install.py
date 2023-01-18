# weewx-aqi
# Copyright 2023 - Jonathan Koren <jonathan@jonathankoren.com>
# License: GPL 3

from setup import ExtensionInstaller

def loader():
    return HistoryGeneratorInstaller()

class HistoryGeneratorInstaller(ExtensionInstaller):
    def __init__(self):
        super(HistoryGeneratorInstaller, self).__init__(
            version="1.0",
            name='historygenerator',
            description='Display monthly data aggregations in a convenient color coded grid.',
            author="Jonathan Koren",
            author_email="jonathan@jonathankoren.com",
            files=[('bin/user',
                    [ 'historygenerator.py' ])
            ]
        )
