数値流体力学第6回講義非構造格子系の手法 (**有限体積法・有限要素法など**) による流体解析 (2) 三目直登

![1_image_0.png](1_image_0.png)

| 講義回 | 内容 |
|---------|------|
| 第1回 | 数値シミュレーションと数値流体力学の概観 |
| 第2回 | 構造格子系の手法 (差分法など) による流体解析 (1) |
| 第3回 | 構造格子系の手法 (差分法など) による流体解析 (2) |
| 第4回 | 構造格子系の手法 (差分法など) による流体解析 (3) |
| 第5回 | 非構造格子系の手法 (有限体積法・有限要素法など) による流体解析 (1) |
| 第6回 | 非構造格子系の手法 (有限体積法・有限要素法など) による流体解析 (2) |
| 第7回 | 格子を用いない手法 (粒子法など) による流体解析 (1) |
| 第8回 | 格子を用いない手法 (粒子法など) による流体解析 (2) |
| 第9回 | 数値計算プログラミング演習 |
| 第10回 | 移動境界問題・流体構造連成問題の数値解析 |

Y. Bazilevs, K. Takizawa and T.E. Tezduyar, Computational Fluid–Structure Interaction, Wiley, 2013.

Y. Bazilevs, K. Takizawa and T.E. Tezduyar, (訳: 津川祐美子, 滝沢研二), 流体-構造連成問題の数値解析, 森北出版, 2015.

![2_image_3.png](2_image_3.png)

日本計算工学会 流れの有限要素法研究委員会, 続・有限要素法による流れのシミュレーション, シュプリンガージャパン, 2008.

![2_image_0.png](2_image_0.png)

![2_image_1.png](2_image_1.png)

![2_image_2.png](2_image_2.png)

# 差分法と有限体積法

|   | 特徴 |
|---|-----|
| 差分法 | 座標系に沿った構造格子を使用し、Taylor展開をベースに微分演算子を近似し、保存性を担保する工夫を行う。 |
|   | 非構造格子 (コントロールボリューム) が使用可能。 |
| 有限体積法 | Staggered格子の使用が難しい場合にはCollocated格子を利用し、2点間 (コントロールボリューム内の点) でフラックスを求め、偏微分方程式を離散化する。 |

![4_image_10.png](4_image_10.png)

![4_image_14.png](4_image_14.png)

![4_image_15.png](4_image_15.png)

![4_image_16.png](4_image_16.png)

![4_image_17.png](4_image_17.png)

![4_image_18.png](4_image_18.png)

有限体積法とは?

- Staggered格子を使用し、偏微分方程式を一般化保存則の形で記述。
- 格子間のフラックス (流束)
- 保存性を担保する工夫。ガウスの発散定理を用いて非構造格子間のフラックスを解析する手法。
- 非構造格子 (コントロールボリューム) が使用可能。
- 2点間 (コントロールボリューム内の点) でフラックスを求め、偏微分方程式を離散化。

![4_image_19.png](4_image_19.png)

偏微分方程式を離散化

![4_image_20.png](4_image_20.png)

# 差分法と有限体積法

Vi = 一般化保存則

\(\frac{\partial \phi}{\partial t} + \nabla \cdot F(\phi) = S(\phi)\)

- コントロールボリューム (CV) 内で両辺を積分。
  
\[
\int_{\Omega_i} \frac{\partial \phi}{\partial t} d\Omega + \int_{\partial \Omega_i} F(\phi) \cdot n d\Gamma = \int_{\Omega_i} S(\phi) d\Omega
\]

体積積分を近似 (CV内で物理量が一定)

\[
\int_{\Omega_i} \frac{\partial \phi}{\partial t} d\Omega \approx V_i \frac{\partial \phi_i}{\partial t}, \quad \int_{\Omega_i} S(\phi) d\Omega \approx V_i S(\phi_i)
\]

表面積分を近似 (中点公式・台形則)

\[
\sum_{s=1}^{6} S_{i,s} \hat{F}(\phi_i, \phi_{\text{conn}(i,s)}) \cdot n
\]

j = conn(i, s): i番のCV内にある表面sの向こう側のCV番号を返す関数

一般化保存則の離散化

\[
\int_{\Omega_i} \left(\frac{\partial \phi}{\partial t} + \nabla \cdot F(\phi)\right) d \Omega = \int_{\Omega_i} S(\phi) d \Omega
\]

各表面の積分の和に変形

\[
\frac{\partial \phi_i}{\partial t} + \sum_{s=1}^{6} S_{i,s} \hat{F}(\phi_i, \phi_{\text{conn}(i,s)}) \cdot n = V_i S(\phi_i)
\]

