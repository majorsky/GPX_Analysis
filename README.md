🗺️ GPX Route Visualization and Speed Analysis

This Python script allows you to read a GPX file, visualize the route on a satellite map, and generate a speed graph for each kilometer of the route.

🚀 Features:

✅ Reads a GPX file and extracts the route points.
✅ Visualizes the route on a satellite map using the gmplot library.
✅ Calculates the distance and speed between each pair of points.
✅ Generates a cumulative speed graph for each kilometer of the route.
✅ Calculates and displays the average speed of the entire route.

📝 Instructions:

1️⃣ Ensure you have the necessary libraries installed: gpxpy, gmplot, and matplotlib.
2️⃣ Replace 'your_track.gpx' with the path to your GPX file.
3️⃣ Run the script.

🌍 GPX Route Visualization:

The script reads the GPX file, extracts the latitude and longitude coordinates of the route points, and creates a gmplot object. It visualizes the route by adding a marker at the starting point and drawing a path on the map.

📈 Speed Graph:

The script calculates the distance and speed between each pair of points using the haversine formula. It then generates a cumulative speed graph, where the x-axis represents the distance in kilometers and the y-axis represents the speed in kilometers per hour. The graph also displays the average speed of the entire route in the graph title.

🌟 Enjoy exploring and analyzing your GPX route with this script! 🌟
🗺️ Визуализация и анализ маршрута GPX

Данный скрипт на языке Python позволяет читать файлы GPX, визуализировать маршрут на спутниковой карте и строить график скорости для каждого километра маршрута.

🚀 Особенности:

✅ Чтение GPX файла и извлечение точек маршрута.
✅ Визуализация маршрута на спутниковой карте с использованием библиотеки gmplot.
✅ Расчет расстояния и скорости между каждой парой точек.
✅ Построение кумулятивного графика скорости для каждого километра маршрута.
✅ Расчет и отображение средней скорости по всему маршруту.

📝 Инструкции:

1️⃣ Убедитесь, что у вас установлены необходимые библиотеки: gpxpy, gmplot и matplotlib.
2️⃣ Замените 'your_track.gpx' на путь к вашему файлу GPX.
3️⃣ Запустите скрипт.

🌍 Визуализация маршрута GPX:

Скрипт читает файл GPX, извлекает координаты широты и долготы точек маршрута и создает объект gmplot. Он визуализирует маршрут, добавляя маркер в начальную точку и рисуя путь на карте.

📈 График скорости:

Скрипт рассчитывает расстояние и скорость между каждой парой точек с помощью формулы гаверсинуса. Затем он строит кумулятивный график скорости, где по оси x отображается расстояние в километрах, а по оси y - скорость в километрах в час. В заголовке графика также указывается средняя скорость всего маршрута.

🌟 Наслаждайтесь изучением и анализом вашего маршрута GPX с помощью этого скрипта! 🌟
