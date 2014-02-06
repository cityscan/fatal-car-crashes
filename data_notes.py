# ST_CASE
# unique identifier

# VEH_NO
# vehicle number assigned to each vehicle

# PER_NO
# consecutive number assigned to each person

# VEVENTNUM
# consecutive number assigned to each harmful and non-harmful event for this vehicle, in chronological order

# NHS
# 1994-later
# 0: not in NHS
# 1: in NHS

# ROAD_FNC
# if year between 1975 and 1980:
# N/A

# if year between 1981-1986:
ROAD_FNC = {
        '1': 'Principal Arterial - Interstate',
        '2': 'Principal Arterial - Other Urban Freeways and Expressways',
        '3': 'Principal Arterial - Other',
        '4': 'Minor Arterial',
        '5': 'Urban Collector',
        '6': 'Major Rural Collector',
        '7': 'Minor Rural Collector',
        '8': 'Local Road or Street',
        '9': 'Unknown'
        }

# if year 1987 or greater:
ROAD_FNC = {
        # RURAL
        '01': 'Principal Arterial - Interstate',
        '02': 'Principal Arterial - Other',
        '03': 'Minor Arterial',
        '04': 'Major Collector',
        '05': 'Minor Collector',
        '06': 'Local Road or Street',
        '09': 'Unknown',
        # URBAN
        '11': 'Principal Arterial - Interstate',
        '12': 'Principal Arterial - Other Freeways or Expressways',
        '13': 'Other Principal Arterial',
        '14': 'Minor Arterial',
        '15': 'Collector',
        '16': 'Local Road or Street',
        '19': 'Unknown',
        '99': 'Unknown'
        }

# Route signing: of trafficway on which crash occurred
# if year between 1975-1980:
CL_TWAY = {
        '1': 'Interstate',
        '2': 'Other Limited Access',
        '3': 'Other U.S. Route',
        '4': 'Other State Route',
        '5': 'Other Major Artery',
        '6': 'County Road',
        '7': 'Local Street',
        '8': 'Other Road',
        '9': 'Unknown'
        }

# not available for 1981
# if year between 1982 and 1986:
CL_TWAY = {
        '1': 'Interstate',
        '2': 'Other U.S. Route',
        '3': 'Other State Route',
        '4': 'County Road',
        '5': 'Local Street',
        '8': 'Other Road',
        '9': 'Unknown'
        }

# if year greater than 1987:
ROUTE = {
        '1': 'Interstate',
        '2': 'U.S. Highway',
        '3': 'State Highway',
        '4': 'County Road',
        '5': 'Local Street - Township',
        '6': 'Local Street - Municipality',
        '7': 'Local Street - Frontage Road (Since 1994)',
        '8': 'Other',
        '9': 'Unknown'
        }

#######
# Trafficway identifier: trafficway on which crash occurred
# 1982-Later
# TWAY_ID2 introduced in 2004
# Actual Posted Number, Assigned Number, or Common Name
# 1982-1997: 10 characters
# 1998-2011: 20 characters
# 2012-later: 30 characters

#####
# MILEPT
# 00000: None
# 99998: Not Reported
# 99999: Unknown

#####
# SP_JUR
# Special jurisdiction: may be patrolled by state, county, or local police but in a special jurisdiction
SP_JUR = {
        '0': 'No Special Jurisdiction (Includes National Forests Since 2008)',
        '1': 'National Park Service',
        '2': 'Military',
        '3': 'Indian Reservation',
        '4': 'College/University Campus',
        '5': 'Other Federal Properties (Since 1977)',
        '8': 'Other (Since 1976)',
        '9': 'Unknown'
        }

####
# First harmful event
# Applies to the crash, M_HARM (most harmful) applies to the vehicle
# judgement calls of FARS analysts
# From 2004-2009, HARM_EV, M_HARM, SE (sequence of events) have same attributes
# Starting in 2009, non-harmful event attributes were added to Sequence of Events
# This data element also apears in the Vehicle and Person data files and in Parkwork data

