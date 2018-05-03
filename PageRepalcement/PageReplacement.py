# -*- coding: utf-8 -*-

import copy
import BornSrand

class PageReplacement:
    def __init__(self,AddrStream):
        #self.PeakNum = copy.deepcopy(MemNum)
        self.block = ['*'] * BornSrand.GetSliderValue()
        self.addrstream = AddrStream

    def FIFO(self):
        Fstep = 0
        FIFOBlock = copy.deepcopy(self.block)
        BornSrand.ClearFifo()
        for item in self.addrstream:
            if item not in FIFOBlock[:]:
                k = FIFOBlock.pop(0)
                FIFOBlock.append(item)
                Fstep += 1
                BornSrand.SetFifo(FIFOBlock+['Missed',Fstep,item,k])
            else:
                BornSrand.SetFifo(FIFOBlock+['Hit','-','-','-'])
        return 1 - Fstep/len(self.addrstream)

    
    def LRU(self):
        Lstep = 0
        LRUBlock = copy.deepcopy(self.block)
        BornSrand.ClearLru()
        for item in self.addrstream:
            if item not in LRUBlock[:]:
                    kk = LRUBlock.pop(0)
                    LRUBlock.append(item)
                    Lstep += 1
                    BornSrand.SetLru(LRUBlock+['Missed',Lstep,item,kk])
            else:
                LRUBlock.remove(item)
                LRUBlock.append(item)
                BornSrand.SetLru(LRUBlock+['Hit','-','-','-'])
        return 1 - Lstep/len(self.addrstream)


    def OPT(self):
        tmp = []
        Ostep = 0
        OPTBlock = copy.deepcopy(self.block)
        OPageNum = copy.deepcopy(self.addrstream)
        BornSrand.ClearOpt()
        for item in OPageNum[:]:
            if item not in OPTBlock:
                if '*' in OPTBlock:
                    kkk = OPTBlock.pop(0)
                    OPTBlock.append(item)
                    OPageNum.pop(0)
                    Ostep += 1
                    BornSrand.SetOpt(OPTBlock+['Missed',Ostep,item,kkk])
                else:
                    for xitem in OPTBlock:
                        if xitem not in OPageNum:
                            Index = OPTBlock.index(xitem)
                            OPTBlock[Index] = item
                            OPageNum.pop(0)
                            Ostep += 1
                            BornSrand.SetOpt(OPTBlock+['Missed',Ostep,item,xitem])
                            tmp = []
                            break
                        else:
                            tmp.append(OPageNum.index(xitem))
                    if tmp != []:
                        Index = OPTBlock.index(OPageNum[max(tmp)])
                        Ostep += 1
                        BornSrand.SetOpt(OPTBlock+['Missed',Ostep,item,OPTBlock[Index]])
                        OPTBlock[Index] = item
                        OPageNum.pop(0)
                        tmp = []
                        
            else:
                OPageNum.pop(0)
                BornSrand.SetOpt(OPTBlock+['Hit','-','-','-'])
        return 1 - Ostep/len(self.addrstream)

    def LFU(self):
        global LFUBlock,temp,k4
        LFUBlock = []
        temp = []
        freq = []
        k4 = []
        LFPageNum = copy.deepcopy(self.addrstream)
        BornSrand.ClearLfu()
        length = BornSrand.GetSliderValue()
        count = 0
        for item in LFPageNum:
            if item not in LFUBlock[:]:
                count += 1
                if len(LFUBlock) != length:
                    freq.append([item,1,0])
                    LFUBlock.append(item)
                    BornSrand.SetLfu(['*']*(length-len(LFUBlock))+LFUBlock + ['Missed',count,item,'*'])
                else:
                    k4 = freq.pop(0)
                    freq.append([item,1,1])
                    freq.sort(key=lambda x:x[1])
                    LFUBlock = []
                    for hunter in freq:
                        LFUBlock.append(hunter[0])
                    BornSrand.SetLfu(LFUBlock + ['Missed',count,item,k4[0]])

                
                #BornSrand.SetLfu(LFUBlock + ['Missed',count,item,k4[0]])
                #k4 = []
                #print(LFUBlock)
                #print(count)
            else:
                for cookie in freq:
                    if cookie[0] == item:
                        cookie[1] += 1
                        cookie[2] = 1
                freq.sort(key=lambda x:x[1])

                for cookie_c in freq:
                    if cookie_c[2] == 1:
                        cookie_1 = cookie_c[1]
                
                for cookie_co in freq:
                    if cookie_co[1] == cookie_1:
                        temp.append(freq.index(cookie_co))
                
                if len(temp) == 1:
                    temp = []
                    pass
                else:
                    A = freq[min(temp):max(temp)+1]
                    A.sort(key=lambda x:x[2])
                    freq[min(temp):max(temp)+1] = A
                    temp = []

                for cooker in freq:
                    cooker[2] = 0

                LFUBlock = []
                for cook in freq:
                    LFUBlock.append(cook[0])
                
                BornSrand.SetLfu(['*']*(length-len(LFUBlock))+LFUBlock+['Hit','-','-','-'])
                
        return 1 - count/len(self.addrstream)