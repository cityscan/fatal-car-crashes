# ST_CASE
# VEH_NO
# these are unique identifiers for each record
# ST_CASE used to join vehicle and accident files
# ST_CASE and VEH_NO used to join Vehicle data with other vehicle-level data files and Person data file

#### Number of Occupants
# Numeric Value
# 1978-2008
OCCUPANTS = {
        '00': 'None',
        '96': '96 or More Occupants in Vehicle',
        '97': 'Unknown - Only Injured Reported',
        '99': 'Unknown'
        }

#2009-later
OCCUPANTS['98'] = 'Not Reported'

####
# Unit Type
#2005-2007
UNITTYPE = {
        '1': 'Motor Vehicle in Transport',
        '2': 'Motor Vehicle Not in Transport Within the Trafficway',
        '3': 'Motor Vehicle Not in Transport Outside the Trafficway',
        '4': 'Working Motor Vehicle (Highway Construction, Maintenance, Utility Only)'
        }
# 2008-Later
UNITTYPE['1'] = 'Motor Vehicle in Transport (Inside or Outside the Trafficway)'

#### Hit and Run
# 1975-76
HIT_RUN = {
        '0': 'Not Applicable',
        '1': 'With Motor Vehicle',
        '2': 'With Non-Occupant'
        }

# 1977-81
HIT_RUN['0'] = 'No/No Hit-and-Run'
HIT_RUN['1'] = 'With Motor Vehicle'
HIT_RUN['2'] = 'Hit Non-Motorist'
HIT_RUN['3'] = 'Left Scene'

# 1982-2008
HIT_RUN['1'] = 'Hit Motor Vehicle in Transport'
HIT_RUN['2'] = 'Hit Pedestrian or Non-Motorist'
HIT_RUN['3'] = 'Hit Parked Vehicle (Working Vehicle, Since 2004) or Object'

# 2002
HIT_RUN['4'] = 'Occupant is Struck by or Fell From Own Hit-and-Run Vehicle'

# 2004
HIT_RUN['4'] = 'Driver Leaves Scene after Non-Collision Event'

# 2003
HIT_RUN['5'] = 'Driver/Occupant Leaves Scene after a Non-Collision Event'

# 2005-06
HIT_RUN['5'] = 'Other Involved Person, not a driver, left Scene'

# 2007-later
HIT_RUN['5'] = 'Hit-and-Run, Other Involved Person Left Scene'

# 2009
HIT_RUN['1'] = 'Yes'
HIT_RUN['9'] = 'Unknown'

# 2010-2011
HIT_RUN['1'] = 'Yes'
HIT_RUN['8'] = 'Not Reported'

# 2012-later
HIT_RUN['1'] = 'Yes'


####
# Registered Vehicle Owner
# Also appears in Parkwork file as POWNER
# 1991-2007
OWNER = {
        '0': 'Not Applicable, Vehicle Not Registered',
        '1': 'Driver (of This Vehicle) Was Registered Owner',
        '2': 'Driver (of This Vehicle) Not Registered Owner (Other Private Owner)',
        '3': 'Vehicle Registered as Business/Company/Government Vehicle',
        '4': 'Vehicle Registered as Rental Vehicle',
        '5': 'Vehicle Was Stolen (Reported By Police)',
        '6': 'Driverless Vehicle',
        '9': 'Unknown'
        }

# 2008-later
OWNER['6'] = 'Driverless/Motor Vehicle Parked/Stopped Off Roadway'

####
# Vehicle Make
# For 1986 or earlier, may have to refer to first several values, 01-09, with single digit
# rather than double digit with leading 0
# also appears in Person and Parkwork files as PMAKE
# 1975-1990
MAKE = {
        '01': 'American Motors',
        '02': 'Jeep',
        '03': 'AM General',
        '06': 'Chrysler',
        '07': 'Dodge',
        '08': 'Imperial',
        '09': 'Plymouth',
        '10': 'Eagle',
        '12': 'Ford',
        '13': 'Lincoln',
        '14': 'Mercury',
        '18': 'Buick',
        '19': 'Cadillac',
        '20': 'Chevrolet',
        '21': 'Oldsmobile',
        '22': 'Pontiac',
        '23': 'GMC',
        '29': 'Other Domestic',
        '30': 'Volkswagen',
        '31': 'Alfa Romeo',
        '32': 'Audi',
        '33': 'Austin-Healey',
        '35': 'Datsun',
        '36': 'Fiat',
        '37': 'Honda',
        '38': 'Isuzu',
        '39': 'Jaguar',
        '40': 'Lancia',
        '41': 'Mazda',
        '42': 'Mercedes-Benz',
        '43': 'MG',
        '44': 'Peugeot',
        '45': 'Porsche',
        '46': 'Renault',
        '47': 'Saab',
        '48': 'Subaru',
        '49': 'Toyota',
        '50': 'Triumph',
        '51': 'Volvo',
        '52': 'Mitsubishi',
        '53': 'Suzuki',
        '57': 'Lexus',
        '58': 'Infiniti',
        '59': 'Other Imports',
        '60': 'BSA',
        '61': 'Ducati',
        '62': 'Harley-Davidson',
        '63': 'Kawasaki',
        '64': 'Moto Guzzi',
        '65': 'Norton',
        '67': 'Yamaha',
        '69': 'Other Motor Cycle',
        '70': 'Moped',
        '80': 'Brockway',
        '81': 'Diamond Reo',
        '82': 'Freightliner',
        '83': 'FWD',
        '84': 'International Harvester',
        '85': 'Kenworth',
        '86': 'Mack',
        '87': 'Peterbilt',
        '88': 'White',
        '95': 'Other Truck/Bus',
        '98': 'Other Make',
        '99': 'Unknown Make'
        }

# 1991-Later
MAKE['18'] = 'Buick/Opel'
MAKE['24'] = 'Saturn'
MAKE['25'] = 'Grumman'
MAKE['33'] = 'Austin/Austin Healey'
MAKE['34'] = 'BMW'
MAKE['35'] = 'Datsun/Nissan'
MAKE['54'] = 'Acura'
MAKE['55'] = 'Hyundai'
MAKE['56'] = 'Merkur'
MAKE['57'] = 'Yugo'
MAKE['59'] = 'Lexus'
MAKE['60'] = 'Daihatsu'
MAKE['61'] = 'Sterling'
MAKE['62'] = 'Land Rover'
MAKE['63'] = 'KIA'
MAKE['64'] = 'Daewoo'
MAKE['65'] = 'Smart'
MAKE['66'] = 'Mahindra'
MAKE['67'] = 'Scion'
MAKE['69'] = 'Other Imports'
MAKE['70'] = 'BSA'
MAKE['71'] = 'Ducati'
MAKE['72'] = 'Harley-Davidson'
MAKE['73'] = 'Kawasaki'
MAKE['74'] = 'Moto Guzzi'
MAKE['75'] = 'Norton'
MAKE['76'] = 'Yamaha'
MAKE['77'] = 'Victory'
MAKE['78'] = 'Other Make Moped'
MAKE['79'] = 'Other Make Motored Cycle'
MAKE['80'] = 'Brockway'
MAKE['81'] = 'Diamond Reo/Reo'
MAKE['82'] = 'Freightliner'
MAKE['83'] = 'FWD'
MAKE['84'] = 'International Harvester/Navistar'
MAKE['85'] = 'Kenworth'
MAKE['86'] = 'Mack'
MAKE['87'] = 'Peterbilt'
MAKE['88'] = 'Iveco/Magirus'
MAKE['89'] = 'White/Autocar, White/GMC'
MAKE['90'] = 'Bluebird'
MAKE['91'] = 'Eagle Coach'
MAKE['92'] = 'Gillig'
MAKE['93'] = 'MCI'
MAKE['94'] = 'Thomas Built'
MAKE['97'] = 'Not Reported'
MAKE['98'] = 'Other Make'
MAKE['99'] = 'Unknown Make'