移流拡散方程式の場合

\[
\frac{\partial \varphi}{\partial t} + \nabla \cdot \mathbf{F}(\phi) = S(\phi)
\]

![6_image_1.png](6_image_1.png)

どうやって微分を計算する?

## 1次元 (構造格子) の場合

差分法と同様に、2点以上を用いて補間する高精度モデルが問題なく使用可能。

## 多次元・非構造格子の場合

座標軸に関係なく格子や計算点が配置されているため、表面に隣接している2点以外は利用できる保証がないため、有限体積法は高次精度化が困難。

![6_image_0.png](6_image_0.png)

# メッシュベース Vs メッシュフリー

## メッシュベース法

構造格子: 格子 (メッシュ) が座標に沿って配置

→ 差分法など

- 計算点の連結情報が自明であり、行列の形も特徴的 (三重対角行列など) なので、計算コストが低い。
- 座標変換による境界適合格子などの工夫が可能だが、空間の表現に限界がある。
  
非構造格子: 四面体など任意形状のメッシュを使用。
  
→ 有限体積法・有限要素法など。

- 計算点の連結情報が必要であり、計算コストが高い。
- 複雑形状の対象にも利用できる。

## 有限体積法

- **原理的に保存性を有する**
- 非構造格子における高次精度化が困難

## メッシュフリー法

→ Smoothed Particle Hydrodynamics法・Element-Free Galerkin法など。

- メッシュ作成のコストやメッシュの歪みによる計算不安定性が少ない。
- 表面などの幾何学的情報が一部失われるので、境界等の精度が低い。

# 目次

1. **連続体力学と変分法の関係**
2. **有限要素法の基本**
   - 2.1. **重み付き残差法と弱形式化**
   - 2.2. Galerkin法
   - 2.3. 形状関数による補間
3. **安定化有限要素法**
   - 3.1. Upwind Galerkin法
   - 3.2. Streamline upwind Petrov/Galerkin法
   - 3.3. **その他の安定化スキーム**

![10_image_0.png](10_image_0.png)

![10_image_2.png](10_image_2.png)

質点系の力学 **剛体の力学**

![10_image_1.png](10_image_1.png)

![10_image_4.png](10_image_4.png)

![10_image_5.png](10_image_5.png)

![10_image_9.png](10_image_9.png)

![10_image_3.png](10_image_3.png)

![10_image_6.png](10_image_6.png)

![10_image_7.png](10_image_7.png)

![10_image_8.png](10_image_8.png)

![10_image_10.png](10_image_10.png)

無限個の質点が間なく並んで連続的な分布を形成するよう拡張。連続体力学レオロジー

![10_image_11.png](10_image_11.png)

固体
(弾性体)
弾性体力学構造力学材料力学流体力学水理学流体 = 静止状態においてせん断応力が発生しない連続体。
※ せん断応力のイメージは、物体表面の接線方向に働く力。連続体力学学習におすすめの書籍: よくわかる連続体力学ノート, 京谷孝史, 森北出版.

# 1. 連続体力学と変分法の関係

![11_image_0.png](11_image_0.png)

変分法とは?

高校数学 → 関数の最大値・最小値問題 (有限次元の微分)
関数: 数値 → 数値

解法: 最大値・最小値を満たすxを求める変分法 → 汎関数の最大値・最小値問題 (無限次元の微分: 汎関数微分)

汎関数: 関数 → 数値

解法: 最大値・最小値を満たす (停留関数) を求める

→ 汎関数微分 (変分) による解法

Euler–Lagrange方程式

最小作用の原理 **(principle of least action):**

- 力学系の運動は、作用(解析力学で定義される汎関数)が最小になるような運動である。
- 力学問題を変分問題として捉えることができる。

変分問題の例

屈折率が連続的に変化する媒質内での光の経路。

光の経路: 媒質の屈折率。
光が経路C (右図のP0からP1まで) を通過するのにかかる時間を求める。

![19_image_0.png](19_image_0.png)

cを真空中の光の速度とすると、点 (x, y) における光の速度はで与えられ,これを用いると,C上の微小線素dsを光が通過する時間は以下のように表される。

![20_image_0.png](20_image_0.png)

光が経路CをP0からP1まで通過するのにかかる時間はとなる。線素dsの長さを用いて,Tは以下のように求められる。

\[
T={\frac{1}{c}}\int_{x_{0}}^{x_{1}}n(y(x))\sqrt{1+y^{\prime}{(x)}^{2}}\,dx
\]

光は所要時間が最小になるような経路を通る (フェルマーの原理) より,光の経路はとした変分問題の停留関数として求められる。

![22_image_0.png](22_image_0.png)

