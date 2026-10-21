# V2b Stage 13 — Economic Editorial Value Final Gate (Cheng–Huang を限定保留)

**Date:** 2026-10-21 JST  
**Subject:** *International Standards Coalitions and Endogenous Product Design*  
**Audited fixed source:** `b73469b1504b0c8e6680869fcdd93412b216c5ea`, draft PR [#5](https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/pull/5).  
**Review type:** 独立のAI支援・懐疑的RIO編集者による**経済学的掲載価値ゲート**。実在の学術誌の査読・人間専門家による独立審査・採択予測ではない。原稿、既存コード、証明の凍結情報はこの監査PRで不変更。  
**Excluded only:** Cheng–Huang (2025) の刊行版本文主要命題の完全照合。これは**延期**であり、重複リスクが消滅したことを意味しない。Cabral–Salant / Gandal–Shy / Takarada–Kawabata / Buchholz–Hattori / Brander–Spencer 等は依然として積極的に照合する。

## 最終判定

**RIO向け現行の full research article 投資：NO-GO（経済学的重要性・編集価値の観点）。**  
**限定的な理論的診断・短い research note としての再構成：CONDITIONAL GO（Stage 7.5への明示的差戻し、著者による研究投資判断が必要）。**  
**Stage 14 submission QA：NO-GO。** 技術的な Stage4A/Stage8 repair PASS と、本レビューの editorial-value 判定を混同しないこと。

これは `FATAL mathematical theorem false` / `DIRECT ABSORPTION` 判定ではない。掲載価値の現時点での**正の根拠がfull-length theory論文に十分でない**ことを判定する。RIOの採択が不可能だという断言でもない。

### なぜ現行full paperにNO-GOか（最短の論拠）

既知の①政府の標準化協定と第三国の外部性、②企業の内生的差別化・貿易利益、③内生化による固定予測の順位逆転を組み合わせ、④三国の固定深度・二国先行・第三国参加という特定の手順で、**exact θ の存在例**を証明している。全 g>0 を排除し、同じ政府ルールの固定設計反実仮想で正の三国協定を実現することは数学的にきちんとした強化だが、「いつ/なぜ一般にこの問題が生じるか」または「既存の有力な理論予測の射程をどこまで変えるか」の経済学的特徴づけを提示していない。直接三国提示では同じ深度で全員が賛成するので議題設定が本質的だが、その制度限定を現実の規則・データに結び付ける独立資料はない。

**唯一残る刊行候補：**「所定の二国先行・深度継承という標準化参加ルールで、政策後の私的製品設計の Nash 調整を停止した反実仮想なら協定可能と判定するのに、実際の継続ゲームでは全正深度で不成立になる。それでも、直接付与された三国標準化の厚生は分断を上回ることがある」という**制度特有の、条件付き比較の存在反例**。この狭さを認めた note には限定的価値がある可能性がある。

## 1. 編集的な意義の5問（元原稿の言い換えに頼らない判断）

| 価値テスト | 編集者側の回答 | 評価 |
|---|---|---|
| 読者が新しく学ぶことは何か | 技術標準の**条件付き全国家の厚生利益**は、二国先行・固定深度・第三国参加の**逐次同意可能性**を含意しない。同じ手順でも企業が事後設計を最適化すると、私的反応を固定した政策比較と合意可能性が逆になることがある | **YES, narrowly**。一般的な外部性/拒否権の新発見ではない |
| 既存研究の予測を明示的に反駁するか | 「企業設計固定での協定成立が一般的に正しい」と述べる主要な研究定理を特定・反証できたわけではない | **NO**。存在反例の一般的反証価値は限定 |
| 経済的な必要性はあるか | 残余属性の変更が輸出企業の利益と国内CSに逆符号の影響を与え、政府の参加余剰が変わる。自己最適化の自己利益一次効果はFOCでゼロ、ライバル設計の誘発効果はゼロでない | **YES**。これは説明力ある既存モデル内メカニズムだが、その基本成分は既知 |
| どの制度で役立つか | 二国が先行して技術的互換性深度を拘束し、第三国はそのままの深度で加入するか否かを選べる制度 | **CONDITIONAL**。現実にこのゲームの主要制約が同時成立する一次的制度証拠は現在ない |
| 再現可能で専門外読者が理解できるか | 17頁稿の技術修復、包括的な区間証明、包絡式は整合。だが文章/式を理解できることと掲載価値は別 | **Proof-oriented PASS は編集価値の代替にならない** |

## 2. 最も近い先行理論に対する「残差」検証

この表は確認済みの元資料の**取得範囲**に限定する。Cheng–Huang本文の不在を重複しない証拠としない。

| 文献・一次ソース | 実際の発見/モデルの主要点 | 今回と重なる機構 | 現在残る差分 |
|---|---|---|---|
| **Gandal & Shy (2001)** [刊行本文と要旨](https://www.sciencedirect.com/science/article/pii/S0022199600000672) | 三国政府の標準認識・連合、ネットワーク/変換費用、外国の標準を承認する制度、国民厚生 | 政府主体、国内消費者と本国企業の世界利益、連合・外部国 | 私的な技術外属性の**標準化後の**設計Nashを固定/最適化で比較する本結果は直接には取り扱わないと取得本文範囲で確認。モデルのSWは「無組合＝無世界承認」とは限らず、無条件比較不可 |
| **Takarada & Kawabata (2025)** [大学DP原本](https://oikono.econ.nagoya-cu.ac.jp/wp-content/uploads/sites/2/2025/02/DP701_Kawabata_February2025.pdf) | 地域/多国間相互承認と第三国の不利益・外部国の選択肢による多国間への障壁 | 「第三国が拡大を阻む」「地域→多国間で国家厚生が変わる」は既知 | 企業の事後的な非標準化属性設計が**同一政府ルールの参加予測を逆転**するという限定比較 |
| **Cabral & Salant (2014)** [IJIO刊行要旨・本文紹介](https://www.sciencedirect.com/science/article/pii/S0167718713000805) | 標準化のR&D誘因/free ride、別標準がイノベーション上有利になり得る | 技術標準の政策後の私的選択が厚生に作用することは既知 | 先行二国同意と第三国の継続外部選択肢/国別参加予測は別の対象 |
| **Brander & Spencer (2015)** [刊行版](https://www.sciencedirect.com/science/article/abs/pii/S1090944315000113), [NBER版](https://www.nber.org/papers/w21008) | 二国の国際寡占で輸出/貿易利益に**内生的な水平差別化**を導入。貿易利益・消費者利益・差別化インセンティブを比較 | V2bの国際販売・差別化・本国輸出企業の利潤への橋渡しは、2022年を待たず2015年から既知 | 三国政府が技術標準に合意するかどうかの継続国別利得を比較していない。**これを「残余新規性の圧縮要因」として必ず位置付け直す** |
| **Brander & Spencer (2022)** [RIO刊行全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8800905/) | 内生水平差別化が固定差別化時のBertrand/Cournot価格・利益順位を逆転する (Props 7–8) | 「差別化を内生化すれば予測順位が変わる」という一般的修辞は既存 | 三国家の条件付き厚生と政府の逐次参加判断は直接含まれない |
| **Buchholz & Hattori (2024)** [刊行要旨](https://www.sciencedirect.com/science/article/abs/pii/S0264999324000786) | 将来の部分連合の可否が現在の技術選択・公共財供給を逆転させ得る | 技術・連合形成の双方向性と逆説そのもの | V2bの企業設計は政府協定**後**、国際3製品市場のCS+輸出企業利潤を通じた政府参加比較。ただしこの順序差だけでは自動的な掲載価値にならない |

**分類：** current accessible predecessors = substantial COMPONENT OVERLAP; V2b residual = a potentially distinct **narrow equilibrium counterexample**. Without Cheng–Huang full published theorem audit, no complete priority clearance. 不確実性は所与として隔離し、本ゲートの経済的重要性判定をそれで甘くしない。

### RIOでの掲載類例との編集的な差

[RIO公式 scope](https://link.springer.com/journal/11151/aims-and-scope) は「経済的に重要なIO理論」も求め、経済実証・現実で検証可能な論点を主に重視し、**短い notes/commentaries も歓迎**する。一般理論のみに限定していない。

[Wang & Zhao (2026)](https://link.springer.com/article/10.1007/s11151-026-10069-x) は単純線形Cournotと費用構造から、合併利潤・CS・厚生に関する**読者が応用できるパラメータ条件と方向性**を導く。[Sorek (2026)](https://link.springer.com/article/10.1007/s11151-025-10046-w) は需要弾力性・品質革新の比較静学を扱う。これらは「数値存在反例がRIOで一律禁止」という根拠ではないが、現在のV2bは読者に持ち帰れる制度条件/経済条件の特徴づけが比較的弱い。

## 3. 誤解を生む可能性がある説明：政府自身が予測を誤るのか

**MAJOR — EDITORIAL CLAIM ALIGNMENT.** 原稿は `forecast error` や「政府の参加予測が誤る」を主要経済結果に掲げる。しかし**原ゲームの政府は完全情報・合理的後方帰納法によって企業の後続Nashを予見する**。したがって、現行ゲームで政府が**誤信念を持って実際に誤決定する**ことは証明していない。

厳密に言えることは：

> Holding private design at fragmented-market Nash levels generates an inaccurate **analyst's restricted-game prediction** of the governmental coalition outcome; the rational, informed government in the fully endogenous game does **not** itself make a forecasting mistake.

この違いは研究意義を損なわず、「標準政策評価で企業の反応を無視すると合意可能性を**誤判定する**」という政策評価・研究者のモデル化上の警告にできる。ただし実政府の認知バイアス・情報欠落・誤った政策採用の定理であるかのように語ることは禁止。

**最小修正候補:** Abstract, Intro, main-results, Discussion, Conclusion の `forecast error/mispredict` を `restricted-design assessment/forecast of feasibility` に統一。説明の一文で政府は両ゲームで自ゲームのcontinuationを正確に予見し、予測の誤りは固定設計で評価する**外部評価者**のもの、と明示。現実への関係は条件付き制度診断の範囲。

これは原モデルを変更せずStage13で修正可能。ただし full-paper significance deficit はこの語句置換だけで解決しない。

## 4. Full RIO paper vs shorter note の編集投資テスト

| 投資経路 | 残余の経済成果 | 学術的強み | 最強拒否理由/実行条件 | 推奨 |
|---|---|---|---|---|
| **A. 現行17頁のfull RIO paperをそのまま磨いて投稿** | 1 theta / particular A→B→C consent で反例、φ1/φ2存在 | 全g厳密証明、同一政府交渉手順のrestricted design反実仮想、条件付きPareto利得 | 重要な既知機構との増分が単一制度・数値存在例に限られ、制度的適用/パラメータ特性が不足。文章やCIを増やしても解消しない | **NO-GO** |
| **B. 研究ノート/短い理論noteとして再構成** | 「国別の継続利得を使わず条件付きIS Paretoだけ見ると協定可否を誤る。デザイン固定評価と後続設計Nash評価は別」という厳密反例 | 限定診断として鋭い; RIOはshorter notesに言及 | 明瞭な命題の三点セットと節点表、独立の経済的学習内容、証明の最小可読性が必要。二関数を過大な汎用頑健性としない | **CONDITIONAL GO** |
| **C. Full RIO理論論文の新たな貢献を狙う** | 経済的に解釈できる参加逆転領域の条件/技術・制度の分類など、*現在は未証明*の結果 | 成功すれば一般性とsignificant theoryを強め得る | 現在のStage13では許可しない理論変更。新規定理が既存一般理論に吸収されず実行可能かStage3/4A/6/7.5を再実施。例の追加やパラメータ微調整は禁止 | **今は投資不承認** |

**Noteでも必ず一段の厳密性を維持：** ①元政府制度で全g>0不成立、②restricted固定ゲームで適切な実行可能ISのみならず提案者にSU/SW全対案を上回る最適ISがある、③conditional endogenous ISはSWから全国家利得の改善（SUとのParetoではない）、④直接三国提案では成立するため制度依存、⑤p2のg=.05失敗とg=.005の小余裕を保持。

### Full articleへ足りない「ひとつの要点」

現状の中心は **controlled, existence-only institutional forecast contrast** にとどまる。それにどんな経済環境/条件で一般にこの違いが現れるかの理論的なクラス記述はない。存在例それ自体が必ず不十分だとする一般規則はないが、この特定反例は**従来「標準化すれば必ず協定成立」と予言されていた重要定理への反証**としては今の文献と結び付いていない。問題は証明の計算時間や論文長ではなく「読者の理解を何ほど変えるのか」である。

## 5. 再査読での価値を改善する最小修正（内容はまだ書き換えない）

| 優先順位 | 具体的な改善対象 | 論文位置 | 既存結果だけか | 成功判定 |
|---|---|---|---|---|
| 1 MAJOR | 政府の `forecast error` という誤解を `analyst's restricted-design prediction` に精密化。政府自体の誤認はモデル外、と断定 | main.tex Abstract/Conclusion, 00_intro, 03_results, 07_discussion | **Yes**, expository | 政府は両ゲームで完全情報の合理的主体という前提と矛盾しない |
| 2 MAJOR | 最も小さな独立の学習内容を1段落で示す：①国別各節点の比較、②設計反応→輸出利得/CS、③固定制約と設計Nashの**国際同意**の対比 | intro, welfare, results, discussion | Yes | Brander–Spencer/ Gandal–Shy/Takarada個々の既知発見を主張せず、国別 participation sign contrast のみを新規候補として位置付ける |
| 3 MAJOR | 議題設定反実仮想（直接全会一致IS）を中心のscope testとして付け、二国先行/固定深度が何を駆動したか表にする | results/discussion | Yes | 別の交渉ルールでは結果が失われると明示、実在規則の証明を作らない |
| 4 IMPORTANT | Brander–Spencer 2015 **国際貿易×内生差別化**の明示的な追加、2022の順位逆転との違いを論理で示す | literature; references.bib | Yes, once source verified | 「新しい国際差別化モデル」という過大な文言を削除 |
| 5 MINOR | 「falsifiable diagnostic」→「conditional observational diagnostic」、研究用内部メモ/Stage14文言削除、過密証明は付録に残す | discussion; robustness | Yes | 実証的に未検証な範囲を守る |
| 6 ESSENTIAL ONLY IF FULL ARTICLE | 経済的に読める符号逆転条件を解析的に定式化し、意味のある範囲・制約を示す。証明できなければ現行note案に撤退 | 研究Stage3/4A/6/7.5 | **No, new research** | Stage13で未証明の一般定理を捏造しない |

## 6. 強い懐疑的な拒否コメント

> The manuscript constructs a carefully certified numerical counterexample, but it does not yet establish a significant general economic contribution for a regular full-length theory article. Governments' strategic participation under standards and third-country spillovers have been analysed, as have endogenous horizontal differentiation, its effects on international profits, and reversals of familiar fixed-differentiation predictions. The residual claim is a change in coalition feasibility under one bilateral-first inherited-depth agenda and one parameter vector. Direct three-party unanimity at the displayed depth would produce agreement, so the agenda restriction is essential; historical standardization examples are not evidence that the specified consent protocol and absent renegotiation are operative in real standards bodies. Moreover, the current term 'forecast error' may be misleading: governments in the model correctly anticipate the private-design Nash continuation, whereas only an analyst using a different restricted-design game would mispredict the outcome. Exact interval proofs make this a valid, interesting diagnostic, but not automatically an economically important full paper. I would not invite full-paper external review in this framing; a short, sharply delimited theory note may be viable if its contribution and proof are made transparent.

## 7. 最も強い推薦コメント（残存貢献に限定）

> A clean diagnostic is that welfare improvements from a hypothetical complete standard do not establish that a staged consent protocol can reach it. Governments decide against intermediate alternatives, and firms may redesign product features outside the standardized interface after commitments. The author proves a controlled comparison with identical governmental procedures, welfare accounting and economic primitives, except for whether private designs are permitted to adjust. The internationally coordinated outcome is supported by unanimous welfare gains relative to fragmented standards, yet becomes politically unreachable under the staged agenda; it would be predicted feasible under a restricted fixed-design policy assessment. The proof covers every positive compatibility depth at the exhibited parameter vector, not just an arbitrarily sampled grid. A short note that clearly distinguishes this specific conditional, model-based feasibility mistake from generic network inefficiency would teach a useful caution to readers constructing policy counterfactuals. The contribution is narrower than a general theory of international standardization and its relevance beyond the stipulated protocol would remain to be investigated.

## 8. Stage routing / stop rules

- **Current results:** 17-page draft and proof script **unchanged** in this PR. Fixed source PR#5 HEAD had 15 green workflow runs (Stage4A/Rosen/nonlinear g/full freeze / Stage9/Stage10/Lean proxy) at audit time. This establishes reproducibility and mathematical support, not editorial acceptance. Evidence: https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39573603416 and https://github.com/ryotamatsuki/standards-coalitions-differentiation-cournot/actions/runs/39573603726 .
- **Decision governance:** Stage13 cannot relabel the original full-paper GO while its economic-completeness issue remains; **reopen Stage7.5** for `RESEARCH NOTE / REFRAME` decision and obtain explicit author permission before producing a replacement note manuscript. Stage8 freeze of the economic theorem stays immutable; proof recertification v2 stays documented. Stage13 prose edits allowed only after path decision.
- **Cheng–Huang:** paused from THIS value evaluation per user. Keep priority status `UNRESOLVED`, neither PASS nor FATAL. Before journal submission it must be independently resolved or the author knowingly account for the unverified priority risk; postponement is not source verification.
- **Author intellectual sign-off:** pending. Formal journal submission not done.
- **Suggested Stage7.5 test:** Decide whether the retained 3-piece claim (all-g failure / restricted feasible IS / conditional Pareto gain) alone justifies a theory note when strongest Gandal–Shy, Brander–Spencer (2015/2022), Takarada–Kawabata and Buchholz–Hattori are acknowledged. If **NO**, stop rather than stretching a long narrative. If **YES**, authorize a concise note architecture while keeping accessible full proof appendix and reproducible certificates. Do not add parameters or proofs merely to raise the page count.