####
# Body Type
# Look up the manual because there's a whole bunch of caveats holy fucking shit
# 1975-81
BODY_TYP = {
        '01': 'Convertible',
        '02': '2-Door Sedan HT/Coupe',
        '03': '4-Door Sedan HT',
        '04': 'Hatchback',
        '05': 'Car-Pickyp Body',
        '06': 'Station Wagon',
        '07': 'On/Off Road Vehicle - Jeep CJ-S, Bronco, Blazer, Scout, etc.',
        '08': 'Other Auto',
        '09': 'Unknown Auto Type',
        '15': 'Motorcycle',
        '16': 'Moped',
        '17': 'Other Cycle',
        '18': 'Unknown Cycle',
        '25': 'School Bus',
        '26': 'Cross-County',
        '27': 'Transit Bus',
        '28': 'Other Bus',
        '29': 'Unknown Bus',
        '35': 'Snowmobile',
        '36': 'Farm Equipment',
        '37': 'Dune/Swamp Buggy',
        '38': 'Construction Equipment',
        '39': 'Ambulance/Hearse Type',
        '40': 'Large Limousine',
        '41': 'Camper/Motorhome',
        '42': 'Fire Truck',
        '43': 'On/Off-Road Vehicle - Jeep CJ-S, Bronco, Blazer, Scout, etc.',
        '44': 'Other Special Vehicle',
        '45': 'Ambulance EMS',
        '50': 'Pickup',
        '51': 'Van',
        '52': 'Truck-Based Station Wagon',
        '53': 'Straight Truck, Low GVW',
        '54': 'Straight Truck, Medium GVW',
        '55': 'Straight Truck, High GVW',
        '56': 'Straight Truck, Unknown GVW',
        '57': 'Two-Unit Truck',
        '58': 'Multi-Unit Truck',
        '59': 'Truck-Tractor',
        '60': 'Unknown Type Truck',
        '99': 'Unknown'
        }

# 1982-1990
BODY_TYP = {
        '01': 'Convertible',
        '02': '2-Door Sedan/Ht/Coupe',
        '03': '3-Door/2-Door Hatchback',
        '04': '4-Door Sedan/Ht',
        '05': '5-Door/4-Door Hatchback',
        '06': 'Station Wagon',
        '07': 'Hatchback/Number of Doors Unknown',
        '08': 'Other Auto',
        '09': 'Unknown Auto Type',
        '10': 'Auto Pickup',
        '11': 'Auto Panel',
        '12': 'Short Utility/Not Truck-Based',
        '13': 'Large Limousine',
        '14': '3-Wheel Vehicle Unknown Body Type',
        '20': 'Motorcycle',
        '21': 'Moped',
        '27': '3-Wheel Motorcycle or Moped',
        '28': 'Other Cycle',
        '29': 'Unknown Cycle',
        '30': 'School Bus',
        '31': 'Cross-Country/Intercity',
        '32': 'Transit Bus',
        '38': 'Other Bus',
        '39': 'Unknown Bus',
        '40': 'Van',
        '41': 'Van Commercial Cutaway',
        '42': 'Van Motorhome',
        '48': 'Other Van Type',
        '49': 'Unknown Van Type',
        '50': 'Pickup',
        '51': 'Pickup W/Slide-in Camper',
        '52': 'Pickup-Based Motorhome',
        '53': 'Cab Chassis Based',
        '54': 'Truck-Based Panel',
        '55': 'Truck-Based Sw',
        '56': 'Truck-Based Utility',
        '58': 'Other Light Conventional Truck',
        '59': 'Unknown Light Convent Truck',
        '67': 'Utility, Base Body Unknown',
        '69': 'Unknown Light Truck',
        '70': 'Straight Truck, Low GVW',
        '71': 'Straight Truck, Medium GVW',
        '72': 'Straight Truck, High GVW',
        '73': 'Medium/Heavy Truck Motorhome',
        '74': 'Truck/Tractor',
        '75': 'Unknown Medium Truck',
        '76': 'Unknown Heavy Truck',
        '77': 'Camper/Motorhome',
        '78': 'Single Unit Straight Truck GVW Unknown',
        '79': 'Unknown Truck Type',
        '80': 'Snowmobile',
        '81': 'Farm Equipment/Not Trucks',
        '82': 'ATV, Dune/Swamp Buggy',
        '83': 'Construction Equipment/Not Trucks',
        '88': 'Other',
        '89': 'Unknown Other Vehicle',
        '90': '3-Wheel Vehicle Unknown Body Type',
        '99': 'Unknown Body Type'
        }

# 1991-2009
BODY_TYP = {
        '01': 'Convertible (Excludes Sunroof, T-Bar',
        '02': '2-Door Sedan/Hardtop/Coupe',
        '03': '3-Door/2-Door Hatchback',
        '04': '4-Door Sedan/Hardtop',
        '05': '5-Door/4-Door Hatchback',
        '06': 'Station Wagon (Excluding Van and Truck-Based)',
        '07': 'Hatchback, Number of Doors Unknown',
        '08': 'Sedan/Hardtop, Number of Doors Unknown',
        '09': 'Other or Unknown Automobile Type',
        '10': 'Auto-Based Pickup',
        '11': 'Auto-Based Panel (Cargo Station Wagon, Auto-Based Ambulance or Hearse',
        '12': 'Large Limousine - More Than Four Side Doors or Stretch Chassis',
        '13': 'Three-Wheel Automobile or Automobile Derivative',
        '14': 'Compact Utility',
        '15': 'Large Utility',
        '16': 'Utility Station Wagon',
        '19': 'Utility Unknown Body',
        '20': 'Minivan',
        '21': 'Large Van - Includes Van-Based Buses',
        '22': 'Step Van or Walk-in Van',
        '23': 'Van Motorhome',
        '24': 'Van-Based School Bus',
        '25': 'Van-Based Transit Bus',
        '28': 'Other Van Type',
        '29': 'Unknown Van Type',
        '30': 'Compact Pickup',
        '31': 'Standard Pickup',
        '32': 'Pickup with Slide-In Camper',
        '33': 'Convertible Pickup',
        '39': 'Unknown',
        '40': 'Cab Chassis-Based',
        '41': 'Truck-Based Panel',
        '42': 'Light-Truck-Based Motorhome (Chassis Mounted)',
        '45': 'Other Light Conventional Truck Type',
        '48': 'Unknown Light-truck Type (Not a Pickup)',
        '49': 'Unknown Light-vehicle Type (Automobile, Utility Vehicle, Van or Light Truck)',
        '50': 'School Bus',
        '51': 'Cross-Country/Intercity Bus',
        '52': 'Transit Bus',
        '58': 'Other Bus Type',
        '59': 'Unknown Bus Type',
        '60': 'Step Van',
        '61': 'Single-Unit Straight Truck or Cab Chassis (10000 lbs < GVWR < or = 19500 lbs)',
        '62': 'Single-Unit Straight Truck or Cab Chassis (19500 lbs < GVWR < or = 26000 lbs)',
        '63': 'Single-Unit Straight Truck or Cab Chassis (GVWR > 26000 lbs)',
        '64': 'Single-Unit Straight Truck',
        '65': 'Medium/Heavy Truck-Based Motorhome',
        '66': 'Truck/Tractor (Cab Only, or with Any Number of Trailing Units: Any Weight)',
        '67': 'Medium/Heavy Pickyp (GVWR > 10000 lbs)',
        '71': 'Unknown if Single-Unit or Combination-Unit Medium Truck (10000 lbs < GVWR < 26000 lbs)',
        '72': 'Unknown if Single-Unit or Combination-Unit Heavy Truck (GVWR > 26000 lbs)',
        '73': 'Camper or Motorhome, Unknown Truck Type',
        '78': 'Unknown Medium/Heavy Truck Type',
        '79': 'Unknown Truck Type',
        '80': 'Motorcycle',
        '81': 'Moped (Motorized Bicycle)',
        '82': 'Three-Wheel Motorcycle/Moped - Not All-Terrain Vehicle',
        '83': 'Off-Road Motorcycle (2-Wheel)',
        '88': 'Other Motorced Cycle Type (Mini-Bikes, Motor Scooters)',
        '89': 'Unknown Motored Cycle Type',
        '90': 'ATV',
        '91': 'Snowmobile',
        '92': 'Farm Equipment Other Than Trucks',
        '93': 'Construction Equipment Other Than Trucks',
        '94': 'Motorized Wheel Chair',
        '97': 'Other Vehicle Type (Includes Go-Cart, Fork-Lift, City Street Sweeper, Dune/Swamp Buggy',
        '99': 'Unknown Body Type'
        }

