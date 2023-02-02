from networktables import NetworkTablesInstance

nt_instanc = NetworkTablesInstance.getDefault()

nt_instanc.startClientTeam( 4930 )

fms_info = nt_instanc.getTable( "FMSInfo" )

alliance = "!!!"
station_number = -0.0

while 1 == 1:
    alliance = "Red" if fms_info.getBoolean( "IsRedAlliance", False ) else "Blue"
    station_number = fms_info.getNumber( "StationNumber", -0.0 )
    print( str( alliance ) + " " + str( station_number ) )