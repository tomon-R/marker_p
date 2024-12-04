# 移動境界を有する有限要素流体解析の次元削減

Reduced-order modeling for finite element flow analysis with moving boundary  
金子栄樹 (東大・工) 吉村忍 (東大・工)  
Shigeki KANEKO, The University of Tokyo Shinobu YOSHIMURA, The University of Tokyo  
FAX: 03-5841-6994, E-mail: s_kaneko@save.sys.t.u-tokyo.ac.jp  

The present study worked on reduced-order modeling (ROM) using proper orthogonal decomposition for arbitrary Lagrangian–Eulerian (ALE) method-based fluid analysis. In the ALE method, Dirichlet boundary conditions on moving boundaries are time-variant. We proposed a ROM method to accurately impose the boundary conditions. We applied the ROM method to a classical fluid–rigid body interaction problem. Then, the number of degrees of freedom was reduced to less than 1% while keeping the accuracy.

## 1. 序論

計算機性能の向上により大規模自由度モデルを用いた数値解析が可能になってきているが、パラメトリックスタディのように何度も解析を実行することは依然として容易ではない。そこで現象の特徴を十分に捉えつつ計算コストの低い代理モデルの開発が求められている。Reduced-order modeling (ROM) の代表的な手法として固有直交分解 (Proper orthogonal decomposition, POD) を用いた手法 (以後、POD-ROMという) があり、様々な分野の数値解析に応用されている1)。POD-ROMでは、まず次元削減前の高自由度解析システムでサンプリング解析を行い、Snapshotと呼ばれるトレーニングデータを収集する。次に、収集したデータからPOD基底を抽出し、そのうちの少数の基底を用いて未知数を近似する。そして、Galerkin法と組み合わせてこの近似を用いることで解析システムの低次元化がなされ、自由度を大幅に削減することができる。本研究では移動境界を有する流体解析へのPOD-ROMの適用を試みる。

Stankiewiczら2) はArbitrary Lagrangian–Eulerian (ALE) 法を用いた流体解析にPOD-ROMを適用した。ALE法を用いた流体解析では、移動境界上の流速のDirichlet境界条件としてメッシュ移動速度が付与される。ゆえに、刻々と変化するDirichlet境界条件を扱う必要があるが、この研究では境界条件の付与が正確にできていない。Tissotら3) はFictitious domain (FD) 法を用いた流体解析にPOD-ROMを適用した。FD法では、移動境界上での条件は未定乗数法で処理されるため、前述のALE法を用いた場合の問題は生じない。界面追跡法は界面捕捉法に比べ解析精度が高いとされることを鑑み、我々はALE法を用いた流体解析に焦点を当てた。本研究では、解空間をDirichlet境界条件を満たすための固定元とそれ以外に分離して考え、後者のほうにPOD基底を用いた次元削減を施す、というROM手法を提案し、Dirichlet境界条件を正確に付与できるPOD-ROM解析システムの構築を行った。

## 2. 移動境界を有する流体解析

非圧縮性粘性流れの支配方程式は以下の通りである。

$$\rho^F \left( \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} - \hat{\mathbf{u}}) \cdot \nabla \mathbf{u} \right) - \nabla \cdot \sigma^F = \rho^F \mathbf{b}^F \tag{1}$$

$$\nabla \cdot \mathbf{u} = 0, \tag{2}$$

式 (1) はALE記述されたNavier–Stokes方程式、式 (2) は連続の式である。$\rho^F$は密度、$\mathbf{u}$は流速ベクトル、$\hat{\mathbf{u}}$はメッシュ速度、$\sigma^F$は応力テンソルを示している。Newton流体を仮定し応力テンソルは以下のように表される。

$$\sigma^F = -p\mathbf{I} + \mu\left(\nabla\mathbf{u} + \nabla\mathbf{u}^T\right) \tag{3}$$

$p$は圧力、$\mathbf{I}$は2階の単位テンソル、$\mu$は粘性係数、$\mathbf{b}^F$は物体力である。式 (1) と式 (2) を弱形式にし、適当に離散化することで、以下の式を得る。

$$\mathbf{K}\mathbf{d} = \mathbf{f} \tag{4}$$

ここで、$\mathbf{K} \in \mathbb{R}^{n \times n}$は係数行列、$\mathbf{d} \in \mathbb{R}^n$は解ベクトル、$\mathbf{f} \in \mathbb{R}^n$は既知量をまとめたベクトルである。ただし$n$は次元削減前のモデルの自由度数である。

## 3. 次元削減の方法

次元削減前の解析システムにおいて、解空間$\mathcal{M}$は$\mathcal{M} = \mathcal{V} + \mathcal{G}$のようにかける。ここで$\mathcal{V}$は

$$\mathcal{V} = \{ \mathbf{q} | \exists \mathbf{c} \in \mathbb{R}^n, \mathbf{q}(x) = \mathbf{N}(x)\mathbf{c} \} \tag{5}$$

である。ただし、Dirichlet境界条件が課される境界 ($\Gamma_D$と表す) 上で$\mathbf{q}$の値が0になるように適宜、係数$\mathbf{c}$の成分の一部には0が与えられる。また、$\mathbf{N} \in \mathbb{R}^{m \times n}$は形状関数を適宜まとめて表記した行列であり、$m$は1節点がもつ自由度数を示す。$\mathcal{G} = \mathbf{N}\mathbf{g}$はDirichlet境界条件を満たすための固定元である。$\mathbf{g}$は$\Gamma_D$上であれば境界条件の値が与えられ、それ以外では0である。序論で述べたとおり、本研究では$\mathcal{V}$に次元削減を施す。そうするために、解ベクトルからDirichlet境界条件の値を減じたもの ($\tilde{\mathbf{d}}$ と表す) をSnapshotとして収集する。Snapshotは以下のようなSnapshot matrix $\mathbf{U} \in \mathbb{R}^{n \times N_S}$にアセンブルされる。