# 2010-later
BODY_TYP['08'] = 'Sedan/Hardtop, Number of Doors Unknown'
BODY_TYP['09'] = 'Other or Unknown Automobile Type'
BODY_TYP['17'] = '3-Door Coupe'
BODY_TYP['55'] = 'Van-Based Bus GVWR > 10000 lbs'
BODY_TYP['68'] = 'Single-Unit Straight Truck (GVWR unknown)'
BODY_TYP['94'] = 'Low Speed Vehicle (LSV)/Neighborhood Electric Vehicle (NEV)'
BODY_TYP['95'] = 'Golf Cart'
BODY_TYP['98'] = 'Not Reported'

        }
# 1991-93
BODY_TYP['08'] = 'Other Auto'
BODY_TYP['09'] = 'Unknown Auto Type'

####
# Vehicle Model Year
# 00-98 - Actual model Year
# 9998 - Not Reported
# 9999 - Unknown

####
# Vehicle Identification Number (VIN)
# 1975-1993: first 10 numbers
# 1994 -later: first 12 numbers
VIN = {
        '000000000000': 'No VIN Required',
        '888888888888': 'Not Reported',
        '999999999999': 'Unknown'
        }

####
# Vehicle Trailing
# applies to tractor trailers, boats, cars, and U-Haul-type vehicles that are towed with hitch
# 1975-81
TOW_VEH = {
        '0': 'No Trailing Unit',
        '1': 'Yes'
        }

# 1982
TOW_VEH['1'] = 'Yes, One Trailing Unit'
TOW_VEH['4'] = 'Yes, Number of Trailing Units Unknown'
TOW_VEH['5'] = 'Yes, Two or More Trailing Units'

# 1983-2003
TOW_VEH['2'] = 'Yes, Two Trailing Units'
TOW_VEH['3'] = 'Yes, Three or More Trailing Units'
TOW_VEH['4'] = 'Yes, Number of Trailing Units Unknown'
TOW_VEH['9'] = 'Unknown'

# 2004-2008
TOW_VEH['5'] = 'Vehicle Towing another Motor Vehicle'

# 2009-later
TOW_VEH['5'] = 'Vehicle Towing another Motor Vehicle - Fixed Linkage'
TOW_VEH['6'] = 'Vehicle Towing another Motor Vehicle - Non-Fixed Linkage'

####
# Jackknife
J_KNIFE = {
        '0': 'Not an Articulated Vehicle',
        '1': 'No',
        '2': 'Yes',
        '3': 'Yes, Subsequent Event'
        }

# if 1982-later
J_KNIFE['2'] = 'Yes, First Event'

####
# Motor Carrier Identification Number (MCID)
# found only on vehicles of interstate for-hire or private carriers inthe transportation business
# collected only for buses and trucks over 4,500 kg GVWR (Bodytype (V5) = 60, 64, 66-79)
# this data element is applicable to the following vehicles:
# Medium/Heavy trucks: vehicles with two axles/six tires and/or gross weight greater than 10000 lbs
# Buses with 16 or more seats (including the driver)
# Trucks and vans of any size carrying hazardous cargo
# light commercial trucks pulling a trailer with gross combination weight rating (GCWR) > 10000 lbs
MCARR_ID = {
        '000000000000': 'Not Applicable',
        '777777777777': "Not Reported",
        '888888888888': 'None',
        '999999999999': 'Unknown'
        }

####
# MCID Issuing Authority
# 1998-2006
# 01-56: FARS State Code
MCARR_I1 = {
        '00': 'Not Applicable',
        '57': 'US DOT',
        '58': 'ICC',
        '88': 'None',
        '95': 'Canada',
        '96': 'Mexico',
        '99': 'Unknown'
        }

# 2007-2009
MCARR_I1['58'] = 'MC/MX (ICC)'

# 2010-later
MCARR_I1['58'] = 'MC/MX (ICC)'
MCARR_I1['77'] = 'Not Reported'

####
# MCID Identification NUmber
# MCARR_I2
# same as MCID

####
# Gross Vehicle Weight Rating
# value specified by manufacturer for single-unit truck, truck tractor, or trailer
GVWR = {
        '0': 'Not Applicable',
        '1': '10,000 lbs or less',
        '2': '10,001 - 26,000 lbs',
        '3': '26,001 lbs or more',
        '8': 'Not Reported',
        '9': 'Unknown'
        }

####
# Vehicle Configuration
# Also appears in Parkwork as PV_CONFIG
# 1991-94
V_CONFIG = {
        '0': 'Not Applicable, Not a Medium/Heavy Truck or Bus',
        '1': 'Single-Unit Truck (2 axles, 6 tires)',
        '2': 'Single-Unit Truck (3 or More axles)',
        '3': 'Truck/Trailers',
        '4': 'Truck Tractor (Bobtail, i.e. Tractor Only, No Trailer)',
        '5': 'Truck Tractor/Semi-Trailer',
        '6': 'Medium/Heavy Trucks, Cannot Classify',
        '7': 'Bus',
        '9': 'Unknown'
        }

# 1995-2000
V_CONFIG = {
        '0': 'Not Applicable, Not a Medium/Heavy Truck or Bus',
        '1': 'Single-Unit Truck (2 axles, 6 tires)',
        '2': 'Single-Unit Truck (3 or more axles)',
        '3': 'Single-Unit Truck (Unknown Number of Axles, Tires)',
        '4': 'Truck/Trailer(s)',
        '5': 'Truck Tractor (Bobtail, i.e., Tractor Only, No Trailer)',
        '6': 'Truck Tractor/Semi-Trailer',
        '7': 'Medium/Heavy Trucks, Cannot Classify',
        '8': 'Bus',
        '9': 'Unknonw if Light or Medium/Heavy Truck/Bus'
        }

