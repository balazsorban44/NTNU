board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'
def make_board(board_string):
    return [list(map(lambda x:x  if x[0]!='.' else None ,board_string[j*5:j*5+5])) for j in range(0,5)]
board= make_board(board_string_1)
#print(board[0][1])
def get_piece(board,x,y):
    return board[5-y][x-1]



print(get_piece(make_board(board_string_1),2,1),'None')
print(get_piece(make_board(board_string_1),5,2),'P')
print(get_piece(make_board(board_string_1),1,1),'B')
print(get_piece(make_board(board_string_1),5,5),'r')
print(get_piece(make_board(board_string_1),4,4),'None')


#def get_legal_moves(board,x,y):
#    return board[-y][-x]



#print(get_legal_moves(board, 5, 5))