# if year between 1975-1981:
HARM_EV = {
        '01': 'Overturn',
        '02': 'Fire/Explosion',
        '03': 'Immersion',
        '04': 'Gas Inhalation',
        '05': 'Fell from Vehicle',
        '06': 'Injured in Vehicle',
        '07': 'Other Non-Collision',
        '08': 'Pedestrian',
        '09': 'Pedalcycle',
        '10': 'Railway Train',
        '11': 'Animal',
        '12': 'Motor Vehicle in Transport',
        '13': 'Motor Vehicle in Transport in Other Roadway',
        '14': 'Parked Motor Vehicle',
        '15': 'Other Type Non-Motorist',
        '16': 'Other Object',
        '17': 'Bridge or Overpass (1975-1978 Only)',
        '18': 'Building',
        '19': 'Culvert',
        '20': 'Curb or Wall',
        '21': 'Divider',
        '22': 'Embankment',
        '23': 'Fence',
        '24': 'Guard Rail',
        '25': 'Light Support',
        '26': 'Sign Post',
        '27': 'Three/Shrubbery'
        '28': 'Utility Pole',
        '29': 'Other Pole/Support',
        '30': 'Impact Attenuator',
        '31': 'Other Fixed Object',
        '32': 'Bridge or Overpass [Passing Under] (1979-1981 Only)',
        '33': 'Bridge or Overpass [Passing Over] (1979-1981 Only)',
        '99': 'Unknown'
        }

# if year between 1982-2003:
HARM_EV = {
        '01': 'Rollover/Overturn',
        '02': 'Fire/Explosion',
        '03': 'Immersion (or Partial Immersion, Since 2012)',
        '04': 'Gas Inhalation',
        '05': 'Fell/Jumped from Vehicle',
        '06': 'Injured in Vehicle',
        '07': 'Other Non-Collision',
        '08': 'Pedestrian',
        '09': 'Pedalcycle',
        '10': 'Railway Train',
        '11': 'Animal',
        '12': 'Motor Vehicle in Transport on Same Roadway',
        '13': 'Motor Vehicle in Transport on Other Roadway',
        '14': 'Parked Motor Vehicle (Not in Transport)',
        '15': 'Other Type Non-Motorist',
        '16': 'Thrown or Falling Object',
        '17': 'Boulder',
        '18': 'Other Object (Not Fixed)',
        '19': 'Building',
        '20': 'Impact Attentuator/Crash Cushion',
        '21': 'Bridge Pier or Abutment',
        '22': 'Bridge Parapet End',
        '23': 'Bridge Rail',
        '24': 'Guardrail Face',
        '25': 'Concrete Traffic Barrier',
        '26': 'Other Traffic Barrier',
        '27': 'Highway/Traffic Sign Post',
        '28': 'Overhead Sign Support/Sign',
        '29': 'Luminary/Light Support',
        '30': 'Utility Pole',
        '31': 'Other Post, Other Pole, or Other Support',
        '32': 'Culvert',
        '33': 'Curb',
        '34': 'Ditch',
        '35': 'Embankment - Earth',
        '36': 'Embankment - Rock, Stone or Concrete',
        '37': 'Embankment - Material Type Unknwon',
        '38': 'Fence',
        '39': 'Wall',
        '40': 'Fire Hydrant',
        '41': 'Shrubbery',
        '42': 'Tree (Standing Only)',
        '43': 'Other Fixed Object',
        '44': 'Pavement Surface Irregularity (1993 Only)',
        '45': 'Transport Device Used as Equipment (1993-2003 Only)',
        '46': 'Traffic Signal Support',
        '47': 'Vehicle Occupant Struck or Run Over by Own Vehicle (Since 1997)',
        '48': 'Collision with Snow Bank (Since 1997)',
        '49': 'Ridden Animal or Animal-Drawn Conveyance (Since 1998)',
        '50': 'Bridge Overhead Structure',
        '99': 'Unknown'
        }