# 2001-2009
V_CONFIG = {
        '00': 'Not Applicable, Not a Medium/Heavy Truck or Bus or Vehicle Displaying a Hazardous Material Placard',
        '01': 'Single-Unit Truck (2 axles, 6 tires)',
        '02': 'Single-Unit Truck (3 or more axles)',
        '03': 'Single-Unit Truck (Unknown Number of Axles, Tires)',
        '04': 'Truck/Trailer(s)',
        '05': 'Truck Tractor (Bobtail, i.e., Tractor Only, No Trailer)',
        '06': 'Truck Tractor/Semi-Trailer (One Trailer)',
        '07': 'Truck Tractor/Doubles (Two Trailers)',
        '08': 'Tractor/Triples (Three Trailers)',
        '19': 'Medium/Heavy Trucks, Cannot Classify',
        '20': 'Bus (Seats for 9-15 Occupants, Including Driver)',
        '21': 'Bus (Seats for 16 or More People, Including Driver)',
        '70': 'Light Truck (Van, Mini-Van, Panel, Pickup, Sport Utility Vehicle Displaying a Hazardous Material Placard)'
        '80': 'Passenger Car (Only When Displaying a Hazardous Material Placard)',
        '99': 'Unknown if Light or Medium/Heavy Truck Bus'
        }
# 2001-2006
V_CONFIG['21'] = 'Bus (Seats for More Than 15 People, Including Driver)'

#2010 or later
V_CONFIG = {
        '00': 'Not Applicable',
        '01': 'Single-Unit Truck (2 axles and GVWR more than 10,000 lbs)',
        '02': 'Single-Unit Truck (3 or more axles)',
        '04': 'Truck Pulling Trailer(s)',,
        '05': 'Truck Tractor (Bobtail, i.e., Tractor Only, No Trailer)',
        '06': 'Truck Tractor/Semi-Trailer',
        '07': 'Truck Tractor/Double',
        '08': 'Truck Tractor/Triple',
        '10': 'Vehicle 10,000 lbs or Less Placarded for Hazardous Materials',
        '19': 'Truck More than 10,000 lbs, Cannot Classify',
        '20': 'Bus/Large Van (Seats for 9-15 Occupants, Including Driver)',
        '21': 'Bus (Seats for More than 15 Occupants, Including Driver, 2010 and Later)',
        '98': 'Not Reported',
        '99': 'Unknown'
        }

####
# Cargo Body Type
# Also appears in Parkwork as PCARGTYP
# 1991-94
CARGO_BT = {
        '00': 'Not Applicable Not a Truck or Bus',
        '01': 'Van/Enclosed Box',
        '02': 'Cargo Tank',
        '03': 'Flatbed',
        '04': 'Dump',
        '05': 'Concrete Mixer',
        '06': 'Auto Transporter',
        '07': 'Garbage/Refuse',
        '08': 'Medium/Heavy Truck, Other Body Type',
        '09': 'Bus',
        '99': 'Unknown Vehicle Type'
        }

# 1995-2000
CARGO_BT['08'] = 'Bus'
CARGO_BT['97'] = 'Medium/Heavy Truck, Other Cargo Body Type'
CARGO_BT['98'] = 'Medium/Heavy Truck, Unknown Cargo Body Type'
CARGO_BT['99'] = 'Unknown if Light or Medium/Heavy Truck/Bus'

# 2001-2008
CARGO_BT['00'] = 'Not Applicable, Not a Medium/Heavy Truck or Bus'
CARGO_BT['08'] = 'Grain, Chips, Gravel'
CARGO_BT['09'] = 'Pole'
CARGO_BT['10'] = 'Log'
CARGO_BT['11'] = 'Intermodal Chassis'
CARGO_BT['12'] = 'Vehicle Towing Another Motor Vehicle'
CARGO_BT['20'] = 'Bus (Seats 9-15 People, Including Driver)'
CARGO_BT['21'] = 'Bus (Seats More Than 15 People, including Driver)'
CARGO_BT['96'] = 'No Cargo Body Type'
CARGO_BT['97'] = 'Medium/Heavy Truck, or Bus, Other Cargo Body Type'
CARGO_BT['98'] = 'Medium/Heavy Truck or Bus, Unknown Cargo Body Type'
CARGO_BT['99'] = 'Unknown if Light or Medium/Heavy Truck/Bus'

# 2007-2008
CARGO_BT['21'] = 'Bus (Seats for 16 or More People, Including Driver)'

# 2009
CARGO_BT['09'] = 'Pole-Trailer'
CARGO_BT['11'] = 'Intermodal Container Chassis'
CARGO_BT['22'] = 'Bus'
CARGO_BT['97'] = 'Other'
CARGO_BT['98'] = 'Unknown Cargo Body Type'
CARGO_BT['99'] = 'Unknown'

# 2010-Later
CARGO_BT['28'] = 'Not Reported'

####
# Hazardous Materials Involvement
HAZ_INV = {
        '1': False,
        '2': True
        }

####
# Hazardous Materials Placard
# Identifies presence of hazardous materials and whether vehicle displayed
# a hazardous materials placard
HAZ_PLAC = {
        '0': 'Not Applicable',
        '1': False,
        '2': True,
        '8': 'Not Reported'
        }

####
# Hazardous Materials Identification Number
# Any 4 digit number other than 0000 or 8888
HAZ_ID = {
        '0000': 'Not Applicable',
        '8888': 'Not Reported'
        }

####
# Hazardous Materials Class Number
# 1-7 or 9 : Actual Number (2007)
# 01-09: Actual Number (2008-later)
HAZ_CNO = {
        '0': 'Not Applicable',
        '00': 'Not Applicable',
        '8': 'Not Reported',
        '88': 'Not Reported'
        }

####
# Release of Hazardous Material from the Cargo Compartment
HAZ_REL = {
        '0': 'Not Applicable',
        '1': False,
        '2': True,
        '8': 'Not Reported'
        }

####
# Bus Use
# Common type of bus service this vehicle was being used as at the time of
# the crash or the primary use for the bus if not in service at the time 
# of the crash
# 2000-2009:
BUS_USE = {
        '0': 'Not Used as a Bus',
        '1': 'Used as a Public School Bus',
        '2': 'Used as a Private School Bus',
        '3': 'Used as a School Bus, Public or Private Unknown',
        '4': 'Used as a Scheduled Service Bus',
        '5': 'Used as a Tour Bus',
        '6': 'Used as a Commuter Bus',
        '7': 'Used as a Shuttle Bus',
        '8': 'Modified for Personal/Private Use',
        '9': 'Unknown Bus Use'
        }

# 2010-later
BUS_USE = {
        '00': 'Not a Bus',
        '01': 'School Bus',
        '04': 'Intercity Bus',
        '05': 'Charter/Tour Bus',
        '06': 'Transit/Commuter Bus',
        '07': 'Shuttle Bus',
        '08': 'Modified for Personal/Private Use',
        '98': 'Not Reported',
        '99': 'Unknown'
        }

####
# Special Use
# Also appears in Person and Parkwork as PSP_USE
SPEC_USE = {
        '0': 'No Special Use',
        '00': 'No Special Use',
        '1': 'Taxi',
        '01': 'Taxi',
        '2': 'Vehicle Used as School Bus',
        '02': 'Vehicle Used as School Bus',
        '3': 'Vehicle Used as Other Bus',
        '03': 'Vehicle Used as Other Bus',
        '4': 'Military',
        '04': 'Military',
        '5': 'Police',
        '05': 'Police',
        '6': 'Ambulance',
        '06': 'Ambulance',
        '7': 'Fire Truck',
        '07': 'Fire Truck',
        '8': 'Emergency Services Vehicle',
        '08': 'Emergency Services Vehicle',
        '9': 'Unknown',
        '98': 'Not Reported',
        '99': 'Unknown'
        }

# 2012-later
SPEC_USE['02'] = 'Vehicle Used for School Transport'

