# Stage 13R：投稿用参考文献の再選定
日付：2026-10-23 JST
対象：Draft PR #32、選定時の原稿コミット `97a732ce74ddb865038518a793d6f0f2e2b1b0c4`
論文：Endogenous Product Design and Participation in International Compatibility Agreements

## 結論
現行11件を維持し、下記9件を追加する20件構成を推奨する。件数は選定の結果であり、目標数やJPETの必須件数ではない。現行稿は政府間標準政策を比較的よく押さえているが、企業主導の標準連合、費用を伴う水平差別化、政策後の私的投資と国家厚生という橋渡しが薄い。追加の目的はこの空白を埋め、既知の一般論と本稿の限定した貢献を読者が区別できるようにすることにある。

本ファイルは引用選定・配置案であり、原稿、証明、数値コード、Theory Freeze、PDFを変更しない。採用推奨は既存結果への非吸収や新規性の完全認証を意味しない。全文未取得の文献にも、公式抄録で確認できる内容に限定した引用は可能である。ただし、全文で確認していない定理の不存在・正確な命題番号・非吸収は主張しない。

## 1. 再確認したGitHub内の履歴
以下を相互照合した。現在の参考文献リストだけから新しい候補を思いついたものではない。
- `literature/PRIOR_ART_QUEUE.md`
- `literature/V2B_STAGE02_CLOSEST_PAPERS_2026-10-21.md`
- `literature/V2B_STAGE06_PARENT_THEOREM_ABSORPTION_2026-10-21.md`
- `literature/STAGE14_PRIOR_ART_ABSORPTION.md`
- `literature/STAGE15_CLOSE_PRIOR_ART_GATE.md`
- `literature/STAGE15_GROSSMAN_FULLTEXT_PROPOSITION_MAP.md`
- `literature/STAGE16_PRIOR_ART_KILL.md`
- `literature/STAGE17_PRIOR_THEOREM_ABSORPTION_GATE.md`
- `literature/STAGE19_CLOSE_PRIOR_ART_AND_NOVELTY.md`
- `literature/STAGE21_SW_REVERSAL_PRIOR_ART_AUDIT.md`
- `literature/STAGE23_EIGHT_LAYER_NOVELTY_AND_ABSORPTION.md`
- `literature/STAGE23_BFG_CH_THEOREM_LEVEL_ABSORPTION_20261022.md`
- `literature/STAGE24_EIGHT_LAYER_AND_ABSORPTION_MATRIX.md`
- `reviews/V2B_ANALYTIC_PROPOSITION_PRIOR_ART_MATRIX.md`
- `paper/sections/06_related_literature.tex`、`paper/references.bib`
- `manuscript/stage13r_jpet_revised.tex`

注意：これらは研究履歴であり、各ファイルの古いアクセス状態・判定を一括継承しない。例えばGrossman et al.について、2019著者版しか読めていないとする記録は、Stage15/16の刊行版読解記録と区別した。研究段階で列挙した全候補をそのまま投稿論文へ戻すことも推奨しない。