# 連続体力学と変分法の関係

直交関数展開

関数は無限個の直交関数列として表すことができる
例) **フーリエ級数展開**:

\(y(x) = \frac{1}{2} a_0 + a_1 \cos \omega x + a_2 \cos 2\omega x + \cdots + b_1 \sin \omega x + b_2 \sin 2\omega x + \cdots\)

$$e_{x}\cdot e_{y}=0$$

関数の直交性 ← Euclidの基底ベクトルの直交性 (内積=0) の拡張。

直交関数の例(ルジャンドル展開):
- \(P_0 = 1\)
- \(P_1 = x\)
- \(P_2 = \frac{1}{2}(3x^2 - 1)\)
- \(P_3 = \frac{1}{2}(5x^3 - 3x)\)
- \(P_4 = \frac{1}{8}(35x^4 - 30x^2 + 3)\)
- \(P_5 = \frac{1}{8}(63x^5 - 70x^3 + 15x)\)

偏微分方程式は関数を入力し、(初期条件等の) 関数を解の関数に移す写像。線形写像の場合は、無限次元空間内における線形代数学, 関数解析学。

1. **連続体力学と変分法の関係**
   変分法における近似解法

変分法 →汎関数の最大値・最小値問題
→**変分問題**
(無限次元の微分: 汎関数微分)

解法: を満たす (停留関数) を求める

→汎関数微分 (変分) による解法 Euler–Lagrange方程式

有限個の基底関数で近似

関数 → 直交関数を基底とした無限次元空間内の一点

有限要素法の基本

偏微分方程式に対して重み付き残差法を適用し弱形式化した上で、メッシュの形状に対応した関数 (形状関数) を基底関数とした変分法の近似解法 (Galerkin法など) を用いて解析する手法。

![38_image_0.png](38_image_0.png)

2.1. **重み付き残差法と弱形式化**

移流拡散方程式:
(convection–diffusion equation)

\[
\frac{\partial u}{\partial t} +(v \cdot \nabla)u = \alpha \nabla^2 u + f
\]

残差 (residual):

\[
r(\mathbf{x},t) = \frac{\partial u}{\partial t} + (\mathbf{v}\cdot\nabla)u - \alpha \nabla^2u - f
\]

7. **重み付き残差法と弱形式化** **(Weighted Residual Method)**

重み付き残差方程式 **(weighted residual equation):** 
偏微分方程式の残差に重み関数を掛けて対象領域で積分した方程式。

\[
\int_{\Omega} w(\mathbf{x}) r(\mathbf{x}, t) \,d\Omega = 0
\]

境界条件 **(boundary conditions):**

\(\partial\Omega = \partial\Omega_D + \partial\Omega_N\)

Dirichlet **境界条件:**

u = u_D

解uは境界条件を満たすように設定し、重み関数は境界上で0とする。

Neumann **境界条件:**

\(\alpha (\nabla u) \cdot n = q_N \)

重み付き残差法を用いて定式化

\[
\int_{\partial \Omega_N} w(x) (\alpha (\nabla u) \cdot n - q_N ) \,d\Gamma = 0
\]

境界条件を考慮した重み付き残差方程式:

\[
\int_{\Omega} w(\mathbf{x}) \left(\frac{\partial u}{\partial t} + (\mathbf{v}\cdot\nabla)u - f\right) \,d\Omega + \int_{\partial \Omega_N} w(\mathbf{x}) \left(\alpha \left(\nabla u\right)\cdot\mathbf{n} - q_N\right) \,d\Gamma = 0
\]

弱形式化された重み付き残差方程式:

\[
\int_{\Omega} w(\mathbf{x}) \left(\frac{\partial u}{\partial t} + (\mathbf{v}\cdot\nabla)u - f\right) \,d\Omega + \int_{\Omega} \alpha (\nabla w) \cdot (\nabla u) \,d\Omega - \int_{\partial \Omega_N} wq_N \,d\Gamma = 0
\]

![56_image_0.png](56_image_0.png)

偏微分方程式に対して **重み付き残差法を適用し弱形式化** した上で、メッシュの形状に対応した関数 (形状関数) を基底関数とした変分法の近似解法 (Galerkin法など) を用いて解析する手法。

# 目次

1. 連続体力学と変分法の関係
2. **有限要素法の基本**
   - 2.1. **重み付き残差法と弱形式化**
   - 2.2. Galerkin法
   - 2.3. **形状関数による補間**
3. **安定化有限要素法**
   - 3.1. Upwind Galerkin法
   - 3.2. Streamline upwind Petrov/Gakerkin法
   - 3.3. **その他の安定化スキーム**