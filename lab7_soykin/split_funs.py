def split_data(file, interval):
    data = []
    data_temp = []

    start_time = None
    prev_time = None

    for info in file:
        try:
            time_value = float(info["time"])
            value = int(info["value"])
        except:
            return None
        if start_time is None:  # 1
            start_time = time_value

        if prev_time is not None and time_value >= start_time + interval:  # >=2
            data.append((data_temp, {"start_time": start_time, "end_time": prev_time}))
            start_time = time_value
            data_temp = []

        data_temp.append(value)
        prev_time = time_value  # Обновляем предыдущее время

    if data_temp:
        data.append((data_temp, {"start_time": start_time, "end_time": prev_time}))

    return data
