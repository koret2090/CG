import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QPixmap, QTransform
from PyQt5.QtCore import Qt, QEventLoop, QPointF
import designn

def sign(x):
    if not x:
        return 0
    return x / abs(x)


class App(QtWidgets.QMainWindow, designn.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.scene = MyScene()
        self.scene.setSceneRect(0, 0, 710, 520)
        self.graphicsView.setScene(self.scene)
        self.pen = QPen(Qt.black, 1)

        self.input_bars = False
        self.input_polygon = False
        self.polygon = []
        
        self.lines = []
        self.last_point = None
        
        self.color_in_polygon = Qt.red
        self.color_out_polygon = Qt.blue
        self.color_polygon = Qt.green
        
        self.last_edge_point = None

        self.clear_btn.clicked.connect(self.clear)
        self.adding_lines_btn.clicked.connect(self.set_bars)
        self.adding_cutter_btn.clicked.connect(self.set_polygon_bars)
        self.cut_btn.clicked.connect(self.cut)

    def clear(self):
        self.scene.clear()
        self.points_table.clear()
        self.inputBars = False
        self.inputRect = False
        self.lines = []
        self.polygon = []
        self.last_edge_point = None
        self.input_polygon = None
    
    def set_bars(self):
        if self.input_bars:
            self.input_bars = False
            self.adding_cutter_btn.setDisabled(False)
            self.clear_btn.setDisabled(False)
            self.cut_btn.setDisabled(False)
        else:
            self.input_bars = True
            self.adding_cutter_btn.setDisabled(True)
            self.clear_btn.setDisabled(True)
            self.cut_btn.setDisabled(True)

       

    def set_polygon_bars(self):
        if self.input_polygon:
            self.scene.addLine(self.polygon[len(self.polygon) - 1].x(),\
                 self.polygon[len(self.polygon) - 1].y(), self.polygon[0].x(),\
                      self.polygon[0].y(), self.pen)
            self.input_polygon = False
            self.adding_lines_btn.setDisabled(False)
            self.clear_btn.setDisabled(False)
            self.cut_btn.setDisabled(False)
        else:
            self.pen.setColor(self.color_out_polygon)
            self.input_polygon = True
            self.adding_lines_btn.setDisabled(True)
            self.clear_btn.setDisabled(True)
            self.cut_btn.setDisabled(True)


    def add_line(self, point):  #point - QpointF(x,y)
        if self.last_point == None:
            self.last_point = point
        else:
            self.lines.append([[self.last_point.x(), self.last_point.y()], \
                                                [point.x(), point.y()]])
            x = self.last_point.x()
            y = self.last_point.y()
            text = '(' + str(x) + ', ' + str(y) + ')\n' + '('\
                 + str(point.x()) + ', ' + str(point.y())  + ')\n----------------------'
            self.points_table.append(text)
            self.pen.setColor(self.color_out_polygon)
            self.scene.addLine(x, y, point.x(), point.y(), self.pen)
            self.last_point = None
    


    def add_edge(self, point):
        if self.last_edge_point == None:
            self.last_edge_point = point
            self.polygon.append(QPointF(point.x(), point.y()))
        else:
            self.pen.setColor(Qt.green)
            self.polygon.append(QPointF(point.x(), point.y()))
            x = self.last_edge_point.x()
            y = self.last_edge_point.y()
            self.scene.addLine(x, y, point.x(), point.y(), self.pen)
            self.last_edge_point = point

    def add_point(self, point):
        if self.input_bars:
            self.add_line(point)
        else:
            self.add_edge(point)


    def cut(self):
        norm = self.is_convex(self.polygon)
        if (norm and not (self.lines == [])):
            for line in self.lines:
                self.pen.setColor(Qt.red)
                self.cyrus_beck_algorithm(line, self.polygon, norm)
        elif not norm:
            QMessageBox.warning(self, "Error", "Polygon is NOT convex")
        elif self.lines == []:
            QMessageBox.warning(self, "Error", "Lines are not entered")

    def draw_line(self, point1, point2):
        self.scene.addLine(point1.x(), point1.y(), point2.x(), point2.y(), self.pen)

    def get_points(self, line):
        return QPointF(line[0][0], line[0][1]), QPointF(line[1][0], line[1][1])


    def is_convex(self, polygon):
        points = self.polygon
        
        flag = True
        
        vo = points[0]
        vi = points[1]
        vn = points[2]

        x1 = vi.x() - vo.x()
        y1 = vi.y() - vo.y()

        x2 = vn.x() - vi.x()
        y2 = vn.y() - vi.y()
        
        ordinate_sign = x1 * y2 - x2 * y1
        previous = sign(ordinate_sign)
        
        for i in range(2, len(points) - 1):
            if not flag:
                break
            vo = points[i - 1]
            vi = points[i]
            vn = points[i + 1]
            
            # векторное произведение двух векторов
            x1 = vi.x() - vo.x()
            y1 = vi.y() - vo.y()

            x2 = vn.x() - vi.x()
            y2 = vn.y() - vi.y()
            
            ordinate_sign = x1 * y2 - x2 * y1
            current = sign(ordinate_sign)
            if current != previous:
                flag = 0
            previous = current
        
        vo = points[len(points) - 1]
        vi = points[0]
        vn = points[1]
        x1 = vi.x() - vo.x()
        y1 = vi.y() - vo.y()

        x2 = vn.x() - vi.x()
        y2 = vn.y() - vi.y()
        
        ordinate_sign = x1 * y2 - x2 * y1
        current = sign(ordinate_sign)
        
        if current != previous:
            flag = 0
        
        return flag * current


    def scalar_mult(self, p1, p2):
        return p1.x() * p2.x() + p1.y() * p2.y()

    # line - отрезок, points - точки мноугольника, norm - внутр. нормаль
    def cyrus_beck_algorithm(self, line, points, norm): 
        # инициализируем пределы значений параметра, предполагая, что весь отрезок полностью видимый
        # максимизируем t нижнее и t верхнее, исходя из того что 0 <= t <= 1
        t_low = 0
        t_up = 1
        
        # концевые точки отрезка
        p1 = QPointF(line[0][0], line[0][1])
        p2 = QPointF(line[1][0], line[1][1])
        
        # вычисляем директрису(определяет направление/ориентацию отрезка) D = p2 - p1
        D = QPointF(p2.x() - p1.x(), p2.y() - p1.y())

        for i in range(len(points)):
            # весовой множитель w = p1 - точка, лежащая на i-й стороне окна
            w = QPointF(p1.x() - points[i].x(), p1.y() - points[i].y())

            # определяем нормаль
            normal = QPointF()
            if i == len(points) - 1:
                normal.setX(-norm * (points[0].y() - points[i].y()))
                normal.setY(norm * (points[0].x() - points[i].x()))
            else:
                normal.setX(-norm * (points[i + 1].y() - points[i].y()))
                normal.setY(norm * (points[i + 1].x() - points[i].x()))

            # определяем скалярные произведения
            D_scalar = self.scalar_mult(D, normal)
            w_scalar = self.scalar_mult(w, normal)
            print(D_scalar)
            if D_scalar == 0:
                # если отрезок параллелен ребру отсекателю
                if w_scalar < 0:
                    print(1)
                    # виден ли
                    return
            else:
                # отрезок невырожден, определяем t
                t = - w_scalar / D_scalar
                
                # поиск верхнего и нижнего предела t
                if D_scalar > 0:
                    # поиск нижнего предела
                    # верно ли, что t <= 1
                    if t > 1:
                        print(2)
                        return
                    else:
                        t_low = max(t_low, t)
                elif D_scalar < 0:
                    # поиск верхнего предела
                    if t < 0:
                        print(3)
                        return
                    else:
                        t_up = min(t_up, t)
            
        if t_low > t_up:
            print(4)

        # проверка фактической видимости отрезка
        if t_low <= t_up:
            self.scene.addLine(p1.x() + (p2.x() - p1.x()) * t_up,
                        p1.y() + (p2.y() - p1.y()) * t_up,
                        p1.x() + (p2.x() - p1.x()) * t_low,
                        p1.y() + (p2.y() - p1.y()) * t_low, self.pen)

class MyScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        global window
        if window.input_bars or window.input_polygon:
            window.add_point(event.scenePos())




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()  
    window.show()
    app.exec_()