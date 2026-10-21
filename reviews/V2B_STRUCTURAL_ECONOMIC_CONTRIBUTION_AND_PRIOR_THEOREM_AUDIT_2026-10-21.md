# V2b 研究貢献の構造監査 — モデルの原始的構造・内生差別化・経済的帰結・先行研究の命題距離

**Date:** 2026-10-21 JST  
**Object:** International Standards Coalitions and Endogenous Product Design (V2b)  
**Fixed manuscript/proof base:** audit/stage13-full-paper-contribution-reappraisal-20261021（親のStage13修復源 b73469b1504b0c8e6680869fcdd93412b216c5ea）。  
**Method:** 再解釈・敵対的貢献監査のみ。元の原始モデル、定理、CI、Theory Freeze、論文の本文を編集しない。数学的な既報証明を新たに独立形式検証したという意味ではない。  
**Deferred:** Cheng–Huang (2025) の掲載版命題全文照合をユーザーの意向により保留。未照合は「重複なし」を意味しない。

## 0. 判定の修正

**現在の証明済み成果には「通常のフルペーパーとして構成する合理的な貢献候補」がある。しかし、現状の証明だけでRIO掲載価値が無条件認証されたとはいえない。結論：FULL-PAPER DEVELOPMENT = CONDITIONAL GO; SUBMISSION = NOT CLEARED.**

従来の両極端――「既知モデル要素が多いのでフルペーパー不可」と「Brander–Spencerと政策結果が違うのでフルペーパー確定」――をともに退ける。審査単位は（i）既知の数学的手法、（ii）新しく組み合わせた経済的意思決定問題、（iii）そこから成立が厳密に示された非自明な命題、（iv）既知の先行命題から直接/構造的に吸収されるか、（v）学術誌が必要とする重要性である。

**主たる貢献の最強の候補（一つの一体的結果）：** 政府の技術的相互運用性を選ぶ段階と、企業が非標準化属性の水平的差別化を改めて最適化する段階を区別すると、企業設計反応が国内CSと本国企業の世界利益の帰属を変え、二国先行・深度継承・第三国加入という制度の参加条件を変える。固定設計反実仮想で実現可能な三国協定は内生設計下で**全正深度**不成立となる一方、条件付き三国協定は分断より各国の厚生を改善し得る。モデル固有の存在命題であり、一般的な不成立原理、政府の認知的誤予測、全スタンダードへの応用とは主張しない。

## 1. モデルの構造と単なる設定ではない役割

| 構造 | 原始仮定・意思決定 | 識別される経済学的役割 | 理論的新規性の程度 |
|---|---|---|---|
| 3政府 + 3本国企業 + 3分割市場 | 同じ3企業が全市場で数量競争、政府iは国内CSと本国企業の**世界**純利益を評価 | 国内の消費者便益と外国で稼ぐ企業利潤を一国の参加余剰として接続する、政治経済的 incidence | 国民厚生/国際寡占の枠組み自体は既知（Gandal–Shy、Takarada–Kawabata、Brander–Spencer） |
| H と X の**別の変数** | H_ij=g は共有する技術的interface互換性、X_ij=(x_i+x_j)/2 は標準化されない製品属性の同質性 | interfaceの合意は製品全体の同質化を強制しない。標準化後に企業に選択余地を残す | 未完成/不完全標準はCostinot 2008等に既知、**残余属性の政策後内生Nash**がV2bの設定上の差分 |
| 効用・需要/ネットワーク | U=a1'q − (1/2)q'Bq+eta q'H n^e, B=rho H+(1−rho)X; Cournot fulfilled expectations M=I+B−eta H | 互換性は便益と商品代替性を別経路で変え、企業の差別化はBを通じ代替性を変えるがHを自動的には変えない | 独自のparametric specificationだが、これだけを発明/一般機構の新規性としない |
| 企業はx_i∈[0,1]を一回払いの世界設計費 kappa(1−x_i)^2/2 のもとで選択 | 各企業は政策S,gの**後**に私的Nash設計、さらに後に数量Cournot | 同じ標準政策が企業の残余同質性をendogenousに変える。加盟企業/第三国企業が異なる設計を選び得る | 内生水平差別化（Brander–Spencer 2015/2022）は既知。**政府標準協定後の非標準化属性**に限定した結果は差分候補 |
| 企業の完全な戦略空間と均衡の一意性 | 全非対称x-cubeのRosen、根包含で政策ごとに唯一の設計Nash | 政府はゲーム内で合理的に企業の反応を予見でき、均衡選択の恣意性がない | 主に定理を支えるtechnical rigor。単独で主たる経済学的新規性とはしない |
| A→B→C加入申請→A/B拒否権、深度g継承 | Aがbilateral gを提案、B受諾、C申請、A/B承認、設計→Cournot | 直接三国提案と異なる**継続外部選択肢**を生む。Cの比較はISとSU outsider、BのfallbackはSW | 参加/veto/経路依存は既知。**設計を動かすと同じ制度の参加符号が変化**が候補 |
| 設計固定のrestricted counterfactual | x_iを全履歴でSW Nashの値に強制、政府メニュー/費用/需要の経済的原始は維持 | 最も重要な対照実験。市場成果と参加可否への「設計調整を評価しない」ことの影響を識別 | 既知のfixed/endogenous方法の新用途。これは**別ゲーム**でありoriginal gameの別均衡ではない |

