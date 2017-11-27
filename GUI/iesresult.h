#ifndef IESRESULT_H
#define IESRESULT_H

#include <QWidget>

namespace Ui {
class IESResult;
}

class IESResult : public QWidget
{
    Q_OBJECT

public:
    explicit IESResult(QWidget *parent = 0);
    ~IESResult();

private:
    Ui::IESResult *ui;
};

#endif // IESRESULT_H