# if year between 1982-1992:
HARM_EV['45'] = 'Working Construction, Maintenance or Utility Vehicles'

# if year between 2004-2009:
HARM_EV['15'] = 'Non-Motorist on Personal Conveyance'
HARM_EV['44'] = 'Pavement Surface Irregularity'
HARM_EV['51'] = 'Jackknife'
HARM_EV['52'] = 'Guardrail End'
HARM_EV['53'] = 'Mail Box'
HARM_EV['54'] = 'Motor Vehicle Struck by Falling/Shifting Cargo or Anything Set in Motion by Another Motor Vehicle in Transport'
HARM_EV['55'] = 'Other Not in-Transport Motor Vehicle (2005-2007 Only)'
HARM_EV['57'] = 'Cable Barrier (since 2008)'
HARM_EV['60'] = 'Cargo/Equipment Loss or Shift (Causing Injury or Damage)'

# if year greater than 2008:
HARM_EV['55'] = 'Motor Vehicle in Motion Outside the Trafficway'

# if year greater than 2010:
HARM_EV['06'] = 'Injured in Vehicle (Non-Collision)'
HARM_EV['09'] = 'Pedalcyclist'
HARM_EV['10'] = 'Railway Vehicle'
HARM_EV['11'] = 'Live Animal'
HARM_EV['12'] = 'Motor Vehicle in Transport'
HARM_EV['15'] = 'Non-Motorist on Personal Conveyance'
HARM_EV['21'] = 'Bridge Pier or Support'
HARM_EV['23'] = 'Bridge Rail (Includes Parapet)'
HARM_EV['30'] = 'Utility Pole/Light Support'
HARM_EV['35'] = 'Embankment'
HARM_EV['44'] = 'Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)'
HARM_EV['45'] = 'Working Motor Vehicle'
HARM_EV['48'] = 'Snow Bank'
HARM_EV['51'] = 'Jackknife (Harmful to This Vehicle)'
HARM_EV['52'] = 'Guardrail End'
HARM_EV['53'] = 'Mail Box'
HARM_EV['54'] = 'Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons, or Objects Set-in-Motion from/by Another Motor Vehicle In-Transport'
HARM_EV['55'] = 'Motor Vehicle Outside the Trafficway'
HARM_EV['57'] = 'Cable Barrier'
HARM_EV['58'] = 'Ground'
HARM_EV['59'] = 'Traffic Sign Support'
HARM_EV['72'] = 'Cargo/Equipment Loss or Shift (Harmful to This Vehicle)'
HARM_EV['98'] = 'Not Reported (2010 Only)'

####
# Manner of Collision
# Describes the orientation of two motor vehicles in-transport when they are involved in the
# "First Harmful Event of a collision crash. If the "First Harmful Event" is not a ocllision
# between two motor vehicles in-transport it is classified as such
# from 1975-1977 sideswipe was coded as 5 but since changed to 7
# This data element also appears in the Vehicle and Person data files and in the Parkwork data file as PMAN_COLL

# if year between 1975-1977:
MAN_COLL = {
        '0': 'Not Collision with Motor Vehicle in Transport',
        '1': 'Rear-End',
        '2': 'Head-On',
        '3': 'Rear-to-Rear',
        '4': 'Angle',
        '7': 'Sideswipe (May Either be Same or Opposite Direction',
        '9': 'Unknwon'
        }

# if year between 1978-2001:
MAN_COLL['5'] = 'Sideswipe, Same Direction'
MAN_COLL['6'] = 'Sideswipe, Opposite Direction'
MAN_COLL['7'].pop()

