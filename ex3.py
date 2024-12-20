class Solution(object):
    def merge(intervals):
        intervals.sort(key=lambda x: x[0]) #сортирует интервалы по началу каждого интервала

        merged = [intervals[0]] #список для хранения объединенных интервалов

        for interval in intervals: #если текущий интервал не пересекается с последним добавленным,
                                #добавляется как новый элемент в список
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else: #иначе обновляется конец последнего добавленного интервала
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    print(merge(([[1,3],[2,6],[8,10],[15,18]])))