**構造の独立性**だけを経済貢献とは認定しない。必ず次節の帰結に接続する。

## 2. 現在すでに証明・監査された経済学的帰結を監査単位で分離

| 候補命題 | 本当に得られた帰結と量化 | 先行研究への依存/吸収リスク | 査読上の地位 |
|---|---|---|---|
| R1 内生設計の成立・一意性 | exact theta0、S∈{SW,SU,IS}、全g∈[0,1]で各企業の完全x-cube設計Nashが一意・内点 | Rosenの一般均衡一意性手法は既知。**有意義な証明上の保障** | PROVED technical foundation、単独主要新規性はLOW |
| R2 政策に対する企業設計反応 | SUのg=0で u'(0)≈+0.060810232, v'(0)≈+0.032304817。xは「同質化」指数なので加盟/外部企業とも差別化を減らし、加盟国側が局所でより強く反応 | Brander–Spencerなど内生差別化の存在は既知。**政府の政策ショックに対する加盟/外部企業の異なる反応**は差別化候補。ただし符号・順位は現在単一theta局所 | POINTWISE COMPARATIVE STATIC; stand-alone general theorem NOT YET PROVED |
| R3 国別厚生への戦略的波及 | 国民厚生 W_i=CS_i+Pi_i。企業iの設計FOC Pi_i,x_i=0でも、政策誘発総効果には全企業のCS変化と他社のxの本国企業利益への影響が残る。会員国g=0で直接+0.0067679241、消費者誘発−0.005216220、他社設計の自国企業利益誘発−0.009853524、純−0.008301820 | FOC/包絡は既知の道具。**国別標準化参加にこのincidenceを適用した具体的な反転結果**が貢献。一般的な包絡恒等式自体は新定理としない | VERIFIED at theta0, mechanism bridge HIGH |
| R4 同じ交渉ルールでの政府参加逆転 | canonical exact theta0、endogenous設計なら **all real g>0** について m(g)<s と i(g)<o(g)。restricted frozen designでは g=.05のISが参加可能かつ全可能SU/SWよりAに有利、proposer-optimal positive-depth ISが存在 | 連合参加阻害だけはGandal–Shy/Takarada–Kawabata既知。設計内生化による同一制度での**政府feasibility set**の変化が独立の主要成果候補 | **MAIN PROVED INSTITUTION-SPECIFIC EXISTENCE RESULT** |
| R5 社会厚生/実装可能性の乖離 | conditional true IS at g=.05 makes i(.05)−s≈+0.016934628 for EVERY country, yet no positive-depth equilibrium union under AB-first. 直接ISをSWの代替で全会一致に提示すれば成立。g=.05で o>i>s>m（別々の国別継続対象） | 第三国による協定阻害・望ましい協定不成立は既知（Petropoulou2013等）。**R4と同時に内生設計によって実装可能集合が変わる**と一体化した貢献 | SECOND MAIN CONSEQUENCE OF R4; not independent novelty |
| R6 設計関数への頑健性/限界 | phi=x^2を別証明。endogenousは全g排除、frozenでの存在のみg=.005、事前同深度g=.05 C参加はNEGATIVE (約−0.000440395)。成功g=.005 C差は約+9.1e−7 | 自由な関数形一般化は証明なし。正の余裕は小さい。一般性評価の境界を示す点は価値 | STRICTLY LIMITED DIAGNOSTIC; no broad function portability theorem |

