#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_IESButton_released();

    void on_DOCButton_released();

    void on_CURButton_released();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