## 2. 追加採用する9件
| ID | 書誌情報・一次資料 | 必要な役割／配置 | 本稿との差と引用の限界 |
|---|---|---|---|
| A1 | Katz, M. L., & Shapiro, C. (1985). Network Externalities, Competition, and Compatibility. American Economic Review, 75(3), 424–440. https://www.jstor.org/stable/1814809 | Modelのネットワーク期待の段落。fulfilled expectationsと互換性競争の基礎を明示する。旧PRIOR_ART_QUEUEにも登場。 | 本稿の三国間政府ゲームや厳密な二次効用・設計費用をこの論文から導いたとは書かない。今回の再確認は刊行記録と索引本文の範囲。 |
| A2 | Economides, N., & Flyer, F. (1998). Equilibrium Coalition Structures in Markets for Network Goods. Annales d’Économie et de Statistique, 49/50, 361–380. 刊行PDF https://neconomides.com/uploads/Economides_Flyer_Equilibrium_Coalition_Structures.pdf ; stable URL https://www.jstor.org/stable/20076121 | Related Literatureの企業主導標準連合。ネットワーク便益と競争、連合への加入・同意は既知であると認める。 | 主体は企業。本稿は国家厚生を最大化する政府と独立した事後設計を分ける。今回、刊行PDFの冒頭・導入・ゲーム定義を再確認した。旧bibのWPタイトル「Compatibility and Market Structure for Network Goods」と刊行タイトルを混ぜない。 |
| A3 | Brander, J. A., & Spencer, B. J. (2015). Intra-industry trade with Bertrand and Cournot oligopoly: The role of endogenous horizontal product differentiation. Research in Economics, 69(2), 157–165. https://doi.org/10.1016/j.rie.2015.02.007 ; 著者/NBER記録 https://www.nber.org/papers/w21008 | Modelのcostly differentiationの説明とRelated Literature。国際寡占で差別化投資が競争を緩和する基礎に最も直接的。 | 協定加盟の主結果の出典ではない。今回NBER公開抄録と刊行版情報を再確認。2022年論文の順位逆転命題を2015年論文へ移植しない。 |
| A4 | Zhou, D., Spencer, B. J., & Vertinsky, I. (2002). Strategic trade policy with endogenous choice of quality and asymmetric costs. Journal of International Economics, 56(1), 205–232. https://doi.org/10.1016/S0022-1996(01)00118-0 | Related Literatureの政策→私的属性→輸出利益という橋渡し。単に企業を政府に置き換えたとの疑念に応える比較対象。 | 垂直品質と第三国市場への輸出政策の研究。本稿の水平残余設計、国内CS、三政府加盟投票とは異なる。今回、出版社公開抄録・導入を確認。 |
| A5 | Baake, P., & Boom, A. (2001). Vertical product differentiation, network externalities, and compatibility decisions. International Journal of Industrial Organization, 19(1–2), 267–284. https://doi.org/10.1016/S0167-7187(99)00029-6 | Modelのgとxの区別、Related Literatureの属性と互換性の二つの選択。両者を分けたこと自体を新規性にしない。 | 企業が先に固有品質、次にアダプタ互換性を選び、価格競争する。本稿とは主体と順序が異なる。今回、出版社抄録・導入を確認。完全命題比較は未完。 |
| A6 | Barrett, C. B., & Yang, Y.-N. (2001). Rational incompatibility with international product standards. Journal of International Economics, 54(1), 171–191. https://doi.org/10.1016/S0022-1996(00)00082-9 | IntroductionまたはRelated Literature。ネットワーク便益があっても企業・国が国際標準に従わないことは既知と説明する。 | 既存設備・変換/設計変更費用と外生的国際標準。本稿の非標準化残余属性のNashと同一agendaでの固定/内生比較とは異なる。今回、出版社公開部分と原WPの大学公開記録を確認。刊行命題番号をWPから転記しない。 |
| A7 | Cabral, L., & Salant, D. (2014). Evolving technologies and standards regulation. International Journal of Industrial Organization, 36, 48–56. https://doi.org/10.1016/j.ijindorg.2013.07.006 ; March 2009著者版 https://pages.stern.nyu.edu/~lcabral/workingpapers/CabralSalantMar09.pdf | Introduction/Related Literature。私的投資の反応を入れると静学的な標準化評価が変わる、という一般論を先行研究へ帰属させる。 | 動学的R&D・ただ乗りのメカニズム。本稿の国別消費者/輸出利益の配分と加盟制約とは区別する。今回、刊行抄録・導入と2009著者版導入を再確認。2009の命題番号を2014へ付け替えない。 |
| A8 | Lambertini, L., & Rossini, G. (1998). Vertical Differentiation, Trade and Endogenous Common Standards. University of Bologna, Department of Economics, Working Paper 263. https://doi.org/10.6092/unibo/amsacta/774 ; https://amsacta.unibo.it/id/eprint/774/ | Related Literatureで短く引用。政府の共通標準と企業の内生的属性を同じ枠組みに入れること自体は既知、と位置づける。 | 作業論文と明記し、技術・垂直品質と本稿の残余水平設計を混同しない。公開リポジトリの登録日は2004だが原稿年は1998。今回は大学書誌/抄録を再確認、過去監査にはWP命題7–9の読解記録あり。 |
| A9 | Takarada, Y., & Kawabata, Y. (2025). Multilateral Versus Regional Mutual Recognition. Nagoya City University Discussion Paper 701. https://oikono.econ.nagoya-cu.ac.jp/wp-content/uploads/sites/2/2025/02/DP701_Kawabata_February2025.pdf | Related Literatureの政府間協定群。地域的相互承認の外部国が多国間化を拒む近接研究を落とさない。 | 規制上の相互承認と負の消費外部性であり、物理的互換性と同一視しない。今回、原DP抄録とKAKEN書誌を確認。KAKENの見出し「Journal Article」だけで査読誌掲載と判断しない。実際の媒体欄はDiscussion Paper。 |

