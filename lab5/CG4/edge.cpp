#include "edge.h"
#include <stdlib.h>

Point get_highest_point(Edge edge)
{
    if (edge.point1.y > edge.point2.y)
        return edge.point1;

    return edge.point2;
}

Point get_lowest_point(Edge edge)
{
    if (edge.point1.y < edge.point2.y)
        return edge.point1;

    return edge.point2;
}

Point get_left_point(Edge edge)
{
    if (edge.point1.x < edge.point2.x)
        return edge.point1;

    return edge.point2;
}

Point get_right_point(Edge edge)
{
    if (edge.point1.x > edge.point2.x)
        return edge.point1;

    return edge.point2;
}

Edge make_edge(double x1, double y1, double x2, double y2)
{
    Point point1;
    point1.x = x1;
    point1.y = y1;

    Point point2;
    point1.x = x2;
    point2.y = y2;

    Edge edge;
    edge.point1 = point1;
    edge.point2 = point2;

    return  edge;
}

Edge_active make_active_edge(double x, double dx, int dy)
{
    Edge_active edge;
    edge.x = x;
    edge.dx = dx;
    edge.dy = dy;

    return edge;
}




