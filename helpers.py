import random


def get_area(ent, side_a, side_b, side_c):
    ent.delete(0, 'end')
    try:
        a = float(side_a)
        b = float(side_b)
        c = float(side_c)

        if ((a + b > c) and (a + c > b) and (b + c > a)):
            s = (a + b + c)/2

            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

            ent.insert(0, "{:.2f}".format(area))
        else:
            ent.insert(0, 'That\'s impossible')
    except ValueError:
        ent.insert(0, 'Numbers only please')


def get_max_edge(ent, side_a, side_b):
    ent.delete(0, 'end')
    try:
        a = float(side_a)
        b = float(side_b)

        side_c_max = a + b - 1
        side_c_min = max(a, b) - min(a, b) + 1

        if (side_c_min > side_c_max):
            ent.insert(0, 'Does not compute')
        else:
            ent.insert(0, int(side_c_max))
    except ValueError:
        ent.insert(0, 'Numbers only please')


def convert_to_seconds(ent, hours, minutes):
    ent.delete(0, 'end')
    time_hash = {'hours': hours, 'minutes': minutes}

    if(not hours and not minutes):
        ent.insert(0, 'Gimme something')
    else:
        for k, v in time_hash.items():
            if(not v):
                time_hash[k] = 0
            else:
                try:
                    time_hash[k] = float(v)
                except ValueError:
                    ent.insert(0, 'Numbers only please')
                    return

        ent.insert(0, int(time_hash['hours']*3600 + time_hash['minutes']*60))


def set_lable_concat(ent, times, string):
    ent.delete(0, 'end')
    try:
        times = int(times)
        ent.insert(0, concat_string(times, string))
    except ValueError:
        ent.insert(0, '{} is not a number.'.format(times))


def concat_string(n, string):
    if n > 0:
        return string + concat_string(n-1, string)
    else:
        return ''


def clear_entries(entries):
    for ent in entries:
        ent.delete(0, 'end')