####
# Emergency Use
# Whether vehicle was engaged in emergency use.
# Legally authorized by a government authority to respond to emergencies
# with or without the use of emergency warning equipment
# Also appears in Person and Parkwork as PEM_USE
EMER_USE = {
        '0': False,
        '1': True,
        '8': 'Not Reported',
        '9': 'Unknown'
        }

####
# Travel Sped
# Speed vehicle was traveling prior to the occurrence of the crash as 
# reported by investigating officer
# Data collected after crash and is estimate of travel speed (often a judgement)
# Computing mean without removing unknowns will increase mean travel speed
# Always a high number of unknowns
# 1975-2008: 2-digit number between 01-96 is reported speed; 97 means greater than 96
# 2009-Later: 3-digit number between 001-151 is reported speed; 
TRAV_SP = {
        '00': 'Stopped Motor Vehicle in Transport',
        '000': 'Stopped Motor Vehicle in Transport',
        '97': 'Speed Greater Than 96 mph',
        '997': 'Speed Greater Than 151 mph',
        '98': 'Not Reported',
        '998': 'Not Reported',
        '99': 'Unknown',
        '999': 'Unknown'
        }

####
# Underride/Override
# Striking vehicle (not vehicle struck) determines the u/o condition
# Also appears in Parkwork as PUNDERIDE
# 1994-later
# 1994-2011
UNDERRIDE = {
        '0': 'No Underride or Override',
        '1': 'Underride (Compartment Intrusion) - With Motor Vehicle in Transport',
        '2': 'Underride (No Compartment Intrusion) - With Motor Vehicle in Transport',
        '3': 'Underride (Compartment Intrusion Unknown) - With Motor Vehicle in Transport',
        '4': 'Underride (Compartment Intrusion) - With Motor Vehicle Not in Transport',
        '5': 'Underride (No Compartment Intrusion) - With Motor Vehicle Not in Transport',
        '6': 'Underride (Compartment Intrusion Unknown) - With Motor Vehicle Not in Transport',
        '7': 'Override, Motor Vehicle in Transport',
        '8': 'Override, Motor Vehicle Not in Transport',
        '9': 'Unknwon if Underride or Override'
        }
####
# Rollover
# Any vehicle rotation of 90 degrees or more about any true longitudinal or 
# lateral axis
# Also appears in Person file
ROLLOVER = {
        '0': 'No Rollover',
        '1': 'First Event',
        '2': 'Subsequent Event'
        }

# 2009-later
ROLLOVER['1'] = 'Rollover, Tripped by Object/Vehicle'
ROLLOVER['9'] = 'Rollover, Unknown Type'

#### Location of Rollover
ROLINLOC = {
        '0': 'No Rollover',
        '1': 'On Roadway',
        '2': 'On Shoulder',
        '3': 'On Median/Separator',
        '4': 'In Gore',
        '5': 'On Roadside',
        '6': 'Outside of Trafficway',
        '7': 'In Parking Lane/Zone',
        '9': 'Unknown'
        }

####
# Initial Contact Point
# 01-12: clock points
# 1975-2009
IMPACT1 = {
        '00': 'Non-Collision',
        '13': 'Top',
        '14': 'Undercarriage',
        '15': 'Underride',
        '16': 'Override',
        '18': 'This Vehicle Set Something in Motion Causing Injury or Damage',
        '99': 'Unknown'
        }

# 2010-2011
IMPACT1['18'] = 'Set-in-Motion (Not a Clock Point)'
IMPACT1['61'] = 'Left'
IMPACT1['62'] = 'Left-Front Half'
IMPACT1['63'] = 'Left-Back Half'
IMPACT1['81'] = 'Right'
IMPACT1['82'] = 'Right-Front Half'
IMPACT1['83'] = 'Right-Back Half'
IMPACT1['98'] = 'Not Reported'
IMPACT1['99'] = 'Unknown'

# 2012-later
IMPACT1['18'] = 'Set-in-Motion (Not a Clock Value)'
IMPACT1['62'] = 'Left-Front Side'
IMPACT1['63'] = 'Left-Back Side'
IMPACT1['81'] = 'Right'
IMPACT1['82'] = 'Right-Front Side'
IMPACT1['83'] = 'Right-Back Side'
IMPACT1['98'] = 'Not Reported'
IMPACT1['99'] = 'Unknown'

####
# Extent of Damage
# 1975-2008
DEFORMED = {
        '0': 'None',
        '2': 'Other (Minor)',
        '4': 'Functional (Moderate)',
        '6': 'Disabling (Severe)',
        '9': 'Unknown'
        }

# 2009-later
DEFORMED = {
        '0': 'No Damage',
        '2': 'Minor Damage',
        '4': 'Functional Damage',
        '6': 'Disabling Damage',
        '8': 'Not Reported',
        '9': 'Unknown'
        }

####
# Vehicle Removal
# mode by which vehicle left the scene of the crash
# 1975-2008
TOWAWAY = {
        '1': 'Driven Away',
        '2': 'Towed Away',
        '3': 'Abandoned/Left Scene',
        '4': 'Not Towed Away',
        '9': 'Unknown'
        }

# 2009 - later
TOWED = {
        '1': 'Driven Away',
        '2': 'Towed Due to Disabling Damage',
        '3': 'Towed ot Due to Disabling Damage',
        '4': 'Abandoned/Left at Scene',
        '8': 'Not Reported',
        '9': 'Unknonw'
        }

####
# Most Harmful Event
# First Hamful Event (HARM_EV in Accident file) applies to crash
# This applies to vehicle
# Judgement calls of FARS analysts
# 1979-1981
M_HARM = {
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
        '17': 'Bridge or Overpass',
        '18': 'Building',
        '19': 'Culvert',
        '20': 'Curb or Wall',
        '21': 'Divider',
        '22': 'Embankment',
        '23': 'Fence',
        '24': 'Guard Rail',
        '25': 'Light Support',
        '26': 'Sign Post',
        '27': 'Tree/Shrubbery',
        '28': 'Utility Pole',
        '29': 'Other Pole/Support',
        '30': 'Impact Attenuator',
        '31': 'Other Fixed Object',
        '32': 'Bridge or Overpass (Passing Under)',
        '33': 'Bridge or Overpass (Passing Over)',
        '99': 'Unknown'
        }

# 1982 - 2003
M_HARM = {
        '01': 'Rollover/Overturn',
        '02': 'Fire/Explosion',
        '03': 'Immersion (or Partial Immersion, Since 20120)',
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
        '14': 'Parked Motor Vehicle',
        '15': 'Other Type Non-Motorist',
        '16': 'Thrown or Falling Object',
        '17': 'Boulder',
        '18': 'Other Object (Not Fixed)',
        '19': 'Building',
        '20': 'Impact Attenuator/Crash Cushion',
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
        '36': 'Embankment - Rock, Stone, or Concrete',
        '37': 'Embankment - Material Type Unknown',
        '38': 'Fence',
        '39': 'Wall',
        '40': 'Fire Hydrant',
        '41': 'Shrubbery',
        '42': 'Tree (Standing Only)',
        '43': 'Other Fixed Object',
        '44': 'Pavement Surface Irregularity',
        '45': 'Working Construction, Maintenance, or Utility Vehicles',
        '46': 'Traffic Signal Support',
        '47': 'Vehicle Occuant Struck or Run Over by Own Vehicle',
        '48': 'Collision With Snow Bank',
        '49': 'Ridden Animal or Animal-Drawn Conveyance',
        '50': 'Bridge Overhead Structure',
        '99': 'Unknown'
        }
