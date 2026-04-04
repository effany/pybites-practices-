WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    iter = 0
   
    if size % 2 == 0:
        while iter < size:
            if iter % 2 == 0:
                print((WHITE + BLACK) * int(size / 2))
            else:
                print((BLACK + WHITE) * int(size / 2))
            iter += 1

create_chessboard(7)