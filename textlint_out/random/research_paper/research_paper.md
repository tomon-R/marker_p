# 移動境界を有する有限要素流体解析の次元削減

Reduced-order modeling for finite element flow analysis with moving boundary金子栄樹 (東大・工) 吉村忍 (東大・工)
Shigeki KANEKO, The University of Tokyo Shinobu YOSHIMURA, The University of Tokyo FAX: 03-5841-6994, E-mail: s kaneko@save.sys.t.u-tokyo.ac.jp The present study worked on reduced-order modeling (ROM) using proper orthogonal decomposition for arbitrary Lagrangian–Eulerian (ALE) method-based fluid analysis. In the ALE method, Dirichlet boundary conditions on moving boundaries are time-variant. We proposed a ROM method to accurately impose the boundary conditions. We applied the ROM method to a classical fluid–rigid body interaction problem. Then, the number of degrees of freedom was reduced to less than 1 % while keeping the accuracy.

## 1. 序論

計算機性能の向上により大規模自由度モデルを用いた 数値解析が可能になってきているが、パラメトリックスタ ディのように何度も解析を実行することは依然として容 易ではない。そこで現象の特徴を十分に捉えつつ計算コ ストの低い代理モデルの開発が求められている。Reducedorder modeling (ROM) の代表的な手法として固有直交分解 (Proper orthogonal decomposition, POD) を用いた手法 (以後、
POD-ROMという) があり、様々な分野の数値解析に応用さ れている1)。POD-ROMでは、まず次元削減前の高自由度 解析システムでサンプリング解析を行い、Snapshotと呼ば れるトレーニングデータを収集する。次に、収集したデー
タからPOD基底を抽出し、そのうちの少数の基底を用い て未知数を近似する。そして、Galerkin法と組み合わせて この近似を用いることで解析システムの低次元化がなさ れ、自由度を大幅に削減することができる。本研究では移 動境界を有する流体解析へのPOD-ROMの適用を試みる。

Stankiewiczら2) はArbitrary Lagrangian–Eulerian (ALE) 法を用いた流体解析にPOD-ROMの適用した。ALE法を用いた流体解析では、移動境界上の流速のDirichlet境界条件としてメッシュ移動速度が付与される。ゆえに、刻々と変化するDirichlet境界条件を扱う必要があるが、この研究では境界条件の付与が正確にできていない。Tissotら3) はFictitious domain (FD) 法を用いた流体解析にPOD-ROMを適用した。FD法では、移動境界上での条件は未定乗数法で処理されるため、前述のALE法を用いた場合の問題は生じない。界面追跡法は界面捕捉法に比べ解析精度が高いとされることを鑑み、我々はALE法を用いた流体解析に焦点を当てた。本研究では、解空間をDirichlet境界条件を満たすための固定元とそれ以外に分離して考え、後者のほうにPOD基底を用いた次元削減を施す、というROM手法を提案し、Dirichlet境界条件を正確に付与できるPOD-ROM解析システムの構築を行った。

## 2. 移動境界を有する流体解析

非圧縮性粘性流れの支配方程式は以下の通りである。

$$\rho^{F}\left(\frac{\partial\mathbf{u}}{\partial t}+(\mathbf{u}-\hat{\mathbf{u}})\cdot\nabla\mathbf{u}\right)-\nabla\cdot\sigma^{F}=\rho^{F}\mathbf{b}^{F}\tag{1}$$
$$\nabla\cdot\mathbf{u}=0,$$

∇ · u = 0, (2)
式 (1) はALE記述されたNavier–Stokes方程式、式 (2) は 連続の式である。ρ Fは密度、uは流速ベクトル、uˆ はメッ シュ速度、σ Fは応力テンソルを示している。Newton流体 を仮定し応力テンソルは以下のように表される。

$$\sigma^{F}=-p\mathbf{I}+\mu\left(\nabla\mathbf{u}+\nabla\mathbf{u}^{T}\right)$$
T)(3)
pは圧力、Iは2階の単位テンソル、µ は粘性係数、b Fは物体力である。式 (1) と式 (2) を弱形式にし 、適当に離散化することで、以下の式を得る。

$$({\mathfrak{I}})$$
$$\mathbf{Kd}=\mathbf{f}$$
$$(4)$$
Kd = f (4)
ここで、K ∈ R
n×nは係数行列、d ∈ R
nは解ベクトル、f ∈ R
nは既知量をまとめたベクトルである。ただしnは次元削減前のモデルの自由度数である。

## 3. 次元削減の方法

次元削減前の解析システムにおいて、解空間MはM =
V + Gのようにかける。ここでVはV = {q|∃c ∈ R
n, q(x) = N(x)c} (5)
である。ただし、Dirichlet境界条件が課される境界 (ΓDと表す) 上でqの値が0になるように適宜、係数cの成分の一部には0が与えられる。また、N ∈ R
m×nは形状関数を適宜まとめて表記した行列であり、mは1節点がもつ自由度数を示す。G = NgはDirichlet境界条件を満たすための固定元である。gは ΓD上であれば境界条件の値が与えられ、
それ以外では0である。序論で述べたとおり、本研究ではVに次元削減を施す。そうするために、解ベクトルからDirichlet境界条件の値を減じたもの (d˜ と表す) をSnapshotとして収集する。Snapshotは以下のようなSnapshot matrix U ∈ R
n×NSにアセンブルされる。