採用順位：A3・A6・A7・A2は現行稿の機構説明を直接補強する。A4・A5・A8は既存モデルとの境界を明示する。A1はモデルの基礎を、A9は近接する政府間協定研究の更新を補う。いずれも本文に一つの明確な役割を持たせる。

## 3. 現行11件は維持
| 文献 | 引用の役割／注意 |
|---|---|
| Gandal & Shy (2001), Standardization policy and international trade. JIE 53, 363–383. DOI 10.1016/S0022-1996(00)00067-2 | 三国政府・標準連合・国内CSと自国企業世界利益という直接の出発点。formal unionなし＝本稿のSWとは書かない。 |
| Takarada et al. (2020), Standards policy and international trade: Multilateralism versus regionalism. JPET 22, 1420–1441. DOI 10.1111/jpet.12425 | 最も近いJPETの地域/多国間協定比較。制度と私的設計の差を本文で説明する。 |
| Kawabata & Takarada (2021), Deep trade agreements and harmonization of standards. Southern Economic Journal 88, 118–143. DOI 10.1002/soej.12500 | 地域協定が多国間調和を妨げ得ることの既知性。 |
| Grossman, McCalman & Staiger (2021), The “New” Economics of Trade Agreements: From Trade Liberalization to Regulatory Convergence? Econometrica 89, 215–249. DOI 10.3982/ECTA17536 | 企業属性・調整費用・規制協定の主要比較対象。企業設計の内生化自体を新規性にしない。 |
| Klimenko (2009), Policies and international trade agreements on technical compatibility for industries with network externalities. JIE 77, 151–166. DOI 10.1016/j.jinteco.2008.08.005 | 政府互換性政策とネットワークの直接先行研究。完全命題照合の未確認を維持。 |
| Costinot (2008), A comparative institutional analysis of agreements on product standards. JIE 75, 197–213. DOI 10.1016/j.jinteco.2007.11.004 | 国際規制制度と厚生帰属。 |
| Buccella, Fanti & Gori (2023), Strategic product compatibility in network industries. Journal of Economics 140, 141–168. DOI 10.1007/s00712-023-00834-x | 企業の互換性・程度選択とCournot。別の2024品質差論文と混ぜない。 |
| Cheng & Huang (2025), Quality competition and product compatibility in network industries. Journal of Economics 145, 31–57. DOI 10.1007/s00712-024-00896-5 | 内生品質と企業拒否権。公開Appendixを読めても本体全命題確認済とはしない。 |
| Simcoe (2012), Standard setting committees: Consensus governance for shared technology platforms. AER 102, 305–336. DOI 10.1257/aer.102.1.305 | 現実の委員会手続の動機づけ。本稿の政府投票順序の実証的検証ではない。 |
| Rosen (1965), Existence and uniqueness of equilibrium points for concave N-person games. Econometrica 33, 520–534. DOI 10.2307/1911749 | 実際に利用するNash一意性の方法。 |
| Rump (2010), Verification methods: Rigorous results using floating-point arithmetic. Acta Numerica 19, 287–449. DOI 10.1017/S096249291000005X | 実際に利用する厳密数値認証の方法。 |

