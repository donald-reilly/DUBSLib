
WHITE_SPACE_CHARS = [
"\n",
"\t",
" "
]

OPERATOR_CHARS = [
"!",
"\"",
"#",
"$",
"%",
"&",
"'",
"(",
")",
"*",
"+",
",",
"-",
".",
"/",
":",
";",
"<",
"=",
">",
"?",
"@",
"[",
"\\",
"]",
"^",
"_",
"`",
"{",
"|",
"}",
"~"
]

NUMBER_CHARS = [
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9"
]

LETTER_CHARS = [
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z"
]

WHITE_SPACE_ORDS = [ord(i) for i in WHITE_SPACE_CHARS]

OPERATOR_ORDS = [ord(i) for i in OPERATOR_CHARS]

NUMBER_ORDS = [ord(i) for i in NUMBER_CHARS]

LETTER_ORDS = [ord(i) for i in LETTER_CHARS]

WHITE_SPACE_DICT = dict(zip(WHITE_SPACE_CHARS, WHITE_SPACE_ORDS))

OPERATORS_DICT = dict(zip(OPERATOR_CHARS, OPERATOR_ORDS))

NUMBER_DICT = dict(zip(NUMBER_CHARS, NUMBER_ORDS))

LETTER_DICT = dict(zip(LETTER_CHARS, LETTER_ORDS))
