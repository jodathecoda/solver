#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import settings
import shutil
import operator
import report
import time
import settings

class Ranked_fish:
        def __init__(self, fish_name):
                self.name = fish_name
                self.hu_value = 0.0
                self.sp_value = 0.0
                self.ca_value = 0.0
                self.mt_value = 0.0

                self.hu_rank = 0
                self.sp_rank = 0
                self.ca_rank = 0
                self.mt_rank = 0
                self.ov_rank = 0.0 #overall rank

                cwd = os.getcwd()
                fishname = fish_name
                filename = cwd + "/fishes/" + fishname + "/bankroll.dat"
                try:
                        with open(filename, "r") as f:
                                lines = f.read().splitlines()
                                self.hu_value = float(lines[0])
                                self.sp_value = float(lines[1])
                                self.ca_value = float(lines[2])
                                self.mt_value = float(lines[3])
                        f.close()
                except IOError:
                        print("no such file " + filename)
                        dumb = input("]")
                 
def run():
        cwd = os.getcwd()
        list_of_ranked_fishes = []
        hu_rank_list = []
        sp_rank_list = []
        ca_rank_list = []
        mt_rank_list = []

        for fish in settings.allfishes:
                ranked_fish = Ranked_fish(fish)
                list_of_ranked_fishes.append(ranked_fish)
        #here sort list_of_ranked_fishes by key ov_rank
        #and continue with learning - read todo
        hu_rank_list = sorted(list_of_ranked_fishes, key=operator.attrgetter('hu_value'), reverse=True)
        sp_rank_list = sorted(list_of_ranked_fishes, key=operator.attrgetter('sp_value'), reverse=True)
        ca_rank_list = sorted(list_of_ranked_fishes, key=operator.attrgetter('ca_value'), reverse=True)
        mt_rank_list = sorted(list_of_ranked_fishes, key=operator.attrgetter('mt_value'), reverse=True)
        #we get lists sorted, now we need to get ranks 0,1,2,3,...
        #heads up ranks:
        rank_counter = 0
        for botfish in hu_rank_list:
                for fiish in list_of_ranked_fishes:
                        if fiish == botfish:
                                fiish.hu_rank = rank_counter
                rank_counter += 1

        #spin ranks:
        rank_counter = 0
        for botfish in sp_rank_list:
                for fiish in list_of_ranked_fishes:
                        if fiish == botfish:
                                fiish.sp_rank = rank_counter
                rank_counter += 1

        #cash ranks:
        rank_counter = 0
        for botfish in ca_rank_list:
                for fiish in list_of_ranked_fishes:
                        if fiish == botfish:
                                fiish.ca_rank = rank_counter
                rank_counter += 1

        #mtt ranks:
        rank_counter = 0
        for botfish in mt_rank_list:
                for fiish in list_of_ranked_fishes:
                        if fiish == botfish:
                                fiish.mt_rank = rank_counter
                rank_counter += 1

        #overall rank
        for fiish in list_of_ranked_fishes:
                fiish.ov_rank = (fiish.hu_rank + fiish.sp_rank + fiish.ca_rank + fiish.mt_rank)/4.0

        sorted_by_overall_list_of_ranked_fishes = sorted(list_of_ranked_fishes, key=operator.attrgetter('ov_rank'), reverse=False)
        settings.print_logo()
        print("name/rank     heads up   spins      cash    tournament")
        print("------------------------------------------------------")
        for fiish in sorted_by_overall_list_of_ranked_fishes:
                print('%-12s%-5s%-5s%-5s%-5s%-5s%-5s%-5s%-5s' % (fiish.name, " ",  str(fiish.hu_rank + 1), " ", str(fiish.sp_rank + 1), " ", str(fiish.ca_rank + 1), " ", str(fiish.mt_rank + 1)))
        dumb = input("]")