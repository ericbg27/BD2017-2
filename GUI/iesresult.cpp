#include "iesresult.h"
#include "QLabel"
#include "QGridLayout"
#include "QList"
#include "QTableWidget"
#include "ui_iesresult.h"
#include "mysql/mysql.h"
#include "iostream"
#include "QVector"
#include "string"
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
    QTableWidget* table = new QTableWidget(this);
    QStringList label;
    int i=0;
    mysql_init(&con);
    table->setColumnCount(20);
    label<<"Codigo"<<"Nome"<<"Sigla"<<"Região";
    table->setHorizontalHeaderLabels(label);
    table->verticalHeader()->setVisible(false);
    table->setMaximumWidth(TABLEWIDTH);
    table->setMinimumWidth(TABLEWIDTH);
    table->setMaximumHeight(TABLEHEIGHT);
    table->setMinimumHeight(TABLEHEIGHT);
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
                    table->setRowCount(i+1);
                    cout<<"Conectado"<<endl;
                    table->setItem(i,0,new QTableWidgetItem(data[0]));
                    table->setItem(i,1, new QTableWidgetItem(data[1]));
                    table->setItem(i,2,new QTableWidgetItem(data[2]));
                    table->setItem(i,3,new QTableWidgetItem(data[8]));
                    i++;
                }
            }
        }
    }
    mysql_close(&con);
}

IESResult::~IESResult()
{
    delete ui;
}