# 1993-2003
M_HARM['45'] = 'Transport Device Used as Equipment'
# 2004-2009
M_HARM['15'] = 'Non-Motorist or Personal Conveyance'
M_HARM['44'] = 'Pavement Surface Irregularity'
M_HARM['45'] = 'Working Construction, Maintenance, or Utility Vehicles'
M_HARM['51'] = 'Jackknife'
M_HARM['52'] = 'Guardrail End'
M_HARM['53'] = 'Mail Box'
M_HARM['54'] = 'Motor Vehicle Struck by Falling/Shifting Cargo or Anything Set in Motion by Another Motor Vehicle in Transport'
M_HARM['55'] = 'Other Not-in-Transport Motor Vehicle'
M_HARM['57'] = 'Cable Barrier'
M_HARM['60'] = 'Cargo/Equipment Loss or Shift (Causing Injury or Damage)'

# 2008 or later
M_HARM['55'] = 'Motor Vehicle in Motion Outside the Trafficway'

# 2010 or later
M_HARM['06'] = 'Injured in Vehicle (Non-Collision)'
M_HARM['09'] = 'Pedalcyclist'
M_HARM['10'] = 'Railway Vehicle'
M_HARM['11'] = 'Live Animal'
M_HARM['12'] = 'Motor Vehicle in Transport'
M_HARM['21'] = 'Bridge Pier or Support'
M_HARM['23'] = 'Bridge Rail (includes Parapet)'
M_HARM['30'] = 'Utility Pole/Light Support'
M_HARM['35'] = 'Embankment'
H_HARM['44'] = 'Pavement Surface Irregularity (Ruts, Potholes, Grates, etc.)'
M_HARM['45'] = 'Working Motor Vehicle'
M_HARM['48'] = 'Snow Bank'
M_HARM['51'] = 'Jackknife (Harmful to this Vehicle)'
M_HARM['54'] = 'Motor Vehicle In-Transport Strikes or is Struck by Cargo, Persons, or Objects Set-in-Motion from/by Another Motor Vehicle In-Transport'
M_HARM['58'] = 'Ground'
M_HARM['59'] = 'Traffic Sign Support'
M_HARM['72'] = 'Cargo/Equipment Loss or Shift (Harmful to This Vehicle)'
M_HARM['98'] = 'Not Reported'

####
# Related Factors - Vehicle Level
# 1975-1981
VEH_CF1 = {
        '00': 'None',
        '01': 'Tires and Wheels',
        '02': 'Brake System',
        '03': 'Steering System - Tie Rod, Kingpin, Ball Joint, etc.',
        '04': 'Suspension - Springs, Shock Absorbers, MacPherson struts, Axle Bearing, Control Arms, etc.',
        '05': 'Power Train - Universal Joint, Drive Shaft, Transmission, etc.',
        '06': 'Exhaust System',
        '07': 'Headlights',
        '08': 'Signal Lights',
        '09': 'Other Lights',
        '10': 'Horn',
        '11': 'Mirrors',
        '12': 'Wipers',
        '13': 'Driver Seating and Control',
        '14': 'Body, Doors, Hood, Other',
        '15': 'Trailer Hitch',
        '99': 'Unknown'
        }

# 1982-2009
VEH_CF1['01'] = 'Tires (Does Not Include Wheels)'
VEH_CF1['16'] = 'Wheels'
VEH_CF1['17'] = 'Air Bags'
VEH_CF1['18'] = 'Other Vehicle Defects'
VEH_CF1['19'] = 'Safety Belts'
VEH_CF1['31'] = 'Hit-and-Run Vehicle'
VEH_CF1['32'] = 'Vehicle Registration for Handicapped'
VEH_CF1['33'] = 'Vehicle Being Pushed by Non-Motorist'
VEH_CF1['34'] = 'Vehicle Impact Point - the Result of Something Set in Motion'
VEH_CF1['35'] = 'Reconstructed/Altered Vehicle'
VEH_CF1['36'] = 'Electric/Alternative Fuel Vehicle'
VEH_CF1['37'] = 'Transporting Children to/from Head Start/Day Care'
VEH_CF1['38'] = 'Vehicle Went Airborne During Crash'
VEH_CF1['39'] = 'Highway Construction, Maintenance, or Utility Vehicle'
VEH_CF1['40'] = 'Highway Incident Response Vehicle'
VEH_CF1['41'] = 'Police, Fire, or EMS Vehicle Working at the Scene of an Emergency or Performing Other Traffic Control Activities'
VEH_CF1['42'] = 'Other Working Vehicle (Not Construction, Maintenance, Utility, Police, Fire, or EMS Vehicle)'
VEH_CF1['43'] = 'Hazardous Materials/Cargo Released From This Vehicle'
VEH_CF1['44'] = 'Adaptive Equipment'

VEH_CF2 = VEH_CF1

# 2010-later
VEH_SC1 = {
        '00': 'None',
        '30': '3-Wheeled Motorcycle Conversion',
        '32': 'Vehicle Registration for Handicapped',
        '33': 'Vehicle Being Pushed by Non-Motorist',
        '35': 'Reconstructed/Altered Vehicle',
        '36': 'Electric/Alternative Fuel Vehicle',
        '37': 'Transporting Children to/from Head Start/Day Care',
        '39': 'Highway Construction, Maintenance, or Utility Vehicle, In Transport',
        '40': 'Highway Incident Response Vehicle',
        '41': 'Police, Fire, or EMS Vehicle Working at the Scene of an Emergency or Performing Other Traffic Control Activities',
        '42': 'Other Working Vehicle (Not Construction, Maintenance, Utility, Police, Fire, or EMS Vehicle, Since 2004)',
        '44': 'Adaptive Equipment',
        '99': 'Unknown'
        }

####
# Fire Occurrence
FIRE_EXP = {
        '0': False,
        '1': True,
        '2': 'Fire Occurred in This Vehicle and Initiated Fire/Explosion in Another Vehicle'
        }

####
# Make Model Combined
# Refer to FARS-NASS GES Coding Manual
# MAK_MOD

####
# VIN Character 1
# first character in VIN
# VIN_1
# for i in range(1,13)...

####
# VIN Vehicle Type
VINTYPE = {
        'P': 'Passenger Vehicle',
        'T': 'Truck',
        'M': 'Motorcycle',
        'U': 'Unknown'
        }

####
# VIN make
# National Crime Information Center (NCIC) Standard Make Abbreviation
# 4-character abbreviation
# VINMAKE

####
# VIN Model
### 3-character model (series) abbreviation
# VINA_MOD

