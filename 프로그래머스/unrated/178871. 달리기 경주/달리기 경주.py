def solution(players, callings):
    players_rank = {player: int(idx) for idx, player in enumerate(players)}
    
    for call in callings:
        rank = players_rank[call]
        
        players_rank[call] -= 1
        players_rank[players[rank - 1]] += 1
        
        players[rank - 1], players[rank] = call, players[rank - 1]
                
    return players