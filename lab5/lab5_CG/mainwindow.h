#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtCore>
#include <QtGui>
#include <QGraphicsView>
#include <QGraphicsScene>
#include <iostream>
#include <QDebug>
#include <QMessageBox>
#include <math.h>
#include <QGraphicsTextItem>
#include <QPushButton>
#include <QGraphicsView>
#include <QColor>
#include <QPen>
#include <QPainter>
#include <QtWidgets>

#include "lists.h"
#include "edge.h"


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

public:
    Edge* edges;
    node_t* active_edges_list = NULL;

private:
    Ui::MainWindow *ui;
    QGraphicsScene *scene;
    QPen *pen;

    double x_array[100];
    double y_array[100];

    int amount = 0;

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
    void ordered_list_of_active_edges();

    void zero_array(double* array, int amount);
    void mousePressEvent(QMouseEvent *event);

};
#endif // MAINWINDOW_H
