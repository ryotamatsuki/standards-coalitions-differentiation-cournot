# V2b — Stage 11 修正初稿 v0.5（研究用）

2026-10-22 JST。研究対象：*Endogenous Product Design and Participation in International Compatibility Agreements*、JPET想定。

## 状態
- PR #27の必須M1～M3を修正。mainとTheory Freezeは未変更。
- Figure 3は41×41格子の**数値的候補相図**。SW灰色は「探索で利益のある受諾可能提案が見つからなかった」意味で、全深度の数学的な否定証明ではない。
- 中心定理に関する1000区間の厳密な全深度認証は、Fig.3の広い二次元格子とは別の証拠。監査PR #27の immutable source/replayを参照。
- 論文本文＋証明補遺を2回pdflatexでビルドして20ページ。未解決参照／警告／Overfull box はゼロ。
- バージョン0.5。外部査読・投稿承認ではない。

## 修正の検証
1. v0.4の偽SW 11セルを修正（固定7／設計内生4）。正の投票差を確認。
2. 41×41上、固定SW765 / IS916、内生SW1047 / IS634、SU0（探索的分類）。
3. IS 1550セルについて、SU厚生の探索的最大値に対する厳しい比較を追加。差が負となる例0、最小正差約 0.0000396774。
4. SW候補1812セルについて、g=1e-7,1e-6,1e-5,1e-4,1e-3,.002,.004,.008の追加探索。新たな受諾可能IS検出0。これは全域証明ではない。
5. 基準点(.8505,.758)は固定IS／内生SWを再現。
6. 消費者凸性・設計Nash全戦略立方体・Krawczyk区間対象・政府の閉じた受諾集合での最適化を証明補遺に収録。
7. 1-x は費用のかかる残余製品差別化、x は残余類似性、g は政府の共通技術仕様深度として区別。
8. C2はρ=1の厳密領域とρ<1ごく近傍の限定的ストリップのみを主張。

## フォルダ
- `manuscript/stage25_jpet_v05.tex`, `.pdf` : 英文全稿
- `manuscript/stage11_proof_supplement.tex` : 追加の数学的証明・区間認証仕様
- `manuscript/figure3_v05_tikz.tex` : 編集可能な数値相図
- `figures/figure3_v05_corrected.png`, `.pdf`: 相図単体
- `verification/*` : 計算コード、元の相図分類との比較、セル別の数値、ストレステスト、QA JSON

## 再現

`python verification/stage11_fix_classifier.py` （zip展開配置によって元のスクリプトの相対パスを確認）。原始モデルの固有のg・xを保持してNashを計算。参考として独立監査PR #27の `verification/stage11` 配下の証明ログを併読。

## 未解決の範囲（投稿停止項目とは分ける）
- 相図の全セルを厳密区間演算で証明してはいない。したがってその主張を本文から撤回し、Figure 3を探索的図と明示。
- 一部関連研究の未取得補遺は新規性の断定材料にしない。
- 本稿の最終査読とStage 12投稿先確定、AI利用開示等は別工程。
