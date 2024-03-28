board = Board(7, 7)

# p1 = Point(Position(4,4),"red")
# p2 = Point(Position(8,3),"red")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(8,4),"blue")
# p2 = Point(Position(8,8),"blue")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(4,3),"green")
# p2 = Point(Position(8,1),"green")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(0,0),"yellow")
# p2 = Point(Position(7,3),"yellow")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(0,1),"orange")
# p2 = Point(Position(3,1),"orange")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(8,4),"pink")
# p2 = Point(Position(8,7),"pink")
# board.add_point_pair(p1,p2)

# p1 = Point(Position(8,0),"navy")
# p2 = Point(Position(4,6),"navy")
# board.add_point_pair(p1,p2)

board2 = Board(8,8)

p1 = Point(Position(2,2),"red")
p2 = Point(Position(6,4),"red")
board2.add_point_pair(p1,p2)

p1 = Point(Position(0,5),"navy")
p2 = Point(Position(6,1),"navy")
board2.add_point_pair(p1,p2)

p1 = Point(Position(2,4),"yellow")
p2 = Point(Position(5,5),"yellow")
board2.add_point_pair(p1,p2)

p1 = Point(Position(1,1),"green")
p2 = Point(Position(5,4),"green")
board2.add_point_pair(p1,p2)

p1 = Point(Position(3,0),"orange")
p2 = Point(Position(5,3),"orange")
board2.add_point_pair(p1,p2)

p1 = Point(Position(4,1),"blue")
p2 = Point(Position(7,0),"blue")
board2.add_point_pair(p1,p2)

p1 = Point(Position(5,1),"pink")
p2 = Point(Position(6,3),"pink")
board2.add_point_pair(p1,p2)

start = time.time()

print(board2.brut_force(2, 2))
print("time : "+str(time.time()-start))
print(board2)
print(board2.draw())




board3 = Board(10,10)

p1 = Point(Position(9,0),"red")
p2 = Point(Position(8,2),"red")
board3.add_point_pair(p1,p2)

p1 = Point(Position(2,5),"navy")
p2 = Point(Position(8,7),"navy")
board3.add_point_pair(p1,p2)

p1 = Point(Position(0,1),"yellow")
p2 = Point(Position(2,9),"yellow")
board3.add_point_pair(p1,p2)

p1 = Point(Position(1,6),"green")
p2 = Point(Position(7,4),"green")
board3.add_point_pair(p1,p2)

p1 = Point(Position(3,7),"orange")
p2 = Point(Position(5,7),"orange")
board3.add_point_pair(p1,p2)

p1 = Point(Position(9,1),"blue")
p2 = Point(Position(9,5),"blue")
board3.add_point_pair(p1,p2)

p1 = Point(Position(9,0),"pink")
p2 = Point(Position(8,8),"pink")
board3.add_point_pair(p1,p2)

p1 = Point(Position(8,0),"purple")
p2 = Point(Position(6,7),"purple")
board3.add_point_pair(p1,p2)

p1 = Point(Position(2,2),"brown")
p2 = Point(Position(4,5),"brown")
board3.add_point_pair(p1,p2)

start = time.time()

print(board3.brut_force(9,0))
print("time : "+str(time.time()-start))
print(board3)
print(board3.draw())



board9 = Board(9,9)

p1 = Point(Position(4,7),"red")
p2 = Point(Position(7,6),"red")
board9.add_point_pair(p1,p2)

p1 = Point(Position(2,6),"blue")
p2 = Point(Position(7,2),"blue")
board9.add_point_pair(p1,p2)

p1 = Point(Position(1,1),"yellow")
p2 = Point(Position(6,6),"yellow")
board9.add_point_pair(p1,p2)

p1 = Point(Position(5,4),"green")
p2 = Point(Position(7,1),"green")
board9.add_point_pair(p1,p2)

p1 = Point(Position(3,0),"orange")
p2 = Point(Position(3,3),"orange")
board9.add_point_pair(p1,p2)

p1 = Point(Position(0,0),"navy")
p2 = Point(Position(8,3),"navy")
board9.add_point_pair(p1,p2)

p1 = Point(Position(6,2),"pink")
p2 = Point(Position(6,4),"pink")
board9.add_point_pair(p1,p2)

p1 = Point(Position(1,0),"purple")
p2 = Point(Position(8,2),"purple")
board9.add_point_pair(p1,p2)

start = time.time()

print(board9.brut_force(4,7))
print("time : "+str(time.time()-start))
print(board9)
print(board9.draw())


