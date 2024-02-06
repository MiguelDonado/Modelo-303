import re


def to_number(number):
    return float(number.replace(".", "").replace(",", "."))


def check_match(input, string):
    try:
        result = input.search(string).group(1)
        if result:
            return to_number(result)
        else:
            return 0.00
    except AttributeError:
        return 0.00


########################################   PRIMERA PAGINA   ######################################################
fecha = re.compile(r"(\d\d-\d\d-\d\d\d\d)\s")
########################################   SEGUNDA PAGINA   ######################################################
# ------------------------------------------------------------------------
ejercicio = re.compile(r"Ejercicio\s(\d{4})\s", flags=re.MULTILINE)
periodo = re.compile(r"Per.odo\s(\d\w)\nNIF", flags=re.MULTILINE)
casilla_150 = re.compile(r"\s150(\s-?[0-9\.]+,\d\d)?\s151", flags=re.MULTILINE)
casilla_151 = re.compile(r"\s151(\s-?[0-9\.]+,\d\d)?\s152", flags=re.MULTILINE)
casilla_152 = re.compile(r"\s152(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_01 = re.compile(r"^01(\s-?[0-9\.]+,\d\d)?\s02", flags=re.MULTILINE)
casilla_02 = re.compile(r"\s02(\s-?[0-9\.]+,\d\d)?\s03", flags=re.MULTILINE)
casilla_03 = re.compile(r"\s03(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_153 = re.compile(r"\s153(\s-?[0-9\.]+,\d\d)?\s154", flags=re.MULTILINE)
casilla_154 = re.compile(r"\s154(\s-?[0-9\.]+,\d\d)?\s155", flags=re.MULTILINE)
casilla_155 = re.compile(r"\s155(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_04 = re.compile(r"^04(\s-?[0-9\.]+,\d\d)?\s05", flags=re.MULTILINE)
casilla_05 = re.compile(r"\s05(\s-?[0-9\.]+,\d\d)?\s06", flags=re.MULTILINE)
casilla_06 = re.compile(r"\s06(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_07 = re.compile(r"^07(\s-?[0-9\.]+,\d\d)?\s08", flags=re.MULTILINE)
casilla_08 = re.compile(r"\s08(\s-?[0-9\.]+,\d\d)?\s09", flags=re.MULTILINE)
casilla_09 = re.compile(r"\s09(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_10 = re.compile(r"\s10(\s-?[0-9\.]+,\d\d)?\s11", flags=re.MULTILINE)
casilla_11 = re.compile(r"\s11(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_12 = re.compile(r"\s12(\s-?[0-9\.]+,\d\d)?\s13", flags=re.MULTILINE)
casilla_13 = re.compile(r"\s13(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_14 = re.compile(r"\s14(\s-?[0-9\.]+,\d\d)?\s15", flags=re.MULTILINE)
casilla_15 = re.compile(r"\s15(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_156 = re.compile(r"\s156(\s-?[0-9\.]+,\d\d)?\s157", flags=re.MULTILINE)
casilla_157 = re.compile(r"\s157(\s-?[0-9\.]+,\d\d)?\s158", flags=re.MULTILINE)
casilla_158 = re.compile(r"\s158(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_16 = re.compile(r"\s16(\s-?[0-9\.]+,\d\d)?\s17", flags=re.MULTILINE)
casilla_17 = re.compile(r"\s17(\s-?[0-9\.]+,\d\d)?\s18", flags=re.MULTILINE)
casilla_18 = re.compile(r"\s18(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_19 = re.compile(r"^19(\s-?[0-9\.]+,\d\d)?\s20", flags=re.MULTILINE)
casilla_20 = re.compile(r"\s20(\s-?[0-9\.]+,\d\d)?\s21", flags=re.MULTILINE)
casilla_21 = re.compile(r"\s21(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_22 = re.compile(r"^22(\s-?[0-9\.]+,\d\d)?\s23", flags=re.MULTILINE)
casilla_23 = re.compile(r"\s23(\s-?[0-9\.]+,\d\d)?\s24", flags=re.MULTILINE)
casilla_24 = re.compile(r"\s24(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_25 = re.compile(r"\s25(\s-?[0-9\.]+,\d\d)?\s26", flags=re.MULTILINE)
casilla_26 = re.compile(r"\s26(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_27 = re.compile(r"\s27(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_28 = re.compile(r"\s28(\s-?[0-9\.]+,\d\d)?\s29", flags=re.MULTILINE)
casilla_29 = re.compile(r"\s29(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_30 = re.compile(r"\s30(\s-?[0-9\.]+,\d\d)?\s31", flags=re.MULTILINE)
casilla_31 = re.compile(r"\s31(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_32 = re.compile(r"\s32(\s-?[0-9\.]+,\d\d)?\s33", flags=re.MULTILINE)
casilla_33 = re.compile(r"\s33(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_34 = re.compile(r"\s34(\s-?[0-9\.]+,\d\d)?\s35", flags=re.MULTILINE)
casilla_35 = re.compile(r"\s35(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_36 = re.compile(r"\s36(\s-?[0-9\.]+,\d\d)?\s37", flags=re.MULTILINE)
casilla_37 = re.compile(r"\s37(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_38 = re.compile(r"\s38(\s-?[0-9\.]+,\d\d)?\s39", flags=re.MULTILINE)
casilla_39 = re.compile(r"\s39(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_40 = re.compile(r"\s40(\s-?[0-9\.]+,\d\d)?\s41", flags=re.MULTILINE)
casilla_41 = re.compile(r"\s41(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_42 = re.compile(r"\s42(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_43 = re.compile(r"\s43(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_44 = re.compile(r"\s44(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_45 = re.compile(r"\s45(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_46 = re.compile(r"\s46(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)

########################################   TERCERA PAGINA   ######################################################
# ------------------------------------------------------------------------
casilla_59 = re.compile(r"\s59(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_60 = re.compile(r"\s60(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_120 = re.compile(r"\s120(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_122 = re.compile(r"\s122(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_123 = re.compile(r"\s123(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_124 = re.compile(r"\s124(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_63 = re.compile(r"\s63(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_75 = re.compile(r"\s75(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_76 = re.compile(r"\s76(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_64 = re.compile(r"\s64(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_66 = re.compile(r"\s66(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_77 = re.compile(r"\s77(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_110 = re.compile(r"\s110(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_78 = re.compile(r"\s78(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_87 = re.compile(r"\s87(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_69 = re.compile(r"\s69(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
casilla_68 = 0.00
# ------------------------------------------------------------------------
casilla_70 = re.compile(r"\s70(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_71 = re.compile(r"\s71(\s-?[0-9\.]+,\d\d)?$", flags=re.MULTILINE)
# ------------------------------------------------------------------------
casilla_62 = re.compile(r"\s62(\s-?[0-9\.]+,\d\d)?\s63", flags=re.MULTILINE)
casilla_74 = re.compile(r"\s74(\s-?[0-9\.]+,\d\d)?\s75", flags=re.MULTILINE)


def extract_base_cuota_second_page(s):
    casillas = [
        casilla_150,
        casilla_151,
        casilla_152,
        casilla_01,
        casilla_02,
        casilla_03,
        casilla_153,
        casilla_154,
        casilla_155,
        casilla_04,
        casilla_05,
        casilla_06,
        casilla_07,
        casilla_08,
        casilla_09,
        casilla_10,
        casilla_11,
        casilla_12,
        casilla_13,
        casilla_14,
        casilla_15,
        casilla_156,
        casilla_157,
        casilla_158,
        casilla_16,
        casilla_17,
        casilla_18,
        casilla_19,
        casilla_20,
        casilla_21,
        ejercicio,
        periodo,
        casilla_22,
        casilla_23,
        casilla_24,
        casilla_25,
        casilla_26,
        casilla_27,
        casilla_28,
        casilla_29,
        casilla_30,
        casilla_31,
        casilla_32,
        casilla_33,
        casilla_34,
        casilla_35,
        casilla_36,
        casilla_37,
        casilla_38,
        casilla_39,
        casilla_40,
        casilla_41,
        casilla_42,
        casilla_43,
        casilla_44,
        casilla_45,
        casilla_46,
    ]
    lst = [
        (
            check_match(casilla, s)
            if casilla != ejercicio and casilla != periodo
            else casilla.search(s).group(1)
        )
        for casilla in casillas
    ]
    return lst


def extract_base_cuota_third_page(s):
    casillas = [
        casilla_59,
        casilla_60,
        casilla_120,
        casilla_122,
        casilla_123,
        casilla_124,
        casilla_63,
        casilla_75,
        casilla_76,
        casilla_64,
        casilla_66,
        casilla_77,
        casilla_110,
        casilla_78,
        casilla_87,
        casilla_69,
        casilla_68,
        casilla_70,
        casilla_71,
        casilla_62,
        casilla_74,
    ]
    lst = [check_match(casilla, s) for casilla in casillas]
    return lst
