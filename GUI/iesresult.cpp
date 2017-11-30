#include "iesresult.h"
#include "QLabel"
#include "QGridLayout"
#include "QList"
#include "ui_iesresult.h"
#include "mysql/mysql.h"
#include "iostream"
#include "QVector"
using namespace std;

IESResult::IESResult(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::IESResult)
{
    ui->setupUi(this);
}

IESResult::IESResult(QString busca, int opt){
    ui->setupUi(this);
    MYSQL con;
    MYSQL_RES* result;
    MYSQL_ROW data;
    string query="", buscatmp;
    QGridLayout *grid = new QGridLayout;
    QLabel* colabel = new QLabel(this);
    QLabel* nolabel = new QLabel(this);
    QLabel* sgllabel = new QLabel(this);
    QLabel* reglabel = new QLabel(this);
    int i=0;
    mysql_init(&con);
    buscatmp=busca.toUtf8().constData();
    query="select * from IES where ";
    switch(opt){
        case 1:
            query+="CO_IES="+buscatmp;
            break;
        case 2:
            query+="NO_IES=\""+buscatmp+"\"";
            break;
        case 3:
            query+="NO_REGIAO_IES=\""+buscatmp+"\"";
            break;
        case 4:
            query+="SGL_IES=\""+buscatmp+"\"";
            break;
        default:
            break;
    }
    cout<<query<<endl;
    if(mysql_real_connect(&con,"127.0.0.1","root","root","IES_Schema",0,NULL,0)){
        if(!mysql_query(&con,query.c_str())){
            result=mysql_store_result(&con);
            if(result){
                while((data=mysql_fetch_row(result))!=NULL){
                   cout<<"Conectado"<<endl;
                   colabel->setText(data[0]);
                   grid->addWidget(colabel,i,0);
                   nolabel->setText(data[1]);
                   grid->addWidget(nolabel,i,1);
                   sgllabel->setText(data[2]);
                   grid->addWidget(sgllabel,i,2);
                   reglabel->setText(data[3]);
                   grid->addWidget(reglabel,i,3);
                   i++;
                }
                this->setLayout(grid);
            }
        }
    }
    mysql_close(&con);
}

IESResult::~IESResult()
{
    delete ui;
}
