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
    void save_prev();
    void move(double dx, double dy);
    void scale(double x_point, double y_point, double kx, double ky);
    void rotate(double x_point, double y_point, double angle);
    void draw();

    void on_undo_btn_clicked();

    void on_scale_btn_clicked();

    void on_rotate_btn_clicked();

    double radians(double degrees);

    double rotate_convert_x(double x, double y, double x_point, double y_point, double angle);
    double rotate_convert_y(double x, double y, double x_point, double y_point, double angle);

    void on_start_btn_clicked();

    void on_move_btn_clicked();

    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;
    double triangle_x[3] = {280, 380, 380};
    double triangle_y[3] = {310, 280, 340};

    double triangle_x_prev[3] = {280, 380, 380};
    double triangle_y_prev[3] = {310, 280, 340};

    double triangle_x_start[3] = {280, 380, 380};
    double triangle_y_start[3] = {310, 280, 340};

    double x_circle = 380;
    double y_circle = 310;

    double x_circle_start = 380;
    double y_circle_start = 310;

    double x_circle_prev = 380;
    double y_circle_prev = 310;

    double x_arc[41] = {380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390,\
                      391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 399, 398,\
                       397, 396, 395, 394, 393, 392, 391, 390, 389, 388, 387, 386,\
                       385, 384, 383, 382, 381, 380};
    double y_arc[41] = {340, 339.962, 339.85, 339.661, 339.394, 339.047, 338.618, 338.102,\
                         337.495, 336.791, 335.981, 335.055, 334, 332.798, 331.424, 329.843,\
                         328, 325.803, 323.077, 319.367, 310, 300.633, 296.923, 294.197,\
                         292, 290.157, 288.576, 287.202, 286, 284.945, 284.019, 283.209,\
                         282.505, 281.898, 281.382, 280.953, 280.606, 280.339, 280.15, 280.038, 280};

    double x_arc_prev[41] = {380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390,\
                      391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 399, 398,\
                       397, 396, 395, 394, 393, 392, 391, 390, 389, 388, 387, 386,\
                       385, 384, 383, 382, 381, 380};
    double y_arc_prev[41] = {340, 339.962, 339.85, 339.661, 339.394, 339.047, 338.618, 338.102,\
                             337.495, 336.791, 335.981, 335.055, 334, 332.798, 331.424, 329.843,\
                             328, 325.803, 323.077, 319.367, 310, 300.633, 296.923, 294.197,\
                             292, 290.157, 288.576, 287.202, 286, 284.945, 284.019, 283.209,\
                             282.505, 281.898, 281.382, 280.953, 280.606, 280.339, 280.15, 280.038, 280};
    double x_arc_start[41] = {380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390,\
                      391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 399, 398,\
                       397, 396, 395, 394, 393, 392, 391, 390, 389, 388, 387, 386,\
                       385, 384, 383, 382, 381, 380};
    double y_arc_start[41] = {340, 339.962, 339.85, 339.661, 339.394, 339.047, 338.618, 338.102,\
                             337.495, 336.791, 335.981, 335.055, 334, 332.798, 331.424, 329.843,\
                             328, 325.803, 323.077, 319.367, 310, 300.633, 296.923, 294.197,\
                             292, 290.157, 288.576, 287.202, 286, 284.945, 284.019, 283.209,\
                             282.505, 281.898, 281.382, 280.953, 280.606, 280.339, 280.15, 280.038, 280};

    double x1_lines[10] = {300, 310, 320, 330, 340, 350, 360, 370, 380, 388};
    double x2_lines[10] = {310, 320, 330, 340, 350, 360, 370, 380, 390, 398};


    double y1_lines[10] = {304, 301, 298, 295, 292, 289, 286, 283, 280, 282.505};
    double y2_lines[10] = {319, 322, 325, 328, 331, 334, 337, 340, 335.981, 323.077};

    double y1_lines_prev[10] = {304, 301, 298, 295, 292, 289, 286, 283, 280, 282.505};
    double y2_lines_prev[10] = {319, 322, 325, 328, 331, 334, 337, 340, 335.981, 323.077};

    double y1_lines_start[10] = {304, 301, 298, 295, 292, 289, 286, 283, 280, 282.505};
    double y2_lines_start[10] = {319, 322, 325, 328, 331, 334, 337, 340, 335.981, 323.077};

    double x1_lines_prev[10] = {300, 310, 320, 330, 340, 350, 360, 370, 380, 388};
    double x2_lines_prev[10] = {310, 320, 330, 340, 350, 360, 370, 380, 390, 398};

    double x1_lines_start[10] = {300, 310, 320, 330, 340, 350, 360, 370, 380, 388};
    double x2_lines_start[10] = {310, 320, 330, 340, 350, 360, 370, 380, 390, 398};

    bool undo = 0;

    QGraphicsScene *scene;
};
#endif // MAINWINDOW_H
