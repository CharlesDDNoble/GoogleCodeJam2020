# Case 1: Same
# can determine whether its
# the ORI or REV
# the COM or COM + REV
# if new 1st differs from old, complement all
11 ORI
11 REV
00 COM
00 COM + REV

# Case 2: Different
# can determine whether its
# the ORI or COM + REV
# the REV or COM
10 ORI
01 REV
01 COM
10 COM + REV


100101 010110 ORI
011010 101001 REV
011010 101001 COM
100101 010110 COM + REV


# Case 3: Unequal (number of 0's and 1's)
# We can solve for the entire array
# if bits are the same == orig
# if the XOR is all 1's == com
# if the bits are reversed == reversed
# else == COM + REV
1101 ORI
1011 REV
0010 COM
0100 COM + REV

# we can use 2 and 3 to solve for the entire array
# if 2 == ORI and 3 == ORI then its ORI
# if 2 != ORI and 3 == ORI then its REV
# if 2 == ORI and 3 != ORI then its COM + REV
# else its COM


XX XX XX XX XX
PP XX XX XX PP 
XX PP XX PP XX


11001011010010110110 ORI
00110100101101001001 COM
01101101001011010011 REV
10010010110100101100 COM + REV



11001011010010110110 ORI
dsdssddssd
    |          |    
10010010110100101100 COM + REV


1101110100 ORI


1
0
1
0
0
1
1
0
1
1




