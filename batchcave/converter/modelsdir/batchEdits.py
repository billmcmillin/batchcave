class batchEdits:

    def ER_EAI_2nd(self, x, name='ER-EAI-2ND'):
        print('\nRunning change script '+ name + '\n')
        #print filename
        x = 'a'
        #x = utilities.MarcEditBreakFile(filename)
        # Change =001 field to =002, and add 003
        #x = re.sub('(?m)^=001  (.*)', '=002  \\1\n=003  ER-EAI-2nd', x)
        # ADD local 730, 949 before supplied 008
        #x = re.sub('(?m)^=008', r'=949  \\\\$a*b3=z;bn=buint;\n=949
#\\1$luint$rs$t99\n=730  0\$aEarly American imprints (Online).$nSecond
#series,$pShaw-Shoemaker.$5OCU\n=506  \\$aAccess restricted to users at
#subscribing institutions\n=008', x)
#        x = utilities.DeleteLocGov(x)
#        x = utilities.Standardize856_956(x)
#        x = utilities.CharRefTrans(x)
#        x = utilities.MarcEditSaveToMRK(x)
#        x = utilities.MarcEditMakeFile(x)
        return x