## 4. 今回は自動追加しない候補
| 候補 | 決定と理由 |
|---|---|
| Brander & Spencer (2022), Differentiated Entry or “Me-Too” Entry in Bertrand and Cournot Oligopoly. RIO 60, 1–27. DOI 10.1007/s11151-021-09822-1 | 有力な代替/追加候補。固定設計と内生設計で競争形態の価格・利潤順位が変わるという文章を入れる場合は採用する。現行の国際貿易とcostly designの説明には2015がより直結するため、両方を機械的に追加しない。今回、公開刊行本文の導入を確認。 |
| Maggi & Mrázová, Harmonization...What Else? The Role for International Regulatory Agreements. NBER WP33318 / CEPR DP19840 | 最新比較の最優先保留。今回、著者のYaleページのリンク先は2024-12-18版50頁。一方SSRNの記録は2026-07-16改訂を示す。2024版の導入・モデルで規制多様性の固定費、自然発生的調和と非効率、協定が多様性を促す点を確認したが、2026版全文の確認済み扱いはしない。引用するなら実際に読んだ版を固定し、一般的な協定の役割との比較に限定する。2026版に対する非吸収判定は保留。 |
| Cellini & Lambertini (2004), Private and Social Incentives Towards Investment in Product Differentiation. IGTR 6, 493–508. DOI 10.1142/S0219198904000320 | 私的/社会的差別化投資を詳しく論じる場合の補足。今回の主眼は国家間の厚生帰属と政府加盟であり、Brander–SpencerとZhouで橋を作れるため必須追加にしない。 |
| Petropoulou (2013); Jeanneret & Verdier (1996) | 垂直品質基準・貿易政策の追加例。重要性を否定しないが、選定したZhou/Grossman/Lambertini等との役割の重複を避ける。最低品質基準や政策コミットメントの比較を拡張する場合に再採用する。最終本文未取得を「結果がない」根拠にしない。 |
| Economides & Skrzypacz (2003); Bloch (1996); Ray & Vohra (1999) | 一般的・企業主導の連合交渉研究。本稿はその連合形成解概念を採用していないため、後ろ向き帰納法を使うだけでは引用理由にならない。企業の合意形成を詳述する場合はEconomides–Skrzypaczを追加。 |
| Casella (2001) | 標準というクラブ財・国際的な分割の研究。旧WPの中央計画者による分割を政府Nash連合ゲームと呼ばない。今回は関連が一段遠いため保留。 |
| Farrell & Saloner (1985); Farrell & Simcoe (2012); Aghion, Antràs & Helpman (2007) | 情報による慣性や手続・交渉そのものを比較するなら有用。現行の完全情報・固定手順のモデルで一般的な背景引用を重ねない。 |
| Chen & Chen (2011); Toshimitsu (2018); Wang & Lyu (2020); Geng (2019) | 互換性・代替性・制度の関連研究だが、現行採用群との重複が大きい。固有の比較命題を説明する場合に採用する。 |
| Buchholz & Hattori (2024) | 公共財と技術・連合形成の類推。企業による残余設計と国際標準が主題の現行稿では優先度が低い。 |
| Buccella–Fanti–Gori (2024)および2026訂正、同著者らの別の2026互換性費用論文 | 2023年論文と別物。訂正内容・刊行版に依存する主張を新たに利用する前に原文を確認する。今回、引用数を増やす目的で追加しない。 |
| Hashimzade & Sun (2026); Rodrigues (2026); Green R&D cooperation... (2026) | 現代的な周辺研究。政策/R&Dや一般的属性需要というだけで本稿の直接比較対象にはしない。今後のモデル一般化段階のキューに残す。 |
| Hotelling; Salop; d’Aspremont et al.; Singh & Vives (1984) | 却下した空間モデルの歴史、または価格対数量の比較のためだけに追加しない。とくに本稿の多国間ネットワーク需要の厳密な出所を、異なるモデルの古典に仮託しない。 |