### モデルからの明示的な分配帰属

3つの国の市場が同一で各企業が同一数量を各国で販売するため、**同じ一つの制度・設計プロファイルにおいて各国国内CSは同一**。したがってSUでの加盟国/外部国厚生格差は本国企業世界利潤・設計費の差のみ：
o(g)−m(g)=Pi_C(x*(SU,g))−Pi_A(x*(SU,g)).
これは定義からの帰結であり、新規定理ではないが、**対称な国内消費者便益があっても第三国の参加外部選択肢が非対称になる理由**を経済的に説明できる。政策gを通じCS全体が変化する効果と、同一制度内の国間帰属差を分けると説得力が上がる。

### 預言を過大にしない

- 実政府は完全情報で設計のNash継続を正しく後方帰納している。forecast errorは設計固定を仮定する**外部分析者の比較**であって、政府の錯誤ではない。
- \(g=.05\) は合理的反例深度、最適深度の同定ではない。
- Pareto は IS と SW の比較であり IS と SU の全国家比較ではない。
- 「全g」はtheta0固定での全深度。全theta、全交渉制度、全微分可能設計関数には言えない。
- R4とR5は**一つのメカニズムが生む2つの帰結**であり、既知の外部性と包絡式を新定理として水増ししない。

## 3. 先行研究との命題距離 — 先行要素の単なる表面比較を超える

取得状況表記：FULL（刊行版の可読本文/公開DP）、ABSTRACT（刊行要旨と一部公開本文）、PRIOR（先行GitHub監査で原文確認）。Cheng–Huang (2025)は本表では保留。

