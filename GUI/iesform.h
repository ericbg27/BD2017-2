#ifndef IESFORM_H
#define IESFORM_H

#include <QWidget>
#include <string>
using namespace std;

namespace Ui {
class IESForm;
}

class IESForm : public QWidget
{
    Q_OBJECT

public:
    explicit IESForm(QWidget *parent = 0);
    ~IESForm();

private slots:
    void on_pushButton_released();

private:
    Ui::IESForm *ui;
};

#endif // IESFORM_H
