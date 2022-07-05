from itertools import permutations
from pprint import pprint


def distance(point_1: tuple, point_2: tuple) -> float:
    """Расчет растояния между двумя точками(городами)"""
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def different_ways(addr: tuple) -> dict:
    """Возможные варианты путей начиная с 'post'"""
    start = (addr[0],)
    diff_ways = {}
    ways = [start + i + start for i in permutations(addr[1:])]
    for way in ways:
        temp_lst = []
        for i in range(len(way) - 1):
            dist = distance(way[i], way[i + 1])
            temp_lst.append(dist)
        diff_ways[way] = temp_lst
    return diff_ways


def short_way(diff_ways: dict) -> (tuple, float):
    """Поиск кратчайшего пути"""
    min_road = 0
    road = ()
    data = []
    for key, value in diff_ways.items():
        s = sum(value)
        data.append(s)
        if s == min(data):
            min_road = s
            road = key
    return road, min_road


def output_data(data: tuple, min_dist: float) -> str:
    """Вывод данных по форме ТЗ"""
    start = str(data[0])
    st = start
    for i in range(len(data) - 1):
        st += f" -> {data[i + 1]}"
        d = distance(data[i], data[i + 1])
        st += f"[{d}]"
    st += f" = {min_dist}"
    return st


if __name__ == "__main__":
    post = (0, 2)
    griboedova = (2, 5)
    baker_st = (5, 2)
    bolshaya_sadovaya_st = (6, 6)
    evergreen_alley = (8, 3)
    some_point = (20, 60)  # доп. точка
    other_some_point = (90, 21)  # доп. точка
    addresses = (post, griboedova, baker_st,
                 some_point, bolshaya_sadovaya_st,
                 evergreen_alley,  other_some_point)
    diff_way = different_ways(addresses)
    way, min_distance = short_way(diff_way)
    result = output_data(way, min_distance)
    pprint(result)
