#ifndef DOCFORM_H
#define DOCFORM_H

#include <QWidget>

namespace Ui {
class DOCForm;
}

class DOCForm : public QWidget
{
    Q_OBJECT

public:
    explicit DOCForm(QWidget *parent = 0);
    ~DOCForm();

private slots:
    void on_BuscaButton_released();

private:
    Ui::DOCForm *ui;
};

#endif // DOCFORM_H
