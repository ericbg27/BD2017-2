#include "iesresult.h"
#include "qlabel.h"
#include "ui_iesresult.h"
#include "mysql/mysql.h"
#include "iostream"

IESResult::IESResult(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::IESResult)
{
    ui->setupUi(this);
}

IESResult::IESResult(QString busca){
    ui->setupUi(this);
    MYSQL connection;
    MYSQL_RES* result;
    MYSQL_ROW data;
    string query="", buscatmp;
    int i;

    mysql_init(&connection);
    if(mysql_real_connect(&connection,"127.0.0.1","root","root", "IES_Schema",0,NULL,0)){
        cout<<"Conectado"<<endl;
        buscatmp=busca.toUtf8().constData();
        query="select * from IES where CO_IES="+buscatmp;
        if(!mysql_query(&connection,query.c_str())){
            cout<<"entrou"<<endl;
            result=mysql_store_result(&connection);
            if(result){
                while((data=mysql_fetch_row(result))!=NULL){
                    for(i=0;i<20;i++){
                        cout<<data[i]<<' ';
                    }
                    cout<<endl;
                }
            }
        }
    }
}

IESResult::~IESResult()
{
    delete ui;
}
