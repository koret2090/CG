#include "mainwindow.h"
#include "./ui_mainwindow.h"
//centre 335 315
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);
    ui->graphicsView->setScene(scene);
    //ui->graphicsView->setBaseSize(671,631);
    //ui->graphicsView->setFixedSize(671, 631);
    //ui->graphicsView->setFixedWidth(671);
    ui->graphicsView->setRenderHint(QPainter::Antialiasing);
    ui->graphicsView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    ui->graphicsView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

    scene->setSceneRect(0, 0, 670, 630);
    // Устанавливаем границы поля scene
    QLineF topLine(scene->sceneRect().topLeft(), scene->sceneRect().topRight());
    QLineF leftLine(scene->sceneRect().topLeft(), scene->sceneRect().bottomLeft());
    QLineF rightLine(scene->sceneRect().topRight(), scene->sceneRect().bottomRight());
    QLineF bottomLine(scene->sceneRect().bottomLeft(), scene->sceneRect().bottomRight());


    QPen black_pen(Qt::black);
    black_pen.setWidth(2);
    // оси
    scene->addLine(5, 5, 660, 5, black_pen);
    scene->addLine(653, 2, 660, 5, black_pen);
    scene->addLine(653, 8, 660, 5, black_pen);

    QGraphicsTextItem *text_x = new QGraphicsTextItem();
    text_x->setPos(650, 8);
    text_x->setPlainText("X");
    scene->addItem(text_x);


    scene->addLine(5, 5, 5, 620, black_pen);
    scene->addLine(8, 613, 5, 620, black_pen);
    scene->addLine(2, 613, 5, 620, black_pen);

    QGraphicsTextItem *text_y = new QGraphicsTextItem();
    text_y->setPos(8, 600);
    text_y->setPlainText("Y");
    scene->addItem(text_y);


    this->draw();
}

MainWindow::~MainWindow()
{
    delete ui;
    delete scene;
}

void MainWindow::draw()
{
    QPen black_pen(Qt::black);
    black_pen.setWidth(2);
    QBrush blue_brush(Qt::blue);
    blue_brush.setStyle(Qt::FDiagPattern);
    QPolygon *triangle = new QPolygon();
    *triangle << QPoint(this->triangle_x[0], this->triangle_y[0])\
            << QPoint(this->triangle_x[1], this->triangle_y[1])\
            << QPoint(this->triangle_x[2], this->triangle_y[2]);
    //scene->addPolygon(*triangle, black_pen, blue_brush);
    scene->addPolygon(*triangle, black_pen);


    QPainterPath *path = new QPainterPath();

    path->moveTo(this->x_arc[0], this->y_arc[0]);
    // фор для отрисовки дуги
    for (int i = 0; i < 41; i++)
        path->lineTo(this->x_arc[i], this->y_arc[i]);



    scene->addPath(*path, black_pen);

    // lines
    QPen line_pen(Qt::black);
    line_pen.setWidth(1);

    for (int i = 0; i < 10; i++)
        scene->addLine(this->x1_lines[i], this->y1_lines[i], this->x2_lines[i], this->y2_lines[i], line_pen);

    path->~QPainterPath();
}

void MainWindow::save_prev()
{
    for (int i = 0; i < 3; i++)
    {
        this->triangle_x_prev[i] = this->triangle_x[i];
        this->triangle_y_prev[i] = this->triangle_y[i];
    }

    this->x_circle_prev = this->x_circle;
    this->y_circle_prev = this->y_circle;

    for (int i = 0; i < 41; i++)
    {
        this->x_arc_prev[i] = this->x_arc[i];
        this->y_arc_prev[i] = this->y_arc[i];
    }

    for (int i = 0; i < 10; i++)
    {
        this->x1_lines_prev[i] = this->x1_lines[i];
        this->x2_lines_prev[i] = this->x2_lines[i];

        this->y1_lines_prev[i] = this->y1_lines[i];
        this->y2_lines_prev[i] = this->y2_lines[i];
    }
}


void MainWindow::move(double dx, double dy)
{
    scene->clear();
    this->save_prev();

    for (int i = 0; i < 3; i++)
    {
        this->triangle_x[i] += dx;
        this->triangle_y[i] += dy;
    }

    this->x_circle += dx;
    this->y_circle += dy;

    for (int i = 0; i < 41; i++)
    {
        this->x_arc[i] += dx;
        this->y_arc[i] += dy;
    }

    for (int i = 0; i < 10; i++)
    {
        this->x1_lines[i] += dx;
        this->x2_lines[i] += dx;

        this->y1_lines[i] += dy;
        this->y2_lines[i] += dy;
    }

    this->draw();
    this->undo = 0;
}

