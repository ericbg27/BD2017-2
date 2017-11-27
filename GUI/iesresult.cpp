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

IESResult::IESResult(QString busca){
    ui->setupUi(this);
    MYSQL con;
    MYSQL_RES* result;
    MYSQL_ROW data;
    string query="", buscatmp;
    QWidget *wid = new QWidget(this);
    QGridLayout *grid = new QGridLayout;
    QLabel* colabel = new QLabel(this);
    QLabel* nolabel = new QLabel(this);
    QLabel* sgllabel = new QLabel(this);
    int i=0;
    mysql_init(&con);
    if(mysql_real_connect(&con,"127.0.0.1","root","root","IES_Schema",0,NULL,0)){
        cout<<"Conectado"<<endl;
        buscatmp=busca.toUtf8().constData();
        query="select * from IES where CO_IES="+buscatmp;
        if(!mysql_query(&con,query.c_str())){
            result=mysql_store_result(&con);
            if(result){
                while((data=mysql_fetch_row(result))!=NULL){
                   colabel->setText(data[0]);
                   grid->addWidget(colabel,i,0);
                   nolabel->setText(data[1]);
                   grid->addWidget(nolabel,i,1);
                   sgllabel->setText(data[2]);
                   grid->addWidget(sgllabel,i,2);
                   i++;
                }
                wid->setLayout(grid);
            }
        }
    }
    mysql_close(&con);
}

IESResult::~IESResult()
{
    delete ui;
}