保留は価値がないとの判断ではない。また、引用候補を採用しなかったことと、その文献による新規性脅威が消えたことは別である。

## 5. そのまま使用できる英文と配置
以下は推奨する一組であり、相互に競合する複数案ではない。BibTeXキーは次節の案と対応。Introductionで全20件を一度に列挙しない。既存の主要比較を残し、下の専門的比較はRelated Literatureへ配置する。

### Model：ネットワーク期待を導入する段落へ1文
> We use fulfilled expectations in the sense of Katz and Shapiro (1985): expected network consumption is held fixed in each firm's quantity decision and is required to equal realized consumption in equilibrium.

TeX：Katz and Shapiro (1985)を `\citet{KatzShapiro1985}` とする。現行のCournotの期待固定の説明に統合し、同じ説明を二度書かない。式の微分方法は変更しない。

### Model：costly differentiationの段落へ1文
> Costly horizontal differentiation allows firms to soften product-market competition, as in Brander and Spencer (2015); here firms choose a residual design dimension after governments have selected interface compatibility.

TeX：`\citet{BranderSpencer2015}`。本稿と同一の費用関数を採用したとの主張にはしない。

### Related Literature：政府間協定群の既存段落へ追加する2文
> Takarada and Kawabata (2025) likewise show that regional mutual recognition can obstruct multilateral recognition by changing nonmembers' welfare. Our additional comparison holds the government proposal and voting procedure fixed and asks how subsequent private redesign changes the national participation constraints.

既存Takarada2020/Kawabata2021との共通点を繰り返しすぎないよう、3文献を同じ政府間協定段落へ統合する。

### Related Literature：企業連合・属性と互換性
> At the firm level, Economides and Flyer (1998) study standards coalitions shaped by network benefits and product-market competition. Baake and Boom (2001) distinguish intrinsic product quality from compatibility through adapters, with quality chosen before compatibility. We instead separate a government-selected interface from a residual product attribute that firms choose after the policy decision. The contribution is therefore not the distinction between compatibility and product characteristics itself, but its consequences for national consent under the specified accession procedure.

この後に既存Buccella2023/Cheng2025の短い比較を置く。経済主体を変えただけで新規性が確定するとの表現を避ける。

### Related Literature：標準化失敗と内生的投資
> Rational nonconformity with international standards is already studied by Barrett and Yang (2001), while Cabral and Salant (2014) show how standardization can weaken private R&D incentives. Lambertini and Rossini (1998) also examine endogenous common standards alongside firms' technology and quality choices. Together with Grossman, McCalman and Staiger (2021), these studies establish that private product and investment choices matter for standards policy. Our result isolates a narrower comparison: allowing residual redesign can eliminate agreements that would be accepted with the same designs frozen at their no-agreement equilibrium, even though a direct three-country agreement would still raise every country's welfare.

「same designs」は同一のno-agreement設計を固定する反実仮想を指す。すべての深度/パラメータで成立する一般論として読ませないため、この段落の直前/直後に本稿の認証領域と制度限定の記述を維持する。Cabralの2009WPの番号・特定命題をここには入れない。

### Related Literature：差別化と国家利益の接続
> Brander and Spencer (2015) analyze costly horizontal differentiation in international oligopoly, and Zhou, Spencer and Vertinsky (2002) study how policy-induced quality choices affect export rents. These studies provide the strategic-trade background for our distinction between a firm's design incentives and national welfare. We trace the redesign response through domestic consumer surplus and the resident firm's worldwide profits to the member and outsider participation constraints.

既存のD−Lの直観は本文に残す。この引用段落で証明を代替しない。Brander2022の価格/利潤順位を説明しないので2015と2022の二重引用は不要。

## 6. 追加用の書誌キー
既存の `paper/references.bib` にあるキーは可能な限り再利用する。ただし現行稿はthebibliographyを使うため、そのまま.bibだけに追加してもPDFに反映されない。実装時には本文のciteキーとbibitemを揃える。