void MainWindow::on_move_btn_clicked()
{
    bool check = 1;
    QString text_x;
    text_x = ui->x_move->text();

    QString text_y;
    text_y = ui->y_move->text();

    if (text_x.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели координату x.");

    }
    if (text_y.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели координату y.");

    }
    if (check)
    {
        bool to_float_check_x = 0;
        double x = 0;
        x = text_x.toFloat(&to_float_check_x);

        bool to_float_check_y = 0;
        double y = 0;
        y = text_y.toFloat(&to_float_check_y);

        if (!to_float_check_x)
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля х введено не число.");

        if (!to_float_check_y)
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля y введено не число.");


        if (to_float_check_x && to_float_check_y)
            this->move(x, y);
    }
}

void MainWindow::scale(double x_point, double y_point, double kx, double ky)
{
    scene->clear();
    this->save_prev();

    for (int i = 0; i < 3; i++)
    {
        this->triangle_x[i] = kx * this->triangle_x[i] + (1 - kx) * x_point;
        this->triangle_y[i] = ky * this->triangle_y[i] + (1 - ky) * y_point;
    }

    this->x_circle = kx * this->x_circle + (1 - kx) * x_point;
    this->y_circle = ky * this->y_circle + (1 - ky) * y_point;

    for (int i = 0; i < 41; i++)
    {
        this->x_arc[i] = kx * this->x_arc[i] + (1 - kx) * x_point;
        this->y_arc[i] = ky * this->y_arc[i] + (1 - ky) * y_point;;
    }

    for (int i = 0; i < 10; i++)
    {
        this->x1_lines[i] = kx * this->x1_lines[i] + (1 - kx) * x_point;
        this->x2_lines[i] = kx * this->x2_lines[i] + (1 - kx) * x_point;

        this->y1_lines[i] = ky * this->y1_lines[i] + (1 - ky) * y_point;
        this->y2_lines[i] = ky * this->y2_lines[i] + (1 - ky) * y_point;
    }

    this->draw();
    this->undo = 0;
}

double MainWindow::radians(double degrees)
{
    return degrees * 3.1415 / 180;
}

double MainWindow::rotate_convert_x(double x, double y, double x_point, double y_point, double angle)
{
    return x_point + (x - x_point) * cos(this->radians(angle))\
            + (y - y_point) * sin(this->radians(angle));
}

double MainWindow::rotate_convert_y(double x, double y, double x_point, double y_point, double angle)
{
    return  y_point - (x - x_point) * sin(this->radians(angle))\
            + (y - y_point) * cos(this->radians(angle));
}

void MainWindow::rotate(double x_point, double y_point, double angle)
{
    scene->clear();
    this->save_prev();

    double x = 0;
    double y = 0;

    for (int i = 0; i < 3; i++)
    {
        x = this->triangle_x[i];
        y = this->triangle_y[i];

        this->triangle_x[i] = this->rotate_convert_x(x, y, x_point, y_point, angle);
        this->triangle_y[i] = this->rotate_convert_y(x, y, x_point, y_point, angle);

    }

    x = this->x_circle;
    y = this->y_circle;

    this->x_circle = this->rotate_convert_x(x, y, x_point, y_point, angle);
    this->y_circle = this->rotate_convert_y(x, y, x_point, y_point, angle);
    for (int i = 0; i < 41; i++)
    {
        x = this->x_arc[i];
        y = this->y_arc[i];

        this->x_arc[i] = this->rotate_convert_x(x, y, x_point, y_point, angle);
        this->y_arc[i] = this->rotate_convert_y(x, y, x_point, y_point, angle);
    }
    for (int i = 0; i < 10; i++)
    {
        x = this->x1_lines[i];
        y = this->y1_lines[i];

        this->x1_lines[i] = this->rotate_convert_x(x, y, x_point, y_point, angle);
        this->y1_lines[i] = this->rotate_convert_y(x, y, x_point, y_point, angle);

        x = this->x2_lines[i];
        y = this->y2_lines[i];

        this->x2_lines[i] = this->rotate_convert_x(x, y, x_point, y_point, angle);
        this->y2_lines[i] = this->rotate_convert_y(x, y, x_point, y_point, angle);

    }

    this->draw();
    this->undo = 0;
}