# if year between 2002-2009
MAN_COLL = {
        '00': 'Not Collision With Motor Vehicle in Transport (Not Necessarily in Transport for 2005-2009)',
        '01': 'Front-to-Rear',
        '02': 'Front-to-Front',
        '03': 'Angle - Front-to-Side, Same Direction',
        '04': 'Angle - Front-to-Side, Opposite Direction',
        '05': 'Angle - Front-to-Side, Right Angle (Includes Broadside)',
        '06': 'Angle - Front-to-Side/Angle-Direction Not Specified',
        '07': 'Sideswipe - Same Direction',
        '08': 'Sideswipe - Opposite Direction',
        '09': 'Rear-to-Side',
        '10': 'Rear-to-Rear',
        '11': 'Other (End-Swipes and Others)',
        '99': 'Unknown'
        }

# if year > 2010:
MAN_COLL['03'].pop()
MAN_COLL['04'].pop()
MAN_COLL['05'].pop()
MAN_COLL['06'] = 'Angle'
MAN_COLL['98'] = 'Not Reported'

# Relation to Junction- Within Interchange Area
# Identifies the crash's location with respect to presence in an interchange area
RELJCT1 = {
        '0': 'No',
        '1': 'Yes',
        '8': 'Not Reported',
        '9': 'Unknwon'
        }

####
# Relation to Junction-Specific Location
# identifies the crash's location with respect to presence in or proximity to components
# typically in junction or interchange areas

# if year between 1975-1990:
REL_JUNC = {
        '1': 'Non-Junction',
        '2': 'Intersection',
        '3': 'Intersection-Related',
        '4': 'Intersection Area',
        '5': 'Driveway, Alley, Access, etc.'
        '6': 'Entrance/Exit Ramp (Since 1978)',
        '7': 'Rail Grade Crossing (Since 1979)',
        '8': 'In Crossover (Since 1980)',
        '9': 'Unknown'
        }

# if year between 1991 and 2009:
# 01-09: Non-Interchange Area
# 10-99: Interchange Area
REL_JUNC = {
        '00': 'None',
        '01': 'Non-Junction',
        '02': 'Intersection',
        '03': 'Intersection-Related',
        '04': 'Driveway, Alley Access, etc.',
        '05': 'Entrance/Exit Ramp-Related',
        '06': 'Railway Grade Crossing',
        '07': 'In Crossover',
        '08': 'Driveway Access Related (Since 2003)',
        '09': 'Unknown, Non-Interchange',
        '10': 'Intersection',
        '11': 'Intersection-Related',
        '12': 'Driveway Access',
        '13': 'Entrance/Exit Ramp-Related',
        '14': 'In Crossover',
        '15': 'Other Location in Interchange',
        '19': 'Unknown, Interchange Area',
        '99': 'Unknown'
        }

# if year > 2010:
RELJCT2 = {
        '01': 'Non-Junction',
        '02': 'Intersection',
        '03': 'Intersection Related',
        '04': 'Driveway Access',
        '05': 'Entrance/Exit Ramp Related',
        '06': 'Railway Grade Crossing',
        '07': 'Crossover Related',
        '08': 'Driveway Access Related',
        '16': 'Shared-Use Path or Trail',
        '17': 'Acceleration/Deceleration Lane',
        '18': 'Through Roadway',
        '19': 'Other Location Within Interchange Area',
        '98': 'Not Reported',
        '99': 'Unknown'
        }

####
# Type of Intersection
# 2010-Later
TYP_INT = {
        '1': 'Not an Intersection',
        '2': 'Four-Way Intersection',
        '3': 'T-Intersection',
        '4': 'Y-Intersection',
        '5': 'Traffic Circle',
        '6': 'Roundabout',
        '7': 'Five-Point, or More',
        '8': 'Not Reported',
        '9': 'Unknown'
        }

####
# Relation to Trafficway
# location of crash as it relates to its position within or outside the trafficway based on the
# "First Harmful Event"
# if year between 1975-1997:
REL_ROAD = {
        '1': 'On Roadway',
        '2': 'Shoulder',
        '3': 'Median',
        '4': 'Roadside',
        '5': 'Outside Right-of-way',
        '6': 'Off Roadway - Location Unknown',
        '7': 'In Parking Lane (since 1980)',
        '8': 'Gore (Since 1982)',
        '9': 'Unknown'
        }