- KatzShapiro1985 — 上表A1
- EconomidesFlyer1998 — 上表A2。旧WP書誌を刊行書誌に更新する場合は別文献と取り違えない。
- BranderSpencer2015 — 上表A3
- ZhouSpencerVertinsky2002 — 上表A4
- BaakeBoom2001 — 上表A5
- BarrettYang2001 — 上表A6
- CabralSalant2014 — 上表A7
- LambertiniRossini1998 — 上表A8
- TakaradaKawabata2025 — 上表A9

## 7. 実装時の最小QAと終了条件
1. 上記9件を各々の役割が分かる本文の文とともに追加し、本文引用のない参考文献を残さない。
2. 段落を文献名の羅列にしない。政府間制度、企業の互換性/設計、国家厚生という流れを維持し、Introductionの早い主結果提示を妨げない。
3. 2025DPを刊行済み査読論文としない。WPの命題番号を別の刊行版に付け替えない。2024/2026版を混ぜない。
4. 書誌を著者姓順に整え、全citeキー・DOI・ページ・重複を照合する。Economides–Flyerは上記刊行PDFに印刷されたstable ID 20076121を用いる。
5. 再ビルドして未定義引用・重複・行あふれと、文献増加による改ページ・図表位置を確認する。ページ数が変われば旧21ページとの同一性は再主張しない。
6. PDFが更新されるため、最終QAのサイズ・Git Blob SHAと配布ZIPも更新する。文献だけの変更でもPDFのハッシュは変わる。
7. 数学モデル・数値コードの変更は不要。文献追加そのものを理由に科学計算全体の再実行は要求しない。
8. Maggi–Mrázováの最新版やCheng–Huang本体の未完比較は、引用追加によって解決済みにならない。強い新規性/不在主張を追加しない限り、今回の選定作業と独立したアクセス・研究課題として記録する。

## 8. 今回再確認した公開一次資料（研究履歴とは別）
- Katz–Shapiro刊行記録/本文索引：https://www.jstor.org/stable/1814809
- Economides–Flyer刊行PDF：https://neconomides.com/uploads/Economides_Flyer_Equilibrium_Coalition_Structures.pdf
- Brander–Spencer2015著者/NBER抄録・刊行情報：https://www.nber.org/papers/w21008
- Brander–Spencer2022公開刊行本文：https://link.springer.com/article/10.1007/s11151-021-09822-1
- Zhou et al.出版社抄録/導入：https://www.sciencedirect.com/science/article/pii/S0022199601001180
- Baake–Boom出版社抄録/導入：https://www.sciencedirect.com/science/article/pii/S0167718799000296
- Barrett–Yang出版社公開部分：https://www.sciencedirect.com/science/article/abs/pii/S0022199600000829
- Barrett–Yang原WPの大学記録：https://digitalcommons.usu.edu/eri/104/
- Cabral–Salant出版社抄録/導入：https://www.sciencedirect.com/science/article/pii/S0167718713000805
- Cabral–Salant2009著者版：https://pages.stern.nyu.edu/~lcabral/workingpapers/CabralSalantMar09.pdf
- Lambertini–Rossini大学書誌/抄録：https://amsacta.unibo.it/id/eprint/774/
- Takarada–Kawabata原DP：https://oikono.econ.nagoya-cu.ac.jp/wp-content/uploads/sites/2/2025/02/DP701_Kawabata_February2025.pdf
- Takarada–Kawabata媒体確認：https://kaken.nii.ac.jp/en/grant/KAKENHI-PROJECT-21K01444/
- Maggi著者ページ：https://economics.yale.edu/people/giovanni-maggi/papers
- そのリンク先の2024-12-18版：https://economics.yale.edu/sites/default/files/2024-12/20241218-RegCoop.pdf
- 2026改訂を示すSSRN書誌：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5076021

複数の出版社/NBERへの直接openは403等で失敗した。検索サービスが返した当該出版社の公開抄録・導入・書誌を読めた場合も「完全本文をダウンロードして全命題を確認」とは扱わない。今回の到達点は、研究履歴に根拠を持つ投稿用引用の選定と配置の完成である。
