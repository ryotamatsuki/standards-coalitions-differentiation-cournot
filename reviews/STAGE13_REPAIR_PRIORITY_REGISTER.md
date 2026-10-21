# Stage 13 修正優先順位台帳（監査のみ、2026-10-21 JST）

対象 SHA: `8aeb27f4df47a759723b03ce77fbe53adf4bb1d1`。本文・パラメータ・凍結証明コードは変更していない。

| 優先順位/ID | 重大度 | 問題と根拠 | 最小修正案 | 対象箇所 | 理論凍結への影響/戻る段階 | 閉鎖条件 |
|---|---|---|---|---|---|---|
| 1 P1 | MAJOR — CERTIFICATION REGRESSION | 非線形lambdifyの有理係数がfloatで先評価。真の71/500とiv.mpf(71/500)が非交差 | 有理係数をiv.mpf(p)/qとして評価、候補探索のfloatと証明評価を分離 | verification/v2b_alt_quadratic_policy_interval.py37–69; v2b_alt_quadratic_rosen_interval.py17–42 | 凍結2ファイルを変更するため、該当変種Stage4A→7.5A→8の依存部分再認証。silent hash更新不可 | 有理定数包含regression、根面/全g/厚生/envelope再認証、正規manifest更新。scratch shadow PASSは修復可能性だけ |
| 1 P2 | MAJOR — CERTIFICATION REGRESSION | Rosen上界の端点float化とfloat加算には外向き包含保証なし | diagonalとabs(symmetrized offdiag)の和を区間内で計算しupper<0を判定 | nonlinear Rosen54–61 | P1と同じ。経済モデル変更は不要と現在の証拠は示す | 全非対称cube再認証と出力slack |
| 2 N1 | UNRESOLVED — MAJOR novelty gate | Cheng–Huang full main propositions等の命題単位吸収が未閉鎖 | 一次本文・proofの正確な比較、取得不能部分は保留、未取得を独立性と数えない | 06_related_literature; STAGE13_PRIOR_ART_COMPARISON.md | 機能上Stage6再開。吸収実証ならStage6 ROLLBACK、未取得だけで吸収確定にしない | 主体/順序/品質/拒否権/厚生/固定設計比較/一般定理の含意を特定 |
| 3 V1 | MAJOR proof exposition | baseline Krawczykの具体箱・半径・有理化・scalar Newton省略 | appendixに半径1/5000、12桁Fraction化、35dps、C有理化、scalar interval Newtonとunit cube包含を記す | A_proofs134–151 Eq35 | Stage13、凍結モデル変更なし | 読者が根包含の仕様を推測せず識別できる |
| 3 V2 | MAJOR proof exposition | nonlinearの曲率/根面証明が一段のcertificate参照に留まる | repaired arithmetic後、SU/IS箱、面符号、Poincare–Miranda、Rosen row上界、全g partitionを付録に記す | A_proofs170–191; 05_robustness44–68 | Stage13、P1/P2修復に依存 | 根→Nash→微分→政府不等式の連結が原稿内で追える |
| 4 E1 | MAJOR economic mechanism | 費用節約にもかかわらず企業net incomeが減る理由を数値だけで説明 | NashのΠ_A,xA=0を使い、CS全設計項とrival-design profit項に分解。rootの有限差分診断はCS≈−.00521622、rival profit≈−.00985352 | 04_welfare62–97 Eq21 | Stage13、既存FOCの説明。新経済命題不要 | 自己最適化と他社反応の帰属を説明 |
| 5 E2 | MAJOR editorial value, conditional | 単一vector/特定agendaの診断が独立した掲載価値を持つか | 全gがtheta/制度の一般性でないことを維持し、最大claimと最強parent theoryを比較。Brander–Spencer2022も追加 | Intro, literature, discussion | 現存結果の限定的価値を支持できなければStage7.5再判断。文章で重要性不足を隠さない | 狭い診断として価値があるという証拠付き投資判断。拡張は自動承認しない |
| 6 V3 | MINOR bridge | positive-depth acceptance set自体は一般にclosedでない | g=0を含むclosed weak-acceptance setを最大化、strict .05 candidateで0およびSU/SWを排除 | 03_main_results136–140 | Stage13、主命題変更不要 | compactness argument2文で補完 |
| 6 V4 | MINOR bridge | B PSDを主張のみ | affine/convexと16頂点全principal minor非負の短証明 | 01_model75–76; appendix | Stage13、既存原始仮定のみ | PSDと境界非strict concavityを区別 |
| 6 E3 | MINOR interpretation | m−sを初期B同意条件と読める表注 | m−sは終端SU比較、ISを予見する初期同意はi−s、i−mはAB accession vote、と明示 | 03_main143–151; consent table caption | Stage13 | 意思決定主体と比較節点が一意 |
| 7 E4 | MINOR scope/style | falsifiable diagnosticは一般予測でなく観測要件 | observational diagnosticにし、条件付きモデルテストの意味を限定 | 07_discussion62–75 | Stage13 | 普遍的方向予測を付加しない |
| 7 E5 | MINOR style | 研究内部メモ、反復、政府評価の時系列表現 | Stage14 pending/Stage10 bibliographyメモを投稿本文から除き、anticipateという後方帰納表現にする。負結果は必ず残す | 06_lit56–60; 05_robustness71–98; 07_discussion98–109; references.bib | Stage13 | CORE/HELPFUL/APPENDIX/DELETE台帳に従いbridgeを残す |

**文章だけで可能:** V1/V2の説明部、E1、V3/V4、E3–E5。**文章だけでは不可:** P1/P2の証明実装と再認証、N1の一次資料照合。**新命題が必要と確定した問題:** なし。ただしN1で吸収される、またはE2で残存成果の価値が不足と判断された場合、現存結果の言い換えで解決せずStage6/7.5へ戻る。

**FATAL:** 今回、数学命題の偽または既存定理への直接吸収を確定した案件はない。FATALを作るために狭い存在定理へ一般定理を要求しない。

**Stage14 closure:** 上記P1/P2・N1・V1/V2・E1/E2の再審査完了までは進めない。原稿改訂・証明修復は本監査PRと別PR。
