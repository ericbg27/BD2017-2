#include "docresult.h"
#include "ui_docresult.h"

DOCResult::DOCResult(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::DOCResult)
{
    ui->setupUi(this);
}

DOCResult::~DOCResult()
{
    delete ui;
}

void DOCResult::run(QString busca, int opt){
    MYSQL con;
    MYSQL_RES* result;
    MYSQL_ROW data;
    string query="", buscatmp;
    QTableWidget* table = new QTableWidget(this);
    QStringList label;
    int i=0;
    mysql_init(&con);
    table->setColumnCount(2);
    label<<"Código"<<"IES";
    table->setHorizontalHeaderLabels(label);
    table->verticalHeader()->setVisible(false);
    table->setMaximumWidth(TABLEWIDTH);
    table->setMinimumWidth(TABLEWIDTH);
    table->setMaximumHeight(TABLEHEIGHT);
    table->setMinimumHeight(TABLEHEIGHT);
    buscatmp=busca.toUtf8().constData();
    query="select * from DOCENTE inner join NACIONALIDADE on CO_NACIONALIDADE=CO_NACIONALIDADE_DOCENTE natural join SITUACAO_DOCENTE left outer join MUNICIPIO on CO_MUNICIPIO_NASCIMENTO=CO_MUNICIPIO natural join ESCOLARIDADE_DOCENTE natural join REGIME_TRABALHO left outer join UF on CO_UF_NASCIMENTO=CO_UF inner join SEXO on IN_SEXO=IN_SEXO_DOCENTE inner join IES_DOCENTE inner join IES where ";
    switch(opt){
        case 1:
            query+="CO_DOCENTE="+buscatmp;
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
            break;
        case 6:
            query+="SGL_UF=\""+buscatmp+"\"";
            break;
        default:
            break;
    }
    cout<<query<<endl;
    if(mysql_real_connect(&con,"127.0.0.1","root","root","IES_Schema_Test",0,NULL,0)){
        if(!mysql_query(&con,query.c_str())){
            result=mysql_store_result(&con);
            if(result){
                while((data=mysql_fetch_row(result))!=NULL){
                    cout<<"ok";
                    table->setRowCount(i+1);
                    table->setItem(i,0,new QTableWidgetItem(data[3]));
                    table->setItem(i,1,new QTableWidgetItem(data[51]));
                    i++;
                }
            }
        }
    }
    mysql_close(&con);
}