# if year between 1998-2009:
REL_ROAD = {
        '01': 'On Roadway',
        '02': 'On Shoulder',
        '03': 'On Median',
        '04': 'On Roadside',
        '05': 'Outside Trafficway/Outside Right-Of-Way',
        '06': 'Off Roadway - Traffic Unknown',
        '07': 'In Parking Lane/Zone',
        '08': 'Gore',
        '10': 'Separator',
        '11': 'Two-way Continuous Left-Turn Lane (Since 2001)',
        '99': 'Unknown'
        }
# if year between 1998-2006
REL_ROAD['07'] = 'In Parking Lane'

# if year > 2010:
REL_ROAD['05'] = 'Outside Trafficway'
REL_ROAD['11'] = 'Continuous Left-Turn Lane'
REL_ROAD['98'] = 'Not Reported'

####
# Work Zone: crash in which first harmful event occurs within the boundries of a work zone or 
# approach to or exit from a work zone
# if year between 1975-1979:
# all null
# if year between 1980-1981:
C_M_ZONE = {
        '0': 'None',
        '1': 'Construction',
        '2': 'Maintenance',
        '3': 'Construction or Maintenance'
        }
# if year between 1982-2008:
C_M_ZONE['3'] = 'Utility'
C_M_ZONE['4'] = 'Work Zone, Type Unknown'

# if year = 2009:
WRK_ZONE = C_M_ZONE.copy()

# if year between 2010-2011:
WRK_ZONE = {
        '0': 'None',
        '1': 'Construction',
        '2': 'Maintenance',
        '3': 'Utility',
        '4': 'Work Zone, Type Unknown',
        '8': 'Not Reported'
        }

####
# Light Condition
# if year between 1975-1979:
LGT_COND = {
        '1': 'Daylight',
        '2': 'Dark',
        '3': 'Dark but Lighted',
        '6': 'Dawn or Dusk',
        '9': 'Unknown'
        }
# if year between 1980-2008:
LGT_COND['4'] = 'Dawn'
LGT_COND['5'] = 'Dusk'

# if year = 2009:
LGT_COND['2'] = 'Dark - Not Lighted'
LGT_COND['6'] = 'Dark - Unknown Lighting'
LGT_COND['7'] = 'Other'

# if year > 2010:
LGT_COND['3'] = 'Dark - Lighted'
LGT_COND['8'] = 'Not Reported'

####
# Atmospheric Conditions
# If more than two reported (2007 and later), two that most affect visibility selected
#if year betwen 1975-1979:
WEATHER = {
        '1': 'Clear',
        '2': 'Rain',
        '3': 'Sleet',
        '4': 'Snow',
        '7': 'Cloudy',
        '9': 'Unknown'
        }

# if year between 1980-1981:
WEATHER = {
        '1': 'Normal',
        '2': 'Rain',
        '3': 'Sleet',
        '4': 'Snow',
        '5': 'Fog',
        '8': 'Other: Smog, Smoke, Blowing Sand or Dust'
        '9': 'Unknown'
        }

# if year between 1982-2006:
WEATHER = {
        '1': 'No Adverse Atmospheric Conditions',
        '2': 'Rain (Mist)',
        '3': 'Sleet (Hail)',
        '4': 'Snow',
        '5': 'Fog',
        '6': 'Rain and Fog',
        '7': 'Sleet and Fog',
        '8': 'Other: Smog, Smoke, Blowing Sand or Dust',
        '9': 'Unknown'
        }

# if year between 2007-2009
WEATHER = {
        '0': 'No Adverse Atmospheric Conditions',
        '1': 'Clear/Cloud (No Adverse Conditions)',
        '2': 'Rain (Mist)',
        '3': 'Sleet (Hail)',
        '4': 'Snow or Blowing Snow',
        '5': 'Fog, Smog, Smoke',
        '6': 'Severe Crosswinds',
        '7': 'Blowing Sand, Soil, Dirt',
        '8': 'Other',
        '9': 'Unknown'
        }