## U = [D˜(J1), D˜(J2), · · · , D˜(Jns)] (6)

ここでjはパラメータセットを表しており、NSはSnapshotの総数である。時刻も解ベクトルを決定するパラメータと捉え、各時刻でSnapshotの収集を行う。次に、Uに内在する特徴を分析し基底を抽出するため、特異値分解を施す。

$$(6)$$
$$(T)$$

## U = Vswt(7)

$${\mathrm{(2)}}$$

ここでV ∈ R
n×Rank(U) =[v1, v2, · · · , vRank(U)]の各列が左特異ベクトルとなる。また、S = diag(σ1, · · · , σRank(U)) であり、σ は特異値を表しており、添字が小さいほど大きく、非負である。左特異ベクトルがPOD基底であり、相当する特異値が大きいほど支配的なモードとなる。前述の通り、Dirichlet境界条件の値を減じたものを収集したので、各モードの ΓD
上の値は0となる。次元削減のために、はじめのk本 (ただしk << n) の基底を用い、結果としてdは次のように近似される。

d = Vka + g (8)
ここで、a ∈ R
kは係数、Vk ∈ R
n×kはVk =[v1, v2, · · · , vk]
のようにPOD基底をまとめた行列である。この近似はGalerkin法と組み合わせて用いられるので、式 (4) は以下のように低次元化される。

$$i_{\mathbf{k}\mathbf{a}}+\mathbf{g}$$
$$\mathbf{V}_{k}{}^{T}\mathbf{K}\mathbf{V}_{k}\mathbf{a}=\mathbf{V}_{k}{}^{T}\left(\mathbf{f}-\mathbf{K}\mathbf{g}\right)$$
T(f − Kg) (9)

## 4. 数値解析例

![1_Image_2.Png](1_Image_2.Png)

図1に示すような、典型的な流体剛体連成問題を扱う。

一様流れ内に円柱シリンダーが配置され、仮想的なバネとダンパにつながれているものとし、シリンダーは流体力により自励振動を起こす。表1に解析条件を示す。

Fig. 1 Schematic view of fluid–rigid body interaction problem

| Table 1              | Analysis conditions   |
|----------------------|-----------------------|
| Time step width      | 1.0 × 10−3 [s]        |
| Number of nodes      | 9235                  |
| Density of fluid     | 1.0 × 103 [kg/m3 ]    |
| Viscosity            | 1.0 × 10−3 [kg/m · s] |
| Inlet velocity       | 62.5[m/s]             |
| Density of structure | 1.0 × 103 [kg/m3 ]    |
| Stiffness            | 69.84[N/m]            |
| Damping              | 4.0 × 10−3 [N · s/m]  |

データ収集として3000タイムステップまで解析を行った

![1_image_3.png](1_image_3.png)

(NS = 3000)。2,3章では簡便のために未知数をまとめた場合の定式化を示したが、実際の実装では流速と圧力に分けてPOD基底を抽出している。図2に流速の1次モードのy成分を可視化した。円柱付近の拡大図から明らかなよう

Fig. 2 1st POD mode of y-velocity
に、ΓD上で値が0になっている。ROMのために、流速に関して162本、圧力に関して37本のPOD基底を用いた。 よって、自由度数は199となり、もともとのシステム (自由度数27705) の1%以下となった。

ROM解析ともともとの高精度解析の結果を比較するために、t = 4 sにおける流速の大きさの分布を図3に示した。これより両者は大域的に良い一致を示していることがわかる。図4にシリンダーの変位の時刻歴応答を示す。次

![1_image_0.png](1_image_0.png)

$$(9)$$

Fig. 3 Velocity norm at t = 4 s, (a) High-fidelity (b) ROM

![1_image_1.png](1_image_1.png)

Fig. 4 Time histories of displacement of cylinder
元削減モデルでも自励振動を再現できている。3000ステッ プ分の情報をもとにROMは行われたので、それ以降、時 間経過に伴い若干の誤差が生じている。

## 5. 結論

本研究では、ALE法をベースとした流体解析へのPOD-
ROMの適用を行った。既存研究で課題となっていた刻々と 変化するDirichlet境界条件の付与を、正確に処理できるよ うな手法を提案した。節点数が1万程度の流体剛体連成解 析に提案手法を適用し、自由度が200程度の次元削減モデ ルを構築した。そして、ROM解析ともともとの高精度解 析の結果を比較し、良い一致を確認した。ROM解析時の パラメータセットや時刻がサンプリング解析時のものから 大きく離れると、解析精度が低下するため、基底を解析途 中でエンリッチするといったアダプティブな精度向上手法 の開発が今後必要である。

## 参考文献

1) A. Quarteroni, A. Manzoni, F. Negri.: Reduced basis methods for partial differential equations, Springer, 2016.

2) W. Stankiewicz, R. Roszak, M. Morzynski.: Arbitrary Lagrangian–Eulerian approach in reduced order modeling of a flow with a moving boundary, *Prog. Flight. Phys.*, Vol.5, pp.109–124, 2013.

3) G. Tissot, L. Cordier, B. Noack. Feedback stabilization of an oscillating vertical cylinder by POD reduced-order model, 22th French Mechanics Congress, Lyon, France, August 2015.