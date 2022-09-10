"""Setup script for CWLite/1200 with CW305 target
"""
#Setup target and CW
import chipwhisperer as cw
scope = cw.scope()
self.scope = scope
self.api.setParameter(['Generic Settings', 'Target Module', 'ChipWhisperer CW305 (Artix-7)'])

target = cw.target(scope)

try:
    scope = self.scope
    target = self.target
except NameError:
    pass

#self.api.setParameter(['ChipWhisperer CW305 (Artix-7)', 'FPGA Bitstream', 'Bitstream File', u'C:/Users/hecja/Desktop/cw305_top_untouched.bit'])
#self.api.setParameter(['ChipWhisperer CW305 (Artix-7)', 'FPGA Bitstream', 'Program FPGA', None])


