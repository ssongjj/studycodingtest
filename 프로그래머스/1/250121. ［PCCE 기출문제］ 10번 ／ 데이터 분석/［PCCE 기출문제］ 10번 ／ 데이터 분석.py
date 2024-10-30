def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    keys = ["code", "date", "maximum", "remain"]
    
    ext_idx = keys.index(ext)
    sort_idx = keys.index(sort_by)
    
    answer = sorted([d for d in data if d[ext_idx] <= val_ext], key = lambda x: x[sort_idx])
    return answer