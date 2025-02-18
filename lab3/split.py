def split_data(data, interval):

    intervals = []
    start_time = data[0][0]
    current_segment = []

    for time, value in data:
        if time < start_time + interval:
            current_segment.append((time, value))
        else:
            intervals.append((start_time, start_time + interval, current_segment))
            start_time += interval
            current_segment = [(time, value)]

    if current_segment:
        intervals.append((start_time, start_time + interval, current_segment))

    return intervals