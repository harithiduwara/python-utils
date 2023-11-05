import shutil
import os

source_dir = '/Volumes/HIduwara3/2023/2023-10-26'  
target_dir = '/Users/harithiduwara/Documents/photos/2023/2023-10-26' 

file_numbers_input = """
HSS09997,HSS09994,HSS09991,HSS09988,HSS09986,HSS09985,HSS09982,HSS09977,HSS09974,HSS09964,HSS09955,HSS09951,HSS09950,HSS09947,HSS09944,HSS09942,HSS09940,HSS09937,HSS09932,HSS09927,HSS09926,HSS09922,HSS09919,HSS09915,HSS09913,HSS09912,HSS09906,HSS09905,HSS09893,HSS09892,HSS09891,HSS09890,HSS09888,HSS09887,HSS09872,HSS09865,HSS09857,HSS09855,HSS09851,HSS09845,HSS09844,HSS09837,HSS09836,HSS09831,HSS09830,HSS09827,HSS09824,HSS09820,HSS09818,HSS09815,HSS09814,HSS09810,HSS09808,HSS09803,HSS09802,HSS09798,HSS09788,HSS09780,HSS09777,HSS09776,HSS09764,HSS09759,HSS09750,HSS09749,HSS09747,HSS09732,HSS09727,HSS09726,HSS09721,HSS09719,HSS09714,HSS09711,HSS09708,HSS09704,HSS09701,HSS09699,HSS09686,HSS09685,HSS09681,HSS09678,HSS09677,HSS09674,HSS09667,HSS09663,HSS09655,HSS09654,HSS09652,HSS09651,HSS09648,HSS09640,HSS09639,HSS09637,HSS09635,HSS09633,HSS09632,HSS09626,HSS09623,HSS09622,HSS09621,HSS09620,HSS09619,HSS09617,HSS09616,HSS09614,HSS09613,HSS09610,HSS09609,HSS09606,HSS09605,HSS09604,HSS09603,HSS09602,HSS09599,HSS09598,HSS09596,HSS09592,HSS09590,HSS09589,HSS09588,HSS09587,HSS09586,HSS09585,HSS09583,HSS09580,HSS09578,HSS09573,HSS09571,HSS09570,HSS09569,HSS09567,HSS09562,HSS09560,HSS09544,HSS09543,HSS09511,HSS09501,HSS09496,HSS09494,HSS09493,HSS09483,HSS09482,HSS09481,HSS09480,HSS09474,HSS09468,HSS09467,HSS09464,HSS09462,HSS09459,HSS09455,HSS09451,HSS09449,HSS09443,HSS09442,HSS09438,HSS09435,HSS09431,HSS09428,HSS09426,HSS09425,HSS09424,HSS09423,HSS09421,HSS09419,HSS09418,HSS09414,HSS09413,HSS09411,HSS09410,HSS09408,HSS09407,HSS09406,HSS09405,HSS09402,HSS09401,HSS09400,HSS09399,HSS09386,HSS09376,HSS09375,HSS09373,HSS09370,HSS09369,HSS09367,HSS09366,HSS09365,HSS09363,HSS09361,HSS09359,HSS09356,HSS09354,HSS09352,HSS09351,HSS09344,HSS09343,HSS09342,HSS09337,HSS09335,HSS09334,HSS09333,HSS09332,HSS09331,HSS09330,HSS09326,HSS09322,HSS09321,HSS09319,HSS09318,HSS09316,HSS09315,HSS09311,HSS09310,HSS09306,HSS09303,HSS009300,HSS09299,HSS09294,HSS09293,HSS09292,HSS09290,HSS09288,HSS09287,HSS09281,HSS09280,HSS09278,HSS09277,HSS09274,HSS09273,HSS09267,HSS09266,HSS09264,HSS09263,HSS09262,HSS09260,HSS09258,HSS09255,HSS09254,HSS09253,HSS09252,HSS09251,HSS09245,HSS09243,HSS09241,HSS09240,HSS09239,HSS09237,HSS09236,HSS09234,HSS09229,HSS09221,HSS09217,HSS09215,HSS09214,HSS09209,HSS09199,HSS09195,HSS09191,HSS09190,HSS09189,HSS09185,HSS09184,HSS09182,HSS09178,HSS09176,HSS09175,HSS09172,HSS09170,HSS09167,HSS09166,HSS09165,HSS09163,HSS09161,HSS09160,HSS09159,HSS09158,HSS09156,HSS09155,HSS00129,HSS00111,HSS00110,HSS00108,HSS00106,HSS00093,HSS00091,HSS00090,HSS00086,HSS00083,HSS00080,HSS00079,HSS00076,HSS00075,HSS00074,HSS00073,HSS00072,HSS00071,HSS00070,HSS00069,HSS00068,HSS00056,HSS00050,HSS00046,HSS00045,HSS00041,HSS00037,HSS00035,HSS00034,HSS00032,HSS00029,HSS00027,HSS00025,HSS00021,HSS00019,HSS00018,HSS00017,HSS00016,HSS00015,HSS00012,HSS00009,HSS00003,HSS00001
""".strip().split(",")

for file_number in file_numbers_input:
    file_number = f"{file_number}.ARW"
    source_file = os.path.join(source_dir, file_number)  
    target_file = os.path.join(target_dir, file_number) 

    try:
        shutil.copy2(source_file, target_file) 
        print(f"Copied: {source_file} to {target_file}")
    except FileNotFoundError:
        print(f"File not found: {source_file}")
    except shutil.SameFileError:
        print(f"Source and target are the same: {source_file}")

print("File copying complete.")
