# 独立証明監査（担当分、対象 8aeb27f4df47a759723b03ce77fbe53adf4bb1d1）

## 判定
基準モデルの中心命題を偽とする反例は見つからず、全領域解析曲率上界と全g区間計算を再現した。一方、凍結済み非線形証明プログラム2本は「正確な有理数パラメータを外向き包含する証明」という仕様を満たしていない。これは文章上の不足ではない。原稿の査読可能性はFAIL（修正・再認証が必要）。ただし後述のscratch厳密再評価が通る範囲では、経済命題の変更なしに修復できる可能性が高い。

## Phase Aの出典境界
`proof_phase_a.md` をコード/既存監査資料に先立って記録。ユーザー依頼から点数値、非線形失敗、Leanの限界は事前に知っていた。原稿だけからCournot/利潤/厚生/基準Rosen論理/後ろ向き帰納法を再構成。半径・preconditioner有理化・生成関数の丸め欠陥はコードを読んで初めて知った。既存PASSは証拠として利用していない。

## 新たに発見した非線形証明書の欠陥（SUBSTANTIVE DEFECT / MAJOR）

対象 `verification/v2b_alt_quadratic_policy_interval.py:37–69`、`verification/v2b_alt_quadratic_rosen_interval.py:17–42,54–61`。

SymPy Rationalで定数を代入した後 `lambdify(...,modules='math')` を使うため、生成Pythonは例えば

```python
x1 = -71/500*g - 1/10*y**2 + 621/500
x5 = (1863/1250)*x2*x4
```

を実行する。`71/500` はintervalとの乗算より先に通常のbinary floatとなる。40桁区間演算に渡しても失われた正確値は復元されない。独立再現では

```
iv.mpf(71/500)
=[0.141999999999999987343457519273215439170598984, 同じ値]
iv.mpf(71)/500
=[0.141999999999999999999999999999999999999999862,
  0.142000000000000000000000000000000000000002732]
```

が非交差である。各式/導関数の有理数係数が個別丸めされるため、「単に近傍の一つのパラメータ点を正しく証明した」とさえ自動には言えない。原関数と導関数の恒等関係も独立の丸めを受ける。このままではexact θ0の根包含、微分上界、厚生区間の厳密な証明とは呼べない。

さらにRosen上界の判定自体が各区間端点をfloat化して通常の加算でrowを作っており、外向き丸めではない。今回得られた余裕は十分大きく、結論を反転させる証拠ではないが、仕様上の欠陥である。

最小修正は全有理数係数を区間有理演算 `iv.mpf(p)/q` として評価するprinterを使用するか、パラメータをsymbolicのまま正確intervalとして渡すこと。Gershgorin和も区間のまま評価してupper<0を判定する。数値候補探索と厳密評価を明確に分離し、符号・根包含・根面・全g・policy envelopeを再実行してfreeze manifestの保護対象修正を正規手順で再認証する必要がある。戻すべき最も早い段階は**該当非線形変種のStage 4/4A**、その後Stage7.5A/8の証明依存部分を更新。基準モデルのモデル変更や新パラメータは不要。

今回原稿/元証明コード/freezeは変更していない。scratch `exact_shadow_runner.py` において、SymPy Rational出力だけを厳密intervalへ置換し、Rosen row和を区間に保った独立再評価を実施した。これは原証明書の欠陥が消えたことを意味せず、修復可能性を調べる監査計算である。

## 基準モデルの独立解析再構成

`independent_proof.py` は既存コードをimportせず作成。

