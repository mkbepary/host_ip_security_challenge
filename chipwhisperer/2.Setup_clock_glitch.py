#bitstream = r"C:/Users/hecja/Desktop/cw305_top_untouched.bit"
#target = cw.target(scope, cw.targets.CW305, bsfile=bitstream, force=False)

#Change file location based on desired bitstream
self.api.setParameter(['ChipWhisperer CW305 (Artix-7)', 'FPGA Bitstream', 'Bitstream File', u'D:/FIAT/HOST/Int1/aes128_verilog/aes128_verilog.runs/impl_35t/cw305_top.bit'])
#self.api.setParameter(['ChipWhisperer CW305 (Artix-7)', 'FPGA Bitstream', 'Bitstream File', u'D:/FIAT/DFA/aes128_verilog/aes128_verilog.runs/impl_35t/cw305_top.bit'])
#self.api.setParameter(['ChipWhisperer CW305 (Artix-7)', 'FPGA Bitstream', 'Bitstream File', u'D:/FIAT/DFA/AES/aes128_verilog/aes128_verilog.runs/impl_35t/cw305_top.bit'])
self.api.setParameter(['ChipWhisperer CW305 (Artix-7)', 'FPGA Bitstream', 'Program FPGA', None])

#Setup Plaintext
self.api.setParameter(['Generic Settings', 'Basic', 'Plaintext', 'Fixed'])
#self.api.setParameter(['Generic Settings', 'Basic', 'Fixed Plaintext', '32 43 F6 A8 88 5A 30 8D 31 31 98 A2 E0 37 07 34'])
#self.api.setParameter(['Generic Settings', 'Basic', 'Fixed Plaintext', '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01'])
self.api.setParameter(['Generic Settings', 'Basic', 'Fixed Plaintext', '54 77 6F 20 4F 6E 65 20 4E 69 6E 65 20 54 77 6F'])
self.api.setParameter(['Results', 'Trace Output Plot', 'X Axis', 'Time'])
#self.api.setParameter(['Generic Settings', 'Basic', 'Fixed Encryption Key', u'2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'])
#self.api.setParameter(['Generic Settings', 'Basic', 'Fixed Encryption Key', u'00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'])
self.api.setParameter(['Generic Settings', 'Basic', 'Fixed Encryption Key', u'54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75'])

#Number of Traces
self.api.setParameter(['Generic Settings', 'Acquisition Settings', 'Number of Traces', 200])

#Turn on Glitch Transistors
self.api.setParameter(['CW Extra Settings', 'HS-Glitch Out Enable (High Power)', True])
self.api.setParameter(['CW Extra Settings', 'HS-Glitch Out Enable (Low Power)', True])

#Scope Setup    
scope.gain.gain = 40
scope.gain.mode = "high"
scope.adc.samples = 350
scope.adc.offset = 0
scope.adc.basic_mode = "rising_edge"
scope.clock.adc_src = "clkgen_x4"
scope.clock.freq_ctr_src = "clkgen"
scope.clock.adc_phase = 175
scope.trigger.triggers = "tio4"

#CLKGEN Settings
scope.clock.extclk_freq = 10000000
scope.clock.clkgen_mul = 5
scope.clock.clkgen_div = 48
scope.clock.clkgen_freq = 10000000

#Glitch Setup 
scope.io.hs2 = "glitch"
scope.glitch.clk_src = 'clkgen'
scope.glitch.ext_offset = 244
scope.glitch.width = 5.078125
scope.glitch.offset = -1.953125
scope.glitch.trigger_src = "continuous" #change this depending on glitching desired
self.api.setParameter(['Glitch Module', 'Output Mode', 'Clock XORd'])


#Correct AES Outputs that can be used to test against in glitch window
#s == "06f36a65e8a99ff8907b2e5e5ddd77de"
#s != "06f36a65e8a99ff8907b2e5e5ddd77de"

#s == '09668b78a2d19a65f0fce6c47b3b3089'
#s != '09668b78a2d19a65f0fce6c47b3b3089'

