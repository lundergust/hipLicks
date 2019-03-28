
from chordTonesDict import chordTonesDict


def pickChordTones(minor, dom, maj):
    minor1 = chordTonesDict[minor]['1']
    minor3 = chordTonesDict[minor]['3']
    minor5 = chordTonesDict[minor]['5']
    minor7 = chordTonesDict[minor]['7']
    dom1 = chordTonesDict[dom]['1']
    dom3 = chordTonesDict[dom]['3']
    dom5 = chordTonesDict[dom]['5']
    dom7 = chordTonesDict[dom]['7']
    maj1 = chordTonesDict[maj]['1']
    maj3 = chordTonesDict[maj]['3']
    maj5 = chordTonesDict[maj]['5']
    maj7 = chordTonesDict[maj]['7']
    print (minor1, minor3, minor5, minor7, dom1, dom3,
           dom5, dom7, maj1, maj3, maj5, maj7)
