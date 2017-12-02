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
    table->setColumnCount(28);
    label<<"Codigo"<<"Nome"<<"Sigla"<<"Município"<<"UF"<<"Região"<<"Categoria administrativa"<<"Organização Acadêmica"<<"IES da Capital";
    label<<"Acesso portal CAPES"<<"Acesso outras bases"<<"Repositório Institucional"<<"Busca Integrada"<<"Serviço de Internet"<<"Participa de rede social"<<"Catálogo Online";
    label<<"Quantidade de periodicos eletrônicos"<<"Quantidade de livros eletrônicos"<<"Valor receita própria"<<"Valor transferência"<<"Valor outra receita"<<"Valor remuneração docente"<<"Valor despesa técnico";
    label<<"Depesa pessoal encargo"<<"Valor custeio"<<"Despesa investimento"<<"Despesa pesquisa"<<"Despesa outras";
    table->setColumnWidth(0,60);
    table->setColumnWidth(1,650);
    table->setColumnWidth(2,160);
    table->setColumnWidth(3,150);
    table->setColumnWidth(4,35);
    table->setColumnWidth(6,200);
    table->setColumnWidth(7,180);
    table->setColumnWidth(9,200);
    table->setColumnWidth(10,200);
    table->setColumnWidth(11,200);
    table->setColumnWidth(12,200);
    table->setColumnWidth(13,200);
    table->setColumnWidth(14,200);
    table->setColumnWidth(15,200);
    table->setColumnWidth(16,260);
    table->setColumnWidth(17,250);
    table->setColumnWidth(18,250);
    table->setColumnWidth(19,250);
    table->setColumnWidth(20,250);
    table->setColumnWidth(21,250);
    table->setColumnWidth(22,250);
    table->setColumnWidth(23,250);
    table->setColumnWidth(24,250);
    table->setColumnWidth(25,250);
    table->setColumnWidth(26,250);
    table->setColumnWidth(27,250);
    table->setHorizontalHeaderLabels(label);
    table->verticalHeader()->setVisible(false);
    table->setMaximumWidth(TABLEWIDTH);
    table->setMinimumWidth(TABLEWIDTH);
    table->setMaximumHeight(TABLEHEIGHT);
    table->setMinimumHeight(TABLEHEIGHT);
    buscatmp=busca.toUtf8().constData();
    query="select * from IES natural join MANTENEDORA natural join CATEGORIA_ADMINISTRATIVA natural join ORGANIZACAO_ACADEMICA inner join MUNICIPIO on CO_MUNICIPIO_IES=CO_MUNICIPIO inner join UF on CO_UF_IES=CO_UF  natural join VALORES where ";
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
                    if(data[11][0]==1)
                        table->setItem(i,10,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,10,new QTableWidgetItem("Falso"));
                    if(data[12][0]=='1')
                        table->setItem(i,11,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,11,new QTableWidgetItem("Falso"));
                    if(data[13][0]=='1')
                        table->setItem(i,12,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,12,new QTableWidgetItem("Falso"));
                    if(data[14][0]=='1')
                        table->setItem(i,13,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,13,new QTableWidgetItem("Falso"));
                    if(data[15][0]=='1')
                        table->setItem(i,14,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,14,new QTableWidgetItem("Falso"));
                    if(data[16][0]=='1')
                        table->setItem(i,15,new QTableWidgetItem("Verdadeiro"));
                    else
                        table->setItem(i,15,new QTableWidgetItem("Falso"));
                    table->setItem(i,16,new QTableWidgetItem(data[17]));
                    table->setItem(i,17,new QTableWidgetItem(data[18]));
                    table->setItem(i,18, new QTableWidgetItem(data[27]));
                    table->setItem(i,19, new QTableWidgetItem(data[28]));
                    table->setItem(i,20, new QTableWidgetItem(data[29]));
                    table->setItem(i,21, new QTableWidgetItem(data[30]));
                    table->setItem(i,22, new QTableWidgetItem(data[31]));
                    table->setItem(i,23, new QTableWidgetItem(data[32]));
                    table->setItem(i,24, new QTableWidgetItem(data[33]));
                    table->setItem(i,25, new QTableWidgetItem(data[34]));
                    table->setItem(i,26, new QTableWidgetItem(data[35]));
                    table->setItem(i,27, new QTableWidgetItem(data[36]));
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
