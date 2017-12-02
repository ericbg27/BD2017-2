#include "curform.h"
#include "ui_curform.h"

CURForm::CURForm(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::CURForm)
{
    ui->setupUi(this);
}

CURForm::~CURForm()
{
    delete ui;
}
