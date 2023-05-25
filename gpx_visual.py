import gpxpy
import gmplot
import matplotlib.pyplot as plt

# Чтение GPX файла
def read_gpx_file(file_path):
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        return gpx.tracks[0].segments[0].points

# Визуализация маршрута на спутниковой карте
def visualize_route(points):
    # Получение координат точек маршрута
    lats = [point.latitude for point in points]
    lngs = [point.longitude for point in points]

    # Создание объекта карты
    gmap = gmplot.GoogleMapPlotter(lats[0], lngs[0], 14)

    # Добавление маркера на начальную точку
    gmap.marker(lats[0], lngs[0], 'cornflowerblue')

    # Добавление пути на карту
    gmap.plot(lats, lngs, 'cornflowerblue', edge_width=2)

    # Сохранение карты в HTML файл
    gmap.draw('route_map.html')

# Построение графика скорости для каждого километра маршрута
def plot_speed_graph(points):
    distances = []
    speeds = []

    # Расчет расстояния и скорости между точками
    for i in range(1, len(points)):
        distance = points[i].distance_2d(points[i-1])
        speed = distance / (points[i].time - points[i-1].time).total_seconds()

        distances.append(distance)
        speeds.append(speed)

    # Кумулятивная сумма расстояний для километров
    cumulative_distances = [0]
    cumulative_speeds = [0]

    for i in range(len(distances)):
        cumulative_distances.append(cumulative_distances[-1] + distances[i])
        cumulative_speeds.append(speeds[i])

    # Построение графика скорости
    plt.plot(cumulative_distances, cumulative_speeds)
    plt.xlabel('Distance (m)')
    plt.ylabel('Speed (m/s)')
    plt.title('Speed vs Distance')
    plt.grid(True)
    plt.savefig('speed_graph.png')
    plt.show()

# Путь к GPX файлу
gpx_file_path = 'mushroms_2023-05-24_15-59_Wed.gpx'

# Чтение GPX файла
points = read_gpx_file(gpx_file_path)

# Визуализация маршрута на карте
visualize_route(points)

# Построение графика скорости
plot_speed_graph(points)

