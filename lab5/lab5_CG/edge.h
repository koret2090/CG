#ifndef EDGE_H
#define EDGE_H

struct Active_edge
{
    double x;
    double y;
    double dx;
    double dy;
};


struct Point
{
    double x;
    double y;
};

struct Edge
{
    Point point1;
    Point point2;
};

struct Edge_active
{
    double x;
    double y;
    int dy;
    double dx;
};

Point get_highest_point(Edge edge);
Point get_lowest_point(Edge edge);
Edge make_edge(double x1, double y1, double x2, double y2);
Edge_active make_active_edge(double x, double y, double dx, int dy);

#endif // EDGE_H

/*Для каждого ребра создадим структуру данных:
у=int(y1+1) – начальная точка ребра по у координате,
х0- х координата точки пересечения ребра с наивысшей сканирующей строкой.
dx–смещение по x при движении вдоль ребра, соответствующее увеличению y-координаты на 1,
dy-число пересекаемых ребром строк.

Ребро многоугольника заносится в соответствующую y-группу.

OR drugoe explanation

Для каждого ребра создадим структуру данных: y x0 dy dx

y - Начальная точка ребра по Y координате

x0 – x координата точки пересечения ребра со сканирующей строкой(крайняя левая точка)

dy – число пересекаемых ребром строк

dx – смещение по X

*/
