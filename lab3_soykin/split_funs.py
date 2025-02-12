
def split_data(file, interval):
    count = float(0)
    data, data_temp=[], []
    end_time=float(0)
    for info in file:
        if count==0:
            data_temp=[]
            start_time=float(info['time'])
            end_time=start_time+interval
            print(start_time, end_time)
        if float(info['time'])>=end_time:
            data.append(data_temp)
            count=0
            data_temp=[]
        else:
            count+=float(info['time'])
            data_temp.append(float(info['value']))
    print(data)