####
# VIN Body Type
# also appears in Person and Parkwork as PVIN_BT
VIN_BT = {
        '2D': 'Passenger Vehicle Sedan 2-Door',
        '2F': 'Passenger Vehicle Formal Hardtop 2-Door',
        '2H': 'Passenger Vehicle Hatchback 2-Door',
        '2L': 'Passenger Vehicle Liftback 3-Door',
        '2P': 'Passenger Vehicle Pillard Hardtop 2-Door',
        '2T': 'Passenger Vehicle Hardtop 2-Door',
        '2W': 'Truck 2-Door Wagon/Sport Utility',
        '3D': 'Passenger Vehicle Runabout 3-Door',
        '4D': 'Passenger Vehicle Sedan 4-Door',
        '4H': 'Passenger Vehicle Hatchback 4-Door',
        '4L': 'Passenger Vehicle Liftback 5-Door',
        '4P': 'Passenger Vehicle Pillard Hardtop 4-Door',
        '4T': 'Passenger Vehicle Hardtop 4-Door',
        '4W': 'Truck 4-Door Wagon/Sport Utility or Passenger Vehicle Wagon 4-Door',
        '5D': 'Passenger Vehicle Sedan 5-Door',
        '8V': 'Truck 8-Passenger Sport Van',
        'AC': 'Truck Auto Carrier',
        'AM': 'Passenger Vehicle Ambulance',
        'AR': 'Truck Armored Truck',
        'AT': 'Motorcycle All-Terrain',
        'BU': 'Bus',
        'CB': 'Truck Chassis and Cab or Passenger Vehicle Cab & Chassis',
        'CC': 'Truck Conventional Cab',
        'CG': 'Truck Cargo Van',
        'CH': 'Truck Crew Chassis',
        'CL': 'Truck Club Chassis',
        'CM': 'Truck Concrete or Transit Mixer',
        'CP': 'Truck Crew Pickup or Passenger Vehicle Coupe',
        'CR': 'Truck Crane',
        'CS': 'Truck Super Cab/Chassis Pickup',
        'CU': 'Truck Custom Pickup',
        'CV': 'Truck Convertible (Jeep Commando, Suzuki Samurai, Dodge Dakota) or Passenger Vehicle Convertible',
        'CY': 'Truck Cargo Cutaway',
        'DP': 'Truck Dump',
        'DS': 'Truck Tractor Truck',
        'EC': 'Truck Extended Cargo Van',
        'EN': 'Motorcycle Enduro',
        'ES': 'Truck Extended Sport Van',
        'EV': 'Truck Extended Van',
        'EW': 'Truck Extended Window Van',
        'FB': 'Truck Flatbed or Platform',
        'FC': 'Truck Forward Control',
        'FT': 'Truck Fire Truck',
        'GG': 'Truck Garbage or Refuse',
        'GL': 'Truck Gliders',
        'GN': 'Truck Grain',
        'HB': 'Passenger Vehicle Hatchback Number Doors Unknown',
        'HO': 'Truck Hopper',
        'HR': 'Passenger Vehicle Hearse',
        'HT': 'Passenger Vehicle Hardtop Number Doors Unknown',
        'IC': 'Truck Incomplete Chassis',
        'IE': 'Truck Incomplete Ext Van',
        'LB': 'Passenger Vehicle Liftback',
        'LG': 'Truck Logger',
        'LL': 'Truck Suburban & Carry-All',
        'LM': 'Passenger Vehicle Limousine',
        'MH': 'Truck Motorized Home',
        'MK': 'Motorcycle Mini-Bike',
        'MN': 'Motorcycle Mini Moto Cross',
        'MM': 'Motorcycle Moped',
        'MP': 'Truck Multipurpose',
        'MR': 'Motorcycle Mini Road/Trail',
        'MS': 'Motorcycle Motor Scooter',
        'MV': 'Truck Maxi-Van',
        'MX': 'Motorcycle Moto Cross',
        'MY': 'Truck Motorized Cutaway or Motorcycle Mini-Cycle',
        'NB': 'Passenger Vehicle Notchback',
        'PC': 'Truck Club Cab Pickup',
        'PD': 'Truck Parcel Delivery',
        'PK': 'Truck Pickup or Passenger Vehicle Pickup, Truck Commonly Registered Passengers',
        'PM': 'Truck Pickup with Camper Mounted on Bed',
        'PN': 'Truck Panel or Passenger Vehicle Panel, Truck Commonly Registered as Passengers',
        'PS': 'Truck Super Cab Pickup',
        'RC': 'Motorcycle Racer',
        'RD': 'Truck or Passenger Vehicle Roadster',
        'RS': 'Motorcycle Road/Street',
        'RT': 'Motocrcyl Road/Trail',
        'S1': 'Truck One-Seat',
        'S2': 'Truck Two-Seat',
        'SB': 'Passenger Vehicle Sport Hatchback',
        'SC': 'Passenger Vehicle Sport Coupe',
        'SD': 'Passenger Vehicle Sedan, number doors unknown',
        'SN': 'Truck Step Van',
        'SP': 'Truck Sport Pickup',
        'ST': 'Truck Skate or Rack',
        'SV': 'Truck or Passenger Vehicle Sport Van',
        'SW': 'Truck or Passenger Vehicle Station Wagon',
        'T': 'Motorcycle Dirt',
        'TB': 'Truck Tilt Cab',
        'TL': 'Truck Tilt Tandem or Motorcycle Trail/Dirt',
        'TM': 'Truck Tandem',
        'TN': 'Truck Tank',
        'TR': 'Motorcycle Trails or Truck Tractor (Gasoline)',
        'UT': 'Passenger Vehicle Utility, truck commonly registered as passenger or Truck Utility',
        'VC': 'Truck Van Camper',
        'VD': 'Truck Display Van',
        'VN': 'Truck Van',
        'VT': 'Truck Vanette (Includes Metro and Handy Van)',
        'VW': 'Truck Window Van',
        'WK': 'Truck Tow Truck Wrecker',
        'WW': 'Truck or Passenger Vehicle Wide-Wheel Wagon',
        'XT': 'Truck Travel-all',
        'YY': 'Truck Cutaway',
        '99': 'Unknown'
        }

# 2010 - later
VIN_BT['3B'] = 'Truck 3-Door Extended Cab/Chassis'
VIN_BT['3C'] = 'Truck 3-Door Extended Cab/Pickup'
VIN_BT['3P'] = 'Passenger Vehicle Coupe 3-Door'
VIN_BT['4B'] = 'Truck 4-Door Extended Cab/Chassis'
VIN_BT['4C'] = 'Truck 4-Door Extended Cab Pickup'
VIN_BT['C4'] = 'Passenger Vehicle Coupe 4-Door'
VIN_BT['IN'] = 'Passenger Vehicle Incomplete Passenger'
VIN_BT['LM'] = 'Truck Limousine'
VIN_BT['MW'] = 'Truck Maxi Wagon'
VIN_BT['P2'] = 'Passenger Vehicle 2- or 4-Passenger Low Speed'

####
# VIN Model Year
# last 2 digits
# VINMODYR

####
# Curb Weight
# base weight, only for Passenge Type Vehicles (VINTYPE='P')
# 1-9998: actual weight
VIN_WGT = {
        '0': 'Not Available',
        '9999': 'Unavailable'
        # derp
        }
####
# Wheelbase Short
# Shortest wheelbase respectively for manufactured model
# also appears in Parkwork as PWHLBS_SH
# 1-9998: actual value (inches)
WHLBS_SH = {
        '0000': 'Value Not Available from the VINA Programs',
        '9999': 'Value Not Coded'
        }

####
# Wheelbase Long
# also appears in Persn and parkwork as PWHLBS_LG
# 1-9998: actual value (inches)
WHLBS_LG = {
        '0000': 'Value Not Available from the VINA Program',
        '9999': 'Value Not Coded'
        }

####
# Fuel Code
# 1975-2009
FLDCD_TR = {
        'C': 'Gasoline Engine That Can Be Easily Converted to Gaseous-Powered Engine (Powered by Natural Gas, Propane, etc.)',
        'D': 'Diesel',
        'E': 'Electric',
        'F': 'Flexible Fuel',
        'G': 'Gas',
        'H': 'Ethanol Fuel Only',
        'M': 'Methanol Gas Only',
        'N': 'Compressed Natural Gas',
        'P': 'Propane',
        '9': 'Unknown'
        }

# 2010-later
FUELCODE = FLDCD_TR.copy()
FUELCODE['B'] = 'Electric and Gasoline Hybrid Engine'

####
# VIN Truck Series
# 3-character model series abbreviation
# SER_TR

