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

Học Tăng Cường
Câu 1: Với hàm init Đầu tiên ta duyệt hết các giá trị của range(iterations), ta xét từng giá trị của từng state, mỗi state ta lại xét từng trạng thái nếu trạng thái là đích thì ta sẽ thoái ra và không có phần thưởng, còn nếu đây không phải đích thì ta sẽ tìm tổng phần thưởng mong đợi lớn nhất của các hành động khác nhau

Với hàm computeQValueFromValues Ta có một hàm ở đây để có thể tính toán trạng thái chuyển đổi và xác suất là getTransitionStatesAndProbs(state, action). Đối với mỗi lần chuyển đổi được tính bằng tổng phần thưởng của việc chuyển đổi và trạng thái chuyển tiếp sau đó. Và chính giá trị này cung cấp cho q-value một cặp hành động và trạng thái (action,state) mà từ đó ta có thể tính được giá trị cần tìm

Với hàm computeActionFromValues Ta đơn giản là chỉ khai báo một bộ đém stateAction để lưu q-value. Với mỗi cặp (Action,state) thì policy hoặc action chính là cho ta biết được tổng phần thưởng mong đợi tốt nhất

Câu 2: Với question2 ta chọn hai giá trị answerDiscount = 0.9 và answerNoise = 0 vì với noise = 0 thì mới có thể dễ dàng xác đinh đồng thời agent sẽ luôn kế thúc khi có agent mới

Câu 3: Với Q3a các giá trị là: answerDiscount = 1 answerNoise = 0.2 answerLivingReward = -1 Vì ta muốn agent nhanh chóng di chuyển đến lối ra nhanh nhất có thể ta chọn phần thưởng phải âm để khiến nó thoát ra nhanh nhất Với Q3b các giá trị là: answerDiscount = 0.3 answerNoise = 0.3 answerLivingReward = 0 Chọn như vậy để agent thoát bằng đường khác nhưng với con đường xa hơn Với Q3c các giá trị là: answerDiscount = 1 answerNoise = 0.2 answerLivingReward = -0.5 Vì để cho agent có thể sống đủ lâu ở mức +10 bằng cách chấp nhận rủi ro nên phần thưởng cho lớn hơn câu 3a Với Q3d các giá trị là: answerDiscount = 1 answerNoise = 0.2 answerLivingReward = -0.03 Vì không để agent chấp nhận rủi ro nên ta để phần thưởng có mức âm nhỏ hơn 3c Với Q3e các giá trị là: answerDiscount = 1 answerNoise = 0.2 answerLivingReward = 9999 Vì phần thưởng cho việc sống sót lớn hơn nhiều so với việc thoát ra nên nó sẽ không thoát ra nữa

Câu 4: Để giải quyết bài này với hàm computeActionFromQValues Ta lấy tât các trạng thái của hành động bằng hàm getLegalActions() với giá trị khởi đầu ta cho giá trị bằng 0 còn với các trạng thái khác thì trả về giá trị tối đa của q-value trạng thái Còn hàm computeActionFromQValues Ý tưởng để tính toán ra được hành động tốt nhất để thực hiện trong một trạng thái như sau

Câu 5: Với việc chọn ngẫu nhiên một action epsilon chỉ khi đánh giá được self.epsilon còn không sẽ trả về giá trị hành động của hàm computeActionFromQValues

Câu 6: Ta chọn các giá trị : answerEpsilon = 0.1 answerLearningRate = 0.8 Vì không thể tìm được con đường tối ưu đến 99%, 50 tập là quá nhỏ nên cần thêm để tìm kiếm
