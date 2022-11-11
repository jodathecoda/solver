#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import settings
import seat
import formulas

global cwd
cwd = os.getcwd()

class PoolSeat():
    def __init__(self, fishname):
        self.name = fishname
        self.sea = "blue sea"
        self.splitrange = "unknown"
        self.paggression = 0 #preflop aggression
        self.faggression = 0 #flop aggression
        self.taggression = 0 #turn aggression
        self.raggression = 0 #river aggression
        self.range_ug_open = [] #ug open
        self.range_hj_open = [] #hj open
        self.range_co_open = [] #co open
        self.range_db_open = [] #dealer open
        self.range_sb_open = [] #sb open
        self.range_hd_open = [] #heads up dealer open
        self.range_hb_defend = [] #heads up big blind defend
        self.range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
        self.range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
        self.range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
        self.range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
        self.range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
        self.range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
        self.range_defend_vs_db_op = [] #defend range vs dealer button always out of position
        self.range_defend_vs_sb_ip = [] #defend range vs small blind always in position
        self.range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
        self.range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
        self.range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
        self.range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
        self.range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
        self.range_call_vs_under10bb_push_more_left_behind = [] #call a push from player who has under 10bb and pushes, 2+ left after you to act
        self.range_top1_8 = ['aa', 'kk', 'qq', 'jj']
        self.range_top2_7 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99']
        self.range_top6 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs', 'kqs', '88', 'ats', 'aqo']

        #flop threshold values vs 1
        self.threshold_flop_open_vs_one = 0.0
        self.threshold_flop_bluff_vs_one = 0.0
        self.threshold_flop_call_vs_one = 0.0
        self.threshold_flop_raise_vs_one = 0.0
        self.threshold_flop_call3bet_vs_one = 0.0
        self.threshold_flop_raise4bet_vs_one = 0.0
        self.threshold_flop_shove = 0.0
        #flop threshold values vs more
        self.threshold_flop_open_vs_more = 0.0
        self.threshold_flop_call_vs_more = 0.0
        self.threshold_flop_raise_vs_more = 0.0
        self.threshold_flop_call3bet_vs_more = 0.0
        self.threshold_flop_raise4bet_vs_more = 0.0
        #turn threshold values vs 1
        self.threshold_turn_open_vs_one = 0.0
        self.threshold_turn_bluff_vs_one = 0.0
        self.threshold_turn_call_vs_one = 0.0
        self.threshold_turn_raise_vs_one = 0.0
        self.threshold_turn_call3bet_vs_one = 0.0
        self.threshold_turn_raise4bet_vs_one = 0.0
        self.threshold_turn_shove = 0.0
        #turn threshold values vs more
        self.threshold_turn_open_vs_more = 0.0
        self.threshold_turn_call_vs_more = 0.0
        self.threshold_turn_raise_vs_more = 0.0
        self.threshold_turn_call3bet_vs_more = 0.0
        self.threshold_turn_raise4bet_vs_more = 0.0
        #river threshold values vs 1
        self.threshold_river_open_vs_one = 0.0
        self.threshold_river_bluff_vs_one = 0.0
        #self.threshold_river_call_vs_one = 0.0
        self.threshold_river_raise_vs_one = 0.0
        self.threshold_river_call3bet_vs_one = 0.0
        self.threshold_river_raise4bet_vs_one = 0.0
        self.threshold_river_shove = 0.0
        #river threshold values vs more
        self.threshold_river_open_vs_more = 0.0
        self.threshold_river_call_vs_more = 0.0
        self.threshold_river_raise_vs_more = 0.0
        self.threshold_river_call3bet_vs_more = 0.0
        self.threshold_river_raise4bet_vs_more = 0.0
       

