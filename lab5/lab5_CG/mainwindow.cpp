#include "mainwindow.h"
#include "./ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    *pen = QPen(Qt::black);
    scene = new QGraphicsScene(this);
    ui->graphicsView->setScene(scene);
   //ui->graphicsView->setBaseSize(671,631);
   //ui->graphicsView->setFixedSize(671, 631);
   //ui->graphicsView->setFixedWidth(671);
    ui->graphicsView->setRenderHint(QPainter::Antialiasing);
    ui->graphicsView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    ui->graphicsView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

    this->edges = (Edge*)malloc(100 * sizeof(Edge));
    scene->setSceneRect(0, 0, WIDTH, HEIGHT);


    //scene->addLine(0, 0, 200, 200, *pen);

}

MainWindow::~MainWindow()
{
    //free(edges);
    delete scene;
    delete ui;
}

void MainWindow::colour_bg_white()
{
    this->scene->setBackgroundBrush(Qt::white);
}

void MainWindow::colour_bg_blue()
{
    this->scene->setBackgroundBrush(Qt::blue);
}

void MainWindow::colour_bg_red()
{
    this->scene->setBackgroundBrush(Qt::red);
}

void MainWindow::colour_bg_green()
{
    this->scene->setBackgroundBrush(Qt::green);
}

void MainWindow::colour_bg_black()
{
    this->scene->setBackgroundBrush(Qt::black);
}

void MainWindow::colour_line_black()
{
    this->pen->setColor(Qt::black);
}

void MainWindow::colour_line_blue()
{
    this->pen->setColor(Qt::blue);
}

void MainWindow::colour_line_red()
{
    this->pen->setColor(Qt::red);
}

void MainWindow::colour_line_green()
{
    this->pen->setColor(Qt::green);
}

void MainWindow::colour_line_white()
{
    this->pen->setColor(Qt::white);
}

void MainWindow::draw_point(double x, double y)
{
    this->scene->addLine(x, y, x, y, *pen);
}

void MainWindow::add_point(double x, double y)
{
    x_array[amount] = x;
    y_array[amount] = y;
    amount++;

    QString text;
    QString var;
    text.append('(');

    var.setNum(x);
    text.append(var);
    text.append(',');

    var.setNum(y);
    text.append(var);
    text.append(')');

    this->ui->points_table->append(text);
}

void MainWindow::add_point_table()
{
    double x = this->ui->x_point_box->value();
    double y = this->ui->y_point_box->value();
    this->add_point(x, y);
    this->draw_point(x, y);

    if (this->amount > 1)
    {
        this->last_link_points(this->amount, this->x_array, this->y_array);
    }
}

void MainWindow::last_link_points(int amount, double *x_points, double *y_points)
{
    this->scene->addLine(x_points[amount - 2], y_points[amount - 2],\
            x_points[amount - 1], y_points[amount - 1], *(this->pen));
}

void MainWindow::end_rectangle()
{
    if (this->amount > 1)
        this->scene->addLine(this->x_array[0], this->y_array[0],\
            this->x_array[amount - 1], this->y_array[amount - 1], *(this->pen));
}

void MainWindow::mousePressEvent(QMouseEvent *event)
{
    QPoint point = event->pos();
    double x = point.x() - INDENT_X;
    double y = point.y();

    if (x >= 0)
    {
        this->add_point(x, y);
        this->draw_point(x, y);
        if (this->amount > 1)
            this->last_link_points(this->amount, this->x_array, this->y_array);
    }
}

void MainWindow::fill_edges()
{
    for (int i = 0; i < this->amount - 1; i++)
    {
        this->edges[i].point1.x = this->x_array[i];
        this->edges[i].point1.y = this->y_array[i];
        this->edges[i].point2.x = this->x_array[i + 1];
        this->edges[i].point2.y = this->y_array[i + 1];
    }
    this->edges[amount - 1].point1.x = this->x_array[amount - 1];
    this->edges[amount - 1].point1.y = this->y_array[amount - 1];
    this->edges[amount - 1].point2.x = this->x_array[0];
    this->edges[amount - 1].point2.y = this->y_array[0];
}

void MainWindow::on_make_bg_white_clicked()
{
    this->scene->setBackgroundBrush(Qt::white);
}


void MainWindow::on_make_bg_blue_clicked()
{
    this->colour_bg_blue();
}

void MainWindow::on_make_bg_red_clicked()
{
    this->colour_bg_red();
}

void MainWindow::on_make_bg_green_clicked()
{
    this->colour_bg_green();
}