| 研究 | 観察単位、実際の意思決定、主要結論 | V2bで変わる経済的因果連鎖 / その研究を使ってもまだ必要な証明 | 現時点の吸収評価 |
|---|---|---|---|
| **Brander & Spencer (2015)** Research in Economics 69:157–165 | 2国2企業、輸出・内生水平差別化・数量/価格競争、貿易の発生/利益/市場成果。差別化投資は企業内生 [ABSTRACT+公開イントロ] | V2bは政府の標準化合意を**先行**させ、後続の企業の残余属性Nash→国別参加厚生→第三国加入/拒否を後方帰納。貿易利益は既知、政府feasibility結果は同論文の公表された主結論にない | STRONG COMPONENT OVERLAP; R4への直接吸収は未確認 |
| **Brander & Spencer (2022)** RIO 60:1–27, Props7–8 | 参入企業の模倣/差別化、Bertrand-Cournot価格・利潤順位、差別化費用閾値 [FULL open-access HTML] | V2bは競争様式をCournotのまま固定し、**外生技術標準化政策→企業Nashの反応→国別参加結果**を比較。固定/内生順位の逆転の一般語りは既知 | STRONG COMPONENT OVERLAP; R4への直接吸収は未確認 |
| **Zhou, Spencer & Vertinsky (2002)** JIE 56:205–232 | 政府の品質投資補助・課税→企業の内生垂直品質→価格/数量、国際競争と最適貿易政策 [ABSTRACT+刊行ページ詳細] | 「政府政策の後に企業品質を内生決定し輸出利潤が変わる」は**既知**。V2bでは政策は標準化参加/互換性で、選択は**水平的な残余属性**、被説明結果は三国の**coalition feasibility**である | 新たなHIGH-RISK prior。原論文の全命題照合が必要 |
| **Jeanneret & Verdier (1996)** EJPE 12:253–271 | 垂直的品質差別化、標準化/貿易政策、政府事前commitmentが民間標準化選択と関係 [ABSTRACT] | 政府コミットメントと企業差別化の基本相互作用は新規主張不可。別の尺度(H vs X)と三国政府同意の反転に絞る | HIGH-RISK overlap; full theorem unavailable |
| **Casella (2001)** Kyklos 54:243–264 [NBER w5853 ABSTRACT] | 民間の技術標準連合/市場統合、標準間harmonizationと製品差別化の併存 | harmonizationとvariety/differentiationの両立自体を初発と主張不可。V2bでは政府間協定の後に独立属性が各社で最適化 | COMPONENT OVERLAP |
| **Costinot (2008)** JIE 75:197–213, published MIT PDF | NT/MRの硬直的政府間制度、quality/compatibility standards、異なるproduct versions、部分的essential standards、strategic profit shifting。EUの essential requirements は製品全体を完全に規定しないと明示 [FULL published PDF] | **技術的標準は製品全体を定めない**という着想は既知。V2bはその**残余非標準化attributeの事後企業設計Nash**を解き、3政府による事後加入への参加利益比較を証明する点が焦点 | 特にモデルの構造について新たな強い近接文献。R4差分あり、H/X分離のアイデア優先権は主張不可 |
| **Petropoulou (2013)** OEP 65:372–393 | 2国市場の内生的minimum quality standards、垂直的な品質差、各国厚生、相互調整で世界最適な規則を実現できない場合 [ABSTRACT、Oxford WP] | **標準化での厚生最適と非協調国際協定の乖離は既知**。V2bで残るのは、技術interface/残余水平属性を分けた設計Nashの政策後反応により**同じ三国参加手順の固定/内生予測が反転**すること | HIGH-RISK prior for R5; R4の条件付き比較を独立に見せる必要 |
| **Gandal & Shy (2001)** JIE 53:363–383 | 3国、政府による外国標準認証・二国union、世界企業利潤と国内CS、network/compatibility効果 [prior source audit + publisher] | 国家/非加盟国の参加・国別厚生それ自体は既知。V2bのR4は政府の合意の後に企業が非標準化属性を再設計する点と fixed/endogenous government choice 比較 | CORE PREDECESSOR; no wholesale priority |
| **Takarada & Kawabata (2025)** Nagoya DP701 36p | 3国、地域MR/multilateral MR、外部国の阻害、政府による継続的minimum standards設定→企業Cournot数量決定。本文p5–6: firms have no incentive to voluntarily raise regulated minimum standard; x_iのような独立した事後horizontal private designはない [FULL DP] | 参加の阻害は既知だが、**政策後 private residual product design が国別参加を逆転**させることは同DPの政府 standards→数量ゲームにはない。MR/NTとV2bのinterface linkは**異なる制度**であることも明示 | CORE PREDECESSOR; R4 may be distinct |
| **Buchholz & Hattori (2024)** Economic Modelling 135:106722 | 先行の技術選択が後続部分連合の可能性に反応し、技術導入と公共財供給/厚生に逆説的結果 [ABSTRACT] | V2bは因果順序が政府の技術標準合意**→後続の企業残余設計**、商品市場とnational exporter profitsを接続。順序違いだけでnoveltyは認定しない | COMPONENT OVERLAP |
| **Cabral & Salant (2014)** IJIO 36:48–56 | 技術開発R&Dにおける標準のfree-ridingと投資減退 [ABSTRACT+discussion] | post-standard private investment feedbackは既知。V2bは製品代替性への残余属性の変化、国民厚生帰属と三国参加制約に限定 | COMPONENT OVERLAP |