$$\mathbf{U} = [\tilde{\mathbf{D}}(j_1), \tilde{\mathbf{D}}(j_2), \cdots, \tilde{\mathbf{D}}(j_{N_S})] \tag{6}$$

ここで$j$はパラメータセットを表しており、$N_S$はSnapshotの総数である。時刻も解ベクトルを決定するパラメータと捉え、各時刻でSnapshotの収集を行う。次に、$\mathbf{U}$に内在する特徴を分析し基底を抽出するため、特異値分解を施す。

$$\mathbf{U} = \mathbf{V}\mathbf{S}\mathbf{W}^T \tag{7}$$

ここで$\mathbf{V} \in \mathbb{R}^{n \times \text{Rank}(\mathbf{U})} = [\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_{\text{Rank}(\mathbf{U})}]$の各列が左特異ベクトルとなる。また、$\mathbf{S} = \text{diag}(\sigma_1, \cdots, \sigma_{\text{Rank}(\mathbf{U})})$ であり、$\sigma$は特異値を表しており、添字が小さいほど大きく、非負である。左特異ベクトルがPOD基底であり、相当する特異値が大きいほど支配的なモードとなる。前述の通り、Dirichlet境界条件の値を減じたものを収集したので、各モードの$\Gamma_D$上の値は0となる。次元削減のために、はじめの$k$本 (ただし$k \ll n$) の基底を用い、結果として$\mathbf{d}$は次のように近似される。

$$\mathbf{d} = \mathbf{V}_k\mathbf{a} + \mathbf{g} \tag{8}$$

ここで、$\mathbf{a} \in \mathbb{R}^k$は係数、$\mathbf{V}_k \in \mathbb{R}^{n \times k}$は$\mathbf{V}_k = [\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_k]$のようにPOD基底をまとめた行列である。この近似はGalerkin法と組み合わせて用いられるので、式 (4) は以下のように低次元化される。

$$\mathbf{V}_k^T \mathbf{K} \mathbf{V}_k \mathbf{a} = \mathbf{V}_k^T (\mathbf{f} - \mathbf{K} \mathbf{g}) \tag{9}$$

## 4. 数値解析例

![1_Image_2.Png](1_Image_2.Png)

図1に示すような、典型的な流体剛体連成問題を扱う。一様流れ内に円柱シリンダーが配置され、仮想的なバネとダンパにつながれているものとし、シリンダーは流体力により自励振動を起こす。表1に解析条件を示す。

Fig. 1 Schematic view of fluid–rigid body interaction problem

| Analysis conditions  |                       |
|----------------------|-----------------------|
| Time step width      | 1.0 × 10^-3 [s]      |
| Number of nodes      | 9235                  |
| Density of fluid     | 1.0 × 10^3 [kg/m^3]  |
| Viscosity            | 1.0 × 10^-3 [kg/m·s] |
| Inlet velocity       | 62.5 [m/s]            |
| Density of structure | 1.0 × 10^3 [kg/m^3]  |
| Stiffness            | 69.84 [N/m]           |
| Damping              | 4.0 × 10^-3 [N·s/m]  |

データ収集として3000タイムステップまで解析を行った(NS = 3000)。2,3章では簡便のために未知数をまとめた場合の定式化を示したが、実際の実装では流速と圧力に分けてPOD基底を抽出している。図2に流速の1次モードのy成分を可視化した。円柱付近の拡大図から明らかなように、$\Gamma_D$上で値が0になっている。ROMのために、流速に関して162本、圧力に関して37本のPOD基底を用いた。よって、自由度数は199となり、もともとのシステム (自由度数27705) の1%以下となった。

ROM解析ともともとの高精度解析の結果を比較するために、t = 4 sにおける流速の大きさの分布を図3に示した。これより両者は大域的に良い一致を示していることがわかる。図4にシリンダーの変位の時刻歴応答を示す。次元削減モデルでも自励振動を再現できている。3000ステップ分の情報をもとにROMは行われたので、それ以降、時間経過に伴い若干の誤差が生じている。

![1_Image_3.Png](1_Image_3.Png)

Fig. 2 1st POD mode of y-velocity

![1_Image_0.Png](1_Image_0.Png)

Fig. 3 Velocity norm at t = 4 s, (a) High-fidelity (b) ROM

![1_Image_1.Png](1_Image_1.Png)

Fig. 4 Time histories of displacement of cylinder

## 5. 結論

本研究では、ALE法をベースとした流体解析へのPOD-ROMの適用を行った。既存研究で課題となっていた刻々と変化するDirichlet境界条件の付与を、正確に処理できるような手法を提案した。節点数が1万程度の流体剛体連成解析に提案手法を適用し、自由度が200程度の次元削減モデルを構築した。そして、ROM解析ともともとの高精度解析の結果を比較し、良い一致を確認した。ROM解析時のパラメータセットや時刻がサンプリング解析時のものから大きく離れると、解析精度が低下するため、基底を解析途中でエンリッチするなどのアダプティブな精度向上手法の開発が今後必要である。

## 参考文献

1) A. Quarteroni, A. Manzoni, F. Negri.: Reduced basis methods for partial differential equations, Springer, 2016.

2) W. Stankiewicz, R. Roszak, M. Morzynski.: Arbitrary Lagrangian–Eulerian approach in reduced order modeling of a flow with a moving boundary, *Prog. Flight. Phys.*, Vol.5, pp.109–124, 2013.

3) G. Tissot, L. Cordier, B. Noack. Feedback stabilization of an oscillating vertical cylinder by POD reduced-order model, 22th French Mechanics Congress, Lyon, France, August 2015.