# if year > 2010:
WEATHER = {
        '01': 'Clear',
        '00': 'No Additional Atmospheric Conditions',
        '02': 'Rain',
        '03': 'Sleet, Hail (Freezing Rain or Drizzle)',
        '04': 'Snow',
        '05': 'Fog, Smog, Smoke',
        '06': 'Severe Crosswinds',
        '07': 'Blowing Sand, Soil, Dirt',
        '08': 'Other',
        '10': 'Cloudy',
        '11': 'Blowing Snow',
        '98': 'Not Reported',
        '99': 'Unknown'
        }

####
# School Bus Related
# boolean
# if > 2010, 8 = 'Not Reported'

####
# Rail Grade Crossing
RAIL = {
        '000000': 'Not Applicable',
        '999999': 'Unknwown'
        }
# xxxxxA : Six Digits followed by one Alphabetic Valid FRA code

####
# Hour of arrival at scene
# 1975-1988
ARR_HOUR = {
        '00': 'Not notified or officially cancelled (when ARR_MIN = 00)',
        '99': 'Unknown Hour'
        }

# 1999-2008
ARR_HOUR = {
        '00': 'Not Notified (when ARR_MIN = 00)',
        '99': 'Unknown Hour',
    }
# if ARR_MIN == 97
ARR_HOUR['99'] = 'Officially cancelled'

# if ARR_MIN == 98
ARR_HOUR['99'] = 'Unknown if arrived'

# 2009 or later
ARR_HOU = {
        '88': 'Not Applicable or Not Notified',
        }
# 1999-2008 conditions above also apply

####
# Arival Minute
# 1975-1998
ARR_MIN = {
        '00': 'Not Notified or Officially Cancelled (when ARR_HOUR == 00)',
        '99': 'Unknown Minutes'
        }

# 1999-2008
ARR_MIN = {
        '00': 'Not Notified (when ARR_HOUR == 00)',
        '97': 'Officially Cancelled',
        '98': 'Unknown if Arrived',
        '99': 'Unknown Minutes'
        }

# 2009 or later
ARR_MIN['88'] = 'Not Applicable or Not Notified'

###
# Hour of EMS Arrival at Hospital
# 1987-1998
HOSP_HR = {
        '00': 'Not Notified, Officially Cancelled, or Not Transported (when HOSP_MIN == 00)',
        '99': 'Unknown Hour'
        }

# 1999-2008
HOSP_HR = {
        '00': 'Not notified or Not Transported (when HOSP_MIN = 00)',
        '99': 'Unknown Hour'
        }

# if HOSP_MIN == 97:
HOSP_HR['99'] = 'Officially Cancelled'

# if HOSP_MIN == 98:
HOSP_HR['99'] = 'Unknown if Transported'

# 2009 or later
HOSP_HR['88'] = 'Not Applicable or Not Notified'
# 1999-2008 conditions above also apply

####
# Minute of EMS Arrival at Hospital
# 1987-1988
HOSP_MIN = {
        '00': 'Not Notified, Officially cancelled, or not transported (when HOSP_HR == 00)',
        '99': 'Unknown Minutes'
        }

# 1999-2008
HOSP_MIN = {
        '00': 'Not Notified or Not Transported (when HOSP_HR == 00)',
        '96': 'Terminated Transport',
        '97': 'Officially Cancelled',
        '98': 'Unknown if Transported',
        '99': 'Unknown Minutes'
        }

# 2009 or later
HOSP_MIN['88'] = 'Not Applicable or Not Notified'

