# pacman
First project AI ( CS188 )
- Game Pacman AI
- Problems solved: Search Position (DFS, BFS, A*), Search Position
- Search Position: Các trạng thái lưu theo x và y, lần lượt tìm các trạng thái tiếp theo thỏa mãn để đi đến đích
 + DFS, BFS: đi tuần tự lần lượt
 + UCS, A*: Có thêm các điều kiện ưu tiên với A* thì là khoảng cách mahatan
- Corners Problem: Lưu các trạng thái theo x, y, và 4 biến boolean báo hiệu là đi đến 4 đỉnh hay chưa. và làm tương tự như position problem ngoại từ A* ta sẽ có hàm heristic khác sẽ là tính độ ưu tiên bằng cách tính khoảng cách từ đỉnh đang đứng tới 4 đỉnh giá trị hàm heristic là max của 4 giá trị đó