**文献上の重要な訂正:** V2bは「政府による標準政策後の内生的企業設計」も「政府間の厚生最適標準が不達」も初発と主張しない。Brander–Spencer 2015/2022、Zhou et al. 2002、Jeanneret–Verdier 1996、Petropoulou 2013、Costinot 2008を包括して評価する必要がある。今回の調査では**R4の厳密な三国逐次同意の固定/内生比較を直接証明した先行命題は特定できなかった**が、網羅的不存在証明でもない。

### Primary material / DOI ledger

- Brander and Spencer 2015: https://www.sciencedirect.com/science/article/abs/pii/S1090944315000113 (doi:10.1016/j.rie.2015.02.007)
- Brander and Spencer 2022: https://link.springer.com/article/10.1007/s11151-021-09822-1
- Zhou, Spencer and Vertinsky 2002: https://www.sciencedirect.com/science/article/pii/S0022199601001180
- Jeanneret and Verdier 1996: https://www.sciencedirect.com/science/article/abs/pii/017626809500016X
- Casella NBER: https://www.nber.org/papers/w5853
- Costinot published PDF: https://economics.mit.edu/sites/default/files/publications/standards_final.pdf
- Petropoulou 2013: https://academic.oup.com/oep/article-abstract/65/2/372/2912954
- Gandal and Shy 2001: https://www.sciencedirect.com/science/article/pii/S0022199600000672
- Takarada and Kawabata DP701: https://oikono.econ.nagoya-cu.ac.jp/wp-content/uploads/sites/2/2025/02/DP701_Kawabata_February2025.pdf
- Buchholz and Hattori 2024: https://www.sciencedirect.com/science/article/abs/pii/S0264999324000786
- Cabral and Salant 2014: https://www.sciencedirect.com/science/article/pii/S0167718713000805

## 4. 独立した研究貢献の強さ（リストではなく定理単位に評価）

| 研究貢献ラベル | 現時点の独立性評価 | 「フル論文の主要貢献」としての適格性 | 最も強い査読反論 |
|---|---|---|---|
| C0 制度Hと残余設計Xの分離 | 新しい切り取り方だがモデル構造は類例多数。Costinot essential vs nonessentialも既知 | **MODEL FOUNDATION; MAIN RESULT NOT BY ITSELF** | 変数を一つ増やしただけ |
| C1 標準化が企業の残余設計Nashを変え、加盟/部外国設計応答が異なる | exact theta0で支持、一般経済条件と強制符号は未証明 | **STRONG SECONDARY CONTRIBUTION CANDIDATE**, subject to analytical regime/parameter characterization | R2は単一ベクトルで数値比較しただけ。既存内生差別化の自然応用 |
| C2 企業自身の最適反応→競合企業と消費者への外部性→国家厚生符号の逆転 | 明確な因果連鎖と分解を持つが包絡恒等式は既知 | **MECHANISM LEMMA / CENTRAL INTERPRETATION** | 一次のFOCと同じく標準計算、独立の一般結果ではない |
| C3 固定設計の政府協定成立予測が内生設計で全g不成立に変わる | exact theta0 + entire g + full proposer menu の厳密存在命題 | **STRONGEST PROVED MAIN CONTRIBUTION**（理論的に独立の特定実装問題。ただしpriorityとimportance最終未確定） | 既知の政府coalitionと既知のprivate designを特殊なagendaとwitnessで組んだだけ |
| C4 条件付き全国家Pareto改善と実装不可能 | R4と結合して強い、単独は既知の制度的非効率 | **JOINT IMPLICATION, NOT INDEPENDENT MAIN THEOREM** | Petropoulou等が同様の不達を説明。直接grand agendaなら問題が消える |
| C5 二関数phiの存在確認 | 2つの点のexistence、同深度失敗・小正marginを維持 | **BOUNDED ROBUSTNESS CHECK** | 過大なfunctional generalityに相当しない |

### 投稿用に許容可能な中心claim案

