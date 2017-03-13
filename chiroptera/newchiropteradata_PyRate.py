#!/usr/bin/env python
from numpy import * 


data_1=[array([34.190257]),
array([48.165688,50.505598]),
array([54.376835,54.052195]),
array([15.272106]),
array([15.243955,15.600943,21.838877,14.08066,4.612152,4.808474]),
array([9.123417,2.2977,2.77194,9.363374,4.230879,0.009204,0.010788,0.001446,0.056364,0.032185,0.112595,0.099299,0.047686,0.078544,0.055264,0.0548,0]),
array([2.285868,2.516785]),
array([46.913397,40.0246]),
array([45.52684,54.824653,39.671527,39.666702]),
array([48.714415,54.435395]),
array([48.881019]),
array([48.290296]),
array([33.691176,30.383212]),
array([15.90012]),
array([0.031306,0.114583,0]),
array([0.00766,0.118888,0.042208,0]),
array([18.720816]),
array([54.013661]),
array([0.019927,0]),
array([0.403942,0.438779,0.214994,0.4072,0]),
array([19.906199,22.918886,19.611152,11.990794,13.085716]),
array([0.045507,0.013183,0.010271,0]),
array([19.387165]),
array([55.409777]),
array([0.008243,0]),
array([42.381999]),
array([36.298648,36.395071]),
array([33.741059]),
array([13.076942,4.670214,46.747154,43.904092,41.836794,43.995188,40.897764,41.099212,41.68208,45.001482,43.966635,45.329162,38.483451,36.650019,36.993072,33.927088,34.524589,35.781093,36.923517,37.186796,25.269405,14.942056,11.644751,17.99691,10.217211,16.011063,14.822631,12.794021,14.923054,14.541,14.337754,15.401613,14.056852,1.1894,1.029119,0.356901,0.847242,0.769784,0.03906,1.120809,1.759741,2.574935,13.033209,8.311638,16.522942,3.333096,0.786493,14.17072,12.700984,13.594224,1.276495,1.997724,2.168017,1.186292,0.85701,2.039358,1.266281,2.391474,2.534688,1.267055,0.7003,15.353595,1.313214,0.477713,0.777194,6.206653,3.287596,3.084567,1.068508,2.666698,2.826777,3.593336,1.754292,2.425105,1.286413,1.932616,0.715285,0.737985,0.199184,0.312691,42.274111,0.873875,13.448274,13.16252,15.292387,46.696903,13.236179,19.851075,40.948808,39.572883,0.156292,0.766924,0.530327,1.847328,0.394275,2.849364,3.118943,56.051551,0.002304,0.003108,0.001123,0.012508,0.207217,0.396715,13.838356,11.167074,6.745501,6.59853,12.742427,55.974455,0.924714,4.23033,41.884907,27.371048,32.791546,42.717335,0.519523,0.454275,48.812944,44.174606,0.119557,0.010287,0.004995,0.522473,0.037338,0.118269,0.01949,0.012509,0.0824,3.553909,4.951968,0.005748,15.30962,0.574789,0.024978,50.250822,29.384401,13.171505,25.127251,23.061049,21.620961,21.294284,40.956799,39.459668,49.893519,0.055301,0]),
array([0.057275,0.706345,0]),
array([0.116742,0]),
array([27.491445]),
array([0.100504,0]),
array([0.99062,1.404246,2.729952,0.761354,0]),
array([0.073327,2.465619,0]),
array([0.004916,0.086477,0.082822,0]),
array([0.179134,0.080875,0.060214,0.072657,0.117428,0.058045,0.039688,0]),
array([33.880269]),
array([30.766235]),
array([16.003957]),
array([55.232324]),
array([3.377913,0.010784,0]),
array([24.37035,32.941579,30.921223,43.509301,15.621756,28.329097,22.955243,8.313519]),
array([53.971869,51.468844,44.282501,47.925463]),
array([55.539621,53.882392]),
array([7.2816,6.457087,3.435782,0.011392,0.005139,1.694608,1.816172,1.043852,0.676349,3.29124,3.183374,3.902043,3.972363,5.704296,0.30331,0.243749,8.698877,6.360099,0.618398,0.701272,3.79975,0.044076,0.083641,6.351014,0.01137,0.020076,0.045257,0.092276,9.897262,0]),
array([17.986365,16.284916]),
array([13.087934,13.903621,10.150205]),
array([3.145385,2.082808,0.966542,0.371827,1.291826,0.787429,1.412127,0.077046,0.114607,0.008307,0.080019,0.033172,0.077157,0.005868,1.524949,0.10256,0.026183,0.091693,0.436767,0.068651,0.117107,0.062385,0.005062,0.014126,0.03057,0.406601,0.468457,0.105994,0.013303,0.089371,0.311254,0.03529,0.076146,1.515065,0.824445,0.002092,0.022159,0]),
array([3.051985,1.609897,0]),
array([0.001991,0.002364,0.010127,0.001975,12.9633,0]),
array([0.001738,0.124321,0]),
array([3.037496,0.005128,0.005502,0.028456,0.005874,0]),
array([0.00998,0.006584,0]),
array([15.542059]),
array([53.000572]),
array([50.554675]),
array([6.406513,6.025703,8.05583,34.220319,34.681028,35.085655,14.452806,10.82598,15.472203,30.572714,40.2487,40.995441,31.165301]),
array([0.144603,0.006716,2.298235,2.834669,3.47806,18.094311,40.882674,34.460088,37.539002,36.562437,0.775035,0.83855,0.005546,0.12003,0.05916,15.229079,14.794702,0]),
array([16.067989]),
array([18.411491]),
array([9.08941]),
array([11.831673]),
array([37.011415,36.431094,34.463518,35.023197,36.857557,36.396053,30.50639]),
array([30.75793]),
array([41.049271,39.554272,37.861169,35.194895,34.822663,35.317714,35.844918,36.190938,28.649208,34.144534,34.273477]),
array([2.553324]),
array([53.181704,54.308023,53.84843]),
array([15.333659]),
array([55.998593,48.155606,54.690368,43.449203]),
array([50.930126]),
array([51.784237,49.218604]),
array([49.394197]),
array([54.895972]),
array([16.268029]),
array([31.300596]),
array([13.041677]),
array([39.652396]),
array([45.783033]),
array([2.742273,0.016828,0.04947,0]),
array([12.441671,3.146405,4.581202,4.556767,0.401353,0.002151,0]),
array([3.206346,0.12894,0.010663,0.104391,2.6892,0.06576,0.091155,0.117789,1.195257,1.465606,0]),
array([0.832707,1.187564,0]),
array([2.595144,3.482798,2.01498]),
array([1.407714,0]),
array([0.075366,0.118379,0.017823,0.062919,0.058733,0]),
array([2.830456]),
array([0.005552,0]),
array([0.018182,0]),
array([0.125554,0]),
array([0.12507,0]),
array([8.182171,17.831625,1.255272,1.065918,0.045525,0.438374,0.476673,0.608806,13.346558,0]),
array([4.170148,5.044471]),
array([0.043775,0.015207,0.009987,0]),
array([43.635036,44.955263]),
array([1.741243,0.058866,15.522364,4.427151,0]),
array([18.102116]),
array([13.162998]),
array([9.579396,8.478319,5.120466]),
array([3.676749,11.966152,14.181835]),
array([46.458364,47.051662,41.239754,35.490405,12.195099,0.622467,1.323694,39.804565,40.367744,38.620301,39.621802,4.319993,4.02772,29.24874,34.97122,35.157845,40.500668,46.306568,41.286681,40.731804,32.66012,37.01004,0]),
array([50.94301]),
array([0.004729,0.001576,0.009224,0.077225,0]),
array([0.555825,0.2414,3.39758,3.469331,0.006114,4.446247,0.714761,1.644713,1.91252,1.574665,0.214255,0.246321,0.971678,0.105391,0.660715,0.638983,0.501633,0.008468,0.016055,0.044195,1.409172,0.078527,0.101965,0]),
array([10.603802,13.482865]),
array([16.695467]),
array([11.315963]),
array([13.065949,10.843874]),
array([31.857475]),
array([32.702335]),
array([14.766327,6.864748,9.718342,37.503504,6.384853]),
array([0.006159,0.007471,0]),
array([0.010313,0.011054,0.011243,0]),
array([0.010361,0]),
array([25.322474,32.432092]),
array([0.046004,0.082874,0.008992,0.008397,0.123537,0]),
array([0.004459,18.238772,0]),
array([17.844836]),
array([2.334233,4.43569,0.078507,0.093863,0]),
array([6.637649,0.119262,19.315628,16.227254,14.865194,10.805025,12.862465,7.374929,3.413952,10.184292,3.222351,0.557727,3.892535,0.326757,0.009082,0.001808,0.132627,0.812649,4.071333,6.44916,4.414163,0.720182,0.666585,4.723613,4.57258,4.871223,1.999542,2.309436,4.511619,4.625939,3.649778,3.575621,3.221042,3.810611,0.5689,1.007062,1.211603,2.363068,2.030303,0.927178,0.348698,0.043389,2.09326,1.063824,9.122356,2.879332,2.681753,3.018531,2.688929,3.1588,2.822428,2.947063,1.353195,0.993559,2.340696,1.12621,0.984195,1.251595,1.280913,1.850839,0.947184,0.52613,0.465637,0.639908,0.763442,0.393124,0.537188,0.22193,0.554577,0.425286,0.234733,0.343587,0.204452,0.667505,0.641795,0.533885,0.206291,0.157987,0.356374,1.207569,0.218302,0.843316,0.549149,0.376233,0.323288,32.517377,1.817202,0.989684,2.336844,1.013377,1.963361,1.73473,2.51428,2.203521,0.815822,1.603353,1.937237,0.941439,19.310504,0.030767,0.016769,0.024039,0.050134,0.019201,0.013356,0.055418,6.318936,7.527971,16.402256,0.264861,0.525194,0.132469,0.245792,0.751465,0.208143,0.243267,0.444919,0.417121,0.627166,2.0457,1.69029,2.40606,0.115853,0.038133,0.030802,0.076781,0.069198,0.088949,0.069563,0.002431,0.002327,9.567689,8.950447,10.513244,8.14254,1.719721,26.985447,0.083424,0.063276,0.032726,0.049016,3.658897,4.425139,4.543766,1.460945,0.017463,0.05266,0.046031,0.055663,0.046604,0.050925,0.08215,0.059987,0.119093,0.062349,0.011571,0.048444,0.019331,0.05622,0.120098,0.068876,0.023188,0.789118,0.044693,0.077249,0.063311,1.435283,0.04623,0.02246,0.123645,0.05567,0.038676,2.244327,1.466412,0.111913,1.685722,29.576819,0.004942,0.090951,4.908254,14.006537,1.236559,2.039571,33.413072,0.125933,0.050293,0]),
array([1.650313,1.041545,1.162865,0.261888,0.04593,0.071319,0.085434,0.084273,0.04504,0.086578,0.091813,0]),
array([7.803765,8.673716,5.216173]),
array([1.760078,1.21582,0.135749,0.099093,0.915115,0.115809,0.083531,0.049613,0]),
array([4.164702]),
array([1.574396,0.112397,0.058336,0]),
array([1.267677,2.425694,0]),
array([0.822603,0.059607,0.067212,0.107808,0.070316,0.032615,0.093828,0.075034,0]),
array([11.53627]),
array([1.208213,1.509927,0.074065,0.017648,0.117391,0.188321,0]),
array([1.567644,0.112632,0.050617,0]),
array([0.965361,0.080179,0.002937,0.089387,0.115143,0]),
array([11.36863]),
array([0.079086,0.056116,0.03209,0.022637,0.526868,0]),
array([18.732719,18.994547]),
array([17.452745,16.161247,17.406868,16.232548]),
array([32.121206]),
array([0.010378,0]),
array([42.886878,35.895394]),
array([0.006899,15.712864,0]),
array([8.557184,7.184944]),
array([0.001602,0]),
array([12.071645,15.738197,12.616401]),
array([12.622618,16.065592]),
array([0.412126,0.171879,0.514574,0]),
array([3.514152,0]),
array([52.370463]),
array([0.006661,2.39707,3.106925,4.502715,0]),
array([0.01626,0.123101,0]),
array([16.325626]),
array([2.470503,2.07196,0]),
array([33.558272,27.439672]),
array([51.055016]),
array([55.173984,40.625668]),
array([45.851933,45.644098,42.452737,40.571715,39.375947]),
array([29.186455,34.456417,35.552815,37.852272]),
array([36.307119,36.177005,36.944817]),
array([38.376264,33.920754,35.960941,32.866861,34.337451,33.560228,35.600368]),
array([8.506904,9.301313,9.368078,10.760156,10.777347,13.932614,15.528465]),
array([13.593823]),
array([15.800424]),
array([28.725783,31.925112]),
array([30.229325]),
array([0.081507,0]),
array([31.344317,10.948729,16.806395,24.463481,44.708772]),
array([0.01183,0]),
array([15.916641,20.126785,18.500168]),
array([0.003552,0.007454,0.005885,0]),
array([6.29872,0.006668,6.999729,6.969176,8.026169,0.267918,0.458197,0.044575,0.080121,0.091676,0.069774,0.704719,0.055913,0]),
array([0.011271,0]),
array([0.488871,2.511007,0.585402,0.125266,1.716689,0.807723,0.098975,2.629112,0.087002,0.10637,0.034471,1.646719,0.050819,0.119825,1.181732,0.112088,0.986579,0.051998,0]),
array([7.648188,4.76874,1.575905,3.959681,2.602452,1.732382,8.017265,8.560106,0.397871,8.128017,0.04789,0.070357,0.022137,0.609887,0.033486,1.289277,1.984293,0.795612,0]),
array([0.043063,0]),
array([1.280318,0.897823,0]),
array([0.685438,0.24101,0.520332,1.820792,0.247463,0.098821,0]),
array([4.641549,4.121627,1.386501,0]),
array([0.583927,0]),
array([0.094784,0]),
array([0.048794,0.054907,0]),
array([10.262513]),
array([14.898287]),
array([13.054229]),
array([16.6302]),
array([51.499637]),
array([28.441349]),
array([6.921535,6.118753]),
array([0.009288,0]),
array([37.670483]),
array([18.703252,16.545854]),
array([41.107249,25.432694]),
array([0.005159,1.276612,1.450697,2.015058,3.432399,2.924092,2.69588,4.683083,4.017798,5.248976,3.395197,1.539873,2.206662,0.796098,5.848957,0.988088,0.674716,0.304412,0.397159,0.979656,1.756857,2.684698,3.140787,37.917418,36.084629,0.388556,0.536687,14.99185,0.084382,0.103545,0.053528,16.520841,2.018483,0]),
array([18.794346]),
array([4.474052,4.149858,14.810738,10.318891,7.801038,4.998451,12.961333]),
array([0.953645,1.578165,3.048561,1.18402,0.974267,2.206565,1.946831,2.007954,2.212999,0.251379,2.955744,0]),
array([2.412179,1.552972,1.454217,2.649262,2.703526,3.196514,0.779994,0.232396,2.232899,0.497518,0.09994,1.217683,0.581445,0.031639,0.053204,0.047336,0.084793,0]),
array([3.675663,4.860915,1.291369,16.806177,8.845181,10.162555,7.965614,13.572232,0]),
array([5.919072]),
array([36.416046,37.488669,33.957669,36.70289,34.260736,37.856676]),
array([12.829788]),
array([18.778314]),
array([13.92006]),
array([0.011253,0.024345,0]),
array([0.00261,0]),
array([17.984089,18.102326]),
array([0.010844,0.002243,0.00493,0.911092,1.44785,1.017551,0.001875,0.001528,0]),
array([33.190395]),
array([0.049102,0]),
array([0.003337,0.522484,2.941257,15.419894,0]),
array([13.353788]),
array([11.66824]),
array([37.145229,35.18627,40.502209,40.522653,35.592476,36.199517,37.335668,41.006443,38.944361,31.473919,31.476067,29.673862,38.656632]),
array([29.626343]),
array([35.820335,37.99625,34.995349,38.102504,36.681594,28.463229]),
array([0.002935,0.008646,0]),
array([18.008466]),
array([41.798521]),
array([3.505986,2.069054,0.006086,10.002815,17.656262,36.810567,35.663251,33.981573,11.72321,37.575636,1.87116,0.003922,0.098707,0.027397,0.011229,0]),
array([0.03943,0]),
array([0.032901,0.073876,0.01059,0.004631,0.012692,0.044628,0.00135,0.189102,0.009317,0]),
array([13.519111]),
array([0.020015,0]),
array([13.454972]),
array([16.588932]),
array([45.913104]),
array([0.008484,1.810439,3.120101,17.841058,20.889367,13.642045,0]),
array([16.295268]),
array([16.20067]),
array([16.043996]),
array([0.001768,0.004928]),
array([0.002377,0.086982,0]),
array([0.006296,0]),
array([0.063442,0]),
array([31.191991]),
array([32.218297,30.435494,31.022006]),
array([44.671592,35.050377,28.529234,38.994758,38.530944,38.451901,37.676897,35.136875,34.025412,34.995338,36.795532]),
array([38.640423,33.919123,34.152884,33.314075,28.763008,29.658749]),
array([43.538778]),
array([2.892165,0.633745,0.256757,3.867766,1.82683,4.287993,0.62365,1.314943,0]),
array([0.067633,0.34323,0]),
array([14.844335,33.841642,21.820804,29.884882,24.083456,14.080416,15.275313,13.77723,17.117635,5.28867,17.818759,10.815178,10.046474,1.488847,10.482142,32.198274,0.756163,20.40631,4.610753,12.018095,12.584273,12.265107,12.655361,15.983591,16.493473,0.032875,12.009538,14.600204,2.361138,0]),
array([37.738842,25.556633,30.280822,23.46029]),
array([34.339678,34.941031]),
array([45.311431,39.624172]),
array([35.52667]),
array([35.107113]),
array([18.107793])
]