class Pool():
    def __init__(self):
        self.fishpool = []
        for fishname in settings.allfishes:
            self.fishpool.append(PoolSeat(fishname))
        self.update_all()

    def update_fish(self, fish):
        for poolfish in self.fishpool:
            if fish.name == poolfish.name:
                fish.paggression = poolfish.paggression
                fish.faggression = poolfish.faggression
                fish.taggression = poolfish.taggression
                fish.raggression = poolfish.raggression
                fish.splitrange = poolfish.splitrange
                fish.range_ug_open = poolfish.range_ug_open
                fish.range_co_open = poolfish.range_co_open
                fish.range_hj_open = poolfish.range_hj_open
                fish.range_db_open = poolfish.range_db_open
                fish.range_sb_open = poolfish.range_sb_open
                fish.range_hd_open = poolfish.range_hd_open
                fish.range_hb_defend = poolfish.range_hb_defend
                fish.range_defend_vs_ug_ip = poolfish.range_defend_vs_ug_ip
                fish.range_defend_vs_ug_op = poolfish.range_defend_vs_ug_op
                fish.range_defend_vs_hj_ip = poolfish.range_defend_vs_hj_ip
                fish.range_defend_vs_hj_op = poolfish.range_defend_vs_hj_op
                fish.range_defend_vs_co_ip = poolfish.range_defend_vs_co_ip
                fish.range_defend_vs_co_op = poolfish.range_defend_vs_co_op
                fish.range_defend_vs_db_op = poolfish.range_defend_vs_db_op
                fish.range_defend_vs_sb_ip = poolfish.range_defend_vs_sb_ip
                fish.range_under10bb_push_vs_1 = poolfish.range_under10bb_push_vs_1
                fish.range_under10bb_push_vs_2 = poolfish.range_under10bb_push_vs_2
                fish.range_under10bb_push_vs_more = poolfish.range_under10bb_push_vs_more
                fish.range_call_vs_under10bb_push_0_left_behind = poolfish.range_call_vs_under10bb_push_0_left_behind
                fish.range_call_vs_under10bb_push_1_left_behind = poolfish.range_call_vs_under10bb_push_1_left_behind
                fish.range_call_vs_under10bb_push_more_left_behind = poolfish.range_call_vs_under10bb_push_more_left_behind
                #postflop threshold values
                #flop
                fish.threshold_flop_open_vs_one = poolfish.threshold_flop_open_vs_one
                fish.threshold_flop_call_vs_one = poolfish.threshold_flop_call_vs_one
                fish.threshold_flop_bluff_vs_one = poolfish.threshold_flop_bluff_vs_one
                fish.threshold_flop_raise_vs_one = poolfish.threshold_flop_raise_vs_one
                fish.threshold_flop_call3bet_vs_one = poolfish.threshold_flop_call3bet_vs_one
                fish.threshold_flop_raise4bet_vs_one = poolfish.threshold_flop_raise4bet_vs_one
                fish.threshold_flop_shove = poolfish.threshold_flop_shove
                fish.threshold_flop_open_vs_more = poolfish.threshold_flop_open_vs_more
                fish.threshold_flop_call_vs_more = poolfish.threshold_flop_call_vs_more
                fish.threshold_flop_raise_vs_more = poolfish.threshold_flop_raise_vs_more
                fish.threshold_flop_call3bet_vs_more = poolfish.threshold_flop_call3bet_vs_more
                fish.threshold_flop_raise4bet_vs_more = poolfish.threshold_flop_raise4bet_vs_more
                #turn
                fish.threshold_turn_open_vs_one = poolfish.threshold_turn_open_vs_one
                fish.threshold_turn_call_vs_one = poolfish.threshold_turn_call_vs_one
                fish.threshold_turn_bluff_vs_one = poolfish.threshold_turn_bluff_vs_one
                fish.threshold_turn_raise_vs_one = poolfish.threshold_turn_raise_vs_one
                fish.threshold_turn_call3bet_vs_one = poolfish.threshold_turn_call3bet_vs_one
                fish.threshold_turn_raise4bet_vs_one = poolfish.threshold_turn_raise4bet_vs_one
                fish.threshold_turn_shove = poolfish.threshold_turn_shove
                fish.threshold_turn_open_vs_more = poolfish.threshold_turn_open_vs_more
                fish.threshold_turn_call_vs_more = poolfish.threshold_turn_call_vs_more
                fish.threshold_turn_raise_vs_more =  poolfish.threshold_turn_raise_vs_more
                fish.threshold_turn_call3bet_vs_more = poolfish.threshold_turn_call3bet_vs_more
                fish.threshold_turn_raise4bet_vs_more = poolfish.threshold_turn_raise4bet_vs_more
                #river
                fish.threshold_river_open_vs_one = poolfish.threshold_river_open_vs_one
                fish.threshold_river_bluff_vs_one = poolfish.threshold_river_bluff_vs_one
                fish.threshold_river_raise_vs_one =  poolfish.threshold_river_raise_vs_one
                fish.threshold_river_call3bet_vs_one = poolfish.threshold_river_call3bet_vs_one
                fish.threshold_river_raise4bet_vs_one = poolfish.threshold_river_raise4bet_vs_one
                fish.threshold_river_shove = poolfish.threshold_river_shove
                fish.threshold_river_open_vs_more = poolfish.threshold_river_open_vs_more
                fish.threshold_river_call_vs_more = poolfish.threshold_river_call_vs_more
                fish.threshold_river_raise_vs_more = poolfish.threshold_river_raise_vs_more
                fish.threshold_river_call3bet_vs_more = poolfish.threshold_river_call3bet_vs_more
                fish.threshold_river_raise4bet_vs_more = poolfish.threshold_river_raise4bet_vs_more
                
                fish.sea = poolfish.sea
                return

    def update_all(self):
        for s in self.fishpool:
            fileaggression = cwd + "/fishes/" + s.name + "/pa.dat" #first take preflop aggression
            try:
                with open(fileaggression, "r") as f:
                    s.paggression = int(f.read())
                f.close()
            except:
                print("no such file " + fileaggression)
                dumb = input("]")
            fileaggression = cwd + "/fishes/" + s.name + "/fa.dat" # take flop aggression
            try:
                with open(fileaggression, "r") as f:
                    s.faggression = int(f.read())
                f.close()
            except:
                print("no such file " + fileaggression)
                dumb = input("]")
            fileaggression = cwd + "/fishes/" + s.name + "/ta.dat" # take turn aggression
            try:
                with open(fileaggression, "r") as f:
                    s.taggression = int(f.read())
                f.close()
            except:
                print("no such file " + fileaggression)
                dumb = input("]")
            fileaggression = cwd + "/fishes/" + s.name + "/ra.dat" # take river aggression
            try:
                with open(fileaggression, "r") as f:
                    s.raggression = int(f.read())
                f.close()
            except:
                print("no such file " + fileaggression)
                dumb = input("]")    

            
            #if s.name in settings.allfishes:                    
            filerangetype = cwd + "/fishes/" + s.name + "/rt.dat" #range type 0=merged 1=polarized
            range_type_as_digit = 2
            try:
                with open(filerangetype, "r") as f:
                    range_type_as_digit = int(f.read())
                f.close()
            except:
                print("no such file " + fileaggression)
                dumb = input("]")
            if range_type_as_digit == 1:
                s.splitrange = "polarized"
            else:
                s.splitrange = "merged"

            #sea update
            filesea = cwd + "/fishes/" + s.name + "/sea.dat"
            #newsea = "gray sea"
            try:
                with open(filesea, "r") as f:
                    seacode = f.read()
                    s.sea = seacode #read from file and update in program
                f.close()
            except IOError:
                print("no such file " + filesea)
                dumb = input("]")

                    
            filerange = cwd + "/fishes/" + s.name + "/ranges/ug_open.range"
            try:
                with open(filerange, "r") as f:
                    s.range_ug_open = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_ug_open) < len(s.range_top1_8):
                #less than minimum, will use minimum
                s.range_ug_open = s.range_top1_8

            filerange = cwd + "/fishes/" + s.name + "/ranges/hj_open.range"
            try:
                with open(filerange, "r") as f:
                    s.range_hj_open = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_hj_open) < len(s.range_top1_8):
                #less than minimum, will use minimum
                s.range_hj_open = s.range_top1_8

            filerange = cwd + "/fishes/" + s.name + "/ranges/co_open.range"
            try:
                with open(filerange, "r") as f:
                    s.range_co_open = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_co_open) < len(s.range_top2_7):
                #less than minimum, will use minimum
                s.range_co_open = s.range_top2_7

            filerange = cwd + "/fishes/" + s.name + "/ranges/db_open.range"
            try:
                with open(filerange, "r") as f:
                    s.range_db_open = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_db_open) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_db_open = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/sb_open.range"
            try:
                with open(filerange, "r") as f:
                    s.range_sb_open = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_sb_open) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_sb_open = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/hd_open.range"
            try:
                with open(filerange, "r") as f:
                        s.range_hd_open = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_hd_open) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_hd_open = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/hb_defend.range"
            try:
                with open(filerange, "r") as f:
                    s.range_hb_defend = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_hb_defend) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_hb_defend = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_ug_ip.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_ug_ip = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_ug_ip) < len(s.range_top2_7):
                #less than minimum, will use minimum
                s.range_defend_vs_ug_ip = s.range_top2_7

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_ug_op.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_ug_op = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_ug_op) < len(s.range_top2_7):
                #less than minimum, will use minimum
                s.range_defend_vs_ug_op = s.range_top2_7

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_hj_ip.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_hj_ip = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_hj_ip) < len(s.range_top2_7):
                #less than minimum, will use minimum
                s.range_defend_vs_hj_ip = s.range_top2_7

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_hj_op.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_hj_op = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_hj_op) < len(s.range_top2_7):
                #less than minimum, will use minimum
                s.range_defend_vs_hj_op = s.range_top2_7

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_co_ip.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_co_ip = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_co_ip) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_defend_vs_co_ip = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_co_op.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_co_op = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_co_op) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_defend_vs_co_op = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_db_op.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_db_op = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_db_op) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_defend_vs_db_op = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/defend_vs_sb_ip.range"
            try:
                with open(filerange, "r") as f:
                    s.range_defend_vs_sb_ip = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_defend_vs_sb_ip) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_defend_vs_sb_ip = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/under10bb_push_vs_1.range"
            try:
                with open(filerange, "r") as f:
                    s.range_under10bb_push_vs_1 = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_under10bb_push_vs_1) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_under10bb_push_vs_1 = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/under10bb_push_vs_2.range"
            try:
                with open(filerange, "r") as f:
                    s.range_under10bb_push_vs_2 = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_under10bb_push_vs_2) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_under10bb_push_vs_2 = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/under10bb_push_vs_more.range"
            try:
                with open(filerange, "r") as f:
                    s.range_under10bb_push_vs_more = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_under10bb_push_vs_more) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_under10bb_push_vs_more = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/call_vs_under10bb_push_0_left_behind.range"
            try:
                with open(filerange, "r") as f:
                    s.range_call_vs_under10bb_push_0_left_behind = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_call_vs_under10bb_push_0_left_behind) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_call_vs_under10bb_push_0_left_behind = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/call_vs_under10bb_push_1_left_behind.range"
            try:
                with open(filerange, "r") as f:
                    s.range_call_vs_under10bb_push_1_left_behind = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_call_vs_under10bb_push_1_left_behind) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_call_vs_under10bb_push_1_left_behind = s.range_top6

            filerange = cwd + "/fishes/" + s.name + "/ranges/call_vs_under10bb_push_more_left_behind.range"
            try:
                with open(filerange, "r") as f:
                    s.range_call_vs_under10bb_push_more_left_behind = f.read().split()
                f.close()
            except:
                print("no such file " + filerange)
                dumb = input("]")
            if len(s.range_call_vs_under10bb_push_more_left_behind) < len(s.range_top6):
                #less than minimum, will use minimum
                s.range_call_vs_under10bb_push_more_left_behind = s.range_top6
            
            #postflop threshold values
            #flop
            fa = s.faggression/100.0
            ta = s.taggression/100.0
            ra = s.raggression/100.0
            s.threshold_flop_open_vs_one = formulas.threshold_flop_open_vs_one(fa)
            s.threshold_flop_call_vs_one = formulas.threshold_flop_call_vs_one(fa)
            s.threshold_flop_bluff_vs_one = formulas.threshold_flop_bluff_vs_one(fa)
            s.threshold_flop_raise_vs_one = formulas.threshold_flop_raise_vs_one(fa)
            s.threshold_flop_call3bet_vs_one = formulas.threshold_flop_call3bet_vs_one(fa)
            s.threshold_flop_raise4bet_vs_one = formulas.threshold_flop_raise4bet_vs_one(fa) 
            s.threshold_flop_shove = formulas.threshold_flop_shove(fa)
            s.threshold_flop_open_vs_more = formulas.threshold_flop_open_vs_more(fa)
            s.threshold_flop_call_vs_more = formulas.threshold_flop_call_vs_more(fa)
            s.threshold_flop_raise_vs_more = formulas.threshold_flop_raise_vs_more(fa)
            s.threshold_flop_call3bet_vs_more = formulas.threshold_flop_call3bet_vs_more(fa)
            s.threshold_flop_raise4bet_vs_more = formulas.threshold_flop_raise4bet_vs_more(fa)
            #turn
            s.threshold_turn_open_vs_one = formulas.threshold_turn_open_vs_one(ta)
            s.threshold_turn_call_vs_one = formulas.threshold_turn_call_vs_one(ta)
            s.threshold_turn_bluff_vs_one = formulas.threshold_turn_bluff_vs_one(ta)
            s.threshold_turn_raise_vs_one = formulas.threshold_turn_raise_vs_one(ta)
            s.threshold_turn_call3bet_vs_one = formulas.threshold_turn_call3bet_vs_one(ta)
            s.threshold_turn_raise4bet_vs_one = formulas.threshold_turn_raise4bet_vs_one(ta)
            s.threshold_turn_shove = formulas.threshold_turn_shove(ta)
            s.threshold_turn_open_vs_more = formulas.threshold_turn_open_vs_more(ta)
            s.threshold_turn_call_vs_more = formulas.threshold_turn_call_vs_more(ta)
            s.threshold_turn_raise_vs_more =  formulas.threshold_turn_raise_vs_more(ta)
            s.threshold_turn_call3bet_vs_more = formulas.threshold_turn_call3bet_vs_more(ta)
            s.threshold_turn_raise4bet_vs_more = formulas.threshold_turn_raise4bet_vs_more(ta)
            #river
            s.threshold_river_open_vs_one = formulas.threshold_river_open_vs_one(ra)
            s.threshold_river_bluff_vs_one = formulas.threshold_river_bluff_vs_one(ra)
            s.threshold_river_raise_vs_one =  formulas.threshold_river_raise_vs_one(ra)
            s.threshold_river_call3bet_vs_one = formulas.threshold_river_call3bet_vs_one(ra)
            s.threshold_river_raise4bet_vs_one = formulas.threshold_river_raise4bet_vs_one(ra)  
            s.threshold_river_shove = formulas.threshold_river_shove(ra)
            s.threshold_river_open_vs_more = formulas.threshold_river_open_vs_more(ra)
            s.threshold_river_call_vs_more = formulas.threshold_river_call_vs_more(ra)
            s.threshold_river_raise_vs_more = formulas.threshold_river_raise_vs_more(ra)
            s.threshold_river_call3bet_vs_more = formulas.threshold_river_call3bet_vs_more(ra)
            s.threshold_river_raise4bet_vs_more = formulas.threshold_river_raise4bet_vs_more(ra)
