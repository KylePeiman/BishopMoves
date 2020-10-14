
def solution(start,end,moves):
    y_1 = ord(start[0])
    y_2 = ord(end[0])
    x_1 = int(start[1])
    x_2 = int(end[1])
    if moves == 0:
        return start==end
    if (moves == 1) and ((abs(y_2 - y_1)) == abs((x_2 - x_1))):
       return True
    elif moves >= 2 and ((y_1 + x_1) % 2 == (y_2 + x_2) % 2):
        return True
    return False

