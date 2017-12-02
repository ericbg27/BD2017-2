#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "iesform.h"
#include "docform.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_IESButton_released()
{
    IESForm *iesform = new IESForm();
    iesform->show();
    this->close();
}

void MainWindow::on_DOCButton_released()
{
    DOCForm *docform = new DOCForm();
    docform->show();
    this->close();
}
