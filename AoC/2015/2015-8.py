#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DESCRIPTION

--- Day 8: Matchsticks ---

Space on the sleigh is limited this year, and so Santa will be bringing
his list as a digital copy. He needs to know how much space it will take
up when stored.

It is common in many programming languages to provide a way to escape
special characters in strings. For example, C, JavaScript, Perl, Python,
and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of
characters in the code representation of the string literal and the
number of characters in the in-memory string itself.

For example:

"" is 2 characters of code (the two double quotes), but the string
contains zero characters.

"abc" is 5 characters of code, but 3 characters in the string data.

"aaa\"aaa" is 10 characters of code, but the string itself contains six
"a" characters and a single, escaped quote character, for a total of 7
characters in the string data.

"\x27" is 6 characters of code, but the string itself contains just one
- an apostrophe ('), escaped using hexadecimal notation.


Santa's list is a file that contains many double-quoted string literals,
one on each line. The only escape sequences used are \\ (which
represents a single backslash), \" (which represents a lone double-quote
character), and \x plus two hexadecimal characters (which represents a
single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of
characters of code for string literals minus the number of characters in
memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of
characters of string code (2 + 5 + 10 + 6 = 23) minus the total number
of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 -
11 = 12.


DISCUSSION
    As the desciption already states, several languages handle these
    literal strings basically the same way.

    Since I am doing this in python, here seems like a quick and simple
    strategy: If you just read the data file, for every line there, you
    can strip the trailing \n and the enclosing set of double quotes.
    You are then left with a string which is all the text in the input
    file (i.e., '\"' in the input file is a backslash (chr(92)) followed
    by a double-quote '"' (chr(34)).

    I can measure the length of these directly. I can also print out
    these strings and textuall put them into Python code then measure
    the length of those strings, where all the escapes are interpreted.

STRATEGY
    Read lines out of the text file, strip the whitespace (trialing
    newline), then measure length of string. Subtract two for the 
    '"'-sandwich, this is the "number of characters for string literal".

    Print out the lines, embed those into Python code, then measure the
    lengths of those strings.

"""

# program code is at bottom

LINES = [
"sjdivfriyaaqa\xd2v\"k\"mpcu\"yyu\"en",
"vcqc",
"zbcwgmbpijcxu\"yins\"sfxn",
"yumngprx",
"bbdj",
"czbggabkzo\"wsnw\"voklp\"s",
"acwt",
"aqttwnsohbzian\"evtllfxwkog\"cunzw",
"ugvsgfv",
"xlnillibxg",
"kexh\"pmi",
"syvugow",
"m\"ktqnw",
"yrbajyndte\\rm",
"f\"kak\x70sn\xc4kjri",
"yxthr",
"alvumfsjni\"kohg",
"trajs\x5brom\xf1yoijaumkem\"\"tahlzs",
"\"oedr\"pwdbnnrc",
"qsmzhnx\"",
"\"msoytqimx\\tbklqz",
"mjdfcgwdshrehgs",
"\"rivyxahf\"",
"ciagc\x04bp",
"xkfc",
"xrgcripdu\x4c\xc4gszjhrvumvz\"mngbirb",
"gvmae\"yiiujoqvr\"mkxmgbbut\"u",
"ih",
"ncrqlejehs",
"mkno\x43pcfdukmemycp",
"uanzoqxkpsksbvdnkji\"feamp",
"axoufpnbx\\ao\x61pfj\"b",
"dz\\ztawzdjy",
"ihne\"enumvswypgf",
"\"dgazthrphbshdo\\vuqoiy\"",
"dlnmptzt\\zahwpylc\\b\"gmslrqysk",
"mhxznyzcp",
"rebr\"amvxw\x5fmbnfpkkeghlntavj",
"lades\x47ncgdof\"\"jmbbk",
"dwxuis\xa5wdkx\\z\"admgnoddpgkt\\zs",
"g\\k\x27qsl\x34hwfglcdxqbeclt\xca\\",
"lhyjky\\m\"pvnm\\xmynpxnlhndmahjl",
"c\"uxabbgorrpprw\"xas\\vefkxioqpt",
"rfrvjxpevcmma\x71gtfipo",
"fgh\"kcwoqwfnjgdlzfclprg\"q",
"onxnwykrba",
"hkkg\x60f\"tjzsanpvarzgkfipl",
"\"aintes\"ofq\"juiaqlqxmvpe\\a",
"wiyczzs\"ciwk",
"mfqeu",
"v\xe1z\x7ftzalmvdmncfivrax\\rjwq",
"k\"vtg",
"exhrtdugeml\xf0",
"behnchkpld",
"mhgxy\"mfcrg\xc5gnp\"\"osqhj",
"rlvjy",
"awe",
"ctwy",
"vt",
"\x54t",
"zugfmmfomz",
"cv\"cvcvfaada\x04fsuqjinbfh\xa9cq\xd2c\"d",
"oj",
"xazanf\"wbmcrn",
"\\\\zkisyjpbzandqikqjqvee",
"dpsnbzdwnxk\\v",
"sj\"tuupr\\oyoh",
"myvkgnw\x81q\xaaokt\\emgejbsyvxcl\\\xee",
"ejeuqvunjcirdkkpt\"nlns",
"twmlvwxyvfyqqzu",
"\"xwtzdp\x98qkcis\"dm\\\"ep\"xyykq",
"vvcq\\expok",
"wgukjfanjgpdjb",
"\"mjcjajnxy\\dcpc",
"wdvgnecw\\ab\x44klceduzgsvu",
"dqtqkukr\"iacngufbqkdpxlwjjt",
"\"xj\"\x66qofsqzkoah",
"nptiwwsqdep",
"gsnlxql\x30mjl",
"yeezwokjwrhelny\"",
"bjauamn\\izpmzqqasid",
"tvjdbkn\"tiziw\x82r",
"w",
"xwoakbbnjnypnaa\xa9wft\"slrmoqkl",
"vwxtnlvaaasyruykgygrvpiopzygf\"vq",
"qdancvnvmhlmpj\\isdxs",
"xzc\\elw",
"b\"wxeqvy\"qf\"g\xcaoklsucwicyw\"dovr",
"yomlvvjdbngz\"rly\"afr",
"bfb\"x\"aweuwbwmoa\x13\"t\"zhr",
"\"dmfoxb\"qvpjzzhykt\xd2\"\"ryhxi",
"psqef\"yu\\qiflie\"\x79w",
"arzewkej\"lqmh\\sayyusxxo\\",
"vuvvp",
"hc\"lg\x6bcpupsewzklai\"l",
"cjdfygc\"auorqybnuqghsh\x10",
"j",
"wqjexk\"eyq\\lbroqhk\\dqzsqk",
"dws\"ru\"dvxfiwapif\"oqwzmle",
"agcykg\\jt\\vzklqjvknoe",
"kksd\"jmslja\\z\"y\\b\xaagpyojct",
"nnpipxufvbfpoz\"jno",
"dtw",
"xlolvtahvgqkx\\dgnhj\\spsclpcxv\\",
"mxea\\mbjpi",
"lgbotkk\"zmxh\\\\qji\"jszulnjsxkqf",
"lwckmhwhx\"gmftlb\x91am",
"xxdxqyxth",
"\"lmqhwkjxmvayxy",
"tf",
"qy",
"wdqmwxdztax\"m\"\x09\x11xdxmfwxmtqgwvf",
"\xcbnazlf\"ghziknszmsrahaf",
"e\x6aupmzhxlvwympgjjpdvo\"kylfa",
"\x81vhtlillb\xactgoatva",
"dvnlgr",
"f",
"xg\xfacwizsadgeclm",
"vnnrzbtw\"\\prod\\djbyppngwayy\"",
"lrt\xf4jahwvfz",
"aqpnjtom\"ymkak\\dadfybqrso\\fwv",
"gz\"aac\"mrbk\"ktommrojraqh",
"wycamwoecsftepfnlcdkm",
"nrhddblbuzlqsl\x9cben",
"vckxhyqkmqmdseazcykrbysm",
"sil\xbbtevmt\"gvrvybui\"faw\"j",
"cjex\\tp\x45pzf",
"asjobvtxszfodgf\"ibftg",
"gkyjyjdrxdcllnh\"sjcibenrdnxv",
"oswsdpjyxpbwnqbcpl\"yrdvs\\zq",
"\"\"tyowzc\\fycbp\"jbwrbvgui",
"cbpcabqkdgzmpgcwjtrchxp",
"iyrzfh\x45gw\"fdlfpiaap\x31xqq",
"evgksznidz",
"b\\w\\",
"loufizbiy\x57aim\"bgk",
"qjfyk",
"g\"anmloghvgr\x07zwqougqhdz",
"usbbmwcxd\\bdgg",
"htitqcpczml",
"eke\\cqvpexqqk\"to\"tqmljrpn\xe6lji\"",
"g\xd2ifdsej",
"h\"sk\"haajajpagtcqnzrfqn\xe6btzo",
"wfkuffdxlvm\\cvlyzlbyunclhmpp",
"myaavh\"spue",
"hqvez\x68d\"eo\"eaioh",
"s\"qd\"oyxxcglcdnuhk",
"ilqvar",
"srh",
"puuifxrfmpc\"bvalwi\x2blu\\",
"yywlbutufzysbncw\\nqsfbhpz\"mngjq",
"zbl\\jfcuop",
"hjdouiragzvxsqkreup\\",
"qi",
"ckx\\funlj\xa7ahi",
"k",
"ufrcnh\"ajteit",
"cqv\"bgjozjj\x60x\xa8yhvmdvutchjotyuz",
"hkuiet\"oku\x8cfhumfpasl",
"\"\\sbe\x4d",
"vhknazqt",
"eyyizvzcahgflvmoowvs\\jhvygci",
"kki\x3ewcefkgtjap\"xtpxh\"lzepoqj",
"wvtk",
"\"ynet",
"zh\\obk\"otagx\x59txfzf",
"ocowhxlx\xe6zqg\x63wx\\tclkhq\\vmaze",
"w\"cf",
"qpniprnrzrnvykghqnalr",
"jctcqra\"\x05dhlydpqamorqjsijt\\xjdgt",
"sig",
"qhlbidbflwxe\"xljbwls\x20vht",
"irmrebfla\xefsg\"j",
"nep",
"hjuvsqlizeqobepf",
"guzbcdp\"obyh",
"\"mjagins\xf9tqykaxy\"",
"knvsdnmtr\"zervsb",
"hzuy",
"zza\"k\"buapb\\elm\xfeya",
"lrqar\"dfqwkaaqifig\"uixjsz",
"\"azuo\x40rmnlhhluwsbbdb\x32pk\\yu\"pbcf",
"dplkdyty",
"rfoyciebwlwphcycmguc",
"ivnmmiemhgytmlprq\\eh",
"lhkyzaaothfdhmbpsqd\\yyw",
"tnlzifupcjcaj",
"\\qiyirsdrfpmu\\\x15xusifaag",
"\\lcomf\\s",
"uramjivcirjhqcqcg",
"kkbaklbxfxikffnuhtu\xc6t\"d",
"n\xefai",
"\"toy\"bnbpevuzoc\"muywq\"gz\"grbm",
"\"muu\\wt",
"\\srby\"ee",
"erf\"gvw\"swfppf",
"pbqcgtn\"iuianhcdazfvmidn\\nslhxdf",
"uxbp",
"up\\mgrcyaegiwmjufn",
"nulscgcewj\\dvoyvhetdegzhs\"",
"masv\"k\\rzrb",
"qtx\x79d\"xdxmbxrvhj",
"fid\\otpkgjlh\"qgsvexrckqtn\xf4",
"tagzu",
"bvl\\\"noseec",
"\\xgicuuh",
"w\"a\"npemf",
"sxp",
"nsmpktic\x8awxftscdcvijjobnq\"gjd",
"uks\"\"jxvyvfezz\"aynxoev\"cuoav",
"m",
"lkvokj",
"vkfam\"yllr\"q\x92o\x4ebecnvhshhqe\\",
"efdxcjkjverw",
"lmqzadwhfdgmep\x02tzfcbgrbfekhat",
"cpbk\x9azqegbpluczssouop\x36ztpuoxsw",
"cqwoczxdd\"erdjka",
"cwvqnjgbw\\fxdlby",
"mvtm",
"lt\"bbqzpumplkg",
"ntd\xeeuwweucnuuslqfzfq",
"y\xabl\"dbebxjrlbmuoo\\\x1au",
"qjoqx\\a",
"pu\"ekdnfpmly\xbago\"",
"fjhhdy",
"arl",
"xcywisim\"bwuwf\"\"raepeawwjub",
"pbe",
"dbnqfpzyaumxtqnd\xc5dcqrkwyop",
"ojv\x40vtkwgkqepm\x8bzft\\vedrry",
"wggqkfbwqumsgajqwphjec\"mstxpwz",
"zjkbem",
"icpfqxbelxazlls",
"pvpqs\\abcmtyielugfgcv\"tjxapxqxnx",
"oqddwlvmtv\"\x39lyybylfb\"jmngnpjrdw",
"gisgbve",
"\"aglg",
"y\"\"ss\xafvhxlrjv",
"qbgqjsra",
"ihshbjgqpdcljpmdwdprwloy",
"djja\\wcdn\"svkrgpqn\"uz\"hc\x43hj",
"cbjm",
"pnn",
"pqvh\"noh",
"\"\\fdktlp",
"ncea",
"pqgzphiyy",
"\xbedovhxuipaohlcvkwtxwmpz\"ckaif\"r",
"arjuzbjowqciunfwgxtph\"vlhy\"n",
"c",
"nrpdxunulgudqzlhtae",
"iefheu\"uru\"",
"aqijysxuijud\"np\\opbichhudil\xbesum",
"pfpevmtstl\"lde\"bzr\"vspdxs",
"vparfbdjwvzsocpnzhp",
"g\x4ffxaarafrsjthq\\\xc1rw",
"ng\\rqx\\gwpzucbh\xafl",
"rw\"nf\\dna",
"jkkeahxurxla\\g\xb3czrlsyimmwcwthr",
"twaailoypu\"oas\"kpuuyedlaw\\\xb0vzt",
"hznex\\gdiqvtugi",
"imdibsunjeswhk",
"ta\\icileuzpxro\"cfmv\"mzp",
"coykr\x57luiysucfaflmilhlehmvzeiepo",
"u\x3dfh\xd4yt",
"piw\x1bz\"eowy\"vfk\"wqiekw",
"gan\"y",
"p\"bevidoazcznr\"hddxuuq\"",
"bwzucczznutbxe",
"z\"viqgyqjisior\\iecosmjbknol",
"dmlpcglcfkfsctxydjvayhymv\x3c\\gp",
"bfvkqrintbbvgfv",
"xlzntrgdck\"cprc\xadczyarbznqmuhxyuh",
"uqdxnuwioc\"kdytxq\\ig",
"xrafmucpmfi",
"vr\"hltmfrge",
"eonf\"nt\\wtcnsocs",
"j\xb7xoslyjeyjksplkqixncgkylkw",
"njw\"pefgfbez\x9axshdmplxzquqe",
"di\x58bvptfsafirpc",
"l\x1fkco",
"x",
"mprndo\"n",
"psegit",
"svbdnkkuuqs\"sqxu\"oqcyz\"aizashk",
"cwkljukxer\\\"\\nff\"esjwiyaoy",
"ilxrkgbjjxpvhdtq\"cpiuoofdnkpp",
"hlngi\"ulxep\\qohtmqnqjb\"rkgerho",
"gxws\"bcgm\"p",
"bv\"mds\\zhfusiepgrz\\b\x32fscdzz",
"l\xfampwtme\x69qvxnx\"\"\xc4jruuymjxrpsv",
"qqmxhrn",
"xziq\\\x18ybyv\x9am\"neacoqjzytertisysza",
"aqcbvlvcrzceeyx\\j\"\"x",
"yjuhhb",
"\x5em\"squulpy",
"dpbntplgmwb",
"utsgfkm\\vbftjknlktpthoeo",
"ccxjgiocmuhf\"ycnh",
"lltj\"kbbxi",
]

import sys
import pdb  # http://pymotw.com/2/pdb/


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = '2015-8-input.txt'


def main():
    lines = open(INPUT_FILENAME, 'r').readlines()
    lengths = [len(line.strip()) for line in lines]
    code_length = sum(lengths)

    # print dump
    # for line in lines:
    #     print(line.strip() + ',')

    print()
    print(f"total code length is: {code_length}")

    total_store_length = sum([len(line) for line in LINES])
    print(f"total store length is: {total_store_length}")
    print(f"difference: {code_length - total_store_length}")

    """
    total code length is: 6310
    total store length is: 4977
    difference: 1333
    """
    # 1333 verified correct for Part 1 on 2022Jul26


if __name__ == '__main__':
    main()


# EOF

