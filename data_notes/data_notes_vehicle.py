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
V_CONFIG = {
        '0': 'Not Applicable, Not a Medium/Heavy Truck or Bus',
        '00': 'Not Applicable',
        '1': 'Single-Unit Truck (2 axles, 6 tires)',
        '2': 'Single-Unit Truck (3 or More axles)',
        '3': 'Truck/Trailers',
        '4': 'Truck Tractor (Bobtail, i.e. Trac
