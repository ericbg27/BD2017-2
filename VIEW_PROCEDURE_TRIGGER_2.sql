DELIMITER $$
CREATE PROCEDURE Conta_Docentes()
BEGIN
  SELECT 'Numero de docentes: ', COUNT(CO_DOCENTE) FROM DOCENTE;
END $$
DELIMITER;

CREATE VIEW MEDIA_TECNICOS 
AS SELECT AVG(TEC)
FROM (SELECT I.NO_IES,T.QT_TEC_TOTAL AS TEC FROM TECNICO AS T INNER JOIN IES AS I ON T.CO_IES=I.CO_IES);

CREATE TRIGGER Trigger BEFORE INSERT ON DOCENTE
FOR EACH ROW
BEGIN
IF (NEW.CO_SEXO_DOCENTE != 1 AND NEW.CO_SEXO_DOCENTE != 2) 
THEN
  SET NEW.CO_SEXO_DOCENTE = NULL;
END IF;
END;
