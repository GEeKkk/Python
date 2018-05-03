# -*- coding: utf-8 -*-

class Srand:
    srandnum = None
    addrstream = None
    slidervalue = 0
    fifo = []
    lru = []
    opt = []
    lfu = []
    
def SetSrandValue(SrandN):
    Srand.srandnum = SrandN
    
def SetAddrValue(AddrS):
    Srand.addrstream = AddrS
    
def GetSrandValue():
    return Srand.srandnum
    
def GetAddrValue():
    return Srand.addrstream

def SetSliderValue(Slider):
    Srand.slidervalue = Slider

def GetSliderValue():
    return Srand.slidervalue

def SetFifo(FIFO_temp):
    Srand.fifo.append(FIFO_temp)

def ClearFifo():
    Srand.fifo = []

def GetFifo():
    return Srand.fifo

def SetLru(LRU_temp):
    Srand.lru.append(LRU_temp)

def GetLru():
    return Srand.lru

def ClearLru():
    Srand.lru = []

def SetOpt(OPT_temp):
    Srand.opt.append(OPT_temp)

def GetOpt():
    return Srand.opt

def ClearOpt():
    Srand.opt = []

def SetLfu(LFU_temp):
    Srand.lfu.append(LFU_temp)

def GetLfu():
    return Srand.lfu

def ClearLfu():
    Srand.lfu = []