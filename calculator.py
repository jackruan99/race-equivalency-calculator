import datetime
# import matplotlib.pyplot as plt


WORLD_RECORDS = {'800m': '1:40.91',
                 '1000m': '2:11.96',
                 '1500m': '3:26.00',
                 'mile': '3:43.13',
                 '3k': '7:20.67',
                 '5k': '12:35.36',
                 '10k': '26:11.00',
                 'half marathon': '57:31',
                 'marathon': '2:01:39'}


def dist_str_to_meters(dist_str: str) -> int:
    DISTANCES = {'800m': 800,
                 '1000m': 1000,
                 '1500m': 1500,
                 'mile': 1609.34,
                 '3k': 3000,
                 '5k': 5000,
                 '10k': 10000,
                 'half marathon': 21097.5,
                 'marathon': 42195}
    return DISTANCES[dist_str]


def time_str_to_seconds(time_str: str) -> float:
    times = time_str.split(':')
    if len(times) == 2:
        seconds = int(times[0]) * 60 + float(times[1])
    elif len(times) == 3:
        seconds = int(times[0]) * 3600 + int(times[1]) * 60 + float(times[2])
    return seconds


def print_prediction(factor: float):
    print('-- PREDICTIONS --')
    for event, time in WORLD_RECORDS.items():
        time_in_seconds = time_str_to_seconds(time)
        your_time_str = str(datetime.timedelta(
            seconds=round(time_in_seconds * factor)))
        print(f'{event}: {your_time_str}')


# def graph(factor: float):
#     distances = [dist_str_to_meters(key) for key in WORLD_RECORDS.keys()]
#     times = [time_str_to_seconds(value) for value in WORLD_RECORDS.values()]
#     plt.plot(distances, times)
#     plt.title('World Records')
#     plt.xlabel('Distance')
#     plt.ylabel('Time')
#     plt.show()


def calculator():
    print('Distances: 800m, 1000m, 1500m, mile, 3k, 5k, 10k, half marathon, marathon')
    dist_str = input('Enter a distance: ')
    time_str = input('Enter your time: ')

    your_time_in_seconds = time_str_to_seconds(time_str)
    world_record_in_seconds = time_str_to_seconds(WORLD_RECORDS[dist_str])
    factor = your_time_in_seconds / world_record_in_seconds
    print_prediction(factor)

    # graph(factor)


calculator()
