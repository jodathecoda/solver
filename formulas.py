#copyright (c) 2019
#jodathecoda@yahoo.com

#postflop threshold values
#flop threshold values vs 1

def threshold_flop_open_vs_one(a):
    return 1-(1.6*a) #threshold_flop_open_vs_one

def threshold_flop_call_vs_one(a):
     return 1-1.4*a #threshold_flop_call_vs_one

def threshold_flop_bluff_vs_one(a):
    return (threshold_flop_call_vs_one(a) - 0.1)

def threshold_flop_raise_vs_one(a):
    return 1-0.7*a #threshold_flop_raise_vs_one

def threshold_flop_call3bet_vs_one(a):
    return 1-(2.0*a-1/1.2*a)#threshold_flop_call3bet_vs_one

def threshold_flop_raise4bet_vs_one(a):
    return 1-(2.0*a-1/0.7*a)#threshold_flop_raise4bet_vs_one

def threshold_flop_shove(a):
    return 1-(2.0*a-1/0.7*a)#threshold_flop_shove

def threshold_flop_open_vs_more(a):
    return 1-(1.4*a)#threshold_flop_open_vs_more

def threshold_flop_call_vs_more(a):
    return 1-(2.0*a-1/1.6*a)#threshold_flop_call_vs_more

def threshold_flop_raise_vs_more(a):
    return 1-0.7*a#threshold_flop_raise_vs_more

def threshold_flop_call3bet_vs_more(a):
    return 1-(2.0*a-1/1.2*a)#threshold_flop_call3bet_vs_more

def threshold_flop_raise4bet_vs_more(a):
    return 1-(2.0*a-1/0.7*a)#threshold_flop_raise4bet_vs_more

def threshold_turn_open_vs_one(a):
    return 1-1.1*a#threshold_turn_open_vs_one

def threshold_turn_call_vs_one(a):
    return 1-1.3*a#threshold_turn_call_vs_one

def threshold_turn_bluff_vs_one(a):
    return (threshold_turn_call_vs_one(a) - 0.08)

def threshold_turn_raise_vs_one(a):
    return 1-0.7*a#threshold_turn_raise_vs_one

def threshold_turn_call3bet_vs_one(a):
    return 1-a#threshold_turn_call3bet_vs_one

def threshold_turn_raise4bet_vs_one(a):
    return 1-(2.0*a-1/0.7*a)#threshold_turn_raise4bet_vs_one

def threshold_turn_shove(a):
    return 1-(2.0*a-1/0.7*a)#threshold_turn_shove

def threshold_turn_open_vs_more(a):
    return 1-a#threshold_turn_open_vs_more

def threshold_turn_call_vs_more(a):
    return 1-(2.0*a-1/1.2*a)#threshold_turn_call_vs_more

def threshold_turn_raise_vs_more(a):
    return 1-(2.0*a-1/0.86*a)#threshold_turn_raise_vs_more

def threshold_turn_call3bet_vs_more(a):
    return 1-(2.0*a-1/0.86*a)#threshold_turn_call3bet_vs_more

def threshold_turn_raise4bet_vs_more(a):
    return 1-(2.0*a-1/0.7*a)#threshold_turn_raise4bet_vs_more

def threshold_river_open_vs_one(a):
    return 1-0.8*a#threshold_river_open_vs_one

def threshold_river_bluff_vs_one(a):
    return 1-a#threshold_river_bluff_vs_one

def threshold_river_raise_vs_one(a):
    return 1-0.4*a#threshold_river_raise_vs_one

def threshold_river_call3bet_vs_one(a):
    return 1-0.75*a#threshold_river_call3bet_vs_one

def threshold_river_raise4bet_vs_one(a):
    return 1-(2.0*a-1/0.7*a)#threshold_river_raise4bet_vs_one

def threshold_river_shove(a):
    return 1-0.3*a#threshold_river_shove

def threshold_river_open_vs_more(a):
    return 1-0.7*a#threshold_river_open_vs_more

def threshold_river_call_vs_more(a):
    return 1-0.8*a#threshold_river_call_vs_more

def threshold_river_raise_vs_more(a):
    return 1-0.3*a#threshold_river_raise_vs_more

def threshold_river_call3bet_vs_more(a):
    return 1-0.3*a#threshold_river_call3bet_vs_more

def threshold_river_raise4bet_vs_more(a):
    return 1-0.2*a#threshold_river_raise4bet_vs_more
