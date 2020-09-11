#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);
    ui->graphicsView->setScene(scene);
    //ui->graphicsView->setBaseSize(671,631);
    ui->graphicsView->setFixedSize(671, 631);
    ui->graphicsView->setFixedWidth(671);
    ui->graphicsView->setRenderHint(QPainter::Antialiasing);
    ui->graphicsView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    ui->graphicsView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

    scene->setSceneRect(670, 630, 669, 629);
    // Устанавливаем границы поля scene
    QLineF topLine(scene->sceneRect().topLeft(), scene->sceneRect().topRight());
    QLineF leftLine(scene->sceneRect().topLeft(), scene->sceneRect().bottomLeft());
    QLineF rightLine(scene->sceneRect().topRight(), scene->sceneRect().bottomRight());
    QLineF bottomLine(scene->sceneRect().bottomLeft(), scene->sceneRect().bottomRight());



    this->draw();

    /*
    scene->setSceneRect(670, 630, 669, 629);
    QRectF rect = scene->sceneRect();
    rect.setWidth(669);
    rect.setHeight(629);
    scene->setSceneRect(rect);
    ui->graphicsView->updateSceneRect(scene->sceneRect());
    ui->graphicsView->setFixedSize(669,629);

    QBrush red_brush(Qt::red);
    QBrush blue_brush(Qt::blue);
    QPen black_pen(Qt::black);
    black_pen.setWidth(6);
    */
    //ellipse = scene->addEllipse(10,10,100,100, black_pen, red_brush);
    //ui->pushButton_4->clicked();
    //connect(ui->pushButton_4, SIGNAL(clicked()), this, SLOT(draw()));
}

MainWindow::~MainWindow()
{
    delete ui;
    delete scene;
}

void MainWindow::draw()
{
    qDebug() << this->triangle_x[0];
    QPen black_pen(Qt::black);
    QBrush blue_brush(Qt::blue);
    blue_brush.setStyle(Qt::FDiagPattern);
    QPolygon *triangle = new QPolygon();
    *triangle << QPoint(this->triangle_x[0], this->triangle_y[0])\
            << QPoint(this->triangle_x[1], this->triangle_y[1])\
            << QPoint(this->triangle_x[2], this->triangle_y[2]);
    //scene->addPolygon(*triangle, black_pen, blue_brush);
    scene->addPolygon(*triangle);

    QPainterPath *path = new QPainterPath();

    double x = 0;
    path->moveTo(x + this->x_circle, sqrt((1 - ((x*x) / (rx*rx))) * (ry*ry)) + this->y_circle);

    // два фора для отрисовки дуги
    for (;x < rx; x += 0.1)
    {
        double y = sqrt((1 - ((x*x) / (rx*rx))) * (ry*ry));
        path->lineTo(x + this->x_circle, y + this->y_circle);
    }

    for (;x > 0; x -= 0.1)
    {

        double y = sqrt((1 - ((x*x) / (rx*rx))) * (ry*ry));
        path->lineTo(x + this->x_circle, -y + this->y_circle);
    }

    scene->addPath(*path);
}

void MainWindow::move(double dx, double dy)
{
    scene->clear();
    for (int i = 0; i < 3; i++)
    {
        this->triangle_x_prev[i] = this->triangle_x[i];
        this->triangle_y_prev[i] = this->triangle_y[i];

        this->triangle_x[i] += dx;
        this->triangle_y[i] += dy;
    }

    this->x_circle_prev = this->x_circle;
    this->y_circle_prev = this->y_circle;

    this->x_circle += dx;
    this->y_circle += dy;

    this->draw();
}

void MainWindow::on_undo_btn_clicked()
{
    scene->clear();

    for (int i = 0; i < 3; i++)
    {
        this->triangle_x[i] = this->triangle_x_prev[i];
        this->triangle_y[i] = this->triangle_y_prev[i];
    }

    this->x_circle = this->x_circle_prev;
    this->y_circle = this->y_circle_prev;

    this->draw();
}

void MainWindow::check_point_entry()
{
    int check = 1;
    QString text;
    text = ui->x_move->text();

    qDebug() << text;
}

void MainWindow::on_pushButton_clicked()
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
        {
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля х введено не число.");
            qDebug() << "НЕ перевелось";
        }

        if (!to_float_check_y)
        {
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля y введено не число.");
            qDebug() << "НЕ перевелось";
        }

        if (to_float_check_x && to_float_check_y)
        {
            qDebug() << "перевелось ВСЁ";
            this->move(x, y);
        }
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
            qDebug() << "НЕ перевелось";
        }

        if (!to_float_check_y)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля y введено не число.");
            qDebug() << "НЕ перевелось";
        }
        if (!to_float_check_x_coef)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля коэффициента x введено не число.");
            qDebug() << "НЕ перевелось";
        }
        if (!to_float_check_y_coef)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля коэффициента y введено не число.");
            qDebug() << "НЕ перевелось";
        }

        if (check)
        {
            qDebug() << "перевелось ВСЁ";
            this->x_point_scale = x;
            this->y_point_scale = y;
            this->x_coef = x_c;
            this->y_coef = y_c;
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
            qDebug() << "НЕ перевелось";
        }

        if (!to_float_check_y)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля y введено не число.");
            qDebug() << "НЕ перевелось";
        }
        if (!to_float_check_angle)
        {
            check = 0;
            QMessageBox::warning(this, "Ошибка", "Некорректный ввод.\nДля угла введено не число.");
            qDebug() << "НЕ перевелось";
        }

        if (check)
        {
            qDebug() << "перевелось ВСЁ";
            this->angle = angle;
        }
    }
}
