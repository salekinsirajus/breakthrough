src_dst_pairs = [[(0,0),(0,0)], # False, src = dst
                        [(0,0),(0,2)],   # False, two units, same row
                        [(0,0),(-1,0)],  # False, out of index
                        [(0,0),(0,1)],   # False, same row
                        [(0,0),(1,-1)],   # False, out of index
                        [(0,0),(1,2)],   # False, moving two units
                        [(0,0),(2,0)],   # False, moving two units
                        [(0,0),(2,2)],   # False, moving two units
                        [(0,0),(11,11)]   # False, out of index
                        ]
for pair in src_dst_pairs:
    print (pair)
    print(pair[0], pair[1])
