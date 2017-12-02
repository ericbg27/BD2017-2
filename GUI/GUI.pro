#-------------------------------------------------
#
# Project created by QtCreator 2017-11-24T02:20:17
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

LIBS+=-I/usr/include/mysql/ -lmysqlclient

TARGET = GUI
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    iesform.cpp \
    iesresult.cpp \
    docform.cpp \
    class.cpp \
    curform.cpp \
    docresult.cpp

HEADERS  += mainwindow.h \
    iesform.h \
    iesresult.h \
    docform.h \
    class.h \
    curform.h \
    docresult.h

FORMS    += mainwindow.ui \
    iesform.ui \
    iesresult.ui \
    docform.ui \
    curform.ui \
    docresult.ui
