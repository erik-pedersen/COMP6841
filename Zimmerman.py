#!/usr/bin/env python3

code = "FGAFAAAVXADGAVXVADADDVDDDVGAVXVDXDVDDFAFDXGXGDDGAVFDVXVAAFXGDADXVDDXDAVXXVAAAVDAVXDAVVGDDXAVDGDXGXVXVDVFVVAFDXAVAFVXDXVDFDAFXAVVVFAVAFVVVVVADGXVAXAFDGGXFXAFAVVADGDFVFAXVDVXXFDAVXGDVAAFXGDADXVDVFAVAFVFDGAVAFVXVDAXAFDGXDAFAFVAAADGVVVVXVVDDFVVGDVDAVVXDFVDVXDADXAFAAAFAVDFVVVXVDAVFGFGXFDGVVGDDADFFXVXVDDFFDDX"

map1 = {
	"A": "B",
	"D": "2",
	"F": "E",
	"G": "5",
	"V": "R",
	"X": "L"
}

map2 = {
	"A": "I",
	"D": "9",
	"F": "N",
	"G": "A",
	"V": "1",
	"X": "C"
}

map3 = {
	"A": "3",
	"D": "D",
	"F": "4",
	"G": "F",
	"V": "6",
	"X": "G"
}

map4 = {
	"A": "7",
	"D": "H",
	"F": "8",
	"G": "J",
	"V": "0",
	"X": "K"
}

map5 = {
	"A": "M",
	"D": "O",
	"F": "P",
	"G": "Q",
	"V": "S",
	"X": "T"
}

map6 = {
	"A": "U",
	"D": "V",
	"F": "W",
	"G": "X",
	"V": "Y",
	"X": "Z"
}

myMap = {
	"A": map1,
	"D": map2,
	"F": map3,
	"G": map4,
	"V": map5,
	"X": map6
}

index = 0

while index < len(code):
	print(myMap[code[index]][code[index+1]], end="")
	index = index + 2
