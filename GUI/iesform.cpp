#include "iesform.h"
#include "ui_iesform.h"
#include "iesresult.h"

IESForm::IESForm(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::IESForm)
{
    ui->setupUi(this);
}

IESForm::~IESForm()
{
    delete ui;
}

void IESForm::on_pushButton_released()
{
    IESResult *iesresult = new IESResult;
    iesresult->show();
    this->close();
}
