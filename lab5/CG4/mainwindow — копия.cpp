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

    this->extrem_min.x = 1000;
    this->extrem_min.y = 1000;
    this->extrem_max.x = -1;
    this->extrem_max.y = -1;
    //scene->addLine(0, 0, 200, 200, *pen);

}

MainWindow::~MainWindow()
{
    free(edges);
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

    if (y < this->extrem_min.y)
    {
        this->extrem_min.y = y;
        this->extrem_min.x = x;
    }

    if (y > this->extrem_max.y)
    {
        this->extrem_max.y = y;
        this->extrem_max.x = x;
    }


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
        this->scene->addLine(this->x_array[this->ended_index], this->y_array[this->ended_index],\
            this->x_array[amount - 1], this->y_array[amount - 1], *(this->pen));

    this->x_array[amount] = -1;
    this->y_array[amount] = -1;
    this->amount++;
    this->ended_index = amount;
    this->is_ended = 1;

}

void MainWindow::mousePressEvent(QMouseEvent *event)
{
    QPoint point = event->pos();
    double x = point.x() - INDENT_X;
    double y = point.y();

    if (x >= 0 && y < 520)
    {
        this->add_point(x, y);
        this->draw_point(x, y);
        if (this->amount > 1 && !this->is_ended)
            this->last_link_points(this->amount, this->x_array, this->y_array);

        this->is_ended = 0;
        //ended = 0;
    }
}

void MainWindow::fill_edges()
{
    int index = 0;
    int i = 0;
    int fakes = 0;
    while (i < this->amount - 1)
    //for (int i = 0; i < this->amount - 1; i++)
    {
        this->edges[i-fakes].point1.x = this->x_array[i];
        this->edges[i-fakes].point1.y = this->y_array[i];
        if (this->y_array[i+1] == -1)
        {
            this->edges[i-fakes].point2.x = this->x_array[index];
            this->edges[i-fakes].point2.y = this->y_array[index];

            if ((i+1) < (this->amount - 1))
                index = i + 2;

            i++;
            fakes++;
            qDebug() << "INDEX" << index;
        }
        else
        {
            this->edges[i-fakes].point2.x = this->x_array[i + 1];
            this->edges[i-fakes].point2.y = this->y_array[i + 1];
        }
        i++;
    }
    this->edges[i-fakes].point1.x = this->x_array[amount - 1];
    this->edges[i-fakes].point1.y = this->y_array[amount - 1];
    this->edges[i-fakes].point2.x = this->x_array[index];
    this->edges[i-fakes].point2.y = this->y_array[index];

    this->amount -= fakes;
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
    zero_array(this->x_array, 100);
    zero_array(this->y_array, 100);
    this->amount = 0;
    //free(this->edges);
    //this->edges = (Edge*)malloc(100 * sizeof(Edge));
    this->is_ended = 0;
    this->ended_index = 0;
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

void MainWindow::activate_pixels()
{
    for (int x = ceil(this->x_1 - 0.5); x + 0.5 < this->x_2; x += 1)
    {
        this->scene->addLine(x, this->y_, x, this->y_, *(this->pen));
        //QThread::msleep(100);
        //Sleeper::msleep(100);
    }
}

int MainWindow::is_crossing_in_non_extremum_vertex(int y_string, Edge_active &edge)
{
    int check = 1;
    if ((round(edge.x) == this->extrem_max.x && y_string == this->extrem_max.y) ||\
            (round(edge.x) == this->extrem_min.x && y_string == this->extrem_min.y))
        check = 0;

    int is_vertex = 0;
    if (!check)
    {
        for (int i = 0; i < this->amount && !is_vertex; i++)
        {
            if (round(edge.x) == this->x_array[i] && y_string == this->y_array[i])
                is_vertex = 1;
        }
    }

    if (!is_vertex)
        check = 0;
    //if (y_string == this->extrem_max.y || y_string == this->extrem_min.y)
        //check = 0;

    return check;
}

void MainWindow::deleting_unactive_edges(int y_string, node_t** active_edges_list)
{
    node_t* temp = *active_edges_list;
    node_t* prev = NULL;
    int deleted = 0;
    while (*active_edges_list)
    {
        deleted = 0;
        if ((*active_edges_list)->edge.dy - 1 == 0)
        {
            if ((*active_edges_list) != temp)
            {
                pop_active_edge(active_edges_list);
                prev->next = *active_edges_list;
            }
            else
            {
                pop_active_edge(active_edges_list);
                temp = *active_edges_list;
            }
            deleted = 1;
        }
        else if (is_crossing_in_non_extremum_vertex(y_string, (*active_edges_list)->edge))
        {
            if ((*active_edges_list) != temp)
            {
                pop_active_edge(active_edges_list);
                prev->next = *active_edges_list;
            }
            else
            {
                pop_active_edge(active_edges_list);
                temp = *active_edges_list;
            }
            deleted = 1;
        }
        prev = *active_edges_list;
        if (!deleted)
            *active_edges_list = (*active_edges_list)->next;
    }
    *active_edges_list = temp;
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
            //x = fabs((lowest_point.x - highest_point.x) * (index - lowest_point.y) / (dy)) + ;
            qDebug() << "X " << x;
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
        qDebug() << "start fill";
        fill_x_list(&active_edges_list, &x_list);
        qDebug() << "sort";
        insertion_sort(&x_list);
        //print_list(x_list);
        qDebug() << "start drawing string";
        list* start = x_list;
        while (x_list && x_list->next)
        {
            double x1 = x_list->x;
            x_list = x_list->next;
            double x2 = x_list->x;
            x_list = x_list->next;

            for (int x = ceil(x1 - 0.5); x + 0.5 < x2; x += 1)
            {
                this->scene->addLine(x, i, x, i, *(this->pen));
            }
        }
        x_list = start;
        qDebug() << "end drawing string";
        del_unactive_edges(&(y_groups[i + 1]), &active_edges_list);
        //deleting_unactive_edges(i, &active_edges_list);
        qDebug() << "del edges";
        preparation_active_edges(&active_edges_list);
        qDebug() << "prep edges";

        free_x_list(&x_list);
    }

    free(y_groups);
}

