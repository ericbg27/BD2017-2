#ifndef CURFORM_H
#define CURFORM_H

#include <QWidget>

namespace Ui {
class CURForm;
}

class CURForm : public QWidget
{
    Q_OBJECT

public:
    explicit CURForm(QWidget *parent = 0);
    ~CURForm();

private:
    Ui::CURForm *ui;
};

#endif // CURFORM_H
