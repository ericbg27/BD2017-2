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
    int cod=0;
    cout<<"ok"<<endl;
    if(ui->CodRadio->isChecked()){
        cod=1;
    }
    else if(ui->NomeRadio->isChecked()){
        cod=2;
    }
    else if(ui->RegRadio->isChecked()){
        cod=3;
    }
    else if(ui->SigRadio->isChecked()){
        cod=4;
    }
    else if(ui->MunRadio->isChecked()){
        cod=5;
    }
    if(cod){
     IESResult *iesresult = new IESResult();
     iesresult->run(ui->Busca->text(), cod);
     iesresult->showMaximized();
     this->close();
    }
}
