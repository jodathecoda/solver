#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import settings
import reset
import shutil
import operator
import report
import random
import time
import ranges

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

def remove_fishes_from_school(the_list, val):
   return [value for value in the_list if value != val]
                 
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

        sorted_by_overall_list_of_ranked_fishes = sorted(list_of_ranked_fishes, key=operator.attrgetter('ov_rank'), reverse=True)
        school = []
        for fiish in sorted_by_overall_list_of_ranked_fishes:
                lines = ""
                filename = cwd + "/fishes/" + fiish.name + "/ranking_history.dat"
                if not os.path.isfile(filename):
                        print("error no such file: " + filename)
                        dumb = input("]")

                with open(filename, "r") as f:
                        lines = f.readlines()
                f.close()
                ranking_history_list = []
                for lin in lines:
                        ranking_history_list.append(int(lin))
                #now remove 1st position, move all others 1 position back and at last position add the new value then save the file again
                for pos in range(0, len(ranking_history_list)-1):
                        ranking_history_list[pos] = ranking_history_list[pos+1]
                #add the new value at last position
                ranking_history_list[len(ranking_history_list)-1] = str(55 - int(fiish.ov_rank))
                #save the new data to the file
                filename = cwd + "/fishes/" + fiish.name + "/ranking_history.dat"
                if not os.path.isfile(filename):
                        print("error no such file: " + filename)
                        dumb = input("]")

                with open(filename, "w") as f:
                        for dat in ranking_history_list:
                                f.write(str(dat) + "\n")
                f.close()

        #school = sorted_by_overall_list_of_ranked_fishes
        for fishi in sorted_by_overall_list_of_ranked_fishes:
                school.append(fishi.name)
        #if fish is explicitly in out_of_school file, do not train it even if it is weak fish
        outofschool=[]
        #if not os.path.isfile('fishes/out_of_school.dat'):
                #open('fishes/out_of_school.dat', 'a').close()
        file_out_of_schl = open('fishes/out_of_school.dat',"r")
        lines_out_of_school = file_out_of_schl.read().splitlines()
        file_out_of_schl.close()
        for lin in lines_out_of_school:
                outofschool.append(lin)

        for dumbfish in school:
                if dumbfish in outofschool or dumbfish in settings.referencefishes:
                        school = remove_fishes_from_school(school, dumbfish)
                        #school.remove(dumbfish)
        
        #dumbest ones - the last 1/4 will change its aggression
        dumbest_fishes = []
        #second dumbest to them 2/4 will change hands in their ranges
        second_to_dumbest_fishes = []


        len_of_school = len(school)
        half = round(len(school)/2)
        one_third = round(len(school)/3 -1)

        if len(school) >= 4:
                for i in range(half, half + one_third):
                        second_to_dumbest_fishes.append(school[i])
                #we need at least 4 fishes in the school 
                #so we can proceed with learning
                #the 4th will change its aggression
                #the third will change its ranges
                for i in range(half + one_third, len_of_school):
                        dumbest_fishes.append(school[i])
        else:
                if settings.view < 4:
                        print("not enough fishes in school, will skip learning")
                        time.sleep(2)

        if len(second_to_dumbest_fishes):
                #here change ranges
                for fool in second_to_dumbest_fishes:
                        ranges.run(fool)
        else:
                pass
        
        if len(dumbest_fishes):
                for fool in dumbest_fishes:
                        dumb_fish_aggression_file = cwd + "/fishes/" + fool + "/pa.dat" #change preflop aggression
                        if os.path.isfile(dumb_fish_aggression_file):
                                with open(dumb_fish_aggression_file, "w") as df:
                                        df.write(str(random.randint(20,40)) + "\n")
                                f.close()
                        else:
                                print("no such file: " + dumb_fish_aggression_file)
                                dumb = input("]")

                        dumb_fish_aggression_file = cwd + "/fishes/" + fool + "/fa.dat" #change flop aggression
                        if os.path.isfile(dumb_fish_aggression_file):
                                with open(dumb_fish_aggression_file, "w") as df:
                                        df.write(str(random.randint(20,40)) + "\n")
                                f.close()
                        else:
                                print("no such file: " + dumb_fish_aggression_file)
                                dumb = input("]")

                        dumb_fish_aggression_file = cwd + "/fishes/" + fool + "/ta.dat" #change turn aggression
                        if os.path.isfile(dumb_fish_aggression_file):
                                with open(dumb_fish_aggression_file, "w") as df:
                                        df.write(str(random.randint(20,40)) + "\n")
                                f.close()
                        else:
                                print("no such file: " + dumb_fish_aggression_file)
                                dumb = input("]")

                        dumb_fish_aggression_file = cwd + "/fishes/" + fool + "/ra.dat" #change river aggression
                        if os.path.isfile(dumb_fish_aggression_file):
                                with open(dumb_fish_aggression_file, "w") as df:
                                        df.write(str(random.randint(20,40)) + "\n")
                                f.close()

                        dumb_fish_rangetype_file = cwd + "/fishes/" + fool + "/rt.dat" #change rnge type merged/polarized
                        if os.path.isfile(dumb_fish_rangetype_file):
                                with open(dumb_fish_rangetype_file, "w") as df:
                                        df.write(str(random.randint(0,1)) + "\n")
                                f.close()

                        else:
                                print("no such file: " + dumb_fish_rangetype_file)
                                dumb = input("]")

                #the most dumb fish will reset ranges to some default values
                #white, yellow, red or black sea because it may be messed up too much
                #for balance in the sea.
                the_most_dumb_fish = dumbest_fishes[-1]
                random_sea_number = random.randint(0,3)
                newseafile = "milkfish"
                #newsea = "white"
                if random_sea_number == 0:
                        #newsea = "white"
                        newseafile = "milkfish"
                elif random_sea_number == 1:
                        #newsea = "yellow"
                        newseafile = "yellowfish"
                elif random_sea_number == 2:
                        #newsea = "red"
                        newseafile = "redfish"
                elif random_sea_number == 3:
                        #newsea = "black"
                        newseafile = "blackfish"
                else:
                        print("inside learning no such sea")
                        dumb = input("]")
                cwd = os.getcwd()
                src = cwd + "/fishes/" + newseafile + "/ranges/"
                dst = cwd + "/fishes/" + the_most_dumb_fish + "/ranges/"
                try:
                        shutil.rmtree(dst)
                        shutil.copytree(src, dst)
                except:
                        print("Error in copy sea ranges")
                        dumb = input("]")
                filesea = "fishes/" + the_most_dumb_fish + "/sea.dat"
                try:
                    with open(filesea, "w+") as f:
                        f.write(str(random_sea_number))
                    f.close()
                except IOError:
                    print("inside learning no such fish: " + the_most_dumb_fish)
                    dumb = input("]")
        else:
                pass

        #update playing pool
        settings.pokerpool.update_all()
        try:
                #pass
                reset.run()
        except:
                print("error in clearing data")
                dumb = input("]")
