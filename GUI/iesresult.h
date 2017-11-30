#ifndef IESRESULT_H
#define IESRESULT_H

#include <QWidget>
#define TABLEWIDTH 1290
#define TABLEHEIGHT 630
using namespace std;

namespace Ui {
class IESResult;
}

class IESResult : public QWidget
{
    Q_OBJECT

public:
    explicit IESResult(QWidget *parent = 0);
    IESResult(QString, int);
    ~IESResult();

private:
    Ui::IESResult *ui;
};

#endif // IESRESULT_H
