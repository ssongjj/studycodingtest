import math 

def calc_time(in_time, out_time):
    time_diff = 0
    
    in_hour, in_min = in_time.split(":")
    out_hour, out_min = out_time.split(":")
    
    #분 계산
    time_diff = int(out_min) - int(in_min)
    
    #시 계산
    time_diff += (int(out_hour) - int(in_hour)) * 60
    
    return time_diff

def calc_fee(fees, car_lst, time): 
    b_time, b_fee, d_time, d_fee = fees
    car_fees = []
    
    for car in car_lst:
        fee = 0
        if time[car] - b_time <= 0:
            car_fees.append(b_fee)
        else:
            fee += b_fee
            fee += math.ceil((time[car] - b_time)/d_time) * d_fee
            car_fees.append(fee)
    return car_fees

def solution(fees, records):
    # 23:59 입차 후 출차 내역 없으면
    # 기본 시간, 기본 시간 지나면 단위 시간부터 단위 요금 추가
    # 단위 시간으로 나누어 떨어지지 않으면 올림
    
    #dictionary  key = 차량 번호, value = 분 계산 (split() In일 때 시간 저장 Out일 때 시간 계산)
    answer = []
    record_dic = {}
    time_dic = {}
    
    for record in records:
        time, car, detail = record.split()
        if detail == "IN":
            record_dic[car] = time
        else:
            if car not in time_dic:
                time_dic[car] = calc_time(record_dic[car], time)
            else:
                time_dic[car] += calc_time(record_dic[car], time)
            del record_dic[car]
            
    end_time = "23:59"
    if len(record_dic) != 0:
        for key, value in record_dic.items():
            if key not in time_dic:
                time_dic[key] = calc_time(value, end_time)
            else:
                time_dic[key] += calc_time(value, end_time)
    
    answer = calc_fee(fees, sorted(time_dic), time_dic)
    
    return answer