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

void IESResult::run(QString busca, int opt){
    MYSQL con;
    MYSQL_RES* result;
    MYSQL_ROW data;
    string query="", buscatmp;
    QTableWidget* table = new QTableWidget(this);
    QStringList label;
    int i=0;
    mysql_init(&con);
    table->setColumnCount(20);
    label<<"Codigo"<<"Nome"<<"Sigla"<<"Município"<<"UF"<<"Região"<<"Categoria administrativa"<<"Organização Acadêmica"<<"IES da Capital";
    label<<"Acesso portal CAPES";
    table->setHorizontalHeaderLabels(label);
    table->verticalHeader()->setVisible(false);
    table->setMaximumWidth(TABLEWIDTH);
    table->setMinimumWidth(TABLEWIDTH);
    table->setMaximumHeight(TABLEHEIGHT);
    table->setMinimumHeight(TABLEHEIGHT);
    buscatmp=busca.toUtf8().constData();
    query="select * from IES natural join MANTENEDORA natural join CATEGORIA_ADMINISTRATIVA natural join ORGANIZACAO_ACADEMICA inner join MUNICIPIO on CO_MUNICIPIO_IES=CO_MUNICIPIO inner join UF on CO_UF_IES=CO_UF  where ";
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
        case 5:
            query+="NO_MUNICIPIO=\""+buscatmp+"\"";
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
                    table->setItem(i,0,new QTableWidgetItem(data[3]));
                    table->setItem(i,1, new QTableWidgetItem(data[4]));
                    table->setItem(i,2,new QTableWidgetItem(data[5]));
                    table->setItem(i,3,new QTableWidgetItem(data[24]));
                    table->setItem(i,4,new QTableWidgetItem(data[26]));
                    table->setItem(i,5,new QTableWidgetItem(data[8]));
                    table->setItem(i,6,new QTableWidgetItem(data[21]));
                    table->setItem(i,7,new QTableWidgetItem(data[22]));
                    if(data[9][0]=='1')
                        table->setItem(i,8,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,8,new QTableWidgetItem("Falso"));
                    if(data[10][0]=='1')
                        table->setItem(i,9,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,9,new QTableWidgetItem("Falso"));
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