void MainWindow::ordered_list_of_active_edges_delayed()
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
        insertion_sort(&x_list);
        while (x_list && x_list->next)
        {
            double x1 = x_list->x;
            x_list = x_list->next;
            double x2 = x_list->x;
            x_list = x_list->next;

            for (int x = ceil(x1 - 0.5); x + 0.5 < x2; x += 1)
            {
                this->scene->addLine(x, i, x, i, *(this->pen));
            }
            QEventLoop loop;
            QTimer::singleShot(100, &loop, SLOT(quit()));
            loop.exec();

        }

        del_unactive_edges(&(y_groups[i + 1]), &active_edges_list);
        preparation_active_edges(&active_edges_list);

        free_x_list(&x_list);
    }

    free(y_groups);
}

void MainWindow::on_fill_btn_clicked()
{

    qDebug() << "Extrems max" << this->extrem_max.x << this->extrem_max.y;
    qDebug() << "Extrems min" << this->extrem_min.x << this->extrem_min.y;

    for (int i = 0; i < amount; i++)
    {
        qDebug() << x_array[i];
        qDebug() << y_array[i];
    }
    qDebug() <<  "______________";
    fill_edges();
    for (int i = 0; i < amount; i++)
    {
        qDebug() << edges[i].point1.x << edges[i].point1.y;
        qDebug() << edges[i].point2.x << edges[i].point2.y;
    }

    unsigned int start = clock();
    if (ui->delay->isChecked())
        ordered_list_of_active_edges_delayed();
    else
        ordered_list_of_active_edges();

    unsigned int end = clock();
    float search_time = (float)(end - start) / CLOCKS_PER_SEC;
    QString text;
    text.setNum(search_time);
    ui->timing_text->setText(text);
}

/*
void MainWindow::delay()
{
    QEventLoop
}
*/
