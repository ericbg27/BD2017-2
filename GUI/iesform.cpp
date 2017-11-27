#include "iesform.h"
#include "ui_iesform.h"
#include "iesresult.h"
#include "iostream"

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
    cout<<"ok"<<endl;
    IESResult *iesresult = new IESResult(ui->Busca->text());
    iesresult->show();
    this->close();
}
