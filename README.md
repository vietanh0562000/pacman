# pacman
First project AI ( CS188 )
- Game Pacman AI
- Problems solved: Search Position (DFS, BFS, A*), Search Position
- Search Position: Các trạng thái lưu theo x và y, lần lượt tìm các trạng thái tiếp theo thỏa mãn để đi đến đích
 + DFS, BFS: đi tuần tự lần lượt
 + UCS, A*: Có thêm các điều kiện ưu tiên với A* thì là khoảng cách mahatan
- Corners Problem: Lưu các trạng thái theo x, y, và 4 biến boolean báo hiệu là đi đến 4 đỉnh hay chưa. và làm tương tự như position problem ngoại từ A* ta sẽ có hàm heristic khác sẽ là tính độ ưu tiên bằng cách tính khoảng cách từ đỉnh đang đứng tới 4 đỉnh giá trị hàm heristic là max của 4 giá trị đó

Multi_agent search
- evaluationFuntion: Các điều kiện để tính giá trị hàm là: 1. Ăn được tiếp trong bước tiếp theo, 2. khoảng cách đến chỗ các con ghost, 3. khoảng cách đến thức ăn gần nhất
- minimaxSearch: dùng đệ quy với các tham số state, agentIndex, depth. Đệ quy sẽ chạy với độ sâu depth, ứng với mỗi agent thì sẽ dùng min hoặc max để chọn ra phương án evaluation của các nút con (agentIndex = 0 là pacman ngược lại là ghost). 
-alphabetaSearch: Có 2 hàm tương tự như minimax có thêm 2 tham số cho 2 hàm là a, b (alpha, beta) , mỗi lần tính evaluation được thì ta sẽ cập nhật cho a hoặc b, dựa vào a, b và các giá trị tính được trong nhánh ta sẽ quyết định được có cắt nhánh hay không
-expectimax: Các con ghost không được thông minh quá nên thay vì dùng min( các giải pháp ) thì thay bằng công thức sum (các giải pháp) / (số lượng giải pháp)
Classification
-Em đi tham khảo được 3 câu ạ.
Buster
1. Exact Inference Observation
Với mỗi phần tử p trong self.legalPositions, nếu noisyDistance là none, có nghĩa là pacman đã ăn con ma và vị trí của ma, cập nhật "jail" nơi ma bị ăn, nếu không thì cập nhật belief dựa vào khoảng cách từ ma đến p.

2. Exact Inference with Time Elapse
Với mỗi phần tử p trong self.legalPositions, duyệt mảng lấy phân phối về nơi ma sẽ đến tiếp theo, cập nhật belief.

3. Exact Inference Full Test
Với những action trong legal, lấy vị trí của successor, duyệt những vị trí con ma sống trong livingGhostPositionDistributions, lấy vị trí của con ma có khả năng cao nhất, tính khoảng cách, nếu vị trí đó khác 0, cập nhật giá trị value cho action đó.

4. Approximate Inference Observation
Hàm initializeUniformly(self, gameState): liệt kê các vị trí của con ma có thể có, thiết lập các vị trí cụ thể.
Hàm getBeliefDistribution(self): lấy beliefDistribution bằng Couter(). Vì các con ma được phân bố chuẩn khắp các ví trí đặt belief bằng 1 có nghĩa là particle có thể ở bất cứ đâu trong grid.
Hàm observe(self, observation, gameState): Nếu noisyDistance là none, thì cập nhật vị trí particle là vị trí jail của con ma. Nếu không cập nhật belief giống như đã implement trong class exactInference.
5. Approximate Inference with Time Elapse
Với mỗi i trong range(self.numParticles), lấy tất cả các vị trí của con ma, lấy mẫu vị trí cho 1 số particle.
