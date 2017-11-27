#include "iesresult.h"
#include "ui_iesresult.h"

IESResult::IESResult(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::IESResult)
{
    ui->setupUi(this);
}

IESResult::~IESResult()
{
    delete ui;
}