- 原始的効用から、期待n固定の需要 `p=a1−Bq+ηHn`。Cournot FOC `p_i−c=q_i` と期待充足から `M=I+B−ηH`, `Mq=1`。各市場の限界収益条件の凹性はown Bii=1。
- 正の固定点はq_i≤1/α。対角優位とoffdiag≤.242からinverse bound `||M^-1||∞≤1/D0`、D0=.758。
- `M_i` はi行列の対称2本edgeにβ/2を持ちrow norm≤β。
- `q_[i]=-M^-1 M_i q`、二階微分は `M^-1 M_j M^-1 M_i q+M^-1 M_i M^-1 M_j q`。
- 独立exact fraction再計算: `||q_[i]||≤25000/235359=.10622070963931696`, 二階微分上界 `.028026572464199727`。
- 利潤Hessian絶対上界 `h_exact=1250000000/6154873209=.2030911048130415 < .203092`。`κ−3h_exact=.24122668556087554`。紙面の保守上界も成立。symmetric pseudo-gradientの各行はdiagonal≤−κ+h、2 offdiag≤hなのでrow upper≤−κ+3h<0。全非対称cubeでRosen/own concavityを得る。
- IS対称点のunilateral matrix derivativeから原稿のscalar FOCとの差をSymPy exactで0と確認。対称経路で全xを動かす誤計算ではない。
- BはxとgにaffineでPSD coneがconvex。各regimeの(xA,xB,xC,g)∈{0,1}^4の16頂点について全principal minorsをexact計算。min principal minors: SW243/250, SU0, IS0。よって全cubeでPSD。非線形はz_i=x_i²∈[0,1]なので同じconvex argumentを適用可能。原稿にはこの短い証明がないが追加で解決できる。

## 全g計算の実行結果

環境 Python3 + numpy2.2.6/scipy1.15.3/sympy1.13.3/mpmath1.3.0（本監査で実行）。既存CIの再引用ではない。

| 実行 | 結果 | 証明上の解釈 |
|---|---|---|
| canonical Krawczyk原コード | PASS、1000セル、split0 | exact paramsをivで引数渡し、生成Pythonの定数割算は1/2,1/4,7/2,9/2のみでbinary exact。非線形の有理数丸め欠陥なし |
| canonical全g微分上界 | m':−.007970192997334808、(i−o)':−.015038883337750794 | 区間でupper<0を判定してからfloatは出力値だけに使用 |
| canonical frozen | C lower .0002346166230648035, IS lower2.441397037346308, SW upper2.4220784217382687, 全g SU upper2.423573564131729 | 500閉有理区間でISが各SU upperを上回ることをinterval比較 |
| canonical Pareto holdout | PASS gap[.0169346278736288503656923329640037513538356017,.0169346279394908146604805858713044084143956692] | 手書きiv有理数パラメータで厳密包含、非線形lambdify問題なし |
| nonlinear original Rosen | 見かけPASS SW1/SU1/IS5box | 係数とrow和の丸めのためexact certificateとして不適格 |
| nonlinear original policy | 見かけPASS100cells/split0、face checks PASS | 同じ係数丸め欠陥。数値的整合の証拠に限定 |
| nonlinear exact shadow Rosen | PASS SW1/SU1/IS5box、IS最大row upper約−.09496342972119372 | 厳密有理printer/区間row sumで再評価。修復可能性の根拠 |

元nonlinear policy出力の幅: frozen g=.05 C gap[−.00044039483411604,−.00044039483094063]、g=.005 gap[.00000090988090448,.00000090988408572]。未修復コードの区間はexact claimの証拠には用いない。shadow exact policyの完了結果は末尾に記載。

## 原稿の橋渡し不足（正しさと別）

| ファイル・位置 | 分類 | 欠落・最小修正 |
|---|---|---|
| 01_model.tex:75–76 | BRIDGE NEEDED | B PSD主張に上記「affine×convex→16頂点principal minors」2文と最小minor値。既存結果だけで足りる |
| A_proofs.tex:77–92 Eq app_Fm/app_Fo | ROUTINE〜BRIDGE NEEDED | M_{xA}の明示行列β/2[[0,1,1],[1,0,0],[1,0,0]]、M_{xC}も1行追加すればunilateral derivativeを逆算せず追える |
| A_proofs.tex:135–151 Eq app_krawczyk | APPENDIX DETAIL NEEDED | Z_k中心はnumeric rootを小数12桁→Fraction化、半径1/5000、CはJ0のnumeric inverse→12桁→Fraction化、iv precision35桁、scalar N=y0−F(y0,G)/F_y(Y,G)⊂intYとF_y<0を明示。Cが近似でよいのはinterval inclusionを最終検査するから。全セルでZ⊂(0,1)^nも明記。最小inclusion slack/機械コマンド/依存versionを小さな証明表で示す。原稿から現状これらの具体値は得られない |
| A_proofs.tex:153–168 | CLEAR | m',i−o'→0で一致→積分→全gのstrict signsは追える。端点は閉区間包含、ゼロ点ではwelfare等式、命題はg>0で妥当 |
| A_proofs.tex:186–191 +05_robustness.tex proof | APPENDIX DETAIL NEEDED + arithmetic SUBSTANTIVE DEFECT | nonlinear root box SU(.60,.67)×(.60,.65),IS(.60,.73)、面上の符号とPoincaré–Mirandaを述べ、100 depth×40counterpart分割、local boxes半径.0025、global Rosen verified boxes SW1/SU1/IS5とrow boundsを記載。特に厳密printer修復を先に済ませる必要 |
| 03_main_results.tex:136–140 | BRIDGE NEEDED | positive-depth feasible setは一般に0極限を失いclosedではない。F={g∈[0,1]:i_hat≥o_hat,i_hat≥m_hat,i_hat≥s}というclosed setをまず最大化、.05 strict candidateが0やSU/SWより高いため最適解>0と1段記す。主結果変更不要 |
| formal/V2bWelfareCore.lean:68–92 / A_proofs:211–219 | CLEAR | 4つのRat proxy比較のみ。実Nash根所属、全g、Cournot、SPNE、Rosenは証明しない、と原稿も正しく記述 |

