#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtCore>
#include <QtGui>
#include <QGraphicsView>
#include <QGraphicsScene>
#include <iostream>
#include <QDebug>
#include <math.h>
#include <QGraphicsTextItem>
#include <QPushButton>
#include <QGraphicsView>
#include <QColor>
#include <QPen>
#include <QPainter>
#include <QtWidgets>

#include <QThread>
#include <QtTest/QTest>

#include "lists.h"
#include "edge.h"

#include <ctime>

#define WIDTH 710
#define HEIGHT 520
#define INDENT_X 250

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_make_bg_white_clicked();

    void on_make_bg_blue_clicked();

    void on_make_bg_red_clicked();

    void on_make_bg_green_clicked();

    void on_make_bg_black_clicked();

    void on_make_line_black_clicked();

    void on_make_line_blue_clicked();

    void on_make_line_red_clicked();

    void on_make_line_green_clicked();

    void on_make_line_white_clicked();

    void on_end_btn_clicked();

    void on_clear_btn_clicked();

    void on_add_point_btn_clicked();

    void on_fill_btn_clicked();

    void activate_pixels();

    void ordered_list_of_active_edges();

public:
    Edge* edges;
    node_t* active_edges_list = NULL;
    node_t** y_groups = NULL;
    int is_ended = 0;
    double x_1 = 0;
    double x_2 = 0;
    double y_ = 0;
    Point extrem_min;
    Point extrem_max;

private:
    Ui::MainWindow *ui;
    QGraphicsScene *scene;
    QPen *pen;

    double x_array[100];
    double y_array[100];


    int y_groups_amount = 520;
    int amount = 0;
    int ended_index = 0;
    void fill_edges();

    void colour_bg_white();
    void colour_bg_blue();
    void colour_bg_red();
    void colour_bg_green();
    void colour_bg_black();

    void colour_line_white();
    void colour_line_blue();
    void colour_line_red();
    void colour_line_green();
    void colour_line_black();

    void draw_point(double x, double y);
    void add_point_table();
    void add_point(double x, double y);
    void last_link_points(int amount, double* x_points, double* y_points);
    void end_rectangle();

    void dda_draw(double x_start, double y_start, double x_end, double y_end);
    void activate_pixels_row(double x1, double x2, double y);
    void activate_pixel(double x, double y);
    //void ordered_list_of_active_edges();

    void zero_array(double* array, int amount);
    void mousePressEvent(QMouseEvent *event);
    void ordered_list_of_active_edges_delayed();
    //void delay(QEventLoop *event);
    int is_crossing_in_non_extremum_vertex(int y_string, Edge_active &edge);
    void deleting_unactive_edges(int y_string, node_t** active_edges_list);

};




class Sleeper : public QThread
{
public:
    static void usleep(unsigned long usecs){QThread::usleep(usecs);}
    static void msleep(unsigned long msecs){QThread::msleep(msecs);}
    static void sleep(unsigned long secs){QThread::sleep(secs);}
};
#endif // MAINWINDOW_H