d=[data_1]
names=[ 'newchiropteradata_1']
def get_data(i): return d[i]
def get_out_name(i): return  names[i]
taxa_names=['Aegyptonycteris_knightae','Ageina','Ageina_tobieni','Ancenycteris','Antrozous','Antrozous_pallidus','Anzanycteris_anzensis','Archaeonycteridae','Archaeonycteris','Archaeonycteris_brailloni','Archaeonycteris_praecursor','Archaeonycteris_storchi','Archaeopteropus_transiens','Archerops_annectens','Artibeus','Artibeus_jamaicensis','Asellia_mariaetheresae','Australonycteris_clarkae','Balantiopteryx_io','Barbastella','Brachipposideros','Brachyphylla','Brevipalatus_mcculloughi','Cambaya_complexus','Carollia','Cecilionycteris_prisca','Chadronycteris_rabenae','Chibanycteris_herberti','Chiroptera','Chrotopterus_auritus','Cubanycteris_silvai','Cuvierimops','Desmodus','Desmodus_archaeodaptes','Desmodus_draculae','Desmodus_rotundus','Desmodus_stocki','Dhofarella_sigei','Dhofarella_thaleri','Diclidurus','Dizzya_exsultans','Eidolon','Emballonuridae','Eochiroptera','Eppsinycteris_anglica','Eptesicus','Eptesicus_aurelianensis','Eptesicus_campanensis','Eptesicus_fuscus','Eptesicus_praeglacialis','Eumops','Eumops_glaucinus','Eumops_perotis','Glossophaga','Glossophaginae','Hassianycteris','Hassianycteris_kumari','Hipposideridae','Hipposideros','Hipposideros_(Brachipposideros)_dechaseauxi','Hipposideros_(Pseudorhinolophus)_bouziguensis','Hipposideros_bernardsigei','Hipposideros_felix','Hipposideros_morloti','Hipposideros_omani','Hipposideros_schlosseri','Histiotus_stocki','Honrovits_tsuwape','Ia','Icaronycteris','Icaronycteris_index','Icaronycteris_menui','Icaronycteris_sigei','Jaegeria_cambayensis','Karstala_silva','Khonsunycteris_aegypticus','Kiotomops_lopezi','Lapichiropteryx','Lapichiropteryx_xiei','Lasionycteris_noctivagans','Lasiurus','Lasiurus_borealis','Lasiurus_cinereus','Lasiurus_fossilis','Lasiurus_golliheri','Lasiurus_intermedius','Lasiurus_seminolus','Leptonycteris','Leptonycteris_nivalis','Lonchophylla','Lophostoma_silvicolum','Macroderma','Macroderma_koppa','Macrotus','Matthesia','Megaderma','Megaderma_franconica','Megaderma_lugdunensis','Megaderma_vireti','Megadermatidae','Microchiroptera','Microchiropteryx_folieae','Micronycteris','Miniopterus','Miniopterus_fossilis','Miomyotis_floridanus','Miophyllorhina_riversleighensis','Miostrellus_risgoviensis','Mixopteryx_dubia','Mixopteryx_weithoferi','Molossidae','Molossops','Molossus','Mops','Mormoopidae','Mormoops','Mormopterus','Mormopterus_barrancae','Murina','Myotis','Myotis_austroriparius','Myotis_boyeri','Myotis_grisescens','Myotis_helleri','Myotis_keenii','Myotis_leibi','Myotis_lucifugus','Myotis_murinoides','Myotis_myotis','Myotis_thysanodes','Myotis_velifer','Myotis_yumanensis','Mystacina','Mystacina_miocenalis','Mystacinidae','Natalidae','Natalus','Necromantis','Noctilio_albiventris','Noctilio_lacrimaelunaris','Noctilio_leporinus','Notonycteris_magdalenensis','Notonycteris_sucharadeus','Nyctalus','Nycteridae','Nycterididae','Nycteris','Nycticeius_humeralis','Nyctinomus','Nyctophilus','Oligomyotis','Onychonycteris_finneyi','Palaeochiropterygidae','Palaeochiropteryx','Palaeophyllophora','Palaeophyllophora_oltina','Palaeophyllophora_quercyi','Paleptesicus','Paleptesicus_priscus','Palynephyllum_antimaster','Philisis','Philisis_sphingis','Phyllops_silvai','Phyllostomatidae','Phyllostomidae','Phyllostominae','Phyllostomus','Pipistrellus','Pipistrellus_hesperus','Pipistrellus_subflavus','Plecotus','Plecotus_(Corynorhinus)','Plecotus_alleganiensis','Plecotus_auritus','Plecotus_crassidens','Plecotus_rafinesquii','Plecotus_tetralophodon','Plecotus_townsendii','Plionycteris','Potamonycteris_biperforatus','Potamops_mascahehenes','Primonatalus_prattae','Protonycteris_gunnelli','Pseudorhinolophus','Pteropidae','Pteropus','Qarunycteris_moerisae','Rhinolophidae','Rhinolophoidea','Rhinolophus','Rhinolophus_dehmi','Rhinolophus_delphinensis','Rhinolophus_euryale','Rhinolophus_ferrumequinum','Rhinolophus_grivensis','Rhinolophus_grivensis_lissiensis','Rhinolophus_priscus','Rhinolophus_yongyuthi','Rhinonycteris','Rhizomops_mengraii','Rhogeessa','Rhynchonycteris','Riversleigha_williamsi','Rousettus','Saharaderma_pseudovampyrus','Scotomanes','Scotophilus','Shanwangia','Shanwangia_unexpectata','Stehlinia','Stehlinia_bonisi','Stehlinia_gracilis','Sturnira','Suaptenos_whitei','Tachypteron_franzeni','Tadarida','Tadarida_aurispinosa','Tadarida_brasiliensis','Tadarida_engesseri','Tadarida_laticaudata','Tadarida_leptognatha','Tadarida_rusingae','Tanzanycteris_mannardi','Taphozous','Thyroptera','Thyroptera_lavali','Thyroptera_robusta','Tonatia','Trachops_cirrhosus','Triaenops','Tylonycteris','Vampyravus_orientalis','Vaylatsia_prisca','Vespertiliavus','Vespertiliavus_gracilis','Vespertiliavus_lapradei','Vespertilio','Vespertilio_murinus','Vespertilionidae','Vespertilionoidea','Wallia','Wallia_scalopidens','Witwatia_eremicus','Witwatia_schlosseri','Xenorhinos_halli']
def get_taxa_names(): return taxa_names