void MainWindow::on_make_bg_black_clicked()
{
    this->colour_bg_black();
}

void MainWindow::on_make_line_black_clicked()
{
    this->colour_line_black();
}

void MainWindow::on_make_line_blue_clicked()
{
    this->colour_line_blue();
}

void MainWindow::on_make_line_red_clicked()
{
    this->colour_line_red();
}

void MainWindow::on_make_line_green_clicked()
{
    this->colour_line_green();
}

void MainWindow::on_make_line_white_clicked()
{
    this->colour_line_white();
}

void MainWindow::on_end_btn_clicked()
{
    this->end_rectangle();
}

void MainWindow::zero_array(double* array, int amount)
{
    for (int i = 0; i < amount; i++)
        array[i] = 0;
}

void MainWindow::on_clear_btn_clicked()
{
    this->scene->clear();
    this->ui->points_table->clear();
    zero_array(this->x_array, this->amount);
    zero_array(this->y_array, this->amount);
    this->amount = 0;
}

void MainWindow::on_add_point_btn_clicked()
{
    this->add_point_table();
}



void MainWindow::dda_draw(double x_start, double y_start, double x_end, double y_end)
{
    if ((x_start == x_end) && (y_start == y_end))
        this->draw_point(x_start, y_start);
    else
    {
        double delta_x = x_end - x_start;
        double delta_y = y_end - y_start;

        double dx = abs(delta_x);
        double dy = abs(delta_y);

        double length = dy;
        if (dx > dy)
            length = dx;

        double x = x_start;
        double y = y_start;

        delta_x = delta_x / length;
        delta_y = delta_y / length;

        int i = 1;
        while (i <= length)
        {
            this->draw_point(round(x), round(y));
            x += delta_x;
            y += delta_y;
            i++;
        }
    }

}

void MainWindow::activate_pixels_row(double x1, double x2, double y)
{
    //this->scene->addLine(x1, y, x2, y, *(this->pen));
    for (int i = x1; i < x2; i++)
    {
        if ((int(i) + 1/2) >= x1 && (int(i) + 1/2) <= x2)
            this->scene->addLine(i, y, i, y, *(this->pen));
    }
}


void MainWindow::ordered_list_of_active_edges()
{
    node_t** y_groups = (node_t**)malloc(sizeof(node_t*) * HEIGHT);

    for (int i = 0; i < HEIGHT; i++)
        y_groups[i] = NULL;

    int y_groups_amount = HEIGHT;

    /// Prepare data
    int edges_amount = this->amount;
    for (int i = 0; i < edges_amount; i++)
    {
        Point highest_point = get_highest_point(edges[i]);
        Point lowest_point = get_lowest_point(edges[i]);

        if (highest_point.y - lowest_point.y > 0)
        {
            double highest_y_row = round(highest_point.y) - 0.5; /////////////////
            int index = highest_y_row - 0.5;////////////////

            /// info for edge //////////////////
            int dy = highest_point.y - lowest_point.y;
            double dx = (lowest_point.x - highest_point.x) / dy;
            double x = highest_point.x + dx * 1 / 2;   /////////////////
            /// add edge
            Edge_active edge = make_active_edge(x, index, dx, dy);
            add_active_edge(&(y_groups[index]), edge);
        }
    }

    /// transform to rastr
    for (int i = y_groups_amount - 1; i >= 0; i--)
    {
        /// add in active_edges_list
        if (y_groups[i] != NULL)
            add_active_edges(&(y_groups[i]), &active_edges_list);

        list* x_list = NULL;

        fill_x_list(&active_edges_list, &x_list);
        //sort_x_list(&x_list);
        //sort(&x_list);
        insertion_sort(&x_list);
        print_list(&x_list);
        while (x_list && x_list->next)
        {
            double x1 = x_list->x;
            x_list = x_list->next;
            double x2 = x_list->x;
            x_list = x_list->next; /////////
            qDebug()<< "AgA";
            activate_pixels_row(x1, x2, i); // по условию x1 <= int(x) <= x2
        }
        //qDebug()<< "DIO";
        //del_unactive_edges(&active_edges_list)
        // Correct active_edges_list
        del_unactive_edges(&(y_groups[i + 1]), &active_edges_list);
        preparation_active_edges(&active_edges_list);

        free_x_list(&x_list);
    }



    free(y_groups);
}

void MainWindow::on_fill_btn_clicked()
{
    fill_edges();
    ordered_list_of_active_edges();
}

