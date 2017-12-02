#include "docform.h"
#include "ui_docform.h"
#include "docresult.h"

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

void DOCForm::on_BuscaButton_released()
{
    int opt=0;
    if(ui->CodRadio->isChecked()){
        opt=1;
    }else if(ui->IESRadio->isChecked()){
        opt=2;
    }else if(ui->AnoRadio->isChecked()){
        opt=3;
    }else if(ui->UFRadio->isChecked()){
        opt=4;
    }else if(ui->MunRadio->isChecked()){
        opt=5;
    }else if(ui->EscRadio->isChecked()){
        opt=6;
    }else if(ui->SexoRadio->isChecked()){
        opt=7;
    }
    if(opt){
        DOCResult * docresult = new DOCResult();
        docresult->showMaximized();
        docresult->run(ui->Busca->text(),opt);
        this->close();
    }
}