void MainWindow::on_undo_btn_clicked()
{
    if (this->undo)
        QMessageBox::information(this, "Ошибка", "Последнее действие уже отменено.");
    else
    {
        scene->clear();

        for (int i = 0; i < 3; i++)
        {
            this->triangle_x[i] = this->triangle_x_prev[i];
            this->triangle_y[i] = this->triangle_y_prev[i];
        }

        this->x_circle = this->x_circle_prev;
        this->y_circle = this->y_circle_prev;

        for (int i = 0; i < 41; i++)
        {
            this->x_arc[i] = this->x_arc_prev[i];
            this->y_arc[i] = this->y_arc_prev[i];
        }

        for (int i = 0; i < 10; i++)
        {
            this->x1_lines[i] = this->x1_lines_prev[i];
            this->x2_lines[i] = this->x2_lines_prev[i];

            this->y1_lines[i] = this->y1_lines_prev[i];
            this->y2_lines[i] = this->y2_lines_prev[i];
        }

        this->draw();
        this->undo = 1;
    }
}

void MainWindow::on_scale_btn_clicked()
{
    bool check = 1;
    QString text_x;
    text_x = ui->x_scale->text();

    QString text_y;
    text_y = ui->y_scale->text();

    QString text_x_coef;
    text_x_coef = ui->x_coef->text();

    QString text_y_coef;
    text_y_coef = ui->y_coef->text();

    if (text_x.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели координату x.");

    }
    if (text_y.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели координату y.");

    }
    if (text_x_coef.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели коэффициент масштабирования по x.");

    }
    if (text_y_coef.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели коэффициент масштабирования по y.");

    }
    if (check)
    {
        bool to_float_check_x = 0;
        double x = 0;
        x = text_x.toFloat(&to_float_check_x);

        bool to_float_check_y = 0;
        double y = 0;
        y = text_y.toFloat(&to_float_check_y);

        bool to_float_check_x_coef = 0;
        double x_c = 0;
        x_c = text_x_coef.toFloat(&to_float_check_x_coef);

        bool to_float_check_y_coef = 0;
        double y_c = 0;
        y_c = text_y_coef.toFloat(&to_float_check_y_coef);

        if (!to_float_check_x)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля х введено не число.");
        }

        if (!to_float_check_y)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля y введено не число.");
        }
        if (!to_float_check_x_coef)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля коэффициента x введено не число.");
        }
        if (!to_float_check_y_coef)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля коэффициента y введено не число.");
        }

        if (check)
        {
            if (x_c == 0 || y_c == 0)
                 QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nКоэффициент не должен быть равен 0.");
            else
                this->scale(x,y, x_c, y_c);
        }
    }
}

void MainWindow::on_rotate_btn_clicked()
{
    bool check = 1;
    QString text_x;
    text_x = ui->x_rotate->text();

    QString text_y;
    text_y = ui->y_rotate->text();

    QString text_angle;
    text_angle = ui->angle->text();

    if (text_x.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели координату x.");

    }
    if (text_y.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели координату y.");

    }
    if (text_angle.isEmpty())
    {
        check = 0;
        QMessageBox::warning(this, "Ошибка", "Некорректный ввод!\nВы не ввели угол.");

    }

    if (check)
    {
        bool to_float_check_x = 0;
        double x = 0;
        x = text_x.toFloat(&to_float_check_x);

        bool to_float_check_y = 0;
        double y = 0;
        y = text_y.toFloat(&to_float_check_y);

        bool to_float_check_angle = 0;
        double angle = 0;
        angle = text_angle.toFloat(&to_float_check_angle);


        if (!to_float_check_x)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля х введено не число.");
        }

        if (!to_float_check_y)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля y введено не число.");
        }
        if (!to_float_check_angle)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля угла введено не число.");
        }

        if (check)
            this->rotate(x, y, angle);
    }
}

void MainWindow::on_start_btn_clicked()
{
    scene->clear();

    for (int i = 0; i < 3; i++)
    {
        this->triangle_x[i] = this->triangle_x_start[i];
        this->triangle_y[i] = this->triangle_y_start[i];
    }

    this->x_circle = this->x_circle_start;
    this->y_circle = this->y_circle_start;

    for (int i = 0; i < 41; i++)
    {
        this->x_arc[i] = this->x_arc_start[i];
        this->y_arc[i] = this->y_arc_start[i];
    }


    for (int i = 0; i < 10; i++)
    {
        this->x1_lines[i] = this->x1_lines_start[i];
        this->x2_lines[i] = this->x2_lines_start[i];

        this->y1_lines[i] = this->y1_lines_start[i];
        this->y2_lines[i] = this->y2_lines_start[i];
    }

    this->draw();
}



void MainWindow::on_pushButton_clicked()
{
    ui->textEdit->setText("ILIYA");
}