####
# Truck Weight Rating
# Weight ranges for this truck of model year 1996 and later
# often coded as 9 for buses
# also appears in Person and Parkwork as PWGTCD_TR
WGTCD_TR = {
        '1': '6,000 lbs or less',
        '2': '6,001 - 10,000 lbs',
        '3': '10,001 - 14,000 lbs',
        '4': '14,001 - 16,000 lbs',
        '5': '16,001 - 19,500 lbs',
        '6': '19,501 - 26,000 lbs',
        '7': '26,001 - 33,000 lbs',
        '8': '33,001 and up',
        '9': 'Unknown'
        }

####
# Motorcycle Engine Displacement (CC)
# Piston bore measured in cubic centimeters
# MCYCL_DS

####
# VIN Length
# 99: unknown
# VIN_LNGT

####
# Original Tire Size
# manufacturer's original equipment specified tire size for series of this vehicle
# 6 characters
# TIRE_SIZE

####
# Cubic Inch Displacement
# manufacturer's cubic inch displacement of the engine pistons for this vehicle
# DISPLACE

####
# Number of Cylinders
# R : Rotary Engine
# CYLINDER

####
# Carburetion
# number of barrels for the engine of this vehicle or a code indicating
# that the engine is high-performance, fuel-injected, turbocharged, or
# electronically-controlled
# Also appears in Person and Parkwork as PCARBUR
# 0-8 Actual Number of Barrels
CARBUR = {
        'A': '1 Barrel, Lower HP',
        'B': '1 Barrel, Higher HP',
        'C': '1 Barrel, Turbo',
        'D': '1 Barrel, Turbo Low HP',
        'E': '1 Barrel, Turbo High HP',
        'F': 'Number of Barrels Not Specified, Fuel Injection',
        'G': '1 Barrel, Electronically controlled',
        'H': 'Number of Barrels Not Specified, High performance',
        'J': '2 Barrels, Lower HP',
        'K': '2 Barrels, Higher HP',
        'L': '2 Barrels, Turbo',
        'M': '2 Barrels, Turbo Low HP',
        'N': '2 Barrels, Turbo High HP',
        'P': '2 Barrels, Electronically controlled',
        'Q': 'Number of Barrels Not Specified, Electronically controlled',
        'R': '4 Barrels, Electronically controlled',
        'S': '4 Barrels, Lower HP',
        'T': '1, 2, or 4 Barrels, Turbo Fuel Injected',
        'U': '4 Barrels, Higher HP',
        'V': '4 Barrels, Turbo',
        'W': '4 Barrels, Turbo Low HP',
        'X': '4 Barrels, Turbo High HP',
        'Y': 'Number of Barrels Not Specified, Turbo',
        'Z': 'Number of Barrels Not Specified, Super Charged'
        }

####
# Number of Wheels/Drive Wheels
# 2 digits: 1st - number of axles, 2nd: number of drive axles * 2
# WHLDRWHL

####
# Truck Ton Rating
# Payload capacity of vehicle based on manufacturer's specifications
# 2 characters: single code - capacity rating; two codes - range of capacity rating
TON_RAT = {
        'A': .25,
        'B': .5,
        'C': .75,
        'D': 1.0,
        'E': 1.5,
        'F': 1.75,
        'G': 2.0,
        'H': 2.5,
        'I': 3.0,
        'J': 3.5,
        'K': 4.0,
        'L': 4.5,
        'M': 5.0,
        'N': 6.0,
        'O': 7.0,
        'P': 8.0,
        'Q': 9.0,
        'R': '10 and over'
        }

####
# Truck Shipping Weight
# Actual weight (lbs)
# TRK_WT

####
# Truck Shipping Weight Variance
# difference (coded in 100 lb increments) between shipping weight of shortest
# wheel base and longest wheel base for this truck model (e.g. 200 lb 
# difference appears as 02
# TRKWTVAR

####
# Truck VIN Restraint Type
# Also appears in Person and Parkwork as PVIN_REST
VIN_REST = {
        'A': 'Active (Manual) Belts',
        'B': 'Driver Front Air Bags/Belt System Unknown',
        'C': 'Dual Front Air Bags/Belt System Unknown',
        'D': 'Dual Front Air Bag/Passenger Side Passive Belts',
        'E': 'Dual Front Air Bags/Active Belts',
        'F': 'Dual Front Air Bags/Passive Belts',
        'G': 'Dual Air Bags Front and Side/Belts Unknown',
        'H': 'Dual Air Bags Front, Head and Sides/Belts Unknown',
        'I': 'Dual Air Bags Front, Head and Sides/Passive Belts',
        'J': 'Dual Air Bags Front and Sides/Passive Belts',
        'K': 'Dual Air Bags Front and Sides/Active Belts',
        'L': 'Dual Air Bags Front, Head and Sides/Active Belt',
        'M': 'Driver Front Air Bag/Passenger Side Active Belt',
        'N': 'If Unable to Determine',
        'P': 'Passive (Automatic) Belts',
        'R': 'Dual Air Bags Front and Side/Active Belts w/ Automatic Passenger Sensor',
        'S': 'Dual Air Bags Front, Head, and Side/Active Belts w/ Automatic Passenger Sensor',
        'T': 'Dual Air Bags Front/Active Belts/Rear Passenger Side Air Bag',
        'U': 'Dual Front Air Bags/Active Belts With Passenger Side Deactivation Cutoff Switch',
        'V': 'Dual Air Bags Front, Head and Side/Active Belts/Rear Dual Side Air Bags',
        'W': 'Dual Air Bags Front, Head and Side/Active Belts w/ Automatic Passenger Sensor/Rear Dual Side Airbags',
        'X': 'Dual Air Bags Front/Side Air Bag, Driver-Side Only/Active Belts',
        'Y': 'Dual Front and Side Air Bags With Passenger Deactivation; Active Belts',
        '3': 'Dual Front and Head Airbags with Passenger Sensor; Active Belts',
        '4': 'Dual Front Airbags With Passenger Sensor; Active Belts',
        '7': 'Dual Front, Side and Head Airbags, Rear Head Airbags; Active Belts',
        '9': 'Unknown'
        }

####
# Motorcycle Dry Weight
# 4 digit, weight in lbs
# MCYCL_WT

####
# Number of motorcycle engines
# Also appears in Person and Parkwork as PMCYCL_CY
MCYCL_CY = {
        '2': 'Two-stroke engine',
        '4': 'Four-stroke engine',
        'R': 'Rotary engine'
        }

####
# Fatalities in Vehicle (Number)
# Also appears in Parkwork as PDEATHS
# DEATHS

####
# Driver Drinking
# Alcohol data is often missing; this means acutal number of drinking drivers
# is often under-counted
DR_DRINK = {
        '0': False,
        '1': True,
        '9': 'Unknown'
        }

####
# Driver Presence
# Whether a driver was present in this vehicle at the onset of the 
# unstabilized situation
# 1975-77
DR_PRES = {
        '1': 'Driver Operated Vehicle',
        '2': 'No Driver',
        '9': 'Unknown'
        }

# 1978-2008
DR_PRES = {
        '1': 'Driver Operated Vehicle',
        '2': 'Driverless (No Driver)',
        '3': 'Driver Left Scene',
        '4': 'Motor Vehicle Not In-Transport (Parked/Stopped Off Roadway/Working Motor Vehicle/In Motion Outside Trafficway)',
        '9': 'Unknown'
        }

# 2009-later
DR_PRES = {
        '0': 'No Driver Present/Not Applicable',
        '1': True,
        '9': 'Unknown'
        }


