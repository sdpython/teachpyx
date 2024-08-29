import unittest
from teachpyx.ext_test_case import ExtTestCase
from teachpyx.practice.rues_paris import (
    bellman,
    kruskal,
    possible_edges,
    distance_haversine,
    graph_degree,
    eulerien_extension,
    distance_paris,
    euler_path,
    connected_components,
)


class TestRueParis(ExtTestCase):
    vertices = [
        (48.873361200000005, 2.3236609),
        (48.8730454, 2.3235788),
        (48.876246800000004, 2.3318573000000002),
        (48.875252700000004, 2.3322956),
        (48.8735712, 2.3109766),
        (48.872916700000005, 2.3104976),
        (48.8433599, 2.3415645),
        (48.8438889, 2.3392425),
        (48.898623, 2.3656344000000002),
        (48.898654400000005, 2.3666086),
        (48.878685000000004, 2.3514280000000003),
        (48.879387400000006, 2.3516223000000003),
        (48.872115900000004, 2.3392093000000003),
        (48.8722422, 2.3382998),
        (48.843958400000005, 2.4134804),
        (48.8418774, 2.4136059000000003),
        (48.8632179, 2.2878296000000002),
        (48.863393, 2.2874957),
        (48.8781848, 2.3522114000000003),
        (48.8777526, 2.3511422),
        (48.849360700000005, 2.3317293),
        (48.849249500000006, 2.3309420000000003),
        (48.8556727, 2.3366922000000003),
        (48.8562785, 2.3366043000000003),
        (48.8535047, 2.3615469),
        (48.8535813, 2.3614117),
        (48.8639445, 2.3755101),
        (48.8648776, 2.3748282),
        (48.8551694, 2.261925),
        (48.855523100000006, 2.2621554),
        (48.891942400000005, 2.3223583000000003),
        (48.8917226, 2.3230341),
        (48.828755300000005, 2.3166122000000002),
        (48.829231400000005, 2.3173138),
        (48.8492437, 2.2750144000000003),
        (48.8494856, 2.2742921000000003),
        (48.894308900000006, 2.3594273),
        (48.894249200000004, 2.3594347),
        (48.8640516, 2.3624232000000003),
        (48.864375900000006, 2.3618135000000002),
        (48.8494077, 2.4151688),
        (48.851955200000006, 2.4151274000000003),
        (48.8601674, 2.3820656000000002),
        (48.8610946, 2.3811391),
        (48.8533142, 2.3459001),
        (48.8537722, 2.344293),
        (48.8423542, 2.2941794),
        (48.8404633, 2.2957232000000003),
        (48.836452200000004, 2.2592016),
        (48.8371057, 2.2601667),
        (48.876521200000006, 2.3127781),
        (48.8776163, 2.3125533000000003),
        (48.849343700000006, 2.3682517),
        (48.8515298, 2.3692419),
        (48.8936245, 2.3300976),
        (48.893475800000004, 2.329429),
        (48.842168300000004, 2.2855643000000003),
        (48.842397500000004, 2.2850610000000002),
        (48.8785497, 2.3505446),
        (48.8794977, 2.3508043),
        (48.851695600000006, 2.3487173),
        (48.8514083, 2.3493394000000003),
        (48.8848719, 2.2979169),
        (48.8851079, 2.2978681),
        (48.86544850000001, 2.3687925),
        (48.8652585, 2.3680487),
        (48.8384706, 2.3507640000000003),
        (48.838631500000005, 2.3515752),
        (48.8475101, 2.4064010000000002),
        (48.8476775, 2.4064302),
        (48.8403009, 2.3460075000000002),
        (48.8398089, 2.3472132),
        (48.896738500000005, 2.3384891000000003),
        (48.8967758, 2.3384491),
        (48.8360859, 2.3003709000000003),
        (48.8367408, 2.299553),
        (48.829905800000006, 2.3341749000000003),
        (48.830201300000006, 2.3348945000000003),
        (48.81933, 2.3619721),
        (48.819208700000004, 2.3620485),
        (48.893085500000005, 2.3157935000000003),
        (48.8929655, 2.3159988),
        (48.8817426, 2.3738127),
        (48.881476600000006, 2.3743903),
        (48.871239900000006, 2.3605841),
        (48.871501800000004, 2.3603519),
        (48.8494262, 2.3956660000000003),
        (48.8498279, 2.395527),
        (48.882198900000006, 2.3044874),
        (48.8824861, 2.3055082000000002),
        (48.892683600000005, 2.3400773000000004),
        (48.891423200000006, 2.3396854),
        (48.828216600000005, 2.3170147),
        (48.828375, 2.3171796000000002),
        (48.8771033, 2.4069115),
        (48.8772473, 2.4067931000000002),
        (48.8404803, 2.3794622000000003),
        (48.8405416, 2.3791428000000003),
        (48.8708554, 2.2850300000000003),
        (48.8698787, 2.2852855),
        (48.878974400000004, 2.3557592),
        (48.8782082, 2.3555521),
        (48.8599399, 2.2907052),
        (48.860304500000005, 2.2911493000000003),
        (48.8679081, 2.3866252),
        (48.8682901, 2.3863284),
        (48.827594100000006, 2.32099),
        (48.8261705, 2.3195845),
        (48.8445667, 2.2870145),
        (48.8449425, 2.2860621),
        (48.8389649, 2.3585651000000003),
        (48.838711800000006, 2.3577637),
        (48.876016, 2.3401507),
        (48.8766649, 2.3394591),
        (48.835332400000006, 2.3733283000000003),
        (48.8354979, 2.3731241),
        (48.8453074, 2.3982187),
        (48.84526210000001, 2.3987593),
        (48.864641000000006, 2.3035632),
        (48.8639207, 2.2989008),
        (48.874107900000006, 2.3397429),
        (48.8747843, 2.3397888),
        (48.862969, 2.3418717),
        (48.8623776, 2.3415815),
        (48.823074500000004, 2.3253825000000004),
        (48.8221222, 2.3250976000000003),
        (48.8856551, 2.2916608000000003),
        (48.8860898, 2.2924402),
        (48.826483100000004, 2.3418208000000003),
        (48.8270119, 2.3420461),
        (48.8877511, 2.3063884000000003),
        (48.8889805, 2.304241),
        (48.8761869, 2.3194496),
        (48.875665500000004, 2.3196156),
        (48.8777215, 2.3315215),
        (48.8776105, 2.3309402),
        (48.837042000000004, 2.2565999000000003),
        (48.837166, 2.2565265),
        (48.8581033, 2.3820198),
        (48.8593835, 2.3828233),
        (48.832689200000004, 2.2883536),
        (48.8334051, 2.289441),
        (48.891664000000006, 2.3349628),
        (48.8918514, 2.3335172),
        (48.8423742, 2.3535862),
        (48.842243, 2.3536228),
        (48.8539302, 2.3648526000000003),
        (48.853958500000005, 2.3647523),
        (48.8454689, 2.2824441),
        (48.845120200000004, 2.2830738),
        (48.8410742, 2.2546347),
        (48.8410893, 2.2550578000000003),
        (48.868929300000005, 2.3146814),
        (48.8693837, 2.3132517000000004),
        (48.876280900000005, 2.3583099),
        (48.876194700000006, 2.3582784),
        (48.876635500000006, 2.3486800000000003),
        (48.8767458, 2.3472677),
        (48.851683200000004, 2.3420153000000004),
        (48.8511144, 2.3415342000000003),
        (48.8790045, 2.3147799),
        (48.8794399, 2.3142755),
        (48.8616691, 2.3448132),
        (48.8617945, 2.3442988000000002),
        (48.835680800000006, 2.3112781),
        (48.836246, 2.3102979),
        (48.855284000000005, 2.2895261000000002),
        (48.8561612, 2.2931029),
        (48.824318500000004, 2.3636902),
        (48.8249517, 2.3624289000000003),
        (48.8628093, 2.2918135),
        (48.862751100000004, 2.2920106000000002),
        (48.8681819, 2.398056),
        (48.868529800000005, 2.3992063000000003),
        (48.8356738, 2.3249401),
        (48.8353905, 2.3257185000000002),
        (48.8624171, 2.3103990000000003),
        (48.8624275, 2.3110419),
        (48.871344, 2.3177128000000002),
        (48.871694000000005, 2.318445),
        (48.8774226, 2.349085),
        (48.8771841, 2.3489544),
        (48.87938320000001, 2.3370294),
        (48.879117900000004, 2.3369039000000003),
        (48.8821905, 2.3011631),
        (48.883269500000004, 2.3019395),
        (48.8673537, 2.3515468),
        (48.867840900000004, 2.3517371000000002),
        (48.848900300000004, 2.3404672),
        (48.847503, 2.3408323),
        (48.866788, 2.3100655000000003),
        (48.8668318, 2.3102252),
        (48.8591447, 2.3749638),
        (48.8587694, 2.3737956000000002),
        (48.8730794, 2.2970525),
        (48.8731894, 2.297116),
        (48.8534328, 2.2973824),
        (48.853697700000005, 2.2969404),
        (48.829909900000004, 2.3677045000000003),
        (48.8293831, 2.3686139),
    ]
    edges = [
        (
            0,
            1,
            1,
            (48.873361200000005, 2.3236609),
            (48.8730454, 2.3235788),
            0.0003262974869682125,
        ),
        (
            2,
            3,
            1,
            (48.876246800000004, 2.3318573000000002),
            (48.875252700000004, 2.3322956),
            0.0010864353179087373,
        ),
        (
            4,
            5,
            2,
            (48.8735712, 2.3109766),
            (48.872916700000005, 2.3104976),
            0.0008110556392718516,
        ),
        (
            6,
            7,
            1,
            (48.8433599, 2.3415645),
            (48.8438889, 2.3392425),
            0.0023814963783302164,
        ),
        (
            8,
            9,
            2,
            (48.898623, 2.3656344000000002),
            (48.898654400000005, 2.3666086),
            0.0009747059043630242,
        ),
        (
            10,
            11,
            1,
            (48.878685000000004, 2.3514280000000003),
            (48.879387400000006, 2.3516223000000003),
            0.0007287786014985378,
        ),
        (
            12,
            13,
            1,
            (48.872115900000004, 2.3392093000000003),
            (48.8722422, 2.3382998),
            0.000918227607948986,
        ),
        (
            14,
            15,
            1,
            (48.843958400000005, 2.4134804),
            (48.8418774, 2.4136059000000003),
            0.0020847808637880117,
        ),
        (
            16,
            17,
            1,
            (48.8632179, 2.2878296000000002),
            (48.863393, 2.2874957),
            0.00037702681602255083,
        ),
        (
            18,
            19,
            2,
            (48.8781848, 2.3522114000000003),
            (48.8777526, 2.3511422),
            0.0011532499642313606,
        ),
        (
            20,
            21,
            1,
            (48.849360700000005, 2.3317293),
            (48.849249500000006, 2.3309420000000003),
            0.000795114287382352,
        ),
        (
            22,
            23,
            1,
            (48.8556727, 2.3366922000000003),
            (48.8562785, 2.3366043000000003),
            0.0006121438148041292,
        ),
        (
            24,
            25,
            2,
            (48.8535047, 2.3615469),
            (48.8535813, 2.3614117),
            0.00015539176297330173,
        ),
        (
            26,
            27,
            2,
            (48.8639445, 2.3755101),
            (48.8648776, 2.3748282),
            0.0011557089685536276,
        ),
        (
            28,
            29,
            2,
            (48.8551694, 2.261925),
            (48.855523100000006, 2.2621554),
            0.0004221230270947142,
        ),
        (
            30,
            31,
            1,
            (48.891942400000005, 2.3223583000000003),
            (48.8917226, 2.3230341),
            0.0007106459596741995,
        ),
        (
            32,
            33,
            1,
            (48.828755300000005, 2.3166122000000002),
            (48.829231400000005, 2.3173138),
            0.0008478878286659365,
        ),
        (
            34,
            35,
            1,
            (48.8492437, 2.2750144000000003),
            (48.8494856, 2.2742921000000003),
            0.0007617302015802999,
        ),
        (
            36,
            37,
            2,
            (48.894308900000006, 2.3594273),
            (48.894249200000004, 2.3594347),
            6.015687824477596e-05,
        ),
        (
            38,
            39,
            1,
            (48.8640516, 2.3624232000000003),
            (48.864375900000006, 2.3618135000000002),
            0.0006905827828738192,
        ),
        (
            40,
            41,
            1,
            (48.8494077, 2.4151688),
            (48.851955200000006, 2.4151274000000003),
            0.0025478363781901324,
        ),
        (
            42,
            43,
            1,
            (48.8601674, 2.3820656000000002),
            (48.8610946, 2.3811391),
            0.0013107639337423486,
        ),
        (
            44,
            45,
            1,
            (48.8533142, 2.3459001),
            (48.8537722, 2.344293),
            0.0016710877924281285,
        ),
        (
            46,
            47,
            1,
            (48.8423542, 2.2941794),
            (48.8404633, 2.2957232000000003),
            0.0024410696938019956,
        ),
        (
            48,
            49,
            1,
            (48.836452200000004, 2.2592016),
            (48.8371057, 2.2601667),
            0.0011655386136882784,
        ),
        (
            50,
            51,
            1,
            (48.876521200000006, 2.3127781),
            (48.8776163, 2.3125533000000003),
            0.0011179351725326468,
        ),
        (
            52,
            53,
            1,
            (48.849343700000006, 2.3682517),
            (48.8515298, 2.3692419),
            0.002399901925075645,
        ),
        (
            54,
            55,
            2,
            (48.8936245, 2.3300976),
            (48.893475800000004, 2.329429),
            0.0006849362379076621,
        ),
        (
            56,
            57,
            2,
            (48.842168300000004, 2.2855643000000003),
            (48.842397500000004, 2.2850610000000002),
            0.0005530312197335353,
        ),
        (
            58,
            59,
            1,
            (48.8785497, 2.3505446),
            (48.8794977, 2.3508043),
            0.0009829283239392353,
        ),
        (
            60,
            61,
            1,
            (48.851695600000006, 2.3487173),
            (48.8514083, 2.3493394000000003),
            0.0006852369663133512,
        ),
        (
            62,
            63,
            1,
            (48.8848719, 2.2979169),
            (48.8851079, 2.2978681),
            0.00024099261399570973,
        ),
        (
            64,
            65,
            1,
            (48.86544850000001, 2.3687925),
            (48.8652585, 2.3680487),
            0.0007676838151226447,
        ),
        (
            66,
            67,
            1,
            (48.8384706, 2.3507640000000003),
            (48.838631500000005, 2.3515752),
            0.0008270031741179077,
        ),
        (
            68,
            69,
            1,
            (48.8475101, 2.4064010000000002),
            (48.8476775, 2.4064302),
            0.00016992763165754094,
        ),
        (
            70,
            71,
            2,
            (48.8403009, 2.3460075000000002),
            (48.8398089, 2.3472132),
            0.0013022198316724116,
        ),
        (
            72,
            73,
            2,
            (48.896738500000005, 2.3384891000000003),
            (48.8967758, 2.3384491),
            5.469268689390239e-05,
        ),
        (
            74,
            75,
            1,
            (48.8360859, 2.3003709000000003),
            (48.8367408, 2.299553),
            0.0010477854837711283,
        ),
        (
            76,
            77,
            1,
            (48.829905800000006, 2.3341749000000003),
            (48.830201300000006, 2.3348945000000003),
            0.0007779102840302752,
        ),
        (
            78,
            79,
            1,
            (48.81933, 2.3619721),
            (48.819208700000004, 2.3620485),
            0.00014335497898282511,
        ),
        (
            80,
            81,
            2,
            (48.893085500000005, 2.3157935000000003),
            (48.8929655, 2.3159988),
            0.00023779842304041672,
        ),
        (
            82,
            83,
            1,
            (48.8817426, 2.3738127),
            (48.881476600000006, 2.3743903),
            0.0006359070372292929,
        ),
        (
            84,
            85,
            2,
            (48.871239900000006, 2.3605841),
            (48.871501800000004, 2.3603519),
            0.0003500120712191077,
        ),
        (
            86,
            87,
            1,
            (48.8494262, 2.3956660000000003),
            (48.8498279, 2.395527),
            0.0004250692767046083,
        ),
        (
            88,
            89,
            1,
            (48.882198900000006, 2.3044874),
            (48.8824861, 2.3055082000000002),
            0.001060432213768252,
        ),
        (
            90,
            91,
            1,
            (48.892683600000005, 2.3400773000000004),
            (48.891423200000006, 2.3396854),
            0.0013199218802638546,
        ),
        (
            92,
            93,
            1,
            (48.828216600000005, 2.3170147),
            (48.828375, 2.3171796000000002),
            0.0002286538213084464,
        ),
        (
            94,
            95,
            1,
            (48.8771033, 2.4069115),
            (48.8772473, 2.4067931000000002),
            0.00018642574929344586,
        ),
        (
            96,
            97,
            1,
            (48.8404803, 2.3794622000000003),
            (48.8405416, 2.3791428000000003),
            0.00032522922685364927,
        ),
        (
            98,
            99,
            2,
            (48.8708554, 2.2850300000000003),
            (48.8698787, 2.2852855),
            0.0010095658175694848,
        ),
        (
            100,
            101,
            1,
            (48.878974400000004, 2.3557592),
            (48.8782082, 2.3555521),
            0.0007936956910564454,
        ),
        (
            102,
            103,
            1,
            (48.8599399, 2.2907052),
            (48.860304500000005, 2.2911493000000003),
            0.0005745937434427083,
        ),
        (
            104,
            105,
            1,
            (48.8679081, 2.3866252),
            (48.8682901, 2.3863284),
            0.00048375018346404227,
        ),
        (
            106,
            107,
            1,
            (48.827594100000006, 2.32099),
            (48.8261705, 2.3195845),
            0.0020005167357479573,
        ),
        (
            108,
            109,
            1,
            (48.8445667, 2.2870145),
            (48.8449425, 2.2860621),
            0.0010238610257259065,
        ),
        (
            110,
            111,
            2,
            (48.8389649, 2.3585651000000003),
            (48.838711800000006, 2.3577637),
            0.0008404174974367317,
        ),
        (
            112,
            113,
            1,
            (48.876016, 2.3401507),
            (48.8766649, 2.3394591),
            0.0009483574062568779,
        ),
        (
            114,
            115,
            2,
            (48.835332400000006, 2.3733283000000003),
            (48.8354979, 2.3731241),
            0.0002628457532435862,
        ),
        (
            116,
            117,
            2,
            (48.8453074, 2.3982187),
            (48.84526210000001, 2.3987593),
            0.0005424946543511399,
        ),
        (
            118,
            119,
            1,
            (48.864641000000006, 2.3035632),
            (48.8639207, 2.2989008),
            0.004717711929527524,
        ),
        (
            120,
            121,
            1,
            (48.874107900000006, 2.3397429),
            (48.8747843, 2.3397888),
            0.0006779555811369695,
        ),
        (
            122,
            123,
            2,
            (48.862969, 2.3418717),
            (48.8623776, 2.3415815),
            0.0006587639941564931,
        ),
        (
            124,
            125,
            1,
            (48.823074500000004, 2.3253825000000004),
            (48.8221222, 2.3250976000000003),
            0.0009940036720269252,
        ),
        (
            126,
            127,
            1,
            (48.8856551, 2.2916608000000003),
            (48.8860898, 2.2924402),
            0.0008924284004890405,
        ),
        (
            128,
            129,
            1,
            (48.826483100000004, 2.3418208000000003),
            (48.8270119, 2.3420461),
            0.0005747952070065542,
        ),
        (
            130,
            131,
            1,
            (48.8877511, 2.3063884000000003),
            (48.8889805, 2.304241),
            0.002474419350069803,
        ),
        (
            132,
            133,
            2,
            (48.8761869, 2.3194496),
            (48.875665500000004, 2.3196156),
            0.0005471873171013459,
        ),
        (
            134,
            135,
            1,
            (48.8777215, 2.3315215),
            (48.8776105, 2.3309402),
            0.0005918029148282243,
        ),
        (
            136,
            137,
            1,
            (48.837042000000004, 2.2565999000000003),
            (48.837166, 2.2565265),
            0.00014409566266867946,
        ),
        (
            138,
            139,
            1,
            (48.8581033, 2.3820198),
            (48.8593835, 2.3828233),
            0.0015114642867070992,
        ),
        (
            140,
            141,
            1,
            (48.832689200000004, 2.2883536),
            (48.8334051, 2.289441),
            0.0013019030570644572,
        ),
        (
            142,
            143,
            1,
            (48.891664000000006, 2.3349628),
            (48.8918514, 2.3335172),
            0.0014576961686158724,
        ),
        (
            144,
            145,
            1,
            (48.8423742, 2.3535862),
            (48.842243, 2.3536228),
            0.00013620939761850324,
        ),
        (
            146,
            147,
            2,
            (48.8539302, 2.3648526000000003),
            (48.853958500000005, 2.3647523),
            0.00010421602564026223,
        ),
        (
            148,
            149,
            1,
            (48.8454689, 2.2824441),
            (48.845120200000004, 2.2830738),
            0.0007198012086660956,
        ),
        (
            150,
            151,
            1,
            (48.8410742, 2.2546347),
            (48.8410893, 2.2550578000000003),
            0.00042336936592088766,
        ),
        (
            152,
            153,
            1,
            (48.868929300000005, 2.3146814),
            (48.8693837, 2.3132517000000004),
            0.0015001738065953281,
        ),
        (
            154,
            155,
            1,
            (48.876280900000005, 2.3583099),
            (48.876194700000006, 2.3582784),
            9.177521451741075e-05,
        ),
        (
            156,
            157,
            1,
            (48.876635500000006, 2.3486800000000003),
            (48.8767458, 2.3472677),
            0.001416600642382841,
        ),
        (
            158,
            159,
            1,
            (48.851683200000004, 2.3420153000000004),
            (48.8511144, 2.3415342000000003),
            0.0007449769459546838,
        ),
        (
            160,
            161,
            2,
            (48.8790045, 2.3147799),
            (48.8794399, 2.3142755),
            0.0006663276371280349,
        ),
        (
            162,
            163,
            1,
            (48.8616691, 2.3448132),
            (48.8617945, 2.3442988000000002),
            0.0005294643708504993,
        ),
        (
            164,
            165,
            1,
            (48.835680800000006, 2.3112781),
            (48.836246, 2.3102979),
            0.0011314782719947791,
        ),
        (
            166,
            167,
            1,
            (48.855284000000005, 2.2895261000000002),
            (48.8561612, 2.2931029),
            0.0036827948734616056,
        ),
        (
            168,
            169,
            1,
            (48.824318500000004, 2.3636902),
            (48.8249517, 2.3624289000000003),
            0.001411318507635477,
        ),
        (
            170,
            171,
            1,
            (48.8628093, 2.2918135),
            (48.862751100000004, 2.2920106000000002),
            0.00020551313826585387,
        ),
        (
            172,
            173,
            1,
            (48.8681819, 2.398056),
            (48.868529800000005, 2.3992063000000003),
            0.0012017589192520163,
        ),
        (
            174,
            175,
            1,
            (48.8356738, 2.3249401),
            (48.8353905, 2.3257185000000002),
            0.000828351042734914,
        ),
        (
            176,
            177,
            1,
            (48.8624171, 2.3103990000000003),
            (48.8624275, 2.3110419),
            0.0006429841133339727,
        ),
        (
            178,
            179,
            1,
            (48.871344, 2.3177128000000002),
            (48.871694000000005, 2.318445),
            0.0008115521178599309,
        ),
        (
            180,
            181,
            1,
            (48.8774226, 2.349085),
            (48.8771841, 2.3489544),
            0.0002719165497001383,
        ),
        (
            182,
            183,
            2,
            (48.87938320000001, 2.3370294),
            (48.879117900000004, 2.3369039000000003),
            0.0002934865243945523,
        ),
        (
            184,
            185,
            2,
            (48.8821905, 2.3011631),
            (48.883269500000004, 2.3019395),
            0.0013292998006503502,
        ),
        (
            186,
            187,
            1,
            (48.8673537, 2.3515468),
            (48.867840900000004, 2.3517371000000002),
            0.0005230467761128879,
        ),
        (
            188,
            189,
            1,
            (48.848900300000004, 2.3404672),
            (48.847503, 2.3408323),
            0.0014442109610448733,
        ),
        (
            190,
            191,
            1,
            (48.866788, 2.3100655000000003),
            (48.8668318, 2.3102252),
            0.00016559749394223043,
        ),
        (
            192,
            193,
            1,
            (48.8591447, 2.3749638),
            (48.8587694, 2.3737956000000002),
            0.0012270050244400786,
        ),
        (
            194,
            195,
            1,
            (48.8730794, 2.2970525),
            (48.8731894, 2.297116),
            0.00012701279463055954,
        ),
        (
            196,
            197,
            2,
            (48.8534328, 2.2973824),
            (48.853697700000005, 2.2969404),
            0.0005153018629915703,
        ),
        (
            198,
            199,
            1,
            (48.829909900000004, 2.3677045000000003),
            (48.8293831, 2.3686139),
            0.0010509646045432734,
        ),
    ]

    def test_algo(self):
        edges = self.edges
        max_segment = max(e[-1] for e in edges)
        possibles = possible_edges(edges, max_segment / 8)
        init = bellman(edges, allow=lambda e: e in possibles)
        init = bellman(edges, allow=lambda e: e in possibles, init=init)
        added = kruskal(edges, init)
        d = graph_degree(edges + added)
        allow = sorted([k for k, v in d.items() if v % 2 == 1])
        allow = set(allow)
        init = bellman(
            edges,
            allow=lambda e: e in possibles or e[0] in allow or e[1] in allow,
            init=init,
        )
        added = kruskal(edges, init)
        d = graph_degree(edges + added)
        allow = sorted([k for k, v in d.items() if v % 2 == 1])
        self.assertEmpty(list(allow))

    def test_algo2(self):
        edges = self.edges
        edges = edges[:1000]
        added = eulerien_extension(edges, alpha=1 / 8)
        assert len(added) > 0

    def test_algo_euler4(self):
        edges = self.edges

        vertices = {}
        for e in edges:
            for i in range(2):
                _ = e[i]
                p = e[i + 3]
                vertices[_] = p

        connex = connected_components(edges)
        v = [v for k, v in connex.items()]
        mi, ma = min(v), max(v)

        while mi != ma:
            edges.append(
                (
                    mi,
                    ma,
                    2,
                    vertices[mi],
                    vertices[ma],
                    distance_haversine(*(vertices[mi] + vertices[ma])),
                )
            )

            connex = connected_components(edges)
            v = [v for k, v in connex.items()]
            mi, ma = min(v), max(v)

        added = eulerien_extension(edges, distance=distance_paris)

        graph_degree(edges + added)

        path = euler_path(edges, added)
        alls = edges + added
        self.assertEqual(len(alls), len(path))

    def test_algo3(self):
        edges = self.edges
        added = eulerien_extension(edges, distance=distance_paris)
        self.assertNotEmpty(added)


if __name__ == "__main__":
    unittest.main(verbosity=2)
