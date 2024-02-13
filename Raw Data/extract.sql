--Extract Heart Rate
SELECT * FROM chartevents_3 WHERE itemid = 211;

--Extract Respiratory Rate
SELECT * FROM chartevents WHERE itemid = 618;

--Extract White Blood Cell Count
SELECT * FROM chartevents WHERE itemid IN (1127, 861, 4200, 1542)

--Extract Temperature
SELECT * FROM chartevents WHERE itemid = 676;