> **Technical standards and product design are distinct choice margins.** In a sequential international standards game, governments commit to interface compatibility before firms re-optimize residual horizontal differentiation. This private adjustment changes consumers' surplus and the international incidence of producers' profits and can therefore reverse the *set of agreements rational governments are willing to implement*, rather than merely reversing oligopoly profit rankings. Under an explicit bilateral-first inherited-depth procedure, we exhibit a game in which a multilateral agreement is attainable if private attributes are counterfactually held at their fragmented-market designs, but is blocked at every positive technical-compatibility depth when those attributes are optimized. Nevertheless, a hypothetical direct grand agreement at a positive depth Pareto-dominates fragmentation in the true design equilibrium. This is an institution-specific existence result, not a general non-cooperation theorem.

「first」「general」「policy optimal」「governments mistakenly predict」などの語は必要な証拠がない限り使用しない。

## 5. Full paperへの論理的ルート：新たな構造分析の優先順

**P1 / Stage3→4A→6→7.5:** 固定基準SWで政策強度の局所変化に対する企業設計反応を、一般thetaのシンメトリ的な基準設計根 z(theta) と非対称SU中の差 u'(0),v'(0) によって**解析的に特徴付け**する。費用kappa、ネットワーク便益eta、rhoが response差をどう決めるかを定理化。単に一地点の数値符号を繰り返さず、逆転が成立する条件が経済的に読めるかが鍵。現時点でその一般的符号・順位は未証明。
**P2 / same gated path:** 国別厚生について W_A,g vs induced CS and rival-export-profit effects の条件式を作り、固定設計時の参加m^hat'(0)と内生時のm'(0)の符号逆転が起きる**十分条件**または明示的非空領域を示す。包絡式自体は新規命題としない。局所符号は政府均衡全gの証明と混同しない。
**P3 / beyond local:** 固定theta0全g符号の既存強みを維持し、P1/P2で得られた領域が全g参加不成立を含意するのか、別途のuniform certificateが必要なのか区別する。正の体積のtheta領域を厳密に再認証できるならフルペーパーの説得力向上。単なる「unquantified open neighborhood」以上の経済学習内容を目指す。
**P4 / agenda scope:** AB-first/unchanged-gとdirect unanimous offerの比較を形式的に**機構境界**として整理する。別agendaでも不成立という一般定理は未証明。境界を示すこと自体に政策解釈価値があるが最適制度は導かない。
**P5 / negative stop:** P1/P2/P3が既知理論から直接導ける、あるいは経済条件の説明がわずか/一般性が極小なら、note案に戻すか研究停止を評価。パラメータチューニングや無関係な拡張で結果を救わない。

**研究投資の閾値：** 主要命題C3はすでに数学的に成立しており「失敗したから証明をやり直す」としない。追加の研究が価値を持つのはC1/C2のメカニズムが一般条件で特徴づけられ、C3のなぜ・いつを説明できる場合に限定する。従来のレビューが粗い「技術的存在例」で済ませたところからの本質的な前進点。

## 6. Stage13 editorial decision / independent constraints

**現在の最適な研究構成：**
1. Model conceptual distinction: government interface decision H, firms' residual nonstandardized design X, international home-profit ownership.
2. Endogenous design Nash lemma with full asymmetric strategy-space existence/uniqueness (technical pillar).
3. Policy-to-design response comparison and the two-country/outsider divergence. **At exact theta present as diagnostic; generalization only after separate proof.**
4. Incidence/envelope decomposition linking private adjustments to national consent.
5. Main one-piece regime feasibility reversal theorem (entire depth + all proposer alternatives).
6. Direct multilateral Pareto welfare vs original staged inability; explicit alternative agenda test.
7. Carefully scoped nonlinear negative/positive robustness and discussion; proofs reproducible.

**Final state:** CONDITIONAL GO FOR FULL THEORY PAPER *DEVELOPMENT*, NOT SUBMISSION READY. 中心的な新規性候補C3は有効。ただし新たに発見したZhou–Spencer–Vertinsky、Jeanneret–Verdier、Costinot、Petropoulouは「政府政策×私的製品特性」の重複検証に必須。Cheng–Huang全文保留は維持。新しい定理を自動で証明済みにしない。著者のモデル・Freeze・元原稿・PR#3/#5をこのaudit PRで変更しない。
