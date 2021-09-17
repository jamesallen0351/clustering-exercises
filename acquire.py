# acquire

 SELECT *
    FROM properties_2017
    LEFT OUTER JOIN airconditioningtype 
    ON airconditioningtype.airconditioningtypeid = properties_2017.airconditioningtypeid
    LEFT OUTER JOIN architecturalstyletype
    ON architecturalstyletype.architecturalstyletypeid = properties_2017.architecturalstyletypeid
    LEFT OUTER JOIN buildingclasstype 
    ON buildingclasstype.buildingclasstypeid = properties_2017.buildingclasstypeid
    LEFT OUTER JOIN heatingorsystemtype
    ON heatingorsystemtype.heatingorsystemtypeid = properties_2017.heatingorsystemtypeid
    LEFT OUTER JOIN predictions_2017
    ON predictions_2017.id = properties_2017.id
    INNER JOIN (
    SELECT id, MAX(transactiondate) as last_trans_date 
    FROM predictions_2017
    GROUP BY id
    ) predictions ON predictions.id = properties_2017.id AND predictions_2017.transactiondate = predictions.last_trans_date
    LEFT OUTER JOIN propertylandusetype
    ON propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid
    LEFT OUTER JOIN storytype
    ON storytype.storytypeid = properties_2017.storytypeid
    LEFT OUTER JOIN typeconstructiontype
    ON typeconstructiontype.typeconstructiontypeid = properties_2017.typeconstructiontypeid
    JOIN unique_properties
    ON unique_properties.parcelid = properties_2017.parcelid
    WHERE latitude IS NOT NULL and longitude IS NOT NULL; 