Lean executableはローカルに無いため新しいLean buildは未実施。静的にInitのみ、4つのdecide +kernelと#print axiomsがあることは照合した。過去CIを今回の独立buildと呼ばない。

## 既存Stage資料とのPhase C照合

production/THEOREM_CERTIFICATE_MAP,REVIEWER_VERIFIABILITY_MAP、Stage8 freeze certificateは証明対象とscopeを丁寧に記しているが、非線形lambdifyの算術欠陥を検出していない。「exact rational targets」「outward-rounding」との記載だけで実装契約が満たされたことにはならない。Stage8がRosen/全g nonlinearをPROVEDとして依存しているため、保護ファイルを勝手に修正せず、再認証とmanifest更新が必要。Lean boundaryは整合。

## 改善の分類

文章だけ: PSD短証明、M_i明示、区間プログラムの具体仕様と推論橋渡し、closed-set最大化修正。
文章だけでは不可: 非線形有理係数とGershgorin丸めの実装修復・独立再実行・freeze再認証。
新しい経済命題が必要とまではこの証明監査から言えない。数理結果が偽と判断する証拠と、現証明書が厳密でない証拠を混同しない。

## 追記：scratch厳密再評価完了

`exact_shadow_runner.py verification/v2b_alt_quadratic_policy_interval.py` は全実行PASS。uniform interior face checks、100個の閉gセル・split0、厳密評価した微分upperは m'≈−.014278736686089652,(i−o)'≈−.01657547425035518。frozen g=.05 C gap=[−.000440394834116262265336895810820872699602680969,−.000440394830940852423049810616981973604402590329]で失敗を再現。g=.005 C gap=[.000000909880904270441158681794106261892984490111032,.000000909884085517109842656260341528629186347822752]、全g SU envelopeを上回ることを再評価。endogenous Pareto gap=[.0166011467983061462934235644053447100201778818,.0166011474094363189510871865311244032408292969]。

したがって、exact witnessで結果が偽であるという証拠はなく、修復版の厳密評価でも保持される。現時点の凍結済み証明書の不備は修復後ログを勝手に取り込んだことで解消したとは扱わない。原稿と凍結元コードはそのままであり、別の修復PR・Stage4A再認証・manifest更新が必要。

Leanの4つのproxy不等式はPython Fractionでも独立に正符号確認した（Lean実行とは別）：frozen_small≈9.098824947597428e−7、original-depthの反対向き≈.0004403948325299966、frozenIS−SW≈.00204149542676664、endogenous proxy Pareto≈.01660114710387123。実Nashの証明ではない。

追加のdomain検査としてcanonical krawczyk_SU/IS返却boxに0<lower<upper<1をassertする監査wrapperを実行し、1000セルすべてPASS。SU root-box全範囲[.7184088585949999,.7665537407619999]、IS root-box全範囲[.71846965156,.821930590514]（表示端点はfloat丸め、strict unit-cube所属判定自体はinterval比較）。元コードの当該domain assert欠落を今回の実行対象について補足検証した。