####
# Related Factors- Crash Level
# Vehicle-level-related factors in the Vehicle data file and person-related factors in person file
# FARS analyst may have used any of the three data elements to code a related factor
# must test all three to ensure that selected related factor is included
# 1975-1981
# 01-08: VISION OBSCURED BY:
# 20-29: SWERVING DUE TO
# 40-51: ROADWAY FEATURES
# CF2, CF3 = 
CF1 = {
        '00': 'None',
        '01': 'Rain, Snow, Fog, Smoke, Sand, Dust (i.e., Weather Conditions)',
        '02': 'Reflected Glare, Bright Sunlight, Headlights',
        '03': 'Curve, Hill or Other Design Features (Including Traffic Signs, Embankments)',
        '04': 'Building, Billboard, etc.',
        '05': 'Trees, Crops, Vegetation',
        '06': 'Moving Vehicle (Including Load)',
        '07': 'Parked Vehicle',
        '08': 'Other Object Not Classified Above',
        '20': 'Severe Crosswind',
        '21': 'Wind From Passing Truck',
        '22': 'Slippery Surface',
        '23': 'Avoiding Debris or Objects in Road',
        '24': 'Ruts, Holes, Bumps, in Road',
        '25': 'Avoiding Animals in Road',
        '26': 'Avoiding Vehicle in Road',
        '27': 'Avoiding Phantom Vehicle',
        '28': 'Avoiding Pedestrian, Pedalcyclist, Other Non-Motorist in Road',
        '29': 'Avoiding Water, Snow, Oil Slick on Road',
        '40': 'Traffic Controls Not Functioning Properly',
        '41': 'Inadequate Warning of Exists, Lanes Narrowing, Traffic Controls, etc.',
        '42': 'Uncontrolled Intersection or Railroad Crossing',
        '43': 'Shoulder Too Low or High',
        '44': 'Shoulders Too Narrow or No Shoulders for Emergency Use',
        '47': 'Other Construction',
        '48': 'No or Obscured Pavement Markings',
        '49': 'Surface Underwater (Since 1979)',
        '50': 'Inadequate Construction or Poor Design Roadway, Bridge, etc. (Since 1979)',
        '51': 'Surface Washed Out (Caved in, Road Slippage, Since 1979)'
        '99': 'Unknown'
        }

#1982 or later
CF1 = {
        '00': 'None',
        '01': 'Inadequate Warning of Exists, Lanes Narrowing, Traffic Controls, etc',
        '02': 'Shoulder Related (Design or Condition, Since 2002)',
        '03': 'Other Maintenance or Construction-Created Condition',
        '04': 'No or Obscured Pavement Marking',
        '05': 'Surface Under Water',
        '06': 'Inadequate Construction or Poor Design or Roadway, Bridge, etc.',
        '07': 'Surface Washed Out (Caved In, Road Slippage)',
        '13': 'Aggressive Driving/Road Rage by Non-Contact Vehicle Driver (Since 2006)',
        '14': 'Motor Vehicle (In Transport 1983-2004 Only) Struck by Falling Cargo or Something That Came Loose From Something That Was Set in Motion By a Vehicle (Since 1983)',
        '15': 'Non-Occupant Struck By Falling Cargo, or Something Came Loose From or Something that Was Set in Motion By a Vehicle (Since 1983)',
        '16': 'Non-Occupant Struck Vehicle (Since 1983)',
        '17': 'Vehicle Set In Motion By Non-Driver (Since 1983)',
        '18': 'Date of Crash and Date of EMS Notification Were Not Same Day (Since 1988)',
        '19': 'Recent Previous Crash Scene Nearby (Since 1989)',
        '20': 'Police-Pursuit Involved (Since 1994)',
        '21': 'Within Designated School Zone (Since 1995)',
        '22': 'Speed Limit Is a Statutory Limit or Was Determined as This State\'s "Basic Rule" (Since 1999)',
        '23': 'Indication of a Stalled/Disabled Vehicle (Since 2008)',
        '24': 'Unstabilized Situation Began and All Harmful Events Occurred Off of the Roadway (Since 2012)',
        '25': 'Toll-Plaza Related (Since 2012)',
        '99': 'Unknown'
        }


