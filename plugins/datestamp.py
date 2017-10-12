"""
Adds a template parameter, __date__, which is replaced with the time and date
that the output was generated.
"""
import datetime

import rawdoglib.plugins
from rawdoglib.rawdog import string_to_html

def date_output_bits(rawdog, config, bits):
	now = datetime.datetime.now()
	bits['generated'] = string_to_html(now.strftime("%Y-%m-%d %H:%M"), config)

rawdoglib.plugins.attach_hook('output_bits', date_output_bits)
