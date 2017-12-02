#ifndef DOCRESULT_H
#define DOCRESULT_H

#include <QWidget>
#include "QTableWidget"
#include "mysql/mysql.h"
#include "string"
#include "iostream"
#define TABLEWIDTH 1290
#define TABLEHEIGHT 630

using namespace std;

namespace Ui {
class DOCResult;
}

class DOCResult : public QWidget
{
    Q_OBJECT

public:
    explicit DOCResult(QWidget *parent = 0);
    void run(QString,int);
    ~DOCResult();

private:
    Ui::DOCResult *ui;
};

#endif // DOCRESULT_H
