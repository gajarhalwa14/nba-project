def calculate_potd(filtered_performances):
    if not filtered_performances:
        return None

    best_player = None
    best_score = float('-inf')

    for p in filtered_performances:
        ts_denominator = 2 * (p.fga + 0.44 * p.fta)
        ts_pct = (p.pts / ts_denominator) if ts_denominator > 0 else 0

        ts_multiplier = (ts_pct / 0.57) if ts_pct > 0 else 1.0

        fg_missed = p.fga - p.fg
        ft_missed = p.fta - p.ft

        base_score = (
            p.pts * 1.0
            + p.off_reb * 0.7
            + p.def_reb * 0.3
            + p.ast * 0.7
            + p.stl * 10.
            + p.blk * 0.7
            - p.fga * 0.7
            - ft_missed * 0.2
            - p.pf * 0.3
            - p.turnovers * 0.6
        )

        adjusted_score = base_score * ts_multiplier

        per_36_score = (adjusted_score / p.actual_minutes) * 36

        if per_36_score > best_score:
            best_score = per_36_score
            best_player = p
    return best_player, round(best_score, 2)      




def calculate_opod(filtered_performances):
    if not filtered_performances:
        return None

    best_player = None
    best_score = float('-inf')

    for p in filtered_performances:
        ts_denominator = 2 * (p.fga + 0.44 * p.fta)
        ts_pct = (p.pts / ts_denominator) if ts_denominator > 0 else 0


        score = (p.pts + p.ast * 1.5 - p.turnovers  * 1.5) * ts_pct

        if (score > best_score):
            best_player = p
            best_score = score
    
    return best_player, round(best_score, 2)



def calculate_dpod(filtered_performances):
    if not filtered_performances:
        return None

    best_player = None
    best_score = float('-inf')

    for p in filtered_performances:
        stocks = p.stl + p.blk

        def_reb_contribution = p.def_reb * 0.3

        foul_penalty = (p.pf * 0.5) + (p.dq * 3.0)

        steal_bonus = p.stl * 0.5

        score = (stocks + def_reb_contribution + steal_bonus - foul_penalty)

        if score > best_score:
            best_player = p
            best_score = score
    
    return best_player, round(best_score, 2)

def calculate_unsung_hero():
    return None

def calculate_cardio_man(filtered_performances):
    if not filtered_performances:
        return None
    
    worst_player = None
    worst_score = float('inf')

    for p in filtered_performances:
        ts_denominator = 2 * (p.fga + 0.44 * p.fta)
        ts_pct = (p.pts / ts_denominator) if ts_denominator > 0 else 0

        ts_multiplier = (ts_pct / 0.57) if ts_pct > 0 else 1.0

        fg_missed = p.fga - p.fg
        ft_missed = p.fta - p.ft

        base_score = (
            p.pts * 1.0
            + p.off_reb * 0.7
            + p.def_reb * 0.3
            + p.ast * 0.7
            + p.stl * 10.
            + p.blk * 0.7
            - p.fga * 0.7
            - ft_missed * 0.2
            - p.pf * 0.3
            - p.turnovers * 0.6
        )

        adjusted_score = base_score * ts_multiplier

        per_36_score = (adjusted_score / p.actual_minutes) * 36

        if worst_player == None:
            worst_player = p
            worst_score = per_36_score
            continue
        if per_36_score < worst_score:
            worst_player = p
            worst_score = per_36_score
    
    return worst_player, round(worst_score, 2)


def calculate_brick_layer(filtered_performances):
    if not filtered_performances:
        return None
    
    worst_player = None
    worst_score = float('inf')

    for p in filtered_performances:
        ts_denominator = 2 * (p.fga + 0.44 * p.fta)
        ts_pct = (p.pts / ts_denominator) if ts_denominator > 0 else 0


        score = (p.pts + p.ast * 1.5 - p.turnovers  * 1.5) * ts_pct

        if worst_player == None:
            worst_player = p
            worst_score = score
            continue
        
        if score < worst_score:
            worst_player = p
            worst_score = score
    
    return worst_player, worst_score

def calculate_traffic_cone(filtered_performances):
    if not filtered_performances:
        return None
    
    worst_player = None
    worst_score = float('inf')

    for p in filtered_performances:
        stocks = p.stl + p.blk

        def_reb_contribution = p.def_reb * 0.3

        foul_penalty = (p.pf * 0.5) + (p.dq * 3.0)

        steal_bonus = p.stl * 0.5

        score = (stocks + def_reb_contribution + steal_bonus - foul_penalty)

        if worst_player == None:
            worst_player = p
            worst_score = score
            continue
        
        if score < worst_score:
            worst_player = p
            worst_score = score
    
    return worst_player, round(worst_score, 2)