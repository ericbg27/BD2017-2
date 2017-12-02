#include "docform.h"
#include "ui_docform.h"

DOCForm::DOCForm(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::DOCForm)
{
    ui->setupUi(this);
}

DOCForm::~DOCForm()
{
    delete ui;
}
