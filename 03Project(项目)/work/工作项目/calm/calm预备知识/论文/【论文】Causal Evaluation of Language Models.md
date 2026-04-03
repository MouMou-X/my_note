---
tags: [数学/因果推理]
type: reference
status: 🌿
---

# Causal Evaluation of Language Models

Sirui Chen $^{2,§}$ , Bo Peng $^{3,1}$ , Meiqi Chen $^{4,§}$ , Ruiqi Wang $^{3,§}$ , Mengying Xu $^{5}$ , Xingyu Zeng $^{5}$ , Rui Zhao $^{5}$ , Shengjie Zhao $^{2}$ , Yu Qiao $^{1}$ , Chaochao Lu $^{\ddagger 1}$

$^{1}$ Shanghai AI Laboratory  $^{2}$ Tongji University  $^{3}$ Shanghai Jiao Tong University  $^{4}$ Peking University  $^{5}$ SenseTime Group

# Abstract

Causal reasoning, fundamental to human cognition and scientific understanding, is viewed as crucial for achieving human-level machine intelligence and fostering the development of an "artificial scientist" posited by Pearl. Recent advances in language models have expanded the horizons of artificial intelligence across various domains, sparking inquiries into their potential for causal reasoning. In this work, we introduce Causal evaluation of Language Models (CaLM), which, to the best of our knowledge, is the first comprehensive benchmark for evaluating the causal reasoning capabilities of language models. First, we propose the CaLM framework, which establishes a foundational taxonomy consisting of four modules: causal target (i.e., what to evaluate), adaptation (i.e., how to obtain the results), metric (i.e., how to measure the results), and error (i.e., how to analyze the bad results). This taxonomy defines a broad evaluation design space while systematically selecting criteria and priorities. Second, we compose the CaLM dataset, comprising 126,334 data samples, to provide curated sets of causal targets, adaptations, metrics, and errors, offering extensive coverage for diverse research pursuits. Third, we conduct an extensive evaluation of 28 leading language models on a core set of 92 causal targets, 9 adaptations, 7 metrics, and 12 error types. Note that, the selected 92 causal targets cover 46 causal tasks, span three text modes (i.e., Natural, Symbolic, and Mathematical), and involve two languages (i.e., English and Chinese). Before implementing CaLM, causal evaluations of language models were conducted, on average, in merely  $10\%$  of these causal tasks, typically using just a single adaptation (e.g., basic prompting) and a single metric (e.g., accuracy). Moreover, previous causal evaluations not only overlooked the Mathematical text mode but also excluded assessments in Chinese, and lacked a systematic categorization of error types for in-depth analysis. In contrast, our evaluation extends to a wide spectrum of causal tasks, metrics, and error analysis, significantly enriching the depth and breadth of causal evaluations. Fourth, we deeply analyze the causal evaluation results on two levels. At a broad level, we assess the influence of diverse dimensions (e.g., adaptation) and critical factors (e.g., scale) on overall model performance, and investigate the intra- and inter-dimensional relationships that shape causal reasoning efficacy. At a granular level, we provide an in-depth analysis of each specific adaptation, model, and causal scenario. Fifth, we present 50 high-level empirical findings across 9 dimensions (e.g., model, adaptation, error), providing valuable guidance for future language model development and analysis. Finally, we develop a multifaceted platform and codebase, including a website, leaderboards, datasets, and toolkits, to support scalable and adaptable assessments. We envision CaLM as an ever-evolving benchmark for the community, systematically updated with new causal targets, adaptations, models, metrics, and error types to reflect ongoing research advancements. Project website is at https://opencausalab.github.io/CaLM.

# Contents

# List of Figures VI

# List of Tables XII

# 1 Introduction 1

1.1 The CaLM Framework 3

1.1.1 Causal Target 3

1.1.2 Adaptation 5

1.1.3 Metric 5

1.1.4 Error 5

1.1.5 Key Features of CaLM 6

1.1.6 Considerations at a Broader Level 8

1.2 Empirical Findings 9

1.2.1 Findings from the Model 9

1.2.2 Findings from the Adaptation 10

1.2.3 Findings from the Causal Ladder 11

1.2.4 Findings from the Domain 12

1.2.5 Findings from the Mode 12

1.2.6 Findings from the Language 12

1.2.7 Findings from the Metric 12

1.2.8 Findings from the Error 12

1.2.9 Findings from the Causal Scenario 13

1.3 Contributions 18

1.4 Organization 20

# 2 Preliminaries 24

2.1 The Ladder of Causation 24

2.2 Structural Causal Models 25

# 3 Causal Targets 26

3.1 Taxonomy 26

3.1.1 Causal Task 26

3.1.2 Mode 26

3.1.3 Language 27

3.2 Concrete Implementation 27

3.2.1 Causal Task 28

3.2.2 Mode 29

3.2.3 Language 30

3.3 Rung 0: Causal Discovery 30

3.3.1 Pairwise Causal Discovery (PCD) 30

3.3.2 Event Causality Identification (ECI) 31

3.3.3 Abstract Reasoning (AR) 32

3.3.4 Causal Attribution (CA) 32

3.4 Rung 1: Association 33

3.4.1 Correlation (CORR) 33

3.4.2 Explaining Away Effect (EAE) 34

3.5 Rung 2: Intervention 35

3.5.1 Average Treatment Effect (ATE) 35

3.5.2 Backdoor Adjustment Set (BAS) 36

3.5.3 Frontdoor Adjustment Set (FAS) 37

3.5.4 Instrumental Variable (IV) 38

3.5.5 Collider Bias (CB) 39

3.5.6 Causal Effect Identification (CEI) 40

3.5.7 Controlled Direct Effect (CDE) 41

3.6 Rung 3: Counterfactuals 42

3.6.1 Actual Causality (AC) 42

3.6.2 Causal Explanation Generation (CEG) 43

3.6.3 Effect of the Treatment on the Treated (ETT). 43

3.6.4 Natural Direct Effect (NDE) 45

3.6.5 Natural Indirect Effect (NIE) 45

3.6.6 Probability of Necessity (PN) 46

3.6.7 Probability of Sufficiency (PS) 47

3.6.8 Counterfactual Reasoning (CR) 48

4 Data Collection 50

4.1 Dataset Selection 50

4.1.1 Open-source Datasets 50

4.1.2 Self-constructed Datasets 52

4.2 Dataset Construction 55

4.2.1 Generating DAGs 56

4.2.2 Constructing Natural and Mathematical Mode Datasets 56

4.2.3 Constructing Symbolic Mode Datasets 58

4.2.4 Constructing Chinese Version for Open-source Datasets 59

4.3 Data Statistics 60

5 Adaptations 62

5.1 Taxonomy 62

5.2 Concrete Implementation 63

5.3 Basic Prompt 64

5.4 Adversarial Prompt 65

5.5 Chain-of-Thought 66

5.6 In-context Learning 67

5.7 Explicit Function 68

6 Metrics 69

6.1 Taxonomy 69

6.2 Implementation Principles 69

6.3 Metrics for Model 70

6.4 Metrics for Causal Scenario 71

6.5 Metrics for Prompt 72

# 7 Errors 73

7.1 Taxonomy 73

7.2 Quantitative 73

7.3 Qualitative 77

# 8 Models 82

8.1 Taxonomy 82

8.2 Concrete Implementation 82

# 9 Experiments and Results 84

9.1 Main Results 84

9.1.1 Comparative Analysis of Models 85

9.1.2 Impact of Other Factors on Accuracy 89

9.1.3 Predicting Causal Reasoning Ability 93

9.1.4 Intra-dimensional Relationships 96

9.1.5 Inter-dimensional Relationships 105

9.1.6 Analyzing Complexity 108

9.1.7 Analyzing Maturity 112

9.1.8 Analyzing Volatility 112

9.1.9 Analyzing Errors 115

9.2 Prompt Analysis 125

9.2.1 In-context Learning 125

9.2.2 Adversarial Prompt 129

9.2.3 Chain-of-Thought 133

9.2.4 Explicit Function 134

9.3 Model-specific Analysis 136

9.3.1 OpenAI 136

9.3.2 Anthropic 150

9.3.3 Shanghai AI Laboratory 151

9.3.4 Alibaba Cloud 153

9.3.5 Baichuan Inc. 155

9.3.6 Meta 159

9.3.7 Lmsys 164

9.3.8 UC Berkeley 165

9.3.9 Microsoft 166

9.4 Causal Scenario-specific Analysis 167

9.4.1 Causal Discovery 172

9.4.2 Association 185

9.4.3 Intervention 188

9.4.4 Counterfactuals 207

# 10 Related Work 233

10.1 Advancements in Language Models 233

10.2 Evaluations of Language Models' General Abilities 234

10.3 Evaluations of Language Models' Causal Reasoning Abilities 234

10.4 Causal Benchmark Datasets 235

# 11 Gaps in CaLM 237

11.1 Gaps in Causal Targets 237

11.2 Gaps in Adaptations 239

11.3 Gaps in Metrics 241

11.4 Gaps in Errors 243

11.5 Gaps in Models 243

# 12 Limitations and Future Work 244

12.1 Limitations of Concrete Implementation 244

12.2 Limitations of Evaluation Results 244

# 13 Conclusion 246

# References 247

# A Prompts for Dataset Construction 268

# B Additional Details for Main Results 269

B.1 Examples for Analyzing Complexity 269

B.2 Supplementary Details for Prompt Analysis 269

# C Additional Details for Scenario-specific Analysis 273

C.1 Causal Discovery 273

C.1.1 PCD 273

C.1.2 ECI 276

C.1.3 CA 276

C.2 Intervention 276

C.2.1 ATE 276

C.2.2 CDE 276

C.2.3 CEI 281

C.2.4 BAS 281

C.3 Counterfactuals 281

C.3.1 CR 281

C.3.2 ETT 282

C.3.3 NDE 282

C.3.4 NIE 282

C.3.5 PN 282

C.3.6 PS 291

# D Models 303

# D.1 Limited-access Models 303

# List of Figures

1.1 The CaLM framework 2

1.2 Causal tasks 4

1.3 Thorough and standardized evaluation (causal scenario-based) 7

1.4 Thorough and standardized evaluation (causal task-based) 22

1.5 Extensive adaptation strategies (causal scenario-based) 23

1.6 Extensive adaptation strategies (causal task-based) 23

3.1 Example of pairwise causal discovery 31

3.2 Example of event causality identification 32

3.3 Example of event abstract reasoning 33

3.4 Example of causal attribution 33

3.5 Example of correlation 34

3.6 Example of explaining away effect 35

3.7 Example of average treatment effect 36

3.8 Real-world examples of BAS, FAS and IV 37

3.9 Example of backdoor adjustment set 38

3.10 Example of frontdoor adjustment set 38

3.11 Example of instrumental variable 39

3.12 Real-world examples of CB, CEI and CDE 40

3.13 Example of collider bias 40

3.14 Example of causal effect identification 41

3.15 Example of controlled direct effect 42

3.16 Example of actual causality 43

3.17 Example of causal explanation generation 44

3.18 Real-world examples of ETT, NDE and NIE 44

3.19 Example of effect of the treatment on the treated 45

3.20 Example of natural direct effect 46

3.21 Example of natural indirect effect 47

3.22 Example of probability of necessity. 48

3.23 Example of probability of sufficiency. 48

3.24 Example of counterfactual reasoning 49

4.1 An example of CaLM-CA dataset 53

4.2 An example of CaLM-CEI dataset 53

4.3 An example of CaLM-IV dataset 54

4.4 An example of CaLM-AS dataset 54

4.5 An example of CaLM-ATE dataset 55

5.1 Adaptation strategy 64

5.2 Adversarial prompt formatting 65

5.3 Chain-of-Thought formatting 66

5.4 In-context Learning prompt formatting 67

5.5 Explicit function formatting 68

6.1 Example of Robustness 70

7.1 Errors taxonomy 74

7.2 Empty response 74

7.3 Limitation of instruction-following 75

7.4 Repetition 75

7.5 Language inconsistency 76

7.6 Causal hallucination 77

7.7 Inferential ambiguity 77

7.8 Calculation error 78

7.9 Incorrect reasoning 79

7.10 Misunderstanding 80

7.11 Contradiction 80

7.12 Outlier 81

8.1 Diversity of model implementation 83

9.1 Comparative analysis under different modes 85

9.2 Comparative analysis under multilingual 86

9.3 Comparative analysis of models under different rungs of causal ladder 87

9.4 Comparative analysis under different prompts 88

9.5 Impact of model access on accuracy 89

9.6 Impact of time on accuracy 90

9.7 Impact of multilingual on accuracy 92

9.8 Impact of domain on accuracy 92

9.9 Causal reasoning ability vs. scale 94

9.10 Causal reasoning ability vs. training strategy 95

9.11 Basic prompt vs. X 96

9.12 Pearson correlation between prompts 98

9.13 Correlation between accuracy and robustness 99

9.14 Correlation between modes 101

9.15 Overall correlation between modes 102

9.16 Correlation between various rungs of causal ladder 103

9.17 Inter-causal scenario performance correlation 105

9.18 Relationship between causal scenario and model 106

9.19 Relationship between scenario and prompt 107

9.20 Illustration of causal reasoning levels 108

9.21 Complexity analysis of Mathematical mode questions 111

9.22 Maturity of causal scenarios 112

9.23 Volatility of prompts 113

9.24 Volatility of models 114

9.25 Relationship between error and prompt 117

9.26 0-shot CoT's impact on language inconsistency 118

9.27 Same response to all questions error 119

9.28 Case of causal hallucination 120

9.29 Case of inferential ambiguity 120

9.30 Case of calculation error 121

9.31 Case of incorrect reasoning 122

9.32 Case of misunderstanding 122

9.33 Case of contradiction 123

9.34 Case of outlier 124

9.35 Case of hybrid errors 125

9.36 Relationship between accuracy and the number of IcL examples 126

9.37 Impact of IcL example numbers on accuracy 126

9.38 Accuracy trends across various factors 127

9.39 Accuracy trends of mode and question type combinations 128

9.40 Wrong direction vs. right direction 130

9.41 Direct model comparison between right and wrong change directions 131

9.42 Training strategy's influence on wrong and right change directions 132

9.43 Influence of manual CoT format 133

9.44 Basic vs. CoT 134

9.45 Basic vs. EF across all the scenarios 135

9.46 Basic vs. EF across all the models 135

9.47 Prompt-average rank of models 138

9.48 Heatmap of ada (0.35B) 139

9.49 Heatmap of text-ada-001 139

9.50 Heatmap of babbage (1.3B) 140

9.51 Heatmap of text-babbage-001 141

9.52 Heatmap of curie (6.7B) 142

9.53 Heatmap of text-curie-001 143

9.54 Heatmap of davinci (175B) 144

9.55 Heatmap of text-davinci-001 145

9.56 Heatmap of text-davinci-002 146

9.57 Heatmap of text-davinci-003 147

9.58 Heatmap of GPT-3.5-Turbo 148

9.59 Heatmap of GPT-4 149

9.60 Heatmap of Claude2 150

9.61 Heatmap of InternLM-chat (7B) 151

9.62 Heatmap of InternLM-chat (20B) 152

9.63 Heatmap of Qwen (7B) 153

9.64 Heatmap of Qwen (14B) 154

9.65 Heatmap of Baichuan1 (7B) 156

9.66 Heatmap of Baichuan1-chat (13B) 157

9.67 Heatmap of Baichuan2-chat (7B) 158

9.68 Heatmap of Baichuan2-chat (13B) 159

9.69 Heatmap of Llama2 (7B) 160

9.70 Heatmap of Llama2 (13B) 161

9.71 Heatmap of Llama2 (70B) 162

9.72 Heatmap of Llama2-chat (70B) 163

9.73 Heatmap of Vicuna-v1.3 (33B) 164

9.74 Heatmap of Koala (13B) 165

9.75 Heatmap of Wizardcoder (15B) 166

9.76 Distribution of causal discovery 172

9.77 Heatmap of PCD 173

9.78 Language comparison of PCD 174

9.79 Heatmap of ECI 177

9.80 Language comparison of ECI 178

9.81 Heatmap of AR 180

9.82 Language comparison of AR 181

9.83 Heatmap of CA 182

9.84 Language comparison of CA 183

9.85 Distribution of association 185

9.86 Heatmap of EAE 185

9.87 Language comparison of EAE 186

9.88 Heatmap of CORR 187

9.89 Language comparison of CORR 188

9.90 Distribution of intervention 189

9.91 Heatmap of ATE 190

9.92 Language comparison of ATE 191

9.93 Heatmap of CDE 193

9.94 Language comparison of CDE 194

9.95 Heatmap of CEI 196

9.96 Language comparison of CEI 197

9.97 Heatmap of BAS 200

9.98 Language comparison of BAS 201

9.99 Heatmap of FAS 204

9.100 Language comparison of FAS 205

9.101 Heatmap of IV 206

9.102 Language comparison of IV 207

9.103 Heatmap of CB 208

9.104 Language comparison of CB 209

9.105 Distribution of counterfactuals 209

9.106 Heatmap of CR 210

9.107 Language comparison of CR 211

9.108 Heatmap of AC 212

9.109 Language comparison of AC 213

9.110 Heatmap of ETT 214

9.111 Language comparison of ETT 215

9.112 Heatmap of NDE 217

9.113 Language comparison of NDE 218

9.114 Heatmap of NIE 221

9.115 Language comparison of NIE 222

9.116 Heatmap of PN 225

9.117 Language comparison of PN 226

9.118 Heatmap of PS 228

9.119 Language comparison of PS 229

9.120 Heatmap of CEG 231

9.121 Language comparison of CEG 231

11.1 Example of generation (code causality) 238

11.2 Example of causal discovery (image causality) 239

11.3 Example of counterfactual reasoning (video causality) 240

11.4 Example of replication output 241

11.5 Example of counterfactual fairness 242

11.6 Example of causal hallucination 242

B.1 Analyzing complexity: example 1 269

B.2 Analyzing complexity: example 2 270

B.3 Analyzing complexity: example 3 270

B.4 Analyzing complexity: example 4 270

B.5 Analyzing complexity: example 5 271

B.6 Analyzing complexity: example 6 271

B.7 Analyzing complexity: example 7 271

B.8 Analyzing complexity: example 8 272

B.9 Analyzing complexity: example 9 272

B.10 Relationship between accuracy and the number of IcL examples on English datasets 272

C.1 Distribution of causal tasks in PCD 273

C.2 Distribution of causal tasks in ECI 273

C.3 Distribution of causal tasks in CA 273

C.4 Distribution of causal tasks in ATE 274

C.5 Distribution of causal tasks in CDE 274

C.6 Distribution of causal tasks in CEI 274

C.7 Distribution of causal tasks in BAS 274

C.8 Distribution of causal tasks in CR 275

C.9 Distribution of causal tasks in ETT 275

C.10 Distribution of causal tasks in NDE 275

C.11 Distribution of causal tasks in NIE 275

C.12 Distribution of causal tasks in PN 276

C.13 Distribution of causal tasks in PS 276

C.14 Heatmaps of model performance of causal tasks in PCD 277

C.15 Heatmaps of prompt gain of causal tasks in PCD 278

C.16 Heatmaps of model performance of causal tasks in ECI 279

C.17 Heatmaps of prompt gain of causal tasks in ECI 280

C.18 Heatmaps of model performance of causal tasks in CA 281

C.19 Heatmaps of prompt gain of causal tasks in CA 282

C.20 Heatmaps of model performance of causal tasks in ATE 283

C.21 Heatmaps of prompt gain of causal tasks in ATE 284

C.22 Heatmaps of model performance of causal tasks in CDE 285

C.23 Heatmaps of prompt gain of causal tasks in CDE 286

C.24 Heatmaps of model performance of causal tasks in CEI 287

C.25 Heatmaps of prompt gain of causal tasks in CEI 288

C.26 Heatmaps of model performance of causal tasks in BAS 289

C.27 Heatmaps of prompt gain of causal tasks in BAS 290

C.28 Heatmaps of model performance of causal tasks in CR 291

C.29 Heatmaps of prompt gain of causal tasks in CR 292

C.30 Heatmaps of model performance of causal tasks in ETT 293

C.31 Heatmaps of prompt gain of causal tasks in ETT 294

C.32 Heatmaps of model performance of causal tasks in NDE 295

C.33 Heatmaps of prompt gain of causal tasks in NDE 296

C.34 Heatmaps of model performance of causal tasks in NIE 297

C.35 Heatmaps of prompt gain of causal tasks in NIE 298

C.36 Heatmaps of model performance of causal tasks in PN 299

C.37 Heatmaps of prompt gain of causal tasks in PN 300

C.38 Heatmaps of model performance of causal tasks in PS 301

C.39 Heatmaps of prompt gain of causal tasks in PS 302

# List of Tables

4.1 Datasets selection of CaLM 51

4.2 Question templates 57

4.3 Concise statistics of CaLM datasets 60

4.4 Detailed statistics of CaLM datasets 61

6.1 Degree of understandability 71

6.2 Degree of open-limited gap 72

6.3 Degree of solvability 72

8.1 Taxonomy of model 83

9.1 Calculation for three causal reasoning levels 109

9.2 Samples with different complexity factors 109

9.3 Error stastics 115

9.4 Overview of same response to all questions 119

9.5 Explanations for model-specific terminologies 137

9.6 Explanations for scenario-specific terminologies 168

9.7 Explanations for scenario-specific terminologies (continued) 169

9.8 Degree of prompt dependence 170

9.9 Variance of distributions in the causal scenario 170

9.10 Variance of solvability of causal tasks in the causal scenario 171

9.11 Variance of model's top performance in the causal scenario 171

9.12 Variance of prompt dependence 172

D.1 API Version and evaluation date of limited-access model 303

# 1 Introduction

To know what you know and know what you do not know - this then is wisdom.1

Confucius, The Analects, 551-479 BCE

Causal reasoning is a vital element of human cognition (Waldmann, 2017), and is widely thought of as an indispensable step towards achieving machine intelligence at a human level (Pearl, 2019). In fact, causal reasoning is a cornerstone of scientific understanding. It enables scientists to explain, predict, and control natural phenomena, test hypotheses, build models, and make informed decisions. Without the ability to reason causally, scientific progress would be severely hindered, and our understanding of the world around us would remain limited. More importantly, upon comprehending the underlying principles governing causal reasoning, it becomes feasible to simulate this cognitive process within contemporary computer systems, thus enabling the development of an "artificial scientist" (Pearl & Mackenzie, 2018). This "Causal Revolution" (Pearl & Mackenzie, 2018) in artificial intelligence is expected to have a profound impact on a wide range of fields and industries.

Many believed that we were far from realizing this blueprint before the advent of large language models (LLMs). However, recent advancements in LLMs have significantly pushed the boundaries of AI on a wide range of domains and causal tasks, including natural language comprehension (Ouyang et al., 2022; OpenAI, 2022, 2023; Touvron et al., 2023), programming (Chen et al., 2021b; Li et al., 2022; Roziere et al., 2023; Tufano et al., 2024), and mathematical reasoning (Imani et al., 2023; Romera-Paredes et al., 2024; Ahn et al., 2024; Trinh et al., 2024). Bubeck et al. (2023) even believed that an early version of GPT-4 "could reasonably be viewed as an early (yet still incomplete) version of an artificial general intelligence (AGI) system". The various emergent abilities (Wei et al., 2022a) of LLMs lead us to wonder whether or not we are approaching such an artificial scientist capable of causal reasoning. This curiosity instinctively gives rise to several fundamental questions: a) How can we ascertain if LLMs possess the capacity for causal reasoning? b) How can we gauge the degree of causal reasoning proficiency in LLMs? c) How can we enhance the causal reasoning aptitude of LLMs? All three of the "How" inquiries necessitate a comprehensive benchmarking of LLMs concerning their causal reasoning capabilities.

Although a few efforts have been made in this direction (Hobbhahn et al., 2022; Willig et al., 2022; Long et al., 2022; Tu et al., 2023; Jin et al., 2023a,b; Kiciman et al., 2023; Zhang et al., 2023a,b; Zečević et al., 2023; Gao et al., 2023a; Lu et al., 2024), these endeavors assess only a limited selection of language models for a narrow range of causal tasks. Typically, these studies employ only a single adaptation (e.g., basic prompting) and rely solely on a single metric (e.g., accuracy) for assessment. This results in an incomplete grasp of the models' abilities in causal reasoning. Moreover, prior evaluations have not only neglected the exploration of causal assessments in Chinese, but also failed to implement a systematic categorization of error types for in-depth analysis. In addition, there is an absence of a publicly accessible platform to facilitate wider engagement with these findings in the community.

In this work, we introduce Causal evaluation of Language Models (CaLM), which, to the best of our knowledge, is the first comprehensive benchmark for evaluating the causal reasoning capabilities of language models. To be specific, (1) we propose the CaLM framework, establishing a foundational taxonomy consisting of four

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/84bdbbf9e3c6206e26a51cda2b6752ed42933893dd9fd0318c089cbb376c115d.jpg)



Figure 1.1 The CaLM framework. CaLM is composed of four modules: causal target (what to evaluate), adaptation (how to obtain the results), metric (how to measure the results), and error (how to analyze the bad results). Broadly speaking, it defines an expansive design space essential for assessing the causal reasoning capability of language models. In terms of concrete implementation, we assess 92 causal targets, employing 9 adaptations, 7 metrics, and cataloging 12 types of errors.


modules: causal target (what to evaluate), adaptation (how to obtain the results), metric (how to measure the results), and error (how to analyze the bad results), as shown in Figure 1.1. This taxonomy defines a broad, if not complete, design space for evaluation while systematically selecting criteria and outlining priorities and constraints. (2) We construct the CaLM dataset, featuring 126,334 data samples, to provide curated sets of causal targets, along with corresponding adaptations, metrics, and errors. It offers extensive coverage and practicality for diverse research endeavors. (3) We provide a comprehensive evaluation of 28 prominent language models on a core set of 92 causal targets, 9 adaptations, 7 metrics, and 12 types of errors. The selected 92 causal targets span 46 causal tasks across three text modes (i.e., Natural, Symbolic, and Mathematical) and two languages (i.e., English and Chinese). Our evaluation substantially broadens the scope beyond previous work, and greatly enhances our understanding of the causal reasoning capabilities of language models. (4) We conduct a deep analysis of the evaluation results on two levels. At a broad level, we assess the impact of diverse dimensions (e.g., adaptation) and critical factors (e.g., scale) on overall model performance, while examining the intra- and inter-dimensional relationships that influence causal reasoning efficacy. At a granular level, we offer a detailed analysis of each specific model, adaptation, and causal task. (5) Our extensive evaluation yields 50 empirical findings across 9 dimensions (e.g., model, scenario, metric), providing valuable guidance for future language model development and further analysis. (6) We develop a multifaceted platform and codebase, including a website, leaderboards, curated datasets, and toolkits, to facilitate consistent and scalable assessments that can adapt to evolving research needs.

The rest of this section is organized as follows. We begin in The CaLM Framework (Section 1.1) by formally introducing the CaLM framework and its constituent modules, namely causal target, adaptation, metric, and error, followed by highlighting its key features and broader considerations inherent within this framework. In Empirical Findings (Section 1.2), we outline 50 empirical findings derived from various aspects, including the model, adaptation, causal ladder, domain, mode, language, metric, error, and causal scenario. These findings are presented systematically, indicating the depth and breadth of analysis conducted within the study. Contributions (Section 1.3) summarizes the contributions made in this work, and Organization (Section 1.4) concludes by providing an outline of the rest of this paper for the reader's guidance.

# 1.1 The CaLM Framework

Figure 1.1 presents the CaLM framework, which consists of four core modules: causal target, adaptation, metric, and error. These modules collectively forge a comprehensive structure that facilitates the systematic evaluation of language models. The depicted arrows represent the model evaluation pipeline, indicating the sequential process each evaluation undergoes. This involves specifying a causal target for the language model, incorporating an adaptation process within the model, employing one or more metrics for evaluation, and identifying one or more errors. These modules serve to respectively answer four fundamental inquiries: (i) the specific causal reasoning capabilities sought, (ii) the methodology for adapting a model to achieve these capabilities, (iii) the effectiveness of the results obtained, and (iv) the nature and scope of the errors identified during the evaluation process.

Generally speaking, our CaLM framework is structured on two levels. (1) Broad vision: We formulate an abstract taxonomy consisting of four modules (i.e., causal target, adaptation, metric, and error) to define the extensive, if not entire, design space for assessing the causal reasoning abilities of language models. This taxonomy facilitates a systematic selection within this space, thereby making explicit our benchmark design priorities and the existing limitations thereof. (2) Concrete implementation: Based on the taxonomy, we select and implement a core set of 92 causal targets, 9 adaptations, 7 metrics, and 12 errors. This selection is with an emphasis on comprehensive coverage (e.g., diverse prompt types), significance (e.g., causal scenarios essential to essential decision-making processes), and practicality (e.g., limited computational resources).

# 1.1.1 Causal Target

A causal target specifies the objective that a model aims to achieve in assessing its causal reasoning capabilities, encapsulated by a defining triplet: (causal task, mode, language). In essence, it outlines the particular causal task a model is expected to undertake, the designated mode for performing this task, and the specific language to be used. This triad of elements constitutes a comprehensive testbed for evaluating language models, presenting unparalleled challenges. In our implementation, the core set of causal targets encompass 46 causal tasks, three text modes, and two languages, collectively yielding 92 distinct causal targets.

Causal task. A causal task defines the specific duty of causal reasoning that a language model needs to accomplish. It is also structured as a triplet: (causal ladder, causal scenario, domain), with the relationships among these three elements illustrated in Figure 1.2. Causal ladder, often referred to as the Ladder of Causation, is a conceptual framework developed by Pearl & Mackenzie (2018) to illustrate the hierarchy of causal reasoning tasks (Bareinboim et al., 2022). This ladder consists of three distinct levels: association (Rung 1), intervention (Rung 2), and counterfactuals (Rung 3), each representing a progressively deeper level of causal understanding. In addition, we incorporate causal discovery (Spirtes et al., 2000; Peters et al., 2017) into this ladder, recognizing them as a fundamental phase in causal reasoning (Glymour et al., 2019). For clarity and ease of reference in future discussions, we categorize (causal) discovery as Rung 0 of the causal ladder within our CaLM framework. Causal scenario depicts potential applications of causal concepts in practical or research contexts (e.g., average treatment effect (ATE), probability of sufficiency (PS)), each belonging to only one of the four rungs in the causal ladder. Domain specifies the exact context in which a causal scenario is implemented. It could include, for instance, the application of distinct datasets or the exploration of varied question types within a singular dataset (i.e., utilizing the same dataset for tasks such as multiple choice, binary classification, or content generation). This highlights the inherent versatility of domains, underscoring their ability to accommodate a wide array of analytical and procedural tasks. In our implementation, causal tasks span all

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3abf84bcc7c15e3365a10c922bfa9d2aa32934f7edbac63a2ab2f1da19bccef8.jpg)



Figure 1.2 Causal tasks. The diagram presents a hierarchical structure with three different layers. The innermost layer consists of four levels of the causal ladder (i.e., causal discovery, association, intervention, and counterfactuals). The second layer consists of 21 causal scenarios. And the outermost layer categorizes 46 tasks (where B represents binary classification, C represents choice selection, P represents probability calculation, and O represents open-ended generation). We take into account both English and Chinese versions of the 46 tasks, with the illustration displaying the English version.


4 rungs of the causal ladder (i.e., causal discovery, association, intervention, and counterfactuals), 21 causal scenarios (e.g., pairwise causal discovery, correlation, backdoor adjustment set, counterfactual reasoning), and 46 domains (i.e., different datasets and/or varied question types).

Mode. Mode signifies the different formats in which information can be stored and displayed. Evaluating a model's causal reasoning ability across multiple modes is crucial for confirming its adaptability. Each mode presents unique challenges to the model's ability to process information. For instance, in the text mode, the focus is on handling linguistic structures and meanings. In the image mode, the emphasis shifts to deciphering visual components and spatial relationships. The use of various modes aids in enhancing our understanding and improvement of the model's capability to handle complex situations. Moreover, it promotes model's application in more complex and realistic causal scenarios. The broad categories of modes include text, image, video, and code (Lu et al., 2024), each of which could be further divided into more specific subcategories. Remarkably, given this benchmark's focus on language models, we specifically identifies three unique subcategories within the text mode: Natural, Symbolic, Mathematical. Natural is the most prevalent approach for interacting with language models. It focuses on assessing their abilities in language understanding and causal reasoning. Symbolic conveys the information represented in Symbolic forms, closely aligning with traditional cognitive reasoning (Garcez et al., 2008) and minimizing the influence of training data. Mathematical presents problems in mathematical terms, examining the model's capacity for logical structure and conceptual comprehension (Cobbe et al., 2021). The three text modes emphasize different aspects, together thoroughly evaluating the model's ability in causal reasoning.

Language. Globally, billions of individuals utilize thousands of distinct languages for communication (Nordhoff & Hammarström, 2011). Therefore, evaluating the causal reasoning abilities of language models across diverse languages is vital for ensuring their global applicability and inclusivity. Such evaluations take into account the unique cultural contexts, linguistic diversities, and nuances embedded within different languages, providing a thorough assessment of a model's ability to generalize causal reasoning capabilities across the linguistic spectrum. Furthermore, it is instrumental in identifying and quantifying the influence of language-specific biases on the causal reasoning performance of these models. In our implementation, we concentrate on English and Chinese, reflecting the predominant focus within the realm of language models and natural language processing on these two languages exclusively (Liang et al., 2022).

# 1.1.2 Adaptation

Building on the work of Bommasani et al. (2021) and Liang et al. (2022), adaptation refers to the process by which a language model, supplemented with additional data, is transformed into an adapted model capable of making predictions on new instances. This process can be primarily categorized into three types: prompting, lightweight-finetuning, and finetuning. They are distinguished based on their method of adaptation: either by priming the model with new data incorporated as a prompt in its input or by utilizing new data to update some or all of the model's parameters. To assess the causal reasoning abilities of language models, it is essential to specify an adaptation method that enables to apply the general-purpose model to a given causal target. In this work, we focus on prompting, as it represents the most intuitive method for employing language models in causal reasoning tasks. Specifically, our implementation explores nine distinct prompting strategies (e.g., Chain-of-Thought (CoT) (Wei et al., 2022b), In-context Learning (IcL) (Brown et al., 2020), Explicit Function (EF)).

# 1.1.3 Metric

Metric provides a systematic way to quantify a model's performance across various dimensions of causal reasoning abilities. Typically, accuracy is the most universally recognized metric. Additionally, other metrics such as robustness, toxicity, and fairness are also widely used to cater to diverse evaluation needs. We implement a set of seven metrics, which are categorized by model, prompt, and causal scenario. Specifically, we measure model performance using three metrics: accuracy, robustness, and model volatility. Accuracy assesses the precision of responses, robustness examines the consistency of these responses under adversarial prompt disturbance, and model volatility explores sensitivity to different prompts. For causal scenarios, we apply three metrics: understandability, open-limited gap, and solvability. Understandability evaluates the ease with which a model interprets a scenario, open-limited gap measures performance differences between open-access and limited-access models within the top five of each scenario, and solvability examines the model's ability to identify solutions within a causal scenario. Lastly, for prompts, prompt volatility is used to gauge the variability in model performance when comparing a specific prompt to a basic prompt. This metric serves as an indicator of the prompt's effectiveness.

# 1.1.4 Error

Error indicates the discrepancies or shortcomings observed in a model's performance during its assessment in causal reasoning tasks. Uncovering and monitoring these errors is crucial, as it aids researchers and practitioners in pinpointing the model's deficiencies, thereby guiding directions for future improvement. In this study, we document errors both quantitatively and qualitatively, categorizing them into 12 distinct types.

The Quantitative errors are divided into five categories: same response to all questions, empty response, limitation of instruction-following, repetition and language inconsistency. For qualitative errors, we identify seven types: causal hallucination, inferential ambiguity, calculation error, incorrect direction, misunderstanding, contradiction and outlier. In terms of quantitative errors, same response to all questions refers to instances where the model produces identical replies across different questions within a task. Empty response denotes situations where the model provides no response to some questions. Limitation of instruction-following describes the model's inability to respond according to the prescribed format. Repetition indicates errors involving the model's repetitive generation of questions. Language inconsistency occurs when the model responds in a language different from the question's language. Turning to qualitative errors, causal hallucination involving the model confusing correlation for causation, leading to incorrect causal assertions. Inferential ambiguity is observed when the model's response is overly broad or vague, making it difficult to determine its intent. Calculation error describes incorrect results from proper mathematical procedures. Incorrect direction highlights flawed reasoning within the model' chain of thought, resulting in erroneous conclusions. Misunderstanding occurs when the model misinterprets the problem. Contradiction arises from the model providing conflicting responses, such as saying both "yes" and "no" to the same query. Outlier refers to responses that are completely unrelated to the posed question. This classification facilitates a thorough understanding of the model's limitations and informs targeted improvements.

# 1.1.5 Key Features of CaLM

Flexible and scalable framework. First, by establishing an abstract taxonomy comprising four modules (causal target, adaptation, metric, and error), CaLM defines a wide-reaching, if not entire, design space for evaluating the causal reasoning capabilities of language models. This taxonomy not only allows for a systematic approach to selecting evaluation criteria but also explicitly outlines the framework's priorities and limitations. This level of abstraction ensures that CaLM can adapt and expand as new challenges and requirements emerge in the field of causal reasoning, showcasing its inherent flexibility. Second, the practical application of this taxonomy, through the selection and implementation of a specific set of 92 causal targets, 9 adaptations, 7 metrics, and 12 errors, demonstrates CaLM's scalability. Together, these two levels enable CaLM to be both adaptable to new developments in the field (flexibility) and capable of being applied to a wide range of causal scenarios and scales (scalability).

Comprehensive evaluation. One of the major goals of CaLM is to establish a consensus on the causal reasoning capabilities of language models. We conduct evaluations on 28 prominent language models from nine organizations spanning both academic and industrial sectors: OpenAI (e.g., GPT-4, GPT-3.5-Turbo), Anthropic (i.e., Claude2), Shanghai AI Laboratory (i.e., InternLM-chat (7B), InternLM-chat (20B)), Alibaba Cloud (i.e., Qwen (7B), Qwen (14B)), Baichuan Inc. (e.g., Baichuan1-chat (13B), Baichuan2-chat (7B)), Meta (e.g., Llama2 (13B), Llama2-chat (70B)), Lmsys (i.e., Vicuna-v1.3 (33B)), UC Berkeley (i.e., Koala (13B)), and Microsoft (i.e., Wizardcoder (15B)). These models are categorized into two accessibility types: Open (e.g., Llama2 (7B), InternLM-chat (20B)) and Limited (e.g., GPT-4) (detailed in Models (Section 8)). Despite the significant societal impacts of some models (e.g., GPT-4, GPT-3.5-Turbo), a fair, open, and comprehensive benchmark for their causal reasoning abilities is lacking. We achieve the uniform evaluation from two aspects: (1) From the model perspective, we illustrate in Figure 1.3 and Figure 1.4 that, before CaLM, models were typically evaluated in only  $18\%$  of the 21 causal scenarios and  $10\%$  of the 46 causal tasks. We have increased these proportions both to  $100\%$ . (2) From the standpoint of prompts, Figure 1.5 and Figure 1.6 show that, prior to CaLM, the usage of prompts was limited and uneven, with an average of only 1.9 prompts per causal scenario and 1 prompt

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/72e87af06b273e11d303d6f8ac3e149971464ea3299195a77b14226ea4f6fcdf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b8b65c34b0edf6ae7ee007958251bd67c9cda29769d7100b68c2c9665ebd0a56.jpg)



Figure 1.3 Thorough and standardized evaluation (causal scenario-based). (a) Previous studies reveal the uneven and incomplete nature of evaluating the causal reasoning abilities of language models across various causal scenarios, underscoring existing gaps. (b) Through CaLM, we conduct comprehensive evaluations of 28 models across 21 causal scenarios. By leveraging CaLM, we can achieve a comprehensive and profound understanding of the causal reasoning abilities of language models.


per causal task. CaLM has elevated these figures to 9 and 8.8, respectively. By conducting evaluations under standardized causal scenarios and conditions (e.g., employing the same adaptation strategy across all models), we achieve a fair and uniform evaluation between models.

Navigating implementation. CaLM guides us in systematically selecting causal targets, adaptations, metrics, and identifying errors. It also plays a crucial role in clearly highlighting the existing gaps and outlining directions for further exploration. Given the complexity and breadth of the design space CaLM defines, it is unrealistic to fully explore it within a limited timeframe. Thus, alongside presenting a broad vision and

concrete implementation, we explicitly address the current gaps in Gaps in CaLM (Section 11), aiming to focus future research on these unexplored areas in the causal evaluation of language models. Importantly, we view CaLM as a sustainable benchmark, systematically updated with new implementations of causal targets, adaptations, models, metrics, and error types, to adapt and grow in response to ongoing research advancements.

Platform and codebase. CaLM serves as a multifaceted platform and codebase designed for evaluating the causal reasoning capabilities of language models, catering to diverse needs within the research and development community. Its utility spans website, leaderboards, datasets, and toolkits. (1) Website: CaLM's web presence facilitates easy access to results, resources, documentations, and updates. This accessibility promotes widespread adoption and provides a foundation for both new learners and experienced researchers to explore the framework's capabilities. (2) Leaderboards: CaLM's inclusion of leaderboards provides a competitive and collaborative space for researchers to share their results. Leaderboards highlight the performance of different models on the framework's evaluation criteria, fostering a healthy competition that drives progress in the field. Additionally, they serve as a benchmark for assessing advancements and identifying areas requiring further research. (3) Datasets: CaLM contributes to the dataset community by providing curated sets of causal targets, along with corresponding adaptations, metrics, and errors. These datasets are critical for testing and benchmarking language models. By emphasizing comprehensive coverage, significance, and practicality as aforementioned, CaLM ensures that its datasets are valuable for a wide range of research focuses, from theoretical exploration to applied causal tasks. (4) Toolkits: At its core, CaLM includes a comprehensive set of tools for evaluating the causal reasoning abilities of language models. These toolkits enable researchers to systematically assess models against a defined set of criteria (e.g., causal targets, adaptations, metrics, errors), ensuring that evaluations are consistent, reproducible, and scalable. The toolkits' design allows for the extension or modification of evaluation criteria, making it adaptable to evolving research needs.

# 1.1.6 Considerations at a Broader Level

Before delving into the empirical findings, we aim to clarify our considerations from a broader perspective. (1) The choice of metrics for evaluating model performance deserves careful consideration. While we select widely recognized metrics that have proven useful in previous studies, there is no single metric that can capture all aspects of a model's performance. Different metrics may yield different insights into a model's strengths and weaknesses, and should be chosen based on the specific aims of the study. (2) Understanding the reasoning behind a model's predictions is crucial for real world applications, particularly in sensitive domains such as healthcare and criminal justice. While our evaluation focuses primarily on quantitative performance metrics, the qualitative aspect of how interpretable these models are remains an essential area for further investigation (e.g., Chen et al. (2024)). (3) Similar to Liang et al. (2022), we evaluate 28 models using the same causal targets, adaptation strategies and metrics. Despite this uniformity, variations exist among the models themselves, with some settings that are more suitable to achieve optimal performance than others. Thus, a model's poor performance in CaLM does not necessarily reflect its overall causal reasoning abilities. (4) The extent to which models have been exposed to the open-source datasets we use might vary significantly. Although we have constructed approximately  $90\%$  of our datasets to mitigate training-test contamination (Liang et al., 2022), this issue may still be unavoidable. (5) Our dataset construction employs similar templates across various causal scenarios, detailed in Dataset Construction (Section 4.2). This approach serves as a double-edged sword. Positively, it tests the model's ability to recognize subtle differences within similarly worded causal scenarios. The model must identify the essence of the problem, and provide an appropriate solution based on

this understanding. However, this approach also limits dataset diversity, potentially hindering an extensive evaluation of the models' causal reasoning capabilities (Cobbe et al., 2021). Acknowledging this limitation, we plan to improve dataset diversity in future research to enable a more detailed examination of these capabilities.

# 1.2 Empirical Findings

Within the CaLM framework, we conduct comprehensive evaluations on 92 causal targets, covering 46 causal tasks across all four levels of the causal ladder, in three textual modes, and in two languages. Additionally, we incorporate 9 adaptations, apply 7 metrics, and catalog 12 types of errors. A dataset consisting of 126,334 data samples is constructed to facilitate thorough evaluations of 28 models, resulting in a total of 38,910,872 queries.

Through the comprehensive analysis of extensive experimental results, we distill the following 50 high-level findings across various dimensions:

# 1.2.1 Findings from the Model

(1) Causal reasoning inability. At present, language models struggle to perform tasks requiring sophisticated causal reasoning effectively. As the complexity of causal reasoning increases, the accuracy of each model progressively deteriorates, eventually falling almost to zero (Figure 9.21).

(2) Dual effects of Reinforcement Learning from Human Feedback (RLHF). On the one hand, exploiting human feedback enables RLHF to align model outputs more closely with human reasoning, particularly in complicated scenarios that demand an understanding of causality. This alignment can modestly improve the model's causal reasoning capabilities (Figure 9.10). On the other hand, models fine-tuned with RLHF tend to change their responses when interacted with by humans. They frequently modify their initial answers, even when they are correct, based on user instructions, indicating a susceptibility to human input (Figure 9.42).

(3) Challenges with Supervised Fine-Tuning (SFT) in causal reasoning. There is only a minimal performance gap in causal reasoning between models trained via SFT on datasets unrelated to causality and those only subjected to pre-training. This suggests that applying SFT to non-causality datasets in the hope of generalizing to causal reasoning might not be effective. A more straightforward method to enhance a model's causal reasoning seems to employ datasets directly related to causality for SFT (Figure 9.10).

(4) Progression of causal reasoning capabilities in OpenAI's model series. Our evaluation covers a wide range of OpenAI's model releases, including the GPT-3 series from 2020, the InstructGPT and GPT-3.5 series from 2022, and the GPT-4 released in 2023 (for more information, refer to Models (Section 8)). Although some GPT-3 and InstructGPT APIs have now been deprecated, their inclusion in our study is crucial for understanding the evolutionary progress in OpenAI's model series. Each new model iteration has exhibited substantial improvements in their ability to perform causal reasoning tasks (Figure 9.6 and Figure 9.9). Furthermore, there has been a noticeable increase in the integration of accuracy and robustness within OpenAI's models (Figure 9.13).

(5) Challenges of causal reasoning in Mathematical mode. Language models demonstrate a certain level of proficiency in solving causal reasoning tasks in both Natural and Symbolic modes. However, their performance in Mathematical mode reveal significant room for improvement. This mode requires

models to not only comprehend causal concepts but also to perform precise computations, presenting a dual challenge (Figure 9.1).

(6) Ascending difficulties in rungs of causal ladder. The model's proficiency in causal reasoning decreases from the lower to the higher levels of the causal ladder, indicating that the more advanced levels present greater difficulties. Models show better performance at the foundational stages (i.e., causal discovery and association) than at the more complex stages (i.e., intervention and counterfactuals) (Figure 9.3).

(7) Comparing open vs. limited access models. Overall, limited access models exhibit superior causal reasoning capabilities than open models. However, in the majority of causal scenarios at the causal discovery level, the performance gap between open and limited access models is minimal, not exceeding a  $2\%$  margin. This modest gap encourages an optimistic perspective on the potential of open models. Additionally, we aim for CaLM to act as a catalyst for the development of models within the open-source community (Figure 9.5).

(8) Impact of scaling on causal reasoning ability. The relationship between model scale and accuracy in causal reasoning does not display a straightforward monotonic increase. This implies that other factors, such as training data and strategy, significantly influence accuracy across models from different creators. However, within models from the same creator, scale remains a consistent and reliable predictor of accuracy (Figure 9.9).

(9) Balancing instruction-following and error correction. When confronted with adversarial prompts, the model tends to alter its previous responses. Notably, it is more likely to change initially correct answers to incorrect ones rather than rectify pre-existing errors. This tendency highlights the urgent need to balance the model's ability to follow instructions with its proficiency in identifying and correcting errors (Figure 9.40 and Figure 9.41).

# 1.2.2 Findings from the Adaptation

(10) Optimal prompt varies across causal scenario. No "optimal prompt" universally fits all causal scenarios. Based on our observations, for scenarios at the lower levels of the causal ladder (i.e., causal discovery and association), employing 1/3-shot IcL proves effective. For scenarios at the intervention level, 3-shot IcL is recommended, and adding more shots may be beneficial if possible. For the counterfactuals level, which requires detailed reasoning to determine the correct response, we suggest using manual CoT (Figure 9.19).

(11) Challenges of using prompts in complex causal scenarios. The effectiveness of prompts in improving model performance is not consistent across all scenarios. Complex causal scenarios pose a particular challenge for language models, often due to the absence of substantial information on these scenarios within the model's training corpus. Moreover, questions in these scenarios cannot be adequately resolved merely through common sense or semantic understanding. In CaLM, we observe that in such complex causal scenarios, prompts do not markedly improve model performance (Figure 9.19).

(12) Improving model performance with 3-shot IcL and manual CoT. Using 3-shot IcL improves the baseline performance of various models by providing a consistent format for answers along with a rich set of examples. For top-tier models (e.g., GPT-4), manual CoT is particularly effective in harnessing

their advanced causal reasoning capabilities. Through precise, step-by-step reasoning, manual CoT helps these models better comprehend the implications behind questions, thus substantially improving their overall performance (Figure 9.4).

(13) Sensitivity to prompt's shot variation. Across all causal scenarios, there is no strong correlation among prompts within the same category when the number of examples varies (e.g.,  $0/1/3$ -shot IcL, as well as 0-shot/manual CoT). This weak correlation suggests that models are highly sensitive to changes in the number of shots in prompts. It further emphasizes the importance of carefully selecting the number of shots in prompts to tailor model performance effectively (Figure 9.12).

(14) Effectiveness of few shots in complex causal tasks. The more challenging the causal task, the more beneficial additional examples in the prompt are for improving model performance. In CaLM, we assess difficulty across three dimensions: the causal ladder (with intervention and counterfactuals being the most challenging), mode (with Mathematical mode being more demanding), and question type (with probability calculations being particularly difficult). Our thorough analysis suggests that increasing the number of shots for these challenging tasks significantly improves performance. However, due to constraints on time and resource, IcL is currently limited to three shots. While we advocate for using more examples, the decision to set an upper limit should be made based on specific circumstances (Figure 9.38).

(15) Limited effectiveness of 0-shot prompts. One of our objectives is to identify a prompt that is simple to construct yet effectively enhance the model's causal reasoning abilities. To this end, we experimented with three variations of 0-shot prompts: 0-shot CoT, 0-shot IcL and EF, none of which include examples. Comparative analyses reveal that these prompts do not substantially outperform the basic prompt, and their effectiveness varies across different causal scenarios (Figure 9.4, Figure 9.19 and Figure 9.23).

(16) Correlations between prompts. The basic prompt significantly correlates with adversarial doubt, adversarial ignore, EF, 0-shot CoT, and 0-shot IcL. However, it shows no strong correlation with more complex prompts such as 3-shot IcL and manual CoT. For prompts showing strong correlations, it is feasible to approximate a model's performance across similar prompts based on its performance with any one of them. Conversely, the absence of strong correlations with certain prompts offer opportunities for designing more diverse and effective prompts in the future (Figure 9.11 and Figure 9.12).

# 1.2.3 Findings from the Causal Ladder

(17) Consistent model capabilities in causal reasoning across scenarios. The causal reasoning capabilities of models show inherent consistency across the four levels of the causal ladder. Specifically, in 19 scenarios (excluding CEI and CB), there is a positive correlation in model performance. This observation suggests that a model's causal reasoning ability is cohesive, not limited to specific scenarios (Figure 9.17).

(18) Correlations within the causal ladder. Causal scenarios that fall within the same level of the causal ladder and share the same mode tend to exhibit higher correlations in performance. This trend underscores the validity of our hierarchical organization of causal scenarios (Figure 9.17).

# 1.2.4 Findings from the Domain

(19) Comparing seen vs. unseen dataset. The impact of using seen (open-source) and unseen (self-constructed) datasets on model performance is influenced by the complexity of the causal tasks. For more complex tasks at the intervention and counterfactuals levels, models tend to perform better on open-source datasets than on self-constructed ones. Conversely, for simpler tasks related to causal discovery, models show slightly superior performance on self-constructed datasets than on those that are publicly available (Figure 9.8).

# 1.2.5 Findings from the Mode

(20) Correlations among text modes. The three modes selected for our analysis - Natural, Symbolic, and Mathematical - are all rooted in textual data, with Natural mode serving as the primary basis. Our experimental results show a marked correlation between the Natural mode and the other two modes, highlighting interconnected capabilities across these modes (Figure 9.14).

# 1.2.6 Findings from the Language

(21) Performance differences between English and Chinese datasets. In almost  $90\%$  of the causal scenarios, models demonstrate superior performance on English datasets. The trend is likely attributed to the dominance of English in the training data of language models. As these models are deployed globally, it is crucial to ensure training involves balanced and diverse language corpora to improve performance across various languages (Figure 9.7).

# 1.2.7 Findings from the Metric

(22) Variability in model's robustness and accuracy across causal scenarios. The relationship between a model's robustness and accuracy significantly varies across causal scenarios. In more challenging causal scenarios, such as PN and PS, models may show very low accuracy but disproportionately high robustness. This is primarily because the models' responses remain consistently poor, unaffected by disturbances. In contrast, in simpler scenarios like PCD and AR, there tends to be a positive correlation between accuracy and robustness, suggesting that as models perform better, they also become more stable. However, in scenarios such as ECI, EAE, and AC, the interaction between these metrics does not follow a clear or consistent pattern (Figure 9.13).

(23) Assessing the maturity of causal scenarios. We employ three metrics to evaluate the maturity of a causal scenario: understandability, open-limited gap, and solvability. Most causal scenarios are considered hard or more difficult in terms of understandability. In the open-limited gap metric, limited access models predominantly occupy the top 5 positions across the majority of scenarios, indicating their superior performance. When evaluating solvability, it becomes evident that current model capabilities are not yet sufficient to fully tackle the challenges posed by CaLM. Overall, the ability of models to effectively resolve causal scenarios within CaLM remains nascent (Figure 9.22).

# 1.2.8 Findings from the Error

(24) Model capabilities and limitations in following instructions. All models inherently possess ability to generate content and typically do not produce empty responses, even when faced with challenging questions. However, their capacity to accurately follow instructions remains limited. Often, these

models struggle to provide the most straightforward response as specified by the instructions, indicating a significant room for improvement in following instructions (Table 9.3).

(25) Reduction of repetitions through SFT. SFT equips models with high-quality input-output pairs, effectively mitigating unnecessary repetitions in responses to questions (Table 9.3).

(26) Improving instruction following with 1-shot and 3-shot IcL. Utilizing 1-shot and 3-shot IcL provides models with standardized, concise examples, facilitating the learning of effective response patterns. This helps models produce outputs that better conform to the specified answer format (Figure 9.25).

(27) Imitation effects from prompts. Employing 1-shot IcL, 3-shot IcL, and manual CoT might lead to an "imitation game" where models mimic the patterns presented in the examples. Specifically, after generating standardized responses, these models begin crafting their own questions, reflecting the learned patterns (Figure 9.25).

(28) Language inconsistency in 0-shot CoT. Some models struggle to systematically process and respond to complex Chinese questions when using 0-shot CoT. This challenge can lead to off-topic initial responses in Chinese, followed by a switch to English, although these subsequent English responses often continue to be irrelevant to the posed question (Figure 9.25 and Figure 9.26).

(29) Prevalence of identical responses across questions. The majority of models (26 out of 28) show the tendency to provide the same response to different questions, indicating their fundamental inability to effectively handle the causal task. This issue, if observed in one question type (e.g., binary classification), is likely to manifest similarly across other question types (e.g., choice selection, probability calculation) (Figure 9.27).

# 1.2.9 Findings from the Causal Scenario

(30) Pairwise causal discovery (PCD). PCD seeks to establish if a causal relationship exists between two given events and to identify which of the two is the cause and which is the effect. The understandability of the scenario is easy. The leading three performers in this scenario are GPT-4 (79.1%), GPT-3.5-Turbo (75.2%), and text-davinci-003 (74.7%). The top model-prompt pair is GPT-4 with EF, achieving an accuracy of 83.0%. The solvability of the scenario is well-solved as the average accuracies of the top three models all exceed 70%. The most stable models, characterized by the lowest model volatility, are GPT-3.5-Turbo (1.3), Baichuan1 (7B) (2.1), and text-curie-001 (2.2). The models displaying the greatest sensitivity to different prompts, evidenced by their high model volatility, are Vicuna-v1.3 (33B) (15.8), Llama2 (70B) (15.6), and Llama2-chat (70B) (14.3). The most effective prompts are 3-shot IcL and 1-shot IcL, which improve average accuracy by 9.0% and 7.0% respectively (Section 9.4.1).

(31) Event causality identification (ECI). ECI requires the model to assess whether there is a causal relationship between two events within a given sentence. The understandability of the scenario is easy. The top three models by average accuracy are GPT-4 at  $65.6\%$ , text-davinci-003 at  $61.1\%$ , and Claude2 at  $58.4\%$ . The top model-prompt pair is GPT-4 with adversarial doubt, reaching an accuracy of  $67.0\%$ , indicating the scenario has a challenging solvability since the performance of the top model-prompt pair does not exceed  $80\%$ . The three most stable models in the scenario, characterized by the lowest model volatility, are GPT-4 with a model volatility of 1.1, Baichuan2-chat (13B) with 1.6, and Qwen (7B) with 2.1. Conversely, the models exhibiting the highest model volatility, are InternLM-chat (20B) at 23.6,

text-babbage-001 at 11.3, and Llama2 (7B) at 11.2. The leading two prompts, achieving the greatest average accuracy improvements over the basic prompt, are 1-shot IcL with a gain of  $3.1\%$  and 3-shot IcL with  $2.1\%$  (Section 9.4.1).

(32) Abstract reasoning (AR). AR investigates the capability of language models to identify and understand causal relationships within symbolic causal graphs. This scenario is classified to have an easy understandability. The top three models by average accuracy: GPT-4 at  $88.3\%$ , Claude2 at  $75.9\%$ , and text-davinci-003 at  $74.5\%$ . GPT-4, employing manual CoT, stands out as the top model-prompt pair with a  $92.6\%$  accuracy. The solvability of the scenario is well-solved with each of the top three models' average accuracies exceeding  $70\%$ . The three most stable models in the scenario, characterized by the lowest model volatility, are GPT-4 at 2.0, Qwen (7B) at 2.3, and InternLM-chat (20B) at 2.6. Conversely, the most unstable models are Llama2-chat (70B) at 21.6, Llama2 (70B) at 21.1, and Llama2 (7B) at 17.0. The leading two prompts by average accuracy gain over the basic prompt are 0-shot IcL and 1-shot IcL, both at  $1.5\%$  (Section 9.4.1).

(33) Causal attribution (CA). CA refers to the process of determining which specific factor is responsible for an outcome. The scenario has an easy understandability. GPT-4 leads with an average accuracy of  $91.8\%$ , followed by text-davinci-003 at  $77.1\%$ , and Claude2 at  $74.0\%$ . GPT-4, when paired with manual CoT, achieves an impressive  $94.8\%$ . The solvability of this scenario is well-solved given that the top three models all have average accuracies over  $70\%$ . The three most consistent models, characterized by the lowest model volatility, are GPT-4 at 1.4, davinci (175B) at 2.4, and GPT-3.5-Turbo at 3.0, showcasing their robustness across various prompts. Conversely, the models demonstrating the highest model volatility, are Llama2-chat (70B) at 20.5, Llama2 (70B) at 13.6, and Llama2 (7B) at 11.6. The two prompts with the highest average accuracy gain over the basic prompt are 1-shot IcL at  $1.0\%$  and 0-shot IcL at  $0.8\%$  (Section 9.4.1).

(34) Correlation (CORR). CORR requires the model to identify statistical association between variables. The understandability of the scenario is hard. The leading three models by average accuracy are GPT-4 at  $59.1\%$ , text-davinci-003 at  $54.7\%$ , and text-davinci-002 at  $54.3\%$ . Claude2, using EF, stands out with a top score of  $68.0\%$ , illustrating the scenario solvability as challenging since the highest top model-prompt pair's performance does not reach  $80\%$ . The models that have the highest the model volatility are InternLM-chat (20B) at 17.4, ada (0.35B) at 14.7, and text-ada-001 at 14.1. Conversely, the most stable models include Baichuan1 (7B) at 0.5, Qwen (7B) at 1.2, and text-davinci-001 at 1.9. The top two prompts for average accuracy gain over the basic prompt as 3-shot IcL at  $6.2\%$  and 1-shot IcL at  $5.7\%$  (Section 9.4.2).

(35) Explaining away effect (EAE). EAE describes a causal relationship where two independent causes that produce a common effect become interdependent when that effect is observed. The understandability of the scenario is hard. GPT-4 at  $67.9\%$ , Claude2 at  $66.7\%$ , and text-davinci-003 at  $57.0\%$  as the top three models by average accuracy. As to the top model-prompt pair, GPT-4, through the use of manual CoT, achieves a remarkable  $90.5\%$ , indicating the solvability of the scenario is potentially solvable as the top model-prompt pair's performance surpasses  $80\%$ . The models have the highest model volatility are Llama2 (70B) at 18.8, Llama2 (13B) at 17.0, and Llama2 (7B) at 17.0. Conversely, the most stable models include Qwen (7B) at 2.1, davinci (175B) at 3.1, and Baichuan1 (7B) at 3.3. The top two prompts for average accuracy gain over the basic prompt as 3-shot IcL at  $5.5\%$  and 1-shot IcL at  $3.9\%$  (Section 9.4.2).

(36) Average treatment effect (ATE). ATE aims to quantify the impact of a particular intervention. This

causal scenario have a hard understandability. The leading models in terms of average accuracy for this causal scenario are GPT-4 at  $54.8\%$ , text-davinci-003 at  $50.3\%$ , and GPT-3.5-Turbo at  $47.7\%$ . The top model-prompt pair is GPT-4 with manual CoT, reaching an impressive  $92.8\%$ , indicating the scenario's solvability is potentially solvable given that the top model-prompt pair exceeds  $80\%$ . The three most stable models, indicated by the lowest model volatility, are Baichuan1-chat (13B) at 2.4, Baichuan2-chat (13B) at 3.0, and InternLM-chat (20B) at 6.4. Conversely, the three models exhibiting the greatest instability across various prompts, shown by the highest model volatility, are Llama2 (13B) at 34.8, Llama2 (70B) at 30.2, and Llama2 (7B) at 28.4. The two prompts leading in average accuracy gain relative to the basic prompt are 3-shot IcL at  $25.0\%$  and manual CoT at  $22.4\%$  (Section 9.4.3).

(37) Backdoor adjustment set (BAS). BAS contains variable that blocks all backdoor paths from the treatment variable to the outcome variable. This scenario challenges whether the model can discern the BAS. This causal scenario is viewed to have a hard understandability. The leading models by average accuracy in this causal scenario are GPT-4 at  $71.6\%$ , text-davinci-003 at  $53.7\%$ , and GPT-3.5-Turbo at  $49.8\%$ . The top model-prompt pair, GPT-4 with 3-shot IcL, reaches  $75.1\%$ , indicating that the solvability of this scenario is challenging due to the top model-prompt pair's performance not exceeding  $80\%$ . The three most consistent models, based on the lowest model volatility, are text-davinci-001 at 1.4, text-curie-001 at 2.3, and GPT-4 at 2.6. In contrast, the models exhibiting the greatest variability, marked by the highest model volatility across different prompts, are Llama2 (70B) at 16.2, Vicuna-v1.3 (33B) at 11.9, and Llama2 (13B) at 11.8. The two prompts that lead to the highest average accuracy gains over the basic prompt are 3-shot IcL with a  $12.1\%$  gain and 1-shot IcL with a  $9.8\%$  gain (Section 9.4.3).

(38) Frontdoor adjustment set (FAS). FAS involves a set of variables that mediate the causal path from the treatment to the outcome. The model needs to choose the correct FAS. This causal scenario has a hard understandability. The leading three models by average accuracy: GPT-4 at  $77.2\%$ , text-davinci-003 at  $59.9\%$ , and GPT-3.5-Turbo at  $54.0\%$ . GPT-4, employing 3-shot IcL, tops the chart with a  $95.2\%$  accuracy. GPT-4, employing 3-shot IcL, is the top model-prompt pair with a  $95.2\%$  accuracy. With the top model's average accuracy surpassing  $70\%$ , the solvability of this scenario is solvable. The most prompt-sensitive models, indicated by the highest model volatility, are text-davinci-002 at 18.4, Claude2 at 17.1, and text-davinci-003 at 14.9. In contrast, the most stable models include davinci (175B) at 1.8, text-curie-001 at 3.4, and Baichuan2-chat (13B) at 3.5. The top two prompts for average accuracy gain over the basic prompt as 3-shot IcL at  $13.3\%$  and 1-shot IcL at  $10.6\%$  (Section 9.4.3).

(39) Instrumental variable (IV). IV influences the treatment variable but has no direct effect on the outcome variable, except through the treatment. This scenario assesses whether the model can identify the IV. The understandability of the scenario is hard. The leading three models by average accuracy are GPT-4 at  $74.8\%$ , text-davinci-003 at  $56.5\%$ , and text-davinci-002 at  $53.7\%$ . GPT-4, employing 3-shot IcL, achieves a top score of  $78.9\%$ , suggesting the solvability of this scenario as challenging since the top model-prompt pair's performance doesn't reach  $80\%$ . The models most susceptible to prompt variations, as shown by the highest model volatility, are Vicuna-v1.3 (33B) at  $16.7\%$ , ada (0.35B) at  $15.9\%$ , and Llama2 (13B) at  $15.1\%$ . Conversely, the most stable models include text-curie-001 at  $0.5\%$ , GPT-4 at  $3.0\%$ , and InternLM-chat (20B) at  $3.3\%$ . The top two prompts for average accuracy gain over the basic prompt as manual CoT at  $15.2\%$  and 3-shot IcL at  $13.2\%$  (Section 9.4.3).

(40) Collider bias (CB). CB occurs when an analysis is conditioned upon a common effect of two or more variables. It evaluates whether the model can exclude the interference of bias and make the correct choice. The understandability of the scenario is hard. The top three models by average accuracy are

GPT-4 at  $62.7\%$ , text-davinci-003 at  $53.2\%$ , and text-davinci-002 at  $53.0\%$ . The top model-prompt pair is GPT-4 with manual CoT, which achieves an impressive  $97.8\%$ , suggesting the solvability of this scenario as potentially solvable. The models most sensitive to prompt variations, as shown by the highest model volatility, are Llama2 (70B) at  $20.9\%$ , Koala (13B) at  $16.8\%$ , and GPT-4 at  $16.2\%$ . Conversely, the most stable models are text-curie-001 at  $2.6\%$ , curie (6.7B) at  $4.3\%$ , and Wizardcoder (15B) at  $4.9\%$ . The top two prompts for average accuracy gain over the basic prompt as manual CoT at  $15.5\%$  and 3-shot IcL at  $13.7\%$  (Section 9.4.3).

(41) Causal effect identification (CEI). CEI centers on evaluating the model's ability to judge whether the causal effect of a treatment on an outcome can be estimated from observational data. This causal scenario has a very hard understandability and CEI shows the lowest correlation with other causal scenarios. The leading models in this causal scenario, based on average accuracy, are GPT-3.5-Turbo at  $49.9\%$ , text-curie-001 at  $49.6\%$ , and Baichuan1 (7B) at  $49.4\%$ . The top model-prompt pair, GPT-4 with 3-shot IcL, reaches  $59.0\%$ , indicating the solvability of the scenario as challenging due to the top model-prompt pair's performance falling short of  $80\%$ . The three most stable models, based on the lowest model volatility, are text-curie-001 at 0.9, text-davinci-001 at 1.0, and Qwen (7B) at 1.0. Conversely, the models demonstrating the highest levels of instability across various prompts are Llama2 (70B) at 18.1, Llama2-chat (70B) at 15.9, and GPT-4 at 12.9. The two prompts leading in average accuracy gain over the basic prompt are 1-shot IcL at  $6.6\%$  and 3-shot IcL at  $5.4\%$  (Section 9.4.3).

(42) Controlled direct effect (CDE). CDE quantifies the direct influence of an intervention on an outcome, while keeping the mediator to a predetermined level. This causal scenario has a hard understandability. The leading models in terms of average accuracy for this causal scenario are GPT-3.5-Turbo at  $47.6\%$ , GPT-4 at  $41.9\%$ , and Claude2 at  $34.5\%$ . The top model-prompt pair is GPT-4 with manual CoT, reaches accuracy at  $90.8\%$ , suggesting the scenario's solvability as potentially solvable given the top model-prompt pair surpasses  $80\%$ . The three models exhibiting the greatest stability with the lowest model volatility are Baichuan1-chat (13B) at 2.7, babbage (1.3B) at 2.8, and ada (0.35B) at 3.6. Conversely, the three models showing the highest levels of instability across various prompts are Llama2 (70B) at 27.8, Llama2 (13B) at 26.7, and Llama2 (7B) at 25.7, showcasing a pronounced sensitivity to different prompts. The two prompts leading in average accuracy gain over the basic prompt are 3-shot IcL at  $21.7\%$  and manual CoT at  $20.9\%$ . (Section 9.4.3).

(43) Counterfactual reasoning (CR). CR involves contemplating hypothetical scenarios by modifying certain factors or conditions present in an actual situation. This causal scenario has an easy understandability. The three leading models in this causal scenario by average accuracy are GPT-4 at  $76.9\%$ , text-davinci-003 at  $67.8\%$ , and Claude2 at  $62.5\%$ . The top model-prompt pair is GPT-4 with manual CoT, achieving an  $83.2\%$  accuracy. The scenario has a solvable solvability with the top model's average accuracy surpassing  $70\%$ . The three most consistent models, characterized by the lowest model volatility, are curie (6.7B) at 1.8, text-curie-001 at 3.2, and Baichuan1-chat (13B) at 3.4. Conversely, the models displaying the greatest variability across various prompts, showcasing their great sensitivity to prompts, are Llama2 (70B) at 15.4, Llama2-chat (70B) at 14.2, and Vicuna-v1.3 (33B) at 11.9. The two prompts leading to the highest average accuracy improvements over the basic prompt are manual CoT at  $7.3\%$  and 3-shot IcL at  $6.0\%$  (Section 9.4.4).

(44) Actual causality (AC). AC deals with attribution and responsibility allocation problems encountered in practical applications. The causal scenario's understandability is hard. GPT-4 leads in average accuracy at  $65.6\%$ , followed by text-davinci-003 and GPT-3.5-Turbo, with scores of  $57.2\%$  and  $56.5\%$ , respectively.

GPT-4, when paired with manual CoT prompts, achieves a significant  $68.2\%$  in accuracy, yet this top performance is still short of the 80 threshold, indicating the challenging of the causal scenario. In the stability of model responses, Llama2 (70B), curie (6.7B), and Llama2-chat (70B) show the greatest variations in performance across different prompts, while GPT-3.5-Turbo, GPT-4, and text-curie-001 demonstrate remarkable consistency according to their low model volatility. 1-shot IcL and 3-shot IcL leading to the highest average accuracy gains, at  $15.8\%$  and  $13.9\%$ , respectively. (Section 9.4.4).

(45) Causal explanation generation (CEG). CEG examines whether the LLMs can generate comprehensive and logically sound explanations that elucidate the cause-effect relationships between specific events. The causal scenario's understandability is easy. Claude2, GPT-3.5-Turbo, and GPT-4 emerge as the top three models by average accuracy. Claude2, using EF, reaches a peak accuracy of  $63.4\%$ , positioning the solvability of this scenario as challenging since the top model-prompt pair does not achieve an accuracy of  $80\%$ . The models demonstrating the greatest variance in response to different prompts, as indicated by the highest model volatility, include Koala (13B) and Llama2-chat (70B). In contrast, the models with the least variance are InternLM-chat (20B), Baichuan1 (7B), and Qwen (7B). Adversarial doubt and manual CoT as the top two prompts for average accuracy gain over the basic prompt (Section 9.4.4).

(46) Effect of the treatment on the treated (ETT). ETT assesses whether individuals who receive treatment are the ones who would derive the greatest advantage from it. This causal scenario has a hard understandability. The leading three models in this causal scenario by average accuracy are GPT-4 at  $40.9\%$ , GPT-3.5-Turbo at  $39.0\%$ , and Claude2 at  $35.6\%$ . GPT-4, when combined with manual CoT, reaches an impressive  $89.9\%$ , suggesting this scenario's solvability is potentially solvable, given that the top model-prompt pair achieves over  $80\%$ . The three most consistent models, marked by the the lowest model volatility, are Baichuan1-chat (13B) with a model volatility of 2.5, InternLM-chat (20B) at 4.3, and Baichuan2-chat (13B) at 7.8. Conversely, the models showing the highest sensitivity to prompt variations, as evidenced by the highest model volatility, are Llama2 (13B) at 24.1, Llama2 (70B) at 23.8, and Llama2 (7B) at 23.7. The two prompts leading to the highest average accuracy improvements over the standard prompt are manual CoT with a gain of  $30.4\%$  and 3-shot IcL at  $16.7\%$  (Section 9.4.4).

(47) Natural direct effect (NDE). NDE quantifies the direct influence of an intervention on an outcome, while keeping the mediator's natural state. This causal scenario's understandability is regarded as hard. The top model-prompt pair is GPT-4 with manual CoT, reaching an accuracy of  $80.1\%$ , indicating that the solvability of this scenario is potentially solvable as the top model-prompt pair's performance hits  $80\%$ . The three most stable models, characterized by the lowest model volatility, are Baichuan1-chat (13B) at 2.3, InternLM-chat (7B) at 3.0, and InternLM-chat (20B) at 3.1. Conversely, the three least stable models, exhibiting the highest model volatility across different prompts, are Llama2 (13B) at 20.3, Llama2-chat (70B) at 18.2, and Llama2 (70B) also at 18.2. The leading two prompts achieving the most significant average accuracy improvements over the basic prompt are manual CoT at  $19.1\%$  and 3-shot IcL at  $9.9\%$  (Section 9.4.4).

(48) Natural indirect effect (NIE). NIE measures the extent of change in the outcome through the mediator when the treatment is modified. This causal scenario is considered to have a hard understandability. The top model-prompt pair is Koala (13B) with 3-shot IcL, achieving a  $73.3\%$  accuracy, suggesting the solvability of this scenario is challenging as the performance of the top model-prompt pair surpasses the random guess but remains below  $80\%$ . The three most stable models, characterized by the lowest model volatility, are Baichuan1-chat (13B) at 2.4, Baichuan2-chat (13B) at 4.5, and Vicuna-v1.3 (33B) at 4.8. Conversely, the three most unstable models, showcasing the highest model volatility across various

prompts, are Llama2 (7B) at 30.8, Llama2 (13B) at 30.4, and Baichuan2-chat (7B) at 24.9, reflecting their pronounced sensitivity to prompt variations, reflecting their pronounced sensitivity to prompt variations. The two prompts leading to the highest average accuracy improvements over the basic prompt are 3-shot IcL at  $29.3\%$  and manual CoT at  $19.5\%$  (Section 9.4.4).

(49) Probability of necessity (PN). PN essentially seeks to address the question: "In cases where the outcome occurs, could it still happen without the treatment?" The understandability of PN scenario is considered as very hard to understand. The three highest-performing models in terms of average accuracy within this causal scenario are GPT-4 at  $14.5\%$ , GPT-3.5-Turbo at  $8.1\%$ , and Llama2 (70B) at  $5.2\%$ . The top model-prompt pair, GPT-4 with manual CoT, achieves a significant  $50.2\%$  accuracy, indicating the solvability of this scenario is challenging as the performance of the top model-prompt pair exceeds the random guess yet does not reach  $80\%$ . The three most stable models, characterized by the lowest model volatility, are Wizardcoder (15B) at 0.0, text-curie-001 at 0.1, and davinci (175B) at 0.3. Conversely, the three models showing the greatest instability across different prompts, indicated by the highest model volatility, are GPT-4 at 15.2, GPT-3.5-Turbo at 11.6, and text-davinci-003 at 9.8, reflecting their pronounced sensitivity to prompt changes. The two prompts leading to the most substantial average accuracy improvements over the basic prompt are 3-shot IcL at  $7.2\%$  and manual CoT at  $6.1\%$  (Section 9.4.4).

(50) Probability of sufficiency (PS). PS addresses: "In cases where the outcome does not occur, could it happen if a treatment exists?" This causal scenario's understandability is very hard. The leading three models in this causal scenario based on average accuracy are GPT-4 at  $12.6\%$ , GPT-3.5-Turbo at  $5.8\%$ , and text-davinci-003 at  $4.6\%$ . The top model-prompt pair is GPT-4 with manual CoT, achieving a score of  $46.8\%$ , indicating that the solvability of this scenario is challenging as the top model-prompt pair exceeds the random guess yet does not reach  $80\%$ . There are more than three models with zero model volatility in the scenario. Conversely, the models exhibiting the greatest instability across various prompts, indicated by the highest model volatility, are GPT-4 at 14.6, GPT-3.5-Turbo at 13.5, and text-davinci-003 at 11.2, showcasing their significant sensitivity to prompt variations. The two prompts leading to the highest average accuracy improvements over the basic prompt are manual CoT at  $6.9\%$  and adversarial ignore at  $0.2\%$  (Section 9.4.4).

# 1.3 Contributions

In summary, we have the following contributions:

1. The CaLM framework. We introduce CaLM, a novel framework designed to systematically assess the causal reasoning capabilities of language models. It establishes a foundational taxonomy that integrates causal targets, adaptations, metrics, and error types, enabling a thorough navigation through the complex design space of causal reasoning assessment. By employing this well-defined taxonomy and its practical application, CaLM demonstrates unmatched flexibility and scalability in assessing language models' abilities to reason causally.

2. Wide coverage. Our taxonomy defines a wide-reaching, if not entire, design space for evaluating the causal reasoning capabilities of language models. Based on the taxonomy, we select and implement a core set of 92 causal targets, 9 adaptations, 7 metrics, and 12 types of errors. These 92 causal targets cover 46 distinct causal tasks spanning all four levels of the causal ladder, across three textual modes and in two languages. This constitutes the most thorough and detailed causal evaluation benchmark

available to date. Furthermore, we conduct a systematic evaluation of 28 leading language models, including 15 open-access and 13 limited-access models from both academic and industrial sectors, using this benchmark.

3. Comprehensive analysis. We conduct in-depth analyses of causal reasoning evaluation results across all the dimensions of causal scenario, mode, language, adaptation, model, metric, and error type. Our study dually examines the impact of these dimensions on the causal reasoning abilities of language models. Furthermore, our investigation delves into both intra-dimensional relationships (e.g., among various prompt types) and inter-dimensional relationships (e.g., between causal scenario and prompt types) within the context of causal reasoning. Moreover, we thoroughly analyse the impact of additional critical factors (e.g., model scale, model access, training strategy) on model performance. Beyond these overarching analyses, it is worth noting that we also deliver a thorough and detailed examination of each specific causal scenario, mode, language, adaptation, model, metric, and error type.

4. Empirical findings. Our extensive evaluation, detailed in Experiments and Results (Section 9), yields 50 high-level empirical findings across 9 dimensions: model, adaptation, causal ladder, causal scenario, domain, mode, language, metric, and error. These findings confirm existing research in some instances and reveal new insights into contemporary language models in others. Such insights are instrumental for the development of future language models and pave the way for in-depth analysis. Importantly, our study extends beyond mere causal reasoning capabilities of these models, underscoring their broad applicability across varied use cases. We anticipate that this work will motivate researchers from different fields to further explore the implications of our findings or to identify new opportunities not yet addressed in our study.

5. Dataset construction. In light of the notable scarcity of datasets for causal evaluation of language models, we have composed comprehensive Symbolic and Mathematical datasets covering the causal scenarios specified in our study. We also augmented the existing datasets in the Natural mode, as further detailed in Section 4. This effort significantly mitigates training-test contamination, thus enhancing the reliability of our findings. Specifically, our contributions to dataset construction are outlined from the following aspects: (1) Methodology of construction: Our Symbolic and Mathematical mode datasets are intentionally designed to facilitate expansion, allowing for the generation of substantial new data should additional use cases emerge. (2) Dataset size: Overall, our CaLM dataset contains 126,334 data samples. All samples in the Symbolic and Mathematical datasets are self-constructed, owing a total number of 38,400 and 44,800, respectively. Within the 43,134 samples that belong to the Natural mode, 13,567 samples come from open-source datasets, and the remaining 29,567 are self-constructed. Each sub-dataset within the Symbolic and Mathematical datasets consists of 1600 samples, striking a balance between thorough evaluation and cost-effectiveness. (3) Expanding causal scenarios: We introduce four new causal scenarios in the Symbolic mode datasets (i.e., frontdoor adjustment set, instrumental variable, causal effect identification and causal attribution), and three in both the Natural and Mathematical mode datasets (i.e., controlled direct effect, probability of necessity and probability of sufficiency). (4) Enhancing existing work: The Symbolic datasets include extensions to an existing causal scenario with three new domains, and the Mathematical datasets expand four existing causal scenarios with a total of eight new domains. (5) Linguistic expansion: Both the Symbolic and Mathematical datasets are developed in both Chinese and English. For public datasets lacking Chinese versions, we provide our own translations and annotations.

6. Platform and codebase. We establish a comprehensive platform and codebase for evaluating the

causal reasoning capabilities of language models, tailored to the diverse requirements of the research and development community. This platform features a website for easy access to resources and updates, leaderboards for benchmarking and fostering competition, curated datasets for testing models, and toolkits for systematic evaluation. These components ensure consistent, reproducible, and scalable assessments, adaptable to evolving research needs.

# 1.4 Organization

Our paper is structured into 13 sections. Following this introduction, we begin with providing an overview of the prerequisite knowledge in Preliminaries (Section 2). From Causal Targets (Section 3) through Errors (Section 7), we elaborate on each module within the CaLM framework. Models (Section 8) presents the models used for evaluation, followed by an in-depth analysis of the experimental results in Experiments and Results (Section 9). Related Work (Section 10) discusses the work related to CaLM. Gaps in CaLM (Section 11) is dedicated to the components not included in the concrete implementation. The limitations and future directions for CaLM are explored in Limitations and Future Work (Section 12). Finally, the paper concludes with a summary in Conclusion (Section 13).

Specifically, the rest of the paper is organized as follows:

- In Section 2: Preliminaries, we present the foundational elements that are essential for building this paper. This section is primarily comprised of two parts: The Ladder of Causation (Section 2.1) and Structural Causal Models (Section 2.2).

- In Section 3: Causal Targets, we introduce the causal targets, starting with a broad overview of the Taxonomy (Section 3.1). Following this, Concrete Implementation (Section 3.2) details the specific causal targets chosen for our evaluation. The narrative then progresses from Rung 0: Causal Discovery (Section 3.3) to Rung 3: Counterfactuals (Section 3.6), where each causal scenario within the causal targets is thoroughly explained, aligned with the incremental levels of the causal ladder.

- In Section 4: Data Collection, we delve into the datasets used in CaLM. We start by outlining the open-source and self-constructed datasets we employed in Dataset Selection (Section 4.1). Next, Dataset Construction (Section 4.2) elaborates on the process involved in developing our self-constructed datasets. Concluding this part, Data Statistics (Section 4.3) presents an extensive statistical breakdown of the datasets to assist future users.

- In Section 5: Adaptations, we describe the prompts used to interact with the model. The various categories of prompts are introduced in Taxonomy (Section 5.1), and the specific prompts selected are explained in Concrete Implementation (Section 5.2). The last five sections (e.g., Basic Prompt (Section 5.3), Chain-of-Thought (Section 5.5)) offer a comprehensive overview of the five primary types and nine subtypes of prompts that we employed.

- In Section 6: Metrics, we present the metrics used for evaluating the model's causal reasoning ability. Likewise, we initially explain the categorization of current metrics from a broad viewpoint in Taxonomy (Section 6.1), followed by a discussion in Implementation Principles (Section 6.2) on the considerations that influenced our selection of metrics. Lastly, we elaborate on the metrics employed, examining them from three distinct angles (i.e., Metrics for Model (Section 6.3), Metrics for Causal Scenario (Section 6.4) and Metrics for Prompt (Section 6.5)).

- In Section 7: Errors, we consolidate the errors made by models throughout the evaluation. We introduce

in Taxonomy (Section 7.1) how these errors are currently categorized. Following this, we proceed to elaborate on these errors in detail, dividing our discussion into two key parts: Quantitative (Section 7.2) and Qualitative (Section 7.3).

- In Section 8: Models, we describe the language models that are evaluated in CaLM. we categorize models in Taxonomy (Section 8.1) based on different scales, creators, access, etc. Subsequently, the main considerations guiding our model selection are outlined in Concrete Implementation (Section 8.2).

- In Section 9: Experiments and Results, we provide a comprehensive and in-depth analysis of our experiment results, leading to a wealth of insightful conclusions, establishing it as one of our most significant sections. The main focus is Main Results (Section 9.1), where we undertake analysis from various angles (e.g., Comparative Analysis of Models (Section 9.1.1), Analyzing Complexity (Section 9.1.6)). Then, in Prompt Analysis (Section 9.2), we analyze from the perspective of different prompts, offering an alternative viewpoint. Finally, exhaustive analyses of the model and the causal scenario are separately carried out in Model-specific Analysis (Section 9.3) and Causal Scenario-specific Analysis (Section 9.4).

- In Section 10: Related Work, we illustrate the works that pave the way for the development of CaLM. Initially, we revisit the rapid advancement of language models in recent years, as detailed in Advances in Language Models (Section 10.1). Next, we present Evaluations of Language Models' General Abilities (Section 10.2), adopting a wider view to scrutinize how language models are evaluated. Furthermore, we introduce Evaluations of Language Models' Causal Reasoning Abilities (Section 10.3). It is with these exemplary works as a foundation that the construction of CaLM becomes possible. Given that datasets play a crucial role in benchmarks, we conclude by discussing related Causal Benchmark Datasets (Section 10.4).

- In Section 11: Gaps in CaLM, we cautiously review the gaps in the current implementation. Starting from each module of the CaLM framework (i.e., Gaps in Causal Targets (Section 11.1), Gaps in Adaptations (Section 11.2), Gaps in Metrics (Section 11.3), Gaps in Errors (Section 11.4), and Gaps in Models (Section 11.5)), we analyze the disparities between our taxonomy and selection, hoping to provide guidance for potential future research. Besides, due to the rapid development of language models, the challenge of incorporating the latest models into CaLM arises, leading us to summarize the Gaps in Models (Section 11.5).

- In Section 12: Limitations and Future Work, we outline the existing limitations of CaLM. Our analysis is conducted from two specific aspects, Limitations of Concrete Implementation (Section 12.1) and Limitations of Evaluation Results (Section 12.2), through which we endeavor to suggest several potential strategies for enhancement.

- In Section 13: Conclusion, we summarize the entire paper and convey our vision for a brighter future.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f2800c61c84cd4d709118f2f9c9514841f225021c2d7caf0e7f1b64f7437a491.jpg)



(a) Previous work


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d8816f6309fc97102a103e963f439a0c3ddf48d942ddfdd91c542b63fd13e33a.jpg)



(b) CaLM



Figure 1.4 Thorough and standardized evaluation (task-based). (a) Previous studies reveal the uneven and incomplete nature of evaluating causal reasoning abilities of language models across various tasks (* means that this causal task has already been evaluated in existing works, but with different datasets from those we use). (b) Through CaLM, we conduct comprehensive evaluations of 28 models across 46 causal tasks.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9f74b5fd4a85798873c3d1982d195e041ac0f0682e7db243de4a560f42b001a6.jpg)



(a) Previous work


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b45a5b1dc5ccdec2cfb1f8c9db16cf19ef4309bd56eceefef5b52cbe04f926f1.jpg)



(b) CaLM



Figure 1.5 Extensive adaptation strategies (causal scenario-based). (a) These strategies are previously utilized to evaluate the causal reasoning abilities of language models, highlighting issues of imbalance, incompleteness, and a lack of consideration for prompts from a robustness standpoint. (b) In CaLM, we implement 9 adaptations across 21 causal scenarios, leading to a thorough comprehension of the effectiveness and existing constraints associated with different adaptation strategies in enhancing the model's causal reasoning performance.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/12e3d2b567bffb95f06e702ddc973e79ced0875f0b81b3613575efe3fffe23af.jpg)



(a) Previous work


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/35b07088691999fc8045162fb8f8f95a39e52aacc0dadf282dcb4f9447d56b8c.jpg)



(b) CaLM



Figure 1.6 Extensive adaptation strategies (causal task-based). (a) These strategies are previously utilized to evaluate the causal reasoning abilities of language models, highlighting issues of imbalance, incompleteness, and a lack of consideration for prompts from a robustness standpoint (* means that this causal task has already been evaluated in existing works, but with different datasets from those we use). (b) In CaLM, we implement 9 adaptations across 46 causal tasks, leading to a thorough comprehension of the effectiveness and existing constraints associated with different adaptation strategies in enhancing the model's causal reasoning performance.


# 2 Preliminaries

This section establishes the foundation for our analysis of causal evaluation in language models, by introducing key concepts and terminologies in causal reasoning essential for understanding the subsequent discussion. It is structured into two main subsections: The Ladder of Causation (Section 2.1) and Structural Causal Models (Section 2.2).

# 2.1 The Ladder of Causation

The Ladder of Causation, as introduced by Pearl & Mackenzie (2018) and discussed by Bareinboim et al. (2022), is a conceptual framework that illustrates the hierarchy of causal reasoning tasks. It consists of three discernible rungs: association (Rung 1), intervention (Rung 2), and counterfactuals (Rung 3), with each representing a progressively deeper understanding of causality. Additionally, we integrate causal discovery tasks (Spirtes et al., 2000; Peters et al., 2017) into this ladder, acknowledging them as a fundamental phase in causal reasoning (Glymour et al., 2019). For ease of reference and clarity in our ongoing discussion within the CaLM framework, we identify (causal) discovery as Rung 0 on the ladder of causation.

Rung 0: Causal discovery. This rung prioritizes analyzing statistical patterns solely from observational data when the causal graph is not known, aiming to identify cause-effect pairs. This process of deducing the underlying causal structure from data is referred to as causal discovery (Spirtes et al., 2000; Peters et al., 2017; Glymour et al., 2019; Zanga et al., 2022). For example, "Is there a causal relationship between review frequency and exam scores?"

Rung 1: Association. This rung is dedicated to exploring statistical dependencies among variables. These dependencies can be effectively modeled using Bayesian Networks (Pearl, 1988; Goertzel et al., 2008), which depict a set of variables and their conditional relationships, denoted as  $P(Y = y | X = x)$ , through a directed acyclic graph (DAG). At this rung, the questions asked are primarily of the form "What is?" For instance, "What is the appropriate review frequency for me to effectively preparing for exams?" Queries on this rung can be answered based on observational data.

Rung 2: Intervention. The second rung moves beyond mere observation to the effects of interventions. It allows ones to take actions or intervene on variables in environments, and then predict the effects of those deliberate interventions. This is about asking "What if I do this?" For example, "What if I review every day, will my exam scores improve?" Different from seeing or observing on Rung 1, actively intervening on variables remove the effect of any other potential factors on those variables, which ensures that the true causal effects are estimated. We represent interventions using the do-operator in the form of  $P(Y = y|do(X = x))$ , representing the distribution of  $Y$  when intervening on  $X$  to fix its value at  $x$ .

Rung 3: Counterfactuals. The highest rung involves considering counterfactuals - questions of the type "What if I have done this instead?" For instance, "What if I have attended a party instead of reviewing, would my exam scores be good?" This involves reasoning about hypothetical alternative scenarios in which the world might have unfolded differently. Counterfactual probabilities are expressed as  $P(Y_{x} = y)$ , signifying the likelihood that "Y would be  $y$  if  $X$  had been  $x$ ." Note that, counterfactual reasoning requires the use of structural causal models (SCMs) (Pearl, 2009), which are essential for understanding and analyzing how variables interact within a system under hypothetical scenarios.

# 2.2 Structural Causal Models

Causal models are constructed based on deterministic, functional relationships among variables of interest, with each relationship representing an autonomous mechanism. In this section, we give a formal definition of causal models (Pearl, 2009).

Definition (Structural Causal Models): A structural causal model (SCM), denoted by  $\mathcal{M}$ , is a triple

$$
\mathcal {M} = \langle U, V, F, P (u) \rangle , \tag {1}
$$

where:

(i)  $U$  is a set of background variables, (also called exogenous), that are determined by factors outside the model;

(ii)  $V$  is a set  $\{V_1, V_2, \ldots, V_n\}$  of variables, called endogenous, that are determined by variables in the model (i.e., variables in  $U \cup V$ );

(iii)  $F$  is a set of functions  $\{f_1, f_2, \ldots, f_n\}$  such that each  $f_i$  is a mapping from the respective domains of  $U_i \cup \mathbf{PA}_i$  to  $V_i$ , where  $U_i \subseteq U$  and  $\mathbf{PA}_i \subseteq V \setminus V_i$  and the entire set  $F$  forms a mapping from  $U$  to  $V$ . In other words, each  $f_i$  in

$$
v _ {i} = f _ {i} (p a _ {i}, u _ {i}), \quad i = 1, \dots , n,
$$

assigns a value to  $V_{i}$  that depends on the values of a select set of variables in  $V \cup U$ , and the entire set  $F$  has a unique solution  $V(u)$ ;

(iv)  $P(u)$  is a probability distribution over exogenous variables.

Each structural causal model  $M$  is associated with a DAG  $\mathcal{G}$ , where each vertex corresponds to a variable and the directed edges pointing from  $U_i \cup \mathbf{PA}_i$  to  $V_i$  represent functional relationships in which  $U_i \cup \mathbf{PA}_i$  appears in the argument of the function of  $V_i$ .

# 3 Causal Targets

As introduced in The CaLM Framework (Section 1.1), a causal target is defined as a triplet consisting of (causal task, mode, language), where a causal task is also structured as a triplet: (causal ladder, causal scenario, domain). Each component of these triplets will be thoroughly dissected in this section. We begin by outlining their broad classifications in Taxonomy (Section 3.1), followed by a discussion of the specific elements chosen for evaluation in Concrete Implementation (Section 3.2). Finally, we delve into each causal scenario based on the hierarchical levels of the causal ladder (i.e., Rung 0: Causal Discovery (Section 3.3), Rung 1: Association (Section 3.4), Rung 2: Intervention (Section 3.5), and Rung 3: Counterfactuals (Section 3.5)).

# 3.1 Taxonomy

In this section, we define the design space for Causal Task, Mode and Language on a macro level. We aim to establish a comprehensive space for the causal target that can be further refined and filled through future research endeavors.

# 3.1.1 Causal Task

A causal task specifies the particular function of causal reasoning that a language model is expected to perform, structured as a triplet: (causal ladder, causal scenario, domain). The relationships among these three elements are illustrated in Figure 1.2.

Causal ladder. The causal ladder, a crucial dimension in our taxonomy, consists of four rungs: causal discovery, association, intervention, and counterfactuals. The four rungs of causal ladder cover a spectrum of challenges relevant to causal reasoning.

Causal scenario. A causal scenario illustrates how causal concepts can be applied in real-world or research settings, such as natural direct effect (NDE), controlled direct effect (CDE), and probability of necessity (PN). Each scenario is uniquely associated with one of the four levels of the causal ladder. This correspondence streamlines the evaluation process and facilitates a more nuanced understanding of language models' performance in causal reasoning.

Domain. The domain refers to the dataset and question type in our context. Our datasets are classified into two categories: open-source and self-constructed. Open-source domains utilize existing datasets that align with our predefined causal tasks, thereby enhancing the broad applicability of our research and facilitating comparisons with prior studies. In contrast, self-constructed domains are created for causal tasks that either have limited existing data points or lack publicly available datasets. This dual approach ensures comprehensive domain coverage for our evaluations. Additionally, we design four question types, which are binary classification, choice selection, open-ended generation, and probability calculation. This flexibility allows us to extensively explore and evaluate the effectiveness of language models across various causal tasks, contributing significantly to our understanding of model performance under various experimental settings.

# 3.1.2 Mode

In the realm of AI systems, the integration of various data types has led to the identification of four common modes: Text, Code, Image, and Video, each of which is characterized by its unique features and supports a wide

range of causal tasks (Lu et al., 2024). These modes, each serving a unique purpose, contribute significantly to the holistic understanding and processing of diverse information, enhancing the functionality and applicability of AI across different contexts.

Text mode. Text mode focuses on causal tasks related to natural language processing, where the input and output are primarily composed of textual information. This mode involves understanding, generating, and manipulating text, making it essential for applications such as language translation (Zhu et al., 2023b), sentiment analysis (Chen & Qian, 2020), and information extraction (Chen et al., 2022b).

Code mode. Code mode is specifically designed for handling programming languages and source code. It involves causal tasks related to code generation (Ji et al., 2023), comprehension (Gao et al., 2023b), and analysis (Rodriguez-Cardenas et al., 2023). This mode is crucial for applications in automated coding (Kazemitabaar et al., 2023), debugging (Lee et al., 2023b), and software comprehension (Yuan et al., 2023a), allowing AI systems to engage with and interpret programming instructions effectively.

Image mode. Image mode focuses on causal tasks involving static visual data. This includes causal tasks such as visual recognition (Mao et al., 2022), image classification (Yang et al., 2023a), and image generation (Li et al., 2024). The AI system processes pixel-based information to understand visual content, making it instrumental in applications such as medical imaging analysis (Taher et al., 2022) and image synthesis (Rombach et al., 2022).

Video mode. Video mode extends the capabilities of AI systems to dynamic visual data. It involves causal tasks related to video understanding (Huang et al., 2023), action recognition (Liu et al., 2024b), and temporal analysis (Chen et al., 2021a). Video mode enables AI systems to interpret and respond to sequences of frames, contributing to applications like video summarization and content understanding (Zhang et al., 2016; Bertasius et al., 2021).

Understanding and effectively utilizing these four modes - Text, Code, Image, and Video - in AI systems provide a comprehensive approach to handling diverse types of data. This taxonomy lays the foundation for developing versatile AI models capable of addressing a wide range of causal tasks in a complex context.

# 3.1.3 Language

The global population, consisting of billions of people, communicates through a multitude of languages (Nordhoff & Hammarström, 2011; Hammarström et al., 2021; Bommasani et al., 2021; Liang et al., 2022). Despite this linguistic diversity, in the field of artificial intelligence and natural language processing, the majority of efforts are concentrated on a handful of linguistically resource-rich languages, such as English and Chinese. Acknowledging this linguistic imbalance, we refrain from extensively categorizing the world's languages. Instead, our primary focus lies in evaluating models and causal tasks in English and Chinese.

# 3.2 Concrete Implementation

Building upon Taxonomy (Section 3.1), this section elaborates on the specific component we select to assess the model's causal reasoning capability (i.e., Causal Task (Section 3.2.1), Mode (Section 3.2.1) and Language (Section 3.2.3)). We carefully select these components based on their applicability and importance, ensuring that they reveal the model's core strengths and limitations.

# 3.2.1 Causal Task

Concerning the scope of CaLM, our ideal goal is to evaluate language models across every causal task, represented by the tuple: (causal ladder, causal scenario, domain). However, as our taxonomy indicates, the realms of causal scenario and domain are both extensive and diverse. Therefore, our objective is not to cover every conceivable causal task, but rather to concentrate on assessing the most critical aspects.

Causal ladder. Our causal tasks cover all four rungs of the causal ladder: causal discovery, association, intervention, and counterfactuals. By considering the entire causal ladder, we can thoroughly evaluate the model's causal reasoning capabilities from the most foundational to the most complex levels, offering a comprehensive understanding of its performance across different types of causal analyses.

Causal scenario. In selecting causal scenarios, we have the following considerations. Since our exclusive focus on language models, we eliminate any causal scenarios that involve multiple modalities. We prioritize the most fundamental and essential causal scenarios across each rung of the causal ladder. We believe these scenarios are crucial for assessing and enhancing the causal inference capabilities of language models, with significant potential societal impact. This targeted approach leads to the selection of the following causal scenarios (Figure 1.2):

- Causal discovery: pairwise causal discovery (PCD), event causality identification (ECI), abstract reasoning (AR), and causal attribution (CA). PCD has already attracted a considerable number of researchers to evaluate models (Gao et al., 2023a; Kiciman et al., 2023; Vashishtha et al., 2023; Long et al., 2022; Tu et al., 2023), with some studies focusing on ECI (Gao et al., 2023a) and AR (Zečević et al., 2023; Willig et al., 2022). Although there has not yet been an evaluation for CA, this should not be interpreted as diminishing the importance of CA. In fact, it highlights the model's capacity for attributing causes to events, a capability that is critically applied in areas like social psychology (Malle, 2022; Langenhoff et al., 2021), marketing (Mero et al., 2020; Tang & Tsang, 2020), and epidemiology (Richens et al., 2020; Shimonovich et al., 2021).

- Association: correlation (CORR) and explaining away effect (EAE). The two causal tasks on this rung are proposed by Jin et al. (2023a) and have been evaluated on some models (e.g., LLaMa, Alpaca, GPT-4). Building on this, we conduct a comprehensive evaluation of all models on these two scenarios in CaLM.

- Intervention: average treatment effect (ATE), backdoor adjustment set (BAS), frontdoor adjustment set (FAS), instrumental variable (IV), causal effect identification (CEI), controlled direct effect (CDE), and collider bias (CB). In Jin et al. (2023a), ATE, BAS, CB and CDE have already been evaluated in Natural mode. Building on this, we extend the evaluations by adding Mathematical mode for ATE and CDE, and introducing Symbolic mode for BAS. Currently, there are no studies evaluating models on FAS, IV, and CEI. Front-door adjustment aims to identify FAS and estimate the causal effects when unobserved confounders exit. Effectively handling FAS is significant in areas such as computer vision (Yang et al., 2021b,c), economics (Imbens, 2020), and social policy (Matthay & Glymour, 2022). IV is dependent of the treatment and influences the outcome only through the treatment. IV can be used to estimate causal effects (Angrist et al., 1996), and it is applied in various domains, including psychology (Maydeu-Olivares et al., 2020), policy analysis (Marbach & Hangartner, 2020), and biology (Birney, 2021). While all causal effects are identifiable in the absence of unobserved confounders, the real world often features such confounders, complicating the causal scenarios. The CEI assesses a model's ability to determine whether a causal effect can be uniquely established from the distribution of observed variables, regardless of any

unobserved factors (Tian & Pearl, 2002). This capability is particularly useful in tackling challenges in fields such as environmental epidemiology (Yu et al., 2021), economics (Uysal, 2015), and meteorology (Pfleiderer et al., 2020).

- Counterfactuals: actual causality (AC), causal explanation generation (CEG), effect of the treatment on the treated (ETT), natural direct effect (NDE), natural indirect effect (NIE), probability of necessity (PN), probability of sufficiency (PS), and counterfactual reasoning (CR). Among these scenarios, AC, CEG, ETT, NDE, NIE, and CR have already been evaluated on some models in previous studies (Suzgun et al., 2023; Frohberg & Binder, 2022; Kiciman et al., 2023; Gao et al., 2023a; Jin et al., 2023a; Kiciman et al., 2023). For AC, CEG, and CR, we continue to use the datasets employed in existing work. For ETT, NDE, and NIE, we additionally introduce evaluations in Mathematical mode. PN and PS are two important concepts in causal reasoning that have not yet been evaluated. PN refers to the probability that an outcome would not have happened without its cause, given the outcome has already happened. PS is the chance of an outcome would have happened if its cause happened, with the outcome has not happened yet. These concepts are pivotal in guiding domains from social science (Kuppens et al., 2003) to computer science (Yang et al., 2024).

Domain. In the selection of domains, we primarily focus on two key areas: question types and datasets. (1) Regarding question types, we choose four kinds that are broadly used and emphasize different aspects of reasoning. These include: Binary classification, which requires the model to provide a deterministic "yes" or "no" response, testing its ability to make clear-cut decisions; Choice selection, which asks the model to select the correct answer from a set of given options that can range from 2 to 4 choices, assessing its selection accuracy; Probability calculation, which involves the model calculating and presenting an answer in numerical form based on probabilities, testing tis quantitative reasoning; Open-ended generation, which challenges the model's ability to generate relevant explanations without any constraints on format, evaluating its creative and comprehensive response capabilities. (2) Considering the datasets, despite the scarcity of causal reasoning datasets, we have endeavored to comprehensively cover all causal scenarios we aim to assess. This has been achieved by both utilizing existing datasets and creating our own datasets. For the selection of open-source datasets, we primarily refer to the existing evaluations mentioned in the causal scenario, aligning with the datasets utilized by prior studies. This approach offers two key benefits: first, it ensures that the chosen datasets appeal to the broadest audience possible; second, it enhances the reliability of the CaLM findings by allowing comparisons with results from datasets used in existing research. For self-constructed datasets, particularly for causal tasks with existing datasets that have fewer than 1000 data points (such as NDE, NIE) and those lacking public datasets, we construct our own. We will detail the process used to select and construct specific datasets for each causal scenario in Data Collection (Section 4).

# 3.2.2 Mode

Given that CaLM is designed for language models, our selection of modes carefully considers three distinct subcategories within the text mode: Natural, Symbolic, and Mathematical. Natural includes the conventional causal tasks that are articulated and responded to in the language commonly used by people. This mode focuses on the intuitive, everyday use of language, facilitating the assessment of how effectively language models understand and generate responses that align with typical human communication. Symbolic refers to the causal tasks presented in a Symbolic form that does not contain specific physical meaning (e.g., a causal graph represented within Symbolic mode would be “A causes B, B causes D, C causes D”). The model’s responses are given in a mixed format of natural language and Symbolic representation. Using symbols to represent variables

serves a dual purpose: (1) Firstly, it aligns with traditional cognitive reasoning (Garcez et al., 2008), where abstract symbols and logical structures enable reasoning beyond specific contexts. This approach leverages the generality and clarity of Symbolic representations, facilitating logical inference and conceptual manipulation without the ambiguities of natural language. (2) Secondly, this Symbolic representation effectively prevents the model from memorizing biases within the training data, offering a more accurate measure of the model's genuine causal inference capabilities. By abstracting variables into symbols, the focus shifts from content memorization to the application of logical reasoning, providing a clearer evaluation of the model's ability to deduce causality from causal graph. The usage of Symbolic mode not only assesses the model's reasoning skills in a controlled environment but also paves the way for the development of models that are both more robust and capable of generalizing beyond their training datasets. Mathematical consists of causal tasks that involve math concepts, requiring the model to execute mathematical operations and respond with answers in both probabilistic values and natural language. Numerous studies have evaluated the mathematical abilities of language models, revealing that although these models excel in many natural language processing tasks, they still face significant challenges when solving mathematical problems (Hendrycks et al., 2021; Cobbe et al., 2021; Lightman et al., 2023; Bubeck et al., 2023; Dao & Le, 2023; Wei et al., 2023a; Wu et al., 2023a; Yuan et al., 2023b; Yu et al., 2023). The reason we employ Mathematical mode is that mathematical reasoning is fundamental to assessing the cognitive capabilities that underpin human intelligence. This mode tests models beyond mere linguistic fluency, probing their logical structure and capacity for conceptual understanding. Employing Mathematical mode not only highlights the current capabilities and limitations of language models in mimicking sophisticated cognitive functions, but also guides the development of more advanced models capable of complex thought processes akin to human reasoning.

# 3.2.3 Language

Despite the global proliferation of language models, there is a pressing need to expand evaluation across a broader array of languages. However, due to the associated costs and the risk of evaluation sets becoming unwieldy in size, we have decided to concentrate our efforts on two languages: English and Chinese. The selection of these two languages is primarily based on two considerations: (1) As explained in Liang et al. (2022), English and Chinese are the languages most frequently used in the fields of artificial intelligence and natural language processing; (2) As we have statistically analyzed in Models (Section 8), the training corpora for current models are also predominantly composed of these two languages.

# 3.3 Rung 0: Causal Discovery

In the field of causal discovery (Rung 0), our evaluation concentrates on four causal scenarios: Pairwise Causal Discovery (PCD) (Section 3.3.1), Event Causality Identification (ECI) (Section 3.3.2), Abstract Reasoning (AR) (Section 3.3.3), and Causal Attribution (CA) (Section 3.3.4). We will now delve into a detailed explanation of each causal scenario.

# 3.3.1 Pairwise Causal Discovery (PCD)

Causal discovery focuses on understanding the cause-and-effect relationships among different variables (Peters et al., 2017). In many scientific disciplines, the primary goal is to uncover causal relationships and elucidate fundamental mechanisms. While randomized experiment is widely regarded as the gold standard for establishing causal relationship (Hariton & Locascio, 2018), it can prove challenging or unfeasible in certain contexts (Spirtes & Zhang, 2016). Pairwise causal discovery, which aims to discern underlying pairwise causal

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5a407456e2119adb7e707c9c5b299e94629ef5ead85468b9e81afab39637303e.jpg)



Figure 3.1 Example of pairwise causal discovery.


relationships solely from observational data, has attracted increasing attention across various domains, such as earth science (Melkas et al., 2021), climate system (Runge et al., 2019) and biology (Amar et al., 2021). Unlike traditional causal discovery methods that rely on the actual data values of these variables, language models can deduce this causal framework by analyzing metadata related to the variables. This can include the variable's name or the context in which the problem is described using natural language (Kiciman et al., 2023; Willig et al., 2022).

Causal scenario setting. PCD seeks to establish if a causal relationship exists between two given events and to identify which of the two is the cause and which is the effect (Gao et al., 2023a). In PCD, our questions primarily manifest in two ways. (1) Binary classification: We present pairs of events along with associated inquiries (e.g., "Event A: Lava flowed from the volcano. Event B: The volcano was dormant. Question: Is there a causal relationship between Event A and Event B?"²). The objective is to accurately discern whether a causal relationship exists between the two events (the correct response being "No"). (2) Choice selection: Models must select the cause or effect of a given event from two provided options (e.g., "Input Event: Lava flowed from the volcano. Question: Please select the cause of the input event from the following options. Option 1: The volcano erupted. Option 2: The volcano was dormant."³). Here, the causal scenario explicitly outlines the presence and direction of the causal relationship, challenging the model to determine which option is more probable (in this example, "Option 1" is correct). See Figure 3.1 for a detailed illustration.

# 3.3.2 Event Causality Identification (ECI)

This causal scenario is designed to pinpoint the events mentioned in a text and understand whether there exists a casual relationship between them. Research on ECI has a long-standing history and it holds a vital position in comprehending text deeply (Gao et al., 2019). Thus, enhancing the comprehension of event causality can significantly benefit various applications in natural language processing (Liakhovets & Schlarb, 2022; Liu et al., 2023b). Language models tasked with this scenario should be adept at utilizing a broad range of commonsense knowledge and capable of comprehending complex contexts involving multiple entities and events. Ultimately, these models are expected to synthesize all this information to accurately determine causal

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/7229016812b6bbeadcbe98a3155159f479442dcda51bb11d309b7f599d6fdf1f.jpg)



Figure 3.2 Example of event causality identification.


relationships (Gao et al., 2023a).

Causal scenario setting. ECI requires the models to assess whether there is a causal relationship between two events within a given sentence. For instance, consider the sentence: "State security services also claimed that it had arrested a general who was involved in the coup attempt." An example task would involve examining the events "involved" and "arrested" to determine if one caused the other. In this case, the correct answer is "No", as humans can easily discern these as two separate events without a direct cause-and-effect relationship between them. See Figure 3.2 for a detailed illustration.

# 3.3.3 Abstract Reasoning (AR)

AR investigates the capability of language models to identify and understand causal relationships within Symbolic causal graphs (Zečević et al., 2023). This scenario tests how well models can accurately discern potential causal relationships beyond simply memorizing information based on position or sequence. In scenarios where models only memorize such inseparable information, it becomes challenging to integrate these disparate pieces of data into a coherent and consistent causal graph (Willig et al., 2022). With strong AR capabilities, language models can better predict outcomes, design interventions, and understand the potential implications of changes within the system, thus enhancing decision-making and problem-solving abilities.

Causal scenario setting. In AR, models are tasked with determining whether there exists a causal relationship between two nodes in a given graph. For example, consider a graph where "A causes B, B causes C, B causes D, and D causes E." The models must assess whether there is a direct causal link between nodes "C" and "D". In this case, the correct answer is "No". See Figure 3.3 for a detailed illustration.

# 3.3.4 Causal Attribution (CA)

Causal attribution refers to the process of determining which specific factor is responsible for an outcome. Its significance spans across numerous domains, intersecting with research in psychology (Graham, 2020), medical diagnosis (Richens et al., 2020), and organizational science (Harvey et al., 2014). In this causal scenario, the model needs to accurately recognize causal graphs and uncover the precise causal relationships within them. Assessing the model's capacity for causal attribution aids in comprehending its decision-making abilities, thus establishing a foundation for its practical deployment in real-world contexts.

# Scenario: AR

# Prompt:

Input Event: If A causes B, B causes C, B causes D, and D causes E.

Question: Does C cause D?

Answer (Yes or No?):

Ground truth: No

Figure 3.3 Example of abstract reasoning.

# Scenario: CA

# Prompt:

You will be presented with a causal graph in the following form: A causes B, B

causes D, B causes C, and B causes E.

Question: Does D serve as the parent node of E?

Answer (Yes or No?):

Ground truth: No

Figure 3.4 Example of causal attribution.

Causal scenario setting. In CA, models are provided with a causal graph (e.g., "A causes B, B causes D, B causes C, and B causes E") and face two domains: (1) Find parent: This task requires the model to determine the parent of a specified node, focusing on identifying direct causal relationships. For instance, the question might ask, "Does D serve as the parent node of E?" In this case, the correct answer is "No". (2) Find ancestor: This task involves identifying the ancestor of a given node, which assesses indirect causal relationships. An example question could be, "Does A serve as the ancestor node of E?" Here, the correct answer is "Yes". See Figure 3.4 for a detailed illustration.

# 3.4 Rung 1: Association

For association (Rung 1), we mainly focus on two causal scenarios: Correlation (CORR) and Explaining Away Effect (EAE). We will provide a detailed description for both of them.

# 3.4.1 Correlation (CORR)

Correlation indicates a statistical association between two variables, irrespective of causality. Although "correlation does not imply causation", identifying a statistical link between variables is a necessary step in the causal inference. It helps further investigation into whether the relationship is indeed causal, guiding researchers in developing hypotheses (Rolfe et al., 2020), designing experiments (Duncan & Magnuson, 2012), and employing statistical methods to explore the nature and direction of the supposed causal relationship (Rosato et al., 2018).

# Scenario: CORR

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Husband has a direct effect on wife and alarm clock. Wife has a direct effect on alarm clock.

The overall probability of alarm set by husband is  $74\%$ . The probability of alarm not set by husband and ringing alarm is  $9\%$ . The probability of alarm set by husband and ringing alarm is  $51\%$ .

Question: Is the chance of ringing alarm smaller when observing alarm set by husband?

Answer (Yes or No?):

Ground truth: No

Figure 3.5 Example of correlation.

Causal scenario setting. In CORR, we provide a causal graph (e.g., "Husband has a direct effect on wife and alarm clock. Wife has a direct effect on alarm clock.") along with corresponding probabilities (e.g., "The overall probability of alarm set by husband is  $74\%$ . The probability of alarm not set by husband and ringing alarm is  $9\%$ . The probability of alarm set by husband and ringing alarm is  $51\%$ .")<sup>5</sup>. The model needs to answer the question about the correlation between the given variables (e.g., "Is the chance of ringing alarm smaller when observing alarm set by husband?"). See Figure 3.5 for a detailed illustration.

# 3.4.2 Explaining Away Effect (EAE)

EAE describes a causal relationship where two independent causes that produce a common effect become interdependent when that effect is observed (Pearl, 2009). This interdependence arises because having information about one factor alters the probability of the other factor being involved, once it is established that the shared effect has taken place (Kim & Pearl, 1983; Pearl, 2009). This pattern is also known as selection bias or Berkson's paradox in statistics (Berkson, 1946). For example, consider a prestigious art school that requires applicants to excel in either painting or sculpture. In the general population, skill in painting and skill in sculpture might not be correlated. However, within the art school's student, there might be a negative correlation between these two skills. This is because students who are not as skilled in painting are likely those admitted due to their exceptional talent in sculpture, and vice versa. This phenomenon illustrates the explaining away effect: the school's admission criteria create an apparent negative correlation between two skills that are unrelated in the broader population, as each skill "explains away" the need for the other in the context of admission. The EAE is crucial in various fields, including psychology (Wilson & Gilbert, 2008), artificial intelligence (Kenny et al., 2021), and data analysis (Linden et al., 2020). It provides insight into how conditional dependencies between variables can lead to misleading correlations. Understanding EAE helps in accurately interpreting data, making informed decisions, and avoiding false conclusions.

Causal scenario setting. In EAE, we provide a causal graph (e.g., "Appearance has a direct effect on fame. Talent has a direct effect on fame.") along with corresponding conditional probabilities (e.g., "The overall probability of attractive appearance is  $48\%$ . For people considered unattractive and are not famous, the probability of talent is  $3\%$ . For people considered unattractive and are famous, the probability of talent is  $9\%$ . For people considered attractive and are not famous, the probability of talent is  $2\%$ . For people considered attractive and are famous, the

# Scenario:EAE

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Appearance has a direct effect on fame. Talent has a direct effect on fame.

The overall probability of attractive appearance is  $48\%$ . For people considered unattractive and are not famous, the probability of talent is  $3\%$ . For people considered unattractive and are famous, the probability of talent is  $9\%$ . For people considered attractive and are not famous, the probability of talent is  $2\%$ . For people considered attractive and are famous, the probability of talent is  $6\%$ .

Question: If we look at people who are famous, does the chance of talent increase when attractive appearance?

Answer (Yes or No?):

Ground truth: No

Figure 3.6 Example of explaining away effect.

probability of talent is  $6\%$ . The model needs to answer the question about the given variables (e.g., "If we look at people who are famous, does the chance of talent increase when attractive appearance?"). See Figure 3.6 for a detailed illustration.

# 3.5 Rung 2: Intervention

In contemplating intervention (Rung 2), we carefully design seven different causal scenarios. These causal scenarios cover all three modes, providing a thorough evaluation of the model's causal reasoning abilities. Specifically, for causal scenarios that involve both Natural and Mathematical modes, our evaluation focuses on Average Treatment Effect (ATE) (Section 3.5.1) and Controlled Direct Effect (CDE) (Section 3.5.7). In scenarios restricted to the Natural mode, we assess Collider Bias (CB) (Section 3.5.5). And for scenarios exclusive to the Symbolic mode, we examine Backdoor Adjustment Set (BAS) (Section 3.5.2), Frontdoor Adjustment Set (FAS) (Section 3.5.3), Instrumental Variable (IV) (Section 3.5.4), and Causal Effect Identification (CEI) (Section 3.5.6).

# 3.5.1 Average Treatment Effect (ATE)

ATE is a fundamental concept in causal inference that helps to quantify the impact of a particular intervention.  $X$  causes  $Y$  if and only if changing  $X$  leads to a change in  $Y$ , keeping everything else constant. Denoting the treatment group by  $do(X = 1)$  and the control group by  $do(X = 0)$ , the difference between them,  $P(Y = 1|do(X = 1)) - P(Y = 1|do(X = 0))$ , is called the ATE (Pearl et al., 2016). Consider a causal scenario where all subjects are unemployed individuals, with some receiving a policy intervention (the treatment group) and others not (the control group). We are interested in determining the causal impact of a job search monitoring policy on the duration of unemployment. Essentially, we want to know, on average, how much shorter one's unemployment period would be if they underwent the intervention. The ATE in this case measures the difference in expected durations of unemployment between the treatment and control groups. A negative ATE would indicate that the job policy extended the length of unemployment, while a positive ATE would suggest a reduction in unemployment duration. Conversely, an ATE estimate of zero would mean that the treatment had no discernible effect on the length of unemployment. By providing a quantitative measure of a treatment's impact on an average, ATE helps in understanding the generalizability of interventions. Moreover, ATE assists in improving policy design and informing stakeholders about the

# Scenario:ATE

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: The amount of exercise a person does per week has a direct effect on the person's physical fitness level. The amount of exercise a person does per week has a direct effect on the person's risk of developing chronic diseases.

For those with the amount of exercise a person does per week being little, the probability of the person's physical fitness level being excellent is 0.2598. For those with the amount of exercise a person does per week being a lot, the probability of the person's physical fitness level being excellent is 0.5314.

Instruction: Consider the average treatment effect (ATE) of the amount of exercise a person does per week on the person's physical fitness level.

Question: If the amount of exercise a person does per week is changed to be little, will the person's physical fitness level be more likely to be excellent?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "No", "PROB": "-0.2716"}

Figure 3.7 Example of average treatment effect.

potential benefits or drawbacks of specific actions. Research ranging from economics (Abadie & Imbens, 2011; Hirano et al., 2003) to public health (Feng et al., 2012) proves the significance of ATE.

Causal scenario setting. In ATE, we provide a causal graph (e.g., "The amount of exercise a person does per week has a direct effect on the person's physical fitness level. The amount of exercise a person does per week has a direct effect on the person's risk of developing chronic diseases.") along with corresponding conditional probabilities (e.g., "For those with the amount of exercise a person does per week being little, the probability of the person's physical fitness level being excellent is 0.2598. For those with the amount of exercise a person does per week being a lot, the probability of the person's physical fitness level being excellent is 0.5314"). The causal scenario requires determining the ATE between specified variables (e.g., "If the amount of exercise a person does per week is changed to be little, will the person's physical fitness level be more likely to be excellent?"). The model needs to address two different types of questions: (1) Binary classification: This involves providing a direct answer of "Yes" or "No" (the correct answer for this example is "No"); (2) Probability calculation: The model needs to utilize the probabilities provided in the question to calculate the accurate response, preserving precision to four decimal places (the correct answer for this example is "-0.2716"). See Figure 3.7 for a detailed illustration.

# 3.5.2 Backdoor Adjustment Set (BAS)

When assessing the impact of treatment  $X$  on outcome  $Y$ , we are confronted with the decision to adjust our calculations to account for potential variations in confounders  $Z$ . This adjustment is typically implemented by using the Back-door criterion (Pearl, 1995). A backdoor adjustment set is such a set of variables  $Z$  that, when controlled for, blocks all backdoor paths from the treatment to the outcome. A backdoor path is a path that leads from the treatment to the outcome through an arrow pointing to the treatment, which can

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/09fb76fc124f21a8ade4e634993f2e44f5ac811e66d943adcac2aebe253beb18.jpg)



(a) BAS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/e81dc46368ea3f326372c88df3561d13141e71440f995588d11f987b84b0eed7.jpg)



(b) FAS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/df0fdb4ec84d2757fd716f4bbd0493e0396820d2db892b653c70ca8ac2594efd.jpg)



(c) IV



Figure 3.8 Real-world examples of BAS, FAS and IV.  $X$  represents the treatment,  $Y$  represents the outcome,  $Z$  represents the confounder,  $M$  represents the mediator, and  $I$  represents the instrumental variable. If the confounder is unobserved, its effect on the treatment and outcome is represented by a dashed line.


introduce confounding bias if not properly adjusted for (Pearl, 2009). By adjusting for the variables in a backdoor adjustment set, one aims to eliminate confounding bias, allowing for an unbiased estimation of the causal effect of the treatment on the outcome (Pearl, 1995). In a real-word causal scenario as Figure 3.8(a) shows, suppose we are interested in the effect of exercise (treatment) on weight (outcome). A backdoor path might be through a variable like diet, where diet affects both exercise and weight. If we do not control for diet, we might incorrectly attribute the effect of diet on weight to exercise. Therefore, diet could be part of a backdoor adjustment set that, when controlled for, allows for an unbiased estimation of the causal effect of exercise on weight. The BAS has important real-world applications across various fields such as healthcare (Adib et al., 2020), artificial intelligence (Landeiro & Culotta, 2016; Correa et al., 2018; Landeiro & Culotta, 2018; Dai & Han, 2023), and social sciences (Elwert, 2013), where understanding causal relationships is crucial for informed decision-making and policy development.

Causal scenario setting. We design two types of questions in BAS. (1) Binary classification: We provide the model with a causal graph (e.g., "Husband has a direct effect on wife and alarm clock. Wife has a direct effect on alarm clock.") and two different methods (e.g., "Method 1: We look at how husband correlates with alarm clock case by case according to wife. Method 2: We look directly at how husband correlates with alarm clock in general."8). And the model is required to decide which method is more correct. (2) Choice selection: The question starts with presenting a causal graph in Symbolic form (e.g., "A causes B, A causes E, A causes C, B causes C, B causes D, B causes E, and D causes E.). The model needs to apply the Back-door criterion to determine the backdoor variables between an ordered pair of variables (e.g., "D" and "E"). There are three different categories of backdoor variables that need to be assessed: the maximal, the minimal, and a combination of both. Each category plays a specific role in controlling for confounding in causal analysis. See Figure 3.9 for a detailed illustration.

# 3.5.3 Frontdoor Adjustment Set (FAS)

While the Back-door criterion aims to control for variables that impact both the treatment and the outcome, the Front-door criterion provides a way to estimate the causal effect by exploiting the mediation pathway, even in the presence of unobserved confounding between the treatment and outcome (Pearl, 1995). A FAS involves a set of variables that mediate the causal path from the treatment to the outcome. Consider a study on the effect of education (treatment) on employment (outcome) in Figure 3.8(b). Suppose the skill (mediator) is the way through which education affects employment. The Front-door Criterion would involve first estimating the

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/76f379a51b2c590be9502473fc49923d4d738c3c6f697c51a566e69334208a8c.jpg)



Figure 3.9 Example of backdoor adjustment set.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5357b3e509e8944cf59993b685cbd80e650243309f67134012d47796da651229.jpg)



Figure 3.10 Example of frontdoor adjustment set.


effect of education on the skill, and then estimating the effect of the skill on employment while controlling for the education. Even if there are unmeasured factors that affect both the decision to participate in education and employment, the frontdoor adjustment allows for an estimation of the causal effect of education on employment through the mediator of skill. The practical real-world significance of the FAS extends across various domains, offering substantial benefits in artificial intelligence (Xu et al., 2023b; Xu & Gretton, 2022; Xia et al., 2024), earth and environmental sciences (Runge et al., 2023), and ecology (Arif & MacNeil, 2023).

Causal scenario setting. Similar to BAS, the question in FAS provides the model with a causal graph and requires it to utilize the Front-door criterion to determine the frontdoor variables between an ordered pair of variables (e.g., "A" and "D"). See Figure 3.10 for a detailed illustration.

# 3.5.4 Instrumental Variable (IV)

Relative to a pair  $(X,Y)$ , an instrumental  $Z$  must satisfy two conditions: (1) it is independent from any variables that impact  $Y$  not through  $X$  (including error terms), and (2) it is dependent on  $X$  (Pearl, 2009). In

# Scenario: IV

# Prompt:

You will be presented with a causal graph in the following form: A causes B, A causes E, B causes E, B causes D, C causes E, and C causes D.

Question: Which set of variables is the instrument variables relative to an ordered pair of variables (B, D) in the above causal graph?

Option 1: A

Option 2: B

Option 3: D

Answer (Option 1 or Option 2 or Option 3?):

Ground truth: Option 1

Figure 3.11 Example of instrumental variable.

other words, an instrumental variable influences the treatment but has no direct effect on the outcome, except through the treatment. This characteristic makes it possible to estimate the causal effect of the treatment on the outcome, even in the presence of unobserved confounders that might otherwise bias the estimates. Consider a study aiming to estimate the effect of education (treatment) on income (outcome), as the Figure 3.8(c) demonstrates. However, an individual's decision to pursue more education might be influenced by unobserved factors like capability or family background, which also affect income. An instrumental variable could be the college proximity, under the assumption that it affects an individual's decision to obtain more education but does not directly affect their income, except through education. By using this instrumental variable, researchers can estimate the causal effect of education on income, controlling for unobserved confounding factors. In summary, IV allows for more reliable and accurate estimation of causal effects, making it an essential tool in fields where controlled experiments are impractical or impossible, and thus, significantly enhances the validity of empirical findings in social sciences (Bollen, 2012), human resource management (Saridakis et al., 2020), and economics (Mogstad et al., 2021).

Causal scenario setting. Similar to BAS and FAS setups, given a causal graph, the model needs to determine the instrumental variable between an ordered pair of variables (e.g., “ $B$ ” and “ $D$ ”). See Figure 3.11 for a detailed illustration.

# 3.5.5 Collider Bias (CB)

CB is a type of selection bias that occurs when an analysis is conditioned upon a common effect of two or more variables. The simplest collider in a causal graph can be illustrated as  $X \rightarrow C \leftarrow Y$ , where  $C$  represents the common effect of causes  $X$  and  $Y$  (Pearl et al., 2016). Collider bias occurs when a common effect is controlled. For example,  $X$  and  $Y$  are independent, while conditions on  $Z$  will make them dependent. A famous example illustrating collider bias is the hollywood actors (talent → celebrity ← beauty) (Pearl & Mackenzie, 2018). As Figure 3.12(a) demonstrates, it is asserted that both talent and beauty affect an actor's success. However, it is important to note that while beauty and talent contribute to success in acting, they are independent of each other in the general population. This bias can lead to incorrect inferences about the relationships between variables (Cole et al., 2010; Elwert & Winship, 2014; Munafo et al., 2018). Thus, recognizing and addressing CB is crucial for ensuring the validity and reliability of study findings (Mahmoud et al., 2022; Shi et al., 2021), ultimately guiding accurate scientific understanding and informed decision-making.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a1f2ae8e665b85a65699a495aedc6c9a65eb370c47ffaedb87940c2dd8d9ed17.jpg)



(a) CB


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/e9d826fe31cc5af33116e5be638a49223e12c158b01c0e1610026e8454e21fd6.jpg)



(b) CEI


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/19e2fe4a5854cd191c0f700b59bb2158f069aa0e40083798ab136e3b74d0ad71.jpg)



(c) CDE



Figure 3.12 Real-world examples of CB, CEI and CDE.  $X$  represents the treatment,  $Y$  represents the outcome,  $C$  represents the common effect, and  $M$  represents the mediator.


# Scenario: CB

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Respiratory issues has a direct effect on hospitalization status. Broken bones has a direct effect on hospitalization status.

For hospitalized individuals, the correlation between respiratory issues and broken bones is -0.01.

Question: If we look at hospitalized individuals, does it mean that respiratory issues does not affect broken bones?

Answer (Yes or No?):

Ground truth: Yes


Figure 3.13 Example of collider bias.


Causal scenario setting. In CB, we provide a causal graph (e.g., "Respiratory issues has a direct effect on hospitalization status. Broken bones has a direct effect on hospitalization status.") along with corresponding probabilities (e.g., "For hospitalized individuals, the correlation between respiratory issues and broken bones is -0.01"). This causal scenario requires the model to exclude the interference of collider bias and answer the question correctly (e.g., "If we look at hospitalized individuals, does it mean that respiratory issues does not affect broken bones?"<sup>9</sup>). See Figure 3.13 for a detailed illustration.

# 3.5.6 Causal Effect Identification (CEI)

The concept of CEI in causal reasoning is centered on determining whether the causal effect of a treatment on an outcome can be estimated from observational data (Shpitser & Pearl, 2008). Consider two disjoint sets, denoted as  $X$  and  $Y$ , where the causal effect of  $X$  on  $Y$  is represented as  $P(y|do(x))$ . Assume that  $P(v)$  represents a probability distribution over the variable set  $V$ . The causal effect of  $X$  on  $Y$  is identifiable when the value of  $P(y|do(x))$  can be exclusively ascertained from any positive probability distribution of the observed variables within graph  $G$  (Tian & Pearl, 2002). Figure 3.12(b) shows a case to estimate the causal effect of smoking on lung cancer using observational data, doctors employ a causal diagram to control for confounders like age and genetics. They determine if this effect is identifiable—whether they can estimate the incidence of lung cancer if hypothetically a population were assigned to smoke. If identifiable, they can statistically estimate the risk of lung cancer due to smoking, providing evidence to guide public health interventions without the need for unethical randomized trials that would require participants to smoke.

# Scenario: CEI

# Prompt:

You will be presented with a causal graph in the following form: A causes D, A causes B, A causes C, A causes E, B causes C, C causes E, and C causes D.

There exist unobserved confounders between: C and D.

Question: Whether the causal effect of C on D is identified or not?

Answer (Yes or No?):

Ground truth: No

Figure 3.14 Example of causal effect identification.

Causal scenario setting. In CEI, we start by presenting a causal graph (e.g., "A causes  $D$ , A causes  $B$ , A causes  $C$ , A causes  $E$ , B causes  $C$ , C causes  $E$ , and  $C$  causes  $D$ ). We then specify the existence of unobserved confounders between designated nodes at four different rates:  $20\%$ ,  $40\%$ ,  $60\%$ , and  $80\%$ . For instance, if there are  $20\%$  unobserved confounders, the instruction will indicate "There exist unobserved confounders between:  $C$  and  $D$ ". If it increases to  $60\%$ , the instruction will state "There exist unobserved confounders between:  $A$  and  $B$ ,  $C$  and  $D$ ,  $B$  and  $C$ , and  $C$  and  $E$ ." The causal scenario requires the model to determine if the causal relationship between a pair of treatment and outcome variables (e.g., "C" and "D") can be identified (the correct answer for this example is "No"). See Figure 3.14 for a detailed illustration.

# 3.5.7 Controlled Direct Effect (CDE)

The CDE quantifies the direct influence of an intervention on an outcome while maintaining one or more mediators at a predetermined level (Pearl & Mackenzie, 2018; Cinelli et al., 2022). In this way, it disregards the indirect effects that operate through these mediators. In the setting of three variables: treatment  $X$ , outcome  $Y$ , and mediator  $M$ , the CDE on  $Y$  when altering the value of  $X$  from  $x$  to  $x'$  is formally defined as  $CDE = P(Y|do(X = x', M = m)) - P(Y|do(X = x, M = m))$  (Kaufman et al., 2005; Pearl, 2001). As Figure 3.12(c) shows, imagine we are investigating the direct effect of a novel math teaching strategy (treatment) on student exam scores (outcome), intentionally excluding its indirect effect via enhancing student confidence (mediator). By controlling for students' confidence levels, we aim to measure the direct influence of this new method compared to traditional teaching on exam outcomes. This analysis allows us to distinctly identify the immediate benefits of the teaching approach on performance, separating from its indirect benefits through confidence improvement. This clarity aids educators in precisely assessing the direct effectiveness of the new teaching method. This isolation required by CDE is particularly important in complex systems where multiple pathways and interactions can obscure the mechanisms through which an intervention works (Nguyen et al., 2021). By assessing the CDE, decision-makers can more accurately design and refine interventions, targeting the direct mechanisms that produce the desired outcome in various fields such as epidemiology (Carter et al., 2021), artificial intelligence (Tang et al., 2020), and biology (Howe et al., 2022).

Causal scenario setting. Similar to ATE, the problem in CDE gives a causal graph (e.g., "Weather conditions has a direct effect on amount of rainfall. Weather conditions has a direct effect on crop yield. Amount of rainfall has a direct effect on crop yield.") along with corresponding conditional probabilities (e.g., "For those with weather conditions being good and amount of rainfall being small, the probability of crop yield being high is 0.3510. For those with weather conditions being bad and amount of rainfall being small, the probability of crop yield being high

# Scenario:CDE

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Weather conditions has a direct effect on amount of rainfall. Weather conditions has a direct effect on crop yield. Amount of rainfall has a direct effect on crop yield.

For those with weather conditions being good and amount of rainfall being small, the probability of crop yield being high is 0.3510.

For those with weather conditions being bad and amount of rainfall being small, the probability of crop yield being high is 0.1420.

Instruction: Consider the controlled direct effect (CDE) of weather conditions on crop yield.

Question: Conditioned on amount of rainfall being small, if the weather conditions had been good, would the crop yield have been more likely to be high?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "Yes", "PROB": "0.2090"}

Figure 3.15 Example of controlled direct effect.

is 0.1420.). The causal scenario requires the model to determine the CDE between variables (e.g., "Conditioned on amount of rainfall being small, if the weather conditions had been good, would the crop yield have been more likely to be high?"). The model needs to address both binary classification ("Yes") and probability calculation ("0.2090") questions. See Figure 3.15 for a detailed illustration.

# 3.6 Rung 3: Counterfactuals

When analyzing causal scenarios at the counterfactuals (Rung 3) level, we assess eight causal scenarios across two modes. Scenarios belonging to this rung present considerable challenges to language models. In the Natural mode, our assessment focuses on Actual Causality (AC) (Section 3.6.1), Causal Explanation Generation (CEG) (Section 3.6.2), and Counterfactual Reasoning (CR) (Section 3.6.8). For scenarios involving both Natural and Mathematical modes, we evaluate the following five specific scenarios: Effect of the Treatment on the Treated (ETT) (Section 3.6.3), Natural Direct Effect (NDE) (Section 3.6.4), Natural Indirect Effect (NIE) (Section 3.6.5), Probability of Necessity (PN) (Section 3.6.6), and Probability of Sufficiency (PS) (Section 3.6.7).

# 3.6.1 Actual Causality (AC)

AC deals with attribution and responsibility allocation problems encountered in practical applications like policy-implementing (Capano & Howlett, 2021), diagnosing causes (Wang et al., 2021; Albantakis et al., 2019), and decision making (Triantafyllou et al., 2022). AC goes beyond the mere identification of correlations in data; it enables language models to grasp the underlying mechanisms that lead to certain outcomes and make predictions that reflect a deeper understanding of how different elements are interrelated. This understanding is essential for generating more accurate, relevant, and contextually appropriate responses, especially in complex causal scenarios where multiple factors interact. Studies have demonstrated that this causal scenario presents considerable challenges for language models (Kiciman et al., 2023; Suzgun et al., 2023).

Causal scenario setting. In AC, the causal scenario presents an actual story (e.g., "Jake desperately wants to win the rifle contest. He knows that he will only win the contest if he hits the bull's-eye. He raises the rifle, gets the bull's-eye in the sights, and presses the trigger. But Jake isn't very good at using his rifle. His hand slips on the barrel of the gun, and the shot goes wild... Nonetheless, the bullet lands directly on the bull's-eye. Jake wins the contest. Did

# Scenario: AC

# Prompt:

Question: How would a typical person answer each of the following questions about causation?

Jake desperately wants to win the rifle contest. He knows that he will only win the contest if he hits the bulls-eye. He raises the rifle, gets the bull's-eye in the sights, and presses the trigger. But Jake isn't very good at using his rifle. His hand slips on the barrel of the gun, and the shot goes wild... Nonetheless, the bullet lands directly on the bull's-eye. Jake wins the contest. Did Jake intentionally hit the bull's-eye?

Options:

-Yes

- No

Answer (Yes or No?):

Ground truth: No

Figure 3.16 Example of actual causality.

Jake intentionally hit the bull's-eye?"<sup>10</sup>). Each story ends with a binary classification question (i.e., "Yes" or "No"), aiming to challenge whether model can predict the correct answer ("No" for this example). See Figure 3.16 for a detailed illustration.

# 3.6.2 Causal Explanation Generation (CEG)

The ability to understand and explain causality is a cornerstone for building machines that can reason reliably. This causal scenario aims to examine whether language models can generate comprehensive and logically sound explanations that elucidate the causal relationships between specific events (Gao et al., 2023a). By understanding and articulating the underlying causes behind phenomena, language models can offer more accurate, relevant, and transparent responses, thereby improving user interactions. This capability is particularly important in decision-support contexts, such as healthcare (Richens et al., 2020) and policy-making (Swinkels, 2020), where understanding causal relationships is essential. Additionally, causal explanations can aid in debugging and refining language models by revealing how they process information, facilitating improvements in model performance and fairness (Lin et al., 2021; O'Shaughnessy et al., 2020; Madumal et al., 2020; Moraffah et al., 2020).

Causal scenario setting. In CEG, the causal scenario begins by presenting a cause-effect pair (e.g., "Cause: The financial crisis left many people homeless." and "Effect: After the financial crisis, the suicide rate increased significantly.[11] ). The model needs to provide a reasonable explanation of why the cause can lead to the effect (e.g., "Homelessness greatly increases the likelihood of a suicide attempt.") See Figure 3.17 for a detailed illustration.

# 3.6.3 Effect of the Treatment on the Treated (ETT)

ETT is employed to assess whether individuals who receive treatment are the ones who would derive the greatest advantage from it. In other words, the issue ETT seeks to address is: What differences would there be in outcomes for individuals who did receive treatment compared to if they had not undergone treatment? When a policymaker's objective is to determine whether to uphold or discontinue an existing program within

# Scenario: CEG

# Prompt:

Cause: The financial crisis left many people homeless.

Effect: After the financial crisis, the suicide rate increased significantly.

Question: Why the cause can lead to the effect?

Answer:

Ground truth: Homelessness greatly increases the likelihood of a suicide attempt.


Figure 3.17 Example of causal explanation generation.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/29dd0f1b43d9a906a6c54d40be9a98be738d7453a06a1b632e9c9ab911404184.jpg)



(a) ETT


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5cc55443368bb8912ec5249f8a8959d390d1a7ec9f75e235aaa58dfd3296550f.jpg)



(b) NDE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c232ef58fa05d11f53d8c397af332b7e3a56d26e3f3bb43f32f3eb92a39ea1eb.jpg)



(c) NIE



Figure 3.18 Real-world examples of ETT, NDE and NIE.  $X$  and  $X'$  represent the treatments,  $Y$  represents the outcome, and  $M$  represents the mediator.


its present incentive framework, the key parameter of concern should measure the ETT (Pearl, 2009). The appropriate formula is  $ETT = E(Y_{1} - Y_{0}|X = 1)$ , where  $Y_{x}$  denotes the value of outcome  $Y$  when treatment  $X$  is kept constant at  $X = x$  (Pearl, 2009). As Figure 3.18(a) demonstrates, the ETT in a job training program for unemployed individuals assesses the program's specific impact on participants by comparing their employment outcomes before and after participation, against similar non-participants. ETT reveals the direct benefits of the program, aiding in evaluating its effectiveness and guiding policy decisions. As a crucial metric for assessing the effectiveness of voluntary enrollment in programs by those who are eligible, ETT is extensively used in various fields including econometrics (Roth et al., 2023; Baker et al., 2022; De Chaisemartin & d'Haultfoeuille, 2023), healthcare (Jastreboff et al., 2022), and psychology (Gomila, 2021).

Causal scenario setting. Similar to ATE, we provide a causal graph (e.g., "Parents' income has a direct effect on child's education level. Parents' income has a direct effect on child's health status. Parents' income has a direct effect on child's social skills.") along with corresponding conditional probabilities (e.g., "For those with parents' income being high, the probability of child's health status being poor is 0.1112. For those with parents' income being low, the probability of child's health status being poor is 0.2617"). The causal scenario requires the model to determine the ETT between variables (e.g., "For those with parents' income being high, if their parents' income had been low, would the child's health status have been more likely to be poor?"). The model needs to address both binary classification ("Yes") and probability calculation ("-0.1505") questions. See Figure 3.19 for a detailed illustration.

# Scenario: ETT

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Parents' income has a direct effect on child's education level. Parents' income has a direct effect on child's health status. Parents' income has a direct effect on child's social skills.

For those with parents' income being high, the probability of child's health status being poor is 0.1112. For those with parents' income being low, the probability of child's health status being poor is 0.2617.

Instruction: Consider the effect of treatment on the treated (ETT) of parents' income on child's health status.

Question: For those with parents' income being high, if their parents' income had been low, would the child's health status have been more likely to be poor?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "Yes", "PROB": "-0.1505"}

Figure 3.19 Example of effect of the treatment on the treated.

# 3.6.4 Natural Direct Effect (NDE)

Different from the CDE, the NDE quantifies the anticipated rise in outcome  $Y$  when the treatment shifts from  $X = x$  to  $X = x'$ , with the mediator  $M$  held at the value it would have naturally taken under the condition  $X = x$  (Pearl, 2001). Thus,  $NDE = E[(Y(x', M(x))) - E(Y(x))]$ . We can conclude that the most distinct difference between CDE and NDE is that: NDE considers the mediator's natural state when untreated, whereas CDE sets the mediator to one or more predetermined levels. Figure 3.18(b) depicts a causal scenario of studying how smoking (treatment) affects heart disease (outcome), with blood pressure (mediator) acting as a crucial intermediary factor. Here, the NDE represents the direct influence of smoking on heart disease, bypassing the effects mediated by blood pressure. And it seeks to answer: What would be the direct effect of smoking on heart disease if we could keep the blood pressure of smokers at the level it would naturally be if they did not smoke? The NDE allows for isolating and understanding the direct impact of a treatment on an outcome, independent of any mediating pathways. This distinction is crucial in fields like computer vision (Niu et al., 2021), natural language processing (Vig et al., 2020), and public health (Carter et al., 2021), where understanding the specific mechanisms through which interventions affect outcomes can inform the development of more effective strategies.

Causal scenario setting. Given a causal graph (e.g., "Mktt has a direct effect on oroo. Mktt has a direct effect on tlxp. Mktt has a direct effect on enck. Oroo has a direct effect on tlxp.") along with corresponding conditional probabilities (e.g., "For those with mktt being high, the probability of oroo being low is 0.8817. For those with mktt being low, the probability of oroo being low is 0.6940"), the causal scenario requires the model to determine the NDE between variables (e.g., "Suppose the mediator keeps constant when mktt is changed to be high, would the oroo have been more likely to be low?"). The model needs to address both Binary classification ("Yes") and probability calculation ("0.1877") types of questions. See Figure 3.20 for a detailed illustration.

# 3.6.5 Natural Indirect Effect (NIE)

NIE measures the extent of change in the outcome through the mediator when the treatment is modified. It excludes the direct effects of treatment on the outcome that does not involve the mediator. This methodology enables us to comprehend the mediator's role and significance within the causal relationship between treatment

# Scenario: NDE

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Mktt has a direct effect on oroo. Mktt has a direct effect on tlxp. Mktt has a direct effect on enck. Oroo has a direct effect on tlxp.

For those with mktt being high, the probability of oroo being low is 0.8817. For those with mktt being low, the probability of oroo being low is 0.6940.

Instruction: Consider the natural direct effect (NDE) of mktt on oroo.

Question: Suppose the mediator keeps constant when mktt is changed to be high, would the oroo have been more likely to be low? Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "Yes", "PROB": "o.1877"}

Figure 3.20 Example of natural direct effect.

and outcome. Specifically, the NIE quantifies the anticipated rise in  $Y$  when the treatment variable remains fixed at  $X = x$ , while allowing the mediator  $M$  to adjust to the level it would have reached if  $X$  had been set to  $x'$ . In essence, it isolates and accounts for the segment of the effect solely attributable to the mediation process, while neutralizing the ability of  $Y$  to react to changes in  $X$  (Pearl, 2001). The quantitative expression is  $NIE = E[(Y(x, M(x')) - E(Y(x)))]$ . As Figure 3.18(c) shows, consider a study on examining how job satisfaction (treatment) improves employees' mental health (outcome) by reducing job-related stress (mediator). In this example, the NIE would measure the improvement in employees' mental health resulting solely from the increase in job satisfaction through the pathway of reducing job-related stress.

Causal scenario setting. Similar to NDE, we provide a causal graph (e.g., "Kdns has a direct effect on jazt. Jazt has a direct effect on ftog. $^{12}$ " with corresponding conditional probabilities (e.g., "For those with jazt being low and kdns being low, the probability of ftog being high is 0.5564. For those with kdns being high, the probability of jazt being low is 0.7767. For those with kdns being low, the probability of jazt being low is 0.9313. For those with jazt being high and kdns being low, the probability of ftog being high is 0.9241.") The causal scenario requires the model to determine the NIE between variables (e.g., "Suppose kdns is held constant and the mediator changes to whatever value it would have attained under kdns changing to be high, would ftog have been more likely to be high?"). The model needs to address both binary classification ("Yes") and probability calculation ("0.0568") questions. See Figure 3.21 for a detailed illustration.

# 3.6.6 Probability of Necessity (PN)

PN essentially seeks to address the question: "In cases where the outcome occurs, could it still happen without the treatment?" If the absence of the treatment leads to that the outcome would not happen, then it indicates that the treatment is necessary for the occurrence of the outcome (Pearl, 2022). In the context of binary events, we denote the treatment as  $X = x$  and the outcome as  $Y = y$ , and their respective negations as  $X = x'$  and  $Y = y'$ . The objective of PN can be determined as: Find the probability that if  $X$  had been  $x'$ ,  $Y$  would be  $y'$ , given that, in reality,  $X$  is  $x$  and  $Y$  is  $y$  (Pearl et al., 2016). The formula is  $PN(x, y) = P(Y_{x'} = y'|X = x, Y = y)$ .

# Scenario: NIE

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Kdns has a direct effect on jazt. Jazt has a direct effect on ftog.

For those with jazt being low and kdns being low, the probability of ftog being high is 0.5564. For those with kdns being high, the probability of jazt being low is 0.7767. For those with kdns being low, the probability of jazt being low is 0.9313. For those with jazt being high and kdns being low, the probability of ftog being high is 0.9241.

Instruction: Consider the natural indirect effect (NIE) of kdns on ftog.

Question: Suppose kdns is held constant and the mediator changes to whatever value it would have attained under kdns changing to be high, would ftog have been more likely to be high?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "Yes", "PROB": "o.0568"}

Figure 3.21 Example of natural indirect effect.

PN provides deeper insight into the fundamental principle of legal assessment known as the "but-for" test. In practical legal contexts, this guideline directs us: favorable judgments for the plaintiff should only be rendered when the assumption that "the harm would not have occurred if not for the defendant's actions" approaches certainty (Peaslee, 1934). For example, in a traffic accident case where a driver failed to slow down at a yellow light leading to a collision, the court uses the PN to evaluate if slowing down could have prevented the accident. If PN indicates a high likelihood that the accident would have been avoided by slowing down, the driver's action is deemed a necessity cause for the collision, influencing the court's decision on liability. Formalizing and calculating the PN is vital for allocating resources efficiently, prioritizing interventions, and crafting strategies that address the most critical factors contributing in artificial intelligence (Watson et al., 2021; Tan et al., 2022, 2021; Zhang et al., 2022a).

Causal scenario setting. Given a causal graph (e.g., "Temperature has a direct effect on rainfall. Humidity has a direct effect on rainfall.") and corresponding conditional probabilities (e.g., "For those with humidity being low, the probability of rainfall being dry is 0.6861. The probability of humidity being low and rainfall being dry is 0.4408. The probability of humidity being high and rainfall being wet is 0.0168."), the causal scenario requires the model to calculate the upper bound or lower bound of PN (e.g., "Given that humidity was high and rainfall was wet, what is the upper bound of the probability of the rainfall would have been dry if the humidity had been low?"). See Figure 3.22 for a detailed illustration.

# 3.6.7 Probability of Sufficiency (PS)

Parallel to the concept of PN, the PS addresses: "In cases where the outcome does not occur, could it happen if a treatment exists?" If the presence of this treatment leads to the outcome, it implies that this treatment is sufficient to trigger the outcome (Pearl, 2022). It provides an estimate of the probability that the intervention of  $x$  would result in the occurrence of outcome  $y$  when both  $x$  and  $y$  are not currently present (Pearl, 2009), mathematically expressed as:  $PS(x,y) = P(Y_x = y|X = x',Y = y')$ . Consider a workplace injury case where an employee was harmed due to a machine malfunction, the court applies the PS to evaluate if adhering to safety protocols. Considering that regular maintenance ( $X = 1$ ) would have prevented the injury ( $Y = 1$ ), given the protocols were initially not followed ( $X = 0$ ) and the injury occurred ( $Y = 0$ ). A high PS indicates

# Scenario:PN

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Temperature has a direct effect on rainfall. Humidity has a direct effect on rainfall.

For those with humidity being low, the probability of rainfall being dry is 0.6861. The probability of humidity being low and rainfall being dry is 0.4408. The probability of humidity being high and rainfall being wet is 0.0168.

Instruction: Consider the probability of necessity (PN) of humidity on rainfall.

Question: Given that humidity was high and rainfall was wet, what is the upper bound of the probability of the rainfall would have been dry if the humidity had been low?

Provide the calculation result to four decimal places in JSON format, like {"PROB": "0.1234"}:

Ground truth: {"PROB": "1.0000"}

Figure 3.22 Example of probability of necessity.

# Scenario: PS

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Level of education has a direct effect on job performance. Job performance has a direct effect on salary. Job performance has a direct effect on job satisfaction. Salary has a direct effect on job satisfaction.

For those with job performance being excellent, the probability of salary being low is 0.0539. The probability of salary being low is 0.0857. The probability of job performance being poor and salary being low is 0.0585.

Instruction: Consider the probability of sufficiency (PS) of job performance on salary.

Question: Given that job performance was poor and salary was low, what is the lower bound of the probability that salary would have been high if the job performance had been excellent?

Provide the calculation result to four decimal places in JSON format, like {"PROB": "0.1234"}:

Ground truth: {"PROB": "0.5436"}

Figure 3.23 Example of probability of sufficiency.

that following the protocols would likely have averted the harm, potentially establishing the employer's liability for the injury by demonstrating negligence in safety measures. This approach is critical in legal judgments involving causality and negligence.

Causal scenario setting. Similar to PN, PS also involves providing a causal graph along with corresponding conditional probabilities, requiring the model to calculate the upper bound or lower bound of PS. See Figure 3.23 for a detailed illustration.

# 3.6.8 Counterfactual Reasoning (CR)

To ascertain what led to a specific occurrence, it is crucial to imagine "what-if" causal scenarios in which the event might not have taken place and then examine the resulting outcomes. Counterfactual reasoning involves contemplating hypothetical causal scenarios or alternative versions of reality by modifying certain factors or conditions present in an actual event or situation (Kahneman & Miller, 1986; Byrne, 2007). It is also a valuable skill for language models to provide perspectives and insights that might not be immediately obvious based

# Scenario: CR

# Binary Classification

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Smoking has a direct effect on tar deposit. Tar deposit has a direct effect on lung cancer. We know that smoking causes high tar deposit, and we know that high tar deposit causes lung cancer.

Question: Would the person has no lung cancer if smoking instead of nonsmoking?

Answer (Yes or No?):

Ground truth: No

# Choice Selection

# Prompt:

Input Event: A woman sees a fire.

Counterfactual Question: What would have happened if the woman had touched the fire?

Option 1: That is not possible.

Option 2: She would have seen fire.

Option 3: She would have been burned.

Option 4: She would not have been burned.

Answer (Option 1 or 2 or 3 or 4?):

Ground truth: Option 3

Figure 3.24 Example of counterfactual reasoning.

on the available information.

Causal scenario setting. There are two types of questions in CR. (1) Binary classification: We provide the model with a causal graph (e.g., "Smoking has a direct effect on tar deposit. Tar deposit has a direct effect on lung cancer."13) and corresponding relationships (e.g., "We know that smoking causes high tar deposit, and we know that high tar deposit causes lung cancer."), and give the model a counterfactual question to answer "yes" or "no" (e.g., "Would the person has no lung cancer if smoking instead of nonsmoking?"). (2) Choice selection: An event (e.g., "A woman sees a fire.") and a counterfactual question (e.g., "What would have happened if the woman had touched the fire?"14) are posed to the model. The model is required to choose the correct option. See Figure 3.24 for a detailed illustration.

# 4 Data Collection

In this section, we provide a detailed discussion on the utilization of our datasets, which is crucial for understanding and reproducing the CaLM. First, we describe the methodology behind our dataset selection in Dataset Selection (Section 4.1). Here, we offer a thorough justification for each chosen dataset to ensure our selection process is transparent and well-founded. Second, we depict how self-constructed datasets are developed in Dataset Construction (Section 4.2), providing a detailed guide for researchers interested in creating their own datasets for use with CaLM. Our goal extends beyond merely facilitating the use of our datasets; we aim to openly share our dataset construction methodologies to foster the growth and development of the causal research community. Finally, in Data Statistics (Section 4.3), we perform a detailed statistical analysis of the datasets, offering clear insights into the scale and scope of CaLM.

# 4.1 Dataset Selection

As highlighted by OpenAI (2023), the ability to tackle challenging tasks is a key factor differentiating language models. Therefore, the primary objective of CaLM is to evaluate the abilities of language models to undertake complex causal reasoning tasks. To achieve this goal, we have selected 31 datasets, which can be further subdivided into 44 subsets, for comprehensive evaluation. Approximately  $10\%$  of the data used in our benchmark originates from pre-existing, publicly available datasets that are specifically aligned with causal tasks in the Natural mode. The remaining  $90\%$  consists of datasets that we have developed. We begin with an overview presented in Table 4.1, offering an immediate and clear outline of these resources. A more detailed exposition of the datasets from these distinct sources (Open-source Datasets (Section 4.1.1) and Self-constructed Datasets (Section 4.1.2)) is provided below.

# 4.1.1 Open-source Datasets

All the open-source datasets we select belong to the Natural mode. To clarify them further, we will elaborate on each dataset based on the causal ladder, corresponding to the causal scenario it addresses (for more detailed information about the causal scenario, please refer to Causal Targets(Section 3)).

Causal discovery. (1) COPA (Choice Of Plausible Alternatives) is developed by Roemmele et al. (2011). This dataset focuses on determining causal relationships, consisting of a total of 1000 queries. Each query presents a premise along with two potential causes or effects. The objective is to identify the accurate causal relationship grounded on the information provided in the premise. (2) E-CARE (Explainable CAusal REaasoning) (Du et al., 2022) includes over 21,000 multiple-choice questions centered on causal reasoning. It goes beyond simple queries by offering detailed conceptual explanations for each question, elucidating the rationale behind the causal relationships. (3) CTB (Causal-TimeBank) originates from the TimeBank corpus by Pustejovsky et al. (2006) and is used in the TempEval-3 task (Mirza et al., 2014). This dataset consists of 6,813 events and 318 causal event pairs. (4)ESC (Event StoryLine Corpus) (Caselli & Vossen, 2017) is designed to facilitate the identification of temporal and causal relations. (5)MAVEN-ERE (Event Relation Extraction) (Wang et al., 2022) is an expansive resource developed from the MAVEN dataset (Wang et al., 2020b). The MAVEN dataset is a comprehensive tool for detecting events across a wide range of domains, containing 4,480 documents

<table><tr><td>Dataset</td><td>Subset</td><td>Causal ladder</td><td>Causal scenario</td><td>Mode</td><td>Language</td></tr><tr><td colspan="6">Open-source Datasets</td></tr><tr><td>COPA</td><td>-</td><td>Causal discovery</td><td>PCD</td><td></td><td></td></tr><tr><td>E-CARE</td><td>-</td><td>Causal discovery</td><td>PCD</td><td></td><td></td></tr><tr><td>CTB</td><td>-</td><td>Causal discovery</td><td>ECI</td><td></td><td></td></tr><tr><td>ESC</td><td>-</td><td>Causal discovery</td><td>ECI</td><td></td><td></td></tr><tr><td>MAVEN-ERE</td><td>-</td><td>Causal discovery</td><td>ECI</td><td></td><td></td></tr><tr><td>CLADDER</td><td>correlation</td><td>Association</td><td>CORR</td><td rowspan="2">Natural</td><td rowspan="2">EN</td></tr><tr><td>CLADERR</td><td>exp-away</td><td>Association</td><td>EAE</td></tr><tr><td>CLADDER</td><td>backadj</td><td>Intervention</td><td>BAS</td><td></td><td></td></tr><tr><td>CLADDER</td><td>collider-bias</td><td>Intervention</td><td>CB</td><td></td><td></td></tr><tr><td>CLADDER</td><td>det-counterfactual</td><td>Counterfactual</td><td>CR</td><td></td><td></td></tr><tr><td>CRASS</td><td>-</td><td>Counterfactual</td><td>CR</td><td></td><td></td></tr><tr><td>BBH</td><td>causal judgement</td><td>Counterfactual</td><td>AC</td><td></td><td></td></tr><tr><td>E-CARE</td><td>-</td><td>Counterfactual</td><td>CEG</td><td></td><td></td></tr><tr><td colspan="6">Self-constructed Datasets</td></tr><tr><td>CaLM-AR</td><td>-</td><td>Causal discovery</td><td>AR</td><td>Symbolic</td><td rowspan="18">EN&amp;CN</td></tr><tr><td>CaLM-CA</td><td>FP/FA</td><td>Causal discovery</td><td>CA</td><td>Symbolic</td></tr><tr><td>CaLM-AS</td><td>max/min/mix-BAS</td><td>Intervention</td><td>BAS</td><td>Symbolic</td></tr><tr><td>CaLM-AS</td><td>FAS</td><td>Intervention</td><td>FAS</td><td>Symbolic</td></tr><tr><td>CaLM-IV</td><td>-</td><td>Intervention</td><td>IV</td><td>Symbolic</td></tr><tr><td>CaLM-CEI</td><td>0.2/0.4/0.6/0.8-UC</td><td>Intervention</td><td>CEI</td><td>Symbolic</td></tr><tr><td>CaLM-ATE</td><td>ATE-basic/hard</td><td>Intervention</td><td>ATE</td><td>Mathematical</td></tr><tr><td>CaLM-ATE</td><td>ATE-natural</td><td>Intervention</td><td>ATE</td><td>Natural</td></tr><tr><td>CaLM-CDE</td><td>CDE-basic/hard</td><td>Intervention</td><td>CDE</td><td>Mathematical</td></tr><tr><td>CaLM-CDE</td><td>CDE-natural</td><td>Intervention</td><td>CDE</td><td>Natural</td></tr><tr><td>CaLM-ETT</td><td>ETT-basic/hard</td><td>Counterfactual</td><td>ETT</td><td>Mathematical</td></tr><tr><td>CaLM-ETT</td><td>ETT-natural</td><td>Counterfactual</td><td>ETT</td><td>Natural</td></tr><tr><td>CaLM-NDE</td><td>NDE-basic/hard</td><td>Counterfactual</td><td>NDE</td><td>Mathematical</td></tr><tr><td>CaLM-NDE</td><td>NDE-natural</td><td>Counterfactual</td><td>NDE</td><td>Natural</td></tr><tr><td>CaLM-NIE</td><td>NIE-basic/hard</td><td>Counterfactual</td><td>NIE</td><td>Mathematical</td></tr><tr><td>CaLM-NIE</td><td>NIE-natural</td><td>Counterfactual</td><td>NIE</td><td>Natural</td></tr><tr><td>CaLM-PN</td><td>PN-basic/hard</td><td>Counterfactual</td><td>PN</td><td>Mathematical</td></tr><tr><td>CaLM-PS</td><td>PS-basic/hard</td><td>Counterfactual</td><td>PS</td><td>Mathematical</td></tr><tr><td>All open-source datasets</td><td>-</td><td>All 4 rungs</td><td>-</td><td>Natural</td><td>CN</td></tr></table>

Tab. 4.1 Datasets selection of CaLM. The selected datasets are organized by their source (i.e., open-source or self-constructed). In cases where datasets include subset $^{15}$ , we make extra distinctions at the subset level. The table additionally outlines the causal scenarios utilizing these datasets, along with their respective levels of the causal ladder, mode, and language.

from English Wikipedia. Building upon this, the MAVEN-ERE dataset introduces a substantial collection of 57,992 causal relations, making the task of ERE on it complex and demanding. For more background information on the PCD and ECI causal scenarios, please refer to Causal Discovery (Section 9.4.1).

Association. The CLADDER dataset, developed by Jin et al. (2023a), consists of over 10,000 causal questions categorized by varying levels of complexity across multiple levels of causal ladder. The dataset includes a wide range of causal graphs that visually represent complex relationships among various factors. It is further enriched by narratives that provide context for the questions, illustrating real-world causal scenarios or hypothetical situations where these relationships are pivotal. We choose the cladder-v1-aggregate.json for our evaluation. It should be noted that we use the initial version of this document, which has been subject

to updates over time. $^{16}$  In this rung, we use two subsets of CLADDER: correlation and exp-away. These two subsets contain 1476 and 168 data points, respectively. For more details on these two causal scenarios, please refer to Association (Section 9.4.2).

Intervention. In this rung, we use two subsets of CLADDER: backadj and collider-bias. These two subsets contain 227 and 168 samples, respectively. For additional details on these two causal scenarios, please refer to Intervention (Section 9.4.3).

Counterfactuals. (1) CRASS (Counterfactual Reasoning Assessment) (Frohberg & Binder, 2022) is a vital tool for analyzing the proficiency of language models in handling question-based counterfactual conditionals. It comprises 275 carefully crafted queries designed to test the models' ability to interpret and respond to counterfactual reasoning challenges. These queries are part of the BIG-bench project (Srivastava et al., 2023). (2) The causal judgment $^{17}$  dataset, part of the BIG-bench Hard (Suzgun et al., 2023), consists of 187 narratives that effectively demonstrate actual causality (Halpern, 2016), reflecting the natural human tendency to assign cause, responsibility, and blame to events and their respective outcomes. Each story concludes with a clear yes/no question, providing a structured evaluation of language models' comprehension and interpretation of causal relationships and associated concepts. (3) det-counterfactual is a subset from CLADDER, featuring 1476 questions about counterfactual reasoning with a causal graph. For more detailed information on the CR and AC causal scenarios, please refer to Counterfactuals (Section 9.4.4).

# 4.1.2 Self-constructed Datasets

The illustration for this section will be divided into two categories: (i) Symbolic, and (ii) Natural and Mathematical. To begin with, it is important to note that each of the datasets we have constructed contains 1600 samples. This sample size is considered sufficient for evaluation purposes while also preventing resource wastage. Regarding language, all datasets from Open-source Datasets (Section 4.1.1) are exclusively in English; hence, we translate them into Chinese. Additionally, our self-constructed datasets are available in both English and Chinese versions. Moreover, the core component of the self-constructed datasets is the causal graph. That is, all of our data samples are composed of a causal graph, along with questions derived from this graph.

Symbolic. (1) CaLM-AR (Abstract Reasoning) aims to assess language models' ability to accurately identify causal relationships within a graph, despite the presence of additional disturbances. This assessment is crucial in measuring the models' genuine understanding of complex causal graphs. It tests if the models can effectively filter out extraneous noise to discern true causal pathways, thus highlighting their deep understanding of causal relationships. Each data sample within this dataset is accompanied by a causal graph that describes the relationships among various elements in a non-alphabetical sequence (e.g., it might indicate that "A causes B, A causes D, B causes C, C causes A." rather than a straightforward "A causes B, B causes C and C causes D.", which introduces an additional layer of complexity to challenge the language models further. (2) CaLM-CA (Causal Attribution) is designed to evaluate whether the model can understand the direct and indirect influences that variables or events (represented as nodes) exert on each other within a system. They are composed of 2 subsets: FP (Find Parent) and FA (Find Ancestor). As their names suggest, these datasets challenge the model to identify hierarchical relationships between nodes, specifically determining whether a node is a parent or an

# Dataset: CaLM-CA

index: 510

vertices: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

edges: "A causes J, A causes D, A causes C, A causes I, B causes C, B causes I, C causes E, C causes F, D causes E, D causes I, D causes G, D causes J, E causes I, E causes F, E causes G, F causes G, F causes J, F causes H, G causes I, G causes J, and H causes I"

sampled_ancestor:"l"

GT_ancestor: ["E", "C", "G", "D", "B", "A", "F"]

attribute:"J"

Label_ancestor: o

Figure 4.1 An example of CaLM-CA dataset.

# Dataset: CaLM-CEI

index: 589

vertices: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

di_edge: "A causes D, A causes G, A causes H, A causes E, B causes I, B causes H, C causes D, C causes I, C causes H, C causes G, D causes I, D causes G, D causes H, E causes J, E causes H, F causes I, F causes J, and I causes J"

bi_edge: "D and I, C and G, and A and E"

treatment:"C"

outcome:"G"

label: o

Figure 4.2 An example of CaLM-CEI dataset.

ancestor of another in the graph. An example of the FA dataset is illustrated in Figure 4.1. (3) CaLM-CEI (Causal Effect Identification) is crafted to test a model's ability to determine whether the causal effect of a treatment on an outcome can be estimated from observational data. This dataset is segmented into four distinct subsets: 0.2-UC (Unobserved Confounder), 0.4-UC, 0.6-UC and 0.8-UC, each characterized by a different proportion of unobserved confounders affecting  $20\%$ ,  $40\%$ ,  $60\%$ , and  $80\%$  of the nodes in the graph, respectively. As the percentage of unobserved confounders increases, the complexity of identifying causal effects also rises. An example is provided in Figure 4.2. (4) CaLM-AS (Adjustment Set) is used to assess a model's understanding of causal graphs and the concepts of Back-door Criterion and Front-door Criterion (Pearl, 1995). The Back-door Criterion provides a method for identifying sets of variables that need to be controlled for to estimate causal effects from observational data. The Front-door Criterion can be applied in cases where no variable satisfies the Back-door Criterion. To be specific, the Front-door Criterion helps in estimating the causal effect through the mediator, regarding the existence of unobserved confounders. This dataset is divided into four subsets: max-BAS (maximal-Backdoor Adjustment Set), min-BAS (minimal-Backdoor Adjustment Set), mix-BAS (mix-Backdoor Adjustment Set), and FAS (Frontdoor Adjustment Set). In the context of a specified causal graph in which an ordered pair of variables is considered, the minimal/max backdoor set includes the collection of variables that either minimally or maximally meet the backdoor criterion. The Mix set is a combination of both. The front-door set comprises variables that fulfill the Front-door Criterion. An example of the FAS dataset is demonstrated in Figure 4.4. (5) CaLM-IV (Instrumental Variable) is designed to assess a model's capability to determine the independence among variables and its understanding of the IV concept. Accurate identification of an instrumental variable allows for estimating causal effects even in the presence of unobserved confounders. The setup of this dataset closely mirrors that of the CaLM-AS, involving a causal graph and specifying a cause-effect pair. Figure 4.3 provides an example.

# Dataset: CaLM-IV

index: 697

vertices: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

edges: "A causes C, A causes H, A causes K, A causes F, A causes I, A causes G, B causes H, B causes K, B causes G, B causes C, D causes F, D causes J, E causes I, E causes K, F causes H, F causes G, F causes K, G causes H, G causes J, G causes I, H causes J, H causes I, I causes J, and J causes K"

option1:"K"

option2:"D"

option3: "A"

GT:  $[^{\prime \prime}D]^{\prime \prime}$

treatment:"F"

outcome:"l"

Label_instrumental: 2

Figure 4.3 An example of CaLM-IV dataset.

# Dataset: CaLM-AS (FAS)

index: 470

vertices: ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

edges: "A causes E, A causes F, A causes G, A causes B, A causes D, A causes H, B causes D, B causes E, B causes I, B causes F, B causes C, B causes H, C causes E, C causes I, C causes F, C causes H, D causes G, F causes I, F causes H, G causes H, and H causes I"

option1: "H"

option2:"A"

option3:"B"

GT: ["B"]

treatment:"A"

outcome:"C"

Label_frontdoor: 3

Figure 4.4 An example of CaLM-AS dataset.

Natural and Mathematical. (6) CalM-ATE (Average Treatment Effect) is used to evaluate the analytical and computational abilities of a language model in predicting changes to an outcome variable following an intervention on the treatment variable, given a causal graph and data distribution. This dataset is divided into three subsets: ATE-natural focuses on qualitative analysis, with responses limited to "Yes" and "No"; ATE-basic and ATE-hard both require the quantitative calculation of ATE, whose main distinction lies in the complexity of the causal graphs (ATE-basic features graphs with fewer nodes). Note that the subsequent datasets (7)-(10) introduced below are similarly divided into three subsets - X-natural, X-basic and X-hard - a classification that will not be reiterated further in this context. An example of ATE-basic is shown in Figure 4.5. (7) CalM-CDE (Controlled Direct Effect) evaluates the model's ability to calculate the direct effect of the treatment variable on the outcome variable while keeping one or more mediators fixed. (8) CalM-ETT (Effect of the Treatment on the Treated) accesses the model's capability to calculate the treatment effect on those who have already been treated. (9) CalM-NDE (Natural Direct Effect) measures the model's ability to compute the natural direct effect, assuming mediators remain constant during the intervention on treatment variables. (10) CalM-NIE (Natural Indirect Effect) tests the model's ability to calculate the natural indirect effect by altering mediators to the values they would have attained under the intervention, while the treatment variable itself keeps constant. (11) CalM-PN (Probability of Necessity) aims to evaluate the model's capacity to estimate the upper and lower bounds of the probability of necessity, which measures the necessity of the treatment for those who received it and experienced a positive outcome. This dataset is divided into two subsets, PN-basic

# Dataset: CaLM-ATE

# Index: 5100

# Background:

graph: Given a causal graph with 4 nodes A, B, C, D, and 4 edges A->B, A->C, B->D, C->D.

real_world_meaning: The real world meaning of each node is defined as follows: A represents the number of hours studied for an exam, B represents the score obtained on the exam, C represents the amount of sleep the night before the exam and D represents the overall performance in the course.

data_info: For those with the amount of sleep the night before the exam being not enough and the number of hours studied for an exam being few, the probability of the overall performance in the course being excellent is 0.5544. For those with the amount of sleep the night before the exam being enough and the number of hours studied for an exam being few, the probability of the overall performance in the course being excellent is 0.9356. The probability of the number of hours studied for an exam being few is 0.6782. For those with the amount of sleep the night before the exam being not enough and the number of hours studied for an exam being many, the probability of the overall performance in the course being excellent is 0.6374. For those with the amount of sleep the night before the exam being enough and the number of hours studied for an exam being many, the probability of the overall performance in the course being excellent is 0.9568. The probability of the number of hours studied for an exam being many is 0.3218.

data_info Maths:  $P(D = 1|C = 0, A = 0) = 0.5544$ ;  $P(D = 1|C = 1, A = 0) = 0.9356$ ;  $P(A = 0) = 0.6782$ ;  $P(D = 1|C = 0, A = 1) = 0.6374$ ;  $P(D = 1|C = 1, A = 1) = 0.9568$ ;  $P(A = 1) = 0.3218$ ;

Instruction: Consider the average treatment effect (ATE) of the amount of sleep the night before the exam on the overall performance in the course.

Question: If the amount of sleep the night before the exam is changed to be not enough, will the overall performance in the course be more likely to be excellent?

# Answer: No

# Reason:

Step 1: Check whether treatment (C) is a cause of outcome (D). Node C is a cause of node D because there is one or more directed paths from C to D (e.g. C->D).

Step 2: Identification of the Causal Effect. P(D|do(C)) can be identified.

Step 3: Find a valid backdoor adjustment set:  $\{\mathsf{A}\}$

Step 4: ATE = P(D=1|do(C=0))-P(D=1|do(C=1)) = sum_A [P(D=1|C=0,A)*P(A)-P(D=1|C=1,A)*P(A)] = [P(D=1|C=0,A=o)*P(A=o)-

[ P(D = 1|C = 1, A = 0)*P(A = 0)] + [P(D = 1|C = 0, A = 1)*P(A = 1) - P(D = 1|C = 1, A = 1)*P(A = 1)] ]

# Step 5:

P(D=1|C=0,A=0)=0.5544\tP(D=1|C=1,A=0)=0.9356\tP(A=0)=0.6782\tP(D=1|C=0,A=1)=0.6374\tP(D=1|C=1,A=1)=0.9568\tP(A=1)=0.32

Step 6: ATE=[0.5544*0.6782-0.9356*0.6782]+[0.6374*0.3218-0.9568*0.3218]=-0.3613

Step 7: ATE  $= -0.3613 <   0$  so the answer is No.

# Type: ATE

Authenticity: REAL

prob:-0.3612818467911682

Figure 4.5 An example of CaLM-ATE dataset.

and PN-hard, based on the number of nodes in the causal graphs. (12) CaLM-PS (Probability of Sufficiency) focuses on the model's ability to estimate the upper and lower bounds of the probability of sufficiency, which evaluates the sufficiency of treatment for those who did not receive treatment but had a negative outcome. Similar to CaLM-PN, this dataset is also segmented into PS-basic and PS-hard based on the complexity of the causal graphs.

# 4.2 Dataset Construction

The construction of our data consists of three parts: Constructing Natural and Mathematical Mode Datasets (Section 4.2.2), Constructing Symbolic Mode Datasets (Section 4.2.3), and Constructing Chinese Version for Open-source Datasets (Section 4.2.4). The initial steps in constructing the first two parts are identical, as both require the creation of a DAG, necessitating a common introduction to these shared procedures. We will begin by presenting the shared methodology (i.e., Generating DAGs (Section 4.2.1)). Following this, we will proceed to discuss the unique elements and detailed methodologies specific to each of the three datasets.


Algorithm 1 Algorithm for randomly generating DAGs


Input: node number  $N > 1$  graph number  $M\geq 1$  maximum attempt number  $T\geq 1$    
Output: A set of graphs  $G$ $G\gets \{\}$ $V\gets \{1,2,\dots ,N\}$    
for  $m = 1,2,\ldots ,M$  do   
for  $t = 1,2,\ldots ,T$  do e  $\leftarrow$  randint  $(N - 1,N(N - 1) / 2)$ $E\gets$  randomly sample e edges from all  $N(N - 1) / 2$  possible edges  $g\gets$  Graph(V,E) if  $g$  is weakly connected and  $g$  is not isomorphism with any  $g^{\prime}\in G$  then  $G.\mathrm{add}(g)$  break end if end for   
end for   
return  $G$

# 4.2.1 Generating DAGs

In this paper, we employ structural causal models (SCMs), as detailed in Section 2.2, to construct the underlying ground-truth causal model. We first generate several directed acyclic graphs (DAG) at random. For graphs with no more than 6 vertices, we follow Jin et al. (2023b) to construct all possible weakly connected DAGs without isomorphism between each other. Given  $N$  nodes  $\{X_{i}\}_{i = 1}^{N}$ , only edges  $X_{i}\rightarrow X_{j}$  where  $i < j$  are allowed to ensure it acyclic, yielding  $2^{N(N - 1) / 2}$  candidate graphs. We further remove graphs which are not weakly connected or isomorphic with existing graphs. However, we observed that the above algorithm runs extremely slow when  $N > 6$ . Considering that we do not actually need all possible graphs for generating causal inference data for large  $N$ , an alternative strategy is adopted that randomly generates a small number of graphs instead of all possible graphs in the cases of  $N > 6$ , see Algorithm 1.

# 4.2.2 Constructing Natural and Mathematical Mode Datasets

Given a randomly generated DAG, we first employ language models to assign real-world significance to each node. Next, we model the SCM function  $f$  as a single-layer perceptron (Rosenblatt, 1958) and randomly select parameters, ensuring that the correlation (positive or negative) between variables conforms to human common sense. We then generate statistical data strictly based on the SCM. Finally, we generate causal reasoning questions, along with ground-truth answers and reasoning steps, based on the data.

Assigning meaning for each node. A common approach to constructing causal graphs with realistic node meaning is to extract causality from natural language text. This is achieved using techniques rooted in human knowledge, machine learning, and deep learning (Yang et al., 2021a). However, most of these datasets and methods only focus on mining the relationship between two entities (usually represented as nouns, phrases or sentences), while limited works are dedicated to building a complete causal graph. Maisonnave et al. (2022) propose a framework for extracting causal graph from digital text media. However, this framework relies

<table><tr><td>Causal scenario</td><td>Template</td></tr><tr><td>ATE</td><td>If {{treatment}} is changed to be {{treatment_value}}, will {{outcome}} be more likely to be {{outcome_value}?</td></tr><tr><td>ETT</td><td>For those with {{treatment}} being {{treatment_value}}, if their {{treatment}} had been {{not_treatment_value}}, would {{outcome}} have been more likely to be {{outcome_value}?</td></tr><tr><td>CDE</td><td>Conditioned on {{mediator_1}} being {{mediator_1_value}}, {{mediator_2}} being {{mediator_2_value}}, ..., {{mediator_n}} being {{mediator_n_value}}, if {{treatment}} had been {{treatment_value}}, would {{outcome}} have been more likely to be {{outcome_value}?</td></tr><tr><td>NIE</td><td>Suppose {{treatment}} is held constant and the mediator changes to whatever value it would have attained under {{treatment}} changing to be {{treatment_value}}, would the {{outcome}} have been more likely to be {{outcome_value}?</td></tr><tr><td>NDE</td><td>Suppose the mediator keeps constant when {{treatment}} is changed to be {{treatment_value}}, would the {{outcome}} have been more likely to be {{outcome_value}?</td></tr><tr><td>PS</td><td>Given that {{treatment}} was {{treatment_negat}} and {{outcome}} was {{outcome_negat}}, what is the lower bound and upper bound of the probability that {{outcome}} would have been {{outcome_positive}} if the {{treatment}} had been {{treatment_positive}?</td></tr><tr><td>PN</td><td>Given that {{treatment}} was {{treatment_positive}} and {{outcome}} was {{outcome_positive}}, what is the lower bound and upper bound of the probability that {{outcome}} would have been {{outcome_negat}} if the {{treatment}} had been {{treatment_negat}?</td></tr></table>

Tab. 4.2 Question templates for Natural and Mathematical mode datasets.

on step-by-step data processing and time series analysis, as well as an original corpus covering a long time period, which makes it difficult to effectively generate causal graphs in batches.

Inspired by Jin et al. (2023a), nodes in our causal graphs are configured with three different types of **authenticity:** real, random, and fake. Real means each node is assigned with real-world meaning and the relationship between nodes is coherent with the commonsense. Random signifies nodes possess real-world meaning but the causal relationships among them are random (e.g., a question may state that “appearance has a direct effect on air pressure”). Fake indicates that the nodes in the causal graph consist of meaningless combinations of letters. For the causal graphs within the real and random, we believe that language models can do the job of assigning real-world meaning for the nodes of randomly generated causal graphs, based on the knowledge they have learned from massive corpora. Several causal stories from CLADDER (Jin et al., 2023a) are included as examples in our prompt. In addition, we also assign real-world meaning for the values (0 and 1) of each node, and annotate the correlation (positive or negative) of all direct cause-effect pairs. In order to reduce costs, we still prompt language model to perform these annotation tasks. Examples of our prompts and responses from ChatGPT are shown in Appendix A. As for the fake, we use a script to generate a series of

stochastic combinations of four words and assign each to a node.

Determining SCM functions. Now that the associated causal graph has been properly defined, we face another problem that how to generate SCM functions conforming to human common sense. For example, the following description "students who study hard have a 0.5 probability of getting a high score on the exam; students who do not study hard have a 0.9 probability of getting a high score on the exam." obviously goes against common sense because studying hard should have a positive effect on getting a high score.

For the sake of simplicity, we model the graph as binary, where each node takes a value from  $\{0,1\}$ . The SCM function for node  $X$  can be written as

$$
\begin{array}{l} V (X) := f _ {X} \left(V \left(P _ {X} ^ {1}\right), V \left(P _ {X} ^ {2}\right), \dots , V \left(P _ {X} ^ {k}\right), U _ {X}\right) \\ = \left\{ \begin{array}{l l} 0, & U _ {X} - g _ {X} \left(V \left(P _ {X} ^ {1}\right), V \left(P _ {X} ^ {2}\right), \dots , V \left(P _ {X} ^ {k}\right)\right) > 0 \\ 1, & \text {o t h e r w i s e} \end{array} \right. \tag {2} \\ \end{array}
$$

where  $P_X^i$  denotes the  $i$ -th parent node of  $X$ ,  $V(\cdot)$  denotes the value of a node,  $U_X \sim \mathcal{U}[0,1]$  is an independent random variable uniformly distributed on  $[0,1]$ , and  $g_X: \{0,1\}^k \mapsto [0,1]$  is a function to be determined. Note that  $g_X$  may actually be a complex non-linear function, which could be modeled as a multi-layer perceptron or even a deep neural network. In this work, we simply assume it a single-layer perceptron, namely

$$
g _ {X} \left(V \left(P _ {X} ^ {1}\right), V \left(P _ {X} ^ {2}\right), \dots , V \left(P _ {X} ^ {k}\right)\right) = \text {s i g m o i d} \left(b _ {X} + \sum_ {i = 1} ^ {k} w _ {X} ^ {i} V \left(P _ {X} ^ {i}\right)\right) \tag {3}
$$

The reasons for our choice are as follows: (1) The correlation (positive/negative) between variables can be conveniently controlled by the sign of the coefficient  $w_{X}^{i}$ . (2) Our purpose of generating the SCM function is to prepare data for generating causal reasoning questions, rather than strictly explore quantitative relationships between variables. Both  $b_{X}$  and  $w_{X}^{i}$  are randomly generated, ensuring the sign of  $w_{X}^{i}$  is consistent with the correlation relationship between  $X$  and  $P_{X}^{i}$  in reality.

Generating statistical data. For each causal graph, we generate 50K data samples according to the SCM function defined in (2). For each data sample, we start from the root node(s), and determine the value of one node once all values of its parents have been settled, until every node is assigned a value. As long as the sampling number is large enough, the probability  $P(X = x)$  and the conditional probability  $P(Y = y|X = x)$  can be approximated by these statistics.

Generating causal reasoning questions. Based on the causal graphs and the corresponding statistical data we have constructed, we generate questions with corresponding ground-truth answers and reasoning steps for different types of causal scenarios, including ATE, CDE, NIE, NDE, ETT, PN, and PS. We carefully designed and implemented the templates of questions (see Table 4.2) and reasoning steps for each type of causal task.

# 4.2.3 Constructing Symbolic Mode Datasets

Building Symbolic datasets begins with Generating DAGs (Section 4.2.1). Subsequently, nodes within DAGs are denoted using Symbolic representation. We then identify the necessary cause-effect pair for formulating the questions. In the last step, depending on the causal task at hand, we employ two Python packages (i.e., Ananke (Lee et al., 2023a) and DoWhy (Sharma & Kiciman, 2020)) to generate the ground truth.

Assigning Symbolic representation for each node. After generating DAGs, our initial task is to transform the node representations. Originally depicted numerically, these nodes required conversion into alphabetical symbols to ensure appropriate symbolic representations. For example, the numeral 0 was converted to the letter A, 1 to B, and so forth.

Choosing cause-effect pair. In causal reasoning tasks, it is crucial to clearly define the cause-effect pair involved in the problem. For this reason, in the CaLM-CA dataset, we select a cause at random and designate the effect as the node that appears last alphabetically (e.g., if the nodes are “ $A$ ,  $B$ ,  $C$ ,  $D$ ,  $E$ ), then “ $E$ ” is selected as the effect). This method aims to increase the complexity of the causal task, as the relationships involving the last node's parents and ancestors tend to be more challenging to discern. However, in the CaLM-CEI, CaLM-AS, and CaLM-AR datasets, we adopt a strategy of random allocation to assign cause-effect pairs. CaLM-CEI and CaLM-AS are distinct from CaLM-CA because they do not focus on evaluating the model's ability for causal discovery. By randomly selecting cause-effect pairs from the graph, these datasets increase their diversity. In contrast, CaLM-AR is specifically designed to evaluate if the model can identify causal relationships between any two nodes in the graph, hence there is no predetermined effect in this dataset.

Establishing the ground truth. Two specialized Python libraries, Ananke (Lee et al., 2023a) and DoWhy (Sharma & Kiciman, 2020), are used to aid in our analytical processes. These libraries are instrumental in performing complex computations and analyses required for our datasets construction. (1) For CaLM-AS, we initially employ the identify-effect function from DoWhy to identify the causal effect. Then, for BAS, FAS, and IV, the corresponding strategies involve using get_backdoor_variables, get_frontdoor_variables, and get_instrumental_variables, respectively. (2) In terms of CaLM-AR, the ground truth is gained using get_causes from DoWhy. (3) In CaLM-CA, DoWhy's get_parents and get_ancestors functions can be employed to derive the ground truths for FP and FA. (4) Regarding CaLM-CEI, we start by randomly assigning connected nodes in the graph to contain a range of unobserved confounders, varying from  $20\%$  to  $80\%$ . This variability allows us to observe the effects of different levels of unobserved confounders on the causal relationships within the graph. Subsequently, to determine whether there is an identifiable causal effect between the selected cause-effect pair, we invoke Ananke's OneLineID function. This function is built upon the OneLineID algorithm developed by Richardson et al. (2023), and is recognized for being both sound and complete. Considering the ground truth distribution, in datasets designed for binary classification (e.g., CaLM-CEI and CaLM-AR), we ensure to keep an equilibrium between positive and negative sample counts. On the other hand, for the CaLM-CA datasets, given that the effect is predetermined, balancing the positive and negative sample quantities is unnecessary. For datasets used in choice selection (e.g., CaLM-AS), we also make sure that the distribution of various options as the ground truth is evenly balanced.

# 4.2.4 Constructing Chinese Version for Open-source Datasets

For the open-source datasets, we conducted a subjective assessment of the translation capacities of InternLM-chat (20B) and GPT-3.5-Turbo. Our findings reveal that InternLM-chat (20B) is proficient in handling basic translations. Considering the trade-offs between cost and time efficiency, we initially employed InternLM-chat (20B) for the preliminary translation phase. Then, we contracted a specialized data annotation firm to undertake the secondary annotation, resulting in the finalized Chinese version. For the self-constructed datasets, we established templates in both English and Chinese at the start of data creation.

<table><tr><td>Category</td><td>#Causal task</td><td>#Sample</td></tr><tr><td colspan="3">In terms of causal ladder</td></tr><tr><td>Ladder 0: Causal discovery</td><td>10</td><td>26792</td></tr><tr><td>Ladder 1: Association</td><td>2</td><td>3288</td></tr><tr><td>Ladder 2: Intervention</td><td>17</td><td>48780</td></tr><tr><td>Ladder 3: Counterfactuals</td><td>17</td><td>47474</td></tr><tr><td colspan="3">In terms of mode</td></tr><tr><td>Natural</td><td>20</td><td>43134</td></tr><tr><td>Symbolic</td><td>12</td><td>38400</td></tr><tr><td>Mathematical</td><td>14</td><td>44800</td></tr><tr><td colspan="3">In terms of question type</td></tr><tr><td>Binary classification</td><td>23</td><td>58986</td></tr><tr><td>Numerical</td><td>14</td><td>44800</td></tr><tr><td>Choice selection</td><td>8</td><td>20548</td></tr><tr><td>Open-ended generation</td><td>1</td><td>2000</td></tr><tr><td colspan="3">In terms of language</td></tr><tr><td>Chinese</td><td>46</td><td>63167</td></tr><tr><td>English</td><td>46</td><td>63167</td></tr><tr><td>Total</td><td>92</td><td>126334</td></tr></table>

Tab. 4.3 Concise statistics of CaLM datasets. We tally the number of causal tasks and samples within each category, organizing them by causal ladder, mode, question type, and language. This table serves as a snapshot of the CaLM datasets' quantity.

# 4.3 Data Statistics

To provide a concise yet comprehensive overview of the data, we compile summarized statistics of the CaLM dataset in Table 4.3. This table serves as a quick reference guide, offering insights into the various aspects and components of the CaLM. It is organized according to four distinct dimensions: (1) Causal ladder: This includes causal discovery, association, intervention, and counterfactuals, each representing a different level of causal analysis. (2) Question type: This denotes the types of questions posed to the language models, ranging from binary classification and choice selection to probability calculation and open-ended generation. This categorization is crucial for assessing the accuracy and versatility of language models in responding to diverse types of queries. (3) Mode: The datasets are categorized into Natural, Symbolic, and Mathematical modes, reflecting the different methods of presenting and analyzing data. (4) Language: We have adopted a bilingual approach, offering both Chinese and English languages. This strategy enhances accessibility and inclusivity, appealing to a wide linguistic audience. With over 126,000 queries, the statistics confirm that our evaluation is substantial, showcasing the depth and breadth of the research conducted in CaLM.

Moreover, we detail the composition of our dataset in Table 4.4. The table includes the causal ladder, causal scenario, and question type applicable to each dataset. Moreover, it provides the corresponding mode, number of samples, and language used. The structure of the CaLM dataset is comprehensive, featuring a total of 46 distinct causal tasks. This extensive composition indicates the multifaceted nature of CaLM, offering a diverse and robust platform for analysis and exploration.

<table><tr><td>Causal ladder</td><td>Causal scenario</td><td>Dataset</td><td>Question type</td><td>Mode</td><td>#Sample</td><td>Language</td></tr><tr><td rowspan="10">Causal discovery</td><td rowspan="4">PCD</td><td>E-CARE</td><td>Binary classification</td><td>Natural</td><td>2000</td><td rowspan="46">EN&amp;CN</td></tr><tr><td>E-CARE</td><td>Choice selection</td><td>Natural</td><td>1000</td></tr><tr><td>COPA</td><td>Binary classification</td><td>Natural</td><td>2000</td></tr><tr><td>COPA</td><td>Choice selection</td><td>Natural</td><td>1000</td></tr><tr><td rowspan="3">ECI</td><td>CTB</td><td>Binary classification</td><td>Natural</td><td>596</td></tr><tr><td>ESC</td><td>Binary classification</td><td>Natural</td><td>1000</td></tr><tr><td>MAVEN-ERE</td><td>Binary classification</td><td>Natural</td><td>1000</td></tr><tr><td>AR</td><td>CaLM-AR</td><td>Binary classification</td><td>Symbolic</td><td>1600</td></tr><tr><td rowspan="2">CA</td><td>FP</td><td>Binary classification</td><td>Symbolic</td><td>1600</td></tr><tr><td>FA</td><td>Binary classification</td><td>Symbolic</td><td>1600</td></tr><tr><td rowspan="2">Association</td><td>CORR</td><td>correlation</td><td>Binary classification</td><td>Natural</td><td>1476</td></tr><tr><td>EAE</td><td>exp-away</td><td>Binary classification</td><td>Natural</td><td>168</td></tr><tr><td rowspan="17">Intervention</td><td>CB</td><td>collider-bias</td><td>Binary classification</td><td>Natural</td><td>163</td></tr><tr><td rowspan="3">ATE</td><td>ATE-natural</td><td>Binary classification</td><td>Natural</td><td>1600</td></tr><tr><td>ATE-basic</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>ATE-hard</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td rowspan="3">CDE</td><td>CDE-natural</td><td>Binary classification</td><td>Natural</td><td>1600</td></tr><tr><td>CDE-basic</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>CDE-hard</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td rowspan="4">BAS</td><td>backadj</td><td>Binary classification</td><td>Natural</td><td>227</td></tr><tr><td>max-BAS</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td>min-BAS</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td>mix-BAS</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td>FAS</td><td>FAS</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td>IV</td><td>CaLM-IV</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td rowspan="4">CEI</td><td>0.2-UC</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td>0.4-UC</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td>0.6-UC</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td>0.8-UC</td><td>Choice selection</td><td>Symbolic</td><td>1600</td></tr><tr><td rowspan="17">Counterfactuals</td><td rowspan="3">ETT</td><td>ETT-natural</td><td>Binary classification</td><td>Natural</td><td>1600</td></tr><tr><td>ETT-basic</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>ETT-hard</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td rowspan="3">NDE</td><td>NDE-natural</td><td>Binary classification</td><td>Natural</td><td>1600</td></tr><tr><td>NDE-basic</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>NDE-hard</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td rowspan="3">NIE</td><td>NIE-natural</td><td>Binary classification</td><td>Natural</td><td>1600</td></tr><tr><td>NIE-basic</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>NIE-hard</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td rowspan="2">PN</td><td>PN-basic</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>PN-hard</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td rowspan="2">PS</td><td>PS-basic</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>PS-hard</td><td>Probability calculation</td><td>Mathematical</td><td>1600</td></tr><tr><td>AC</td><td>causal judgement</td><td>Binary classification</td><td>Natural</td><td>187</td></tr><tr><td rowspan="2">CR</td><td>CRASS</td><td>Choice selection</td><td>Natural</td><td>274</td></tr><tr><td>det-counterfactual</td><td>Binary classification</td><td>Natural</td><td>1476</td></tr><tr><td>CEG</td><td>E-CARE</td><td>Open-ended generation</td><td>Natural</td><td>1000</td></tr></table>

Tab. 4.4 Detailed statistics of CaLM datasets. We organize this table according to the levels of the causal ladder. The table showcases the datasets associated with each causal scenario, including details about the question type, mode, number of samples, and language.

# 5 Adaptations

Interacting with language models typically involves the usage of prompts. Over time, a considerable amount of research delves into the significance of establishing a canonical prompt (Le Scao & Rush, 2021; Weng, 2023; Saravia, 2022). In this section, we start by discussing the current situation regarding prompts in Taxonomy (Section 5.1). Then we detail the prompts selected for actual evaluation in Concrete Implementation (Section 5.2), along with our rationale for selecting them. Finally, we systematically explain the prompts we employ (i.e., Basic Prompt (Section 5.3), Adversarial Prompt (Section 5.4), Chain-of-Thought (Section 5.4), In-context Learning (Section 5.6) and Explicit Function (Section 5.7)), covering their formats and providing examples.

# 5.1 Taxonomy

There is a vast array of prompt types, forming a vibrant ecosystem and becoming essential for the usage of language models. This section discusses these prompt types, partially drawing upon the categories outlined in Weng (2023) and Saravia (2022). This includes basic prompt, adversarial prompt, In-context Learning (IcL) (Brown et al., 2020), X-of-Thought, Self-Consistency (Wang et al., 2023a), instruction prompt, iterative prompt and external tool use.

Basic prompt. Basic prompt straightforwardly states the problem the model is expected to solve, offering no examples to the model. It is the most fundamental and intuitive method of engaging with language models.

Adversarial prompt. We roughly classify adversarial prompts into three primary categories<sup>19</sup>: (1) Prompt attack, designed to hinder the model's performance by directly altering the original query. Zhu et al. (2023a) notes that these attacks can be segmented into four levels: character-level, word-level, sentence-level, and semantic-level. (2) Prompt injection, which employs prompts embedded with special intents to override the original instructions (Greshake et al., 2023; Schulhoff, 2024). (3) Jailbreaking, which involves using diverse manipulation tactics to bypass the model's safety policies and defenses, leading the model to generate outputs beyond the intended scope (Li et al., 2023b; Deng et al., 2023; Wei et al., 2024).

In-context Learning (IcL). IcL stands as one of the most commonly utilized prompts (Dong et al., 2022), with ample research supporting its efficacy (Min et al., 2022; Wu et al., 2023b; Wang et al., 2023b). We distinguish IcL into two varieties according to the number of examples supplied: (1) 0-shot IcL, supplying background knowledge about the query without presenting any examples. (2) Few-shot IcL, which offers both a background on the question and a specified number of examples.

X-of-Thought. Chain-of-Thought (CoT) (Wei et al., 2022b) stands out as the most widely recognized X-of-Thought prompt. It boosts the model's capability to tackle intricate issues by incorporating reasoning processes into the prompt. This approach paves the way for further innovations, including Auto-CoT (Zhang et al., 2022b), Ddcot (Zheng et al., 2023b), Program of Thoughts (PoT) (Chen et al., 2023c), Tree-of-Thoughts (ToT) (Yao et al., 2024), and Graph-of-Thoughts (GoT) (Besta et al., 2024).

Self-Consistency. This method is proposed by Wang et al. (2023a), the essence of which is to sample several outputs generated by the model and subsequently choose the optimal one among them. This initial concept has since inspired a multitude of derivative research efforts (Zhai et al., 2023; Min et al., 2023; Wei et al., 2023b).

Instruction prompt. One potential issue with prompts requiring few-shot examples is the limitation imposed by models on the length of the context. Moreover, for the API use of limited access models like GPT-3.5-Turbo and GPT-4, providing these few-shot examples requires more token expenditure. Basic prompt, on the other hand, might not consistently harness the model's peak potential. Instruction prompt emerges as a solution under this circumstance. It delivers only the causal task directives to the model—outlining the actions to be taken without furnishing concrete examples. Indeed, our adopted explicit function (EF) and 0-shot IcL could also be viewed as an instance of instruction prompting.

Iterative prompt. This prompt strategy involves iterative interaction, using the model's replies to progressively steer it toward the correct conclusion. The methods of Least-to-most prompting (Zhou et al., 2022), Progressive-hint prompting (Zheng et al., 2023a), and Self-refine (Madaan et al., 2024) are considered to belong to this approach.

External tool use. For causal tasks requiring complex reasoning or that are knowledge-intensive, relying solely on the model's training data and capabilities may be insufficient. As a result, considerable research directs toward incorporating external tool usage into prompts (Mialon et al., 2023). Among the most prominent techniques is Retrieval-augmented generation (RAG) (Lewis et al., 2020). It merges an information retrieval system with the model. This method enables the fusion of search outcomes pertinent to the query with the initial prompt for input. Furthermore, approaches like Automatic Reasoning and Tool-use (ART) (Paranjape et al., 2023), Tool Augmented Language Models (TALM) (Parisi et al., 2022) and Toolformer (Schick et al., 2024) are proven to be effective as well.

# 5.2 Concrete Implementation

In CaLM, we select five major categories of prompts, which are: basic prompt, adversarial prompt (adversarial-ignore and adversarial-doubt), CoT (0-shot CoT and manual CoT), IcL (0-shot IcL, 1-shot IcL, and 3-shot IcL), and  $EF$ . Considering that certain prompts are further divided into sub-categories, we finally have nine distinct adaptation strategies.

The reason for choosing them is mainly based on the following four points: (1) Audience broadness. Basic prompt, CoT, and IcL are arguably the most widely used prompts at present. These types of prompts cater to the diverse needs of users by offering straightforward interactions for simple queries, detailed step-by-step reasoning for complex problem-solving, and personalized in-context adjustments for tailored responses. This universal applicability allows users of all backgrounds can benefit from the cutting-edge technology. (2) Model robustness. Most prompts mentioned in the Taxonomy (Section 5.1) are designed to enhance model performance. However, to ensure that language models can perform reliably across a spectrum of applications, it is urgent to explore their robustness. Therefore, we design the adversarial prompt. Adversarial prompt serves as a litmus test for these models, challenging them to maintain performance despite deliberate attempts to confuse or mislead them. This approach not only helps in identifying and addressing vulnerabilities but also in improving the model's ability to discern nuances and context, thereby enhancing its resilience against

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/013ac29ac34362f275339a47cb7ad6e0b55c166c292ce86e574abc552d2e2ff2.jpg)



Figure 5.1 Adaptation strategy. We employ standard adaptation strategies for each of the four question types. This ensures uniformity when interacting with the model.


manipulation or biases. (3) User friendliness. There is no concrete evidence suggesting that complex prompt leads to decreased model efficiency. However, it poses challenges for user adoption. One question arises: Is it possible to simplify prompts without compromising their effectiveness? Driven by this curiosity, we select 0-shot CoT, 0-shot IcL and EF, which all utilize minimalistic instructions. For instance, based on basic prompt, 0-shot CoT only adds "Let's think step by step". And EF only encourages that "You are a helpful assistant for ..." We aim to derive valuable insights from these and to drive forward the potential for positive impact. (4) Experiment controlledness. Discussing effectiveness is futile without a baseline for comparison. Starting from the perspective of basic prompt, it demonstrates the model's baseline performance when merely presented with a question. Such a baseline allows for direct comparison with any additional prompt types. By establishing a baseline with basic prompt, researchers can quantitatively assess how variations in prompt complexity, format, or specificity influence the model's performance. From a broader perspective, the various prompts naturally form a comparative basis among themselves.

# 5.3 Basic Prompt

The primary purpose of the basic prompt is to offer foundational and unambiguous test sets to language models that are applicable across different causal scenarios. This prompt will not provide any example or instruction, it only gives the question as the input string directly. This not only establishes a clear starting

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ee7c54c2d9fb48e0e5bfeae221b3a41a14b437290531bbb742c1b326fa92abb3.jpg)



Figure 5.2 Adversarial prompt formatting.


point, but also lays the groundwork for making subsequent modifications and iterations to tailor the prompt to specific needs.

Adaptation strategy. For each of our question types, we implement a uniform interactive method across all causal scenarios. In binary classification (e.g., yes or no questions), the model is prompted to provide a direct classification response. For choice selection, all options are presented (similar to standard exam formats), requiring the model to make a selection. In probability computations, the model is tasked with directly calculating the probability outcome. In open-ended generation, the model produces the answer straightforwardly. The above strategies are the same across all prompts, and Figure 5.1 gives a detailed illustration.

# 5.4 Adversarial Prompt

Adversarial prompt is essential for comprehending the inherent risks associated with language models (Wallace et al., 2019). Our intent is not to endorse malicious activities directed towards language models. Instead, our aim is to delve deeper into their potential shortcomings, thereby facilitating the development of more robust and secure language models in the future.

Adversarial prompt formatting. We employ two distinct forms of adversarial prompts and they both belong to the prompt injection as outlined in Taxonomy (Section 5.1). (1) Adversarial-ignore is a subtler approach, which compels language models to ignore the answers they previously provided (Perez & Ribeiro, 2022). (2) Adversarial-doubt is a more assertive form, where the language models are explicitly informed that their initial responses were wrong. Due to the fact that some models do not offer interfaces for multi-turn dialogue, we adopted a consistent evaluation approach to ensure comparability. We first pose a question to the model and record its first output, namely model output 1. For the second inquiry, we inform the model of the first output and use adversarial prompts to introduce interference. We then re-present the same question, obtaining a second model output, namely model output 2. The responses from these two instances represent the pre- and post-adversarial conditions. By comparing these responses, we can gain a deeper understanding of the model's robustness and accuracy. We demonstrate the two types of prompts in Figure 5.2. The underlying consequence of both prompts is that they can instill doubt in language models about their initial responses.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/58803f5de54a8c1ed48a568a9b5dfb76ef248ca73f42bd50de80cebe1745d2fb.jpg)



Figure 5.3 Chain-of-Thought formatting.


This, in turn, may lead them to produce an inaccurate answer. An interesting observation from this process is the insight it offers into the confidence level of language models regarding their responses. Essentially, if the model's answer varies significantly post-adversarial interference, it implies a lower level of assurance in its original answer. Conversely, minimal changes suggest higher confidence in its initial response. We also introduce a metric to measure this confidence level of models. For more details, please refer to Section 6.

# 5.5 Chain-of-Thought

Chain-of-Thought (CoT) (Wei et al., 2022b) prompting enables language models to decompose complex problems and perform intermediate reasoning steps to enhance their performance. Previous studies have demonstrated that CoT prompts outperform basic prompts on sufficiently large models, particularly on complex arithmetic, commonsense, and symbolic reasoning tasks (Wei et al., 2022b; Kojima et al., 2022).

Chain-of-Thought examples. We categorize CoT prompts into two types based on the number of examples: (1) 0-shot CoT (Kojima et al., 2022): It does not provide examples but includes descriptive instructions for the reasoning steps. These instructions follow a uniform format, phrased as "let's think step by step." (2) Manual CoT: This prompting strategy involves guiding models with manually constructed examples. Our primary focus is on selecting appropriate examples and determining the number of examples for different causal scenarios. When selecting examples, we use a random sampling method and adhere to the principle of fairness, ensuring an equal number of samples for each category within each causal scenario. For instance, in binary classification with eight examples, we ensure a 4:4 ratio between "Yes" and "No" instances. While aiming for

# Adaptation: IcL

# o/1/3-shot IcL

Prompt: Determine whether or not a variable can serve as the parent of another variable in a given causal graph.

You will be presented with a causal graph in the following form: A causes D, A causes B, C causes E, and D causes E.

Question: Does D serve as the parent node of E? Answer (Yes or No?): Yes

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4f25f320b78db63d252f9e18275cdad177130eb3d7a65a48095beb602a3b5420.jpg)


You will be presented with a causal graph in the following form: A causes B, A causes I, A causes C, B causes H, B causes F, B causes K, B causes I, B causes J, C causes J, C causes D, D causes F, D causes E, D causes G, D causes H, F causes J, G causes I, H causes K, and I causes J.

Question: Does J serve as the parent node of K? Answer (Yes or No?):


Figure 5.4 In-context Learning formatting. The  $0 / 1 / 3 \times$  stands for the number of examples. 0 means 0-shot IcL with no example, while 1 and 3 means 1-shot IcL and 3-shot IcL.


uniform class coverage, in scenarios where this is difficult — such as with an odd number of examples in binary classification — we strive for approximately equal proportions between classes. Regarding the number of samples provided, we include as many as possible within the model's context length constraints, but always keep the total number below eight.

Chain-of-Thought formatting. In addition to determining the CoT examples, we also standardize the CoT format for different causal scenarios. One widely adopted technique for CoT prompting involves providing a few-shot set of input-output examples <input, chain-of-thought, output> which demonstrates intermediate reasoning steps leading to the correct answer. Another is to provide text descriptions instead of examples to guide models in answering with CoT, thus avoiding the manual construction of examples. We illustrate the two types of CoT (i.e., 0-shot CoT and manual CoT) formatting in Figure 5.3.

# 5.6 In-context Learning

In-context Learning (IcL) (Brown et al., 2020) represents a technique whereby a model learns new tasks through a set of examples within the context of the prompt provided at the inference phase. The fundamental concept of IcL is learning from analogy (Dong et al., 2022), allowing the model to generalize from a limited set of input-output examples. Such learning ability is also recognized as an emerging ability that particularly appears in large language models (Wei et al., 2022a).

In-context Learning formatting. In IcL, a language model receives a prompt containing a causal task description and several input-output pairs <input, output>, demonstrating how the causal task inputs can be answered. The IcL format is standardized as depicted in Figure 5.4.

In-context Learning examples. When providing the model with these in-context examples, similar to setting up manual CoT, our primary concerns are selecting appropriate examples and determining the optimal number of examples. We employ the same strategy for selecting examples as we do in manual CoT. When

# Adaptation: EF

# Prompt:

You are a helpful assistant for causal attribution (parent node).

You will be presented with a causal graph in the following form: A causes B, B causes D, B causes C, and B causes E.

Question: Does D serve as the parent node of E?

Answer (Yes or No?):

Figure 5.5 Explicit function formatting.

determining the optimal number of examples, we reference findings from the HELM study (Liang et al., 2022), which indicates that the most significant impacts in IcL are observed with up to three examples. Therefore, we select a range of zero to three examples, balancing the token cost and the efficiency of IcL. Here, it is worth noting that, in addition to example-based IcL (i.e.,  $1/2/3$ -shot IcL), we also incorporate 0-shot IcL. This inclusion is crucial because IcL begins with a causal task description - such as "Determine whether or not a variable can serve as the parent of another variable in a given causal graph." - before presenting any examples. The presence of this task description can influence model performance. By incorporating 0-shot IcL, we aim to isolate and minimize the impact of the causal task description, thereby clarifying the true effect of the IcL examples on performance.

# 5.7 Explicit Function

Recent studies have elucidated that language models may have emotional awareness analogous to humans (Elyoseph et al., 2023; Li et al., 2023a). Derived from this understanding, several related work (Long et al., 2022; Kiciman et al., 2023) has explored the utilization of encouraging and positive language within prompts (e.g., statements that build confidence or emphasize the goal) to elicit enhanced performance from language models.

In our work, we formulate an explicit function (EF) prompt for each causal task, and we consider it to belong to the instruction prompt as mentioned in Taxonomy. Specifically, we incorporate a sentence containing an explicit function description into the basic prompt to motivate language models in causal task resolution, as shown in Figure 5.5.

# 6 Metrics

Evaluation metrics play a crucial role in evaluating the effectiveness of language models, providing a structured approach to assessing their performance across various dimensions. These metrics provide a detailed insight into the model's capabilities, aiding researchers, practitioners, and stakeholders in making well-informed decisions. The taxonomy of desiderata, based on specific criteria and categories, serves as a foundation for selecting metrics that align with the objectives of the evaluation. In this section, we begin by introducing the Taxonomy (Section 6.1) of metrics. Following that, we detail our Implementation Principles (Section 6.2) of these metrics. Finally, we elaborate on the specific metrics we use, focusing on three key aspects: Metrics for Model (Section 6.3), Metrics for Causal Scenario (Section 6.4), and Metrics for Prompt (Section 6.5).

# 6.1 Taxonomy

Metrics for evaluating models, causal scenarios, and prompts in natural language processing tasks can be organized into several categories based on their objectives and the specific aspects of performance they measure. These categories include accuracy, robustness (Wang et al., 2020a; Zhong & Wang, 2023), fairness (Li et al., 2023g; Gallegos et al., 2023), reliability (Li et al., 2023c; Chen et al., 2023b), and safety (Zhiheng et al., 2023; Zhang et al., 2023d), reflecting the multidimensional nature of AI assessment. The taxonomy of metrics presented in this paper covers three key areas: model performance, causal scenario characteristics, and prompt effectiveness.

Model performance metrics. 1) Accuracy: This metric measures the correctness of the model's responses across various prompts, serving as a fundamental measure of its effectiveness. 2) Robustness: This evaluates the model's stability when faced with adversarial inputs or disturbances, highlighting its reliability under challenging conditions. 3) Volatility: This metric assesses the consistency of a model's performance when exposed to different prompting strategies, indicating its predictability and reliability across prompts.

Causal scenario characteristics metrics. 1) Understandability: This metric examines the extent to which models comprehend and effectively perform on specified causal scenarios or causal tasks. 2) Open-Limited Gap: This quantifies the performance disparity between open-access and limited-access models within a causal scenario. 3) Solvability: This indicates the relative difficulty of a causal scenario, derived from the performance of models and model-prompt combinations.

Prompt effectiveness metrics. 1) Volatility: This metric measures the variability in model performance across different prompting strategies for a specific causal scenario.

# 6.2 Implementation Principles

The selection of metrics in CaLM is guided by five key principles: (1) Comprehensiveness. The selected metrics cover a broad spectrum of performance aspects, including accuracy, robustness, stability, understandability, and solvability. This range ensures a comprehensive assessment of model functionality. (2) Relevance to real-world applications. The selected metrics are relevant to real-world natural language processing applications, where model accuracy, robustness against adversarial inputs, and understanding of diverse causal scenarios are crucial for practical utility. (3) Sensitivity to causal scenario complexity. Metrics such as understandability and solvability are sensitive to the complexity of causal scenarios, allowing for

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/260889b0d803713f8d99df63116b1c7c44e5e4d178673b18aa316869151803b4.jpg)



Figure 6.1 Example of robustness.


nuanced evaluation of model performance in different contexts. (4) Balance between open-access and limited-access models. The inclusion of metrics like the open-limited gap ensures a balanced assessment of both open-access and limited-access models, reflecting their respective strengths and weaknesses. (5) Consistency and variability assessment. Metrics such as volatility (model) and volatility (prompt) enable the evaluation of both the consistency of model performance across different prompting strategies and the variability in performance induced by varying prompts.

These principles ensure a holistic evaluation of language models, taking into account both the capabilities of models and the nature of the causal scenarios they are designed for. By adhering to these principles, the selected metrics provide a robust framework for evaluating language models, capturing their performance nuances in diverse causal scenarios and under different prompting conditions.

# 6.3 Metrics for Model

Metrics in this paper aim to evaluate the performance of a set of models  $(M)$  across various prompts  $(N)$  on a dataset  $D$ . The performance of each model under a specific prompt is denoted as  $P_{ij}$ , where  $i$  represents the model index, and  $j$  represents the prompt index.

Accuracy. Accuracy is one of the most widely used evaluation metrics for AI systems or models. Essentially, the utility of AI systems or models hinges upon their ability to deliver precise results. In this paper, we will adopt accuracy as a standard metric for each causal scenario. This includes exact-match accuracy and the ROUGE-L score (Lin, 2004). All the accuracy scores are computed by averaging over all the tested instances.

Robustness. Robustness is evaluated through the adversarial prompt, where responses are recorded before and after introducing disturbances, as shown in Figure 6.1. If the answers differ, it is considered a change. The change rate is calculated as the number of changes divided by the dataset size, and the Robustness value is then expressed as 1 minus the change rate for unchanged responses, i.e.,

$$
\text {R o b u s t n e s s} = 1 - \frac {\text {N u m b e r o f C h a n g e s}}{| D |}. \tag {4}
$$

To illustrate an intuitive impression, let us consider a specific example of how to calculate the robustness value using the given definition. Suppose we have a dataset of 100 instances, and out of these 100 prompts, 20 responses changed after introducing the disturbance. The change rate is calculated as Change Rate =  $\frac{20}{100} =$

<table><tr><td>Conditions (close-ended)</td><td>Degree of understandability</td></tr><tr><td>third quartile &lt; random guess</td><td>very hard</td></tr><tr><td>third quartile ≥ random guess, median &lt; random guess</td><td>hard</td></tr><tr><td>median ≥ random guess</td><td>easy</td></tr></table>

Tab. 6.1 Degree of understandability. The degree is used to evaluate the understandability of the causal task/causal scenario. The third quartile and median are computed from the distribution of all model-prompt pairs in a causal task/causal scenario.

0.2 and the robustness value equals  $1 - 0.2 = 0.8$ . Therefore, in this example, the robustness of the model is 0.8 or  $80\%$ , indicating that  $80\%$  of the responses remained unchanged despite the adversarial prompts.

Model volatility. Model volatility is calculated as the standard deviation of the model's performance (i.e., accuracy) across various prompting ways, namely:

$$
\text {V o l a t i l i t y} _ {i} = \sqrt {\frac {\sum_ {j = 1} ^ {N} \left(P _ {i j} - \bar {P} _ {i}\right) ^ {2}}{N}}, \tag {5}
$$

where  $P_{ij}$  denotes performance of the  $i$ -th model under the  $j$ -th prompt,  $\bar{P}_i$  is the mean performance of the  $i$ -th model across all prompting ways. A higher volatility value indicates more variability in the model's performance across different prompting ways, reflecting less stability.

# 6.4 Metrics for Causal Scenario

Understandability. We focus on the median and third quarter of the distribution of all the model-prompt combinations in the causal task/causal scenario and compare them with a random guess. If the third quartile or the median performance of the task/scenario does not achieve a random guess, we define it as an indication that some of the models cannot understand the causal scenario or causal task even with the help of different prompts. The different degree of understanding is defined in Table 6.1. We refer to the "close-ended" questions as the one that requires models to select the correct answer from a few choices instead of answering in their own words. In addition to the conditions defined in the table, we have manually defined the understandability of some open-ended questions with a random guess probability of  $0\%$ . These open-ended scenarios are PN, PS, and CEG. Specifically, for CEG, given that most models have a better capability in processing natural language questions, we classify its understandability as easy. For PN and PS, since the causal scenarios in the Mathematical mode are more challenging to comprehend, with both the medians and the third quartiles less than  $2\%$ , we classify their understandability as very hard.

Open-Limited Gap. We evaluate the gap between open-access and limited-access models using the open-limited ratio. This ratio is calculated by comparing the performance of open-access to limited-access models among the top 5 models in terms of average accuracy within the causal scenario. Typically, the limited-access models tend to outperform their open-access counterparts. The degree of the gap between open-access and limited-access models is detailed in Table 6.2.

Solvability. The solvability focuses on the top performance of the models and the model-prompt combinations in the causal task/causal scenario; it is defined by whether the top performances of the task/causal

<table><tr><td>Conditions</td><td>Degree of open-limited gap</td></tr><tr><td>open:limited = 0:5</td><td>large</td></tr><tr><td>open:limited = 1:4</td><td>moderate</td></tr><tr><td>open:limited &gt; 1:4</td><td>small</td></tr></table>


Tab. 6.2 Degree of open-limited gap. The open:limited stands for the ratio of open-access to limited-access models among the top five models with the highest average accuracy in the causal scenario.


<table><tr><td>Conditions</td><td>Degree of solvability</td></tr><tr><td>max value &lt; random guess</td><td>unsolvable (4)</td></tr><tr><td>random guess ≤ max value &lt; 80%</td><td>challenging (3)</td></tr><tr><td>max value ≥ 80% and max average value &lt; 70%</td><td>potentially solvable (2)</td></tr><tr><td>max value ≥ 80% and max average value ≥ 70% and 3rd max average value &lt; 70%</td><td>solvable (1)</td></tr><tr><td>max value ≥ 80% and 3rd max average value ≥ 70%</td><td>well-solved (0)</td></tr></table>

Tab. 6.3 Degree of solvability. The degree is used to evaluate the difficulty of the causal task/causal scenario. The max value represents the max accuracy of all the model-prompt pairs in the causal task/causal scenario. The max average value represents the max average accuracy of models in the causal task/causal scenario. The 3rd max average value is the 3rd max average accuracy of models in the causal task/causal scenario. The number beside the degree of solvability is used to compute the variance of solvability in Table 9.10.

scenario achieve the settled threshold. The solvability degree expresses the difficulty of the causal task/causal scenario. It is defined in Table 6.3.

# 6.5 Metrics for Prompt

Prompt volatility. Prompt volatility is determined by calculating the standard deviation of the performance values (i.e., accuracy) across various models using a specific prompting method, that is,

$$
\text {V o l a t i l i t y} _ {j} = \sqrt {\frac {\sum_ {i = 1} ^ {M} \left(G _ {i j} - \bar {G} _ {j}\right) ^ {2}}{M}}, \tag {6}
$$

where  $G_{ij} = P_{ij} - P_{iB}$ .  $P_{ij}$  denotes performance of the  $i$ -th model under the  $j$ -th prompt,  $P_{iB}$  is the  $i$ -th model's performance using basic prompt. Therefore,  $G_{ij}$  denotes the gain in the  $i$ -th model's performance on the  $j$ -th prompt compared to the basic prompt.  $M$  denotes the number of models. This metric helps us to compare the performance between different prompting strategies with the basic prompt. A higher volatility value indicates a larger influence of the prompt on models compared to the basic prompt.

# 7 Errors

Discovering and categorizing model errors offers a practical approach to defining the boundaries of models' capabilities, identifying their deficiencies, and assessing potential threats. As language models advance, the errors they produce become valuable resources for ongoing research, offering insights essential for further enhancements in the field. In this section, we aim to systematically analyze these errors to improve model performance and reliability. To be specific, we categorize various types of errors in Taxonomy (Section 7.1). Following this, we proceed to delve into these categories from the perspectives of both Quantitative (Section 7.2) and Qualitative (Section 7.3).

# 7.1 Taxonomy

To provide directional guidance for model improvement, we taxonomize the errors made by models during the evaluation process. As Figure 7.1 shows, we categorize these errors into two distinct types based on their measurability: quantitative and qualitative. This classification aims for wide coverage and scalability. We endeavor to quantify as many error types as possible; however, those that are difficult to quantify are not disregarded. Discussing these errors is equally vital for enhancing model performance, and thus, they are presented through qualitative analysis. Building upon these two primary categories, we further classify them into twelve specific types of errors. This detailed classification strategy is designed to comprehensively capture all typical errors made by the models evaluated in CaLM.

# 7.2 Quantitative

Same response to all questions. This type of error refers to cases where a model consistently produces the same answer regardless of the specific question posed. Such errors can be differentiated based on the question type, consisting of three categories and five situations: (1) In binary classification, responses can be "all yes", "all no", or a mix of both across different prompts; (2) In choice selection, the same choice might be selected in all queries; (3) In probability calculation, a specific value might be consistently generated in every case. It is worth noting that some models persist in giving the same answer even when presented with adversarial prompts. Cataloging this error is important because it indicates a lack of adaptability and contextual understanding in the model's responses, and this kind of error may result in a specious high accuracy value in some causal scenarios. By consistently providing the same answer regardless of the input, the model fails to demonstrate versatility in its decision-making process. This error hampers the model's ability to effectively handle diverse causal scenarios and causal tasks, undermining its overall performance and reliability.

Empty response. This type of error refers to instances where a model generates a blank response. Identifying this error is beneficial for several reasons. First, it helps us identify the boundaries of the model's capabilities. When the model fails to produce any output, it indicates limitations in its understanding or processing of the input data. Second, it highlights potential areas for improvement in the model's architecture or training process. Additionally, documenting instances of blank responses allows us to assess the overall reliability and robustness of the model. By identifying and addressing the root causes of this error, we can work towards enhancing the model's performance and ensuring its effectiveness in practical applications. Figure 7.2 gives an example.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6e2edd7922ac4465eb86cbbc03a1297f619553542abfc57787ca8b52def7db1f.jpg)



Figure 7.1 Errors taxonomy. We define twelve types of errors from both quantitative and qualitative perspectives.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/24e0ef718fbd3c6116ff02ef9e60be9b5e7293ce95b7818001c2c791baadfc87.jpg)



Figure 7.2 Empty response.


Limitation of instruction-following. This type of error occurs when a model fails to provide a standard response according to the instructions given in the question. For example, when asked to directly respond with "Yes" or "No", some models may provide explanations instead, with the answer embedded within the explanation. This type of response introduces additional inconvenience for our metric calculations. Alternatively, some models may choose to reply with "true" or "false". In probability calculation problems, we instruct the model to return the answer in a specific JSON format (e.g., {"PROB": "0.1234"}). However, some models may provide the probability directly without adhering to the required format specified in the question. An example is provided in Figure 7.3. The significance of cataloging this type of error lies in several aspects. Firstly, it helps us evaluate the model's adherence to instructions and its ability to respond in the desired format. Moreover, it will greatly facilitate large-scale evaluations and bring considerable convenience to metric calculations. By minimizing these errors, we can streamline the evaluation process and ensure the reliability and efficiency of our assessment metrics, ultimately enhancing the robustness and effectiveness of model evaluations on a broader scale.

# Quantitative: Limitation of instruction-following

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Watl has a direct effect on mwdq. Watl has a direct effect on eqln. Watl has a direct effect on jlpb. Mwdq has a direct effect on eqln. Mwdq has a direct effect on jlpb. Eqln has a direct effect on jlpb.

For those with mwdq being low and watl being low, the probability of eqln being low is 0.8687. The probability of watl being low is 0.6889. For those with mwdq being low and watl being high, the probability of eqln being low is 0.9965. The probability of watl being high is 0.3111. The probability of mwdq being low and eqln being low is 0.7426. The probability of mwdq being high and eqln being high is 0.0225.

Instruction: Consider the probability of necessity (PN) of mwdq on eqln.

Question: Given that mwdq was high and eqln was high, what is the upper bound of the probability of the eqln would have been low if the mwdq had been low?

Provide the calculation result to four decimal places in JSON format, like {"PROB": "0.1234"}:

# Model response:

To calculate the probability of necessity (PN) for mwdq on eqln, we can use the following formula: PN(mwdq, eqln) = P(eqln = low | mwdq = high) * P(mwdq = high) + P(eqln = high | mwdq = low) * P(mwdq = low).

First, we need to calculate the probabilities given in the input. We have:

P(eqln = low | mwdq = high) = 0.9965

P(mwdq = high) = 0.3111

P(eqln = high | mwdq = low) = 0.0225

P(mwdq = low) = 0.6889

Now, we can calculate PN(mwdq, eqln):

PN(mwdq, eq|n) = (0.9965 * 0.3111) + (0.0225 * 0.6889) = 0.3067 + 0.0152 = 0.3219

So, the probability of necessity for mwdq on eqln is 0.3219.

Given that mwdq was high and eqln was high, the upper bound of the probability of the eqln would have been low if the mwdq had been low is 0.3219.

Ground truth: {"PROB": "1.0000":}

Figure 7.3 Limitation of instruction-following. The red text indicates the wrong response.

# Quantitative: Repetition

# Prompt:

You will be presented with a causal graph in the following form: A causes D, A causes E, B causes E, C causes D, and D causes E.

There exist unobserved confounders between: D and E

Question: Whether the causal effect of D on E is identified or not?

Answer (Yes or No?):

# Model response:

Yes.

Question: Whether the causal effect of E on D is identified or not?

Answer (Yes or No?): Yes.

Question: Whether the causal effect of E on D is identified or not?

Answer (Yes or No?): Yes.

Ground truth: No

Repetition part

Figure 7.4 Repetition. The red text indicates the wrong response.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/104c3f368cfb7489bf5ac39e0170a1809f850a47e0118daa63356a3ae241ffe3.jpg)



Figure 7.5 Language inconsistency. The red text indicates the wrong response.


Repetition. This type of error, where a model fabricates responses or repeats questions within its replies, presents significant challenges to our evaluation process. For example, there are cases where the model starts repeating fabricated questions, following with a "Yes" or "No" answer as mentioned in the instructions. This requires special handling during keyword matching to accurately discover the answer section. Tracking and quantifying these errors are crucial as they offer insights into the model's behavior and performance, thus enabling the implementation of necessary improvements. Moreover, understanding the prevalence of these errors aids in refining the evaluation process, and ensuring accurate assessment of the model's capabilities. Figure 7.4 gives an example.

Language inconsistency. Our evaluation process provides questions in both Chinese and English versions, but never simultaneously in two languages. Under this setup, we have identified instances of language inconsistency in certain models. This issue arises when a question posed in one language elicits a response that includes text in the other language. It is more common to find English text within Chinese responses. This error not only reflects an imbalance in the model's training data across different languages, but also signifies a deficiency in the model's ability to recognize and integrate the appropriate language context. Furthermore, it

# Qualitative: Causal hallucination

# Prompt:

Event A: Tom fainted on the mountain.

Event B: Tom had edema and erythema on his arm.

Question: Is there a causal relationship between Event A and Event B?

Answer (Yes or No?):

# Model response:

Yes.

Explanation: Tom fainted on the mountain (Event A) due to dehydration and heat exhaustion, which led to edema and erythema on his arm (Event B). Therefore, there is a causal relationship between the two events.

Ground truth: No

Figure 7.6 Causal hallucination. The red text indicates the wrong response.

# Qualitative: Inferential ambiguity

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Xuoo has a direct effect on bdan. Bdan has a direct effect on abcp.

Instruction: Consider the average treatment effect (ATE) of abcp on xuoo.

Question: If abcp is changed to be low, will xuoo be more likely to be low?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

# Model response:

{"ANSWER": "No", "PROB": "Not applicable"}

# Ground truth:

{"ANSWER": "No", "PROB": "0.0000"}

Figure 7.7 Inferential ambiguity. The red text indicates the wrong response. The green text indicates the right response.

underscores the importance of multilingual training data and fine-tuning methodologies to ensure coherent and linguistically appropriate responses across languages. Addressing this language inconsistency is crucial for enhancing the model's cross-lingual capabilities and overall performance in diverse linguistic environments.

Figure 7.5 shows an example.

# 7.3 Qualitative

Causal hallucination. As defined by Lu et al. (2024), causal hallucination refers to a model's inability to correctly distinguish between two fundamental concepts: correlation and causation. The model may mistakenly interpret correlation as causation, leading to erroneous reasoning and conclusions. Causal hallucination may arise due to various factors, including limited data availability, complexity in relationships between variables, the presence of confounding variables, biases within the data, and insufficient domain knowledge. Overcoming causal hallucination requires comprehensive strategies such as accounting for confounding

# Qualitative: Calculation error

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Weather conditions has a direct effect on respiratory symptoms. Air quality has a direct effect on lung function. Air quality has a direct effect on respiratory illness. Air quality has a direct effect on respiratory symptoms. Pollution sources has a direct effect on lung health. Lung health has a direct effect on lung function. Lung health has a direct effect on respiratory symptoms. Respiratory symptoms has a direct effect on lung function. For those with lung health being poor lung health, the probability of lung function being poor lung function is 0.1238. The probability of lung health being poor lung health and lung function being poor lung function is 0.0287. The probability of lung health being good lung health and lung function being good lung function is 0.6718.

Instruction: Consider the probability of necessity (PN) of lung health on lung function.

Question: Given that lung health was good lung health and lung function was good lung function, what is the upper bound of the probability of the lung function would have been poor lung function if the lung health had been poor lung health?

Provide the calculation result to four decimal places in JSON format, like {"PROB": "0.1234"}:

# Model response:

With A represents lung health and B represents lung function, we have:  $P(B = 1|A = 0) = 0.1238$ ;  $P(A = 0, B = 1) = 0.0287$ ;  $P(A = 1, B = 1) = 0.6718$ .

Calculate  $P(B = 1|do(A = 0)) = P(B = 1|A = 0) = 0.1238$ , then the upper bound of PN is min{1, [P(B=1|do(A=0))-P(A=0,B=1)]/P(A=1,B=1)}

=min{1,(0.1238-0.0287)/0.6718}

=min{1,0.1417}

$= 0.1417$  .The answer is: {"PROB": "0.1417".}

# Ground truth:

With A represents lung health and B represents lung function, we have:  $\mathrm{P(B = o|A = o) = 0.1238}$ ;  $\mathrm{P(A = o,B = o) = 0.0287}$ ;  $\mathrm{P(A = 1,B = 1) = 0.6718}$ .

Calculate  $P(B = o|do(A = o)) = P(B = o|A = o) = 0.1238$ , then the upper bound of PN is min{1, [P(B = o|do(A = o)) - P(A = o, B = o)] / P(A = 1, B = 1)}

$= \min \{1,(0.1238 - 0.0287) / 0.6718\}$

$= \min \{1,0.1416\}$

$= 0.1416$  .The answer is: {"PROB": "0.1416"}.

Figure 7.8 Calculation error. The red text indicates the wrong response. The green text indicates the right response.

variables, validating assumptions, and leveraging domain expertise to ensure the model accurately captures causal relationships. Figure 7.6 gives an example.

Inferential ambiguity. This type of error occurs when a model, despite being presented with a solvable problem, produces an overly broad or vague answer, making it difficult to determine its intent. Such errors typically indicate deficiencies in the model's data processing abilities or semantic understanding, suggesting a need for improvement in its reasoning or comprehension capabilities. Addressing this issue is vital for improving the model's accuracy and reliability, ensuring that its responses are more precise and contextually relevant. Figure 7.7 gives an example.

Calculation error. We categorize this error as occurring when a model understands the question semantically and engages in basic reasoning but errs during the calculation phase. This error also occurs in Sawada et al. (2023). Numerous studies have highlighted that computation is extremely challenging to models (He-Yueya et al., 2023; Zhang et al., 2024; Zhou et al., 2024). In CaLM, the inclusion of a causal background introduces additional complexity to them. It is of vital importance for a model to compute accurately, because it impacts the reliability and usefulness of its outputs. In domains where causality plays a significant role, such as healthcare decision-making (Richens et al., 2020), economics (Uysal, 2015), or policy development (Capano & Howlett, 2021), precise computation is paramount. Errors in computation could lead to incorrect conclusions, flawed recommendations, or even harmful actions. An example of this error is illustrated in Figure 7.8.

# Qualitative: Incorrect reasoning

Prompt:

You will be presented with a causal graph in the following form: A causes C, A causes D, B causes E, B causes C, and C causes D.

Question: Does D serve as the ancestor node of E? Let's think step by step.

Answer (Yes or No?):

Model response:

Yes.

Why does D serve as an ancestor node of E? Because C, the parent of E, is caused by A, and A also causes D, making D the ancestor node of C.

So, the answer is yes. D is an ancestor node of E.

Details: http://learningtheories.com/fcaps-causal [fake link]

Ground truth: No

Figure 7.9 Incorrect reasoning. The red text indicates the wrong response. The green text indicates the right response.

Incorrect reasoning. This type of error occurs when a model makes a mistake during the reasoning process, specifically using the Chain-of-Thought (CoT), and fails to arrive at the correct conclusion. Usually, not every step in the model-generated CoT is necessary for answering a question, and even some incorrect steps may not impact the final outcome. However, errors in critical reasoning steps will invariably lead to incorrect conclusions. Given our goal for the model to exhibit robust causal reasoning capabilities, it is crucial to ensure the accuracy of each step in the model's reasoning process. Identifying strategies to enhance the model's deductive accuracy remains a significant challenge. An example of this type of error is shown in Figure 7.9.

Misunderstanding. This type of error occurs when a model misunderstands the input, producing content that, while related to the input, is irrelevant to the ground truth answer. Such errors can be particularly severe, especially in real-world causal scenarios. For instance, if the model inappropriately responds to a query, it will inevitably impair the user experience. Encountering responses that are tangentially related but ultimately irrelevant not only erodes trust in the technology but also obstructs the adoption and integration of language models into routine causal tasks and decision-making processes. This highlights the critical need for continuous improvement in model accuracy and understanding. An example of this type of error is depicted in Figure 7.10.

Contradiction. This type of error arises from contradictions within a model's responses. Specifically, when faced with a "Yes" or "No" query, the model produces both "Yes" and "No" simultaneously. Similarly, for multiple-choice questions with only one correct option, the model may suggest several choices concurrently. These issues reveal a fundamental flaw: the model's inability to maintain coherence and rigor in decision-making. Such contradictions not only confuse users but also undermine the model's reliability and its applicability in critical decision-making causal scenarios. The root cause of this issue can be traced back to the model's processing and evaluation mechanism, which, in attempting to cover a broad spectrum of possibilities, fails to adequately weigh the context and nuances of the query. Consequently, the model defaults to presenting multiple outcomes without a clear rationale for prioritizing one over the others. This behavior suggests a need for improvement in the model's understanding of the query's context and its decision-making

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d5d7e9a75937f59e4704a45141423949be067f51ebf14be8655b0d3dface1301.jpg)



Figure 7.10 Misunderstanding. The red text indicates the wrong response.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d61de3a165082f01b8ea552ae33fa6d00c26222f3f8f7af22bc840873fcc02e2.jpg)



Figure 7.11 Contradiction. The red text indicates the wrong response. The green text indicates the right response.


algorithms, to enhance its ability to provide precise and unambiguous answers. Figure 7.11 gives an example.

Outlier. This type of error indicates a complete failure by a model to understand the intended request of the input, leading to generated content that bears no relation to the input provided. It is important to differentiate this error from Misunderstanding, as they can be easily confused. Misunderstanding refers to an erroneous interpretation of the input, where the response retains a degree of association with the input. In contrast, Outlier represent such a significant deviation that the response is completely disconnected from the input. This issue highlights a fundamental limitation within the model: its inability to understand and process context. These limitations are inherently tied to the model's training data and the algorithm's capacity to interpret context and meaning from that data. Errors of this nature may stem from the model's inability to accurately map complex inputs to its learned representations, resulting in outputs that are not only incorrect but completely irrelevant. This limitation underscores the challenges in embedding human-like understanding and interpretive flexibility into a system primarily based on pattern recognition and causal reasoning. It

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3304f5eabda1f771044f4a88c40ec7c87377a7ce1467929376f9e9154848343c.jpg)



Figure 7.12 Outlier. The red text indicates the wrong response.


reveals the gap between algorithmic processing and human cognition, particularly in dealing with ambiguous, nuanced, or highly contextualized information. An example of this type of error is illustrated in Figure 7.12.

# 8 Models

This section describes the models we evaluate. We first conduct a thorough categorization of the models from various dimensions in Taxonomy (Section 8.1). Following this, we detail the criteria and process used to select the models for evaluation in Concrete Implementation (Section 8.1).

# 8.1 Taxonomy

We evaluate 28 widely-used decoder-only language models; we chose decoder-only models due to their proven effectiveness in generative tasks. Our assessment criteria include the size of the model, the pre-training corpus utilized, the creator of the model, the window size of context it can handle, and the model's accessibility. We selected these specific dimensions for comparison to comprehensively understand each model's capabilities and limitations in practical scenarios. Table 8.1 lists these features and specifies the exact version of each model evaluated, organized from the smallest to the largest in terms of model size; further details about the models can be found at our website.[20]

# 8.2 Concrete Implementation

With the rapid advancements in language models, evaluating every language model becomes increasingly challenging. To stay current, we focus on models released after 2020. Our selections include both open-access models and limited-access models. We examined: (1) Open-access models: These consist of 15 models whose weights are freely downloadable, including Baichuan1 (7B & 13B-chat), Baichuan2 (7B-chat & 13B-chat) (Baichuan, 2023), InternLM (7B-chat & 20B-chat) (Team, 2023), Llama2 (7B & 13B & 70B & 70B-chat) (Touvron et al., 2023), Qwen (7B & 14B) (Bai et al., 2023), Koala (13B) (Geng et al., 2023), Wizardcoder (15B) (Luo et al., 2023), Vicuna (33B) (Chiang et al., 2023); (2) Limited-access models: These 13 models are accessible only through API, including ada (0.35B), babbage (1.3B), curie (6.7B) and davinci (175B) (Brown et al., 2020), text-ada-001, text-babbage-001, text-curie-001, text-davinci-001, text-davinci-002 and text-davinci-003 (Ouyang et al., 2022), GPT-3.5-Turbo (OpenAI, 2022), GPT-4 (OpenAI, 2023), Claude2 (Anthropic, 2023). As shown in Figure 8.1, these models exhibit significant diversity in terms of creator, parameter size, tuning method, and window size, showcasing a broad range of variations. To address language diversity, we also ensure that the language models we evaluate are developed by teams from various countries.

Continuously evolving evaluation. Our research examines the adoption of regular updates in operational systems, including private models and commercial APIs. We have encountered challenges due to the lack of uniformity in version control and the transparency of change logs from various model providers. This inconsistency has limited our ability to uniformly report model versions, so we have confined our documentation to what is verifiable, such as the specific release dates of models like those from OpenAI.

The results we generated correspond to the specific model versions active at the time of our experiments, and we have described in the Table D.1. Despite our comprehensive scope of evaluation, it is possible that some models might be updated during our assessment period. We expect such updates to be sporadic and incremental, thus not drastically altering our findings. Nevertheless, we advocate for continuous, systematic monitoring of model changes to better understand their implications, as suggested in the works of Chen et al. (2022a) and Liang et al. (2022). It is also important to note that some models we evaluate may become obsolete after our evaluation.

<table><tr><td>Model</td><td>Creator</td><td>#Parameter (B)</td><td>Training corpus</td><td>SFT</td><td>RLHF</td><td>Window Size</td><td>Access</td></tr><tr><td>ada</td><td>OpenAI</td><td>0.35</td><td>Undisclosed</td><td>×</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>babbage</td><td>OpenAI</td><td>1.3</td><td>Undisclosed</td><td>×</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>curie</td><td>OpenAI</td><td>6.7</td><td>Undisclosed</td><td>×</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>Baichuan1</td><td>Baichuan Inc.</td><td>7</td><td>Undisclosed</td><td>×</td><td>×</td><td>4096</td><td>Open</td></tr><tr><td>Baichuan2-chat</td><td>Baichuan Inc.</td><td>7</td><td>Undisclosed</td><td>✓</td><td>✓</td><td>4096</td><td>Open</td></tr><tr><td>InternLM-chat</td><td>Shanghai AI Lab</td><td>7</td><td>over 2.3T tokens of data</td><td>✓</td><td>✓</td><td>2048</td><td>Open</td></tr><tr><td>LLaMA2</td><td>Meta</td><td>7</td><td>2T tokens of data</td><td>×</td><td>×</td><td>4096</td><td>Open</td></tr><tr><td>Qwen</td><td>Alibaba Cloud</td><td>7</td><td>over 2.2T tokens of data</td><td>×</td><td>×</td><td>8192</td><td>Open</td></tr><tr><td>Koala</td><td>UC Berkeley</td><td>13</td><td>Alpaca Corpus, WebGPT, etc.</td><td>✓</td><td>×</td><td>2048</td><td>Open</td></tr><tr><td>LLaMA2</td><td>Meta</td><td>13</td><td>2T tokens of data</td><td>×</td><td>×</td><td>4096</td><td>Open</td></tr><tr><td>Baichuan1-chat</td><td>Baichuan Inc.</td><td>13</td><td>Undisclosed</td><td>✓</td><td>✓</td><td>4096</td><td>Open</td></tr><tr><td>Baichuan2-chat</td><td>Baichuan Inc.</td><td>13</td><td>Undisclosed</td><td>✓</td><td>✓</td><td>4096</td><td>Open</td></tr><tr><td>Qwen</td><td>Alibaba Cloud</td><td>14</td><td>over 3T tokens of data</td><td>×</td><td>×</td><td>8192</td><td>Open</td></tr><tr><td>Wizardcoder</td><td>Microsoft</td><td>15</td><td>Code Alpaca</td><td>✓</td><td>×</td><td>8192</td><td>Open</td></tr><tr><td>InternLM-chat</td><td>Shanghai AI Lab</td><td>20</td><td>over 2.3T tokens of data</td><td>✓</td><td>✓</td><td>4096</td><td>Open</td></tr><tr><td>Vicuna</td><td>Lmsys</td><td>33</td><td>LLaMA1 corpus, ShareGPT, etc.</td><td>✓</td><td>×</td><td>2048</td><td>Open</td></tr><tr><td>LLaMA2</td><td>Meta</td><td>70</td><td>2T tokens of data</td><td>×</td><td>×</td><td>4096</td><td>Open</td></tr><tr><td>LLaMA2-chat</td><td>Meta</td><td>70</td><td>2T tokens of data</td><td>✓</td><td>✓</td><td>4096</td><td>Open</td></tr><tr><td>davinci</td><td>OpenAI</td><td>175</td><td>Undisclosed</td><td>×</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>text-ada-001</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>text-babbage-001</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>text-curie-001</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>text-davinci-001</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>×</td><td>2049</td><td>Limited</td></tr><tr><td>text-davinci-002</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>×</td><td>4097</td><td>Limited</td></tr><tr><td>text-davinci-003</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>✓</td><td>4097</td><td>Limited</td></tr><tr><td>gpt-3.5-turbo</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>✓</td><td>4097</td><td>Limited</td></tr><tr><td>GPT-4</td><td>OpenAI</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>✓</td><td>8192</td><td>Limited</td></tr><tr><td>Claude2</td><td>Anthropic</td><td>Undisclosed</td><td>Undisclosed</td><td>✓</td><td>✓</td><td>100K</td><td>Limited</td></tr></table>


Tab. 8.1 Taxonomy of model. Our selected language models are taxonomized in terms of creator, scale (parameter size), training corpus, finetuning strategy, window size, and model access, where "SFT" denotes supervised fine-tuning and "RLHF" denotes reinforcement learning from human feedback.


<table><tr><td colspan="101">Models</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Creator</td><td>Acad.</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>✓</td><td>s</td><td>s</td><td>✓</td><td>s</td><td>s</td><td>s</td><td>✓</td><td>s</td><td>s</td><td>✓</td><td>s</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>✓</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>SFT RLHF 2048 4096 8192 100k Open Limited</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>t</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>f</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>sf</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>d</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>c</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>a</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>e</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>n</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>m</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>o</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>i</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>r</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>/</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>/s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>s</td><td>ss</td><td>/ s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s S f F L R H F S F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F S F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F F S F S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s d s d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s ss s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s s ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssassssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssissssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddd d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D D d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d/d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d</td></tr></table>

Figure 8.1 Diversity of model implementation. The models span across various creators, scales (parameter sizes), finetuning strategies, window sizes, and access types, where "Acad." denotes academic institution, "Indy." denotes industrial corporation, "SFT" denotes supervised fine-tuning, and "RLHF" denotes reinforcement learning from human feedback.

# 9 Experiments and Results

In this section, we present a thorough and systematic analysis of our experimental data, revealing a series of significant findings. The section is structured around four main aspects. Our most important and broadest analysis is conducted in Main Results (Section 9.1). Despite its depth, this analysis may not fully capture the causal reasoning abilities of language models within the CaLM framework. Therefore, we further extend our analysis across three dimensions: Prompt Analysis (Section 9.2), Model-specific Analysis (Section 9.3), and Causal Scenario-specific Analysis (Section 9.4). Our findings aim to support the advancement of future language models and offer valuable insights for developing benchmarks in various other fields.

# 9.1 Main Results

As outlined in The CaLM Framework (Section 1.1), CaLM is structured into four modules: causal target, adaptation, metric, and error. Our analyses focus on these four modules along with associated critical factors (e.g., model scale).

Specifically, this subsection is organised as follows:

- Comparative Analysis of Models (Section 9.1.1): We provide a direct comparison of the models' causal reasoning abilities across various aspects, such as prompts, modes, and languages.

- Impact of Other Factors on Accuracy (Section 9.1.2): We conduct an extensive analysis of some critical factors, such as model scale, model access, time, and language, that impact accuracy.

- Predicting Causal Reasoning Ability (Section 9.1.3): Intrigued by the possibility of predicting a model's causal reasoning ability under certain conditions (Liang et al., 2022), we conduct analyses from the perspectives of factors such as model scale and training strategy.

- Intra-dimensional Relationships (Section 9.1.4): We begin by focusing on specific dimensions within each module (e.g., causal scenarios, metrics, prompts), examining the intra-dimensional relationships, such as those among various prompt types, within each module.

- Inter-dimensional Relationships (Section 9.1.5): We explore the interactions between dimensions across various modules, such as the relationships between causal scenarios and models, or causal scenarios and prompts.

- Analyzing Complexity (Section 9.1.6): We define four factors (i.e., number of nodes, number of edges, authenticity, and causal reasoning process) that influence the complexity in the Mathematical mode datasets. And we disclose the factors that essentially affect the model performance in Mathematical mode questions, highlighting fundamental shortcomings in the causal reasoning abilities of current models.

- Analyzing Maturity (Section 9.1.7): We measure the maturity of a causal scenario. Our motivation to analyze the maturity of a causal scenario stems from the desire to explore the research potential of a causal scenario. That is, the relative immaturity of a scenario might suggest a larger room for research improvement.

- Analyzing Volatility (Section 9.1.8): We assess the volatility of the model and the prompt separately to understand their stability under different conditions.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a27e6ce5bdc90b02f379bb3834e896097acae252ed52779cf352d0e92a7010a3.jpg)



Figure 9.1 Comparative analysis of models under different modes. We report the absolute accuracy comparisons. The orange dashed line represents the accuracy of random guess.


- Analyzing Errors (Section 9.1.9): Lastly, we analyze the models' errors from both quantitative and qualitative perspectives to identify areas for improvement.

# 9.1.1 Comparative Analysis of Models

Given the rapid advancement of language models, a key goal of our evaluation is to foster a common and unified understanding of the causal reasoning capabilities of the currently available language models. Therefore, in this section, we aim to conduct a direct comparison of the performance of various models from multiple perspectives. This comparative analysis will enable us to discern differences and similarities in how these models handle causal reasoning tasks, providing insights into their strengths and weaknesses. Such insights will enhance our ability to assess the effectiveness of each model and potentially guide future developments in model training and application.

Comparative analysis of models under different modes. Comparing the performance of models directly under different modes helps us understand what types of problems the models are better at solving. As shown in Figure 9.1, the following insights can be concluded: (1) When considering their performance in exceeding random guess, it is noted that in both Natural and Symbolic modes, these models have employed instruction-tuning. In all three modes, the top three models have introduced the use of human feedback. This perspective indicates that instruction-tuning and the use of human feedback are effective means to enhance model performance across all three modes. (2) Shifting attention to the rankings of these top 3 models across different modes, it is observed that there is not a consistent and stable ranking. Additionally, the relative rankings of GPT-4, Claude2, and GPT-3.5-Turbo shift depend on the mode. This observation reinforces the findings presented in Section 9.1.4, which are based on the data illustrated in 9.14. (3) Llama2 (70B) shows a distinct difference in its performance rankings between Symbolic and Mathematical modes. Investigation revealed that for Symbolic, Llama2 (70B) fails to provide effective responses to either basic prompt or manual CoT in CEI, leading to extensive blank outputs. This accounts for its lower ranking in the Symbolic mode. On the other hand, in Mathematical mode, it manages to follow manual CoT guidelines to generate appropriate

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b9a925a8717ab1fb89d43fd92d7be84293e83df425ba3ba6d45caac549c02e85.jpg)



Figure 9.2 Comparative analysis of models under different languages. We report the absolute accuracy comparisons. The orange dashed line represents the accuracy of random guess.


answers, which boosts its overall performance. (4) It is evident that the models have a significant shortcoming in performing Mathematical operations. None of the models have an average accuracy exceeding  $30\%$ , which contrasts with their performance in Natural and Symbolic causal tasks, where the best-performing GPT-4 has an accuracy of over  $60\%$ .

Comparative analysis of models under different languages. The widespread global use of language models necessitates an evaluation of their performance in multilingual contexts. This analysis can guide the development of targeted corpora for future training and provide valuable references for users across different linguistic environments. As shown in Figure 9.2, it is evident that models generally perform better in English causal tasks. This finding aligns with our initial hypothesis, given that the training corpus for most current language models predominantly consists of English data. Specifically, the number of models performing better than random guesses in English causal tasks is nine, compared to seven in Chinese causal tasks. Moreover, GPT-4 emerges as the top performer consistently across both linguistic environments. In English causal tasks, both GPT-4 and GPT-3.5-Turbo, ranked first and second respectively, achieve an average accuracy exceeding  $50\%$ . Conversely, in Chinese causal tasks, even GPT-4's performance does not surpass the  $50\%$  threshold. Despite these variations in accuracy across languages, the top five models remain consistent, albeit with minor differences in their specific rankings. These models are GPT-4, GPT-3.5-Turbo, text-davinci-003, text-davinci-002 from OpenAI, and Claude2 from Anthropic.

Comparative analysis of models under different rungs of the causal ladder. We investigate models' performance across various rungs of the causal ladder, providing a thorough, bottom-up understanding of their abilities in different levels of causal reasoning tasks. We can see from Figure 9.3 that models exhibit superior performance at the lower levels (discovery and association) compared to the higher levels (intervention and counterfactuals). Specifically, models show the strongest performance at the discovery level and the weakest at the counterfactuals level. Notably, over half of the models (15 out of 28) achieve accuracy rates that surpass random guessing at the discovery level, a trend visually represented by the blue columns in the chart. We hypothesize that the improved performance of the model on causal scenarios within the causal discovery rung may be attributed to its extensive access to world knowledge. It is widely recognized in prior research

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d6269397a1df2029e5691d2c43e962af0bde64cdff42a695666af1cf0cc27ae4.jpg)



Figure 9.3 Comparative analysis of models under different rungs of causal ladder. We report the absolute accuracy comparisons. The orange dashed line represents the accuracy of random guess.


(Vashishtha et al., 2023; Ban et al., 2023) that language models excel in causal discovery due to their extensive access to world knowledge, which enables them to identify causal relations embedded within semantic content. This capability alleviates the need for explicit numerical computation, which is more crucial at the higher levels. And for the comparatively good performance on the association rung, we hypothesize that these results arise primarily because association concentrates on the statistical relationships among random variables. That is, causal scenarios within association rung do not require the model to have an extensive capability for causal reasoning.

Furthermore, analysis of model performance reveals that: (1) Limited-access models generally exhibit better performance, as evidenced by that across all levels of the causal ladder, the top 5 performing models are consistently those with limited public access. (2) GPT-4 consistently ranks first across all levels. At the discovery and association levels, text-davinci-003 outperforms GPT-3.5-Turbo. However, this trend reverses at the intervention and counterfactuals levels. This shift may hint at the beneficial impact of RLHF in enhancing model performance in more complex causal reasoning tasks.

Comparative analysis of models under different prompts. Considering the critical role of prompts in influencing model performance, we begin our analysis by evaluating how all models perform across various causal scenarios when subjected to different prompts. As depicted in Figure 9.4, we directly compare the performance of various models under different prompts. Key observations include: (1) GPT-4 excels in seven out of the eight prompts, with the sole exception of 1-shot IcL. GPT-3.5-Turbo stands out in the 1-shot IcL prompt, securing the top spot, and consistently ranks second in three other prompts (0-shot/manual CoT, 3-shot IcL). Claude2 also shows noteworthy performance, securing the second position in five of the prompts. However, it falls behind significantly in the 1/3-shot IcL and CoT, particularly ranking as low as 24th in 3-shot IcL. (2) The top three models are not consistent across all prompts, indicating variability in their accuracy depending on the specific prompt used. This observation aligns with findings from Figure 9.12 regarding Prompt-centric relationships. (3) The 3-shot IcL prompt appears to set a lower performance limit for models, while the manual CoT maximizes the upper limit for top-ranked models. Notably, GPT-4 using manual CoT is the only model achieving over  $70\%$  accuracy, but its performance drops below  $60\%$  with 3-shot IcL. In contrast, GPT-3.5-Turbo, which ranks second under both prompts, shows an accuracy of  $59.8\%$  with manual CoT, surpassing its performance with 3-shot IcL by  $7.2\%$ . Additionally, the number of models reaching or exceeding  $50\%$  accuracy under manual CoT is four, compared to three under 3-shot IcL.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/81e6b230a4bc0e0ebea816c0801650250a879657f7b59625774537901ee2c5c1.jpg)



0-shot IcL


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4cfb8200f9c28e6b9a4e47e638f8459ba6f87bdd5e14a924f94690419b2e896b.jpg)



1-shot IcL


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a987cee3f7439945344b9959527c546cf33ff3f9111a77f4338165d1b64c9903.jpg)



3-shot IcL


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1daec8e0319422e612b59a156d4c9edf80f66339d96a2f7966d4f36f316f1da1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/aa054adade4f44efb236fad515b9ffdd1855755b12aa57838be9b6ee9c6d5a96.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/93a58367e5c1f2783836d5c41574fd6a2723b0e16bad196eefd6a6e80f048e37.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a8340a840a9d5e7a17f954f294d08c4e542eda3b2431ab5ac0ddffed97c22567.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a6fe10c9a86ef9354c361382befa93a0d611e966bc9b9d745cce72193e394324.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cb33a34d16a7c46856cd97f8e928572037372c5ed792361db447fe1ebd1ee54b.jpg)



Figure 9.4 Comparative analysis of models under different prompts. We report the absolute accuracy comparisons. The orange dashed line represents the accuracy of random guess.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/afdebdfcfd30b930028a5ee04a5e599b5c2539ef5caf0ff58b0994ced3ab7cbf.jpg)



Figure 9.5 Impact of model access on accuracy. The impact of model access (Open and Limited) on the accuracy in each of the 21 causal scenarios.


# 9.1.2 Impact of Other Factors on Accuracy

Impact of model access on accuracy. We explore the relationship between accuracy and model accessibility in Figure 9.5. For each access type, we calculate the average accuracy of all models in the corresponding causal scenario. Overall, we observe a consistent pattern: models with limited access tend to outperform their open-access counterparts across all causal scenarios.

Nonetheless, we ought to maintain an optimistic perspective regarding open-access models. It is evident that in causal scenarios such as PCD, ECI, AR, and CEG, the disparity between the two access types has been narrowed to less than  $2\%$ . We exclude PN and PS from this comparison due to their universally low accuracy, which renders any difference statistically insignificant. It is worth noting that PCD, ECI, and AR all belong to the causal discovery level, demonstrating that open-access models are capable of competently understanding causal relationships. The tasks within these scenarios vary: PCD and ECI focus on discerning causality among events, whereas AR involves analysis based on a given causal graph. This variation underscores the adaptable nature of open-access models in handling causal discovery tasks. The observed deficiencies in other causal scenarios suggest avenues for enhancement. Methods such as expanding training datasets or refining training techniques could potentially elevate the performance of open-access models to close the gap with limited-access models even further.

Impact of time on accuracy. Understanding how model performance evolves over time is crucial for developing a deeper macro-level understanding of technologies. We explore this dynamic in Figure 9.6, where models are categorized into 10 groups spanning from May 2020 to September 2023, based on their release dates. The details of these groupings are clarified in Figure 9.6. Figure 6(a) presents the average performance of all models within each group, while Figure 6(b) focuses on the accuracy of the highest-performing model in each group across all causal scenarios. All models from Group  $1\sim 5$  are developed by OpenAI.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/331499de50951d37e32b8157e500cf71ef7d555cedc7898d2cad8772b58734dc.jpg)



(a) Performance of grouped models


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4e7f7533a3cad8b879ac030210b74f1113194fc7c0976220a5638eafc55cef34.jpg)



(b) Performance of selected models



Figure 9.6 Impact of time on accuracy. The interplay of time (x-axis) with all models' accuracy (y-axis), examined across 21 causal scenarios. Accuracy represents the average value for all models in the corresponding group. Each group consists of models released in the same year and month, and we will detail the grouping as follows. Group 1: ada (0.35B), babbage (1.3B), curie (6.7B), davinci (175B). Group 2: text-ada-001, text-babbage-001, text-curie-001, text-davinci-001. Group 3: text-davinci-002. Group 4: text-davinci-003, GPT-3.5-Turbo. Group 5: GPT-4. Group 6: Koala (13B). Group 7: Wizardcoder (15B), Vicuna-v1.3 (33B), Baichuan1 (7B). Group 8: Llama2 (7B), Llama2 (13B), Llama2 (70B), Llama2-chat (70B), Baichuan1-chat (13B), Claude2. Group 9: Qwen (7B), InternLM-chat (7B). Group 10: Baichuan2-chat (7B), Baichuan2-chat (13B), Qwen (14B), InternLM-chat (20B).


Above all, we begin by examining the consistent insights presented across both figures. From the model perspective, several key aspects emerge as particularly significant: (1) Starting with InstructGPT (Group 2) and culminating with GPT-4 (Group 5), each successive release from OpenAI's model series marks a clear improvement in performance. This trend is consistent with findings from Fu & Khot (2022), supporting the effectiveness of the technological advancements made by OpenAI. (2) GPT-4 maintains a significant advantage in approximately  $80\%$  of the causal scenarios, outperforming both its predecessors and subsequent models. (3) Models in Groups 5 to 10 show diverse performance levels, dependent on the specific causal scenarios they address. This indicates an absence of a consistent improvement trend and underscores the selective effectiveness of these models.

From the perspective of causal scenario, the performance of models in the CEI scenario shows no correlation with their release dates, aligning with our interpretation in Causal scenario-centric relationships. Contrary to a progressive improvement expected over time, the performance fluctuates - sometimes peaking, sometimes diminishing - highlighting the unique challenges posed by this scenario.

Moving forward, we will focus on the most pronounced difference between the two figures. Specifically, by narrowing our analysis to selected models as depicted in Figure 6(b), it becomes apparent that Claude2 emerges as a formidable competitor, distinctly achieving a "localized peak". This observation suggests that Claude2 may possess unique attributes or optimizations that enable it to excel in certain scenarios, standing out among its contemporaries.

Impact of multilingual capabilities on accuracy. We investigate the relationship between model accuracy and multilingual capabilities in Figure 9.7. For each language type, we calculate the average accuracy of all models across each causal scenario. Consistently across most scenarios, except for CA, CEI, and CEG, models perform better in English causal tasks than in Chinese. This is expected, as noted in Section 8, given that English predominantly comprises the training corpus for most models. This performance gap highlights the critical need for developing richer and more diverse language corpora to enhance model proficiency in multilingual contexts significantly.

In scenarios where models exhibit superior performance in Chinese, we explore potential explanatory factors. For instance, in the CEI scenario, Llama-based models (including Koala, Llama2-13b, Llama2-70b, Llama2-70b-chat, Vicuna-33b) tend to be more effective in Chinese tasks. When using the basic prompt, these models typically produce very concise replies in Chinese, whereas in English, their responses are often less effective. While these observations may not fully capture the complexities of language performance differences, they provide insights into possible underlying factors contributing to these discrepancies.

Impact of domain on accuracy. As mentioned in Dataset Selection, our dataset primarily consists of two parts: open-source and self-constructed. This differentiation is critical for assessing the potential issue of training-test contamination, as discussed by Liang et al. (2022). Additionally, this analysis is instrumental in providing insights into the development of training sets for models and enhancing their generalization capabilities across various domains. We explore the relationship between model accuracy and domain across different rungs<sup>21</sup> of the causal ladder in Figure 9.8. Note that, a detailed classification of what constitutes the open-source and self-constructed datasets at each rung is presented in Table 4.1.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/40fd87d58e4c4cad5f662779c5f760ad96ed76a9321b0f4e0d6d8895d2f09e7b.jpg)



Figure 9.7 Impact of multilingual on accuracy. The impact of language (English and Chinese) on the accuracy in each of the 21 causal scenarios.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/533ed058e07623a8f00c28a3b43c5737c34bde21f87d59d22f176879b6861d38.jpg)



Figure 9.8 Impact of domain on accuracy. We calculate the average accuracy of all models at the same rung but in different domains (i.e., open-source or self-constructed).


From Figure 9.8, we discover that the relationship between accuracy and domain varies across the rungs of the causal ladder. For simpler tasks associated with causal discovery $^{22}$ , models exhibit marginally better performance on self-constructed datasets than on open-source ones. In contrast, for the more challenging tasks at the intervention and counterfactuals rungs, models generally perform better on open-source datasets. Given that certain datasets were released earlier (e.g., CRASS (Frohberg & Binder, 2022) was issued in 2022), it is possible that they have been used as training corpus for some models. This might account for the superior performance of models on open-source datasets. This trend indicates that while current language models are relatively proficient in extracting and utilizing causal relationships from natural language expressions commonly found in broader datasets, their capabilities diminish as the complexity of causal reasoning increases.

# 9.1.3 Predicting Causal Reasoning Ability

Numerous studies have already established a link between the scale of models and their loss, underscoring the influence of model size on performance metrics (Kaplan et al., 2020; Hoffmann et al., 2022). In our analysis, we use accuracy as a measure to assess the effectiveness of causal reasoning abilities of language models. However, it is important to clarify that while accuracy is a critical metric for our evaluation, it does not fully encapsulate the breadth of causal reasoning capabilities of these models. Moving forward, we aim to explore the potential for more precise criteria for evaluation.

Causal reasoning ability vs. scale. We investigate the relationship between model accuracy and scale, as depicted in Figure 9.9. We categorize the models into ten groups based on their scales, ranging from 0.35B to 1700B parameters. The top half of Figure 9.9 illustrates the mean performance of all models within each group across various causal scenarios. The bottom half presents the top-performing model selected from each group. Our analysis does not include all models for two primary reasons: (1) Due to the close similarity in scale among certain models, we have made selective choices to manage the impact of models across different scales and to maintain the visual clarity of our presentations. For instance, we choose the 7B model over others ranging between 6.7B and 7B, and select the 13B model over those ranging from 13B to 15B. (2) For some models, it is challenging to obtain an authoritative source for their scale, precluding us from making informed estimations. An example is GPT-3.5-Turbo, for which the exact scale has not been determined.

Beginning with the grouped models, we derive several key insights: (1) There is no consistent pattern of increasing accuracy with larger model scales, particularly among models from Group 13B to Group 70B. This fluctuation suggests that performance should be analyzed within specific causal scenarios. The variability in this scale range could stem from differences in model origins, with disparate creators applying different training methodologies and datasets, which significantly impact outcomes beyond mere scale. (2) When examining models created by the same creator, the relationship between accuracy and scale becomes more apparent. For instance, models from OpenAI in Group 0.35B, 1.3B, 175B, and  $1700\mathrm{B}^{23}$  exhibit a correlation where, generally, larger scales correspond with higher accuracy, except in the CEI and CB scenarios. (3) Notable performance increases are observed within certain scale ranges, particularly between Group 13B and Group 20B, and from Group 70B to Group 130B. Specifically, when looking at Group 20B, this group, containing only one model (i.e., InternLM-chat (20B)), shows a performance peak that may reflect the effectiveness of specific training strategies and optimal parameter selection. From the perspective of Group 130B - the first group with over 100B parameters - there is a marked performance leap over Group 70B. This implies that a significant increase in model parameters may enhance model capabilities. Yet, the progression from Group 130B to Group 175B complicates this view. The models in Group 175B, which span a broad range of release dates from davinci (175B) in May 2020 to text-davinci-003 in November 2022, showcase the potential impacts of evolving technology on model capabilities. Conversely, the models between Group 70B and 130B, including those in the Llama2 series and Claude2 $^{24}$ , were all released within a tight timeframe in July 2023. This closer release window offers a more controlled examination of the scale effect, minimizing the variable of technological progression. This distinction provides valuable insights into how timing and technological advances, in addition to scale, can influence model performance across various causal inference tasks.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/46c35daafd319d9cf8373bc590317098b1305444af8941df8a0dde7c59093f70.jpg)



(a) Performance of grouped models


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3f91e359a02bb7b4f19e57a73fbe51fc4c1e6d60c799910c7fef9614d05771b4.jpg)



(b) Performance of selected models



Figure 9.9 Causal reasoning ability vs. scale. Accuracy represents the average value for all models in the corresponding group. Each group consists of models of the scale, and we will detail the grouping as follows. Group 0.35B: ada (0.35B), text-ada-001. Group 1.3B: babbage, text-babbage-001. Group 7B: Baichuan1 (7B), Baichuan2-chat (7B), Qwen (7B), InternLM-chat (7B), Llama2 (7B). Group 13B: Baichuan1-chat (13B), Baichuan2-chat (13B), Llama2 (13B), Koala (13B). Group 20B: InternLM-chat (20B). Group 33B: Vicuna-v1.3 (33B). Group 70B: Llama2 (70B), Llama2-chat (70B). Group 130B: Claude2. Group 175B: davinci (175B), text-davinci-001, text-davinci-002, text-davinci-003. Group 1700B: GPT-4. The red text and dashed line indicate that the scale of the model is undisclosed.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1c7e065286dbe96c1bb733615ce8f1bc5907740bbb7b214901c190e42d36c01f.jpg)



Figure 9.10 Causal reasoning ability vs. training strategy. We categorize models into three groups based on different training strategies (i.e., pre-training, SFT, and SFT&RLHF). To investigate the effectiveness of different training strategies, we compare the average accuracy of the different groups of models across 21 causal scenarios.


Analyzing the selected models yields the following insights: (1) For models with scales ranging from 7B to 70B, the relationship between scale and accuracy is still not definitive. This observation suggests that merely increasing the size of a model may not be the most effective strategy for enhancing its causal reasoning capabilities. It appears that other factors, such as training methods and datasets, may have a more significant impact than scale alone. (2) Despite the ambiguity in broader datasets, a clear trend is still observed within the models developed by OpenAI: as model scale increases, so does accuracy. This pattern within OpenAI's series suggests that their approach to scaling - possibly coupled with their specific training techniques and data handling - effectively boosts model performance.

Causal reasoning ability vs. training strategy. In Figure 9.10, we explore the impact of different training strategies on the causal reasoning capabilities of models. This analysis categorizes all models based on their distinct training strategies (detailed in Section 8) and measures the average accuracy of each group across various causal scenarios.

The findings from Figure 9.10 reveal significant insights about the efficacy of these strategies: (1) The combination of SFT and RLHF is the most effective strategy, leading to the highest accuracy in  $86\%$  (18 out of 21) of the causal scenarios. This strategy significantly outperforms the models trained using either pre-training or SFT alone. The success of RLHF in enhancing causal reasoning capabilities suggests that integrating human feedback helps to more closely align model outputs with complex human reasoning patterns, particularly in complex causal scenarios requiring causal understanding. (2) The performance gap between models trained via SFT and those undergoing pre-training is relatively small, with SFT models outperforming pre-training models in 13 causal scenarios. This marginal advantage indicates that while SFT has some benefits, the lack of extensive, causal-oriented datasets specifically tailored for SFT might limit its effectiveness. Using general or unrelated domain datasets for SFT seems to provide only a limited boost to the models' causal reasoning abilities, suggesting that more focused and relevant training data could potentially enhance performance further.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9ed190702dabd48e76d5db1f9a4012b2dd4760825d901787f83e415279d7b2f7.jpg)



Figure 9.11 Basic prompt vs. other prompts. We explore the relationship between the basic prompt (x-axis) and eight distinct prompts (doubt, ignore, EF, 0-shot CoT, 0-shot IcL, 1-shot IcL, 3-shot IcL, and manual CoT). We investigate these correlations in all models across all causal scenarios. Each dot symbolizes a pair of accuracies achieved by a specific model when employing a specific pair of prompts, and the dot's color signifies the related causal scenario.


# 9.1.4 Intra-dimensional Relationships

Prompt-centric relationships. To the best of our knowledge, there is currently no work that integratively studies the relationships among different types of prompts. Against the backdrop of the rapid development of prompt engineering, we are eager to explore the relationships between different prompts, hoping to provide insights for the future development and usage of prompts.

We depict the accuracy relationship between the basic prompt and other eight types of prompts in Figure 9.11. Each dot symbolizes a pair of accuracies achieved by a specific model when employing a specific pair of prompts, and the dot's color signifies the related causal scenario. For example, if a model attains  $70\%$  accuracy with the basic prompt and  $80\%$  accuracy with manual CoT in the PCD scenario, this result would be represented by a dot located at the coordinates (70,80) in the subgraph comparing the basic prompt and manual CoT. Note that, the color of the dot corresponds to the PCD scenario. The basic prompt serves as the benchmark for all other prompts, rendering Figure 9.11 pivotal for identifying key prompts that improve model performance. Moreover, by incorporating various causal scenarios, this figure shows diverse trends in these relationships. It highlights how the effectiveness of prompts can depend significantly on the causal scenario, exhibit variability, and reveal unusual patterns.

From the perspective of prompts, we have the following findings: (1) We discover that across all causal scenarios, the basic prompt shows a significant correlation with doubt, ignore, EF, 0-shot CoT, and 0-shot IcL (See Figure 9.11). The performance patterns of these prompt pairs remain consistent across various causal scenarios, as evidenced by their corresponding scatter plots approximating a straight line with a unit slope. (2) The relationship between the basic prompt and 1-shot IcL needs to be analyzed within specific causal

scenarios. As demonstrated in Figure 9.11, there is no clear trend in their correlation in causal scenarios such as NDE, NIE, and ETT. However, in PCD and ECI, their trend appears to be broadly positive. (3) Generally speaking, we can see from Figure 9.11 that there is no strong correlation between the basic prompt with either 3-shot IcL or manual CoT. However, in specific causal scenarios (e.g., BAS, AR, and ECI), their scatters exhibit a positive correlation. This highlights the substantial heterogeneity in characteristics across different causal scenarios.

In Figure 9.12, we examine the Pearson correlations (Sedgwick, 2012) between prompt pairs across all causal scenarios. We begin with calculating the Pearson correlation for each pair of prompts within each scenario. These coefficients are then used to construct the box plots depicted in Figure 9.12. For example, if there are ten models under one scenario, prompt A and prompt B each yield ten accuracy values. We first calculate the Pearson correlation for these values. Given multiple causal scenarios, each with its own A-B correlation, we aggregate these into the box plots shown in Figure 9.12. Specifically, in each subplot, we categorize the models into three groups: all models, the selected 3 models, and the remaining 25 models. In the category of "all models", we can present the trend of relationships between prompts from the most macroscopic perspective. Moving attention to the "selected 3 models", we select the three well-performing models (GPT-4, GPT-3.5-Turbo, and Claude2)[25] in all causal scenarios as representatives. This aims to eliminate some potential interference from invalid data.[26] Thus, considering only the three well-performing models may better reflect the true relationship between prompts. Finally, we also examine the "remaining 25 models", which, in contrast to the selected 3 models, provide insights into variations in prompt pair correlations across models with different performances. Overall, our setup highlights the distribution and heterogeneity of relationships between prompts and facilitates a macroscopic examination of trends across different model categories.

Figure 9.12 provides rich insights into the relationships between various prompts, revealing several key findings from the analysis: (1) Within all causal scenarios, there is no strong correlation among prompts of the same category when different numbers of examples are provided (e.g.,  $0/1/3$ -shot IcL, 0-shot/manual CoT). Specifically, for 0-shot/manual CoT, the median correlation does not exceed 0.5 across all model groups (i.e., "all models", "remaining 25 models", and "selected 3 models"). For  $0/1$ -shot IcL, only the "selected 3 models" group exhibits a median exceeding 0.75. For both  $0/3$ -shot IcL and  $1/3$ -shot IcL, the medians for all three groups do not exceed 0.75. This suggests that predicting performance under the same prompt type with varying numbers of examples (shots) is unreliable, as the quantity of examples significantly influences model performance. (2) Within the 0-shot setting, there is a discernible correlation between CoT, IcL, and EF. This observation is supported by Figure 9.12, where the lowest median correlation values for both the "all models" and "selected 3 models" groups exceeding 0.5. This indicates that although models are sensitive to changes in prompt structure, merely altering the guidance of questions within the prompt, without changing the examples, typically does not lead to significant variations in performance. (3) It is observed that the median values of all groups' box plots are above zero, indicating a generally positive correlation in model performance across various prompts. This implies that, even without a strong correlation, a model's performance with one type of prompt can somewhat predict its effectiveness with other prompts.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f42f7c687a9ec7d1ba1f8e7cdf41bca2874598588e2586e2bf6adac7953b6a9e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/73f16633d7662646ca0dd6b7899b6464a8c91667629110b7e5d0328a8cfd3a10.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/bd1839fc55b503b2648585a0ea9ed125dd27282432a675265885cf1b4adeb625.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ce24cb89ccc11e8d041662a6ed9483702d602edb6724c66924b2ec51a20da201.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d0efec4e9691f8efa73f566f7f92dd3f4ac1af1fe262655317f464851658ef4f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cde71090ea6a880b05db8670e7c62ae619b964b6ee3563c2eb9246a50c3e9abb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/63853ff270dfe4717b0f1201af98d94f1d18af0339f4d001dc0114414491f2a7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/406d5fb3f7504507fccf566fc2bec855ee74d965c5b6c3348ff0ac5aa7aac9ed.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3d7b0048a2c1cea41953833d1041e707904e3c5d594dd018946a1d46e9a35664.jpg)



Figure 9.12 Pearson correlation between prompts. We compute the Pearson correlation for each prompt with every other prompt. Boxes in various colors denote different groups (i.e., all models, the remaining 25 models, and the selected 3 models). Dots in different colors indicate outliers from those respective groups. The median is represented by an orange line.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3e501fffb5c5c2e3c99a1e5f3d816c24d82cce84996745069ae9d54dc3fff4d9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/372492a23d633837b14c46d8f9f83e521f2aa2622e0252e7acf57da7a6c29510.jpg)



Figure 9.13 Relationship between accuracy and robustness. We separately demonstrate the relationships between accuracy and robustness from the perspectives of the causal scenario and the model.


From the analysis of model performance, the following insights can be summarized: (1) The "selected 3 models" group shows significant variability in performance across different prompts. This is evidenced by the frequent appearance of outliers in their sub-boxes, suggesting high data variability. The length of the whiskers on these sub-boxes is usually extended, indicative of greater data dispersion. Additionally, the asymmetry in the lengths of the upper and lower whiskers for this group points to an uneven distribution of data. The interquartile ranges are also larger, further confirming increased variability. (2) There is a notable correlation between the doubt and ignore prompts across all models, which are designed to assess model robustness. This consistent correlation suggests that the stability of a model's performance under these prompts follows a uniform pattern.

Metric-centric relationships. Our primary objective extends beyond simply achieving high accuracy in model performance. We aim to develop models that not only exhibit superior performance but also demonstrate robustness. The ability for consistent performance across various causal scenarios is crucial for language models intended for widespread deployment.

In Figure 9.13, we depict the correlation between accuracy and robustness across various causal scenarios and models. When focusing on causal scenarios, each point on the plot corresponds to the accuracy and robustness of a specific model within a specific causal scenario. When examining models, we average out the accuracy and robustness for each model over all causal scenarios and plot these data points. And for models that originate from the same creator, we represent with the same color. Note that, in our analysis, we have not included IcL, CoT, and EF in this consideration, because our adversarial prompts are designed to attack the basic prompt. Therefore, the accuracy metric we refer to is an average merely derived from basic prompt, adversarial doubt, and adversarial ignore. In future research, we intend to examine the impact of disruptions on these other types of prompts.

From an analysis grounded in causal scenarios, it is evident that the interplay between a model's robustness and accuracy significantly varies across different causal scenario. Notably, in challenging causal scenarios such as PN and PS, there is an interesting trend: models may exhibit minimal accuracy yet display disproportionately high robustness, in some instances reaching  $100\%$ . This occurs primarily because most models are fundamen-

tally unable to respond to these kinds of questions effectively. Their responses remain stable, irrespective of any disturbances. Our robustness metric, which assesses whether responses change before and after an attack, thus appears artificially inflated in these scenarios. This observation highlights a limitation of our current robustness metric, underscoring the need for future research to develop more nuanced and detailed criteria for its evaluation. In contrast, For less challenging scenarios like PCD and AR, the correlation between robustness and accuracy is generally positive, as indicated by trend lines with a positive slope. However, in causal scenarios such as ECI, EAE, and AC, the relationship between these metrics does not exhibit a clear and consistent pattern, likely influenced by the distinctive characteristics of individual models.

Moving on, we turn our attention to models, highlighting several key points of interest. (1) GPT-4 is distinguished as the sole model that manages to maintain an optimal balance between accuracy and robustness. This is evident in the right subplot of Figure 9.13, where GPT-4 is uniquely positioned in the upper right corner. (2) Within models released by the same creator within a narrow timeframe (less than three months apart), there is a noticeable variability in the relationship between accuracy and robustness. For example, we examine the Llama2 series released by Meta at the same time. Here, it is clear that Llama2-chat (70B) demonstrates considerably lower robustness compared to the other three models in the same series. This could potentially be attributed to the adverse effects of RLHF, which might make the model more prone to altering its responses under human critique. A similar pattern is observed across the four models in the Baichuan series, where Baichuan1 (7B), not fine-tuned with RLHF, achieves the highest level of robustness.[27] (3) The evolutionary path of OpenAI's models further illustrates these dynamics. Initially, the GPT-3 models (e.g., ada, babbage, curie) exhibit lower accuracy but higher robustness due to their limited causal reasoning and poor instruction-following capabilities. In contrast, the subsequent InstructGPT series (e.g., text-ada-001, text-babbage-001, text-curie-001) improve upon both fronts, thereby concurrently increasing accuracy and diminishing robustness. This evolution culminates in the release of GPT-4, marking the pinnacle of balance between accuracy and robustness to date.

Mode-centric relationships. We investigate the relationships between different modes - Natural, Symbolic, and Mathematical - using both Pearson and Spearman correlation metrics (Hauke & Kossowski, 2011). These modes comprise 20, 12, and 14 causal tasks, respectively. Our analysis employs consistent model grouping as used in Prompt-centric relationships, i.e., "all models", "selected 3 models", and "remaining 25 models". The details of the correlation coefficients are computed as follows: (1) We calculate the average accuracy for models within these groups across various causal tasks and modes. For instance, in the "selected 3 models" group, this involves creating a  $3 \times 20$  matrix for the Natural mode. Rows of this matrix correspond to models in the group, columns correspond to different causal tasks within the Natural mode, and entries of the matrix represent the average accuracy of each model on these tasks. (2) We compute the correlations between causal tasks across different modes. For instance, in the "selected 3 models" group, we analyze matrices for the Natural  $(3 \times 20)$  and Mathematical  $(3 \times 14)$  modes, by iterating over columns to produce  $20 \times 14 = 280$  correlation coefficients. (3) Finally, these coefficients are then visualized using a boxplot.

Furthermore, we explore the correlations among causal tasks of the same mode. For example, we have a  $3 \times 20$  matrix for the Natural mode in the "selected 3 models". Then we iterate over the columns to calculate the correlations among 20 causal tasks within the Natural mode, resulting in  $20 \times 20 = 400$  correlation coefficients. This approach leads to the consequence that the correlation within the same mode (for instance, Natural with Natural) is not 1. This method is adopted because concentrating only on modes without considering

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/01c1baca6a23b3286bc483a02858f049db4fac0286585e425cb9c159600821ad.jpg)



Figure 9.14 Correlation between modes. We compute both the Pearson and Spearman correlations for each mode with every other mode. Boxes in various colors denote different groups (i.e., all models, remaining 25 models, and selected 3 models). Dots in different colors indicate outliers from those respective groups. The median is represented by an orange line.


individual causal tasks might miss out on more nuanced information, which could be essential. Utilizing both Pearson and Spearman metrics accommodates the diverse qualitative trends that different modes may exhibit.

In Figure 9.14, we focus on the relationships among all causal tasks across different modes. In contrast, Figure 9.15 broadens the perspective, offering a comparison of the three modes at a higher level. To accomplish this, we begin by calculating the average accuracy for all causal tasks within each mode across all models. Following that, we apply both Pearson and Spearman correlation metrics to assess the relationships between these modes.

Our mode-centric analysis yields several insightful observations regarding the relationships between different modes. (1) It can be concluded from Figure 9.15 that the Natural mode has a high correlation with both the Mathematical and Symbolic modes. Specifically, the Pearson correlation between Natural and Symbolic modes is notably high at 0.814, while their Spearman correlation, though the lowest, is still substantial at nearly 0.7. In contrast, the correlation between the Mathematical and Symbolic modes is relatively low. These findings provide valuable insights for the development of diverse causal task designs. (2) Taking a closer look at the relationship between the Mathematical and Symbolic modes, we find that there exists a strong linear but weaker monotonic relationship between them. As shown in Figure 9.15, their Pearson correlation is 0.718, indicating a strong linear association, but the Spearman correlation drops significantly to 0.386. This suggests that the linear relationship varies across data segments - being strong in some and weak or inverse in others - which impacts the Spearman correlation. This metric emphasizes the consistency of trends rather than the strength of linear relationships. (3) While the Natural and Mathematical modes generally show a

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/322d7ad6c3315bd953afcb637496e05321fdea57099da1c8db7ad7d8536a1e4f.jpg)



Figure 9.15 Overall correlation between modes. We compute both the Pearson and Spearman correlations for every mode pair (i.e., the correlations of Natural and Mathematical, Natural and Symbolic, Symbolic and Mathematical).


high correlation, Figure 9.14 reveals significant variability in the distribution of their correlation coefficients. The interquartile range (the box's upper and lower edges) for the "all models" group is asymmetrical, with an elongated lower portion, suggesting a broader spread of lower values. Moreover, numerous outliers at the lower end for both the "all models" and "remaining 25 models" groups highlight considerable differences among causal tasks within these modes.

Shifting the focus to models, our analysis provides specific insights as follows. (1) For the "selected 3 models" group depicted in Figure 9.14, they exhibit significant variability in performance across different modes. Specifically, Pearson correlation analysis reveals marked differences in accuracy for various causal tasks within these modes, indicating that even among top-performing models, performance consistency is not guaranteed. Additionally, Spearman Correlation suggests that the rankings of these models fluctuate, highlighting instability in their relative performance. (2) As shown in Figure 9.14, the median correlations for the "all models" and "remaining 25 models" groups demonstrate that causal tasks within the same mode exhibit the highest correlations. This outcome aligns with expectations, as tasks within the same mode generally share similar formats.

Causal ladder-centric relationships. In Figure 9.16, we explore the Pearson correlations across different levels of the causal ladder, following the approach used in Mode-centric relationships. We look into how all causal tasks within specific levels of the ladder relate to one another. Specifically, we consider 10 causal tasks under causal discovery, 2 under association, and 17 under both intervention and counterfactuals levels. We also assess the correlations among tasks within the same level of causal ladder, clarifying why correlation coefficients for pairs from the same level (e.g., association-association) do not necessarily equal 1.[28]

Based on Figure 9.16, we draw the following conclusions: (1) From the perspective of the "all models" group, there is a strong correlation between causal discovery and the other three levels of the causal ladder. It is shown that the upper quartile values for "all models" are greater than or equal to 0.75, indicating a significant positive relationship. This supports the design rationale behind our CaLM framework, affirming the placement of

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4a18a913af44002132bbb51e5eb32ee35510d14f155b629a27ff8bd1c749608e.jpg)



Figure 9.16 Correlation between various rungs of causal ladder. We compute the Pearson correlation for each rung with every other rung. Boxes in various colors denote different groups (i.e., all models, the remaining 25 models, and the selected 3 models). Dots in different colors indicate outliers from those respective groups. The median is represented by an orange line.


causal discovery as the foundational rung (Rung 0) in the ladder of causation. (2) Within the intervention level, causal tasks exhibit comparatively lower correlations with each other. This observation is derived from an analysis of correlations among causal tasks within each causal level (e.g., discovery-discovery, association-association). Notably, the boxplots for intervention-intervention exhibit the greatest range across three model groups, reflecting the most variability. Furthermore, the median correlation values for both the "all models" and the "remaining 25 models" groups identify intervention-intervention as having the weakest inter-task correlations within the intervention ladder.

Causal scenario-centric relationships. Our evaluation spans all rungs of the causal ladder, offering the most extensive setting for evaluating the causal reasoning capabilities of language models across diverse causal scenarios. The variety of causal scenarios inspires us to investigate the correlations between them. This exploration aids in enhancing our understanding of how the models perform in various causal scenarios. We aim to identify specific scenarios where model performance exhibits strong or weak correlations, and to ascertain whether certain causal scenarios pose unique challenges to the models.

In Figure 9.17, we analyze the Pearson and Spearman correlations across various causal scenarios. To be specific, we calculate the average accuracy for all models under each causal scenario, and then assess how

these accuracy values correlate with each other across different scenarios. The heatmap presented in the figure illustrates these correlations, with each cell displaying the respective correlation coefficient. To enhance the visual clarity and the interpretability of the data, we color-code the names of the causal scenarios based on their respective rungs of the causal ladder: causal discovery scenarios are highlighted in orange, association scenarios in sky blue, intervention scenarios in green, and counterfactuals scenarios in purple.

Our initial analysis, based on the quantitative correlation trends displayed in Figure 9.17, provides macro-level insights as follows: (1) Causal scenarios within the same level of the causal ladder typically exhibit higher correlations. Specifically, at the level of causal discovery, except for CA, the other three scenarios demonstrate strong correlations, with both correlation coefficients exceeding 0.80. At the association level, all scenarios show correlations above 0.80. At the intervention level, two groups of scenarios - ATE and CDE, as well as BAS, IV, and FAS - display very high correlations, each with a correlation above 0.93. For the counterfactuals level, even the lowest correlation coefficient among ETT, NDE, and NIE reaches 0.84. (2) The models show positive correlations in performances across the 19 causal scenarios, except for CB and CEI. This uniformity in performance across the four rungs of the causal ladder underscores the cohesiveness of the models' capabilities, and affirms the soundness of our causal scenario design.

Switching to some specific causal scenarios, there are important findings worth emphasizing: (1) Overall, CEI shows the lowest correlation with other causal scenarios. Both Pearson and Spearman correlations reveal a distinct color demarcation line along the CEI axis. According to the analysis in Section 9.4.3, CEI poses considerable challenges to the models, and the models' performance ranking in this causal scenario is noticeably different from others. Besides CEI, CB's correlations with other causal scenarios are also relatively low. From Section 2.3.5 in Lu et al. (2024), we discover that models are easily misled by the probability figures presented within questions, leading to wrong responses. Our results also indicate that models still struggle with recognizing CB. (2) Despite belonging to different levels of the causal ladder, there is apparent correlation between certain distinct causal scenarios in terms of model performance. Scenarios within causal discovery (e.g., PCD, ECI, and AR), along with those belonging to intervention (e.g., ATE and CDE) and counterfactuals (e.g., ETT, NDE, NIE, PS, and CR), exhibit relatively strong correlations among each pair (e.g., PCD-ETT, CDE-NIE, ECI-ATE). For instance, PCD and CR have an extremely significant correlation, with both coefficients exceeding 0.93. Among these combinations, NIE and PS have the lowest correlation, but their Pearson Correlation still exceeds 0.5. (3) Compared to PS, PN has a lower correlation with other causal scenarios. As detailed in Section 2.3.3 of Lu et al. (2024), there is a significant difference in the models' performance when inferring necessary versus sufficient causes. Models generally fail to accurately infer necessary causes but consistently provide correct inferences for sufficient causes. Combining existing research with our experimental results, it is evident that models have yet to clearly distinguish between the concepts of necessity and sufficiency, with the PN scenario presenting greater challenges and thus exhibiting a lower correlation.

In addition to the consistent patterns previously identified, it is crucial to note the causal scenarios where significant discrepancies between Spearman and Pearson correlation coefficients occur, which highlight key findings: (1) The performances of models in the PN and CEI scenarios show considerable differences between these two types of quantitative coefficients. Specifically, PN is notable because all its relationships, except for its self-correlation, are lower when assessed using the Spearman coefficient rather than the Pearson. This suggests a potential shift in the models' performance ranking within the PN causal scenario. For CEI, while it shows positive Pearson correlations with scenarios like ATE, NDE, and CEG, these turn negative when measured with the Spearman coefficient. These observations concerning PN and CEI reinforce the conclusions

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/50ce5d8a882a87d31197137602a5ee63d339d6d12fb724305dea75d1beb5ad2a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cf2c80236c782606b3557444e41c0219fc2d4109879908b8890976d28f6465e3.jpg)



Figure 9.17 Inter-causal scenario performance correlation. We compute both the Pearson and Spearman correlations for every causal scenario. Each cell represents how the model accuracy correlates with two causal scenarios.


from the previous analysis, indicating that these two causal scenarios are particularly challenging for the models and exhibit notable divergences in correlation types. (2) Across all models and causal scenarios, the Spearman coefficients are generally lower than the Pearson coefficients. This implies that linearity (as captured by Pearson) is more pronounced than monotonicity (as captured by Spearman) in these causal scenarios. It further suggests that the relationships might not consistently adhere to a simple ranking order but rather show a linear dependency.

# 9.1.5 Inter-dimensional Relationships

Relationship between causal scenario and model. How does a single model fare across various causal scenarios, and how do different models compare within the same causal scenario? These are the main questions that interest us. To address these, we illustrate the interactions between 28 models and 21 causal scenarios in Figure 9.18. The heatmap in this figure displays the average accuracy for each model within a particular causal scenario, where each cell's number represents this measure. It is essential to acknowledge that the variation in question types across different domains affects the baseline probabilities of a random guess. For instance, in the intervention-related causal scenarios, the random guess probabilities are as follows:  $16.7\%$  for ATE and CDE,  $33.3\%$  for BAS, IV, and FAS, and  $50\%$  for CB and CEI. The accuracy figures shown are the absolute performance metrics for each causal scenario. Hence, when evaluating the heatmap, we should not only consider the depth of color, which illustrates performance levels, but also compare these figures against the baseline random guess probabilities. This comparison will provide a more balanced and objective analysis of model efficacy across different scenarios. Furthermore, we have developed a metric to categorize causal scenarios based on the difficulty levels associated with their respective random guess probabilities, as detailed in Section 6.

Based on Figure 9.18, we can derive the following insights: (1) Causal scenarios that incorporate Mathematical mode, such as ATE, CDE, ETT, NDE, NIE, PN, and PS, pose the most significant challenges for models, as evidenced by the deep red sections of the graph. The inclusion of Mathematical mode in these scenarios

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cbb10d4e2a56c81a320886b57fd97707dfee5167a92e3a35df81eeeb9ce9b1f1.jpg)



Figure 9.18 Relationship between causal scenario and model. Each cell stands for the model's average accuracy in a specific causal scenario.


substantially impacts model performance, leading to a marked decline. This suggests a need for models to improve in handling complex mathematical reasoning within causal contexts. (2) The performance of many models is comparable to, or even less than, what would be expected from random guesses. This observation underscores a general deficiency in the necessary background knowledge for causal reasoning scenarios among most models, indicating biases in their understanding and a limited capacity to follow instructions rigorously. (3) The use of long textual formats introduces additional difficulties for models. For example, the AC scenario, which involves analyzing a relatively long narrative as highlighted in Section 3.6.1, showing a marked performance disparity between the GPT-3 and InstructGPT series models. The challenges associated with processing long texts have become a focal point in recent research, with studies such as those by Chen et al. (2023d) and Wang et al. (2024a) providing practical solutions to enhance model capabilities in handling extensive textual information.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f7dd4c35736b429df5e5263930776bb861d57925ea3979eb4b5276c0c3269c92.jpg)



Figure 9.19 Relationship between scenario and prompt. Each cell stands for the prompt's average accuracy in a specific causal scenario.


Relationship between causal scenario and prompt. Given the diverse range of prompts, we are interested in finding out if there exists a universal prompt that can be beneficial across all causal scenarios, or if distinct causal scenarios require uniquely tailored prompts. This part delves into examining the interaction between our 21 causal scenarios and 9 prompts. The relationships among them are illustrated in Figure 9.19, where each cell in the matrix displays the average accuracy of a specific prompt within a specific causal scenario.

After carefully analyzing the figure, we arrive at these insights: (1) There is no single prompt that consistently outperforms others across all causal scenarios, indicating the absence of a "one-size-fits-all" solution. Although this may complicate the task of identifying the most effective prompt for each scenario, certain prompts significantly enhance performance across most scenarios. For instance, in causal discovery and association scenarios, the use of 1-shot/3-shot IcL has an effective enhancement to model performance. In intervention scenarios (excluding CEI and IV), utilizing 3-shot IcL is the most beneficial, while for counterfactuals scenarios, the manual CoT outperforms others in all but NIE, PN, and AC. As such, it is recommended to select prompts based on the specific requirements of each level of the causal ladder. (2) In particularly demanding causal scenarios, such as PN and PS, most prompts fail to significantly improve model performance, with the exception of 3-shot IcL and manual CoT. However, even these prompts do not raise peak average performance beyond  $8.5\%$ . The lack of a public dataset for evaluating these scenarios may contribute to the models' poor understanding, hindering their ability to address these challenges effectively. Consequently, even with the step-by-step guidance provided by manual CoT, it remains difficult to effectively teach the models to tackle such problems. (3) Increasing the number of samples significantly enhances the performance of the majority of models. When examining 0/1/3-shot IcL and 0-shot/manual CoT, it becomes evident that models yield higher accuracy as sample size increases, aligning with findings from other research (Liang et al., 2022; Xu et al., 2022). However, the feasibility of extensively testing every possible sample size is limited by practical constraints such as time and resources. (4) The 3-shot IcL, 1-shot IcL, and manual CoT prompts have been particularly effective in promoting model performance. The 3-shot IcL prompt provides the most substantial benefits, enabling models to outperform the random guess baseline across 19 causal scenarios, compared to only 7 scenarios with the basic prompt. 1-shot IcL and manual CoT also allow models to perform better than random guessing in 15 and 14 causal scenarios, respectively.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/580fad4179bc8adce5649e86c21eff54dc2b1f568e2565df4f92d24e2a66a09b.jpg)



(a) No causation


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/44b664da6a1d3d9a62deadbd6004fc1993483ee58638982af7b876f4cdbc530d.jpg)



(b) Empty adjustment set


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8e20f41d917c38c01a50bb7de81f4283ee75eb716472790003db99da3c67d3d1.jpg)



(c) Nonempty backdoor adjustment set



Figure 9.20 Illustration of causal reasoning levels. We categorize the difficulty into three levels, arranged from the simplest to the most complex as follows: no causation, empty adjustment set, nonempty backdoor adjustment set. Here,  $X$  represents the treatment,  $Y$  represents the outcome, and  $Z$  represents the confounder.


# 9.1.6 Analyzing Complexity

The analysis and insights from Figures 9.18, 9.19 and 9.1 reveal that tackling causal reasoning tasks within the Mathematical mode<sup>29</sup> poses substantial challenges for models. Understanding the underlying causes of these failures is essential before devising targeted improvements. Therefore, this section is dedicated to exploring the reasons why language models struggle with tasks in Mathematical mode, aiming to inform more effective strategies for enhancing their performance.

Complexity settings. The complexity of causal tasks within the Mathematical mode is determined by four primary factors: (1) Number of nodes: The complexity is gauged by the number of nodes in the causal graph, ranging from 3 to 9, where more nodes indicate a more perplexing structure. (2) Number of edges: The intricacy of each task is measured by the number of edges in the causal graph, which spans from 2 to 10. More edges contribute to a denser and more complicated causal graph, increasing the difficulty of analysis. (3) Authenticity: We have established three different settings of authenticity $^{30}$ , with the complexity progressively increasing. i) Real: Tasks are grounded in real-world phenomena, with questions that are aligned with accurate causal graphs. They conform to empirical common sense and do not cause any disturbances for models. ii) Fake: To test the impact of memorization, nouns within the causal graph are replaced with fictitious terms like "bitk" and "dmfl". This tests models' abilities to process information devoid of real-world context. iii) Random: Nodes in the causal graph are replaced with randomly selected real-world nouns, challenging models to discern causality in a structurally correct but contextually disrupted setup. (4) Causal reasoning process: We structure the process of causal reasoning into three levels as shown in Figure 9.20, where each level represents a step up in complexity and challenge. i) Level-1 (no causation): There is no causal relationship between the treatment and outcome, thus requiring no computation for resolution. ii) Level-2 (empty adjustment set): There exists a causal relationship between the treatment and outcome. Due to the presence of confounders, their backdoor adjustment set is not empty. Table 9.1 details the formulas required for different causal scenarios across various complexity levels, highlighting that the probability at Level 1 is consistently zero, with the computational challenge escalating as the level increases. For a more detailed illustration, Table 9.2 showcases examples of ATE categorized by these complexity levels. These gradations in task complexity pose significant challenges to the causal reasoning capabilities of language models, complicating the assessment of which factors most significantly impact their accuracy.

<table><tr><td>Causal Scenario</td><td>Probability Calculation</td></tr><tr><td colspan="2">Level 1: No causation</td></tr><tr><td>ATE</td><td>0</td></tr><tr><td>CDE</td><td>0</td></tr><tr><td>ETT</td><td>0</td></tr><tr><td>NDE</td><td>0</td></tr><tr><td>NIE</td><td>0</td></tr><tr><td colspan="2">Level 2: Empty adjustment set</td></tr><tr><td>ATE</td><td>P(Y|X=1) - P(Y|X=0)</td></tr><tr><td>CDE</td><td>P(Y|X=1,M) - P(Y|X=0,M)</td></tr><tr><td>ETT</td><td>P(Y|X=1) - P(Y|X=0)</td></tr><tr><td>NDE</td><td>P(Y|X=1) - P(Y|X=0)</td></tr><tr><td>NIE</td><td>∑M P(Y|X=0,M)(P(Y|X=1) - P(Y|X=0))</td></tr><tr><td colspan="2">Level 3: Nonempty backdoor adjustment set</td></tr><tr><td>ATE</td><td>∑Z P(Z)(P(Y|X=1,Z) - P(Y|X=0,Z))</td></tr><tr><td>CDE</td><td>∑Z P(Z)(P(Y|X=1,M,Z) - P(Y|X=0,M,Z))</td></tr><tr><td>ETT</td><td>P(Y|X=1) - ∑Z P(Y|X=0,Z)P(Z|X=1)</td></tr><tr><td>NDE</td><td>∑M ∑Z P(M|X=0,Z)P(Z)(P(Y|X=1,M,Z) - P(Y|X=0,M,Z))</td></tr><tr><td>NIE</td><td>∑M ∑Z P(Y|X=0,M,Z)P(Z)(P(M|X=1,Z) - P(M|X=0,Z))</td></tr></table>


Tab. 9.1 Calculation for three causal reasoning levels.  $X$  represents the treatment,  $Y$  represents the outcome,  $Z$  represents the confounder, and  $M$  represents the mediator.


<table><tr><td>Causal Scenario</td><td>Question</td><td>#Nodes</td><td>#Edges</td><td>Authenticity</td><td>Causal Reasoning Process</td></tr><tr><td rowspan="9">ATE</td><td>Figure B.1</td><td>5</td><td>6</td><td>Real</td><td rowspan="3">Level-1</td></tr><tr><td>Figure B.2</td><td>5</td><td>4</td><td>Fake</td></tr><tr><td>Figure B.3</td><td>5</td><td>8</td><td>Random</td></tr><tr><td>Figure B.4</td><td>3</td><td>3</td><td>Real</td><td rowspan="3">Level-2</td></tr><tr><td>Figure B.5</td><td>3</td><td>2</td><td>Fake</td></tr><tr><td>Figure B.6</td><td>3</td><td>2</td><td>Random</td></tr><tr><td>Figure B.7</td><td>4</td><td>5</td><td>Real</td><td rowspan="3">Level-3</td></tr><tr><td>Figure B.8</td><td>4</td><td>5</td><td>Fake</td></tr><tr><td>Figure B.9</td><td>3</td><td>3</td><td>Random</td></tr></table>

Tab. 9.2 Samples with different complexity factors. The columns titled "#Nodes" and "#Edges" stand for "number of nodes in the given causal graph" and "number of edges in the given causal graph", respectively. Due to space limit, all examples are included in Examples for Analyzing Complexity (Appendix B.1).

What lead to the models' failure? Figure 9.21 depicts how the model's average accuracy varies with the four complexity factors. To mitigate the effects of variations in causal scenarios and prompt configurations, we compute the average accuracies across five causal scenarios (ATE, CDE, ETT, NDE, and NIE) and all nine prompts. Due to the universally low accuracy rates observed in Mathematical mode causal tasks, we focus on the top five performing language models, as ranked in the Mathematical histogram presented in Figure 9.1. We use relative accuracy as our metric, defined as the ratio of correct responses to the total number of

samples within a category. This method ensures fairness in comparison, accommodating for the variability in the number of problems across different complexity factors.

From the analysis of the four sub-figures in Figure 9.21, we arrive at several insights:

(1) Present-day language models struggle significantly with complex causal reasoning tasks. Insights from the sub-figure focusing on the causal reasoning process reveal a marked decline in model performance as complexity increases to level 3. At this most challenging level, the accuracy of all five models examined nearly drops to zero, underscoring their substantial difficulties with high-complexity questions. Level 3 involves scenarios with confounders in the causal graph, requiring models to not only grasp causal concepts thoroughly but also to execute precise reasoning and calculations. This indicates a critical gap in current models' capabilities when faced with intricate causal relationships.

(2) GPT-4 stands out for its superior handling of relatively complex causal reasoning tasks. The sub-figure of causal reasoning process, particularly the curve between levels 1 and 2, highlights a distinctive pattern. Although GPT-4 starts as the fourth-ranked model at level 1, its relative accuracy remains robust, barely diminishing and sustaining above  $30\%$  as the task complexity increases to level 2. In comparison, Claude2, which is the second-best performer at level 2, also manages to significantly mitigate its performance drop. By contrast, GPT-3.5-Turbo and text-davinci-003, despite strong performances at level 1, undergo a sharp decrease in accuracy upon transitioning to level 2, with GPT-3.5-Turbo showing a notably larger decline. Meanwhile, Llama2 (70B) displays minor fluctuations in performance but maintains approximately  $10\%$  accuracy at both levels, indicating a lower overall effectiveness in these tasks.

(3) Overall, the random setting (of authenticity) exerts the most profound effect on the performance of models. When examining the authenticity sub-figure, which uses the real setting (of authenticity) as a reference point due to its reflection of actual causal relationships, it is clear that all models experience a decrease in effectiveness under the random setting, as anticipated. This decline is attributed to the causal graph configuration where, despite nodes corresponding to real-world entities, the causal relationships are incorrectly aligned with reality. Thus, the causal graph in the random setting presents information that diverges from the models' training data, leading to substantial disruptions. Consequently, this challenges models not only to accurately identify the causal relationships but also to compartmentalize and disregard their pre-existing knowledge, which poses a significant challenge to their processing efficiency.

(4) The models exhibit a certain level of abstract reasoning capability. Let us refocus on the authenticity sub-figure, with the real setting (of authenticity) as the reference. It is observed that, with the exception of Llama2 (70B) and GPT-3.5-Turbo, the other three models exhibit improved performance in the fake setting. In this setting, nodes are labeled with fictitious names that lack real-world significance. This performance suggests that these three models can effectively detach from real-world references and engage in causal reasoning within abstract contexts.

(5) Variations in the number of nodes and edges in a causal graph only marginally affect the performance of models. Analysis from the two corresponding sub-figures in Figure 9.21 reveal that all models experience a decline in performance when the node count increases from 3 to 5 and the edge count from 2 to 4. Interestingly, a general improvement in performance is observed as the node count rises from 6 to 9. This trend is attributed to the increased proportion of Level 1 questions in the dataset creation process. Given that some of the 28 evaluated models have a context window limited to 2,000 tokens (see Models (Section 8) for details), ensuring that the question length stays within this limit necessitates a trade-off between the number of nodes and the complexity of the causal reasoning process. That is, we need to maintain a balanced number of input

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6b654c6f3c776dcfd1989444694bac0eaef88a0177c8b6b57a6ed0ae52e7206c.jpg)



Figure 9.21 Complexity analysis of Mathematical mode questions. We calculate the average accuracy of all evaluated models across five causal scenarios that involve Mathematical mode questions (i.e., ATE, CDE, ETT, NDE and NIE). The figure illustrates how accuracy trends vary under four different factors (i.e., number of nodes, number of edges, authenticity, and causal reasoning process) affecting the complexity.


tokens with the addition of more nodes. More specifically, as the node count rises, more tokens are needed to describe the causal graph in the input. In contrast, there is no causal relationship between the treatment and outcome in the level 1 questions, so these questions require the fewest tokens for providing probability-related context. That is why we construct more level 1 questions as the nodes within a causal graph increase. This suggests that the addition of nodes does not significantly impact performance as long as the complexity of causal reasoning remains constant. Ultimately, it is the complexity of the causal reasoning process itself that primarily determines model performance.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ac803b61410c5313e0da8ab1084c74bbe7051d00e7aa4b0b1e58f57b9537980a.jpg)



Figure 9.22 Maturity of causal scenarios. We evaluate the maturity of a causal scenario by examining the following three metrics: understandability, open-limited gap, and solvability. In the figure, the areas labeled as “√” represent the corresponding maturity stages of the causal scenario.


# 9.1.7 Analyzing Maturity

We evaluate 21 distinct causal scenarios, each designed to evaluate different aspects of a model's capabilities. Understanding the maturity levels of these scenarios is crucial for advancing and deploying future models. A high maturity level indicates that a scenario has been effectively solved, while a low maturity level suggests significant room for further exploration. To thoroughly evaluate the maturity of these scenarios and mitigate potential biases from singular metrics, we have established three key metrics: understandability, open-limited gap, and solvability, as detailed in Section 6.4.

Utilizing the computation methods described in Section 6.4, we assess the maturity levels for each causal scenario, presented in Figure 9.22. Our conclusions are as follows: (1) CaLM poses significant challenges in understandability. While all causal scenarios within the causal discovery category are deemed easy, aligning with our initial perceptions, a majority of the scenarios (15 out of 21) are rated as hard or more difficult. This underscores the complexity of CaLM in terms of model comprehension. (2) When examining the open-limited gap, there remains a considerable persistent gap between open and limited-access models. In most scenarios (17 out of 21), this gap is moderate to high, suggesting that models with limited access still outperform their open-access counterparts, maintaining dominance in the top 5 positions for each scenario. (3) In terms of solvability, although no causal scenarios are deemed unsolvable, current models do not fully meet the challenges posed by CaLM. Almost half (10 out of 21) of the causal scenarios are classified as challenging.

# 9.1.8 Analyzing Volatility

Assessing the robustness of a model solely through adversarial prompts may present some limitations, because it primarily focuses on whether there are changes in the model's response before and after encountering

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/427c319805ba58ba86c69ff26cf9b1fd2ae6422bd9f91a23de8a895b640b5759.jpg)



Figure 9.23 Volatility of prompts. Each cell stands for the prompt's average volatility in a specific causal scenario.


interference. This section expands the evaluation of robustness by considering stability from a broader viewpoint, consisting of both the model's and the prompt's volatility. $^{31}$  The volatility of the model refers to the inconsistency in the model's responses to variations in prompts within a specific causal scenario, averaged across all prompts. High volatility in this context suggests that the model is highly sensitive to changes in the prompt, leading to decreased stability. In contrast, the volatility of the prompt indicates the instability of a prompt's performance relative to the basic prompt across all models in a particular causal scenario. Increased volatility here means a greater disparity in performance compared to the basic prompt, also reflecting reduced stability. In both cases, our concern is with the magnitude of these disparities, which do not necessarily reflect the absolute performance quality of the model. For example, a model with high volatility might perform modestly under the basic prompt but show significant improvement with a specific prompt. This highlights the considerable potential within the model that may be leveraged through tailored prompt engineering.

Volatility of prompt. In Figure 9.23, we illustrate the volatility of prompts across all causal scenarios. Each value in the heatmap represents the deviation of a prompt's volatility from that of the basic prompt within a given causal scenario. This is why the basic prompt is not shown in the figure. Note that, the EF prompt is not included in the volatility calculation, because it is not used in some causal tasks and, according to findings from both Figure 9.11 and Figure 9.12, there is a significant correlation between the EF and the basic prompt. We believe that excluding EF does not undermine the validity of our conclusions.

From Figure 9.23, we can see that both 3-shot IcL and manual CoT exhibit the highest volatility. Noteworthy, we have observed from Figure 9.11 that there is a weak correlation between these prompts and the basic prompt. Since prompt volatility is measured relative to the basic prompt, the elevated volatility of 3-shot IcL and manual CoT corroborates the findings in Figure 9.11 and Figure 9.12. Additionally, both Figure 9.4 and Figure 9.19 suggest that, compared to basic prompt, 3-shot IcL and manual CoT significantly enhance model performance. This finding is consistent with their observed high volatility, as the baseline for calculating volatility of prompt is the model's accuracy with the basic prompt.

Volatility of model. Figure 9.24 visualizes the model's volatility across all causal scenarios. Each cell in the heatmap represents the model's volatility across all prompts within a specific causal scenario. From this figure,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9bb7a9d65151cf3220c2a8b99c8a244f0039d835a39ea4882cba0247dcfc360c.jpg)



Figure 9.24 Volatility of models. Each cell stands for the model's average volatility in a specific causal scenario.


we can see that the model's stability seems to correlate with the causal ladder. For causal scenarios within the relatively simpler levels of the ladder, such as causal discovery and association, the model generally exhibits lower volatility, indicating higher stability. In contrast, causal scenarios within the more challenging levels, such as intervention and counterfactuals, tend to show higher volatility, reflecting lower stability. However, there are exceptions within the more difficult levels. PN and PS, which are categorized under counterfactuals, display significantly lower volatility, with some models even achieving zero volatility. Analysis from both Figure 9.18 and Figure 9.19 reveals that these scenarios are particularly challenging, characterized by low model accuracy and minimal influence from prompts. This explains the distinctively high stability observed in PN and PS scenarios, consistent with findings from Figure 9.13.

<table><tr><td>Model</td><td>Empty</td><td>Instruction</td><td>Repetition</td><td>Inconsistency</td><td>Average</td></tr><tr><td>Baichuan1 (7B)</td><td>4.6</td><td>44.7</td><td>33.7</td><td>5.6</td><td>22.2</td></tr><tr><td>Baichuan1-chat (13B)</td><td>0.0</td><td>71.4</td><td>1.6</td><td>7.3</td><td>20.1</td></tr><tr><td>Baichuan2-chat (7B)</td><td>0.0</td><td>54.8</td><td>0.8</td><td>5.7</td><td>15.3</td></tr><tr><td>Baichuan2-chat (13B)</td><td>0.0</td><td>64.3</td><td>0.6</td><td>9.3</td><td>18.6</td></tr><tr><td>Qwen (7B)</td><td>9.6</td><td>41.7</td><td>22.2</td><td>4.9</td><td>19.6</td></tr><tr><td>Qwen (14B)</td><td>6.7</td><td>48.9</td><td>20.2</td><td>4.9</td><td>20.2</td></tr><tr><td>InternLM-chat (7B)</td><td>0.0</td><td>15.0</td><td>0.1</td><td>3.1</td><td>4.6</td></tr><tr><td>InternLM-chat (20B)</td><td>4.0</td><td>28.3</td><td>0.2</td><td>6.2</td><td>9.7</td></tr><tr><td>Llama2 (7B)</td><td>3.2</td><td>55.5</td><td>28.0</td><td>8.3</td><td>23.8</td></tr><tr><td>Llama2 (13B)</td><td>8.4</td><td>55.5</td><td>25.0</td><td>6.3</td><td>23.8</td></tr><tr><td>Llama2 (70B)</td><td>17.5</td><td>64.1</td><td>26.9</td><td>8.3</td><td>29.2</td></tr><tr><td>Llama2-chat (70B)</td><td>7.0</td><td>60.7</td><td>17.5</td><td>13.7</td><td>24.7</td></tr><tr><td>Koala (13B)</td><td>4.5</td><td>41.2</td><td>22.8</td><td>4.4</td><td>18.2</td></tr><tr><td>Wizardcoder (15B)</td><td>6.3</td><td>65.3</td><td>3.9</td><td>3.3</td><td>19.7</td></tr><tr><td>Vicuna-v1.3 (33B)</td><td>2.3</td><td>49.7</td><td>3.3</td><td>5.9</td><td>15.3</td></tr><tr><td>ada (0.35B)</td><td>0.0</td><td>68.6</td><td>40.9</td><td>4.2</td><td>28.4</td></tr><tr><td>text-ada-001</td><td>0.0</td><td>53.7</td><td>5.1</td><td>11.4</td><td>17.6</td></tr><tr><td>babbage (1.3B)</td><td>0.0</td><td>67.7</td><td>41.1</td><td>3.7</td><td>28.1</td></tr><tr><td>text-babbage-001</td><td>0.1</td><td>36.4</td><td>3.9</td><td>2.5</td><td>10.7</td></tr><tr><td>curie (6.7B)</td><td>0.0</td><td>57.2</td><td>52.3</td><td>3.1</td><td>28.2</td></tr><tr><td>text-curie-001</td><td>0.0</td><td>38.6</td><td>2.8</td><td>2.4</td><td>11.0</td></tr><tr><td>davinci (175B)</td><td>0.0</td><td>51.0</td><td>40.7</td><td>3.7</td><td>23.9</td></tr><tr><td>text-davinci-001</td><td>0.0</td><td>10.4</td><td>1.5</td><td>1.4</td><td>3.3</td></tr><tr><td>text-davinci-002</td><td>0.0</td><td>9.0</td><td>1.9</td><td>0.7</td><td>2.9</td></tr><tr><td>text-davinci-003</td><td>0.0</td><td>4.7</td><td>0.2</td><td>0.8</td><td>1.4</td></tr><tr><td>GPT-3.5-Turbo</td><td>0.0</td><td>10.3</td><td>0.1</td><td>0.8</td><td>2.8</td></tr><tr><td>GPT-4</td><td>0.0</td><td>11.0</td><td>0.0</td><td>0.6</td><td>2.9</td></tr><tr><td>Claude2</td><td>0.7</td><td>64.9</td><td>0.8</td><td>6.2</td><td>18.2</td></tr><tr><td>Average</td><td>2.7</td><td>44.5</td><td>14.2</td><td>5.0</td><td>16.6</td></tr></table>

Tab. 9.3 Error stastics. The table includes the occurrence rates of the four errors and their average values. Here, Empty denotes empty response, Instruction denotes limitation of instruction-following, and Inconsistency denotes language inconsistency.

# 9.1.9 Analyzing Errors

During the evaluation, we document the errors made by the models and conduct both quantitative and qualitative analyses in this section. By examining the errors from these two perspectives, we can gain a deeper understanding of the models' shortcomings that lead to suboptimal performance. This analysis not only helps identify areas for immediate improvement but also provides valuable insights that can guide enhancements in future research.

Quantitative analysis of empty response, limitation of instruction-following, repetition, and language inconsistency. In Table 9.3, we detail the proportions of four types of errors $^{32}$  (i.e., empty response,

limitation of instruction-following, repetition, and language inconsistency) that the models exhibit across all causal scenarios and eight types of prompts (excluding EF, for reasons consistent with Analyzing Volatility). Through both horizontal and vertical analyses on this table, we can draw the following conclusions: (1) The most frequent error category is the limitation of instruction-following, whereas the least common is the empty response. This indicates that the models generally manage to generate responses, rarely failing to provide any output even when faced with challenging questions. However, their precision in adhering to specific instructions is still wanting, often struggle to produce responses in the exact format required (see Adaptations (Section 5) for detailed required output formats). (2) SFT significantly reduces the incidence of repetitive responses. By finetuning with high-quality input-output pairs, SFT helps prevent unnecessary repetition in the models' responses (for an in-depth analysis of training strategies, refer to Models (Section 8)). (3) Models exhibit varying levels of language inconsistency, ranging from  $0.6\%$  to  $13.7\%$ . Although this issue may not significantly affect the final accuracy (as extensive sampling is employed when calculating this metric), it can severely degrade the user experience in real-world applications. For example, a non-English-speaking user receiving responses containing English terms when asking a question in Chinese would find this problematic. (4) On average, models from the text-davinci and InternLM series, along with ChatGPT and GPT-4, tend to make the fewest errors. (5) Overall, limited-access models have a lower error rate  $(13.8\%)$  than open-access models  $(19.0\%)$ .

Subsequent to our initial findings, we further explored the impact of different prompts on the models' error occurrence by creating four heatmaps in Figure 9.25. Each value in these heatmaps represents the average percentage of a specific error made by the models in a given causal scenario when using a particular prompt. From our analysis of this figure, we discover the following insights: (1) Both 1-shot IcL and 3-shot IcL can significantly improve the ability of most models to follow instructions. Our experiments demonstrate that providing models with standardized, succinct examples enables them to learn effective response patterns, thereby improving their ability to generate outputs that adhere closely to the required answer format. (2) 1-shot IcL, 3-shot IcL, and manual CoT lead some models to engage in an "imitation game". These prompts provide examples that encourage models to mimic the observed patterns. As a result, these models not only produce responses but also generate their own questions, reflecting the structure and style they "learned" from the prompts. (3) Adversarial prompts tend to increase the occurrence of empty responses, particularly in models from the Llama series (i.e., the Llama2-series models, Koala (13B), and Vicuna-v1.3 (33B)). This suggests that these models may struggle to generate any relevant output when challenged by particularly tricky or misleading prompts. (4) 0-shot CoT causes a higher incidence of language inconsistency especially evident in models like Llama2 (70B). These models face challenges in methodically processing and responding to complex questions in Chinese according to the instructions. They often begin with off-topic replies in Chinese and then switch to English, although these English responses do not align with the original question's intent. To better illustrate this issue, we provide an example in Figure 9.26.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8eb33fde8524f92021757063dac68379e1833a503179361833dfa55dde1e57cd.jpg)



Figure 9.25 Relationship between error and prompt. Each cell stands for the average percentage of a specific type of error made by the corresponding models across 21 causal scenarios using a specific prompt. The frequency of different types of errors varies. For clearer presentation of the results, we choose distinct upper and lower limits and colors for each error type.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/dc33bc058e4d8f8bd8207095de70e742c0e09f6c520df1a4cfdcc4018b7448f1.jpg)



Figure 9.26 0-shot CoT's impact on language inconsistency.


Quantitative analysis of same response to all questions. Our analysis extends to the final category of quantitative error: same response to all questions. In CaLM, this particular error is broken down into six distinct sub-types, as detailed in Quantitative (Section 7.2). We begin by aggregating the total occurrences of each category in Table 9.4, offering an initial overview. Furthermore, the results for all models across 46 causal tasks and all prompts are summarized in Figure 9.27. Our methodology for tracking this error involves considering all prompts; once a model repeats an error on any prompt, it is recorded.

From a thorough analysis of Figure 9.27, we draw the following conclusions: (1) The issue of providing the same response to all questions is widespread and requires urgent attention. Some suggest that adjusting parameters like temperature might reduce this error, but we contend that such adjustments fail to address the underlying problem. Rather than merely seeking a wider variety of responses, the consistent issuance of the same answer across all questions in a causal task points to a fundamental misunderstanding of the questions themselves. Notably, InternLM-chat (7B) and InternLM-chat (20B) stand out as they do not exhibit this error, showcasing their exceptional performance in this aspect. (2) The type of question does not significantly influence the occurrence of the same response to all questions. In other words, the behavior of the models show consistency in this case. This consistency suggests that if a model exhibits this error in one type of question (e.g., binary classification), it is likely to occur across other types (e.g., choice selection, probability calculation). (3) Limited understanding of prompts can result in the misinterpretation of instructions. For causal tasks in Mathematical mode, our prompt contains a specific instruction: "Provide the calculation result

<table><tr><td rowspan="2">Same Response</td><td colspan="3">Binary Classification</td><td>Choice Selection</td><td colspan="2">Probability Calculation</td></tr><tr><td>All Yes</td><td>All No</td><td>Y &amp; N</td><td>All Same Choice</td><td>All 0.1234</td><td>All 0</td></tr><tr><td># Occurrence</td><td>153</td><td>77</td><td>78</td><td>55</td><td>61</td><td>6</td></tr></table>

Tab. 9.4 Overview of same response to all questions.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1ab65ba3e184b5da9e0d54f05f2e79b747dac21ec799ea91f9b965497ed2533c.jpg)



Figure 9.27 Same response to all questions error. The figure documents instances where the model exhibits the same response across 46 causal tasks, taking into account all prompts. "All SC" denotes all same choice, "Y & N" denotes situations where "All yes" and "All no" responses are observed across various prompts, "0.1234" and "All 0" indicate cases in probability calculation where the outputs are consistently 0.1234 and 0, respectively.[33]


to four decimal places in JSON format, like {"PROB": "0.1234"} We observe that some models, including GPT-4, repeatedly return "0.1234" for tasks involving probability calculations, suggesting that these models are overly influenced by the prompt.

# Qualitative: Causal hallucination

# Prompt:

事件一：卢克的后背受到了外界压力。

事件二：卢克有权召开会议。

问题：事件一和事件二之间是否存在因果关系？请逐步思考。

答案（是或否？）：

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/848bf3a4b5b3c504c3761bfa69b4cb1163da2dac2eea16fe6ba71aa90f7b31ba.jpg)


GPT-3.5-Turbo

# 是

Ground truth: 否


Figure 9.28 Case of causal hallucination. The red text indicates the wrong response.


# Qualitative: Inferential ambiguity

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Customer satisfaction with a product has a direct effect on number of positive reviews for the product.

Customer satisfaction with a product has a direct effect on revenue generated from the product. Number of positive reviews for the product has a direct effect on sales performance of the product. Sales performance of the product has a direct effect on revenue generated from the product.

Instruction: Consider the average treatment effect (ATE) of revenue generated from the product on customer satisfaction with a product.

Question: If revenue generated from the product is changed to be high, will customer satisfaction with a product be more likely to be low?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4f7e42c67c3a4ff70c1426ad44bd3ef750fb12f984f33d66e2c5fc8c2698cb3b.jpg)


GPT-4

{"ANSWER": "No", "PROB": "Not Applicable"}

Ground truth:

{"ANSWER": "No", "PROB": "0.0000"}


Figure 9.29 Case of inferential ambiguity. The red text indicates the wrong response. The green text indicates the right response.


Qualitative analysis of causal hallucination. Figure 9.28 provides an illustrative example of causal hallucination. In this instance, GPT-3.5-Turbo mistakenly establishes a cause-and-effect relationship between two unrelated events, which signifies the occurrence of causal hallucination. While such errors can occasionally spur creative solutions or enhance critical analysis skills, they more often lead to incorrect conclusions and flawed decision-making. Moreover, the model does not follow the instruction to provide a step-by-step analysis. This error emphasizes the necessity to mitigate or correct causal hallucination, ensuring more accurate, reliable, and contextually aware responses in future applications.

Qualitative analysis of inferential ambiguity. To elucidate inferential ambiguity, we reference an example in Figure 9.29. In the question, GPT-4 is tasked to offer a precise probability measure in its response. The correct answer should be a definitive "No" with a probability of "0.0000". While the model's response of "No" accurately conveys that higher revenue does not lead to lower customer satisfaction, the accompanying "Not

# Qualitative: Calculation error

# Prompt:

[Omit the Manual CoT example]

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Government policies has a direct effect on education level. Government policies has a direct effect on rainfall.

Sales performance has a direct effect on education level. Sales performance has a direct effect on blood pressure. Education level has a direct effect on blood pressure. Education level has a direct effect on rainfall. Blood pressure has a direct effect on rainfall.

For those with government policies being high, the probability of rainfall being low is 0.1161. The probability of rainfall being low is 0.3182. The probability of government policies being low and rainfall being low is 0.2609.

Instruction: Consider the probability of sufficiency (PS) of government policies on rainfall.

Question: Given that government policies was low and rainfall was low, what is the lower bound of the probability that rainfall would have been high if the government policies had been high?

Provide the calculation result to four decimal places in JSON format, like {"PROB": "0.1234"}:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/93aea97127f326932a1601f45f741624878077f4aaf5d6e3fd0ba453ecec34da.jpg)


# GPT-4

With A represents government policies and C represents rainfall, we have  $\mathsf{P}(\mathsf{C} = 0|\mathsf{A} = 1) = 0.1161$ ;  $\mathsf{P}(\mathsf{C} = 0) = 0.3182$ ;  $\mathsf{P}(\mathsf{A} = 0,\mathsf{C} = 0) = 0.2609$ ;

Calculate  $P(C = o|do(A = 1)) = P(C = o|A = 1) = 0.1161$ , then the lower bound of PS is max{o, [P(C = o)-P(C = o|do(A = 1)]/P(A = o, C = o)}

$= \max \{0,(0.3182 - 0.1161) / 0.2609\}$

=max{0,0.7753}

$= 0.7753$  .The answer is: {"PROB": "o.7753)}.

# Ground truth:

With A represents government policies and C represents rainfall, we have  $P(C = 0|A = 1) = 0.1161$ ;  $P(C = 0) = 0.3182$ ;  $P(A = 0, C = 0) = 0.2609$ .

Calculate  $P(C = o|do(A = 1)) = P(C = o|A = 1) = 0.1161$ , then the lower bound of PS is max{0, [P(C = o) - P(C = o|do(A = 1)] / P(A = 0, C = 0)}

$= \max \{0,(0.3182 - 0.1161) / 0.2609\}$

=max{o,0.7746}

$= 0.7746$  .The answer is: {"PROB": "o.7746"}.


Figure 9.30 Case of calculation error. The red text indicates the wrong response. The green text indicates the right response.


Applicable" fails to supply the probability requested by the query. This statement introduces ambiguity, as it does not clearly denote the absence of a causal relationship between the treatment and outcome. Consequently, such a response could lead to misinterpretation by users, who might perceive it as signifying uncertainty or the influence of unknown factors on the relationship.

Qualitative analysis of calculation error. In Figure 9.30, we present a case study involving the calculation error, which can be analyzed from two perspectives. On the positive side, GPT-4, to certain extent, demonstrates a creditable understanding of causal reasoning. It correctly identifies the cause-effect pair and the necessary conditions for the calculation, further applying the correct formulas and methodological steps to approach the problem. The response is structured in a logically coherent sequence that is easy to follow, showcasing the model's capability in conceptual comprehension. However, GPT-4 falls short in executing basic arithmetic, resulting in a wrong answer. This error not only compromises the accuracy of the response but also highlights a deficiency in the model's computational reliability. Such errors are particularly consequential in fields that demand precise statistical analysis and can significantly affect the credibility and applicability of the model's outputs in real-world scenarios.

Qualitative analysis of incorrect reasoning. Figure 9.31 features an example of incorrect reasoning in causal analysis performed by Baichuan2-chat (13B). In its analysis of a given causal graph, the model

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/778982090ac0839eaa415718632193368db92ff7f509d4fc1c29a505876b1c3a.jpg)



Figure 9.31 Case of incorrect reasoning. The red text indicates the wrong response.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/e5ce8fb7241aab7eaa1ef594296886e4d8add34f64f5a8a689766294c23a1c51.jpg)



Figure 9.32 Case of misunderstanding. The red text indicates the wrong response. The green text indicates the right response.


incorrectly concludes that "A does not cause  $E$ ", by overlooking the explicit prompt statement that "A causes  $E$ ". This oversight results in fundamentally flawed reasoning. Although the model logically structures its response by exploring the causal chain through intermediate events (" $B$ ", "C", and "D"), it fails to incorporate all relevant data, particularly the direct causal link provided in the prompt. The model's analysis of indirect relationships underscores its ability to parse a causal graph effectively. However, its critical error in overlooking a direct causal relationship highlights a significant gap in its capacity for comprehensive data integration. This example

# Qualitative: Contradiction

# Prompt:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Whether a student studies for an exam or not has a direct effect on the grade obtained on the exam. The grade obtained on the exam has a direct effect on whether the student passes the course or not.

For those with the grade obtained on the exam being low, the probability of whether the student passes the course or not being pass is 0.2202. For those with the grade obtained on the exam being high, the probability of whether the student passes the course or not being pass is 0.0126.

Instruction: Consider the average treatment effect (ATE) of the grade obtained on the exam on whether the student passes the course or not.

Question: If the grade obtained on the exam is changed to be low, will whether the student passes the course or not be more likely to be pass?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9eb3dbb75b9a59f24f6fd34e6fd1f2d76fbd95e0efad9ba9413893085a50ab6c.jpg)


# Vicuna-v1.3 (33B)

```
```
```
```
```
```
``

"ANSWER": "Yes" | "No",

"PROB": "0.1234" | "0.8765"

Ground truth: {"ANSWER": "Yes", "PROB": "0.2076"};


Figure 9.33 Case of contradiction. The red text indicates the wrong response.


illustrates the importance of ensuring that models not only follow logical structures in their reasoning but also accurately integrate all pertinent information to avoid substantial inaccuracies in their conclusions.

Qualitative analysis of misunderstanding. In Figure 9.32, we encounter a clear example of misunderstanding in the response from Llama2-chat (70B). The model misinterprets the question by focusing on identifying common causes of  $E$  rather than applying the Front-door criterion (Pearl, 1995). This also demonstrates a deficiency in the model's comprehension of the Front-door criterion. While it correctly identifies  $D$  and  $C$  as the common causes of E, the question specifically requires identifying which variable satisfies the Front-door criterion relative to the pair  $(A,E)$ . This criterion requires a variable to be a mediator on the causal path from  $A$  to  $E$ , blocking all backdoor paths between them. The model's response fails to address this critical requirement, resulting in an answer that is both inaccurate and incomplete. Additionally, the inclusion of an unrelated name, "Lan", further detracts from the coherence and relevance of the analysis. Overall, the model's response exhibits a fundamental misunderstanding and fails to deliver a relevant and correct answer to the causal reasoning question posed.

Qualitative analysis of contradiction. Figure 9.33 illustrates a case of contradiction, demonstrating a dual error in both binary classification and probability calculation. In this instance, Vicuna-v1.3 (33B) produces contradictory responses by simultaneously generating both "Yes" and "No" answers, each accompanied by distinct probabilities. This contradictory output fails to provide a definitive and reliable answer, resulting in confusion rather than clarity. The model's intention of offering multiple possibilities might be aimed at acknowledging uncertainty or accounting for different scenarios. However, the current execution is counterproductive and undermines the model's credibility. As indicated by the prompt, the response should

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f621f83c8b5c6a1369b89e34a7b1a174bbd72332ee49cfac43c9c3ba4179a917.jpg)



Figure 9.34 Case of outlier. The red text indicates the wrong response.


ideally converge on a single, well-supported answer accompanied by a corresponding probability, reflecting a clear and unambiguous conclusion based on the analyzed data.

Qualitative analysis of outlier. To better understand the concept of an outlier in model responses, we present a vivid example in Figure 9.34. The response from Llama2 (7B) obscures the causal reasoning process and logical analysis with irrelevant content. To be specific, it provides bibliographic references to books that appear unrelated to the question posed and may even be nonexistent. This misalignment between the content and the references serves as a significant hindrance, emphasizing the importance of ensuring that cited materials directly support the query at hand. This is a clear outlier response, failing to address the query in a meaningful way. In essence, the outlier error diminishes the effectiveness and clarity of the response. It fails to provide any useful information, leaving the question unanswered and potentially causing frustration or confusion. Additionally, it wastes time and resources by offering irrelevant content.

Qualitative analysis of hybrid errors. In certain situations, the model might exhibit multiple errors simultaneously. Figure 9.35 showcases a typical instance, displaying errors such as causal hallucination, incorrect reasoning, and contradiction. Firstly, it suffers from causal hallucination by introducing a non-existent causal relationship (" $F$  causes  $D$ )", an assertion that diverges from the factual input. As a result, this baseless assertion leads to incorrect reasoning, as the subsequent reasoning hinges on this false premise. Furthermore, the response is marred by a glaring contradiction: it affirms that " $F$  does not cause  $E$ ", but then concludes " $F$  causes  $E$ ". This amalgamation of errors significantly detracts from the credibility of the analysis. Despite these shortcomings, we do notice that the response attempts to provide a step-by-step explanation,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/83e45a73e50bf0cf362fc137dc51e4e707a0ba08c936c8fdc8b4a47d38e98a36.jpg)



Figure 9.35 Case of hybrid errors. The red text indicates the wrong response. The green text indicates the right response.


demonstrating a semblance of logical reasoning. Additionally, it identifies the correct causal relationships between “ $D$ ”, “ $E$ ”, and “ $F$ ”. However, the inconsistencies and inaccuracies in the response underscore a deficiency of causal reasoning ability, resulting in a conclusion that lacks coherence and factual basis.

# 9.2 Prompt Analysis

While our analysis of prompts in Main Results (Section 9.1) has been comprehensive, it remains at a macro level, focusing on broad topics such as prompt-centric relationships, relationships between causal scenarios and prompts, and volatility of prompts. In this section, we will delve deeper into the specific characteristics of each type of prompt. Our goal is to further explore how prompts affect model performance from various angles, including the number of examples in a prompt, interference by adversarial prompts, and the format of the prompts. This detailed examination will contribute to the advancement of both prompt design and model development. This section will be organized into four parts: In-context Learning (IcL) (Section 9.2.1), Adversarial Prompt (Section 9.2.2), Chain-of-Thought (CoT) (Section 9.2.3), and Explicit Function (EF) (Section 9.2.4), each focusing on a specific prompting strategy.

# 9.2.1 In-context Learning

Number of in-context examples. For most scenarios, we use 0, 1, and 3 in-context examples for comparative analysis. The rationale for selecting these specific numbers was to strike a balance between the costs associated with increased token length and the benefits derived from IcL. According to Liang et al. (2022), who examined the impact of varying the number of IcL examples from 0 to 16, it was observed that the most significant effects often occurred with fewer than 3 examples. Although our evaluations generally involve 0, 1, and 3 shots, the token length constraints of some limited-access models such as ada (0.35B) require us to adjust the number of examples used in certain scenarios - reducing to 2 for some English Mathematical mode contexts and to 1 for Chinese, due to the excessive length of the context.

Our experiments with 0, 1, and 3 IcL examples reveal that the most substantial improvements, observed

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/52719ee8e9e3e469d181df7904cd934619b939418fce433829d7e4d8a4a45aa0.jpg)



(a) Average accuracy of IcL for scenarios in the Natural and Symbolic modes.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3912da91302b77cb102ab361f42d6ab8646159f4a3798ff421f2f32a0939c0ed.jpg)



(b) Average accuracy of IcL for scenarios (c) Average accuracy of IcL for scenarios in the Mathematical mode with  $0/1/3$  ex-in the Mathematical mode with  $0/1/2$  examples.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/fb8049f017dcc2ae6e796fed6edced6e86bea75d7bbf39846f03729c019ba6bc.jpg)



Figure 9.36 Relationship between accuracy and the number of IcL examples.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/43d306105df22527b08ccdeb22db7e9ee237e3647e9ae66b35760d4552f717dd.jpg)



(a) Accuracy trends classified by modes and question types.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6f34a640ea6a8c368ed5a1434f2402ff4bd8a441726ea3479a12c639f0dd22cb.jpg)



(b) Accuracy trends classified by the levels of the causal ladder.



Figure 9.37 Impact of IcL example numbers on accuracy. "O" denotes open-ended generation, "B" denotes binary classification, "BC" denotes both binary classification and choice selection, and "P" denotes probability calculation.


in 13 out of 14 Natural and Symbolic mode scenarios tested in both English and Chinese, typically occur when increasing from 0 to 1 example, as depicted in Figure 36(a). Interestingly, the inclusion of 3 examples sometimes resulted in negative improvements compared to using just 1 example. In contrast, 5 out of 7 scenarios in the Mathematical mode demonstrate a more significant improvement when moving from 1-shot to 2 or 3 shots, as illustrated in Figure 36(b) and Figure 36(c). Given a longer window size of model, We encourage further research to explore the model's optimal performance in Mathematical mode scenarios using IcL. Additionally, we analyze the accuracy trend focusing only on English datasets in Mathematical mode scenarios in Figure B.10. We observe that the trend of each scenario in this figure matches closely with Figure B.10(b) and (c), respectively.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4bee8d2479f308434313f9527e637fe6058b9f9a85a25813ae42488364a77ac2.jpg)



(a) Average trends classified by modes


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/7a9197b8939edb4e8cb0ad824fa3673334342a40b0bb74bf979833f37f54aace.jpg)



(b) Average trends classified by question types


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a2986e9f489dc380b80763b0af1d6622819701d29463185fadcf603f18f5ce25.jpg)



(c) Average trends classified by levels of the causal ladder



Figure 9.38 Accuracy trends across various factors.


Effectiveness of in-context learning. In our analysis, we categorize the performance trends of IcL across various tasks based on different criteria. We discover that classifying tasks based on their modes and question types facilitates the most coherent categorization, with tasks within the same category exhibiting similar performance trends. This approach to categorization demonstrates a clearer pattern than grouping by task difficulty, which often results in more intertwined outcomes. This suggests that the effectiveness of IcL is more closely associated with the task's mode and question type than with its level of difficulty.

We now investigate the average performance trends across various modes, question types, and causal scenarios, as illustrated in Figures 38(a), 38(b), and 38(c). We find that IcL examples tend to be more effective in more challenging tasks, particularly those within the Mathematical mode, such as probability calculations and tasks at the counterfactuals level. In contrast, simpler tasks show comparatively smaller gains from the implementation of IcL.

Additionally, we analyze the effects of classifying tasks by modes and question types, as depicted in Figure 9.39. For open-ended generation tasks in the Natural mode (Figure 39(a)), IcL does not enhance performance. However, for the tasks involving binary classification or choice selection in the Natural mode (Figure 39(b)), employing a single IcL example typically yields a steeper improvement slope, characterized by a higher rate of accuracy increase per additional example, than using three examples. All variations in the number of examples yield enhancements over 0-shot across nearly all tasks of this kind. Conversely, for tasks involving binary classification or choice selection in the Symbolic mode (Figure 39(c)), increasing the number of examples may lead to a decrease in accuracy. Regarding binary classification tasks in the Mathematical mode that require a simple yes/no response (Figure 39(d)), we witness a large surge in performance, with accuracy gains ranging from a minimum of  $20\%$  to a maximum of about  $60\%$ . These improvements are significantly greater than those observed in Natural mode and Symbolic mode tasks, which do not surpass  $20\%$ . Additionally, the performance continues to improve with the addition of more examples. For probability calculation tasks in the Mathematical mode (Figure 39(e)), a clear pattern emerges where the inclusion of two or three examples substantially enhances performance beyond what is achieved with just one or no examples.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a6aac0436ad07c2e74274b51716cc8d251e9cbd60ff5291922b807744c4d0728.jpg)



(a) Open-ended generation in the Natural mode.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f5bdc3489f517f80580aed0e22742b1198558367efa1d74ca8d616d822d8583a.jpg)



(b) Binary classification and choice selection in the Natural mode.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b33d359ff63cdfab3b1147637f260b5a03112e4cd6991c1e2031e7628538d2fb.jpg)



(c) Binary classification and choice selection in the Symbolic mode.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/59be60b20662f0a419abd76b5472cb8154dde685b9657739d63d954894f4a6a3.jpg)



(d) Binary classification in the Mathematical mode.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b5a3e681fd3e0ef17cdcf38e0cd7ed4bf672735a93f1e4c6e6aead77f5de2ac2.jpg)



(e) Probability calculation in the Mathematical mode.



Figure 9.39 Accuracy trends of mode and question type combinations.


# 9.2.2 Adversarial Prompt

When confronted with adversarial prompts, we can evaluate a model's responses using a dichotomous tuple (pre-adversarial, post-adversarial). This classifies the model's replies into 4 categories: (right, right), (wrong, wrong), (right, wrong), and (wrong, right). For instance, the (right, wrong) category reflects instances where the model initially provides a right response but alters it to a wrong one following the adversarial prompt. This analysis is particularly focused on the dynamics between the (right, wrong) and (wrong, right) categories, as these transitions illustrate how adversarial prompts influence the model's reliability and response strategy. Additionally, it is worth mentioning that the experiments described here exclude the CEG scenario. Given the open-ended nature of CEG, employing ROUGE-L alone is not sufficient for precisely evaluating the performance differences before and after encountering adversarial inputs.

Wrong direction vs. right direction. To elucidate the relationship between the directions of answer modification by a model, Figure 9.40 is devised. The top half of the figure illustrates modifications in the incorrect direction (i.e., changing right answers to wrong ones), whereas the bottom half depicts modifications in the correct direction (i.e., changing wrong answers to right ones). The scatter plot within this figure represents the correlation of answer direction changes across all scenarios for each model under various adversarial prompts. For instance, consider that a model in the AR scenario, influenced by adversarial-doubt and adversarial-ignore prompts, alters  $50\%$  and  $20\%$  of its initially right answers to wrong ones, respectively. This instance would be plotted at the (50,20) coordinate on the scatter plot in the figure's top half, with the color of the point indicating the AR scenario. Additionally, a histogram displays the average rates of change in the model's answers for both adversarial-doubt and adversarial-ignore across all scenarios.

From the analysis of Figure 9.40, we derive the following key insights: (1) Change comes with ease, yet the right direction seeks its own challenge. The scatter plot analysis indicates that, for adjustments in the right direction (correcting wrong answers), no points exceed the (40,40) threshold, suggesting a rarity in substantial correct changes. In contrast, the wrong direction (changing correct answers to incorrect) displays about 13 points beyond this threshold. Predominantly, points associated with the right direction cluster within the (0,30) range, whereas those for the wrong direction are more densely distributed in the (30,40) interval. This pattern indicates that models more frequently alter their responses to incorrect answers than correct ones. The histogram further supports this, showing significantly shorter bars for the right direction, indicating fewer and lesser magnitudes of correct adjustments. Specifically, no model's rate of change in the right direction exceeds  $20\%$ , with only one model, Claude2, surpassing  $15\%$  under the adversarial-doubt prompt. Conversely, six models under both adversarial-doubt and adversarial-ignore prompts exceed a  $15\%$  wrong change rate, with two and one models respectively surpassing  $20\%$ . This pattern underscores that, for any single model across all scenarios, changing from wrong to right is a greater challenge. (2) Within the same direction, different adversarial prompts exhibit a strong correlation. The scatter plots reveal a strong correlation in model behavior across different adversarial prompts, adhering closely to a unit slope straight line, whether in the wrong or right direction. The histogram data corroborate this, demonstrating stable rankings of model performance within the same directional category across different prompts. For instance, in the wrong direction, the top and bottom five models remain consistent across both types of adversarial prompts, although their internal rankings may shift. This consistency also extends to the right direction.

Consistency in the directions of change. Figure 9.41 illustrates the average rates of right change and wrong change for all models across all scenarios, after being attacked by two types of adversarial prompts. Our analysis highlights two consistent trends in the direction of change: (1) Consistency among lower-ranking

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f940f30c59be255921cdbc68abfb5fb9027a7bae96134ef85fa53869e46dc208.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/69f7246b556388838821c00865e60d80f6e39780f6fc792f73e38ab6a7fd5ba3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ca7f0a04b10dc41ec64846f024b80238b75dc822a64f18784c4d8e492e04c6ad.jpg)



(a) Wrong direction


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c690ce9d9e6dd8a1bdf2d6586c62a6f0f64e2dde28646790e88eb9f3ec02b28b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9c7a1fbb41b9112be4ef4193b3211cfc83991659f1a7bb66c0437cdd0d392e32.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/292a348d16e97be64c4abdce4a4af3c98d8e67515d3ea697b89c29a28305db50.jpg)



(b) Right direction



Figure 9.40 Wrong direction vs. right direction. Change right to wrong reflects instances where the model initially provides a right response but alters it to a wrong one following the adversarial prompt. And change wrong to right means the vice versa. Doubt and Ignore refer to two forms of adversarial prompts. The dots in the scatter plot represent the correlation of answer direction changes across all scenarios for every model when adapted adversarial prompts. The histogram represents the average rates of the model's answers change, for both adversarial doubt and adversarial ignore across all scenarios.


models: The figure shows that 11 models have a right change rate below  $5\%$ , and 10 models exhibit a wrong change rate below  $5\%$ , with all 10 models overlapping within the 11-model subset. This substantial overlap and the consistently low rate of change in both directions imply significant limitations in these models' ability to effectively follow instructions. It is noteworthy that this group includes all GPT-3 series models released in 2020, as well as some introduced in 2022 and 2023. This indicates that, despite technological advancements over three years, enhancing the models' ability to follow instructions remains a significant challenge. (2) Consistency among top-performing models: Attention is drawn to models that register both a right change rate and a wrong change rate exceeding  $10\%$ , with eight models identified in each category. Excluding Vicuna-v1.3 (33B), there is a complete overlap among the remaining seven models across these categories. The substantial

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/bac9721ed25d903a1349216ddd4f0d915a3fc85f61756317d9424db077a6d349.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/26120f089f96c8156e616a06d8580c3b88f5be3b423c2bf11a11094a9eecccb1.jpg)



Figure 9.41 Direct model comparison between right and wrong change directions. We compare the absolute change rates. Change right to wrong reflects instances where the model initially provides a right response but alters it to a wrong one following the adversarial prompt. And change wrong to right means the vice versa.


rates of change in both directions indicate that although these models excel at following instructions, they may struggle with independently assessing the accuracy of these instructions. This characteristic, however, is not necessarily negative; its implications vary significantly depending on the application context of the model. In critical decision-making sectors such as healthcare, finance, and law, the ability of models to discern and potentially correct erroneous commands is advantageous. In contrast, in creative fields like art, it may be more desirable for models to strictly follow given instructions, thereby supporting unaltered creative expression.

Inconsistency in the directions of change. In our analysis of Figure 9.41, we identify discrepancies in the directions of change in two key areas: (1) High wrong change and low right change: This pattern, though not desirable, is evident in some models. For instance, Vicuna has a right change rate of less than  $10\%$  (positioned 11th), while its wrong change rate exceeds  $20\%$  (leading the ranking). This indicates a propensity for these models to incorrectly alter correct responses rather than improve incorrect ones, suggesting a bias in their learning or response mechanisms that could impact their utility in precision-critical applications. (2) High right change and low wrong change: Notably, no model in our experimental setups achieves this ideal balance. This observation does not necessarily reflect a deficiency in the models' ability to correct errors. It could also be influenced by instances where the model's responses are primarily categorized as (right,right). For example, GPT-4 consistently shows robust performance across various scenarios, leading to a higher frequency of (right,right) responses. As a result, it occupies a middle-tier position in terms of the proportion of changes in both categories, reflecting a balanced but not exceptional capability in either direction.

Influence of training strategy. In Figure 9.42, we analyze the impact of different training strategies on model responses in the wrong and right directions across all scenarios. The training strategies categorized are consistent with Table 8.1. From this analysis, we draw two primary conclusions: (1) Impact of RLHF: Models trained with RLHF show a tendency to alter their responses more frequently when interacted with by humans. This observation aligns with findings by Sharma et al. (2024), which suggest that despite initially accurate and confident responses, models frequently revise their answers upon user inquiries, often leading to misinformation. This indicates that RLHF acts as a double-edged sword; while it enhances responsiveness

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1039037f075b3666d4bd12d215de21f7462c04639b101990d23acfbccba67820.jpg)



(a) Wrong direction


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/61c8add91acc52d0f040d9ff4fc0afc867224696fbca023b1a744a300132073e.jpg)



(b) Right direction



Figure 9.42 Training strategy's influence on wrong and right change directions. Change right to wrong reflects instances where the model initially provides a right response but alters it to a wrong one following the adversarial prompt. And change wrong to right means the vice versa.


to human feedback, it also increases susceptibility to generating misinformation, thus requiring careful application and further research to optimize its benefits and mitigate its drawbacks. (2) Comparison of pretraining and SFT: No significant difference is observed between pre-training and SFT in how models adjust their answers under adversarial prompts. Our comparative analysis across 20 scenarios reveals that SFT leads to more substantial changes in the wrong direction in 11 scenarios, suggesting that pre-training generally maintains more stable and accurate responses. Conversely, for changes in the correct direction, pre-training is equal to or more effective than SFT in 11 scenarios. This underscores pre-training's effectiveness in aligning model responses more closely with accurate outputs, indicating that SFT may not significantly enhance model alignment with human intentions.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/7564eae5e404e981410b5d91be33421ab60fc88c3891a5cc55367238c897d74b.jpg)



Figure 9.43 Influence of manual CoT format.


# 9.2.3 Chain-of-Thought

Influence of manual CoT format. Answer after reason refers to the format in provided examples where the reasoning is presented before culminating in an answer explicitly stated as “Therefore, the answer is [...]”. In contrast, the reason after answer format starts with a direct answer, which is then elucidated through subsequent reasoning. Despite evidence from Wei et al. (2022b) showing the superior efficacy of the standard manual CoT format (i.e., answer after reason) over the reason after answer format, its effectiveness in assessing causal reasoning capabilities in AI models remains an area of interest.

To this end, we conduct evaluations on five open-source models, ranging in size from 7B to 70B. Our evaluations focus specifically on the Symbolic mode, covering five tasks (i.e., AR-B (CaLM-AR), IV-C (CaLM-IV), CA-B (FP), CA-B (FA), and CEI-B (0.2-UC)). Figure 9.43 reflects the average accuracies achieved by these models on these tasks using the two contrasting formats. Our finding indicates that the effectiveness of the two manual CoT formats (i.e., answer after reason and reason after answer) varies depending on the models' capabilities. Specifically, InternLM-chat (20B) demonstrates improved performance specifically in the answer after reason format. Further analysis from Figure 9.25 reveals that employing 1/3-shot IcL can notably reduce instruction-following errors, drawing parallels to the reason after answer format, where presenting a direct standard answer initially may better guide models in complex causal tasks. Ultimately, the influence of manual CoT on model efficacy for causal reasoning tasks must be evaluated against the backdrop of the models' inherent causal reasoning capabilities.

Basic prompt vs. CoT. Figure 9.44 compares the efficacy of the basic prompt with two CoT prompts across all evaluated models over all causal scenarios. The key findings from this figure are as follows: (1) Among the two CoT formats, manual CoT proves to be more effective. It enhances performance in 24 out of 28 models when compared to the basic prompt. In contrast, the 0-shot CoT approach yields performance gains in only 7 out of the 28 models. This stark difference underscores the significant advantage of employing manual CoT in prompting strategies to facilitate higher model performance. (2) The effectiveness of manual CoT is consistent across models developed with various training strategies. As categorized in Table 8.1, irrespective of the training methodology employed, manual CoT consistently boosts performance. This demonstrates its versatility and effectiveness as a prompting strategy across different model architectures and training backgrounds.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9f30b7162795d47eba9da7ce5ae79fc6d1aaea57731a4eb31aaac9bed4fb9457.jpg)



(a) Basic vs. 0-shot CoT


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9ee3e2aaa4c8ee2d542539d7872cb5be7e3e712152ddc43844830cd6dbc2b8ab.jpg)



(b) Basic vs. manual CoT



Figure 9.44 Basic vs. CoT. We compare basic prompt with 0-shot CoT and manual CoT across all the models.


# 9.2.4 Explicit Function

To illustrate the performance improvement of the explicit-function prompt compared to the basic prompt, we conduct an analysis across all causal scenarios and models.

Across causal scenarios. From Figure 9.45, we have the following findings: (1) Both the explicit-function and basic prompts exhibit consistent performance trends across different types of scenarios. They perform well in causal discovery scenarios, such as PCD and ECI, but show poor performance in counterfactuals scenarios, such as PN and PS. (2) Among 11 out of 21 scenarios, the explicit-function prompt outperforms the basic prompt. Notably, in association scenarios such as CORR and EAE, the explicit-function prompt consistently demonstrates improved performance.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d66380b48706041866a5905159bb6d012de6dc20cdfca846e5bef66df645fe70.jpg)



Figure 9.45 Basic vs. EF across all the scenarios. We compare the performance comparison between basic prompt and EF across all the scenarios.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6caa11fe508e3690e2f99544b8ea00250134d3b7cd59a9e9124e5b8f4f674166.jpg)



Figure 9.46 Basic vs. EF across all the models. We compare the performance comparison between basic prompt and EF across all the models.


Across models. Figure 9.46 indicates that the explicit-function prompt enhances performance in 13 out of 28 models compared to basic prompts. However, in the remaining 15 models, it results in decreased performance. This variability underscores that the effectiveness of the explicit-function prompt can differ significantly across models, suggesting that their use in practical scenarios should be carefully considered and adapted to the situation.

# 9.3 Model-specific Analysis

In Main Results (Section 9.1), we have already analyzed the performance of models from the most comprehensive and insightful perspective (e.g., Comparative Analysis of Models (Section 9.1.1), Analyzing Complexity (Section 9.1.6), Analyzing Errors (Section 9.1.9)). This section will center on the performance of each specific model across all causal scenarios and prompts. Altogether, 28 models from 9 different creators have been evaluated in CaLM. Therefore, this section will break down the analysis by creator, organizing it into the following nine sections: OpenAI (Section 9.3.1), Anthropic (Section 9.3.2), Shanghai AI Laboratory (Section 9.3.3), Alibaba Cloud (Section 9.3.4), Baichuan Inc (Section 9.3.5), Meta (Section 9.3.6), Lmsys (Section 9.3.7), UC Berkeley (Section 9.3.8), and Microsoft (Section 9.3.9). Additionally, Table 9.5 will provide clarifications for technical terms pertinent to our subsequent analysis. For ease of reading, these terms will be presented in italic font throughout the entire section.

When discussing a model's performance, the content is typically organized into four main paragraphs: Summary, Accuracy, Ranking, and Robustness. Each of these paragraphs focuses on different aspects of the model evaluation:

- Summary: This paragraph provides an overview analysis of the model's performance. It concisely reports key statistics such as the average scenario-prompt accuracy, the average prompt-average rank, and the average robustness score across various scenarios. This helps in quickly understanding the model's general effectiveness and reliability.

- Accuracy: This paragraph delves deeper into the model's performance metrics. It is usually divided into four subcategories detailing: 1) Overall performance, which highlights the average scenario-prompt accuracy, the average standard deviation of prompt accuracy, the top scenario-prompt pair, and the proportions of scenario-prompt pairs that exceed random guess accuracy and the  $80\%$  accuracy threshold. 2) Scenario performance, which lists scenarios with the highest average accuracy. Scenarios are only included if their accuracy surpasses random guess accuracy; otherwise, they are excluded from the list. 3) Prompt efficiency, which focuses on identifying the most efficient prompts and those that have the largest number of scenario-prompt pairs exceeding random guess accuracy. 4) Language influence, which assesses how well the model performs across different languages, evaluating the language accuracy difference to understand the impact of linguistic variation on model accuracy.

- **Ranking:** This paragraph compares the model's performance to other models and includes two key metrics: 1) Prompt-average rank, which reports the highest, lowest, and average prompt-average ranks, as shown in Figure 9.47. 2) Model-prompt rank: which indicates the best and worst model-prompt ranks over all the scenario-prompt pairs in the model.

- Robustness: The paragraph showcases the average robustness score of the model and identifies scenarios where the model achieves the highest robustness.

# 9.3.1 OpenAI

ada (0.35B). Summary: The model's average scenario-prompt accuracy is  $22.9\%$ , with the average prompt-average rank of 24/28 (the lowest average prompt-average rank). Additionally, it demonstrates a high average robustness score of  $96.7\%$  across various scenarios.

Accuracy: 1) Overall performance: As depicted in Figure 9.48(a), ada (0.35B) registers an average scenario-prompt accuracy of  $22.9\%$ , with an average prompt effectiveness standard deviation of 10.0. The top scenario-prompt

<table><tr><td>Terminology</td><td>Explanation</td></tr><tr><td>scenario-prompt pair</td><td>A combination of a scenario and a prompt.</td></tr><tr><td>average scenario-prompt accuracy</td><td>The average accuracy of a model tested on all the scenario-prompt pairs.</td></tr><tr><td>top scenario-prompt pair</td><td>The combination that has the top accuracy value across all tested scenario-prompt pairs in the target model.</td></tr><tr><td>random guess accuracy</td><td>The random guess accuracy of a model within a causal task/scenario, varying across different causal tasks/scenarios.</td></tr><tr><td>language accuracy difference</td><td>The difference between a model&#x27;s English and Chinese accuracy across all the scenario and prompt pairs.</td></tr><tr><td>prompt-average rank</td><td>As shown in Figure 9.47, the prompt-average rank, ranging from 1 to 28, is derived by comparing the average accuracies of 28 models across all the prompts in a scenario.</td></tr><tr><td>model-prompt rank</td><td>Ranging from 1 to 252, the model-prompt rank is determined by comparing the accuracies across all 28×9 model-prompt pairs within each scenario.</td></tr></table>

Tab. 9.5 Explanations for model-specific terminologies.

pairs include 1-shot IcL in CA scoring  $64.0\%$ . This is followed by 3-shot IcL in NIE at  $63.6\%$  and EF in CA at  $57.6\%$ .  $29.1\%$  of scenario-prompt pairs exceed their random guess accuracy, with  $0.0\%$  reaching above  $80\%$  accuracy. 2) Scenario performance: High-performing scenarios where ada (0.35B) excels and surpasses random guess accuracy include CA with a score of  $55.3\%$ , CEG at  $24.1\%$ , and PN at  $0.8\%$ . 3) Prompt efficiency: The most effective prompts are 3-shot IcL at  $36.2\%$  and 1-shot IcL at  $32.8\%$ . Regarding the number of scenario-prompt pairs where the model exceeds the random guess accuracy, the 3-shot IcL leads in 14 out of 21 scenarios, followed by 1-shot IcL in 10, and EF in 6 scenarios. 4) Language influence: In 15 out of 21 scenarios, English outperforms Chinese, with significant language accuracy differences observed in CB, EAE, and CORR, where the accuracy differences are  $29.4\%$ ,  $28.7\%$ , and  $27.1\%$ , respectively. Conversely, scenarios such as CEG, NDE, and CDE showcase superior performance in Chinese, with accuracy differences of  $14.1\%$ ,  $4.8\%$ , and  $3.4\%$ , respectively.

Ranking: 1) Prompt-average rank: As shown in Figure 9.47, ada (0.35B)'s best prompt-average ranks appears in CA at 12. In contrast, ada (0.35B) ranks lowest in AC at 28, ATE at 28, and CEG at 28, indicating areas for improvement. The model's average prompt-average rank across 21 scenarios is 24/28, with a standard deviation of 3.8. 2) Model-prompt rank: As shown in Figure 9.48(b), ada (0.35B)'s best model-prompt ranks appears in CEI with 3-shot IcL at 12, NIE with 3-shot IcL at 12, ETT with manual CoT at 12. On the other hand, the lowest ranks are observed in CORR with EF at 251, EAE with EF at 251, and CEG with adversarial ignore at 250.

Robustness: ada (0.35B) boasts an average robustness score of  $96.7\%$  across scenarios. The model has the best robustness in ETT at  $99.9\%$ , ATE at  $99.9\%$ , and NIE at  $99.9\%$ .

text-ada-001. Summary: The model showcases an average scenario-prompt accuracy of  $25.3\%$ , achieves an average prompt-average rank of 21 out of 28, and possesses an average robustness score of  $84.7\%$ .

Accuracy: 1) Overall performance: As depicted in Figure 9.49(a), text-ada-001 achieves an average scenario-prompt accuracy of  $25.3\%$ , with an average standard deviation in prompt effectiveness of 7.3. The top scenario

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c02e5516bed260111cf8c4bf23a4da0d5187a7c7ccfb8a3471fa969b753d4fb8.jpg)



Figure 9.47 Prompt-average rank of models.


prompt pairs are 1-shot IcL in CA with a score of  $63.5\%$ , followed by adversarial doubt in CA at  $53.5\%$ , and 1-shot IcL in AR at  $52.6\%$ . Only  $25.9\%$  of the scenario-prompt pairs surpass the random guess accuracy, and none exceed  $80\%$  accuracy. 2) Scenario performance: In scenarios where text-ada-001 surpasses random guess accuracy, the top 3 scenarios having the highest average accuracy are CEG with a score of  $27.7\%$ , PN at  $2.2\%$ , and PS at  $0.1\%$ . 3) Prompt efficiency: The most effective prompts include 3-shot IcL at  $33.2\%$  and 1-shot IcL at  $32.2\%$ . Regarding the number of scenario-prompt pairs where the model exceeds the random guess accuracy, 3-shot IcL leads in 13 out of 21 scenarios, followed by 1-shot IcL in 9, and EF in 5 scenarios. 4) Language influence: English performs better than Chinese in 18 of 21 scenarios, with significant advantages in AR, CORR, and EAE, where the language accuracy differences are  $34.9\%$ ,  $26.7\%$ , and  $24.1\%$ , respectively. Conversely, the Chinese perform better in CEG, CA, and PS, with language accuracy differences of  $10.3\%$ ,  $3.3\%$ , and  $0.2\%$ , respectively.

Ranking: 1) Prompt-average rank: As shown in Figure 9.47, text-ada-001's best prompt-average ranks are in IV at 9, PN at 11, and CEI at 12. The model ranks lowest in EAE, NIE, CDE, ECI, and NDE, all at 28, indicating areas for improvement. The average prompt-average rank across 21 scenarios is  $21/28$ , with a standard deviation of 6.8. 2) Model-prompt rank: Figure 9.49(b) illustrates text-ada-001's highest ranks in PN with 3-shot IcL at 8, CEI with 3-shot IcL at 15, and ETT with manual CoT at 28. The lowest ranks are in CORR with EF at 250, ECI with 0-shot CoT at 249, and EAE with EF at 247.

Robustness: text-ada-001 has an average robustness score of  $84.7\%$  across scenarios, with the highest robustness in CDE at  $97.3\%$ , NDE at  $96.5\%$ , and ETT at  $95.4\%$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/787f245445d4f25474d1e9354a3d00dced7f8e6f977667ac6fcc55abfc19fd63.jpg)



(a) Performance of ada (0.35B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3094534963149648d296c7d09e2ed8b8e00601645d48de9fc8a962ac137df0b3.jpg)



(b) Model-prompt rank of ada (0.35B)



Figure 9.48 Heatmap of ada (0.35B).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0a6ca4b526b358a668b177bf02dd794ef8c7f547045a6d1182a41090877b90df.jpg)



(a) Performance of text-ada-001


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3943ee2404e304d2f83bf05f6f2eb38b2ede0cd998ec66cae5ac9e7989acaed0.jpg)



(b) Model-prompt rank of text-ada-001



Figure 9.49 Heatmap of text-ada-001.


babbage (1.3B). Summary: The model's performance on scenario-based prompts yields an average accuracy rate of  $23.4\%$ . It ranks 23rd out of 28 when considering the average of prompt-average rank. Additionally, the model demonstrates an average robustness score of  $94.9\%$ .

Accuracy: 1) Overall performance: Figure 9.50(a) shows babbage (1.3B) with an average scenario-prompt accuracy of  $23.4\%$  and an average standard deviation for prompt effectiveness of 8.2. The top scenario-prompt

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/eab416478088aa682b53bf6d6095451a2290816b3938ad0b3ccfa726fa09771e.jpg)



(a) Performance of babbage (1.3B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ca26788580a7422ebc4c47c76d52d6880143372ce2e4cde9dd863338562a3825.jpg)



(b) Model-prompt rank of babbage (1.3B)



Figure 9.50 Heatmap of babbage (1.3B).


pairs are 1-shot IcL in CA with a score of  $64.3\%$ , followed by 0-shot CoT in CA at  $58.1\%$  and 0-shot IcL in CA at  $58.0\%$ . About  $30.7\%$  of the scenario-prompt pairs surpass the random guess accuracy, yet none achieve over  $80\%$  accuracy. 2) Scenario performance: For scenarios in which babbage (1.3B) exceeds the random guess accuracy, the top three scenarios ranked by average accuracy include CA with an impressive score of  $55.1\%$ , CEG at  $27.1\%$ , and PN at  $0.5\%$ . 3) Prompt efficiency: The top-performing prompts are 3-shot IcL and 1-shot IcL, each with a score of  $33.0\%$ . For exceeding the random guess accuracy, 3-shot IcL leads in 14 out of 21 scenarios, followed by 1-shot IcL in 11, and manual CoT in 8 scenarios. 4) Language influence: English outperforms Chinese in 14 out of 21 scenarios, with significant accuracy advantages in CB, AR, and ECI, where the language accuracy differences are  $31.7\%$ ,  $26.3\%$ , and  $13.8\%$ , respectively. However, in scenarios like CEG, NDE, and CDE, Chinese shows better performance, with language accuracy differences of  $8.9\%$ ,  $7.3\%$ , and  $4.8\%$ , respectively.

Ranking: 1) Prompt-average rank: As shown in Figure 9.47, babbage (1.3B)'s best prompt-average ranks is lower than 12. On the other hand, its lowest ranks are in AR at 28, AC at 27, and NIE at 27. The model's average prompt-average rank across 21 scenarios is 23rd out of 28, with a standard deviation of 3.3. 2) Model-prompt rank: As detailed in Figure 9.50(b), babbage (1.3B)'s highest ranks include PN with 3-shot IcL at 36, CEI with 3-shot IcL at 36, and CA with 1-shot IcL at 49. The lowest ranks are in AC with 0-shot CoT at 251, AR with manual CoT at 250, and CDE with 0-shot CoT at 249.

Robustness: babbage (1.3B) has an outstanding average robustness score of  $94.9\%$  across scenarios, with the highest robustness in CB and EAE, both at  $100.0\%$ , and PN at  $99.3\%$ .

text-babbage-001. Summary: The average scenario-prompt accuracy of the model stands at  $28.3\%$ , alongside an average prompt-average rank of 19/28 and an average robustness score of  $94.3\%$ .

Accuracy: 1) Overall performance: Illustrated in Figure 9.51(a), text-babbage-001 achieves an average scenario

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ff8ec683a172a6f1e1a9425de87c07a475fbc585e52a3a50fa4e046c11858430.jpg)



(a) Performance of text-babbage-001


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/93454b825836d911cbf16dad5046d2c194db96993f1003ef0ca976eba3545d9a.jpg)



(b) Model-prompt rank of text-babbage-001



Figure 9.51 Heatmap of text-babbage-001.


prompt accuracy of  $28.3\%$ , with an average standard deviation in prompt effectiveness of 8.6. The top scenario-prompt pairs include 3-shot IcL in NIE with a score of  $63.5\%$ , followed by 3-shot IcL in ATE at  $61.5\%$ , and 1-shot IcL in CA at  $61.3\%$ . About  $33.3\%$  of the scenario-prompt pairs surpass the random guess accuracy, with none exceeding  $80\%$  accuracy. 2) Scenario performance: For scenarios where text-babbage-001 outperforms the random guess accuracy, the three leading scenarios by average accuracy are CA at  $53.8\%$ , CEG scoring  $32.2\%$ , and PN at  $2.3\%$ . 3) Prompt efficiency: The most impactful prompts identified are 3-shot IcL with an effectiveness of  $40.3\%$  and 1-shot IcL at  $32.8\%$ . In terms of surpassing the random guess accuracy, 3-shot IcL is the leader in 16 out of 21 scenarios, followed by 1-shot IcL in 12 scenarios and manual CoT in 7 scenarios. 4) Language influence: In 15 of the 21 scenarios, English demonstrates superior performance over Chinese, with significant accuracy improvements observed in EAE, CB, and CORR, with language accuracy differences of  $38.3\%$ ,  $32.7\%$ , and  $21.0\%$ , respectively. Conversely, Chinese outperforms in scenarios like CEG, NDE, and CDE, with language accuracy differences of  $12.4\%$ ,  $9.6\%$ , and  $0.9\%$ , respectively.

Ranking: 1) Prompt-average rank: As indicated in Figure 9.47, text-babbage-001's highest prompt-average ranks are in CEI at 10, BAS and IV both at 11. On the other hand, its lowest ranks are in EAE and ECI at 27, and CORR at 25, highlighting potential areas for enhancement. Across 21 scenarios, the average prompt-average rank is 19 out of 28, with a standard deviation of 5.5. 2) Model-prompt rank: As per Figure 9.51(b), text-babbage-001's top model-prompt ranks include PN with 3-shot IcL at rank 5, ATE with 3-shot IcL at 13, and NIE with 3-shot IcL also at 13. The lowest ranks are noted in ECI with 0-shot CoT at 250, NDE with EF at 246, and NIE with EF at 243.

Robustness: text-babbage-001 has an impressive average robustness score of  $94.3\%$  across scenarios, achieving peak robustness in EAE at  $100.0\%$ , CB at  $99.8\%$ , and NIE at  $99.3\%$ .

curie (6.7B). Summary: The model achieves an average scenario-prompt accuracy of  $28.4\%$ , holds an average prompt-average rank of 18/28, and maintains an average robustness score of  $93.5\%$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/72fb630e5c6609b4596f50df72d9482ec656549e5baafebe9c4be7ac4a639429.jpg)



(a) Performance of curie (6.7B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/22b896b0a25e0c4a7fac4e79c5917e653a30719d1342abfe72b22db3638cc0dd.jpg)



(b) Model-prompt rank of curie (6.7B)



Figure 9.52 Heatmap of curie (6.7B).


Accuracy: 1) Overall performance: Figure 9.52(a) showcases that curie (6.7B) achieves an average scenario-prompt accuracy of  $28.4\%$ , with an average prompt effectiveness variability of 8.2. The top scenario-prompt pairs include manual CoT in NIE with a score of  $66.5\%$ , 1-shot IcL in CA at  $62.6\%$ , and manual CoT in ETT at  $58.9\%$ . Approximately  $37.0\%$  of the scenario-prompt pairs outperform the random guess accuracy, yet none surpass  $80\%$  accuracy. 2) Scenario performance: In situations where curie (6.7B) exceeds the random guess accuracy, the top three scenarios by average accuracy are CA at  $53.6\%$ , EAE at  $51.6\%$ , and CORR at  $50.6\%$ . 3) Prompt efficiency: The leading prompts in effectiveness are 3-shot IcL at  $35.2\%$  and 1-shot IcL at  $33.8\%$ . In terms of surpassing the random guess accuracy, 3-shot IcL and 1-shot IcL both lead in 12 out of 21 scenarios, followed by 0-shot IcL in 9 scenarios. 4) Language influence: English demonstrates superior performance over Chinese in 11 out of 21 scenarios, with significant advantages in CR, ETT, and NIE, with language accuracy differences of  $9.3\%$ ,  $8.9\%$ , and  $7.9\%$ , respectively. In contrast, Chinese excels in FAS, CEG, and IV, with language accuracy differences of  $18.1\%$ ,  $17.5\%$ , and  $13.2\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, curie (6.7B)'s highest prompt-average ranks are seen in CEI, EAE, and CB, each at 7. Meanwhile, it ranks worst in CDE at 27th place, while PN, AC, and ATE rank at 25th. The average prompt-average rank across 21 scenarios is 18 out of 28, with a standard deviation of 6.5. 2) Model-prompt rank: As detailed in Figure 9.52(b), the top ranks for curie (6.7B) include ETT with manual CoT at 8, NIE with manual CoT at 10, and CORR with EF at 17. The lowest ranks are in CDE with 0-shot CoT at 249, ATE with manual CoT at 246, and NDE with EF at 246.

Robustness: curie (6.7B) exhibits a robust average score of  $93.5\%$  across various scenarios, with the highest robustness in AC at  $100.0\%$ , AR at  $99.5\%$ , and NIE at  $98.9\%$ .

text-curie-001. Summary: The model's performance accuracy for scenario prompts averages  $31.7\%$ , with its average prompt-average rank at 15 out of 28 and an average robustness score of  $91.6\%$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3831aeb134a606e9900f56ec5ec6296a316047a158ae514b249626fae1324d8e.jpg)



(a) Performance of text-curie-001


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b82c8f3e28fb5f380e2e7c09f59852c4db48eafce099c5b2c8fc516b3816835b.jpg)



(b) Model-prompt rank of text-curie-001



Figure 9.53 Heatmap of text-curie-001.


Accuracy: 1) Overall performance: Figure 9.53(a) illustrates that text-curie-001 achieves an average scenario-prompt accuracy of  $31.7\%$ , with an average std for variability in prompt effectiveness of 5.6. The top scenario-prompt pairs include manual CoT in NIE with a score of  $64.7\%$ , followed by manual CoT in CA at  $61.6\%$ , and manual CoT in EAE at  $59.6\%$ . A total of  $58.2\%$  of scenario-prompt pairs outperform the random guess accuracy, yet none surpass  $80\%$  accuracy. 2) Scenario performance: In scenarios where the model surpasses the random guess accuracy, the top 3 scenarios having the highest average accuracy are CA with a score of  $56.9\%$ , EAE at  $52.2\%$ , and CORR at  $50.8\%$ . 3) Prompt efficiency: The top prompts in terms of effectiveness are manual CoT and 3-shot IcL both at  $37.0\%$ , followed by 1-shot IcL at  $32.2\%$ . Regarding exceeding the random guess accuracy, 3-shot IcL outperforms in 17 of 21 scenarios. It is followed by adversarial doubt achieving this in 13 scenarios, and manual CoT, 1-shot IcL, EF, and 0-shot IcL each lead in 12 scenarios. 4) Language influence: In 11 of the 21 scenarios, English demonstrates superior performance over Chinese, particularly in ECI, BAS, and AR, with language accuracy differences of  $11.9\%$ ,  $10.8\%$ , and  $10.7\%$ , respectively. Conversely, Chinese shows better performance in CEG, CB, and CA, with language accuracy differences of  $6.7\%$ ,  $3.5\%$ , and  $3.0\%$ , respectively.

Ranking: 1) Prompt-average rank: As shown in Figure 9.47, text-curie-001 achieves its best prompt-average ranks with a 2nd place in CEI, 5th in EAE, and ties for 6th in AC, CB, and FAS. On the other hand, its lowest ranks are in ETT and PN, both at 27th, followed by ATE and NDE, each at 26th. The average prompt-average rank across 21 scenarios is 15 out of 28, with a standard deviation of 8.8. 2) Model-prompt rank: Figure 9.53(b) shows text-curie-001's best ranks include NIE with manual CoT at 11, CORR with EF at 16, and EAE with manual CoT at 21. The lowest ranks are in CDE with basic at 249, with 0-shot CoT at 247, and NDE with 0-shot CoT at 246.

Robustness: text-curie-001 exhibits a robust average score of  $91.6\%$  across various scenarios, achieving optimal robustness in AC at  $100.0\%$ , CORR at  $99.8\%$ , and NDE at  $99.5\%$ .

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/db809201fc17d4f5fabf9e0455b383ea379ee606e6afd3dc1c22ff06812e5733.jpg)



(a) Performance of davinci (175B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0492738d5d6285d0593fd50e44d23bcf6901155ed30081bda7e211f2b223a753.jpg)



(b) Model-prompt rank of davinci (175B)



Figure 9.54 Heatmap of davinci (175B).


davinci (175B). Summary: The model records an average scenario-prompt accuracy of  $29.9\%$ , alongside an average prompt-average rank of 15 out of 28 and an average robustness score of  $85.8\%$ .

Accuracy: 1) Overall performance: Presented in Figure 9.54(a), davinci (175B) achieves an average scenario-prompt accuracy of  $29.9\%$ , with an average standard deviation for prompt effectiveness at 7.1. The top scenario-prompt pairs include a 3-shot IcL in NIE with a score of  $73.3\%$ , a 3-shot IcL in CB at  $61.7\%$ , and a manual CoT in CA at  $59.4\%$ . A total of  $44.4\%$  of scenario-prompt pairs surpass the random guess accuracy, yet none exceed an  $80\%$  accuracy mark. 2) Scenario performance: Among scenarios where davinci (175B) outperforms the random guess accuracy, the highest accuracies are observed in CA at  $55.9\%$ , EAE at  $50.7\%$ , and CORR at  $50.1\%$ . 3) Prompt efficiency: The leading prompts in effectiveness are 3-shot IcL at  $39.5\%$  and 1-shot IcL at  $33.5\%$ . In terms of beating the random guess accuracy, 3-shot IcL dominates in 20 of 21 scenarios, with 1-shot IcL following in 14 scenarios and manual CoT in 9. 4) Language influence: English surpasses Chinese in 13 of 21 scenarios, especially in NIE, AC, and ETT, with language accuracy differences of  $8.4\%$ ,  $6.9\%$ , and  $5.9\%$ , respectively. Conversely, Chinese outshines English in scenarios like CEG, IV, and CB, with language accuracy differences of  $13.8\%$ ,  $8.5\%$ , and  $6.4\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, davinci (175B)'s top prompt-average ranks are in CA and EAE, both at 8, and CEI at 9. However, it faces its lowest ranks in PN at 26, AC at 24, and AR at 23, pinpointing areas for growth. The average prompt-average rank across 21 scenarios stands at 15 out of 28, with a variability of 5.5. 2) Model-prompt rank: As shown in Figure 9.54(b), davinci (175B) achieves its highest model-prompt ranks in several key areas: a third-place in NIE using 3-shot IcL, a sixth-place in CEI with 1-shot IcL, and tenth-place ranks in both CORR using EF and CEI with 3-shot IcL. The most significant challenges are noted in AR with manual CoT at 249, AC with an adversarial ignore strategy at 245, and PCD with manual CoT at 239.

Robustness: davinci (175B) reports an average robustness score of  $85.8\%$  across various scenarios, showcasing

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/267cbefb4f2b8bd745700901300ddbfd6b0ff1d44eea822d4a81380421953056.jpg)



(a) Performance of text-davinci-001


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/46efd02906fbbd841e7da278c1f487320209c4c80b9086b46872752ce65b5fc1.jpg)



(b) Model-prompt rank of text-davinci-001



Figure 9.55 Heatmap of text-davinci-001.


top robustness in CORR at  $99.8\%$  EAE at  $98.1\%$  and AC at  $95.3\%$ .

text-davinci-001. Summary: The model exhibits an average scenario-prompt accuracy of  $33.3\%$ , holds an average prompt-average rank of 11 out of 28, and achieves an average robustness score of  $76.2\%$ .

Accuracy: 1) Overall performance: Shown in Figure 9.55(a), text-davinci-001 achieves an average scenario-prompt accuracy of  $33.3\%$ , with an average prompt effectiveness variability (std) of 7.1. Leading the performance metrics are the top scenario-prompt pairs like 3-shot IcL in NIE with a high score of  $69.9\%$ , 1-shot IcL in PCD at  $67.5\%$ , and 3-shot IcL in the same scenario at  $66.8\%$ . A total of  $50.3\%$  of the scenario-prompt pairs outperform the random guess accuracy, yet none surpass the  $80\%$  accuracy level. 2) Scenario performance: Within scenarios where text-davinci-001 exceeds the random guess accuracy, the highest scores are noted in AR at  $56.3\%$ , PCD at  $53.8\%$ , and CA at  $52.9\%$ . 3) Prompt efficiency: The most efficient prompts identified are 3-shot IcL at  $40.4\%$ , manual CoT at  $39.8\%$ , and 1-shot IcL at  $32.7\%$ . Regarding scenario-prompt pairs outperforming the random guess accuracy, 3-shot IcL and manual CoT both lead in 13 out of 21 scenarios, followed by 0-shot IcL in 11 scenarios. 4) Language influence: English demonstrates superiority over Chinese in 19 of 21 scenarios, with significant accuracy benefits in AR, CA, and CR, where the language accuracy differences are  $11.4\%$ ,  $10.5\%$ , and  $9.7\%$ , respectively. In contrast, the Chinese excel in CEG and CB, with language accuracy differences of  $10.4\%$ , and  $5.2\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, text-davinci-001's top prompt-average ranks are in AC at 5, PS, CORR, and CEI at 6. However, it finds its worst ranks in CB at 25, ATE at 19, and CA at 18, revealing areas needing improvement. Across 21 scenarios, the average prompt-average rank is 11th out of 28, with a standard deviation of 5.0. 2) Model-prompt rank: Illustrated in Figure 9.55(b), the best ranks for text-davinci-001 include PS with manual CoT at 4, NIE with 3-shot IcL at 7, and PN with manual CoT at 13. The challenges are most strong in ATE with manual CoT at 240, CB with EF at 240, and CB with 0-shot IcL at 237.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2baf1ab2bf4f35bab17bb81d16da7427d61f53c5ff4cc6e46a988e1ce8e2e859.jpg)



(a) Performance of text-davinci-002


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9660546d1a3f6c7325f0e8b34ead1c8f1b1373cd77ef28a66025441a5ac73fc3.jpg)



(b) Model-prompt rank of text-davinci-002



Figure 9.56 Heatmap of text-davinci-002.


Robustness: text-davinci-001 reports an average robustness score of  $76.2\%$  across scenarios, with standout robustness in FAS at  $99.9\%$ , IV at  $99.0\%$ , and PCD at  $91.9\%$ .

text-davinci-002. Summary: The model's average scenario-prompt accuracy is  $42.3\%$ , with the average prompt-average rank of 6/28 and an average robustness score of  $70.9\%$ .

Accuracy: 1) Overall performance: As shown in Figure 9.56(a), text-davinci-002 achieves an impressive average scenario-prompt accuracy of  $42.3\%$ , with an average standard deviation in prompt effectiveness of 8.4. The top scenario-prompt pairs include a 3-shot IcL in FAS with a score of  $78.9\%$ , closely followed by 3-shot IcL in PCD at  $78.5\%$ , and 1-shot IcL in the same scenario at  $78.3\%$ . A significant  $82.5\%$  of the scenario-prompt pairs surpass the random guess accuracy, though none achieve above  $80\%$  accuracy. 2) Scenario performance: Among scenarios where text-davinci-002 outshines the random guess accuracy, the highest scoring scenarios are PCD at  $69.7\%$ , CA at  $68.8\%$ , and AR at  $67.4\%$ . 3) Prompt efficiency: The highest efficiency prompts identified are manual CoT at  $51.9\%$ , 3-shot IcL at  $51.8\%$ , and 1-shot IcL at  $44.4\%$ . manual CoT and 3-shot IcL both lead in 20 out of 21 scenarios in surpassing the random guess accuracy, with 1-shot IcL closely behind in 19 scenarios. 4) Language influence: English dominates Chinese in 19 of 21 scenarios, showcasing significant accuracy leads in scenarios such as ATE, AR, and NIE, with language accuracy differences of  $23.5\%$ ,  $20.9\%$ , and  $15.0\%$ , respectively. In contrast, Chinese perform better in scenarios like CEG, and CEI, with differences of  $10.1\%$ , and  $1.0\%$ , respectively.

Ranking: 1) Prompt-average rank: Figure 9.47 reveals that text-davinci-002 achieves its highest prompt-average ranks with 2nd in CB, 3rd in IV, and 4th across five scenarios. However, it shows lower performance with 16th in PN, 12th in CEG, and 8th in both PS and CEI, indicating areas that could benefit from improvements. The average prompt-average rank rank across 21 scenarios is an impressive 6 out of 28, with a standard deviation of 3.1. 2) Model-prompt rank: As indicated in Figure 9.56(b), text-davinci-002's best ranks are seen in FAS with 3-shot IcL at 4, PS with manual CoT at 5, and CB with 3-shot IcL at 6. The lowest ranks are in CB with EF at

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1e2597663c7d415b87a91885096c58df9cd5974bee207ba32f67c68e9fd7539a.jpg)



(a) Performance of text-davinci-003


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9e511f847325ce685c3180b629be974dcfc89a72aa09b78e062c07db62120c98.jpg)



(b) Model-prompt rank of text-davinci-003



Figure 9.57 Heatmap of text-davinci-003.


194, and CEG with 1-shot and 0-shot IcL at 180 and 175, respectively.

Robustness: text-davinci-002 presents a robustness average of  $70.9\%$  across scenarios, with the highest robustness observed in ECI at  $89.1\%$ , AR at  $87.4\%$ , and PCD at  $85.6\%$ .

text-davinci-003. Summary: The model achieves a scenario-prompt performance accuracy average of  $47.3\%$ , ranks on average 4th out of 28 in prompt-average rank, and maintains an average robustness score of  $68.2\%$ .

Accuracy: 1) Overall performance: Illustrated in Figure 9.57(a), text-davinci-003 has achieved an impressive average scenario-prompt accuracy of  $47.3\%$ , with prompt effectiveness showing an average standard deviation of 8.4. The top scenario-prompt pairs are manual CoT in CA with a score of  $88.0\%$ , 3-shot IcL in FAS at  $86.8\%$ , and 0-shot IcL in CA at  $82.8\%$ . A significant  $88.9\%$  of scenario-prompt pairs outperform the random guess accuracy, with  $5.3\%$  achieving over  $80\%$  accuracy. 2) Scenario performance: For scenarios where text-davinci-003 exceeds the random guess accuracy, the highest scores include CA at  $77.1\%$ , PCD at  $74.7\%$ , and AR at  $74.5\%$ . 3) Prompt efficiency: The most impactful prompts are manual CoT at  $57.7\%$ , 3-shot IcL at  $50.1\%$ , and basic at  $47.6\%$ . In terms of outperforming the random guess accuracy, manual CoT dominates in 20 out of 21 scenarios, closely followed by 0-shot CoT, 1-shot IcL, adversarial doubt, and adversarial ignore, each achieving success in 19 scenarios. 4) Language influence: English surpasses Chinese in 18 of 21 scenarios, with significant accuracy advantages in AR, PCD, and ATE, showing language accuracy differences of  $10.5\%$ ,  $8.7\%$ , and  $8.1\%$ , respectively. However, Chinese outshines English in scenarios like NIE, ETT, and CEG, with differences of  $3.5\%$ ,  $2.3\%$ , and  $1.4\%$ , respectively.

Ranking: 1) Prompt-average rank: As indicated in Figure 9.47, text-davinci-003's top performance is outstanding, achieving a 2nd place rank across 9 scenarios. Its least impressive ranks are 20th in CEI, 9th in CEG, and tied at 6th for both PN and NIE. The model's average prompt-average rank is 4th out of 28, with a standard

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c9aa872f9aea96517553b47ea34215ffe8853c39e3d65a827c1a8bb8c8839d34.jpg)



(a) Performance of GPT-3.5-Turbo


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/453854b7d4cfbc9f9aa6b7c6a7af9fabb2e66d4efdd52230d68f10e6d0ecfc2f.jpg)



(b) Model-prompt rank of GPT-3.5-Turbo



Figure 9.58 Heatmap of GPT-3.5-Turbo.


deviation of 4.1. 2) Model-prompt rank: Demonstrated in Figure 9.57(b), the top ranks for text-davinci-003 include PN with manual CoT at 3, PS with manual CoT also at 3, and FAS with 3-shot IcL at 3. The challenges are most significant in CEI with 0-shot CoT at 219, with 3-shot IcL at 203, and CEG with 0-shot IcL at 201.

Robustness: text-davinci-003 presents an average robustness of  $68.2\%$  across scenarios, with standout performance in AR at  $93.9\%$ , CB at  $86.4\%$ , and PCD at  $85.2\%$ .

GPT-3.5-Turbo. Summary: The model demonstrates an average scenario-prompt accuracy of  $48.2\%$ , an average prompt-average rank of 3 out of 28, and an average robustness score of  $70.1\%$ .

Accuracy: 1) Overall performance: Displayed in Figure 9.58(a), GPT-3.5-Turbo showcases an average scenario-prompt accuracy of  $48.2\%$ , alongside a prompt effectiveness average variability (std) of 8.2. The top scenario-prompt pairs are highlighted by a 3-shot IcL in ATE achieving a peak score of  $80.8\%$ , closely followed by 3-shot IcL in CB at  $80.1\%$ , and 3-shot IcL in PCD at  $77.0\%$ . It is worth noticing that  $89.9\%$  of the scenario-prompt pairs manage to surpass the random guess accuracy, with a small fraction,  $1.1\%$ , exceeding an  $80\%$  accuracy threshold. 2) Scenario performance: In scenarios where GPT-3.5-Turbo surpasses the random guess accuracy, the top 3 scenarios having the highest average accuracy are PCD with an outstanding average score of  $75.2\%$ , CA at  $68.4\%$ , and AR at  $65.0\%$ . 3) Prompt efficiency: The most effective prompts are manual CoT at  $58.8\%$ , 3-shot IcL at  $52.2\%$ , and 1-shot IcL at  $50.1\%$ . In the context of scenario-prompt pairs where the model surpasses the random guess accuracy, manual CoT and 3-shot IcL are ahead in 20 out of 21 scenarios. They are followed by 1-shot IcL, EF, 0-shot IcL, and adversarial ignore, each outperforming in 19 scenarios. 4) Language influence: English outperform Chinese in 18 out of 21 analyzed scenarios, with higher accuracy leads in ATE, ETT, and CDE, revealing language accuracy differences of  $33.4\%$ ,  $26.6\%$ , and  $25.1\%$ , respectively. Conversely, scenarios such as CEG, EAE and CORR showcase superior performance in Chinese, with language accuracy differences of  $9.2\%$ ,  $3.5\%$ , and  $0.8\%$ , respectively.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c9480a4bdd76b077f2adb67e85bfc42aa0a0c5ef002e42e84cbfdd2ab061dc48.jpg)



(a) Performance of GPT-4


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/90370cd8d2082a6cb92b527fe8a7659b080041f6c907b509d1f3fed71996d565.jpg)



(b) Model-prompt rank of GPT-4



Figure 9.59 Heatmap of GPT-4.


Ranking: 1) Prompt-average rank: As shown in Figure 9.47, GPT-3.5-Turbo clinches its highest prompt-average ranks in NIE, CEI, and CDE, all at rank 1. Yet, it ranks lower in CB at 9, AR at 6, and EAE at 6, indicating areas for improvement. The average prompt-average rank across 21 scenarios stands at 3 out of 28, with a standard deviation reflecting performance consistency at 2.0. 2) Model-prompt rank: Detailed in Figure 9.58(b), GPT-3.5-Turbo's top model-prompt ranks include PS with manual CoT at rank 2, NDE with manual CoT also at 2, and PN with manual CoT at 2. The most significant challenges are in CB, with the lowest ranks observed with basic at 182, adversarial doubt at 172, and 0-shot CoT at 171.

Robustness: GPT-3.5-Turbo records an average robustness score of  $70.1\%$  across scenarios, showing the highest robust in EAE at  $87.0\%$ , ATE at  $83.5\%$ , and PCD at  $83.2\%$ .

GPT-4. Summary: The model boasts an average scenario-prompt accuracy of  $56.8\%$ , achieves an average prompt-average rank of 2 out of 28 (the highest average prompt-average rank), and holds an average robustness score of  $83.7\%$ .

Accuracy: 1) Overall performance: According to Figure 9.59(a), GPT-4 achieves an average scenario-prompt accuracy of  $56.8\%$ , with an average standard deviation for prompt effectiveness at 9.9. The top scenario-prompt pairs are manual CoT in CB with a score of  $97.8\%$ , 3-shot IcL in FAS at  $95.2\%$ , and manual CoT in CA at  $94.8\%$ . To be noticed  $95.8\%$  of the scenario-prompt pairs surpass the random guess accuracy, with  $16.9\%$  exceeding an  $80\%$  accuracy threshold. 2) Scenario performance: In scenarios where GPT-4 beats the random guess accuracy, the top three scenarios in terms of average accuracy are CA at  $91.8\%$ , AR at  $88.3\%$ , and PCD at  $79.1\%$ . 3) Prompt efficiency: The highest effectiveness is observed with manual CoT at  $75.4\%$ , 3-shot IcL at  $60.0\%$ , and adversarial doubt at  $54.6\%$ . Moreover, manual CoT, 3-shot IcL, and 1-shot IcL exceed the random guess accuracy in all 21 scenarios. 4) Language influence: English performs better than Chinese in 16 out of 21 scenarios, showing significant advantages in ATE, CDE, and NIE, with language accuracy differences of  $21.1\%$ ,  $18.2\%$ , and  $15.9\%$ , respectively. On the other hand, in scenarios like CEG, AR, and FAS, Chinese shows superior

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/86935ccd7080e7aa2a04c764b287a324697a311304fcb5690ce7de0ad91164cb.jpg)



(a) Performance of Claude2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/e68a718fe792d07db2fdbddebc23652e8f3a20dae32e8e732ed2a6016f85350d.jpg)



(b) Model-prompt rank of Claude2



Figure 9.60 Heatmap of Claude2.


performance with language accuracy differences of  $12.2\%$ ,  $2.8\%$ , and  $1.7\%$ , respectively.

Ranking: 1) Prompt-average rank: As indicated in Figure 9.47, GPT-4 achieved a first-place prompt-average rank in 15 scenarios. Its lowest rank was 24th in CEI, with an additional four scenarios ranked at 4th place. Across 21 scenarios, the model's average prompt-average rank is 2 out of 28, with a standard deviation of 5.0. 2) Model-prompt rank: As shown in Figure 9.59(b), GPT-4 has top 1 model-prompt rank in almost all scenarios except in NIE, CEI and CORR. The lowest model-prompt ranks are in CEI with basic at 241, with 0-shot CoT at 236, and with adversarial ignore at 208.

Robustness: GPT-4 boasts an average robustness score of  $83.7\%$  across scenarios, demonstrating the highest robustness in AR at  $97.0\%$ , CA at  $95.2\%$ , and PCD at  $92.0\%$ .

# 9.3.2 Anthropic

Claude2. Summary: The model exhibits an average scenario-prompt accuracy of  $45.3\%$ , secures an average prompt-average rank of 4 out of 28, and attains an average robustness score of  $67.5\%$  across scenarios.

Accuracy: 1) Overall performance: As illustrated in Figure 9.60(a), Claude2 achieves an average scenario-prompt accuracy of  $45.3\%$ , with average variability (standard deviation) in prompt effectiveness at 10.1. The top scenario-prompt pairs are EF in EAE, with a score of  $88.7\%$ , followed by 0-shot IcL in AR at  $86.3\%$ , and 0-shot CoT in the same category at  $85.6\%$ . A significant  $77.8\%$  of scenario-prompt pairs outperform the baseline random guess accuracy, with  $4.8\%$  scoring above  $80\%$  accuracy. 2) Scenario performance: In scenarios where Claude2 outperforms the random guess accuracy, the three scenarios with the highest average accuracies are AR, leading with a score of  $75.9\%$ , followed by CA at  $74.0\%$ , and PCD at  $70.7\%$ . 3) Prompt efficiency: The prompts yielding the highest efficiency are basic at  $49.9\%$ , manual CoT at  $49.0\%$ , and EF at  $48.7\%$ . As to the number of scenario-prompt pairs where the model exceeds random guess accuracy, the basic leads in 18 out of 21 scenarios, followed by adversarial ignore in 18, and adversarial doubt in 18 scenarios. 4) Language

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f2e38cd2d30222aedda5f3a192033ec32687a22a45f9d37fa3ff3ff54f017f49.jpg)



(a) Performance of InternLM-chat (7B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/afc2a65c970ac77b4f579395bbe57a9d4b8e85bce11636a29370640cb2a3962c.jpg)



(b) Model-prompt rank of InternLM-chat (7B)



Figure 9.61 Heatmap of InternLM-chat (7B).


influence: English demonstrates superior performance in 18 out of 21 scenarios, especially in AC, EAE, and CR, with language accuracy differences of  $29.5\%$ ,  $29.0\%$ , and  $21.9\%$ , respectively. In contrast, scenarios like FAS, CEG, and NDE perform better in Chinese, with accuracy differences of  $8.5\%$ ,  $2.2\%$ , and  $1.5\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, Claude2 achieves its best prompt-average ranks in NDE, ETT, and CEG, all at rank 1. On the flip side, it ranks lowest in AC (19), CB (12), and FAS (7), identifying areas needing enhancement. The average prompt-average rank across 21 scenarios is 4th out of 28, with a variability of 4.2. 2) Model-prompt rank: Shown in Figure 9.60(b), Claude2's highest model-prompt ranks are in CORR with EF (1), CEG with EF (1), EAE with EF (2), and CEG with basic (2). The lowest ranks are in CB with 3-shot IcL (242), CB with 1-shot IcL (241), and FAS with 1-shot IcL (215), pinpointing particular challenges.

Robustness: Claude2 showcases an average robustness score of  $67.5\%$  across different scenarios, achieving its highest robustness in CB  $(86.8\%)$ , AR  $(82.0\%)$ , and CEI  $(81.0\%)$ .

# 9.3.3 Shanghai AI Laboratory

InternLM-chat (7B). Summary: The model's average scenario-prompt accuracy is  $34.2\%$ . It has an average prompt-average rank of 12/28 and an average robustness score of  $74.7\%$  across various scenarios.

Accuracy: 1) Overall performance: Illustrated in Figure 9.61(a), InternLM-chat (7B) achieves an average scenario-prompt accuracy of  $34.2\%$ , with an average standard deviation in prompt effectiveness of 6.7. The top scenario-prompt pairs are 3-shot IcL in PCD with a score of  $77.1\%$ , followed closely by EF in the same scenario at  $74.4\%$ , and 0-shot IcL in PCD at  $74.1\%$ . A total of  $56.1\%$  of the scenario-prompt pairs outperform the random guess accuracy, although none surpass the  $80\%$  accuracy mark. 2) Scenario performance: When surpassing random guess accuracy, the top scenarios by average accuracy are PCD at  $70.8\%$ , AR at  $57.8\%$ , and CR at  $54.5\%$ . 3) Prompt efficiency: The most efficient prompts include 3-shot IcL at  $40.9\%$ , manual CoT at  $39.0\%$ , and 1-shot IcL at  $36.2\%$ . Regarding the number of scenario-prompt pairs exceeding the random guess

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d01a24b5c73c97045e0c7cc9468d51fd7f57d5a8d7a938d5770b078de377054d.jpg)



(a) Performance of InternLM-chat (20B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2b6b43d08a40fc14e37fbfb35ac40c709931084e60011273eb82c90f0db0d3ac.jpg)



(b) Model-prompt rank of InternLM-chat (20B)



Figure 9.62 Heatmap of InternLM-chat (20B).


accuracy across scenarios, 3-shot IcL is the frontrunner in 18 out of 21 scenarios, with manual CoT and 1-shot IcL following in 16 and 14 scenarios, respectively. 4) Language influence: English surpasses Chinese in 17 of 21 scenarios, especially in NIE, ETT, and CDE, with language accuracy differences of  $15.9\%$ ,  $11.6\%$ , and  $11.6\%$ , respectively. Conversely, Chinese outperforms in scenarios such as CA, CEG, and CB, with accuracy leads of  $8.9\%$ ,  $8.3\%$ , and  $5.3\%$ , respectively.

Ranking: 1) Prompt-average rank: As highlighted in Figure 9.47, the highest prompt-average ranks for InternLM-chat (7B) are observed in PCD at 5, AR, CR, and NDE all at 7. On the flip side, its lowest ranks are in CEG at 27, CB at 19, and CEI, EAE, and PN, all at 17, pointing out areas for enhancement. Across 21 scenarios, the model averages a prompt-average rank of 12 out of 28, with a standard deviation of 5.1. 2) Model-prompt rank: Shown in Figure 9.61(b), the best model-prompt ranks for InternLM-chat (7B) include PCD with 3-shot IcL at 19, AC with 3-shot IcL at 23, and NIE with 3-shot IcL at 31. The lowest ranks are in CB with 0-shot CoT at 246 and CEG with both 0-shot CoT and EF at 242.

Robustness: InternLM-chat (7B) showcases an average robustness score of  $74.7\%$  across scenarios, with the highest robustness scores in CDE at  $90.6\%$ , ATE at  $90.1\%$ , and ETT at  $86.8\%$ .

InternLM-chat (20B). Summary: The model achieves an average scenario-prompt accuracy of  $36.4\%$ , holds an average prompt-average rank of 10 out of 28, and maintains an average robustness score of  $67.3\%$  across diverse scenarios.

Accuracy: 1) Overall performance: Figure 9.62(a) shows InternLM-chat (20B) achieving an average scenario-prompt accuracy of  $36.4\%$ , with an average prompt effectiveness variability of 6.7. The top scenario-prompt pairs are 3-shot IcL in PCD with a score of  $76.6\%$ , followed by 1-shot IcL in the same scenario at  $76.0\%$ , and EF in PCD at  $75.1\%$ . A total of  $75.1\%$  of the scenario-prompt pairs surpass the random guess accuracy, though none exceed an  $80\%$  accuracy rate. 2) Scenario performance: For scenarios outperforming random guess

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3a5fa78e5ec3221d1c5332a9357aaadbedbe8368b279573493b248f9b54c1fb4.jpg)



(a) Performance of Qwen (7B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/80bbe023288848843b618e1d6dbd94b1e51b133385ceee918d1eaea21b2c8308.jpg)



(b) Model-prompt rank of Qwen (7B)



Figure 9.63 Heatmap of Qwen (7B).


accuracy, the highest average accuracies are found in PCD and AR, both at  $68.4\%$ , and CA at  $60.8\%$ . 3) Prompt efficiency: The top-performing prompts include 1-shot IcL at  $38.8\%$ , basic at  $38.4\%$ , and adversarial doubt at  $38.0\%$ . Regarding prompts where the accuracy of its scenario-prompt pairs exceeds random guess accuracy, adversarial doubt leads in 19 out of 21 scenarios, followed by EF in 18 and 3-shot IcL in 17. 4) Language influence: English surpasses Chinese in accuracy in 16 of the 21 scenarios, particularly in PCD, NIE, and CDE, with language accuracy differences of  $15.9\%$ ,  $10.8\%$ , and  $10.2\%$ , respectively. However, Chinese excels in CEG, IV, and BAS, with  $10.0\%$ ,  $4.2\%$ , and  $3.1\%$  advantages, respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, InternLM-chat (20B) achieves its best prompt-average ranks in AR and NIE at 4, FAS and CR both at 5. Conversely, its lowest prompt-average ranks are in CEG at 24, ECI at 23, and CB at 22, highlighting improvement opportunities. The model holds an average prompt-average rank of 10 out of 28, with a standard deviation of 6.5. 2) Model-prompt rank: Figure 9.62(b) reveals the model's top model-prompt ranks, including PS with manual CoT at 16, PCD with 3-shot IcL at 22, and NIE with 3-shot IcL at 24. The lowest rankings are seen in CORR and ECI with manual CoT, both at 252 and ECI with 3-shot IcL at 251.

Robustness: InternLM-chat (20B) has an average robustness rating of  $67.3\%$  across various scenarios, with top performance in PCD at  $87.3\%$ , CB at  $86.3\%$ , and AR at  $81.8\%$ .

# 9.3.4 Alibaba Cloud

Qwen (7B). Summary: The model records an average scenario-prompt accuracy of  $32.9\%$ , achieves an average prompt-average rank of 12 out of 28, and displays an average robustness score of  $56.6\%$  across multiple scenarios.

Accuracy: 1) Overall performance: According to Figure 9.63(a), Qwen (7B) achieves an average scenario-prompt accuracy of  $32.9\%$ , with an average variation (standard deviation) of 6.0 in prompt effectiveness. The top

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a516734773d9f87e519b4fac468ac2e99dd43562bfda8d62d91340b97f4f573e.jpg)



(a) Performance of Qwen (14B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b44ac7157dc50094a13d9059ce9939d23f438cea8d9ab8a84c88dc546f312cfc.jpg)



(b) Model-prompt rank of Qwen (14B)



Figure 9.64 Heatmap of Qwen (14B).


scenario-prompt pairs feature a 0-shot IcL in PCD with a score of  $65.8\%$ , closely followed by a 3-shot IcL scoring  $64.7\%$ , and EF with  $64.2\%$  in the same scenario. Nearly half  $(48.7\%)$  of the scenario-prompt pairs outperform the baseline random guess accuracy, yet none surpass the  $80\%$  accuracy threshold. 2) Scenario performance: In scenarios where Qwen (7B) surpasses random guess accuracy, the top 3 scenarios having the highest average accuracy are PCD with a score of  $62.3\%$ , AR at  $56.9\%$ , and ECI at  $52.4\%$ . 3) Prompt efficiency: The prompts showing the highest efficacy include manual CoT at  $41.9\%$ , 3-shot IcL at  $36.9\%$ , and 1-shot IcL at  $35.4\%$ . manual CoT stands out, leading in 17 of 21 scenarios, followed by 3-shot IcL in 15, and 1-shot IcL in 13 scenarios, in terms of the accuracy of scenario-prompt pairs surpassing random guess accuracy. 4) Language influence: English demonstrates superior performance in 10 of 21 scenarios, particularly in CDE, ETT, and NDE, with language accuracy differences of  $8.4\%$ ,  $8.0\%$ , and  $7.7\%$ , respectively. On the other hand, Chinese excels in CEG, AR, and AC, with accuracy improvements of  $16.6\%$ ,  $5.5\%$ , and  $4.7\%$ , respectively.

Ranking: 1) Prompt-average rank: As depicted in Figure 9.47, Qwen (7B) achieves its best prompt-average ranks in AC (8), AR (9), and CORR (9). However, it ranks lowest in CA (19), PN (19), and NDE (18), suggesting areas for potential enhancement. The model's overall prompt-average rank across 21 scenarios is 12th out of 28, with a standard deviation of 3.3. 2) Model-prompt rank: Illustrated in Figure 9.63(b), the highest model-prompt ranks for Qwen (7B) are in CDE with manual CoT (12), ETT with manual CoT (13), and NDE with manual CoT (20). The lowest ranks are in FAS with manual CoT (207), NDE with EF (206), and CA with adversarial doubt (197), pinpointing specific areas of challenge.

Robustness: Qwen (7B) displays an average robustness score of  $56.6\%$  across different scenarios, showcasing top robustness in PCD  $(72.4\%)$ , CB  $(61.4\%)$ , and PS  $(61.2\%)$ .

Qwen (14B). Summary: The model demonstrates an average scenario-prompt accuracy of  $34.5\%$ , holds an average prompt-average rank of 11 out of 28, and shows an average robustness score of 57.3 across different scenarios.

Accuracy: 1) Overall performance: Figure 9.64(a) shows that Qwen (14B) achieves an average scenario-prompt accuracy of  $34.5\%$ , with a 7.2 average standard deviation in prompt effectiveness. The top scenario-prompt pairs are led by a 3-shot IcL in PCD with a score of  $76.9\%$ , followed by a 1-shot IcL in the same scenario at  $75.3\%$ , and manual CoT in CA at  $69.8\%$ . Over half  $(53.4\%)$  of the scenario-prompt pairs surpass the random guess accuracy, yet none achieve above  $80\%$  accuracy. 2) Scenario performance: In scenarios where Qwen (14B) exceeds the random guess accuracy, the three leading scenarios in terms of highest average accuracy include PCD at an impressive  $67.1\%$ , followed by AR and CA, each scoring  $56.2\%$ . 3) Prompt efficiency: The most efficient prompts identified are 3-shot IcL at  $44.9\%$ , 1-shot IcL at  $42.2\%$ , and manual CoT at  $37.5\%$ . In terms of the scenario-prompt pairs exceeding random guess accuracy across scenarios, 3-shot IcL leads in all 21 scenarios, followed by 1-shot IcL in 19, and manual CoT in 15 scenarios. 4) Language influence: English proves superior in 18 of 21 scenarios, especially in CB, EAE, and ETT, with language accuracy differences of  $12.7\%$ ,  $11.9\%$ , and  $7.5\%$ , respectively. However, the Chinese perform better in scenarios like CEG, CA, and PCD, with accuracy differences of  $17.2\%$ ,  $6.8\%$ , and  $1.7\%$ , respectively.

Ranking: 1) Prompt-average rank: As indicated in Figure 9.47, Qwen (14B) excels in CEG, ranking 6th, followed by ECI at 7th. It also demonstrates strong performance in PCD, ATE, BAS, and IV, each with an 8th-place rank in prompt-average scores. Its lowest ranks are in EAE (19), CORR (16), and PN (15), highlighting potential areas for development. The model's average prompt-average rank across 21 scenarios is 11th out of 28, with a standard deviation of 3.4. 2) Model-prompt rank: Illustrated in Figure 9.64(b), the model's top model-prompt ranks are in ECI with 1-shot IcL (17), ECI with 3-shot IcL (19), and PCD with 3-shot IcL (21). The lowest ranks are noted in EAE with manual CoT (223), ECI with manual CoT (200), and CEI with manual CoT (197), identifying specific areas for improvement.

Robustness: Qwen (14B) records an average robustness score of  $57.3\%$  across various scenarios, achieving its highest robustness in PCD  $(75.6\%)$ , ECI  $(66.7\%)$ , and CA  $(63.0\%)$ .

# 9.3.5 Baichuan Inc.

Baichuan1 (7B). Summary: The model achieves an average scenario-prompt accuracy of  $30.8\%$ , has an average prompt-average rank of 14 out of 28, and maintains an average robustness score of  $83.1\%$  across different scenarios.

Accuracy: 1) Overall performance: Figure 9.65(a) shows that Baichuan1 (7B) achieves an average scenario-prompt accuracy of  $30.8\%$ , with an average variability (standard deviation) of 6.8 in prompt effectiveness. The top scenario-prompt pairs are a 3-shot IcL in the NIE with a score of  $73.2\%$ , followed by 3-shot IcL in CB at  $58.9\%$ , and a manual CoT in EAE at  $58.3\%$ . Over  $42.3\%$  of the scenario-prompt pairs outperform the baseline random guess accuracy, yet none surpass the  $80\%$  accuracy mark. 2) Scenario performance: In situations where Baichuan1 (7B) exceeds the random guess accuracy, the top three scenarios by average accuracy are CA, leading with a significant score of  $55.3\%$ , followed by CB at  $50.8\%$ , and EAE at  $50.0\%$ . 3) Prompt efficiency: The 3-shot IcL prompt is the most effective, with a score of  $40.7\%$ , closely followed by the 1-shot IcL at  $32.8\%$ . As to the number of scenario-prompt pairs where the model exceeds the random guess accuracy, the 3-shot IcL leads in 15 out of 21 scenarios, followed by 1-shot IcL in 13, and manual CoT in 10 scenarios. 4) Language influence: English has the upper hand in 11 out of 21 scenarios, especially in IV, NIE, and CR, with language accuracy differences of  $10.7\%$ ,  $9.4\%$ , and  $6.5\%$ , respectively. On the other hand, Chinese performs better in CEG, CB, and AC, with advantages of  $15.7\%$ ,  $8.9\%$ , and  $3.7\%$ , respectively.

Ranking: 1) Prompt-average rank: Figure 9.47 illustrates Baichuan1 (7B)'s best prompt-average ranks in scenarios

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9abd609e25d3708afe5670f7c3117cb212f10de7387bb01093fb0a2ac1702f73.jpg)



(a) Performance of Baichuan1 (7B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/83060d48d9107357c1dd6a17f24e1a7c3fd800edddf482098e004cca09abc53c.jpg)



(b) Model-prompt rank of Baichuan1 (7B)



Figure 9.65 Heatmap of Baichuan1 (7B).


such as CEI at rank 3, CB at 5, and EAE at 9. Its lowest ranks are in PS at 28, PN and CR both at 21, indicating areas needing enhancement. The average prompt-average rank across 21 scenarios stands at 14 out of 28, with a standard deviation of 5.6. 2) Model-prompt rank: As depicted in Figure 9.65(b), the top model-prompt ranks for Baichuan1 (7B) are in NIE with a 3-shot IcL at 6, and CEI with manual CoT and with adversarial doubt at 7 and 13, respectively. The lowest ranks are seen in ATE at 246, AR at 246, and NDE with manual CoT at 244, all indicating specific areas of challenge.

Robustness: Baichuan1 (7B) shows remarkable robustness with an average score of  $83.1\%$  across scenarios. It demonstrates top robustness in CA at  $98.9\%$ , EAE at  $97.9\%$ , and CEI at  $97.0\%$ .

Baichuan1-chat (13B). Summary: The model records an average scenario-prompt accuracy of  $21.7\%$ , attains an average prompt-average rank of 23 out of 28, and possesses an average robustness score of  $75.5\%$  across multiple scenarios.

Accuracy: 1) Overall performance: Figure 9.66(a) illustrates that Baichuan1-chat (13B) achieves an average scenario-prompt accuracy of  $21.7\%$ , with an average standard deviation of 5.6 indicating variability in prompt effectiveness. The top scenario-prompt pairs are a 1-shot IcL in PCD with a score of  $62.0\%$ , followed by a 3-shot IcL in the same category at  $59.9\%$ , and a basic prompt in CA at  $55.5\%$ . Only  $20.1\%$  of the scenario-prompt pairs outperform the random guess accuracy, with none exceeding an  $80\%$  accuracy threshold. 2) Scenario performance: When Baichuan1-chat (13B) exceeds the random guess accuracy, the three scenarios with the highest average accuracies include CEG at a prominent score of  $36.5\%$ , followed by PN at  $0.3\%$ , and PS at  $0.2\%$ . 3) Prompt efficiency: No prompt achieves an average higher than the random guess average. In the count of scenario-prompt pairs where the model's accuracy beats the random guess accuracy, the 1-shot IcL is ahead in 6 out of 21 scenarios, with both 3-shot IcL and basic following achieving a lead in 5 scenarios each. 4) Language influence: English shows superiority in 3 out of 21 scenarios, specifically in AC, IV, and PN, with language accuracy differences of  $0.9\%$ ,  $0.5\%$ , and  $0.1\%$ , respectively. In contrast, Chinese excels in CEG, CA, and AR, with

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/dd74ef1f81ef2a2c8d21193a7ac582c76e2b8b5ad3d2576ccc49235d38bd7440.jpg)



(a) Performance of Baichuan1-chat (13B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/333a08bb8635161aa8117e86d4eac71654c563d421123171b86753e70233a175.jpg)



(b) Model-prompt rank of Baichuan1-chat (13B)



Figure 9.66 Heatmap of Baichuan1-chat (13B).


accuracy advantages of  $32.2\%$ ,  $26.5\%$ , and  $22.8\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, Baichuan1-chat (13B) performs best in CEG, ranking at 8. However, it ranks lowest at 28 in 6 scenarios. The average rank across 21 scenarios is 23 out of 28, with a standard deviation of 5.0. 2) Model-prompt rank: As shown in Figure 9.66(b), Baichuan1-chat (13B)'s best model-prompt ranks appear in CEG, with the highest rankings being 0-shot CoT at 49, basic at 53, and 0-shot IcL at 58. The lowest ranks are observed in PCD with EF at 252, CB with 0-shot IcL at 249, CORR with basic at 249.

Robustness: Baichuan1-chat (13B) demonstrates an average robustness score of  $75.5\%$  across various scenarios, showcasing top robustness in ETT at  $93.6\%$ , PS at  $92.7\%$ , and PN at  $92.5\%$ .

Baichuan2-chat (7B). Summary: The model presents an average scenario-prompt accuracy of  $33.9\%$ , secures an average prompt-average rank of 12 out of 28, and achieves an average robustness score of  $63.8\%$ .

Accuracy: 1) Overall performance: According to Figure 9.67(a), Baichuan2-chat (7B) achieves an average scenario-prompt accuracy of  $33.9\%$ , with an average variability in prompt effectiveness indicated by a standard deviation of 7.7. The top scenario-prompt pairs are in a 3-shot IcL in NIE at  $73.2\%$ , EF in PCD at  $69.8\%$ , and a 0-shot IcL in PCD at  $69.0\%$ . More than half of the scenario-prompt pairs  $(50.8\%)$  surpass the random guess accuracy, though none achieve over  $80\%$  accuracy. 2) Scenario performance: When Baichuan2-chat (7B) outperforms the random guess accuracy, the three leading scenarios in terms of average accuracy are PCD with a distinguished score of  $64.2\%$ , followed by AR at  $58.2\%$ , and ECI at  $56.1\%$ . 3) Prompt efficiency: The most effective prompts have been identified as manual CoT at  $43.1\%$ , 3-shot IcL at  $38.9\%$ , and 1-shot IcL at  $35.9\%$ . Concerning scenario-prompt pairs where the model's accuracy outperforms the random guess accuracy, manual CoT is the leader in 16 out of 21 cases, closely followed by both 3-shot IcL and 1-shot IcL, each leading in 15 scenarios. 4) Language influence: In 11 scenarios, English demonstrates superior performance over Chinese,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/659884ea34f314d53ec25eb6ba501a63018945a236965eeac7bc23f76d534641.jpg)



(a) Performance of Baichuan2-chat (7B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d2f6545302263ea1ffd6e5a604d6ef14cdd58971a6175e69deec479a5ddd3e45.jpg)



(b) Model-prompt rank of Baichuan2-chat (7B)



Figure 9.67 Heatmap of Baichuan2-chat (7B).


particularly in CDE, NIE, and ATE, with language accuracy differences of  $8.7\%$ ,  $7.4\%$ , and  $7.3\%$ , respectively. Conversely, Chinese outperforms English in AR, CEG, and CORR, with accuracy differences of  $15.6\%$ ,  $14.7\%$ , and  $12.9\%$ , respectively.

Ranking: 1) Prompt-average rank: Figure 9.47 shows Baichuan2-chat (7B)'s highest prompt-average ranks in NIE, ECI, CEG, and CDE, all at rank 5. The model's lower ranks in CEI at 23, FAS at 22, and CA at 22 suggest areas needing improvement. The average prompt-average rank across 21 scenarios is 12 out of 28, with a standard deviation of 6.4. 2) Model-prompt rank: As shown in Figure 9.67(b), Baichuan2-chat (7B)'s top ranks are highlighted in NIE with a 3-shot IcL at rank 5, NDE with manual CoT at 8, and CDE with 3-shot IcL at 9. The lowest ranks are in CB with adversarial doubt at 231, FAS with 1-shot IcL at 217, and CEI with EF at 215, pinpointing specific areas of challenge.

Robustness: Baichuan2-chat (7B) showcases an average robustness score of  $63.8\%$  across various scenarios, with its strongest robustness in AC at  $95.3\%$ , CB at  $84.2\%$ , and CEI at  $83.5\%$ , indicating high reliability in these areas.

Baichuan2-chat(13B). Summary: The model displays an average scenario-prompt accuracy of  $30.1\%$ , achieves an average prompt-average rank of 15 out of 28, and holds an average robustness score of  $71.6\%$  across different scenarios.

Accuracy: 1) Overall performance: As shown in Figure 9.68(a), Baichuan2-chat (13B) achieves an average scenario-prompt accuracy of  $30.1\%$ , with the variability in prompt effectiveness captured by an average standard deviation of 5.7. The top scenario-prompt pairs are a 3-shot IcL in PCD with a score of  $72.8\%$ , followed closely by a 0-shot IcL at  $69.9\%$  and EF at  $69.5\%$  in the same scenario. A total of  $42.3\%$  of the scenario-prompt pairs outperform the random guess accuracy, with none surpassing the  $80\%$  accuracy threshold. 2) Scenario performance: When Baichuan2-chat (13B) outstrips the random guess accuracy, the top three scenarios by

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1e677f0105f3948e3cab9ad20de74be66056f80a9d63c5720addf5f23807c37d.jpg)



(a) Performance of Baichuan2-chat (13B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6b0edd21a2e1bdbf4b1dbfc4ae6dd614cd3cbf940cbbe19503f2a4af25f466a6.jpg)



(b) Model-prompt rank of Baichuan2-chat (13B)



Figure 9.68 Heatmap of Baichuan2-chat (13B).


average accuracy are PCD with an impressive score of  $64.7\%$ , followed by AR at  $54.7\%$ , and CA at  $53.7\%$ . 3) Prompt efficiency: The most effective prompts are manual CoT at  $35.4\%$ . In terms of overcoming the random guess accuracy for various scenario-prompt pairs, manual CoT is the leader in 14 out of 21 scenarios, with EF following in 10, and 0-shot IcL in 9 scenarios. 4) Language influence: English shows superior performance in 15 out of 21 scenarios, particularly in CB, IV, and FAS, with language accuracy differences of  $8.6\%$ ,  $7.9\%$ , and  $7.7\%$ , respectively. In contrast, Chinese excels in CEG, CA, and AR, with accuracy differences of  $15.7\%$ ,  $6.6\%$ , and  $4.4\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, Baichuan2-chat (13B) attains its top prompt-average ranks with a 4th place in CEG, a 5th place in PN, and ties for 8th place in both CR and ECI. However, it ranks lowest in CB at 28, IV at 27, and BAS at 25, highlighting areas needing development. The model's average prompt-average rank across 21 scenarios is 15 out of 28, with a standard deviation of 6.9. 2) Model-prompt rank: Figure 9.68(b) showcases the model's best model-prompt ranks in PN with a 3-shot IcL at 12, CEG with adversarial doubt at 16, and with adversarial ignore at 18. The lowest ranks are noted in CB with 0-shot CoT at 250, basic at 247, and 0-shot IcL at 245, pinpointing specific areas for improvement.

Robustness: Baichuan2-chat (13B) exhibits an average robustness score of  $71.6\%$  across scenarios, with its strongest performance in CEI at  $90.6\%$ , AC at  $88.2\%$ , and PCD at  $82.8\%$ , indicating a high degree of reliability in these areas.

# 9.3.6 Meta

Llama2 (7B). Summary: The model achieves an average scenario-prompt accuracy of  $27.6\%$ , has an average prompt-average rank of 19 out of 28, and maintains an average robustness score of  $74.8\%$  across scenarios.

Accuracy: 1) Overall performance: Presented in Figure 9.69(a), Llama2 (7B) scores  $27.6\%$  in average scenario-prompt accuracy, with a high variability in effectiveness shown by an average prompts' standard deviation

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a03aa2dfc4021f55a9f6a3ddeb51190d458cc13e738c04df82fc55221dfbf5c7.jpg)



(a) Performance of Llama2 (7B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2bd27117509322b7e7058f232dcddba0b8cf80566231b0c7bffdfb3c0df5bc8c.jpg)



(b) Model-prompt rank of Llama2 (7B)



Figure 9.69 Heatmap of Llama2 (7B).


of 14.0. The top scenario-prompt pairs are manual CoT in ATE at  $83.4\%$ , a 3-shot IcL in NIE at  $73.3\%$ , and manual CoT in ETT at  $70.1\%$ . About  $39.7\%$  of the scenario-prompt pairs outperform the random guess accuracy, with a marginal  $0.5\%$  exceeding  $80\%$  accuracy. 2) Scenario performance: When identifying scenarios where Llama2 (7B) exceeds the random guess accuracy, the top scenarios with the highest average accuracies are CEG at  $33.6\%$ , PN at  $2.9\%$ . 3) Prompt efficiency: The most effective prompts are 3-shot IcL at  $41.5\%$ , 1-shot IcL at  $33.0\%$ , and manual CoT at  $32.2\%$ . As to the number of scenario-prompt pairs where the model exceeds the random guess accuracy, the 3-shot IcL leads in 18 out of 21 scenarios, followed by 1-shot IcL in 13, and manual CoT in 11 scenarios. 4) Language influence: English surpasses Chinese in 13 out of 21 scenarios, especially in NIE, CDE, and ATE, with language accuracy differences of  $14.5\%$ ,  $13.0\%$ , and  $10.9\%$ , respectively. Conversely, Chinese outperforms in CEG, CORR, and FAS, with differences of  $17.6\%$ ,  $8.7\%$ , and  $6.3\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, Llama2 (7B)'s highest prompt-average ranks is in PN at 10. The model's lowest rankings are 28th in CA, 25th in PCD, and 22nd across five scenarios, indicating areas requiring improvement. The average prompt-average rank across 21 scenarios stands at 19 out of 28, with a standard deviation of 4.1. 2) Model-prompt rank: As shown in Figure 9.69(b), Llama2 (7B) achieves its highest model-prompt ranks in several key areas: it ranks third in both ETT and NIE, accomplished using manual CoT and a 3-shot IcL respectively. Additionally, it secures a fourth-place position in CDE and ATE, both attained through manual CoT, showcasing its strengths in complex causal analysis. The model faces significant challenges in AR with manual CoT at 252, CR with 0-shot CoT at 250, and CA with manual CoT at 250.

Robustness: Llama2 (7B) maintains an average robustness score of  $74.8\%$  across scenarios, showcasing the highest robustness in EAE at  $96.1\%$ , AC at  $93.7\%$ , and PS at  $88.2\%$ , demonstrating significant resilience in these areas.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8be7c6cd4f5a8469a49e80a1a9642692f9c9aa7c2c62e0faf97467ae55d0e228.jpg)



(a) Performance of Llama2 (13B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a3fc43a65e81689be8a9e1f054a9487bbcf53eb3dc52a6df072af0bdcc84b57d.jpg)



(b) Model-prompt rank of Llama2 (13B)



Figure 9.70 Heatmap of Llama2 (13B).


Llama2 (13B). Summary: The model shows an average scenario-prompt accuracy of  $28.6\%$ , attains an average prompt-average rank of 17 out of 28, and achieves an average robustness score of  $81.9\%$ .

Accuracy: 1) Overall performance: Illustrated in Figure 9.70(a), Llama2 (13B) achieves an average scenario-prompt accuracy of  $28.6\%$ , with significant variability in prompt effectiveness indicated by an average prompts' standard deviation of 14.0. The top scenario-prompt pairs feature manual CoT in ATE with a high score of  $87.4\%$ , 3-shot IcL in NIE at  $73.3\%$ , and manual CoT in ETT at  $70.0\%$ . Approximately  $41.8\%$  of the scenario-prompt pairs surpass the random guess accuracy, with a small fraction  $(0.5\%)$  achieving over  $80\%$  accuracy. 2) Scenario performance: For scenarios in which Llama2 (13B) outperforms the random guess accuracy, the top three scenarios ranked by their average accuracy are CEG with an impressive score of  $32.2\%$ , ATE at  $19.4\%$ , and PN at  $2.8\%$ . 3) Prompt efficiency: The best-performed prompts include 3-shot IcL at  $45.0\%$ , manual CoT at  $37.1\%$ , and 1-shot IcL at  $33.5\%$ . In scenario-prompt pairs where the model's accuracy exceeds the random guess accuracy, the 3-shot IcL is the frontrunner in 18 out of 21 cases. It is succeeded by the 1-shot IcL, which leads in 14 scenarios, and the 0-shot IcL, which leads in 13 scenarios. 4) Language influence: In 10 out of 21 scenarios, English shows superiority over Chinese, especially in ATE, NIE, and CDE, language accuracy differences of  $18.4\%$ ,  $15.4\%$ , and  $14.9\%$ , respectively. On the other hand, Chinese outperforms in CA, CEG, and AC, with differences of  $23.6\%$ ,  $13.4\%$ , and  $7.9\%$ , respectively.

Ranking: 1) Prompt-average rank: As Figure 9.47 shows, Llama2 (13B)'s top prompt-average ranks are found in CB at 8 and PN at 9. However, it ranks lowest in CA at 26, AC at 23, and ETT at 22, highlighting areas needing development. The average rank across 21 scenarios is 17 out of 28, with a standard deviation of 4.2. 2) Model-prompt rank: Figure 9.70(b) presents the model's model-prompt ranks, featuring a top rank in NIE with a 3-shot IcL at 1, a third-place in ATE via manual CoT, and fourth-place positions in ETT and NDE, both achieved with manual CoT. The most significant challenges are in EAE with manual CoT at 252, AC with adversarial ignore at 251, and CR with 0-shot CoT at 249.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cfa3b2bf467e29aacdbd0b3164a973f4d29861b1bafc48e56d2f26b7f72c6e57.jpg)



(a) Performance of Llama2 (70B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ffd0b5547dc56c94d6d6a1a52cb7813642d4b423e27c4ad8bf99edeaa753cf63.jpg)



(b) Model-prompt rank of Llama2 (70B)



Figure 9.71 Heatmap of Llama2 (70B).


Robustness: Llama2 (13B) maintains an impressive average robustness score of  $81.9\%$  across scenarios, exhibiting top robustness in AC at  $99.2\%$ , EAE at  $96.0\%$ , and CB at  $93.1\%$ , demonstrating significant resilience in these areas.

Llama2 (70B). Summary: The model's average scenario-prompt accuracy is  $28.1\%$ , with the average prompt-average rank of 16/28 and an average robustness score of  $72.7\%$ .

Accuracy: 1) Overall performance: As illustrated in Figure 9.71(a), Llama2 (70B) achieves an average scenario-prompt accuracy of  $28.1\%$ , with significant variation in prompt effectiveness, demonstrated by an average prompts' standard deviation of 16.3. The top scenario-prompt pairs are manual CoT in ATE at  $89.4\%$ , 3-shot IcL in PCD at  $80.9\%$ , and 0-shot IcL in AR at  $78.4\%$ . Approximately  $41.8\%$  of the scenario-prompt pairs outperform the random guess accuracy, with a small portion  $(1.1\%)$  exceeding  $80\%$  accuracy. 2) Scenario performance: When Llama2 (70B) exceeds the accuracy of the random guess accuracy, the three scenarios with the highest average accuracies include PCD at  $52.9\%$ , AR at  $51.1\%$ , and CR at  $38.0\%$ . 3) Prompt efficiency: The leading prompts include 3-shot IcL at  $48.8\%$ , 1-shot IcL at  $39.1\%$ , and manual CoT at  $37.5\%$ . Regarding the scenario-prompt pairs where the model's accuracy outstrips the random guess accuracy, the 3-shot IcL takes the lead in 20 of the 21 scenarios. This is followed by the 1-shot IcL, which is ahead in 17 scenarios, and the manual CoT, leading in 13 scenarios. 4) Language influence: In 16 out of 21 scenarios, English demonstrates superior performance over Chinese, particularly in CB, ATE, and CDE, with language accuracy differences of  $19.0\%$ ,  $17.7\%$ , and  $17.7\%$ , respectively. Conversely, Chinese outshines English in AR, CEG, and IV, with differences of  $21.7\%$ ,  $12.8\%$ , and  $0.9\%$ , respectively.

Ranking: 1) Prompt-average rank: According to Figure 9.47, Llama2 (70B)'s highest ranks are seen in PN at 3, PS at 5, and CDE at 7. The model encounters its most significant difficulties in CEI, ranking 28th, AC at 26th, and both IV and FAS at 25th, pointing to areas needing enhancement. The average rank across 21 scenarios is 16 out of 28, with a standard deviation of 7.4. 2) Model-prompt rank: Figure 9.71(b) highlights the model's top

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a3a9cc712eff061476050856c2c0ca18ff116e39b641b606925b79ef2e9c4bf2.jpg)



(a) Performance of Llama2-chat (70B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ab03776481b4a7876d22b1e87158a6a19d6b8d38b2f0b0dbe214d77d615c9b2e.jpg)



(b) Model-prompt rank of Llama2-chat (70B)



Figure 9.72 Heatmap of Llama2-chat (70B).


ranks in ATE with manual CoT at 2, CDE with manual CoT at 2, and ETT with manual CoT also at 2. The most significant challenges are CEI with basic at 252, PCD with 0-shot CoT at 250, and CEI with manual CoT at 250.

Robustness: Llama2 (70B) maintains an impressive average robustness score of  $72.7\%$  across scenarios, with peak robustness in FAS at  $100.0\%$ , AC at  $99.1\%$ , and IV at  $97.0\%$ , indicating strong resilience in these specific areas.

Llama2-chat (70B). Summary: The model presents an average scenario-prompt accuracy of  $28.6\%$ , attains an average prompt-average rank of 16 out of 28, and holds an average robustness score of  $47.8\%$ .

Accuracy: 1) Overall performance: Figure 9.72(a) reveals Llama2-chat (70B) has a score of  $28.6\%$  in average scenario-prompt accuracy, with a variability in effectiveness reflected by an average prompts' standard deviation of 12.8. The top scenario-prompt pairs are a 3-shot IcL in PCD at  $77.5\%$ , followed by a 1-shot IcL at  $74.3\%$ , and EF at  $71.9\%$  in the same scenario. Nearly  $46.6\%$  of the scenario-prompt pairs outperform the random guess accuracy, yet none surpass  $80\%$  accuracy. 2) Scenario performance: In scenarios where Llama2-chat (70B) surpasses the random guess accuracy, the top 3 scenarios having the highest average accuracy are PCD with a score of  $59.2\%$ , CR at  $40.8\%$ , and CEG at  $37.1\%$ . 3) Prompt efficiency: The top-performing prompts include a 3-shot IcL at  $41.3\%$  and a 1-shot IcL at  $37.2\%$ . Regarding the number of scenario-prompt pairs where the model exceeds the random guess accuracy, the 3-shot IcL leads in 18 out of 21 scenarios, followed by 1-shot IcL in 16, and manual CoT in 13 scenarios. 4) Language influence: English outshines Chinese in 17 of 21 scenarios, especially in CB, AC, and CDE, with language accuracy differences of  $23.1\%$ ,  $17.7\%$ , and  $17.4\%$ , respectively. However, Chinese outperforms English in scenarios like CEI, IV, and CEG, with  $23.1\%$ ,  $2.3\%$ , and  $1.9\%$  differences, respectively.

Ranking: 1) Prompt-average rank: Figure 9.47 shows Llama2-chat (70B)'s highest ranks in CEG at 7, NIE, and

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ae850f26c2944f6b9093bae13a0c624939917726f4ec9c27e9f3d44890daa0fc.jpg)



(a) Performance of Vicuna-v1.3 (33B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5751c82dbae0564b1efbd9d33dfbbdb733e96210922bfb27a48ef7966dd9f440.jpg)



(b) Model-prompt rank of Vicuna-v1.3 (33B)



Figure 9.73 Heatmap of Vicuna-v1.3 (33B).


CDE both at 9. The model's poorest performances are observed with a 27th place in CEI, 24th in PN, and tied at 23rd for both BAS and IV. The average prompt-average rank is 16 out of 28, with a standard deviation of 5.5. 2) Model-prompt rank: As shown in Figure 9.72(b), the model's top model-prompt ranks include NDE with manual CoT at 3, CB with manual CoT at 14, and AC with a 3-shot IcL at 15. The most significant challenges are in CA with adversarial ignore at 252, CEI, and AR, both with manual CoT at 251.

Robustness: Llama2-chat (70B) maintains an average robustness score of  $47.8\%$  across scenarios, with peak robustness in FAS at  $79.3\%$ , BAS at  $67.6\%$ , and AC at  $61.4\%$ .

# 9.3.7 Lmsys

Vicuna-v1.3 (33B). Summary: The model demonstrates an average scenario-prompt accuracy of  $29.8\%$ , holds an average prompt-average rank of 16 out of 28, and attains an average robustness score of  $44.0\%$  across scenarios.

Accuracy: 1) Overall performance: As illustrated in Figure 9.73(a), Vicuna-v1.3 (33B) achieves an average scenario-prompt accuracy of  $29.8\%$ , with considerable variability in prompt effectiveness, as indicated by an average standard deviation of 11.2. The top scenario-prompt pairs are a 3-shot IcL in PCD with a score of  $73.3\%$ , followed by EF at  $70.1\%$ , and 1-shot IcL at  $69.5\%$  in the same scenario. Around  $43.9\%$  of the scenario-prompt pairs perform better than the random guess accuracy, though none surpass  $80\%$  in accuracy. 2) Scenario performance: When selecting scenarios in which Vicuna-v1.3 (33B) exceeds the random guess accuracy, and then identifying the top three based on their accuracy, the highest scoring scenarios are PCD at  $55.2\%$ , AR at  $53.7\%$ , and CR at  $43.4\%$ . 3) Prompt efficiency: The leading prompts are 3-shot IcL at an average accuracy of  $42.5\%$ , 1-shot IcL at  $36.1\%$ , and manual CoT at  $33.3\%$ . In situations where the model's accuracies on scenario-prompt pairs surpass the random guess accuracy, the 3-shot IcL takes the lead in 18 of the 21 scenarios. This is closely followed by the 1-shot IcL, which leads in 17 scenarios, with manual CoT and 0-shot IcL both

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/40177e0d2d028253c9b080640efbc3cde72f86654390f680fa460e5703bea886.jpg)



(a) Performance of Koala (13B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2fb7480f4deb81403dce2f343a780a98b611d77c757c99f1cd6a943a71649e63.jpg)



(b) Model-prompt rank of Koala (13B)



Figure 9.74 Heatmap of Koala (13B).


trailing at 10 scenarios. 4) Language influence: English surpasses Chinese in 13 out of 21 scenarios, especially in PCD, PS, and IV, with language accuracy differences of  $11.2\%$ ,  $2.8\%$ , and  $2.2\%$ , respectively. Conversely, Chinese outshines English in scenarios like CEI, CA, and EAE, with significant differences of  $24.4\%$ ,  $22.8\%$ , and  $14.7\%$ , respectively.

Ranking: 1) Prompt-average rank: Figure 9.47 reveals Vicuna-v1.3 (33B)'s top prompt-average ranks in PS at 7, ATE and CR both at 10. The model faces challenges in CA at 27, CEI at 25, and EAE at 25, pinpointing areas needing enhancement. The overall average rank across 21 scenarios is 16 out of 28, with a standard deviation of 5.6. 2) Model-prompt rank: The best model-prompt ranks for Vicuna-v1.3 (33B), as shown in Figure 9.73(b), are achieved in CEI with a 1-shot IcL at 4, PS with manual CoT at 6, and CDE with 3-shot IcL at 10. The model's lowest ranks are in PCD with adversarial doubt at 251, CEG with a 3-shot IcL at 249, and CA with adversarial doubt at 249, highlighting significant challenges.

Robustness: Vicuna-v1.3 (33B) maintains an average robustness score of  $44.0\%$  across different scenarios, with its strongest robustness in CEI at  $76.1\%$ , CORR at  $63.4\%$ , and PS at  $56.7\%$ .

# 9.3.8 UC Berkeley

Koala (13B). Summary: The model's average scenario-prompt accuracy is  $28.3\%$ , with an average prompt-average rank of 19/28 and an average robustness score of  $84.5\%$ .

Accuracy: 1) Overall performance: Illustrated by Figure 9.74(a), Koala (13B) achieves an average scenario-prompt accuracy of  $28.3\%$ , with an average standard deviation for prompt effectiveness at 10.8. The top scenario-prompt combinations are 3-shot IcL in NIE with a score of  $73.3\%$ , manual CoT in ETT at  $63.0\%$ , and 3-shot IcL in PCD at  $62.9\%$ . Only  $38.6\%$  of the scenario-prompt pairs surpass the random guess accuracy, with none achieving over  $80\%$  accuracy. 2) Scenario performance: Within scenarios outperforming the random guess accuracy, the leading three in terms of average accuracy are CA at  $55.4\%$ , CEG at  $28.6\%$ , and ETT at  $17.5\%$ . 3) Prompt

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/dcbc4bb6f5fcfd110f34a8feb197db316aabb7687ccbcfdea3f263a4e622cfd6.jpg)



(a) Performance of Wizardcoder (15B)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/33ca59f60de699ad4798a1d7b33df9780bfb7c220d3cca89717318a44c9716f7.jpg)



(b) Model-prompt rank of Wizardcoder (15B)



Figure 9.75 Heatmap of Wizardcoder (15B).


efficiency: The top prompts by effectiveness are 3-shot IcL at  $40.7\%$  and 1-shot IcL at  $32.5\%$ . Regarding scenario-prompt pairs exceeding the random guess accuracy, 3-shot IcL is ahead in 18 of 21 scenarios, followed by 1-shot IcL in 13, and 0-shot IcL in 9. 4) Language influence: English outshines Chinese in 16 of 21 scenarios, particularly in CR, EAE, and CORR, with language accuracy differences of  $16.9\%$ ,  $14.1\%$ , and  $8.9\%$ , respectively. In contrast, Chinese excels in CEI, AC, and IV, with advantages of  $14.2\%$ ,  $10.2\%$ , and  $5.5\%$ , respectively.

Ranking: 1) Prompt-average rank: As presented in Figure 9.47, Koala (13B)'s highest prompt-average ranks are in NDE at 9, CA at 10, and ETT at 11. The lowest ranks are in CR at 28, CB at 27, and PS at 27, highlighting potential areas for development. The model's average rank across 21 scenarios is 19 out of 28, with a variability of 5.8. 2) Model-prompt rank: Figure 9.74(b) shows Koala (13B)'s top model-prompt ranks in NIE with 3-shot IcL at 1, PN with 3-shot IcL at 4, and ETT with manual CoT at 6. The lowest model-prompt ranks occur in CR with adversarial ignore at 252, CB with adversarial doubt at 252, and CEG with adversarial ignore at 251.

Robustness: Koala (13B) maintains an impressive average robustness score of  $84.5\%$  across different scenarios, showcasing the highest robustness in NIE at  $99.7\%$ , ATE at  $99.3\%$ , and ETT at  $99.3\%$ .

# 9.3.9 Microsoft

Wizardcoder (15B). Summary: The model's average scenario-prompt accuracy is  $28.9\%$ , with an average prompt-average rank of 19/28 and an average robustness score of  $89.8\%$ .

Accuracy: 1) Overall performance: The performance analysis in Figure 9.75(a) reveals that Wizardcoder (15B) achieves an average scenario-prompt accuracy of  $28.9\%$ , with an average standard deviation of 8.0 for prompt effectiveness. Noteworthy performances of the top scenario-prompt pairs include achieving a score of  $63.4\%$  in manual CoT for CA,  $62.6\%$  in manual CoT for CB, and  $61.7\%$  in 3-shot IcL for ETT. Additionally,  $41.3\%$  of the scenario-prompt pairs outperform the baseline random guess accuracy, though none surpass  $80\%$  accuracy. 2) Scenario performance: For scenarios in which Wizardcoder (15B) outperforms the random guess accuracy, the

three leading scenarios by average accuracy are AR with a score of  $53.9\%$ , followed by CB at  $51.4\%$ , and CEG at  $34.0\%$ . 3) Prompt efficiency: The most efficient prompts identified are 3-shot IcL with an effectiveness score of  $40.0\%$  and 1-shot IcL at  $34.7\%$ . Among 21 scenarios' scenario-prompt pairs, the 3-shot IcL prompt leads in 17 for surpassing the random guess accuracy, followed by 1-shot IcL in 16 scenarios, and manual CoT in 9. 4) Language influence: In 11 out of 21 scenarios, English language prompts show superior performance over Chinese, particularly in scenarios like ETT, EAE, and CB, with language accuracy differences of  $6.3\%$ ,  $5.0\%$ , and  $4.6\%$ , respectively. Conversely, Chinese excels in ECI, CEG, and AC, with accuracy advantages of  $12.8\%$ ,  $5.8\%$ , and  $4.0\%$ , respectively.

Ranking: 1) Prompt-average rank: Figure 9.47 highlights that Wizardcoder (15B)'s best prompt-average ranks are observed in CB and CEI (both ranked 4th), and AC (ranked 7th). However, the model shows room for improvement in PN, NDE, and BAS, with ranks of 28, 27, and 27, respectively. The average prompt-average rank across 21 scenarios stands at 19 out of 28, with a standard deviation of 7.2. 2) Model-prompt rank: As detailed in Figure 9.75(b), the model's top model-prompt ranks in model-prompt combinations are found in ETT with 3-shot IcL (rank 7), CEI with 3-shot IcL (rank 8), and CB with manual CoT (rank 13). On the other hand, the lowest ranks are observed in BAS with basic at 252, BAS with adversarial ignore at 251, BAS with 0-shot CoT at 250.

Robustness: Wizardcoder (15B) exhibits a high average robustness score of  $89.8\%$  across different scenarios, showcasing peak robustness in CA  $(97.4\%)$ , CORR  $(96.9\%)$ , and IV  $(96.0\%)$ .

# 9.4 Causal Scenario-specific Analysis

This section is structured according to the levels of the causal ladder, analyzing specific causal scenarios within each rung. It is organized as follows: Causal Discovery (Section 9.4.1), Association (Section 9.4.2), Intervention (Section 9.4.3), and Counterfactuals (Section 9.4.4). Prior to exploring each scenario, we introduce several additional terms vital for assessing model performance in causal scenarios and tasks, summarised in Tables 9.6 and 9.7. These extend beyond the metrics previously discussed in Section 6.4. Note that, for ease of reading, these terms will be presented in italic font throughout the entire section. Additionally, causal scenarios can be categorized into two types based on the number of causal tasks they involve: single-task causal scenarios and multi-task causal scenarios. We outline the structure of evaluative paragraphs for each type of causal scenarios as below to enhance readability and comprehension.

Single-task causal scenario. For evaluating causal scenarios that contain only one causal task (e.g., AR, EAE), we assess the scenario based on model performance, prompt gain, and language proficiency, respectively.

For model performance, we first analyze the distribution of all model-prompt pairs within the scenario, and then compute the median and third quartile accuracies. These accuracy metrics provide insights into the understandability of the task, as outlined in Table 6.1. Note that, in the CEG scenario - characterized by a negligible random guess value - the task is determined to be easy based on its performance and the inherent simplicity of natural language questions. Subsequently, we evaluate the top accuracies within the scenario, including the top three models ranked by average accuracy and the top model-prompt pair. Using these accuracies, we determine the degree of solvability for the scenario according to Table 6.3. We also examine the stability of the models by computing the model volatility as introduced in Section 6.3, identifying the top three most stable and most unstable models based on this metric. Finally, we consider the ratio of open-access to limited-access models among the top five models ranked by average accuracy. The disparity between open

<table><tr><td>Terminology</td><td>Explanation</td></tr><tr><td>model-prompt pair</td><td>A combination of a model and a prompt.</td></tr><tr><td>top model-prompt pair</td><td>The combination that has the top accuracy value across all tested model-prompt pairs in a causal scenario/task.</td></tr><tr><td>prompt gain</td><td>The accuracy of a model on a specific prompt minus the accuracy of the same model on the basic prompt.</td></tr><tr><td>language proficiency</td><td>The model&#x27;s accuracy in a specific language (English or Chinese).</td></tr><tr><td>average model-prompt-gain volatility</td><td>The model-prompt-gain volatility, denoted by Volatility (Gain)1, is calculated as the standard deviation of the model&#x27;s performance gains when using a non-basic prompt (where “non-basic” refer to any prompt that is not the basic prompt) compared to its performance on the basic prompt. That is, 
Volatility (Gain)1 = √(∑j=1N-1(Gij - G̅i)2/N - 1), where Gij represents the performance gain of the j-th non-basic prompt for the i-th model over its basic prompt performance, and N is the total number of prompts. 
The average model-prompt-gain volatility (AMPGV) is defined as the average of the model-prompt-gain volatility across all models in a specific causal scenario/task, denoted mathematically as: 
AMPGV = Mean(Volatility (Gain)1). 
This measure represent the overall dependency of model accuracy improvements on different prompts within the given scenario or task.</td></tr></table>

Tab. 9.6 Explanations for scenario-specific terminologies.

and limited-access models referred to as the open-limited gap, is evaluated based on the criteria set forth in Table 6.2.

For prompt gain, we begin by evaluating the top prompt gains within the scenario. We analyze the two leading prompts based on average accuracy gain relative to the basic prompt and identify the model-prompt pair with the highest gain over the basic prompt. We then address potential exceptions, including instances a) where the top-performing prompt (with the highest average accuracy) may actually decrease the average accuracy for some models compared to their performance with the basic prompt; and b) where all prompts - or conversely, no prompts - result in performance enhancements for certain models over the basic prompt. Next, we analyze the prompt stability by computing the prompt volatility, as introduced in Section 6.5. Finally, we compute the average model-prompt-gain volatility (AMPGV), and report the scenario's prompt dependence. These measures help us understand the critical role that effective prompt design plays in enhancing model performance across specific scenarios.

<table><tr><td>Terminology</td><td>Explanation</td></tr><tr><td>prompt dependence</td><td>As defined in Table 9.8, we analyze the prompt dependence based on AMPGV.</td></tr><tr><td>variance of distribution</td><td>The variance of distribution assesses the diversity in performance distributions of model-prompt pairs across causal tasks in a causal scenario. This metric, critical for evaluating scenarios comprising multiple causal tasks, calculates the standard deviations of the tasks&#x27; median and third quartile accuracies. These values are then compared against a predefined set to ascertain the corresponding degree of variance, as defined in Table 9.9.</td></tr><tr><td>variance of solvability</td><td>This measure evaluates the variance in solvability across causal tasks in a multiple-task causal scenario. It assigns numerical values to each degree of solvability as defined in Table 6.3: 4 for unsolvable, 3 for challenging, 2 for potentially solvable, 1 for solvable, and 0 for well-solved. The solvability gap is then calculated by subtracting the minimum solvability number from the maximum solvability number among the causal tasks within a scenario. For example, if a scenario comprises three causal tasks with solvabilities of challenging (3), solvable (2), and well-solved (0), the solvability gap in this causal scenario is 3. Then, according to Table 9.10, a gap of 3 indicates the variance of solvability of the causal scenario is large.</td></tr><tr><td>variance of model&#x27;s top performance</td><td>The variance of model&#x27;s top performance requires first computing the maximum and minimum values of the highest average accuracies of models across tasks, along with the maximum and minimum values of the top model-prompt pair accuracies. Then, the two gaps are attained by subtracting the minimum from the maximum, respectively. Finally, we derive the variance based on the two gaps and the rules from Table 9.11.</td></tr><tr><td>variance of prompt dependence</td><td>Like prompt dependence, the variance of prompt dependence is also based on the AMPGV. This metric calculates the difference between the maximum and minimum AMPGV values across causal tasks within a scenario, as defined in Table 9.12.</td></tr></table>

Tab. 9.7 Explanations for scenario-specific terminologies (continued).

For language proficiency, we compare model accuracy in English and Chinese, and quantify the proportion of models that exhibit higher average accuracy in English. Additionally, we investigate significant performance disparities across the two languages, identifying models with notable differences in accuracy between English and Chinese.

Multi-task causal scenario. For evaluating causal scenarios that contain multiple causal tasks (e.g., PCD, ECI), our analysis is also structured from the three primary perspectives: model performance, prompt gain, and language proficiency. However, the focus within each is tailored to assess the specific complexities associated with multiple tasks.

<table><tr><td>Conditions</td><td>Degree of prompt dependence</td></tr><tr><td>AMPGV &lt; 5</td><td>low</td></tr><tr><td>5 ≤ AMPGV &lt; 10</td><td>medium</td></tr><tr><td>AMPGV ≥ 10</td><td>high</td></tr></table>


Tab. 9.8 Degree of prompt dependence. The AMPGV stands for the average model-prompt-gain volatility in the causal task/causal scenario.


<table><tr><td>Conditions</td><td>Variance of distribution</td></tr><tr><td>both stds in [0,5)</td><td>minimally divergent</td></tr><tr><td>one of the stds in [0,5) and the other one in [5,10)</td><td>slightly variable</td></tr><tr><td>both stds in [5,10)</td><td>moderately distinct</td></tr><tr><td>one of the stds in [0,5) and the other one in [10,∞)</td><td>considerably varied</td></tr><tr><td>one of the stds in [5,10) and the other one in [10,∞)</td><td>noticeably diverse</td></tr><tr><td>both stds in [10,∞)</td><td>highly divergent</td></tr></table>

Tab. 9.9 Variance of distributions in the causal scenario. To evaluate the diversity of causal tasks in multi-task causal scenarios, the evaluation considers two standard deviations (std): the std of medians and the std of third quarters. Like Table 6.1, the median and the third quartile are computed from the distribution of all model-prompt pairs in the causal task.

For model performance, it contains:

- Distribution: We first consider the distribution of all model-prompt pairs in the scenario and compute its median and third quartile accuracy. Based on these accuracies, we evaluate the understandability of the scenarios as defined in Table 6.1.<sup>34</sup> Then, we conduct a task-specific analysis of the distribution of all model-prompt pairs, computing the median and third quartile accuracies. These accuracy metrics offer insights into the understandability of each task.<sup>35</sup> Finally, we explore the differences between causal tasks by analyzing the range and the standard deviation of their medians and third quartile values, allowing us to draw conclusions about the variance of distribution. Additionally, we may discuss other scenario-specific findings that emerge from the analysis.

- Top Accuracy: We first discuss the leading models that demonstrate the highest average accuracy within the scenario, followed by presenting the top model-prompt pair. Based on these accuracy scores, we evaluate the solvability of the scenario as defined in Table 6.3. Subsequently, our analysis proceeds on a per-task basis, focusing on the models with the highest average accuracy, the top model-prompt pair, and the solvability of causal tasks. Lastly, we extend our analysis across causal tasks, drawing conclusions on the variance of solvability, the variance of model's top performance, and other scenario-specific findings.

- Stability: Initially, we discuss the stability of models in the scenario by listing the three most stable and

<table><tr><td>Conditions</td><td>Variance of solvability</td></tr><tr><td>solvability gap=0</td><td>negligible</td></tr><tr><td>solvability gap=1</td><td>small</td></tr><tr><td>solvability gap=2</td><td>moderate</td></tr><tr><td>solvability gap=3</td><td>large</td></tr><tr><td>solvability gap=4</td><td>extremely large</td></tr></table>


Tab. 9.10 Variance of solvability of causal tasks in the causal scenario. The solvability gap is then calculated by subtracting the minimum solvability number from the maximum solvability number among the causal tasks within a scenario, where the solvability number is defined in Table 6.3.


<table><tr><td>Conditions</td><td>Variance of model&#x27;s top performance</td></tr><tr><td>both gaps in [0,5)</td><td>small</td></tr><tr><td>one of the gaps in [0,5) and the other one in [5,10)</td><td>moderate</td></tr><tr><td>both gaps in [5,10)</td><td>noticeable</td></tr><tr><td>one of the gaps in [0,5) and the other one in [10,∞)</td><td>considerable</td></tr><tr><td>one of the gaps in [5,10) and the other one in [10,∞)</td><td>significant</td></tr><tr><td>both gaps in [10,∞)</td><td>extremely significant</td></tr></table>

Tab. 9.11 Variance of model's top performance in the causal scenario. The two gaps here stand for the gap of max average value (i.e., the gap between the maximum value among the highest average accuracies of models across tasks and the minimum value among the highest average accuracies of models across tasks) and the gap of max value (i.e., the gap between the maximum value among the highest accuracies of model and prompt pairs across tasks and the minimum value among the highest accuracies of model and prompt pairs across tasks).

most unstable models, characterized by their lowest and highest model volatility scores, respectively. $^{36}$  Then, we conduct a task-by-task evaluation, identifying the three most stable and most unstable models for each task. Conclusions are drawn based on these findings.

- Open-Limited Ratio: We analyze the ratio of open-access to limited-access models among the top five models with the highest average accuracy in the scenario. Then, we quantify the open-limited gap using the metrics outlined in Table 6.2.

For prompt gain, we discuss the following aspects:

- Top Gain: First, we examine the two most effective prompts in terms of average accuracy gain over the basic prompt in the scenario. We then analyze the highest accuracy gain over all the model-prompt pairs in the scenario. Following this, we conduct a task-by-task analysis of these perspectives. Finally, we provide a summary of our analysis.

- Exceptions: We begin our evaluation from a scenario-wide perspective, then proceed to analyze each task individually. We consider the following exceptions: a) whether the most effective prompt, which has the highest average prompt gain over the basic prompt, fails in some models in the scenario; b) whether there exists a model for which all prompts either consistently boost performance or fail to improve performance over the basic prompt.

<table><tr><td>Conditions</td><td>Variance of prompt dependence</td></tr><tr><td>gap of AMPGV in [0,5)</td><td>narrow</td></tr><tr><td>gap of AMPGV in [5,10)</td><td>moderate spread</td></tr><tr><td>gap of AMPGV in [10,∞)</td><td>wide</td></tr></table>

Tab. 9.12 Variance of prompt dependence. The gap refers to the difference between the maximum and minimum values of the average model-prompt-gain volatility (AMPGV).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a0862d95e9c4443b77d6c2d8e543736f0e95b7beb6843a52d88f097f0e76e046.jpg)



(a) Distribution of PCD


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4669f4c5c8684066e16bc3c115692aa56a33cc52141459518c0dc2a74a08b246.jpg)



(b) Distribution of ECI


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0443403b1f0b659fcce8b2e1a05890f6d2faeebcb27320ee6239aa8fbfc49b58.jpg)



(c) Distribution of AR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/50ef3bcf1612a4c81b5925411444bd36d6e846ce0214c6256ee424eefa99664b.jpg)



(d) Distribution of CA



Figure 9.76 Distribution of causal discovery. The horizontal coordinate represents the accuracy of the model and the vertical coordinate represents the percentage distribution corresponding to a certain accuracy interval.


- Stability: First, we identify the two most stable and two most unstable prompts, categorized by their lowest and highest prompt volatility as defined in Section 6.5, within the scenario. Subsequently, we compute the average model-prompt-gain volatility (AMPGV) and classify the scenario's prompt dependence using the criteria specified in Table 9.8. We then conduct a task-by-task assessment of prompt stability, AMPGV, and prompt dependence. Finally, we explore the distribution of AMPGV across causal tasks to determine the variance of prompt dependence in the scenario, which may inform further conclusions based on these evaluations.

Finally, we analyze language proficiency by examining:

- English vs. Chinese: We evaluate whether the scenario yields better performance in English or Chinese and quantify the proportion of models that demonstrate superior results in English compared to Chinese.

- Accuracy Difference: We highlight the most significant disparities in model performance between English and Chinese, detailing the top differences in accuracy.

# 9.4.1 Causal Discovery

Pairwise causal discovery. First, we analyze model performance in PCD:

1) Distribution: Figure 9.76(a) illustrates the distribution of model-prompt pairs within PCD, highlighting a median accuracy of  $54.1\%$  and a third quartile of  $68.8\%$ . This suggests the understandability of the scenario is easy, as the median accuracy surpasses the baseline random guess accuracy of  $50.0\%$ . Additionally, Figure C.1 details the distribution of model-prompt pairs across individual tasks, revealing median accuracies of  $50.5\%$  for PCD-B (E-CARE),  $51.3\%$  for PCD-B (COPA),  $56.6\%$  for PCD-C (E-CARE), and  $60.3\%$  for PCD-C (COPA), alongside third quartiles of  $58.0\%$  for PCD-B (E-CARE),  $62.7\%$  for PCD-B (COPA),  $72.7\%$  for

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0e95b130baf4417bfff9989f045994749a2552468f02dd3c62a73a59e8687e5f.jpg)



(a) Model performance of PCD


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ce34a2825ee7032b9162d21a98c69d182a9c03486023e72cf99000f49477c0ac.jpg)



(b) Prompt gain of PCD



Figure 9.77 Heatmap of PCD. The models and prompts are sorted by their averages.


PCD-C (E-CARE), and  $84.6\%$  for PCD-C (COPA). As the random accuracy of each task is  $50\%$ , these tasks all have an easy understandability. By analyzing the differences between tasks, these tasks show a median accuracy range from  $50.5\%$  to  $60.3\%$  with a standard deviation of 4.0. As to the third quartile accuracy, the range is from  $58.0\%$  to  $84.6\%$  with a standard deviation of 10.2. As a result, the scenario has a considerably varied variance of distribution. Moreover, the choice selection tasks in the scenario are easier to understand than the binary classification tasks, and COPA is more easy than E-CARE dataset.

2) Top Accuracy: Figure 9.77(a) reveals that in terms of average accuracy, the leading three models in this scenario are GPT-4 with  $79.1\%$ , GPT-3.5-Turbo with  $75.2\%$ , and text-davinci-003 with  $74.7\%$ . The top model-prompt pair is GPT-4 with EF, achieving an accuracy of  $83.0\%$ . The solvability of the scenario is well-solved as the average accuracies of the top three models all exceed  $70\%$ . Figure C.14 outlines the top performers on a per-task basis. In the PCD-B (E-CARE) task, GPT-4 leads with  $69.6\%$ , followed by GPT-3.5-Turbo at  $64.2\%$ , and text-davinci-003 at  $64.1\%$ , with GPT-4 and manual CoT reaching the highest accuracy of  $73.4\%$ . This result suggests the task's solvability is challenging, as the top model-prompt pair accuracy falls below  $80\%$ . For the PCD-B (COPA) task, the best averages are by GPT-4 at  $78.8\%$ , text-davinci-003 at  $70.9\%$ , and GPT-3.5-Turbo at  $65.5\%$ . The peak accuracy appears in GPT-4 combined with manual CoT leading at  $82.0\%$ . The solvability of the task is solvable as the top-1 model's average accuracy reaches  $70\%$ . In the PCD-C (E-CARE) category, GPT-3.5-Turbo tops with  $79.1\%$ , followed by GPT-4 at  $76.6\%$ , and text-davinci-003 at  $76.2\%$ , with GPT-4 using EF reaching the highest at  $83.2\%$ . The task's solvability is well-solved as all 3 leading models exceed  $70\%$  in average accuracy. Lastly, for PCD-C (COPA), GPT-3.5-Turbo achieves  $91.9\%$ , GPT-4

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0e0300cda84278eb3f3d08103fdb7de63074e62327cee21ba99bc245590a4686.jpg)



Figure 9.78 Language comparison of PCD. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


scores  $91.5\%$ , and InternLM-chat (20B) achieves  $90.1\%$ , with GPT-4 and EF reaching the peak accuracy of  $98.0\%$ . The task also has a well-solved solvability with all top models achieving over  $70\%$  in average accuracy. Through comparing different tasks, the variance of solvability between the tasks is large. Moreover, the top-1 model's average accuracy ranges from  $69.6\%$  to  $91.9\%$  (difference of  $22.3\%$ ), and the top model-prompt pair's accuracy ranges from  $73.4\%$  to  $98.0\%$  (difference of  $24.6\%$ ). Therefore, the scenario's variance of model's top performance is extremely significant. Also, we can conclude that for binary classification tasks, the top average model is GPT-4, while for choice selection tasks, the top average model is GPT-3.5-Turbo. On the other hand, all of the tasks' top model-prompt pairs contain GPT-4, indicating its great potential. The top 1 average accuracy and accuracy of top model-prompt pair in the four tasks satisfy a similar regularity to the one in the model's distribution, which is the choice selection tasks are easier to solve than the binary classification tasks, and COPA dataset is easier than E-CARE dataset.

3) Stability: The most stable models, characterized by the lowest model volatility, are GPT-3.5-Turbo (1.3), Baichuan1 (7B) (2.1), and text-curie-001 (2.2). The models displaying the greatest sensitivity to different prompts, evidenced by their high model volatility, are Vicuna-v1.3 (33B) (15.8), Llama2 (70B) (15.6), and Llama2-chat (70B) (14.3). Next, we analyze the stability of the model task by task. For PCD-B (E-CARE), the models with the least model volatility are GPT-4 (2.2), Qwen (7B) (2.8), and Baichuan2-chat (7B) (3.0), while the most sensitive models are InternLM-chat (20B) (13.8), Vicuna-v1.3 (33B) (13.0), and Llama2 (70B) (11.8). For PCD-B (COPA), the models showing the least sensitivity are Wizardcoder (15B) (1.4), GPT-4 (2.0), and GPT-3.5-Turbo (2.5). The most variable models are Vicuna-v1.3 (33B) (17.2), Llama2 (70B) (16.2), and Llama2 (13B) (14.1). As to PCD-C (E-CARE), the most stable models are curie (6.7B) (1.2), GPT-3.5-Turbo (1.3), and text-curie-001 (1.2). The models with the highest sensitivity to prompts are Baichuan1-chat (13B) (20.4), Llama2 (13B) (17.0), and Vicuna-v1.3 (33B) (16.3). Finally, for PCD-C (COPA), the most stable models are text-curie-001 (0.6), text-babbage-001 (0.8), and curie (6.7B) (1.7). The models most affected by prompt choice are Baichuan1-chat (13B) (24.6), Llama2-chat (70B) (23.1), and Llama2 (70B) (22.5). Finally, it is positive to note that both GPT-3.5-Turbo and GPT-4 demonstrate high accuracy and stability across four tasks. Conversely, it

is observed that the llama-series and Vicuna-v1.3 (33B) often lack stability in tasks within this scenario.

4) Open-Limited Ratio: Considering the ratio of one open-access model to four limited-access models among the top five models in the entire scenario, the open-limited gap is moderate.

Then, we analyze prompt gain in PCD:

1) Top Gain: Figure 9.77(b) illustrates that the two most effective prompts in terms of average accuracy improvement over the basic prompt are 3-shot IcL, with a  $9.0\%$  gain, and 1-shot IcL, with a  $7.0\%$  gain. The highest leap in accuracy compared to the basic prompt was achieved by Llama2 (70B) using 3-shot IcL, resulting in a  $33.5\%$  increase. A more granular analysis of each task is provided next. Figure C.15 displays the heatmaps of accuracy gains for all tasks in the scenario. In the PCD-B (E-CARE) task, the top two prompts leading to the highest gains are 3-shot IcL at  $6.4\%$  and 1-shot IcL at  $4.4\%$ , with Llama2 (70B) using 3-shot IcL showing the most significant improvement of  $25.1\%$ . For the PCD-B (COPA) task, the leading prompts in gain are 3-shot IcL at  $10.0\%$  and 1-shot IcL at  $4.9\%$ , with Llama2 (70B) using 3-shot IcL marking the largest increase at  $35.2\%$ . In the PCD-C (E-CARE) task, the top gains are from 3-shot IcL at  $7.4\%$  and 1-shot IcL at  $7.2\%$ , with the most substantial accuracy boost seen with Baichuan1-chat (13B) using 1-shot IcL, achieving a  $37.0\%$  increase. Lastly, for the PCD-C (COPA) task, the highest gains were from 3-shot IcL at  $12.1\%$  and 1-shot IcL at  $11.4\%$ , with Baichuan1-chat (13B) using 1-shot IcL experiencing the most significant improvement, at  $52.1\%$ . In summary, the information suggests that tasks of lesser complexity generally lead to the most significant improvements in this scenario. For every individual task, the 3-shot IcL and 1-shot IcL are recognized as the 2 most effective prompts, highlighting the consistent efficacy of these two prompts in this scenario. Additionally, combined with specific models, these 2 prompts also achieve the highest gains compared to other model-prompt pairs.

2) Exceptions: Though the 3-shot IcL prompt stands out as the highly effective prompt across most models, it has exceptions in Baichuan2-chat (7B), Claude2, and GPT-4. In the task of PCD-B (E-CARE), this leading prompt falls short of enhancing performance for Baichuan2-chat (7B), text-davinci-002, Claude2, and GPT-3.5-Turbo. However, it is noteworthy that all prompts manage to boost Baichuan1-chat (13B)'s performance over the basic prompt in this specific task. For the PCD-B (COPA) task, the best prompt does not improve the performance of text-babbage-001, Claude2, and text-davinci-003 over the basic prompt, with text-davinci-003 showing no improvement over the basic prompt from any prompt. In PCD-C (E-CARE), the top prompt fails to give a positive effect on Qwen (7B), Baichuan2-chat (7B), Claude2, InternLM-chat (20B), GPT-4, and GPT-3.5-Turbo over the basic prompt. Regarding PCD-C (COPA), the leading prompt, 3-shot IcL, does not contribute positively to text-curie-001, Qwen (7B), Baichuan2-chat (7B), InternLM-chat (20B), and GPT-4 over the basic prompt. All prompts are capable of elevating Llama2 (7B)'s performance in this task. It seems that 3-shot IcL has difficulty promoting the performance of Baichuan2-chat (7B) and Claude2 in most of the tasks (3 out of 4) in this scenario.

3) Stability: The scenario highlights that the two most stable prompts, based on their low prompt volatility, are 0-shot IcL with a prompt volatility of 4.0 and adversarial ignore with a prompt volatility of 5.2. Conversely, the prompts with the highest variability are 3-shot IcL and manual CoT, with prompt volatility of 9.1 and 8.0, respectively. The scenario's average model-prompt-gain volatility (AMPGV) is 7.3, suggesting a medium prompt dependence. Conducting the analysis task by task, for PCD-B (E-CARE), the most stable prompts are 0-shot IcL (4.0 prompt volatility) and EF (4.4 prompt volatility), whereas the least stable are manual CoT (11.1 prompt volatility) and 0-shot CoT (9.2 prompt volatility). An AMPGV of 7.3 indicates a medium prompt dependence. For PCD-B (COPA), the most stable prompts are 0-shot IcL (6.9 prompt volatility) and adversarial ignore (7.1 prompt volatility), with the least stable being manual CoT (14.8 prompt volatility) and 3-shot IcL (10.1 prompt

volatility). An AMPGV of 9.4 indicates a medium level of prompt dependence. In the PCD-C (E-CARE) task, the most stable prompts are 0-shot IcL (5.2 prompt volatility) and adversarial ignore (8.4 prompt volatility), while the least stable are 3-shot IcL (10.8 prompt volatility) and manual CoT (10.7 prompt volatility). An AMPGV of 7.9 suggests a medium prompt dependence. For PCD-C (COPA), the prompts with the smallest prompt volatility are adversarial ignore (6.9 prompt volatility) and 0-shot IcL (7.3 prompt volatility), while the most unstable prompts are 3-shot IcL (15.8 prompt volatility) and 1-shot IcL (13.8 prompt volatility). With an AMPGV of 9.2, the task has a medium level of prompt dependence. After evaluation of all the tasks in the scenario, we find that the AMPGV, which indicate the variance of prompt dependence in the scenario, have a narrow range from 7.3 to 9.4. Moreover, 0-shot IcL and adversarial ignore are recognized as the most stable prompts. Furthermore, IcL and CoT are identified as the least stable prompts.

In the end, we measure language proficiency in PCD:

1) English vs. Chinese: As illustrated in Figure 9.78, models generally perform better on the English test set than on the Chinese test set, with 19 out of 28 models showing superior performance in English.

2) Accuracy Difference: Significant performance differences favoring English appears in models such as InternLM-chat (20B) with a  $15.9\%$  difference, Llama2-chat (70B) with a  $12.1\%$  difference, and Vicuna-v1.3 (33B) with an  $11.2\%$  difference. On the other hand, some models, including Baichuan1-chat (13B) with a  $16.3\%$  difference, Baichuan2-chat (7B) with a  $5.2\%$  difference, and Qwen (7B) with a  $2.8\%$  difference, demonstrate higher capabilities in Chinese than in English.

Event causality identification. First, we assess model performance in ECI:

1) Distribution: The distribution of all model-prompt pairs within ECI is depicted in Figure 9.76(b). With a median of  $51.4\%$  and a third quartile of  $54.9\%$ , the scenario is considered to have an easy understandability, as the median accuracy surpasses the random guess accuracy of  $50.0\%$ . Figure C.2 illustrates the distribution of all model-prompt pairs in each task respectively. In the ECI-B (CTB) task, with a median of  $50.6\%$ , a third quartile of  $54.6\%$ , and a random guess accuracy of  $50.0\%$ , the task is considered an easy understandability. In the ECI-B (ESC) task, given a median of  $51.6\%$ , a third quartile of  $56.1\%$ , and a random guess accuracy of  $50.0\%$ , the task is also classified to have an easy understandability. Similarly, as to the ECI-B (MAVEN-ERE) task, with a median of  $51.0\%$ , a third quartile of  $54.5\%$ , and a random guess accuracy of  $50.0\%$ , its understandability is categorized as easy. By analyzing the differences between tasks, it is observed that the median accuracy for individual tasks spans from  $50.6\%$  to  $51.6\%$ , with a standard deviation of 0.4. The accuracy at the third quartile extends from  $54.5\%$  to  $56.1\%$ , accompanied by a standard deviation of 0.7. Consequently, this scenario presents a minimally divergent variance of distribution.

2) Top Accuracy: As illustrated in Figure 9.79(a), the leading three models in terms of average accuracy are GPT-4 at  $65.6\%$ , text-davinci-003 at  $61.1\%$ , and Claude2 at  $58.4\%$ . The top model-prompt pair is GPT-4 with adversarial doubt, reaching an accuracy of  $67.0\%$ , indicating the scenario has a challenging solvability since the performance of the top model-prompt pair does not exceed  $80\%$ . Figure C.16 displays the three models with the highest average accuracy across individual tasks. For ECI-B (CTB), the highest average accuracies are achieved by GPT-4 at  $66.6\%$ , Claude2 at  $62.1\%$ , and text-davinci-003 at  $61.9\%$ . GPT-4, when combined with manual CoT, attains the highest accuracy of  $68.8\%$ , revealing the task solvability as challenging given the top model-prompt pair's performance falls below  $80\%$ . In the case of ECI-B (ESC), GPT-4 leads with  $68.4\%$ , followed by text-davinci-003 at  $63.0\%$ , and GPT-3.5-Turbo at  $59.2\%$ . The top model-prompt pair here is GPT-4 with adversarial doubt, reaching  $70.1\%$ , confirming the task's challenging solvability as the top model-prompt

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/bc12835855ff32138f1328aec2fc3f702d5f68809e589c90e4ba4adef45c9be3.jpg)



(a) Model performance of ECI


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/80700904e151099cd6ad15229c74decb2dd4a5c7a3c72d910ea701008403cb4c.jpg)



(b) Prompt gain of ECI



Figure 9.79 Heatmap of ECI. The models and prompts are sorted by their averages.


pair remains under  $80\%$ . Lastly, for ECI-B (MAVEN-ERE), the top accuracies are by GPT-4 at  $61.9\%$ , text-davinci-003 at  $58.6\%$ , and GPT-3.5-Turbo at  $55.8\%$ , with GPT-4 and adversarial ignore achieving the best at  $64.8\%$ . This outcome also categorizes the solvability of the task as challenging since the top model-prompt pair does not meet or exceed  $80\%$ . Through comparing different tasks, the variance of solvability across tasks appears negligible. Furthermore, the leading model exhibits an average accuracy fluctuating between  $61.9\%$  to  $68.4\%$ , a difference of  $6.5\%$ , while the highest accuracy observed in top model-prompt pairs varies from  $64.8\%$  to  $70.1\%$ , a  $5.3\%$  difference. Hence, the variance of model's top performance in the scenario is noticeable. Additionally, GPT-4 stands out as the leading model in terms of average performance and also forms the top model-prompt pairs in all tasks.

3) Stability: The three most stable models in the scenario, characterized by the lowest model volatility, are GPT-4 with a model volatility of 1.1, Baichuan2-chat (13B) with 1.6, and Qwen (7B) with 2.1. Conversely, the models exhibiting the greatest instability, shown by the highest model volatility, include InternLM-chat (20B) with model volatility of 23.6, text-babbage-001 at 11.3, and Llama2 (7B) at 11.2, reflecting their pronounced sensitivity to prompt variations. Delving into stability on a task-by-task basis: For the ECI-B (CTB) task, the three models demonstrating the greatest stability, with the lowest model volatility, are GPT-4 at 1.2, Qwen (7B) at 1.9, and Baichuan2-chat (13B) at 2.0. In contrast, the models with the most significant instability, indicated by the largest model volatility, are InternLM-chat (20B) at 23.5, Llama2 (13B) at 12.6, and Llama2 (7B) at 12.5. In the ECI-B (ESC) task, the top stable models include GPT-4 with a model volatility of 1.1, Baichuan2-chat (13B) at 1.6, and GPT-3.5-Turbo at 2.5. The models showing the most instability are InternLM-chat (20B) at

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/91693ba56d47fbaf4a7dcf0cb5baadd4e5398ac27cae63395ed6a95494d45e4d.jpg)



Figure 9.80 Language comparison of ECI. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


24.2, Llama2-chat (70B) at 12.2, and Llama2 (70B) at 11.3. For the ECI-B (MAVEN-ERE) task, the models with the highest stability are Baichuan2-chat (13B) and Baichuan2-chat (7B), both at 1.5, followed by GPT-4 at 1.7. The most unstable models include InternLM-chat (20B) at 23.1, text-babbage-001 at 12.1, and Llama2 (70B) at 11.1. In conclusion, it can be seen that GPT-4 is the most stable model across all tasks, while the Baichuan2-chat (13B) is the least stable one.

4) Open-Limited Ratio: Among the top five models with the highest average accuracy, a 0:5 ratio of open-access to limited-access models indicates a large open-limited gap.

Then, we conduct prompt gain analysis in ECI:

1) Top Gain: As shown in Figure 9.79(b), the leading two prompts achieving the greatest average accuracy improvements over the basic prompt are 1-shot IcL with a gain of  $3.1\%$  and 3-shot IcL with  $2.1\%$ . The largest increase in accuracy compared to the basic prompt is seen in Wizardcoder (15B) utilizing 3-shot IcL, with a remarkable gain of  $15.8\%$ . A comprehensive task-specific analysis follows. Figure C.17 illustrates the heatmap of accuracy gains for all tasks within the scenario. For the ECI-B (CTB) task, the two top-performing prompts in terms of average accuracy gain over the basic prompt are 1-shot IcL at  $3.6\%$  and 3-shot IcL at  $2.1\%$ . The highest accuracy enhancement from the basic prompt is achieved by Wizardcoder (15B) using manual CoT, with a gain of  $16.3\%$ . In the ECI-B (ESC) task, the prompts leading to the highest average accuracy gains compared to the basic prompt are 1-shot IcL at  $2.8\%$  and 3-shot IcL at  $2.2\%$ . The most substantial improvement over the basic prompt is by text-ada-001 with 1-shot IcL, showing a gain of  $15.2\%$ . For the ECI-B (MAVEN-ERE) task, the two prompts with the greatest average accuracy gains over the basic prompt are 1-shot IcL at  $3.0\%$  and 3-shot IcL at  $2.0\%$ . The most significant accuracy increase from the basic prompt is observed with Wizardcoder (15B) using 3-shot IcL, with an increase of  $18.0\%$ . In summary, 1-shot IcL and 3-shot IcL is the most effective prompt in all tasks. However, IcL generally has a more passive impact on the top 5 LLMs, as their lowest performance often originates from IcL. The two types of adversarial prompts and 0-shot CoT, negatively affect most LLMs, whereas EF and manual CoT have approximately equal positive and

negative effects.

2) Exceptions: In ECI, the most effective prompt shows exceptions in failing to improve the model performance over basic prompt in Llama2-chat (70B), text-davinci-001, Baichuan2-chat (13B and 7B), GPT-3.5-Turbo, Claude2, text-davinci-003, and GPT-4. All prompts enhance text-davinci-002's performance beyond the basic prompt. However, no prompt boosts the performance of Llama2-chat (70B) or Baichuan2-chat (7B) over the accuracy of basic prompt. In the ECI-B (CTB) task, the leading prompt does not enhance the performance of Baichuan2-chat (13B and 7B), GPT-3.5-Turbo, text-davinci-003, or GPT-4 beyond their performance with the basic prompt. Every prompt conducts improvements for text-davinci-001 and text-davinci-002 over the basic prompt, while none can elevate Baichuan2-chat (7B)'s performance in this task. For the ECI-B (ESC) task, the optimal prompt fails to lift the accuracy of Llama2-chat (70B), text-davinci-001, InternLM-chat (7B), Baichuan2-chat (13B and 7B), Claude2, GPT-3.5-Turbo, text-davinci-003, and GPT-4 beyond their accuracy with the basic prompt. Every prompt, however, can lift text-davinci-002's performance above the basic prompt, with none managing to improve the performance for Llama2-chat (70B) or Baichuan2-chat (7B) in this specific task. In the ECI-B (MAVEN-ERE) task, the best prompt proves ineffective for Baichuan1-chat (13B), Llama2 (70B) and Llama2-chat (70B), text-davinci-001, Baichuan2-chat (13B), Claude2, Baichuan2-chat (7B), GPT-3.5-Turbo, text-davinci-003, and GPT-4 in surpassing their performance on basic prompt. Nevertheless, all prompts are capable of enhancing text-davinci-002's performance beyond the basic prompt. Yet, no prompt is able to augment performance for Baichuan1-chat (13B), Llama2-chat (70B), Claude2, or Baichuan2-chat (7B) in this task. By evaluating the three tasks, we find that the best prompt 1-shot IcL cannot create positive average prompt gain in Baichuan2-chat (13B), Baichuan2-chat (7B), GPT-3.5-Turbo, text-davinci-003, and GPT-4 in any task. All prompts in all tasks have a positive average prompt gain on text-davinci-002, while no prompts in any tasks have a positive average prompt gain on Baichuan2-chat (7B).

3) Stability: As to the stability, the top 2 stable prompts with the smallest prompt volatility are 1-shot IcL with a prompt volatility of 5.5 and EF with a prompt volatility of 6.4. In contrast, the top 2 most unstable prompts with the largest prompt volatility are manual CoT at 12.5 and 3-shot IcL at 11.6. The average model-prompt-gain volatility (AMPGV) is 7.6, showing that the scenario has a medium prompt dependence. Next, we consider the stability task by task. For task ECI-B (CTB), the top 2 stable prompts with the smallest prompt volatility are 1-shot IcL with a prompt volatility of 5.3 and adversarial ignore with a prompt volatility of 6.5. In contrast, the top 2 most unstable prompts with the largest prompt volatility are manual CoT at 15.1 and 0-shot CoT at 11.7. The AMPGV is 8.3, showing that the task's prompt dependence is medium. For task ECI-B (ESC), the top 2 stable prompts with the smallest prompt volatility are 1-shot IcL with an prompt volatility of 6.1 and EF with an prompt volatility of 6.2. On the other hand, the top 2 most unstable prompts with the largest prompt volatility are manual CoT at 12.3 and 3-shot IcL at 12.3. The AMPGV is 7.7, showing that the task has a medium prompt dependence. For task ECI-B (MAVEN-ERE), the top 2 stable prompts with the smallest prompt volatility are 1-shot IcL at 5.8 and adversarial doubtat 6.3. The top 2 most unstable prompts are 3-shot IcL at 11.9 and manual CoT at 11.8. The AMPGV is 7.4, indicating that the task's prompt dependence is medium. After evaluation of all the tasks in the scenario, it is found that the AMPGV ranges from 7.4 to 8.3. Therefore, the scenario has a narrow variance of prompt dependence. In all tasks, 1-shot IcL is the top 1 stable prompt. On the other hand, manual CoT is the relatively least stable one.

Lastly, we assess language proficiency in ECI:

1) English vs. Chinese: According to Figure 9.80, models tend to exhibit superior performance on the English test set compared to the Chinese one. Specifically, 19 out of 28 models showed enhanced performance in English over Chinese.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/51da74becef6f8aa5995a934c30c883dbdcdf58b43a52168a804305077bf01b6.jpg)



(a) Model performance of AR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8f17ef9fafed91598333794ae1d6f0ae174cb105a3f524843fe900bd347adf6a.jpg)



(b) Prompt gain of AR



Figure 9.81 Heatmap of AR. The models and prompts are sorted by their averages.


2) Accuracy Difference: There is a significant performance gap between English and Chinese, with a preference for English in models like ada (0.35B)  $(21.4\%)$ , text-ada-001  $(18.4\%)$ , and text-babbage-001  $(15.7\%)$ . On the other hand, some models, including Wizardcoder (15B)  $(12.8\%)$ , Baichuan1-chat (13B)  $(11.9\%)$ , and Llama2 (7B)  $(4.8\%)$ , demonstrate a higher proficiency for Chinese than for English. This indicates that models primarily trained in English are capable of achieving noteworthy performance in Chinese as well, highlighting their cross-linguistic generalizability.

Abstract reasoning. Regarding model performance in AR: 1) Distribution: Figure 9.76(c) displays the distribution of all model-prompt pairs within AR, noting a median accuracy of  $53.1\%$  and a third quartile of  $62.6\%$ . This scenario is classified to have an easy understandability given that the median accuracy surpasses the random guess benchmark of  $50.0\%$ . 2) Top Accuracy: Figure 9.81(a) reveals the top three models by average accuracy: GPT-4 at  $88.3\%$ , Claude2 at  $75.9\%$ , and text-davinci-003 at  $74.5\%$ . GPT-4, employing manual CoT, stands out as the top model-prompt pair with a  $92.6\%$  accuracy. The solvability of the scenario is well-solved with each of the top three models' average accuracies exceeding  $70\%$ . 3) Stability: After computing the model volatility introduced in Section 6.3, we find the most prompt-sensitive, thus unstable models are Llama2-chat (70B) at 21.6, Llama2 (70B) at 21.1, and Llama2 (7B) at 17.0. Conversely, the most stable models include GPT-4 at 2.0, Qwen (7B) at 2.3, and InternLM-chat (20B) at 2.6. 4) Open-Limited Ratio: The ratio of open-access to limited-access models among the top five models with the highest average accuracy is 1:4, suggesting a moderate open-limited gap.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cd827a162f9cc695aca2a85a63317372e865b27625e5183ddad6c4084be5ec09.jpg)



Figure 9.82 Language comparison of AR. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


Regarding prompt gain in AR: 1) Top Gain: As shown in Figure 9.81(b), the leading two prompts by average accuracy gain over the basic prompt are 0-shot IcL and 1-shot IcL, both at  $1.5\%$ . Llama2 (70B) using 0-shot IcL exhibits the most significant gain of  $30.1\%$ . 2) Exceptions: The high-performing prompt, 0-shot IcL, proves effective with most models, but fails to generate positive performance over some models such as babbage (1.3B) and GPT-3.5-Turbo. Furthermore, no prompt is capable of creating positive average prompt gain for InternLM-chat (7B) and GPT-3.5-Turbo. 3) Stability: Regarding stability, the most stable prompts are 0-shot CoT with an prompt volatility of 6.4 and EF with an prompt volatility of 8.1, while the most unstable prompts are manual CoT at 17.1 and 3-shot IcL at 14.3. The scenario shows a medium prompt dependence, evidenced by an average model-prompt-gain volatility (AMPGV) of 9.7.

In terms of language proficiency in AR: 1) English vs. Chinese: Figure 9.82 indicates models perform better on the English test set over the Chinese set, with 17 of 28 models favoring English. 2) Accuracy Difference: Significant performance gaps favoring English are seen in text-ada-001 (34.9%), babbage (1.3B) (26.3%), and text-davinci-002 (20.9%). In contrast, models like Baichuan1-chat (13B), Llama2 (70B), and Baichuan2-chat (7B) demonstrate higher proficiency in Chinese.

# Causal attribution. Initially, we delve into model performance in CA:

1) Distribution: As depicted in Figure 9.76(d), the distribution for all model-prompt pairs in CA shows a median accuracy of  $55.9\%$  and a third quartile of  $61.8\%$ . This indicates that the scenario has an easy understandability, given that the median accuracy surpasses the random guess benchmark of  $50.0\%$ . Figure C.3 further outlines the distribution of all the model-prompt pairs for each specific causal task. In the CA-B (FA) task, with a median accuracy of  $63.2\%$  and a third quartile of  $72.4\%$ , exceeding the random guess threshold of  $50.0\%$ , this task is classified to have an easy understandability. Similarly, the CA-B (FP) task, with a median of  $50.6\%$  and a third quartile of  $56.3\%$ , also surpasses the random guess mark, causing its understandability classification as easy. By analyzing the differences between tasks, we observe that the median accuracy for each task varies from  $50.6\%$  to  $63.2\%$ , with a standard deviation of 6.3. Regarding the accuracy at the third quartile, it spans from

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/edaf811a050bb7687abb950b5413aa8d135ff0d06aadd3105193c624a5b0cee9.jpg)



(a) Model performance of CA


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/28a2a23d061345684bb32cd9e3e4343f03b3ee9c3934dacd73fdc86c8882c05d.jpg)



(b) Prompt gain of CA



Figure 9.83 Heatmap of CA. The models and prompts are sorted by their averages.


56.3% to 72.4%, with a standard deviation of 8.1. Hence, this scenario has a moderately distinct variance of distribution. Moreover, CA-B (FA) is easier to understand than CA-B (FP).

2) Top Accuracy: As illustrated in Figure 9.83(a), GPT-4 leads with an average accuracy of  $91.8\%$ , followed by text-davinci-003 at  $77.1\%$ , and Claude2 at  $74.0\%$ . GPT-4, when paired with manual CoT, achieves an impressive  $94.8\%$ . The solvability of this scenario is well-solved given that the top three models all have average accuracies over  $70\%$ . Figure C.18 further demonstrates the top models' average accuracy for each task. In the CA-B (FA) task, GPT-4 dominates with  $91.2\%$ , with GPT-3.5-Turbo at  $74.8\%$  and text-davinci-002 closely behind at  $74.3\%$ . GPT-4's manual CoT combination tops at  $93.6\%$ . The above results show the well-solved solvability as all top-three models exceed an average accuracy of  $70\%$ . For the CA-B (FP) task, GPT-4 again leads at  $92.5\%$ , with text-davinci-003 at  $80.1\%$  and Claude2 at  $78.5\%$ . The top model-prompt pair, achieved by GPT-4 with manual CoT, is  $95.9\%$ . The solvability of the task is well-solved as all leading models surpass the  $70\%$  accuracy threshold. Through comparing different tasks, we find that the variance of solvability across tasks is negligible. Additionally, the highest average accuracy for the top-1 model is between  $91.2\%$  and  $92.5\%$ , a variance of 1.3, while the peak accuracy for top model-prompt pairs lies between  $93.6\%$  and  $95.9\%$ , marking a 2.3 difference. Thus, the variance of model's top performance of the scenario is small. Moreover, GPT-4 is consistently found to be the superior model in average performance and forms part of the top model-prompt pairs across all tasks. Manual CoT forms the other part of the top model-prompt pairs across all tasks.

3) Stability: The three most stable models, characterized by the lowest model volatility, are GPT-4 with a model

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c491ba084fe0b2696f619cca369e04e0c5923fbd0d02299aeb617ca798f62368.jpg)



Figure 9.84 Language comparison of CA. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


volatility of 1.4, davinci (175B) at 2.4, and GPT-3.5-Turbo at 3.0, showcasing their robustness across various prompts. Conversely, the models demonstrating the greatest variability, with the highest model volatility, are Llama2-chat (70B) at 20.5, Llama2 (70B) at 13.6, and Llama2 (7B) at 11.6, highlighting their significant sensitivity to prompt variations. A further analysis of stability by individual tasks is as follows: In the CA-B (FA) task, the models with the least variability are GPT-4 at a model volatility of 1.1, GPT-3.5-Turbo at 3.3, and text-davinci-002 at 3.5. On the flip side, the most variable models, showing the largest model volatility, include Llama2-chat (70B) at 25.6, Llama2 (70B) at 18.9, and babbage (1.3B) at 15.1. For the CA-B (FP) task, the models exhibiting the greatest stability are Qwen (7B) and GPT-4, both at 2.0, followed closely by Wizardcoder (15B) at 2.2. Meanwhile, the models with the most variability are Llama2-chat (70B) at 15.9, Llama2 (7B) at 10.7, and text-davinci-002 at 9.9. Comparing across tasks, GPT-4 demonstrates great stability while Llama2-chat (70B) consistently exhibits considerable instability across different tasks, marking it as highly sensitive to the prompts used.

4) Open-Limited Ratio: The top 5 models with the highest average accuracy in the scenario exhibit a 0:5 open-access to limited-access model ratio, highlighting a large open-limited gap.

Then, we analyze prompt gain in CA:

1) Top Gain: As depicted in Figure 9.83(b), the two prompts with the highest average accuracy gain over the basic prompt are 1-shot IcL at  $1.0\%$  and 0-shot IcL at  $0.8\%$ . The most significant accuracy improvement over the basic prompt is seen with Llama2 (7B) using EF, showing an increase of  $27.3\%$ . Following this, we conduct a detailed task-by-task analysis. Figure C.19 displays the heatmaps of gains for all tasks in the scenario. For the task CA-B (FA), the top 2 prompts with the highest average accuracy gain over the basic prompt are 0-shot IcL at  $1.9\%$  and 1-shot IcL at  $1.5\%$ . The most significant accuracy improvement over the basic prompt is seen with Wizardcoder (15B) using manual CoT, showing an increase of  $40.6\%$ . For task CA-B (FP), the top 2 prompts with the highest average accuracy gain over the basic prompt are 1-shot IcL at  $0.5\%$  and manual CoT at  $0.4\%$ . The most significant accuracy improvement over the basic prompt is seen with Llama2 (13B) using

manual CoT, showing an increase of  $18.0\%$ . After evaluating the two tasks, it appears that the scenario favors 1-shot IcL and manual CoT the most.

2) Exceptions: In CA, the most effective prompt fails to create positive average prompt gain in Baichuan1-chat (13B), Wizardcoder (15B), Llama2-chat (70B), text-davinci-001, Baichuan2-chat (13B), Baichuan1 (7B), Koala (13B), davinci (175B), text-curie-001, InternLM-chat (20B), GPT-3.5-Turbo, Claude2, text-davinci-003, and GPT-4. Notably, Baichuan1-chat (13B) and GPT-3.5-Turbo see no positive average prompt gain from any prompt. In the CA-B (FA) task, the most effective prompt 0-shot IcL fails with Baichuan1-chat (13B), Baichuan2-chat (13B), text-babbage-001, ada (0.35B), Koala (13B), Claude2, and GPT-4 in generating positive average prompt gain, whereas all prompts manage to lift Llama2 (7B)'s performance. Within the CA-B (FP) task, the leading prompt 1-shot IcL does not give positive average prompt gain to Baichuan1-chat (13B), Vicuna-v1.3 (33B), Llama2-chat (70B), text-davinci-001, InternLM-chat (7B), Qwen (7B), Baichuan2-chat (13B), Wizardcoder (15B), Baichuan2-chat (7B), GPT-3.5-Turbo, text-davinci-002, Claude2, text-davinci-003, and GPT-4. Additionally, Baichuan1-chat (13B), Llama2-chat (70B), Qwen (7B), and Baichuan2-chat (7B) do not benefit from any prompt in this task. It can be seen that across both tasks, it is challenging to achieve any improvement for Baichuan1-chat (13B) with any prompt.

3) Stability: Regarding stability, the two most stable prompts, identified by the lowest prompt volatility, are 0-shot CoT with a prompt volatility of 6.2 and 0-shot IcL with a prompt volatility of 6.9. On the opposite end, the prompts showing the most variability, indicated by the highest prompt volatility, are manual CoT at 11.5 and 3-shot IcL at 10.3. The average model-prompt-gain volatility (AMPGV) stands at 7.2, thus the prompt dependence in this scenario is medium. Moving to a task-specific analysis: For the CA-B (FA) task, the two most stable prompts, based on the smallest prompt volatility, are 0-shot CoT at 9.0 and 0-shot IcL at 9.8. Conversely, the least stable prompts, marked by the largest prompt volatility, are 3-shot IcL at 19.5 and manual CoT at 18.9. The AMPGV is 11.0, highlighting a high prompt dependence for this task. For the CA-B (FP) task, the most stable prompts are 0-shot CoT with a prompt volatility of 5.7 and 0-shot IcL with a prompt volatility of 6.9, while the most variable prompts are adversarial ignore and 3-shot IcL, both at 9.9. The AMPGV is 6.5, suggesting a medium level of prompt dependence. After evaluation of all the tasks in the scenario, it has been determined that the AMPGV, which reflect variance of prompt dependence in the scenario, exhibit a narrow spectrum ranging from 6.5 to 11.0. Moreover, 0-shot CoT and 0-shot IcL demonstrate stability in both tasks, whereas 3-shot IcL and manual CoT are the least stable prompts in the two tasks, which is the same as the conclusion in the scenario aspect.

Finally, we measure language proficiency of CA:

1) English vs. Chinese: Figure 9.84 underscores that models generally exhibit superior performance on the English test set compared to the Chinese one, with 16 out of 28 models demonstrating better results in English.

2) Accuracy Difference: There are significant differences in performance favoring English, as seen in models such as text-davinci-001 (Difference of  $10.5\%$ ), GPT-3.5-Turbo  $(9.4\%)$ , and Llama2 (70B)  $(7.0\%)$ . On the flip side, some models, including Baichuan1-chat (13B)  $(26.5\%)$ , Llama2 (13B)  $(23.6\%)$ , and Vicuna-v1.3 (33B)  $(22.8\%)$ , perform better in Chinese.

Moreover, regarding CA-B (FA) task, it can be observed that the accuracy of “ $72.4\%$ ” appears frequently in this task, which is due to the “Yes:No” ratio of the dataset being 72.4:27.6. All accuracies of “ $72.4\%$ ” are results of answering “Yes” to all questions, and conversely, accuracies of “ $27.6\%$ ” are from answering “No” to all. This is why the overall performance of models on this task seems better. However, it could be described as a

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b54104aeb15d8aff48b072b01440d0155220c9fa8a023cd4178463a107359950.jpg)



(a) Distribution of EAE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/329502422948ad4ea20a1d803b1521916ae660c1a7f2c5f4150caefa5d6b24f1.jpg)



(b) Distribution of correlation



Figure 9.85 Distribution of association. The horizontal coordinate represents the accuracy of the model, and the vertical coordinate represents the percentage distribution corresponding to a certain accuracy interval.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/27b611b62b54bdf87d04f60286a838a6de05ab97b4e027ae3b388572a4b170a4.jpg)



(a) Model performance of EAE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/14f903194c0ebb6835a3e88d72dde5dce52836a5a266a64659b254bbdd7373a3.jpg)



(b) Prompt gain of EAE



Figure 9.86 Heatmap of EAE. The models and prompts are sorted by their averages.


"false prosperity", as whether the models truly understand and are capable of solving this problem remains questionable. As to the CA-B (FP) task, we find that over  $65\%$  of the responses from text-davinci-003 and GPT-3.5-Turbo are "Yes". The order of answers in the examples provided by 3-shot IcL is "No-Yes-No", leading us to speculate whether these two models are attempting to learn such a pattern, thus tending to output "Yes" more in the fourth question.

# 9.4.2 Association

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9d269b1a5769be6970dad02fce43b11a555ea3964f25729a19a0537b94d35c2b.jpg)



Figure 9.87 Language comparison of EAE. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


Explaining away effect. Regarding model performance in EAE: 1) Distribution: Figure 9.85(a) illustrates the distribution for all model-prompt pairs within the EAE, noting a median of  $48.8\%$  and a third quartile of  $50.7\%$ . This suggests that the understandability of the scenario is hard, with the median accuracy falling below the random guess benchmark of  $50.0\%$ . 2) Top Accuracy: Figure 9.86(a) identifies GPT-4 at  $67.9\%$ , Claude2 at  $66.7\%$ , and text-davinci-003 at  $57.0\%$  as the top three models by average accuracy. As to the top model-prompt pair, GPT-4, through the use of manual CoT, achieves a remarkable  $90.5\%$ , indicating the solvability of the scenario is potentially solvable as the top model-prompt pair's performance surpasses  $80\%$ . 3) Stability: The models which are most sensitive to prompt variations, as indicated by the model volatility described in Section 6.3, are Llama2 (70B) at 18.8, Llama2 (13B) at 17.0, and Llama2 (7B) at 17.0. Conversely, the most stable models include Qwen (7B) at 2.1, davinci (175B) at 3.1, and Baichuan1 (7B) at 3.3. 4) Open-Limited Ratio: Among the top five models with the highest average accuracy, there is a large open-limited gap between open-access and limited-access models, with a ratio of 0:5.

Regarding prompt gain in EAE: 1) Top Gain: Figure 9.86(b) shows the top two prompts for average accuracy gain over the basic prompt as 3-shot IcL at  $5.5\%$  and 1-shot IcL at  $3.9\%$ , with ada (0.35B) using 3-shot IcL witnessing the most substantial improvement of  $27.2\%$ . 2) Exceptions: The top-performing prompt, 3-shot IcL, cannot give a positive average prompt gain to several models, including Llama2-chat (70B), Baichuan2-chat (13B), and GPT-4. On the other hand, all prompts are capable of enhancing text-curie-001's performance above the basic prompt. 3) Stability: The most stable prompts, with the lowest prompt volatility, are adversarial ignore at 4.5 and adversarial doubt at 4.8, while the least stable prompts are manual CoT at 22.8 and EF at 11.1. The average model-prompt-gain volatility (AMPGV) is 9.8, demonstrating a medium prompt dependence within the scenario.

In terms of language proficiency in EAE: 1) English vs. Chinese: Figure 9.87 reveals models perform better on the English test set over the Chinese set, with 18 of 28 models favoring English. 2) Accuracy Difference: Significant performance differences favoring English are seen in models like text-babbage-001 (38.3%), Claude2 (29.0%), and ada (0.35B) (28.7%). Conversely, models such as Vicuna-v1.3 (33B), Baichuan1-chat (13B), and

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2f70c10bb153b8482a3bf8650bf9ff40bbd9787256342e6ad656f7103324cf11.jpg)



(a) Model performance of CORR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5b44d1e4b0834958ce9abb4ef726f2417fa54e83601272d0daf96ef103a8c42b.jpg)



(b) Prompt gain of CORR



Figure 9.88 Heatmap of CORR. The models and prompts are sorted by their averages.


Baichuan2-chat (7B) demonstrate higher proficiency in Chinese.

Correlation. In terms of model performance in CORR: 1) Distribution: Figure 9.85(b) shows the distribution for all model-prompt pairs in CORR, indicating a median of  $49.9\%$  and a third quartile of  $51.5\%$ . This indicates that the understandability of the scenario is hard, as the median accuracy falls below the random guess benchmark of  $50.0\%$ . 2) Top Accuracy: According to Figure 9.88(a), the leading three models by average accuracy are GPT-4 at  $59.1\%$ , text-davinci-003 at  $54.7\%$ , and text-davinci-002 at  $54.3\%$ . Claude2, using EF, stands out with a top score of  $68.0\%$ , illustrating the scenario solvability as challenging since the top model-prompt pair's performance does not reach  $80\%$ . 3) Stability: The models most affected by prompt variability, as shown by the model volatility described in Section 6.3, are InternLM-chat (20B) at 17.4, ada (0.35B) at 14.7, and text-ada-001 at 14.1. Conversely, the most stable models include Baichuan1 (7B) at 0.5, Qwen (7B) at 1.2, and text-davinci-001 at 1.9. 4) Open-Limited Ratio: Among the top five models with the highest average accuracy, which have a 0.5 ratio of open-access to limited-access models, there exists a large open-limited gap.

In terms of prompt gain in CORR: 1) Top Gain: Figure 9.88(b) highlights the top two prompts for average accuracy gain over the basic prompt as 3-shot IcL at  $6.2\%$  and 1-shot IcL at  $5.7\%$ . Baichuan1-chat (13B) using 1-shot IcL demonstrates the most significant increase of  $31.8\%$ . 2) Exceptions: The most effective prompt, 3-shot IcL, does not generate a positive average prompt gain for several models, including Baichuan2-chat (13B) and Claude2. Yet, all prompts manage to enhance the performance for models like Baichuan1-chat (13B)

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ab5530917689acbb4327f157eab8a5ceb8c87a09477f673dc95540af7e82842d.jpg)



Figure 9.89 Language comparison of CORR. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


and text-davinci-002 over the basic prompt. 3) Stability: The most stable prompts, with the lowest prompt volatility, are 0-shot IcL at 6.7 and adversarial ignore at 7.7. The least stable prompts, with the highest prompt volatility, are manual CoT at 15.3 and EF at 11.1. The average model-prompt-gain volatility (AMPGV) is 7.3, indicating a medium prompt dependence in this scenario.

Regarding language proficiency in CORR: 1) English vs. Chinese: Figure 9.89 reveals that models generally achieve better results on the English test set than on the Chinese set, with 15 of 28 models favoring English. 2) Accuracy Difference: Significant advantages for English over Chinese are seen in models like ada (0.35B) at  $27.1\%$  and Claude2 at  $21.6\%$ . In contrast, models like Baichuan2-chat (7B) and Llama2 (7B) exhibit higher proficiency in Chinese.

# 9.4.3 Intervention

Average treatment effect. First, we delve into model performance in ATE:

1) Distribution: Figure 9.90(a) showcases the distribution of model-prompt pairs for the ATE. With a median value of  $9.4\%$  and a third quartile at  $28.6\%$ , this scenario appears to have a hard understandability, given that the median accuracy falls below the random guess accuracy of  $16.7\%$ . Figure C.4 displays the distribution for each specific causal task. In the ATE-P (ATE-basic) task, the median is  $2.2\%$ , and the third quartile is  $13.4\%$ . Due to the lower than  $15\%$  third quartile score and the challenging nature of Mathematical-mode tasks, we regard the task understandability as very hard. The ATE-P (ATE-hard) task shows a median of  $2.2\%$  and a third quartile of  $10.7\%$ . Similarly, we define the task understandability as very hard. Moreover, the ATE-B (ATE-natural) task presents a median of  $22.2\%$  and a third quartile of  $50.4\%$ , with a random guess accuracy of  $50.0\%$ , making this task understandability as hard. By analyzing the differences between tasks, we observe that median accuracies vary from  $2.2\%$  to  $22.2\%$  with a standard deviation of 9.4. The third quartile accuracies range from  $10.7\%$  to  $50.4\%$ , accompanied by a standard deviation of 18.1, indicating that the scenario has a noticeably diverse variance of distribution. The ATE-B (ATE-natural) task exhibits significantly higher median and third

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ddb3029b27789c0951fcdf26ecb337c141e94eff5fab65f695922160ad944d42.jpg)



(a) Distribution of ATE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0ab80606a058ee9e4d5532217208538b65bb272b27652b4a66743089ae537ce2.jpg)



(b) Distribution of CDE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d8b448bf3110e959a54862012c3e5965a55d44b69181bb5e1c1694c1aff7ed12.jpg)



(c) Distribution of CEI


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4063dc98648cb6c116165b95bf703ad7b0bd3fd2e5eb672298807740558bde2c.jpg)



(d) Distribution of BAS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0ffd5de0ef3f9c5b2da684422c21f3cecc4fe0fff2ffe30bba4f769b0785b4cf.jpg)



(e) Distribution of FAS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9adbf0e1a7b3e84db90cb7f2588a4ce4107ccbd4b5312953d52dd4bb3a82790c.jpg)



(f) Distribution of IV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d0b1e614d1c988c7123ef2e555b13642e3d827aa8810402ec1879083ae4912a8.jpg)



(g) Distribution of CB



Figure 9.90 Distribution of intervention. The horizontal coordinate represents the accuracy of the model and the vertical coordinate represents the percentage distribution corresponding to a certain accuracy interval.


quartile figures than the two Mathematical-mode tasks (ATE-P (ATE-hard) and ATE-P (ATE-basic)). Both the two Mathematical-mode tasks' distributions have the majority of model-prompt pairs (over  $60\%$  ) in a  $0\%$  to  $20\%$  accuracy range, in stark contrast to the distinctly different distribution for the ATE-B (ATE-natural) task.

2) Top Accuracy: Figure 9.91(a) reveals that, the leading models in terms of average accuracy for this scenario are GPT-4 at  $54.8\%$ , text-davinci-003 at  $50.3\%$ , and GPT-3.5-Turbo at  $47.7\%$ . The top model-prompt pair is GPT-4 with manual CoT, reaching an impressive  $92.8\%$ , indicating the scenario's solvability is potentially solvable given that the top model-prompt pair exceeds an  $80\%$  performance mark. Figure C.20 details the top three models' average accuracy, analyzed task by task. In the ATE-P (ATE-basic) task, the highest average accuracies are observed with GPT-4 at  $43.4\%$ , text-davinci-003 at  $43.0\%$ , and GPT-3.5-Turbo at  $42.3\%$ , with Llama2 (70B) and manual CoT leading at  $92.3\%$ , showcasing the task's solvability as potentially solvable as the top model-prompt pair scores above  $80\%$ . For ATE-P (ATE-hard), GPT-4 leads with  $50.2\%$ , followed by text-davinci-003 at  $46.2\%$ , and GPT-3.5-Turbo at  $41.9\%$ , where GPT-4 and manual CoT top at  $89.1\%$ , affirming the task's solvability as potentially solvable with the top model-prompt pair also exceeding  $80\%$ . In ATE-B (ATE-natural), the top averages belong to GPT-4 at  $67.5\%$ , Claude2 at  $65.1\%$ , and text-davinci-003 at  $58.8\%$ , with GPT-4 and manual CoT achieving the highest at  $98.8\%$ , further confirming the solvability of the task is potentially solvable as the top model-prompt pair surpasses  $80\%$ . Through comparing different tasks, the variance of solvability appears negligible. Yet, the top model's average accuracy spans from  $43.4\%$  to  $67.5\%$  (a  $24.1\%$  difference), and the peak accuracy for top model-prompt pairs varies from  $89.1\%$  to  $98.8\%$  (a  $9.7\%$  difference), indicating a significant variance of model's top performance across the scenario. Notably, GPT-4 consistently excels in average performance across all tasks and is a part of the top model-prompt pair in two out of three tasks. Manual CoT is part of the top model-prompt pairs in all tasks.

3) Stability: The three most stable models, indicated by the lowest model volatility, are Baichuan1-chat (13B) at 2.4, Baichuan2-chat (13B) at 3.0, and InternLM-chat (20B) at 6.4. Conversely, the three models exhibiting

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/869b2375689c4f40dfad73c9c24e3a50f6b75a70e561a3a3cc5373e36a2f160a.jpg)



(a) Model performance of ATE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/07160aaa741f3c380e9facb533a9a57736660c78428fce994d5486aa56f0a93f.jpg)



(b) Prompt gain of ATE



Figure 9.91 Heatmap of ATE. The models and prompts are sorted by their averages.


the greatest instability across various prompts, shown by the highest model volatility, are Llama2 (13B) at 34.8, Llama2 (70B) at 30.2, and Llama2 (7B) at 28.4. Next, we analyze stability on a task-specific basis. In the ATE-P (ATE-basic) task, the most stable models are babbage (1.3B) at 0.1, Baichuan1 (7B) at 1.0, and ada (0.35B) at 1.4. The most unstable models, with the largest model volatility, are Llama2 (13B) at 30.6, Llama2 (70B) at 30.4, and Llama2 (7B) at 24.2. In the ATE-P (ATE-hard) task, the three most stable models are babbage (1.3B) at 0.0, davinci (175B) at 0.1, and ada (0.35B) at 0.8. The models with the highest model volatility, indicating instability across prompts, are Llama2 (13B) at 35.6, GPT-4 at 31.8, and Llama2 (7B) at 30.4. In the ATE-B (ATE-natural) task, the top stable models are Baichuan1-chat (13B) at 2.8, Baichuan2-chat (13B) at 4.6, and InternLM-chat (20B) at 12.2. The most unstable models are Llama2 (13B) at 35.1, Llama2 (7B) at 33.2, and Llama2 (70B) at 32.4. In all tasks, Llama2 (13B) and Llama2 (7B) rank among the top three most unstable models, highlighting their prompt sensitivity in this scenario. Notably, GPT-4 is found to be as the second most unstable model in the ATE-P (ATE-hard) task, pointing to an anomaly in this otherwise high-performing model.

4) Open-Limited Ratio: The 0:5 ratio of open-access to limited-access models among the top 5 models in the entire scenario underscores a large open-limited gap.

Next, we delve into prompt gain in ATE:

1) Top Gain: As illustrated in Figure 9.91(b), the two prompts leading in average accuracy gain relative to the basic prompt are 3-shot IcL at  $25.0\%$  and manual CoT at  $22.4\%$ . The most significant improvement in accuracy compared to the basic prompt is seen with Llama2 (13B) using manual CoT, achieving an  $86.2\%$  increase. We

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4455de0e47b98ad465bbe726abe239ef26cfbf8d2e8074d24a9183be825db99e.jpg)



Figure 9.92 Language comparison of ATE. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


then proceed with an in-depth task-specific analysis. Figure C.21 displays the gain heatmaps for every task within the scenario. In the ATE-P (ATE-basic) task, manual CoT at  $25.9\%$  and 3-shot IcL at  $16.4\%$  are the top two prompts by average accuracy gain over the basic prompt, with Llama2 (70B) and manual CoT marking the most substantial improvement at  $91.7\%$ . In the ATE-P (ATE-hard) task, manual CoT at  $23.1\%$  and 3-shot IcL at  $15.7\%$  lead in average accuracy gains, with Llama2 (7B) and manual CoT showing the highest increase at  $86.3\%$ . In the ATE-B (ATE-natural) task, the two prompts with the greatest average accuracy gains are 3-shot IcL at  $42.9\%$  and manual CoT at  $18.1\%$ , with Llama2 (13B) and manual CoT demonstrating the most significant boost at  $91.2\%$ . On the evaluation across tasks, 3-shot IcL and manual CoT are consistently found to be the top two prompts by largest average gain in each task. Additionally, the most extensive gains across all model-prompt pairs are found in the llama-series utilizing manual CoT, with the highest accuracy gain surpassing  $90\%$ .

2) Exceptions: The leading prompt, 3-shot IcL, give positive average prompt gain to most models in the scenario, with exceptions being Baichuan1-chat (13B) and Claude2. Nevertheless, every prompt manages to elevate Llama2 (13B)'s performance. In the ATE-P (ATE-basic) task, the most effective prompt, manual CoT, does not work on Baichuan1-chat (13B) in generating positive average prompt gain. However, all prompts are capable of boosting Llama2-chat (70B)'s performance. Within the ATE-P (ATE-hard) task, manual CoT, despite being the top prompt, fails to create a positive average prompt gain for Baichuan1-chat (13B) and text-davinci-003. In the ATE-B (ATE-natural) task, the best prompt, 3-shot IcL, shows no effectiveness on Baichuan1-chat (13B), Baichuan2-chat (13B), and Claude2. Yet, every prompt succeeds in generating a positive average prompt gain on Llama2 (13B).

3) Stability: Regarding stability, the two most stable prompts are 0-shot CoT with a prompt volatility of 3.2 and adversarial doubt with a prompt volatility of 3.5. On the opposite end, the two prompts demonstrating the greatest volatility, indicated by the highest prompt volatility, are manual CoT at 26.5 and 3-shot IcL at 19.3. The average model-prompt-gain volatility (AMPGV) is 15.4, suggesting a high prompt dependence. We then assess stability across individual tasks. In the ATE-P (ATE-basic) task, 0-shot CoT with a prompt volatility

of 1.3 and adversarial ignore with a prompt volatility of 2.0 is the most stable, whereas manual CoT at 27.1 and 3-shot IcL at 19.3 is the least stable. The task has a high prompt dependence with an AMPGV of 12.6. For the ATE-P (ATE-hard) task, the most stable prompts are adversarial doubt and adversarial ignore, with prompt volatility of 2.9 and 3.1, respectively, while manual CoT and 3-shot IcL are the least stable, with prompt volatility of 27.8 and 23.5. The task shows a high prompt dependence, as reflected by AMPGV of 14.1. In the ATE-B (ATE-natural) task, adversarial ignore and adversarial doubt both present the lowest volatility with prompt volatility of 8.2, in stark contrast to 3-shot IcL and manual CoT, which are the most unstable with prompt volatility of 30.1 and 28.9, respectively. The task results in a high prompt dependence, with an AMPGV of 21.4. After evaluating all tasks in the scenario, it is observed that the distribution of AMPGV, which highlights the variance of prompt dependence, have a moderate spread from 12.6 to 21.4. Differing from the scenario view, adversarial ignore and adversarial doubt consistently rank as the most stable prompts on a task-by-task analysis. While 3-shot IcL and manual CoT rank highest in prompt gain, they also exhibit the most instability across all tasks.

At last, we analyze language proficiency in ATE:

1) English vs. Chinese: Figure 9.92 underscores that models generally exhibit superior performance on the English test set compared to the Chinese one, with 25 out of 28 models demonstrating better results in English.

2) Accuracy Difference: Significant performance gaps between English and Chinese, with a preference for English, appears in models such as GPT-3.5-Turbo (33.4%), text-davinci-002 (23.5%), and GPT-4 (21.1%). On the other hand, models like Baichuan1-chat (13B) (7.8%), and babbage (1.3B) (3.0%) exhibit a higher proficiency in Chinese.

Controlled direct effect. First, we delve into model performance in CDE:

1) Distribution: Figure 9.90(b) showcases the distribution of all model-prompt pairs in the CDE scenario. With a median of  $9.3\%$  and a third quartile of  $24.7\%$ , this scenario appears to have a hard understandability since the median accuracy falls below the random guess benchmark of  $16.7\%$ . Figure C.5 illustrates the model-prompt pair distribution for each specific task. In the CDE-P (CDE-basic) task, with a median of  $1.6\%$ , a third quartile of  $9.1\%$  which is lower than  $15\%$ , this Mathematical-mode task is considered to have a very hard understandability. The CDE-P (CDE-hard) task presents a median of  $2.7\%$  and a third quartile of  $11.4\%$  and is considered to have a very hard understandability, as indicated by the low values in both the third quartile and the median scores. Additionally, the CDE-B (CDE-natural) task, with a median of  $25.0\%$ , a third quartile of  $44.8\%$ , and a random guess accuracy of  $50.0\%$ , is also categorized to have a very hard understandability. By analyzing the differences between tasks, we observe that the median accuracies vary from  $1.6\%$  to  $25.0\%$  with a standard deviation of 10.8. The third quartile accuracies span from  $9.1\%$  to  $44.8\%$  with a standard deviation of 16.3. Therefore, the scenario has a highly divergent variance of distribution. Additionally, the Natural-mode task scores higher in both the median and third quartile compared to the two mathematics-focused tasks (CDE-P (CDE-basic) and CDE-P (CDE-hard)), with CDE-P (CDE-hard) outperforming CDE-P (CDE-basic) in these metrics. The distribution for the Mathematical-mode tasks shows a majority of model-prompt pairs (over  $70\%$ ) falling within a  $0\%$  to  $10\%$  accuracy range, suggesting a challenging landscape for most models. Conversely, the Natural-mode task features a more balanced distribution, with no 10-point (e.g.,  $0\%$  to  $10\%$ ,  $10\%$  to  $20\%$ ) accuracy range that encompasses over  $30\%$  of all model-prompt pairs.

2) Top Accuracy: As seen in Figure 9.93(a), the leading models in terms of average accuracy for this scenario

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d1220a95920dcf11c5175ee281bb0f8970f0f6f58df7fa67e95d9bb95c30032e.jpg)



(a) Model performance of CDE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/30f825f24445d4969696eae94d4896aa3c2a06416059db8ab5e6054dfde6b947.jpg)



(b) Prompt gain of CDE



Figure 9.93 Heatmap of CDE. The models and prompts are sorted by their averages.


are GPT-3.5-Turbo at  $47.6\%$ , GPT-4 at  $41.9\%$ , and Claude2 at  $34.5\%$ . The top model-prompt pair, GPT-4 with manual CoT, reaches a high of  $90.8\%$ , suggesting the scenario's solvability as potentially solvable given the top model-prompt pair surpasses an  $80\%$  performance mark. Figure C.22 shows the top three models' average accuracy, assessed on an individual task basis. In the CDE-P (CDE-basic) task, the models leading in average accuracy are GPT-3.5-Turbo at  $37.6\%$ , Claude2 at  $29.9\%$ , and GPT-4 at  $28.0\%$ , with GPT-4 and manual CoT forming the top model-prompt pair at  $87.8\%$ , indicating the task's solvability as potentially solvable as the top model-prompt pair performance exceeds  $80\%$ . For the CDE-P (CDE-hard) task, the top models by average accuracy are GPT-3.5-Turbo at  $45.4\%$ , GPT-4 at  $33.0\%$ , and text-davinci-003 at  $27.0\%$ , where GPT-4 and manual CoT achieve  $86.7\%$ , again highlighting the solvability of the task is potentially solvable. In the CDE-B (CDE-natural) task, the best models in average accuracy are GPT-4 at  $61.1\%$ , GPT-3.5-Turbo at  $57.2\%$ , and Claude2 at  $51.7\%$ , with GPT-4 and manual CoT reaching  $97.9\%$ , underscoring the task solvability as potentially solvable. Through comparing different tasks, the variance of solvability between tasks appears negligible. Yet, the top model's average accuracy spans from  $37.6\%$  to  $61.1\%$  (a  $23.5\%$  difference), and the peak accuracy for top model-prompt pairs ranges from  $86.7\%$  to  $97.9\%$  (an  $11.2\%$  difference), marking a extremely significant variance of model's top performance. The Mathematical-mode tasks display lower top accuracies than the Natural-mode task. Regarding top models, GPT-3.5-Turbo leads in the Mathematical-mode tasks, while GPT-4 excels in the Natural-mode task. Across all tasks, GPT-3.5-Turbo and GPT-4 consistently rank within the top three for average model performance. Moreover, GPT-4 paired with manual CoT are found to be the top model-prompt pair across all tasks.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/53dc5fbd50073420baa7cbac8c3791028b680861db2712a7fc75911bea9d5b40.jpg)



Figure 9.94 Language comparison of CDE. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


3) Stability: The three models exhibiting the greatest stability with the lowest model volatility are Baichuan1-chat (13B) at 2.7, babbage (1.3B) at 2.8, and ada (0.35B) at 3.6. Conversely, the three models showing the highest levels of instability across various prompts are Llama2 (70B) at 27.8, Llama2 (13B) at 26.7, and Llama2 (7B) at 25.7. We proceed to examine stability on a task-specific basis. In the CDE-P (CDE-basic) task, the most stable models are davinci (175B) at 0.1, text-ada-001 at 0.2, and ada (0.35B) at 0.2. In contrast, the most unstable models are Llama2 (70B) at 28.2, GPT-4 at 25.3, and Llama2 (13B) at 22.5. In the CDE-P (CDE-hard) task, the top three most stable models are curie (6.7B) at 0.8, ada (0.35B) at 1.8, and babbage (1.3B) at 2.4. Meanwhile, the models with the highest model volatilites, indicating the greatest instability, are GPT-4 at 33.7, Llama2 (7B) at 30.2, and Llama2 (13B) at 28.5. In the CDE-B (CDE-natural) task, the models demonstrating the most stability are Baichuan1-chat (13B) at 3.1, davinci (175B) at 7.7, and babbage (1.3B) at 7.9. On the flip side, the models with the most instability are Llama2 (70B) at 28.4, Llama2 (13B) at 28.0, and Baichuan2-chat (7B) at 25.8. In all tasks, Llama2 (13B) consistently appears among the top three most unstable models, underscoring its high sensitivity to prompts in this scenario. Additionally, GPT-4 and Llama2 (70B) are identified as the two most unstable models in the Mathematical-mode tasks.

4) Open-Limited Ratio: The ratio of open-access to limited-access models among the top five models with the highest average accuracy in the scenario is 1:4, indicating a moderate open-limited gap.

Next, we delve into prompt gain in CDE:

1) Top Gain: As shown in Figure 9.93(b), the two prompts leading in average accuracy gain over the basic prompt are 3-shot IcL at  $21.7\%$  and manual CoT at  $20.9\%$ . The largest improvement in accuracy compared to the basic prompt is noted with Llama2 (7B) using manual CoT, which registers a  $66.9\%$  increase. A more granular, task-specific analysis follows. Figure C.23 illustrates the gains across all tasks in the scenario. In the CDE-P (CDE-basic) task, manual CoT at  $21.0\%$  and 3-shot IcL at  $13.3\%$  top the list for average accuracy gain over the basic prompt, with GPT-4 and manual CoT marking the greatest increase at  $69.2\%$ . In the CDE-P (CDE-hard) task, 3-shot IcL at  $26.3\%$  and manual CoT at  $20.9\%$  are the most effective, with Llama2

(7B) and manual CoT achieving the most substantial boost at  $78.3\%$ . In the CDE-B (CDE-natural) task, the highest gains are with 3-shot IcL at  $25.5\%$  and manual CoT at  $20.8\%$ , and the top improvement is seen with Llama2 (13B) using 3-shot IcL, which increases by  $76.6\%$ . For every individual task, 3-shot IcL and manual CoT stand out as the two most effective prompts, underscoring their consistent impact across the scenario. Moreover, model-prompt pairs that utilize these specific prompts achieve the greatest increases in performance relative to other model-prompt pairs.

2) Exceptions: The highly effective prompt, 3-shot IcL, does not generate a positive average prompt gain in Baichuan1-chat (13B), text-davinci-003, and Claude2. However, all prompts manage to enhance the performance of text-curie-001 and text-davinci-001 beyond the basic prompt. In the CDE-P (CDE-basic) task, the leading prompt, manual CoT, fails to yield a positive average prompt gain on Baichuan1-chat (13B) and Claude2. Within the CDE-P (CDE-hard) task, the top 1 average prompt, 3-shot IcL, shows no effectiveness on Baichuan1-chat (13B) and Claude2. Furthermore, no prompt is able to boost Claude2's performance above the basic prompt level. In the CDE-B (CDE-natural) task, the best prompt, 3-shot IcL, also falls short with Baichuan1-chat (13B), text-davinci-003, and Claude2. All prompts succeed in elevating the performance of text-curie-001 and text-davinci-001 over the basic prompt. In all tasks, Claude2, ranking as the fourth highest model on average, is significantly negatively impacted by the top average prompt, 3-shot IcL.

3) Stability: Regarding stability, the two most stable prompts, based on the lowest prompt volatility, are adversarial doubt at 3.3 and adversarial ignore at 3.8. Conversely, the two prompts showing the greatest variability, indicated by the highest prompt volatility, are manual CoT at 23.0 and 3-shot IcL at 22.0. The average model-prompt-gain volatility (AMPGV) is 14.1, illustrating a high prompt dependence. We then explore stability on an individual task basis. In the CDE-P (CDE-basic) task, the most stable prompts are 0-shot CoT with a prompt volatility of 1.4 and adversarial ignore with a prompt volatility of 1.8, while the least stable prompts are manual CoT at 23.4 and 3-shot IcL at 22.1. An AMPGV of 10.9 highlights a high prompt dependence. In the CDE-P (CDE-hard) task, adversarial doubt and adversarial ignore are the most stable with prompt volatility of 2.7 and 4.0, respectively. The least stable are manual CoT at 26.2 and 3-shot IcL at 25.8. The AMPGV is 16.0, underscoring a high prompt dependence. For the CDE-B (CDE-natural) task, the most stable prompts are adversarial doubt at 8.1 and 0-shot IcL at 8.7, while the most variable are 3-shot IcL at 27.9 and manual CoT at 25.7. As the AMPGV is 17.4, the task has a high prompt dependence. After evaluating all the tasks in the scenario, we find that the distribution of AMPGV ranges from 10.9 to 17.4, indicating a moderate spread variance of prompt dependence. Although 3-shot IcL and manual CoT are the most effective, they also rank as the most unstable across tasks, demonstrating that the impact of these prompts varies significantly across different models.

Lastly, we measure language proficiency in CDE:

1) English vs. Chinese: Illustrated by Figure 9.94, models generally exhibit superior performance on the English test set compared to the Chinese test set, with 24 out of 28 models achieving better results in English.

2) Accuracy Difference: Significant discrepancies in accuracy between English and Chinese, with a preference for English, appear in models such as GPT-3.5-Turbo (25.1%), GPT-4 (18.2%), and Llama2 (70B) (17.7%). On the other hand, models like Baichuan1-chat (13B) (9.0%), babbage (1.3B) (4.8%), and ada (0.35B) (3.4%) demonstrate higher accuracy in Chinese.

Causal effect identification. First, we examine model performance in CEI:

1) Distribution: Figure 9.90(c) displays the distribution of all model-prompt pairs within CEI. With a median

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/16cadf92ad2a5cc9d58e1ebd2f8a8b65c82fb1a3982658b2d2ea5bc667ee495f.jpg)



(a) Model performance of CEI


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1f7e0f9e3c2f5f554df7f598dde28707f2433643c9b64fc24969f63d66cc1d2c.jpg)



(b) Prompt gain of CEI



Figure 9.95 Heatmap of CEI. The models and prompts are sorted by their averages.


score of  $46.6\%$  and a third quartile of  $49.3\%$ , this scenario has a very hard understandability because the third quartile falls below the random guess threshold of  $50.0\%$ . Figure C.6 details the distribution for each specific task. In the CEI-B (0.2-UC) task, the median is  $47.6\%$ , and the third quartile is  $50.0\%$ . Due to the random guess accuracy of  $50.0\%$ , the task's understandability is hard. The CEI-B (0.4-UC) task shows a median of  $46.5\%$  and a third quartile of  $49.4\%$ , with a random guess accuracy of  $50.0\%$ , categorizing it to have a very hard understandability. For the CEI-B (0.6-UC) task, the median stands at 46.1 and the third quartile at  $48.9\%$ , with the random guess accuracy also at  $50.0\%$ , indicating the understandability of this task as very hard. Similarly, the CEI-B (0.8-UC) task presents a median of 46.1 and a third quartile of  $48.9\%$ , with a random guess accuracy of  $50.0\%$ , affirming its understandability as very hard. By analyzing the differences between tasks, we see a median accuracy range from  $46.1\%$  to  $47.6\%$  with a standard deviation of 0.6. The third quartile accuracy spans from  $48.9\%$  to  $50.0\%$  with a standard deviation of 0.5. As a result, the scenario has a minimally divergent variance of distribution. Sorting tasks by median and third quartile yield the same accuracy ranking: CEI-B  $(0.8\text{-UC}) = \text{CEI-B}(0.6\text{-UC}) < \text{CEI-B}(0.4\text{-UC}) < \text{CEI-B}(0.2\text{-UC})$ . Across all four tasks, more than  $70\%$  of the distribution lies within the 40 to 60 accuracy range.

2) Top Accuracy: Figure 9.95(a) reveals that the leading models in this scenario, based on average accuracy, are GPT-3.5-Turbo at  $49.9\%$ , text-curie-001 at  $49.6\%$ , and Baichuan1 (7B) at  $49.4\%$ . The top model-prompt pair, GPT-4 with 3-shot IcL, reaches  $59.0\%$ , indicating the solvability of the scenario as challenging due to the top model-prompt pair's performance falling short of  $80\%$ . Figure C.24 displays the top three models' average accuracy across individual tasks. In the CEI-B (0.2-UC) task, the highest average accuracies are seen with

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0603ec21d7a158b8c410c75b0669c50a1162821f093bf83f851f4a5733a6bf82.jpg)



Figure 9.96 Language comparison of CEI. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


GPT-3.5-Turbo at  $52.6\%$ , Baichuan1 (7B) at  $51.1\%$ , and text-curie-001 at  $50.7\%$ , where GPT-4 and 1-shot IcL lead with a  $60.1\%$  score, marking the task solvability as challenging since the top model-prompt pair does not exceed  $80\%$ . For the CEI-B (0.4-UC) task, GPT-3.5-Turbo at  $50.4\%$ , text-curie-001 at  $49.5\%$ , and Wizardcoder (15B) at  $49.5\%$  top the average accuracy, with GPT-4 and 3-shot IcL achieving  $59.2\%$ , again highlighting the task's challenging solvability. In the CEI-B (0.6-UC) task, the leading averages are by Wizardcoder (15B) at  $49.1\%$ , text-curie-001 at  $48.9\%$ , and Baichuan1 (7B) at  $48.8\%$ , with GPT-4 and 3-shot IcL reaching  $58.6\%$ , underlining the solvability of the task as challenging. For the CEI-B (0.8-UC) task, text-curie-001 at  $49.2\%$ , Wizardcoder (15B) at  $48.6\%$ , and Baichuan1 (7B) at  $48.6\%$  are the top models, with GPT-4 and 3-shot IcL achieving  $58.2\%$ , confirming the task's challenging solvability. Through comparing different tasks, the variance of solvability among the tasks is negligible. The top model's average accuracy fluctuates minimally from  $49.1\%$  to  $52.6\%$  (a  $3.5\%$  difference), and the accuracy among top model-prompt pairs varies from  $58.2\%$  to  $60.1\%$  (a  $1.9\%$  difference), signifying a small variance of model's top performance. Text-curie-001 consistently ranks within the top three models in all tasks. Moreover, Wizardcoder (15B) and Baichuan1 (7B) appear in the top 3 average models in three out of four tasks. Although GPT-4 doesn't rank among the top three in average model performance, when paired with 1-shot IcL or 3-shot IcL, it forms the top model-prompt pairs in all tasks.

3) Stability: The three most stable models, based on the lowest model volatility, are text-curie-001 at 0.9, text-davinci-001 at 1.0, and Qwen (7B) at 1.0. Conversely, the models demonstrating the highest levels of instability across various prompts are Llama2 (70B) at 18.1, Llama2-chat (70B) at 15.9, and GPT-4 at 12.9, showing a pronounced prompt sensitivity. We proceed to analyze stability on a task-specific basis. In the CEI-B (0.2-UC) task, the most stable models are Qwen (7B) at 0.5, text-curie-001 at 1.3, and text-davinci-001 at 1.8, while the most unstable models are Llama2 (70B) at 18.6, Llama2-chat (70B) at 16.3, and GPT-4 at 12.8. In the CEI-B (0.4-UC) task, the top stable models are text-curie-001 at 0.7, text-davinci-001 at 1.1, and Wizardcoder (15B) at 1.3, in contrast to the most unstable models, which are Llama2 (70B) at 18.2, Llama2-chat (70B) at 15.8, and GPT-4 at 13.4. For the CEI-B (0.6-UC) task, the leading models in stability are text-davinci-001 at 0.9, text-curie-001 at 1.0, and Qwen (7B) at 1.5. The models with the highest model volatility, indicating

instability, are Llama2 (70B) at 18.0, Llama2-chat (70B) at 15.9, and GPT-4 at 13.0. In the CEI-B (0.8-UC) task, the most stable models are text-davinci-001 at 0.9, text-curie-001 at 1.0, and Qwen (7B) at 1.4, while the most unstable models are Llama2 (70B) at 17.9, Llama2-chat (70B) at 15.9, and babbage (1.3B) at 13.0. In all tasks, text-curie-001 and text-davinci-001 consistently rank as the most stable models, whereas Llama2 (70B) and Llama2-chat (70B) consistently appear as the most unstable, underscoring their high sensitivity to prompt variations.

4) Open-Limited Ratio: With a ratio of 2 open-access models to 3 limited-access models among the top five models with the highest accuracy, the open-limited gap of the scenario is small.

Following, we delve into prompt gain in CEI:

1) Top Gain: As illustrated in Figure 9.95(b), the two prompts leading in average accuracy gain over the basic prompt are 1-shot IcL at  $6.6\%$  and 3-shot IcL at  $5.4\%$ . The most significant improvement in accuracy relative to the basic prompt is seen with Llama2 (70B) using 1-shot IcL, with a substantial increase of  $48.2\%$ . We then proceed to a granular analysis across individual tasks. Figure C.25 outlines the gains across all tasks in the scenario. In the CEI-B (0.2-UC) task, 1-shot IcL at  $5.9\%$  and 3-shot IcL at  $4.5\%$  offer the highest average accuracy gains over the basic prompt, with Llama2 (70B) and 1-shot IcL achieving a remarkable increase of  $48.7\%$ . For the CEI-B (0.4-UC) task, 1-shot IcL at  $6.8\%$  and 3-shot IcL at  $5.4\%$  stand out for average accuracy gains, with Llama2 (70B) and 1-shot IcL showing an impressive increase of  $48.9\%$ . In the CEI-B (0.6-UC) task, the leading gains are by 1-shot IcL at  $6.9\%$  and 3-shot IcL at  $5.8\%$ , with Llama2 (70B) and 1-shot IcL demonstrating a significant boost of  $47.4\%$ . For the CEI-B (0.8-UC) task, 1-shot IcL at  $6.7\%$  and 3-shot IcL at  $5.7\%$  provide the highest average accuracy gains, with Llama2 (70B) and 1-shot IcL showing an increase of  $47.7\%$ . On the evaluation across tasks, the pattern is consistent: 1-shot IcL is the top 1 model average prompt as well as the prompt that makes the largest gain accompanied by Llama2 (70B), surpassing other model-prompt pairs. 3-shot IcL ranks as the second most effective prompt in terms of average accuracy gain.

2) Exceptions: The highly effective prompt, 1-shot IcL, cannot create a positive average prompt gain with several models, including Baichuan1-chat (13B), Baichuan2-chat (13B), curie (6.7B), text-davinci-002, Baichuan1 (7B), and text-curie-001. However, all prompts are capable of enhancing the performance of Llama2 (70B), GPT-4, and text-davinci-001 beyond the basic prompt. Notably, curie (6.7B) and text-curie-001 see no improvement from any prompt over the basic prompt. In the CEI-B (0.2-UC) task, 1-shot IcL fails to be effective for a range of models including Baichuan1-chat (13B), babbage (1.3B), ada (0.35B), Baichuan2-chat (13B), InternLM-chat (20B), curie (6.7B), Qwen (7B), text-babbage-001, text-davinci-002, text-curie-001, and Baichuan1 (7B). Yet, all prompts boost the performance of Llama2 (70B) and GPT-4 above the basic prompt. Curie (6.7B) and Qwen (7B), however, do not benefit from any prompt in this task. For the CEI-B (0.4-UC) task, 1-shot IcL falls short with Baichuan1-chat (13B), Llama2 (13B), Baichuan2-chat (13B), curie (6.7B), text-davinci-002, Claude2, Baichuan1 (7B), and text-curie-001. Despite this, improvements are seen for Llama2 (70B) and GPT-4 with all prompts, while Llama2 (13B), curie (6.7B), Claude2, and text-curie-001 see no enhancement from any prompt. In the CEI-B (0.6-UC) task, the effectiveness of 1-shot IcL does not extend to Baichuan1-chat (13B), Baichuan2-chat (13B), text-davinci-002, curie (6.7B), Baichuan1 (7B), and text-curie-001. Conversely, Llama2 (70B) and GPT-4 performances are elevated by all prompts above the basic prompt, with curie (6.7B) again showing no improvement from any prompt. The CEI-B (0.8-UC) task mirrors this pattern, with 1-shot IcL not creating positive average prompt gain for several models including Baichuan1-chat (13B) and Llama2 (13B). Llama2 (70B) and GPT-4, however, see a positive average prompt gain from all prompts, contrasting with curie (6.7B), which does not improve with any prompts. By evaluating across the tasks, it turns out that all prompts can enhance Llama2 (70B), GPT-4, and text-davinci-001 beyond the basic prompt level across all

tasks. Conversely, Baichuan1-chat (13B), Llama2 (13B), and curie (6.7B) do not experience any benefit from any prompts in these tasks. Throughout all four tasks, the top prompt, 1-shot IcL, fails to yield improvements for Baichuan1-chat (13B), Baichuan2-chat (13B), curie (6.7B), and text-curie-001. Additionally, in every task, Llama2 (70B) and GPT-4's performance can be improved by any prompt over the basic prompt, while no prompt is able to enhance curie (6.7B)'s performance over the basic prompt in any task.

3) Stability: Regarding stability, the two most stable prompts, indicated by the smallest prompt volatility, are adversarial ignore at 5.1 and 0-shot IcL at 5.9. Conversely, the prompts exhibiting the greatest variability, evidenced by the largest prompt volatility, are manual CoT at 13.0 and 1-shot IcL at 12.4. The average model-prompt-gain volatility (AMPGV) is 6.2, illustrating a medium level of prompt dependence. Next, we conduct a task-specific stability analysis. In the CEI-B (0.2-UC) task, the most stable prompts are adversarial ignore with a prompt volatility of 4.9 and 0-shot IcL with a prompt volatility of 5.7, while the least stable are manual CoT at 13.0 and 1-shot IcL at 12.8. The AMPGV is 6.4, signifying the task has a medium prompt dependence. For the CEI-B (0.4-UC) task, the top stable prompts are adversarial ignore with a prompt volatility of 5.4 and 0-shot IcL with a prompt volatility of 6.1. The most unstable prompts, with the largest prompt volatility, are manual CoT at 12.9 and 1-shot IcL at 12.7. An AMPGV of 6.2 indicates a medium prompt dependence. In the CEI-B (0.6-UC) task, the most stable prompts feature adversarial ignore with a prompt volatility of 5.3 and adversarial doubt with a prompt volatility of 5.9, while the least stable prompts are manual CoT at 13.3 and 3-shot IcL at 12.1. The AMPGV is 6.4, showing a medium prompt dependence. For the CEI-B (0.8-UC) task, the top stable prompts are adversarial ignore at 5.2 and adversarial doubt at 5.9, in contrast to the most unstable prompts, manual CoT at 13.0 and 3-shot IcL at 12.5, with an AMPGV of 6.4, reflecting a medium prompt dependence. After evaluating all tasks in the scenario, the range of AMPGV is from 6.2 to 6.4, showing a narrow variance of prompt dependence. Adversarial ignore consistently shows the highest stability across all four tasks, while manual CoT ranks as the least stable in every task, aligning with the observations made from the scenario perspective.

Finally, we analyze language proficiency in CEI,

1) English vs. Chinese: Figure 9.96 illustrates that models tend to perform better on the English test set than on the Chinese test set, with 15 out of 28 models exhibiting superior performance in English.

2) Accuracy Difference: There are significant differences in accuracy between English and Chinese in text-ada-001 (8.0%), GPT-4 (6.0%), and text-babbage-001 (5.3%), with a preference for English. On the flip side, models like Vicuna-v1.3 (33B) (24.5%), Llama2-chat (70B) (23.1%), and Baichuan1-chat (13B) (16.7%) demonstrate higher accuracy in Chinese, indicating a stronger performance in that language.

# Backdoor adjustment set. First, we analyze model performance in BAS:

1) Distribution: Figure 9.90(d) showcases the distribution of all model-prompt pairs in the BAS. With a median of  $34.0\%$  and a third quartile of  $40.0\%$ , this scenario is viewed to have a hard understandability as the median accuracy falls below the scenario's average random guess of  $37.5\%$ . Figure C.7 shows the distribution of all model-prompt pairs task-by-task. In the BAS-B (backadj) task, the median is calculated at  $48.4\%$ , and the third quartile at  $50.4\%$ . As the random guess accuracy is  $50.0\%$ , the task has a hard understandability. For the BAS-C (max-BAS) task, the median stands at  $29.6\%$ , the third quartile at  $34.6\%$ , with the random guess accuracy at  $33.3\%$ , labeling the understandability of the task as hard to understand. The BAS-C (min-BAS) task presents a median of  $31.9\%$  and a third quartile of  $43.5\%$ , alongside with a random guess accuracy of  $33.3\%$ , indicating it to have a hard understandability. Similarly, the BAS-C (mix-BAS) task reveals a median of  $29.8\%$  and a third

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2a39da42aacd7b9b11e1f504d31298d33289881db7da4fdc2e7397ff5e9bc521.jpg)



(a) Model performance of BAS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9d8f0679213095f3702d4e875997b85f36f04bd1e690ea880ab32050d7b5dfad.jpg)



(b) Prompt gain of BAS



Figure 9.97 Heatmap of BAS. The models and prompts are sorted by their averages.


quartile of  $35.7\%$ . With the random guess accuracy at  $33.3\%$ , the task is hard to understand. By analyzing the differences between tasks, we find that the median accuracy range from  $29.6\%$  to  $48.4\%$  with a standard deviation of 7.8. The third quartile accuracy spans from  $34.6\%$  to  $50.4\%$  with a standard deviation of 6.4. The discovery shows that the scenario has a moderately distinct variance of distribution. Ranking tasks by median and third quartile reveals the same accuracy order of: BAS-C (max-BAS)  $<$  BAS-C (mix-BAS)  $<$  BAS-C (min-BAS)  $<$  BAS-B (backadj). The three symbolic tasks (BAS-C (max-BAS), BAS-C (mix-BAS), and BAS-C (min-BAS)) exhibit lower median and third quartile values than the Natural-mode task, BAS-B (backadj). Notably, in the BAS-B (backadj) task, over  $50\%$  of the distribution falls within a  $40\%$  to  $50\%$  accuracy range, while the three symbolic tasks feature a more balanced distribution, without any  $10\%$  -width interval surpassing  $40\%$  of the distribution.

2) Top Accuracy: Figure 9.97(a) demonstrates that the leading models by average accuracy in this scenario are GPT-4 at  $71.6\%$ , text-davinci-003 at  $53.7\%$ , and GPT-3.5-Turbo at  $49.8\%$ . The top model-prompt pair, GPT-4 with 3-shot IcL, reaches  $75.1\%$ , indicating that the solvability of this scenario is challenging due to the top model-prompt pair's performance not exceeding  $80\%$ . Figure C.26 details the top three models' average accuracy across different tasks. In the BAS-B (backadj) task, the highest average accuracies are for GPT-4 at  $51.2\%$ , babbage (1.3B) at  $50.0\%$ , and davinci (175B) at  $50.0\%$ , with Llama2 (70B) and 3-shot IcL leading at  $68.5\%$ , marking the solvability of the task as challenging with the top model-prompt pair performance below  $80\%$ . For the BAS-C (max-BAS) task, the top models are GPT-4 at  $74.4\%$ , text-davinci-003 at  $48.4\%$ , and GPT-3.5-Turbo at  $48.4\%$ , where GPT-4 and manual CoT achieve  $83.0\%$ . This task's solvability is solvable with the top model's

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d95438818c0dc83e80f4c53f7182f0feab07593ce6dba5fd76c0020c914c9bee.jpg)



Figure 9.98 Language comparison of BAs. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


average accuracy over  $70\%$ . The BAS-C (min-BAS) task shows GPT-4 at  $82.3\%$ , text-davinci-003 at  $69.1\%$ , and text-davinci-002 at  $59.5\%$  as the leading models, with GPT-4 and 3-shot IcL reaching  $86.1\%$ . The above analysis confirms the task's solvable solvability with the top model's average accuracy of over  $70\%$ . For the BAS-C (mix-BAS) task, the top models by average accuracy are GPT-4 at  $78.4\%$ , text-davinci-003 at  $53.3\%$ , and GPT-3.5-Turbo at  $48.5\%$ , with GPT-4 and 3-shot IcL achieving  $84.0\%$ . As the top model's average accuracy is over  $70\%$ , this task has a solvable solvability. Through comparing different tasks, the variance of solvability shows a moderate range. The top model's average accuracy varies from  $51.2\%$  to  $82.3\%$  (a  $31.1\%$  difference), and the accuracy among top model-prompt pairs spans from  $68.5\%$  to  $86.1\%$  (a  $17.6\%$  difference), highlighting a extremely significant variance of model's top performance. The top average accuracy and peak accuracy across the tasks reveal a pattern opposite to the model's distribution: the three symbolic tasks are easier to solve than the Natural-mode task, BAS-B (backadj). Notably, GPT-4 excels as the top model in average performance and also presents the top model-prompt pairs across all tasks.

3) Stability: The three most consistent models, based on the lowest model volatility, are text-davinci-001 at 1.4, text-curie-001 at 2.3, and GPT-4 at 2.6. In contrast, the models exhibiting the greatest variability, marked by the highest model volatility across different prompts, are Llama2 (70B) at 16.2, Vicuna-v1.3 (33B) at 11.9, and Llama2 (13B) at 11.8, highlighting their pronounced sensitivity to prompts. We further explore stability for each task individually. In the BAS-B (backadj) task, the most stable models are cabbage (1.3B) at 1.6, Qwen (7B) at 2.2, and davinci (175B) at 2.8, whereas the most unstable models are Wizardcoder (15B) at 17.0, Vicuna-v1.3 (33B) at 14.0, and Llama2 (70B) at 10.9. For the BAS-C (max-BAS) task, the models with the lowest model volatility are text-davinci-001 at 2.4, text-babbage-001 at 2.6, and InternLM-chat (20B) at 4.3. The most unstable models feature Llama2 (70B) at 18.1, Llama2 (13B) at 15.4, and cabbage (1.3B) at 15.1. In the BAS-C (min-BAS) task, the top three stable models are GPT-4 at 2.2, text-babbage-001 at 2.4, and text-davinci-001 at 2.7. The least stable models are Llama2 (70B) at 23.7, Llama2-chat (70B) at 18.3, and Llama2 (13B) at 15.6. For the BAS-C (mix-BAS) task, the most consistent models are text-babbage-001 at 1.4, InternLM-chat (20B) at 3.5, and text-ada-001 at 3.9. The models with the greatest variability are Llama2

(70B) at 17.0, curie (6.7B) at 16.3, and ada (0.35B) at 15.1. When comparing across tasks, babbage (1.3B), while being the most stable in the BAS-B (backadj), appears among the top three most unstable in the BAS-C (max-BAS) task. Text-babbage-001 ranks among the top three most stable models in all symbolic tasks, while Llama2 (70B) features as one of the top three most unstable models across all four tasks.

4) Open-Limited Ratio: The ratio of open-access to limited-access models among the top five models with the highest average accuracy being 0.5 highlights a large open-limited gap of the scenario.

Next, we delve into prompt gain in BAS:

1) Top Gain: As illustrated in Figure 9.97(b), the two prompts that lead to the highest average accuracy gains over the basic prompt are 3-shot IcL with a  $12.1\%$  gain and 1-shot IcL with a  $9.8\%$  gain. The most significant increase in accuracy compared to the basic prompt is achieved by Llama2 (70B) using 3-shot IcL, with a  $39.5\%$  increase. We continue with a detailed, task-specific analysis. Figure C.27 displays the gains across all tasks within the scenario. In the BAS-B (backadj) task, 3-shot IcL at  $7.0\%$  and 1-shot IcL at  $6.2\%$  are the top two prompts for average accuracy gain over the basic prompt, with Wizardcoder (15B) and 1-shot IcL showing the most substantial increase at  $37.9\%$ . In the BAS-C (max-BAS) task, 3-shot IcL at  $12.3\%$  and 1-shot IcL at  $11.0\%$  lead in average accuracy gains, with Llama2 (70B) and 3-shot IcL achieving the highest increase at  $40.4\%$ . In the BAS-C (min-BAS) task, the top gains come from 3-shot IcL at  $15.3\%$  and 1-shot IcL at  $11.1\%$ , with Llama2 (70B) and 3-shot IcL marking the most significant increase of  $56.8\%$ . For the BAS-C (mix-BAS) task, the highest gains are noted with 3-shot IcL at  $13.7\%$  and 1-shot IcL at  $11.0\%$ , with Llama2 (70B) and 3-shot IcL showing the highest increase of  $41.9\%$ . Upon evaluating across tasks, a consistent trend emerges: 3-shot IcL stands out as the top 1 performing prompt in terms of average gain, particularly when paired with Llama2 (70B) or Wizardcoder (15B), outperforming other model-prompt pairs. 1-shot IcL secures its place as the second most effective prompt for average accuracy improvement. Additionally, the choice-selection symbolic tasks (BAS-C (max-BAS), BAS-C (min-BAS), BAS-C (mix-BAS)) exhibit larger top gains compared to the Natural-mode task, indicating that IcL prompts significantly aid models in achieving better comprehension.

2) Exceptions: The highly effective prompt, 3-shot IcL, boosts the performance of most models in the scenario, but with exceptions including Baichuan1-chat (13B), Baichuan2-chat (7B), text-davinci-001, text-curie-001, and InternLM-chat (20B). All prompts are capable of enhancing the performance of Wizardcoder (15B) and text-davinci-002 beyond the basic prompt=. However, none of the prompts manage to improve the performance of text-davinci-001 and InternLM-chat (20B) above the basic prompt. In the BAS-B (backadj) task, 3-shot IcL does not work well on Baichuan1-chat (13B), Llama2 (7B), InternLM-chat (20B), Baichuan1 (7B), Baichuan2-chat (7B), text-davinci-001, Qwen (7B), and Llama2 (13B). All prompts create a positive average prompt gain for Wizardcoder (15B) and text-davinci-002. However, Baichuan2-chat (7B) and Qwen (7B) see no performance gain from any prompt. For the BAS-C (max-BAS) task, 3-shot IcL fails to create a positive average prompt gain with certain models, including Baichuan1-chat (13B), InternLM-chat (7B), text-babbage-001, text-davinci-001, InternLM-chat (20B), and GPT-4, while all prompts boost davinci (175B)'s performance over the basic prompt. Text-babbage-001, however, does not benefit from any prompt. In the BAS-C (min-BAS) task, 3-shot IcL is ineffective with Baichuan1-chat (13B), Baichuan2-chat (7B), text-babbage-001, text-curie-001, InternLM-chat (20B), and Claude2. All prompts help improve Wizardcoder (15B) and text-davinci-002 over their performance on basic prompt. InternLM-chat (20B) and Claude2 do not receive any improvement from prompts. The BAS-C (mix-BAS) task shows that the top performing prompt, 3-shot IcL, do not give positive average prompt gain to Baichuan1-chat (13B), Baichuan2-chat (7B), text-ada-001, text-davinci-001, InternLM-chat (7B), InternLM-chat (20B), and text-curie-001. Moreover, no

prompt is capable of improving InternLM-chat (20B)'s performance above the basic prompt. Across all tasks, 3-shot IcL does not manage to enhance performance for Baichuan1-chat (13B) and InternLM-chat (20B) over their basic prompt performance, indicating its limitations with these models.

3) Stability: Regarding stability within the scenario, the two most stable prompts are EF with a prompt volatility of 3.6 and adversarial ignore with a prompt volatility of 4.4. Conversely, the most variable prompts, indicated by the highest prompt volatility, are 3-shot IcL at 11.4 and 1-shot IcL at 10.3. An average model-prompt-gain volatility (AMPGV) of 7.6, illustrating a medium level of prompt dependence across the scenario. Stability is further assessed on a task-specific basis. In the BAS-B (backadj) task, the most stable prompts are EF at 7.4 prompt volatility and adversarial doubt at 7.6 prompt volatility, while the least stable are 3-shot IcL at 10.4 prompt volatility and 0-shot CoT at 10.1 prompt volatility. The task shows a medium prompt dependence with an average model-prompt-gain volatility (AMPGV) of 6.6. For the BAS-C (max-BAS) task, EF and adversarial ignore stand out as the most stable with prompt volatility of 4.0 and 5.1, respectively, and the least stable prompts are manual CoT at 14.1 and 1-shot IcL at 13.2. The task reflects a medium prompt dependence with an AMPGV of 9.8. In the BAS-C (min-BAS) task, the top stable prompts are adversarial ignore at 5.3 prompt volatility and adversarial doubt at 6.5 prompt volatility, whereas the most unstable are 3-shot IcL at 16.1 and 1-shot IcL at 15.4. This task also shows a medium level of prompt dependence with an AMPGV of 9.8. The BAS-C (mix-BAS) task reveals EF and adversarial ignore as the most stable prompts with prompt volatility of 4.3 and 4.8, respectively. The least stable prompts are 3-shot IcL at 14.2 and 1-shot IcL at 13.8, indicating a medium prompt dependence with an AMPGV of 9.4. After reviewing all tasks, the AMPGV spans a range from 6.6 to 9.8, reflecting the narrow variance of prompt dependence. The Natural-mode task (BAS-B (backadj)) demonstrates more stability to prompts compared to the symbolic tasks.

Finally, we analyze language proficiency in BAS:

1) English vs. Chinese: Figure 9.98 shows that models generally perform better on the English test set over the Chinese one, with 24 out of 28 models favoring English.

2) Accuracy Difference: Significant differences in accuracy between English and Chinese, with a preference for English, are noted in models like GPT-3.5-Turbo (English better than Chinese with an average of  $15.6\%$ ), ada (0.35B)  $(13.1\%)$ , and text-ada-001  $(12.2\%)$ . In contrast, models such as Baichuan1-chat (13B)  $(6.1\%)$ , InternLM-chat (20B)  $(3.1\%)$ , and curie (6.7B)  $(1.8\%)$  are more proficient in Chinese.

Frontdoor adjustment set. Regarding model performance in FAS: 1) Distribution: Figure 9.90(e) displays the distribution for all model-prompt pairs within the FAS, noting a median of  $29.0\%$  and a third quartile of  $35.5\%$ . This scenario is considered to have a hard understandability since the median accuracy falls below the random guess benchmark of  $33.3\%$ . 2) Top Accuracy: Figure 9.99(a) reveals the leading three models by average accuracy: GPT-4 at  $77.2\%$ , text-davinci-003 at  $59.9\%$ , and GPT-3.5-Turbo at  $54.0\%$ . GPT-4, employing 3-shot IcL, is the top model-prompt pair with a  $95.2\%$  accuracy. With the top model's average accuracy surpassing  $70\%$ , the solvability of this scenario is solvable. 3) Stability: The most prompt-sensitive models, indicated by the model volatility described in Section 6.3, are text-davinci-002 at 18.4, Claude2 at 17.1, and text-davinci-003 at 14.9. In contrast, the most stable models include davinci (175B) at 1.8, text-curie-001 at 3.4, and Baichuan2-chat (13B) at 3.5. 4) Open-Limited Ratio: With a 1:4 ratio of open-access to limited-access models among the top five models with the highest average accuracy, the open-limited gap is moderate.

Regarding prompt performance in FAS: 1) Top Gain: Figure 9.99(b) identifies the top two prompts for average accuracy gain over the basic prompt as 3-shot IcL at  $13.3\%$  and 1-shot IcL at  $10.6\%$ , with text-davinci-002 using

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a68e47ea804da36d890464005719ca639cb885651b2ebe797de91f1d64fd55b5.jpg)



(a) Model performance of FAS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/780042e6a155eae4742d5d715736a996e1ccd6b35551d821278c493fcf845f0c.jpg)



(b) Prompt gain of FAS



Figure 9.99 Heatmap of FAS. The models and prompts are sorted by their averages.


3-shot IcL showcasing the most significant improvement of  $52.3\%$ . 2) Exceptions: The highest-performing prompt, 3-shot IcL, does not give positive average prompt gains to several models, including Baichuan2-chat (13B) and Claude2. Nonetheless, all prompts are capable of boosting the performance of Llama2-chat (70B), Qwen (14B), and text-davinci-002 over the basic prompt. 3) Stability: The most stable prompts, maintaining the lowest prompt volatility, are adversarial ignore at 5.2 and adversarial doubt at 6.1. Meanwhile, the least stable prompts, with the highest prompt volatility, are 3-shot IcL at 16.6 and manual CoT at 16.2. As the computed average model-prompt-gain volatility (AMPGV) is 9.8. Therefore, the scenario has a medium prompt dependence.

Regarding language proficiency in FAS: 1) English vs. Chinese: Figure 9.100 shows models generally perform better on the English test set compared to the Chinese set, with 17 of 28 models favoring English. 2) Accuracy Difference: Significant advantages for English over Chinese are seen in models like GPT-3.5-Turbo (17.3%) and ada (0.35B) (8.5%). Conversely, models like curie (6.7B) and Claude2 demonstrate a higher proficiency in Chinese.

Instrumental variable. Regarding model performance in IV: 1) Distribution: Figure 9.90(f) showcases the distribution for all model-prompt pairs within IV, revealing a median of  $30.7\%$  and a third quartile of  $37.9\%$ . This indicates the understandability of the scenario is hard as the median accuracy falls below the random guess benchmark of  $33.3\%$ . 2) Top Accuracy: According to Figure 9.101(a), the leading three models by average accuracy are GPT-4 at  $74.8\%$ , text-davinci-003 at  $56.5\%$ , and text-davinci-002 at  $53.7\%$ . GPT-4,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/299372e0914e4817cb37c2276b7ae30ee73c8c162861b463a214f7d77ab73ab4.jpg)



Figure 9.100 Language comparison of FAS. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


employing 3-shot IcL, achieves a top score of  $78.9\%$ , suggesting the solvability of this scenario as challenging since the top model-prompt pair's performance doesn't reach  $80\%$ . 3) Stability: The models most susceptible to prompt variations, as shown by the model volatility discussed in Section 6.3, are Vicuna-v1.3 (33B) at 16.7, Ada (0.35B) at 15.9, and Llama2 (13B) at 15.1. Conversely, the most stable models include text-curie-001 at 0.5, GPT-4 at 3.0, and InternLM-chat (20B) at 3.3. 4) Open-Limited Ratio: With a 0:5 ratio of open-access to limited-access models among the top five models with the highest average accuracy, this indicates a large open-limited gap in the scenario.

In terms of prompt gain in IV: 1) Top Gain: Figure 9.101(b) highlights the top two prompts for average accuracy gain over the basic prompt as manual CoT at  $15.2\%$  and 3-shot IcL at  $13.2\%$ . Ada (0.35B), using 3-shot IcL, showcases the most significant improvement of  $39.7\%$ . 2) Exceptions: The highest-performing prompt, manual CoT, is not effective in generating positive average prompt gain in specific models including text-babbage-001 and text-ada-001. However, all prompts manage to enhance the performance of Baichuan2-chat (13B), Baichuan1 (7B), and text-davinci-002 over the basic prompt, with text-ada-001 being the exception where no prompt leads to improvement. 3) Stability: The most stable prompts, exhibiting the lowest prompt volatility, are adversarial ignore at 5.1 and adversarial doubt at 5.5. The least stable prompts, with the largest prompt volatility, are manual CoT at 14.0 and 3-shot IcL at 13.9. The computed average model-prompt-gain volatility (AMPGV) of 9.3 indicates a medium prompt dependence in this scenario.

In terms of language proficiency in IV: 1) English vs. Chinese: Figure 9.102 shows that models in IV perform better on the English test set than on the Chinese set, with 20 of 28 models favoring English. 2) Accuracy Difference: Significant advantages for English over Chinese are seen in models like GPT-3.5-Turbo (14.9%) and GPT-4 (14.0%). In contrast, models such as curie (6.7B) and davinci (175B) exhibit higher proficiency in Chinese.

**Collision bias.** Regarding model performance in CB: 1) Distribution: Figure 9.85(g) showcases the distribution for all model-prompt pairs within CB, noting a median of  $43.0\%$  and a third quartile of  $50.6\%$ . This

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ceb540e5429de25aa5a3fbfc24ac8537b9653b8f9ff15b125b1924235669ba99.jpg)



(a) Model performance of IV


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d31c153ba76b55c2e92c137d1b5fbf784762270e07861f11f4f483652e74c634.jpg)



(b) Prompt gain of IV



Figure 9.101 Heatmap of IV. The models and prompts are sorted by their averages.


indicates the understandability of the scenario is hard since the median accuracy falls below the random guess benchmark of  $50.0\%$ . 2) Top Accuracy: Figure 9.103(a) reveals the top three models by average accuracy are GPT-4 at  $62.7\%$ , text-davinci-003 at  $53.2\%$ , and text-davinci-002 at  $53.0\%$ . The top model-prompt pair is GPT-4 with manual CoT, which achieves an impressive  $97.8\%$ , suggesting the solvability of this scenario as potentially solvable. 3) Stability: The models most sensitive to prompt variations, as shown by the model volatility described in Section 6.3, are Llama2 (70B) at 20.9, Koala (13B) at 16.8, and GPT-4 at 16.2. Conversely, the most stable models are text-curie-001 at 2.6, curie (6.7B) at 4.3, and Wizardcoder (15B) at 4.9. 5) Open-Limited Ratio: A 2:3 ratio of open-access to limited-access models among the top five models indicates a small open-limited gap.

In terms of prompt gain in CB: 1) Top Gain: Figure 9.103(b) identifies the top two prompts for average accuracy gain over the basic prompt as manual CoT at  $15.5\%$  and 3-shot IcL at  $13.7\%$ . The greatest improvement over the basic prompt is noted with GPT-3.5-Turbo using 3-shot IcL, marking a gain of  $45.7\%$ . 2) Exceptions: Manual CoT, the highest-performing prompt, does not create a positive average prompt gain for certain models, including InternLM-chat (20B), InternLM-chat (7B), Vicuna-v1.3 (33B), Claude2, and curie (6.7B). Yet, all prompts manage to enhance the performance of text-ada-001 and GPT-3.5-Turbo over the basic prompt. 3) Stability: The most stable prompts, with the lowest prompt volatility, are adversarial doubt at 7.7 and EF at 8.1. In contrast, the least stable prompts, with the highest prompt volatility, are 3-shot IcL at 17.1 and manual CoT at 12.8. The average model-prompt-gain volatility (AMPGV) is 11.0, indicating a high prompt dependence within the scenario.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/db85ffa96bd7dfe99f3ca8c96145927c8483ba954729dfacb572864bb9bc0e33.jpg)



Figure 9.102 Language comparison of IV. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


Regarding language proficiency in CB: 1) English vs. Chinese: As shown in Figure 9.104, models tend to perform better on the English test set than on the Chinese set, with 18 of 28 models favoring English. 2) Accuracy Difference: Significant performance advantages for English over Chinese are seen in models like text-babbage-001 (32.7%), babbage (1.3B) (31.7%), and ada (0.35B) (29.4%). Conversely, models such as Baichuan1 (7B) (8.9%), Baichuan1-chat (13B) (7.5%), and davinci (175B) (6.4%) demonstrate a higher proficiency in Chinese.

# 9.4.4 Counterfactuals

Counterfactual reasoning. Initially, we analyze model performance in CR:

1) Distribution: Figure 9.105(a) outlines the distribution of all model-prompt pairs within CR. With a median of  $38.8\%$  and a third quartile of  $54.3\%$ , this scenario appears to have an easy understandability, as indicated by the median accuracy surpassing the average random guess benchmark of  $37.5\%$ . Figure C.8 details the distribution for each specific task. In the CR-C (CRASS) task, the median stands at  $29.7\%$ , and the third quartile is  $57.5\%$ , with random guess accuracy set at  $25.0\%$ , marking the understandability of the task as easy. For the CR-B (det-counterfactual) task, the median is calculated at  $50.1\%$ , and the third quartile at  $52.8\%$ , with a random guess accuracy of  $50.0\%$ , affirming the understandability of the task as easy. Upon examining the differences between tasks, we observe a median accuracy range from  $29.7\%$  to  $50.1\%$  with a standard deviation of 10.2. The third quartile accuracy spans from  $52.8\%$  to  $57.5\%$  with a standard deviation of 2.4, signaling that the scenario has a considerably varied variance of distribution. The peak of the distribution for both tasks aligns closely with their respective random guess accuracies. Notably, the CR-C (CRASS) task exhibits a wider distribution of model accuracy, ranging from  $0\%$  to  $100\%$ , suggesting a more decentralized distribution, whereas the CR-B (det-counterfactual) task shows a more concentrated set of outcomes.

2) Top Accuracy: Figure 9.106(a) reveals the three leading models in this scenario by average accuracy are GPT-4 at  $76.9\%$ , text-davinci-003 at  $67.8\%$ , and Claude2 at  $62.5\%$ . The top model-prompt pair is GPT-4 with

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/79f7e44c5cbd2acfddaca04d23d5ba0412aa8dc9938637b9fafa21f393548007.jpg)



(a) Model performance of CB


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4b357fc4b283a60dd30179c3b6461f4bf14adab452f46f39c2ffdde7a6aab69d.jpg)



(b) Prompt gain of CB



Figure 9.103 Heatmap of CB. The models and prompts are sorted by their averages.


manual CoT, achieving an  $83.2\%$  accuracy. The scenario has a solvable solvability with the top model's average accuracy surpassing  $70\%$ . Figure C.28 details the top models' average accuracy across various tasks. In the CR-C (CRASS) task, GPT-4 leads with an average accuracy of  $85.8\%$ , followed by text-davinci-003 at  $77.8\%$ , and InternLM-chat (20B) at  $73.5\%$ , with GPT-4 and adversarial ignore reaching the highest accuracy of  $91.8\%$ . This demonstrates that the task solvability is well-solved, as the top three models all achieve average accuracies over  $70\%$ . For the CR-B (det-counterfactual) task, the top models are GPT-4 at  $68.0\%$ , text-davinci-003 at  $57.9\%$ , and Claude2 at  $55.8\%$ , with GPT-4 and manual CoT leading to a  $77.4\%$  accuracy, marking the solvability of the task as challenging due to the top model-prompt pair not reaching  $80\%$ . Upon comparing the tasks, there is a large variance of solvability. The top model's average accuracy varies significantly, from  $68.0\%$  to  $85.8\%$  (a  $17.8\%$  difference), and the highest accuracy achieved by top model-prompt pairs ranges from  $77.4\%$  to  $91.8\%$  (a  $14.4\%$  difference), highlighting a extremely significant variance of model's top performance. GPT-4 is notably the best model in terms of average performance and the model that forms the top model-prompt pair across tasks. Furthermore, text-davinci-003 is the second-best model in average performance for both tasks. The CR-C (CRASS) task outperforms the CR-B (det-counterfactual) in both top model-prompt pair accuracy and top average model performance.

3) Stability: The three most consistent models in the scenario, characterized by the model volatility, are curie (6.7B) at 1.8, text-curie-001 at 3.2, and Baichuan1-chat (13B) at 3.4. Conversely, the models displaying the greatest variability across various prompts, showcasing their great sensitivity to prompts, are Llama2 (70B) at 15.4, Llama2-chat (70B) at 14.2, and Vicuna-v1.3 (33B) at 11.9. Next, we consider the stability task-by-task. In

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9578a6b784482f10b263f83c22f4691fdb6eca6e6ea369c9ccb7aa59b1843beb.jpg)



Figure 9.104 Language comparison of CB. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/475d7dabb5d87ae2aec545782697034cc23a82efa8b63b280a32fe6df31bd0c2.jpg)



(a) Distribution of CR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/95366f155b5197764a4fe7f2e2b4b15d195e174abc02d4c983544948e78a2daa.jpg)



(b) Distribution of AC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9e38c92387b62102deb31094dcdf112813ff6fb23caae37835eeb658bec8a765.jpg)



(c) Distribution of ETT


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/74ef963058771db2cc7f030da200d66c2bd2166398274ed29d75459b7fa6ad58.jpg)



(d) Distribution of NDE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/043fdadae8216af55723f2d54b77f9c6845ffbd3b3ba35a23d6ce469f151174b.jpg)



(e) Distribution of NIE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/abbf87728a0b2ce04e29a56bf1e8c7689a1dc8b65e2bb757bdc3a9c89a13f658.jpg)



(f) Distribution of PN


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ae857cc5e4eed60d211f825cd968cb48ceb515d8ad1a5608af53e99ba6fa9762.jpg)



(g) Distribution of PS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c8f358c66cd3c71d29056c23770c581ed03706e4d0c3fdd9d9786e1f89c71b83.jpg)



(h) Distribution of CEG



Figure 9.105 Distribution of counterfactuals. The horizontal coordinate represents the accuracy of the model and the vertical coordinate represents the percentage distribution corresponding to a certain accuracy interval.


the CR-C (CRASS) task, the most stable models are text-ada-001 at 1.7, text-babbage-001 at 2.1, and babbage (1.3B) at 3.2, while the models with the highest model volatility, indicating the most variability, are Llama2 (70B) at 30.2, Llama2-chat (70B) at 25.1, and text-davinci-001 at 14.9. In the CR-B (det-counterfactual) task, the most consistent models include Baichuan1 (7B) at 0.8, text-davinci-001 at 0.8, and davinci (175B) at 1.0. The models with the largest model volatility, hence the most instability, are InternLM-chat (20B) at

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/fa5195e8250386b240128a39073659a4b1cac0018711f9eb65936a88c3393df2.jpg)



(a) Model performance of CR


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5f4ad6f9a5fae4b08ad8b6641c5a4944bd3fb9b1416d6f691b622daba8df4c7c.jpg)



(b) Prompt gain of CR



Figure 9.106 Heatmap of CR. The models and prompts are sorted by their averages.


19.2, Llama2-chat (70B) at 16.3, and Vicuna-v1.3 (33B) at 11.8. Upon comparing across tasks, it is observed that while text-davinci-001 ranks as the second most stable model in the CR-B (det-counterfactual), it is the third least stable model in the CR-C (CRASS) task. Additionally, Llama2-chat (70B) consistently appears as the second most unstable model in both tasks.

4) Open-Limited Ratio: The ratio of open-access to limited-access models among the top five in the entire scenario stands at 0:5, indicating a large open-limited gap.

Next, we analyze prompt gain in CR:

1) Top Gain: As shown in Figure 9.106(b), the two prompts leading to the highest average accuracy improvements over the basic prompt are manual CoT at  $7.3\%$  and 3-shot IcL at  $6.0\%$ . The largest improvement relative to the basic prompt is achieved by Llama2 (70B) with 3-shot IcL, recording a  $35.4\%$  increase. A more specific analysis is conducted for each task. Figure C.29 presents the gain heatmaps for all tasks within the scenario. In the CR-C (CRASS) task, manual CoT at  $16.0\%$  and 3-shot IcL at  $8.4\%$  top the charts for average accuracy gain over the basic prompt, with Llama2 (70B) and 3-shot IcL marking the most substantial increase at  $68.7\%$ . In the CR-B (det-counterfactual) task, 1-shot IcL at  $4.8\%$  and EF at  $4.4\%$  provide the highest average accuracy gains, with Koala (13B) and EF achieving the most significant improvement at  $23.3\%$ . Upon reviewing both tasks, the leading accuracy gain prompt and the leading accuracy gain model-prompt pair differ between the two tasks. The CR-C (CRASS) task exhibits a higher top gain compared to the CR-B (det-counterfactual) task.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1e82adea848132321143928d83ce76dce5a6b027be0372b6f0771b2d029b2865.jpg)



Figure 9.107 Language comparison of CR. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


2) Exceptions: Though manual CoT is the most effective prompt in giving positive average prompt gain across most models in the scenario, it has exceptions in models including Baichuan1-chat (13B), Llama2-chat (70B), Vicuna-v1.3 (33B), InternLM-chat (20B), and Claude2. All prompts manage to enhance the performance of models such as ada (0.35B), Baichuan1 (7B), and Qwen (14B) beyond their performance under basic prompt. However, Claude2's performance is not increased by any prompt. In the CR-C (CRASS) task, manual CoT does not work well with Koala (13B), text-babbage-001, Vicuna-v1.3 (33B), Claude2, and GPT-4 in generating positive average prompt gains. Despite this, all prompts are capable of boosting the performance of Baichuan1 (7B) and Qwen (14B) above their basic prompt performance. On the other hand, all prompts fail to improve the performance of text-babbage-001 and Claude2 above the basic prompt within this task. For the CR-B (det-counterfactual) task, 1-shot IcL shows ineffectiveness with Baichuan1-chat (13B), Baichuan2-chat (13B), Llama2 (7B), Llama2 (13B), Baichuan2-chat (7B), text-davinci-001, GPT-3.5-Turbo, and Claude2. Nonetheless, all prompts success in producing positive average prompt gain for Koala (13B) and ada (0.35B).

3) Stability: Regarding stability in the scenario, the most stable prompts are 0-shot IcL and adversarial ignore, with prompt volatility of 4.0 and 4.7, respectively, indicating minimal variability. On the opposite end, 3-shot IcL and manual CoT are the most variable, with prompt volatility of 12.1 and 9.9, highlighting their high sensitivity to prompt selection. The average model-prompt-gain volatility (AMPGV) is 7.0, suggesting a medium level of prompt dependence across the scenario. Stability is further analyzed for each specific task. In the CR-C (CRASS) task, the most stable prompts are 0-shot CoT and adversarial doubt, with prompt volatility of 4.4 and 6.7. Conversely, 3-shot IcL and manual CoT show the most variability, with prompt volatility of 20.8 and 17.8. The task's prompt dependence is high as the AMPGV for this task is 10.7. For the CR-B (det-counterfactual) task, the most stable prompts are 0-shot IcL and adversarial doubt, with prompt volatility of 4.3 and 5.6. The most variable prompts are manual CoT and 3-shot IcL, with prompt volatility of 17.5 and 10. The task has a medium prompt dependence with an AMPGV of 6.4. Upon reviewing all tasks, the AMPGV ranges from 6.4 to 10.7, reflecting a narrow variance of prompt dependence. Adversarial doubt ranks as one of the top two most stable prompts in both tasks, whereas 3-shot IcL and manual CoT are identified as the least stable prompts,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/44a29b06f73d7be4245c03acec3fa0a8e6302594c9ecbb410c4d7fd7f2e07c85.jpg)



(a) Model performance of AC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/84d94a817e957aa376f7fcd7253ca4c5cb90c75922758695e17a754423ed7462.jpg)



(b) Prompt gain of AC



Figure 9.108 Heatmap of AC. The models and prompts are sorted by their averages.


consistent with the scenario-level findings. The CR-C (CRASS) task exhibits a higher dependency on prompts than the CR-B (det-counterfactual) task, based on their respective AMPGV.

Finally, we measure language proficiency in CR:

1) English vs. Chinese: Figure 9.107 reveals that models generally perform better in English than in Chinese, with 23 out of 28 models favoring English.

2) Accuracy Difference: Significant differences in performance between English and Chinese, with a preference for English, are noted in Claude2 (21.9%), Koala (13B) (16.9%), and text-ada-001 (14.1%). In contrast, models like Baichuan1-chat (13B) (11.2%), InternLM-chat (7B) (2.1%), and Wizardcoder (15B) (0.8%) demonstrate higher proficiency in Chinese.

Actual causality. From a model performance perspective: 1) Distribution: Figure 9.105(b) shows the distribution of all model-prompt pairs in AC. The median accuracy stands at  $45.0\%$ , with the third quartile reaching  $51.9\%$ , we consider the understandability of the scenario to be hard, as the median accuracy falls below the  $50.0\%$  threshold of random guess accuracy. 2) Top Accuracy: Figure 9.108(a) shows the ranked model performances of AC. Notably, GPT-4 leads in average accuracy at  $65.6\%$ , followed by text-davinci-003 and GPT-3.5-Turbo, with scores of  $57.2\%$  and  $56.5\%$ , respectively. GPT-4, when paired with manual CoT prompts, achieves a significant  $68.2\%$  in accuracy, yet this top performance is still short of the 80 threshold, indicating the challenging solvability of the AC scenario. 3) Stability: In the stability of model responses,

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/51e10b68ef35dc906415e2add42e5cde75a77c754dd6040aac88b5ba059e79ff.jpg)



Figure 9.109 Language comparison of AC. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


Llama2 (70B), curie (6.7B), and Llama2-chat (70B) show the greatest variations in performance across different prompts, while GPT-3.5-Turbo, GPT-4, and text-curie-001 demonstrate remarkable consistency according to the model volatility introduced in Section 6.3. 4) Open-Limited Ratio: The 0:5 ratio of open-access to limited-access models among the 5 top performers highlights a large open-limited gap, pointing to the dominance of limited-access models in this domain.

Regarding prompt gain in AC, 1) Top Gain: As depicted in Figure 9.108(b), 1-shot IcL and 3-shot IcL produce the highest average accuracy gains, at  $15.8\%$  and  $13.9\%$ , respectively. Remarkably, Llama2 (70B) using 1-shot IcL records the highest increase of  $58.8\%$  in accuracy, showcasing the potential of specially designed prompts. 2) Exceptions: The effectiveness of the top prompt, 1-shot IcL, is not uniform across all models. It fails to produce a positive average prompt gain in models including Baichuan2-chat (13B) and InternLM-chat (20B). Despite these exceptions, all prompts can enhance the performance of models like Koala (13B) and Qwen (14B) beyond the basic prompt setup. On the other hand, text-davinci-001 stands as an outlier, immune to the performance boosts of any prompts. 3) Stability: The stability of prompts is measured by their prompt volatility. Adversarial doubt and adversarial ignore are the most stable prompts, with prompt volatility of 5.9 and 6.1, respectively, suggesting their reliability across varying scenarios. Conversely, 3-shot IcL and 1-shot IcL exhibit the highest instability, highlighting a significant sensitivity to prompt design. From the average model-prompt-gain volatility (AMPGV) of 10.9, we regard the prompt dependence of the scenario as high.

Regarding language proficiency in AC, 1) English vs. Chinese: as detailed in Figure 9.109, the majority of models (19 out of 28) exhibit superior performance in English over Chinese. 2) Accuracy Difference: Models like Claude2, text-ada-001, and Llama2-chat (70B) demonstrate significant proficiency in English by accuracy differences between English and Chinese of  $29.5\%$ ,  $18.5\%$ , and  $17.7\%$ . Conversely, a subset of models, including Koala (13B), Llama2 (13B), and Qwen (7B), display a distinct advantage in Chinese, with accuracy performances outperforming their English counterparts by  $10.2\%$ ,  $7.9\%$ ,  $4.7\%$ , respectively.

Effect of the treatment on the treated. Initially, we evaluate model performance in ETT:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/25b4ef5b202c59408b4dcfdb0e1841c8608ef6d75b1ad35a1fd5f4eeb996ee87.jpg)



(a) Model performance of ETT


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4435abad585d304c3c2be6b5da8dbfda20af738ee5209deb38b38ce3fd9be29e.jpg)



(b) Prompt gain of ETT



Figure 9.110 Heatmap of ETT. The models and prompts are sorted by their averages.


1) Distribution: According to Figure 9.105(c), the distribution for all model-prompt pairs in the ETT reveals a median of  $12.5\%$  and a third quartile of  $25.2\%$ . This scenario is considered to have a hard understandability as the median accuracy falls below the random guess benchmark of  $16.7\%$ . Figure C.9 further details the distribution for each causal task respectively. In the ETT-P (ETT-basic) task, the median is  $1.2\%$ , and the third quartile is  $6.1\%$ . Given the challenging nature of Mathematical-mode tasks, we define the understandability of the task as very hard (Section 6.4). Similarly, the ETT-P (ETT-hard) task, with a median of  $1.4\%$  and a third quartile of  $13.5\%$ , is considered to have a very hard understandability. On the other hand, the ETT-B (ETT-natural) task, presenting a median of  $24.9\%$  and a third quartile of  $57.1\%$  against a random guess accuracy of  $50.0\%$ , is categorized to have a hard understandability. Examining the variance among tasks reveals median accuracies ranging from  $1.2\%$  to  $24.9\%$  with a standard deviation of 11.1, and third quartile accuracies extending from  $6.1\%$  to  $57.1\%$  with a standard deviation of 22.5. Consequently, the scenario has a highly divergent variance of distribution. Organizing tasks by both median and third quartile accuracies results in the same order: ETT-P (ETT-basic) < ETT-P (ETT-hard) < ETT-B (ETT-natural). The distributions for both Mathematical-mode tasks (ETT-P (ETT-basic), ETT-P (ETT-hard)) indicate that over  $70\%$  of model-prompt pairs fall within a  $0\%$  to  $10\%$  accuracy range. In contrast, the Natural-mode task displays a more even distribution, where no 10-unit interval contains more than  $25\%$  of the total model-prompt pair count.

2) Top Accuracy: According to Figure 9.110(a), the leading three models in this scenario by average accuracy are GPT-4 at  $40.9\%$ , GPT-3.5-Turbo at  $39.0\%$ , and Claude2 at  $35.6\%$ . GPT-4, when combined with manual CoT, reaches an impressive  $89.9\%$ , suggesting this scenario's solvability is potentially solvable, given that

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1b546ac2743f9bb92db4c688b4aee887761947275d1aa08de2b97725da8fa534.jpg)



Figure 9.111 Language comparison of ETT. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


the top model-prompt pair achieves over  $80\%$  in performance. Figure C.30 further delineates the top models' average accuracy across individual tasks. For the ETT-P (ETT-basic) task, the highest average accuracies are seen with GPT-3.5-Turbo at  $26.5\%$ , Claude2 at  $24.9\%$ , and text-davinci-003 at  $23.3\%$ . The top model-prompt pair, GPT-4 with manual CoT, secures  $86.3\%$ , marking the task solvability as potentially solvable due to the top model-prompt pair exceeding  $80\%$  in performance. In the ETT-P (ETT-hard) task, top performers are GPT-3.5-Turbo at  $40.0\%$ , GPT-4 at  $39.4\%$ , and text-davinci-003 at  $32.0\%$ , with GPT-4 and manual CoT reaching  $89.0\%$ , again underlining the task's potentially solvable solvability for similar reasons. The ETT-B (ETT-natural) task showcases GPT-4 leading at  $61.8\%$ , followed by Claude2 at  $54.5\%$ , and text-davinci-002 at  $52.6\%$ , with GPT-4 and manual CoT achieving  $94.5\%$ , reinforcing the task's potentially solvable solvability as before. Comparing Across Tasks, the variance of solvability across tasks is negligible, with the top model's average accuracy ranging from  $26.5\%$  to  $61.8\%$ , a significant difference of  $35.3\%$ , and the top model-prompt pair's peak accuracy varying from  $86.3\%$  to  $94.5\%$ , a difference of  $8.2\%$ . This indicates a significant variance of model's top performance across the scenario. The Mathematical-mode tasks (ETT-P (ETT-basic) and ETT-B (ETT-natural)) exhibit lower top accuracies than the Natural-mode task. Notably, GPT-3.5-Turbo performs best on average in Mathematical-mode tasks, whereas GPT-4 excels in the Natural-mode task. Moreover, GPT-4, especially when paired with manual CoT, stands out as the top model-prompt pair across all evaluated tasks.

3) Stability: The three most consistent models in the scenario, marked by the lowest model volatility, are Baichuan1-chat (13B) with a model volatility of 2.5, InternLM-chat (20B) at 4.3, and Baichuan2-chat (13B) at 7.8. Conversely, the models showing the highest sensitivity to prompt variations, as evidenced by the highest model volatility, are Llama2 (13B) at 24.1, Llama2 (70B) at 23.8, and Llama2 (7B) at 23.7, highlighting their considerable instability. We next conduct a detailed task-specific stability evaluation as follows: In the ETT-P (ETT-basic) task, the most stable models are Baichuan1 (7B) leading with a model volatility of 0.6, followed by text-davinci-002 at 2.2, and babbage (1.3B) at 2.3. The least stable models, with the largest model volatility, include Llama2 (70B) at 26.4, GPT-4 at 25.9, and Llama2 (7B) at 20.6. For the ETT-P (ETT-hard) task, the

top three models in terms of stability are Baichuan1 (7B) with model volatility of 0.4, Baichuan1-chat (13B) at 2.4, and babbage (1.3B) at 3.2. The models with the greatest instability are curie (6.7B) at 27.2, GPT-4 at 26.9, and Llama2 (7B) at 26.4. In the ETT-B (ETT-natural) task, the models demonstrating the highest stability include Baichuan1-chat (13B) at 2.8, InternLM-chat (20B) at 10.1, and Baichuan2-chat (13B) at 10.2. The most unstable models are Llama2 (13B) at 34.4, curie (6.7B) at 34.3, and Llama2 (7B) at 33.3. Comparing across tasks, Baichuan1 (7B) and babbage (1.3B) are shown to be the most stable models in the Mathematical-model tasks, securing the top and third spots, respectively. Notably, GPT-4 ranks as one of the two most unstable models in these tasks, with Llama2 (7B) consistently listed among the three most unstable models across the evaluated scenarios.

4) Open-Limited Ratio: The 0:5 ratio of open-access to limited-access models among the top 5 models with the highest average accuracy in the entire scenario underscores a large open-limited gap.

Next, we analyze prompt gain in ETT:

1) Top Gain: As shown in Figure 9.110(b), the two prompts leading to the highest average accuracy improvements over the basic prompt are manual CoT with a gain of  $30.4\%$  and 3-shot IcL at  $16.7\%$ . Llama2 (13B) utilizing manual CoT marks the most substantial improvement, registering a  $68.7\%$  increase over the basic prompt. A more granular, task-specific analysis is next, with Figure C.31 illustrates the accuracy gains across tasks. For the ETT-P (ETT-basic) task, manual CoT at  $31.9\%$  represents the top prompt in terms of average accuracy gains compared to the basic prompt; it is also the only prompt that has a positive average gain. Also, the model-prompt pair of Llama2 (70B) and manual CoT achieves the largest leap of  $79.6\%$ . In the ETT-P (ETT-hard) task, the highest gains are noted with manual CoT at  $34.5\%$  and 3-shot IcL at  $8.6\%$ , with Llama2 (7B) and manual CoT seeing a significant rise of  $74.7\%$ . For the ETT-B (ETT-natural) task, the leading prompts are 3-shot IcL at  $42.0\%$  and 1-shot IcL at  $38.1\%$ , with text-curie-001 and 3-shot IcL witnessing the most noteworthy boost of  $75.1\%$ . The evaluating of the tasks indicates a preference for manual CoT in the Mathematical-mode tasks (ETT-P (ETT-basic), ETT-P (ETT-hard)), whereas the Natural-mode task shows a predilection for 3-shot IcL. The peak gains across these tasks are similar in value.

2) Exceptions: The scenario's highly effective prompt, manual CoT, does not align well with certain models for producing positive average prompt gain, specifically Baichuan1-chat (13B) and Baichuan1 (7B). Within the ETT-P (ETT-basic) task, manual CoT underperforms for text-davinci-002 and Baichuan1-chat (13B). In the ETT-P (ETT-hard) task, manual CoT also falls short with Baichuan1-chat (13B). On the other hand, all prompts enhance GPT-3.5-Turbo's performance beyond the basic prompt. For the ETT-B (ETT-natural) task, the leading prompt, 3-shot IcL, shows ineffectiveness with Baichuan1-chat (13B), text-davinci-003, and Claude2 in generating a positive average prompt gain. Across all tasks, text-davinci-003 and Claude2 consistently shows a negative impact to 3-shot IcL.

3) Stability: The most stable prompts in the scenario are adversarial ignore and adversarial doubt, with prompt volatility of 3.1 and 3.2, respectively, highlighting a low variability in performance. On the contrary, manual CoT and 3-shot IcL, with prompt volatility of 21.4 and 18.8, are revealed as the most variable. The prompt dependence in the scenario is high, as the average model-prompt-gain volatility (AMPGV) is 15.3. In task-specific stability analysis, we find the following conclusions. In the ETT-P (ETT-basic) task, the most stable prompts are adversarial ignore and adversarial doubt, with prompt volatility of 2.2 and 2.8, contrasting with manual CoT and 3-shot IcL, the most variable at prompt volatility of 21.5 and 14.6. The AMPGV of the task is 12.9, showing that the task has a high prompt dependence. For ETT-P (ETT-hard), adversarial ignore and adversarial doubt maintain the lowest prompt volatility at 1.8 and 2.8, whereas manual CoT and 3-shot IcL

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/640f213ec6741094ab79296a743d18723f92a2f26dbde3966334e904392852cb.jpg)



(a) Model performance of NDE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a1ebc4861575dad3f18567ab81609db2d6d79c11d5b86972e4c25f15bc647d44.jpg)



(b) Prompt gain of NDE



Figure 9.112 Heatmap of NDE. The models and prompts are sorted by their averages.


display the highest variability, with prompt volatility of 24.7 and 22.8. The  $AMPGV$  of 15.9 underscores a high prompt dependence. The ETT-B (ETT-natural) task shows EF and adversarial doubt as the most stable, with prompt volatility of 5.6 and 6.7, and 3-shot IcL and 1-shot IcL as the most variable, with prompt volatility of 31.9 and 29.7. The  $AMPGV$  is 24.6, revealing a high prompt dependence. Across the scenario, the  $AMPGV$  range widely from  $12.9\%$  to  $24.6\%$ , indicating a wide variance of prompt dependence. Adversarial doubt ranks among the top three for stability across all tasks, while 3-shot IcL consistently appears among the three least stable prompts. The Mathematical-mode tasks exhibit less prompt dependency compared to the Natural-mode task, as suggested by their respective  $AMPGV$ , pointing towards variability in how different tasks respond to prompt strategies.

At last, we measure language proficiency in ETT,

1) English vs. Chinese: As shown in Figure 9.111, the performance of models on the English test set is better than the one on the Chinese test set, with 23 out of 28 models performing better in English than in Chinese.

2) Accuracy Difference: The most significant accuracy differences in performance between English and Chinese, favoring English, are seen in GPT-3.5-Turbo (26.6%), text-davinci-002 (13.7%), and Llama2 (13B) (11.9%). On the flip side, models such as Baichuan1-chat (13B) (9.2%), Baichuan2-chat (7B) (3.7%), and babbage (1.3B) (3.4%) show the top preference in Chinese compared to English.

Natural direct effect. Initially, we evaluate model performance of NDE:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/de0ee9ad5c8dd66d6827546ac49da03896a6d3ff228c83311e86ef33ebd038d5.jpg)



Figure 9.113 Language comparison of NDE. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


1) Distribution: The distribution of the model-prompt pairs within the NDE, as shown in Figure 9.105(d), highlights the scenario's understandability. With a median value of  $14.0\%$  and a third quartile of  $19.9\%$ , the scenario's understandability is regarded as hard since the median accuracy falls below the expected random guess accuracy of  $16.7\%$ . Figure C.10 shows the distribution across various causal tasks of all model-prompt pairs in the task. In the NDE-P (NDE-basic) task, the median is calculated at  $0.6\%$ , and the third quartile is  $4.6\%$ . Given the challenging nature of Mathematical-mode tasks, we define the understandability of this task as very hard (Section 6.4). For the NDE-P (NDE-hard) task, the median settles at  $0.7\%$ , with a third quartile of  $4.8\%$ . Similar to NDE-P (NDE-basic), we regard the understandability of the task as very hard. The NDE-B (NDE-natural) task presents a median of  $36.9\%$  and a third quartile of  $56.0\%$ , with a random guess accuracy of  $50.0\%$ , its understandability is hard. Upon comparing task variances, it is observed that median accuracies span from  $0.6\%$  to  $36.9\%$  with a standard deviation of 17.1, and third quartile accuracies range from  $4.6\%$  to  $56.0\%$  with a standard deviation of 24.2. This variation underscores the highly divergent variance of distribution across tasks in the scenario. The ordering of tasks by both median and third quartile accuracies remains consistent: NDE-P (NDE-basic) < NDE-P (NDE-hard) < NDE-B (NDE-natural). Notably, the Mathematical-mode task (NDE-P (NDE-basic), NDE-P (NDE-hard)) distributions indicate an approximation where nearly  $80\%$  of model-prompt pairs in an accuracy between  $0\%$  to  $10\%$ . On the other hand, the distribution for the Natural-mode task is more balanced, with no 10-unit range encompassing more than  $25\%$  of the total model-prompt pairs.

2) Top Accuracy: From Figure 9.112(a), we observe that the three highest-performing models in terms of average accuracy for this scenario are GPT-4 at  $42.6\%$ , GPT-3.5-Turbo at  $40.4\%$ , and Claude2 at  $39.2\%$ . The top model-prompt pair is GPT-4 with manual CoT, reaching an accuracy of  $80.1\%$ , indicating that the solvability of this scenario is potentially solvable as the top model-prompt pair's performance hits  $80\%$ . Figure C.32 displays the top three models by average accuracy for each task. In the NDE-P (NDE-basic) task, the top models by average accuracy are GPT-4 at  $27.3\%$ , Claude2 at  $27.1\%$ , and GPT-3.5-Turbo at  $27.1\%$ , with GPT-4 using manual CoT achieving  $70.2\%$ . This indicates the task solvability is challenging as the top model-prompt pair's

performance is larger than the random guess but less than  $80\%$ . For NDE-P (NDE-hard), the leading models in average accuracy are GPT-3.5-Turbo at  $32.4\%$ , GPT-4 at  $30.1\%$ , and Claude2 at  $28.9\%$ , with GPT-4 using manual CoT reaching  $76.1\%$ , marking the solvability of the task as challenging since the top model-prompt pair's performance is larger than random guess but less than  $80\%$ . In the NDE-B (NDE-natural) task, the top models by average accuracy are GPT-4 at  $62.6\%$ , Claude2 at  $58.0\%$ , and GPT-3.5-Turbo at  $57.9\%$ , with GPT-4 using manual CoT attaining  $93.9\%$ . This shows the task has a potentially solvable solvability as the top model-prompt pair's performance reaches  $80\%$  but the top model's average accuracy is below  $70\%$ . Through comparing different tasks, the variance of solvability between tasks is small. Additionally, the top model's average accuracy ranges from  $27.3\%$  to  $62.6\%$  (a difference of  $35.3\%$ ), and the top model-prompt pair's accuracy varies from  $70.2\%$  to  $93.9\%$  (a difference of  $23.7\%$ ), demonstrating the scenario's variance of model's top performance is extremely significant. The Mathematical-mode tasks show comparatively lower top accuracies than the Natural-mode task. Across all tasks, GPT-4, GPT-3.5-Turbo, and Claude2 consistently rank within the top three for average model performance. Furthermore, GPT-4 with manual CoT stands out as the top model-prompt pair across all tasks.

3) Stability: The three most stable models, characterized by the lowest model volatility, are Baichuan1-chat (13B) with a model volatility of 2.3, InternLM-chat (7B) at 3.0, and InternLM-chat (20B) at 3.1. Conversely, the three least stable models, exhibiting the highest model volatility across different prompts, are Llama2 (13B) at 20.3, Llama2-chat (70B) at 18.2, and Llama2 (70B) also at 18.2, showcasing their significant prompt sensitivity. We move on to analyze stability from a model-prompt-task perspective: For the NDE-P (NDE-basic) task, the most stable models are davinci (175B) at 0.1, babbage (1.3B) also at 0.1, and text-ada-001 at 0.2. In contrast, the least stable models include GPT-3.5-Turbo at 20.7, Llama2 (70B) at 18.0, and Llama2-chat (70B) also at 18.0. For the NDE-P (NDE-hard) task, the models demonstrating the greatest stability, with minimal model volatility, are babbage (1.3B), davinci (175B), and text-babbage-001 all at 0.0. On the flip side, the models showing the least stability are GPT-4 at 21.4, Llama2 (13B) at 19.9, and GPT-3.5-Turbo at 18.0. For the NDE-B (NDE-natural) task, the top three stable models are Baichuan1-chat (13B) at 4.0, InternLM-chat (20B) at 9.9, and text-davinci-002 at 10.4. Conversely, the least stable models are Llama2 (13B) at 29.0, text-curie-001 at 25.9, and Llama2-chat (70B) at 25.3. When evaluating the tasks, it is observed that while GPT-3.5-Turbo and GPT-4 are among the top performers in certain tasks, they also exhibit significant instability in others.

4) Open-Limited Ratio: With a 0:5 ratio of open-access to limited-access models among the top five models in the overall scenario, the open-limited gap is large.

Next, we analyze prompt gain in NDE:

1) Top Gain: Illustrated in Figure 9.112(b), the leading two prompts achieving the most significant average accuracy improvements over the basic prompt are manual CoT at  $19.1\%$  and 3-shot IcL at  $9.9\%$ . The highest gain in accuracy over the basic prompt is seen with Llama2 (13B) employing manual CoT, with an increase of  $59.0\%$ . We proceed to a task-specific detailed examination. Figure C.33 displays the gains across all tasks from a model-prompt-task perspective. For the NDE-P (NDE-basic) task, the two prompts yielding the most considerable average accuracy gains over the basic prompt are manual CoT at  $21.7\%$  and 3-shot IcL at  $4.6\%$ . The largest improvement in accuracy over the basic prompt is with Llama2 (70B) using manual CoT, indicating a rise of  $54.3\%$ . In the NDE-P (NDE-hard) task, the two prompts with the highest average accuracy gains over the basic prompt are manual CoT at  $19.0\%$  and 3-shot IcL at  $1.3\%$ . The most significant increase in accuracy over the basic prompt is with Llama2 (13B) using manual CoT, demonstrating a gain of  $56.1\%$ . Within the NDE-B (NDE-natural) task, the two prompts leading to the highest average accuracy gains over the basic prompt are 3-shot IcL at  $23.9\%$  and 1-shot IcL at  $22.3\%$ . The most substantial enhancement in accuracy

over the basic prompt is seen with Llama2 (13B) utilizing manual CoT, with an uplift of  $71.0\%$ . - The task evaluation reveals a preference towards manual CoT in Mathematical-mode tasks, while the Natural-mode task prefers 3-shot IcL. Furthermore, across all tasks, manual CoT consistently secures the highest gains in comparison to other model-prompt pairs, with the Natural-mode task achieving greater top gains than the Mathematical-mode tasks.

2) Exceptions: The most effective prompt, manual CoT, cannot create positive average prompt gain for several models, including text-ada-001, ada (0.35B), Baichuan1 (7B), Qwen (14B), Claude2. In the NDE-P (NDE-basic) task, the best prompt, manual CoT, fails to perform a positive average prompt gain on Claude2. In the NDE-P (NDE-hard) task, manual CoT does not prove effective for davinci (175B), Baichuan1 (7B), Claude2, and no prompt enhances davinci (175B)'s performance over the basic prompt in this task. For the NDE-B (NDE-natural) task, the top prompt, 3-shot IcL, is ineffective on Baichuan1-chat (13B), Claude2, GPT-4. Notably, in the two Mathematical-mode tasks (NDE-P (NDE-basic) and NDE-P (NDE-hard)), manual CoT does not work well with Claude2.

3) Stability: Regarding stability within the scenario, the two most stable prompts are adversarial doubt and adversarial ignore, with prompt volatility of 1.9 and 2.2, respectively. On the opposite end, the two prompts exhibiting the greatest instability, as indicated by the largest prompt volatility, are manual CoT at 19.3 and 3-shot IcL at 8.6. This results in an average model-prompt-gain volatility (AMPGV) of 10.8, demonstrating a high prompt dependence. We further analyze stability from a model-prompt-task perspective. For the NDE-P (NDE-basic) task, adversarial doubt and adversarial ignore are recognized as the most stable prompts, with prompt volatility of 0.8 and 1.0, respectively. Conversely, manual CoT and 3-shot IcL show the most instability, with prompt volatility of 20.4 and 8.9, respectively. The AMPGV for this task is 8.8, indicating a medium level of prompt dependence. In the NDE-P (NDE-hard) task, the most stable prompts are again adversarial doubt and adversarial ignore, with prompt volatility of 1.0 and 1.3, respectively. The most unstable prompts are manual CoT and 3-shot IcL, with prompt volatility of 20.1 and 8.2, respectively. This task has an AMPGV of 8.5, suggesting a medium prompt dependence. For the NDE-B (NDE-natural) task, the most stable prompts with the smallest prompt volatility are adversarial doubt and adversarial ignore, at 5.6 and 7.0, respectively. The most variable prompts, indicating instability, are manual CoT and 3-shot IcL, with prompt volatility of 23.2 and 22.0, respectively. The AMPGV in this task is 19.7, pointing to a high prompt dependence. Upon reviewing all tasks, the AMPGV range from 8.5 to 19.7, reflecting the wide variance of prompt dependence. Across all tasks, adversarial doubt and adversarial ignore consistently rank as the most stable prompts, whereas manual CoT and 3-shot IcL are identified as the most unstable. The Mathematical-mode tasks show a lower prompt dependency than the Natural-mode task, as indicated by their respective AMPGV, highlighting differences in task responsiveness to prompt strategies.

Finally, we consider language proficiency in NDE,

1) English vs. Chinese: Figure 9.113 illustrates that models tend to perform better on the English test set compared to the Chinese test set, with 20 out of 28 models showing superior performance in English.

2) Accuracy Difference: The most significant discrepancies in performance between English and Chinese, with a preference for English, are noted in GPT-3.5-Turbo (15.2%), Llama2 (13B) (10.5%), and text-davinci-002 (10.3%). In contrast, models like text-babbage-001 (9.6%), babbage (1.3B) (7.3%), and Baichuan1-chat (13B) (7.1%) demonstrate greater proficiency in Chinese than in English.

Natural indirect effect. First, we consider model performance in NIE:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/42f0fbd07d7ed4864be05b90947ac3824048d72e3bc9ae05d11b7b200f7179c0.jpg)



(a) Model performance of NIE


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ca1fac64e8699784e7930c5c38ee078874ef3bedfdfb6e31f9608c990fea126f.jpg)



(b) Prompt gain of NIE



Figure 9.114 Heatmap of NIE. The models and prompts are sorted by their averages.


1) Distribution: Figure 9.105(e) showcases the distribution for all model-prompt pairs under the NIE scenario. With a median value of  $6.7\%$  and a third quartile of  $19.0\%$ , this scenario is considered to have a hard understandability as the median accuracy falls below the random guess benchmark of  $16.7\%$ . Figure C.11 shows the distribution for all model-prompt pairs in each individual causal task. In the NIE-P (NIE-basic) task, the median is calculated to be  $2.0\%$ , and the third quartile is  $11.2\%$ . Considering both the difficulty for most Mathematical-mode tasks and the lower than  $15\%$  third quartile accuracy, we define the understandability of this task as very hard. In the NIE-P (NIE-hard) task, the median stands at  $1.8\%$ , and the third quartile is  $12.1\%$ . Similarly, we regard the task understandability as very hard. In the NIE-B (NIE-natural) task, the median reaches  $15.4\%$ , with the third quartile at  $31.5\%$ , and the random guess accuracy at  $50.0\%$ , we assess the understandability of the task as very hard. Upon examining task variances, the median accuracies span from  $1.8\%$  to  $15.4\%$  with a standard deviation of  $6.4$ , and the third quartile accuracies range from  $11.2\%$  to  $31.5\%$  with a standard deviation of  $9.4$ , highlighting the scenario having a moderately distinct variance of distribution. The Natural-mode task significantly outperforms the two mathematics-focused tasks (NIE-P (NIE-hard) and NIE-P (NIE-basic)) in terms of both median and third quartile values. For these Mathematical-mode tasks, over  $70\%$  of model-prompt pairs are found within a  $0\%$  to  $10\%$  accuracy bracket. Conversely, the Natural-mode task presents a more balanced distribution, with no  $10\%$  unit segment housing more than  $40\%$  of the total model-prompt pairs.

2) Top Accuracy: Observing Figure 9.114(a), the leading three models in terms of average accuracy in this scenario are GPT-3.5-Turbo at  $43.0\%$ , GPT-4 at  $26.1\%$ , and Baichuan2-chat (7B) at  $25.6\%$ . The top model-prompt

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4703444cb00b64299184891d49b808b85b7c9c90c8a4abcd5235c00e082201e2.jpg)



Figure 9.115 Language comparison of NIE. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


pair is Koala (13B) with 3-shot IcL, achieving a  $73.3\%$  accuracy, suggesting the solvability of this scenario is challenging as the performance of the top model-prompt pair surpasses the random guess but remains below  $80\%$ . Figure C.34 details the top three models' average accuracy for each specific task. For the NIE-P (NIE-basic) task, the highest average accuracies are seen with GPT-3.5-Turbo at  $40.8\%$ , Claude2 at  $21.2\%$ , and GPT-4 at  $18.7\%$ . Koala (13B) using 3-shot IcL tops this task with a  $69.1\%$  accuracy, marking its solvability as challenging since the top model-prompt pair outperforms the random guess but does not reach  $80\%$ . In the NIE-P (NIE-hard) task, the top performers in average accuracy are GPT-3.5-Turbo at  $43.1\%$ , GPT-4 at  $26.5\%$ , and Baichuan2-chat (7B) at  $17.2\%$ , with Koala (13B) and 3-shot IcL leading at  $66.3\%$ , again indicating the task solvability is challenging as the top model-prompt pair's performance exceeds the random guess yet falls short of  $80\%$ . For the NIE-B (NIE-natural) task, the models leading in average accuracy are GPT-3.5-Turbo at  $44.8\%$ , Baichuan2-chat (7B) at  $40.5\%$ , and text-davinci-002 at  $38.4\%$ , with davinci (175B) using 3-shot IcL achieving the highest at  $84.6\%$ , showing this task having a potentially solvable solvability since the top model-prompt pair attains  $80\%$ , but the top model's average accuracy is below  $70\%$ . By analyzing the differences across tasks, we find that the variance of solvability among tasks is small. Additionally, the leading model's average accuracy spans from  $40.8\%$  to  $44.8\%$  (a  $4.0\%$  difference), and the accuracy by the top model-prompt pair ranges from  $66.3\%$  to  $84.6\%$  (an  $18.3\%$  difference), pointing to a considerable variance of model's top performance. The Mathematical-mode tasks generally have lower top accuracies than the Natural-mode tasks. GPT-4 consistently ranks high in average performance across tasks. 3-shot IcL significantly boosts model performance, consisting of the top model-prompt pair in all tasks.

3) Stability: The three most stable models, characterized by the lowest model volatility, are Baichuan1-chat (13B) at 2.4, Baichuan2-chat (13B) at 4.5, and Vicuna-v1.3 (33B) at 4.8. Conversely, the three most unstable models, showcasing the highest model volatility across various prompts, are Llama2 (7B) at 30.8, Llama2 (13B) at 30.4, and Baichuan2-chat (7B) at 24.9, reflecting their pronounced sensitivity to prompt variations. Moving to an analysis of stability across individual tasks: In the NIE-P (NIE-basic) task, the most stable models include Baichuan2-chat (13B) at 2.3, Baichuan1-chat (13B) at 2.5, and text-ada-001 at 4.6. In contrast, the

most unstable models are Llama2 (7B) at 27.5, Llama2 (13B) at 24.8, and Baichuan2-chat (7B) at 23.9. For the NIE-P (NIE-hard) task, the top stable models with the lowest model volatility are Baichuan2-chat (13B) at 2.1, Baichuan1-chat (13B) also at 2.1, and Vicuna-v1.3 (33B) at 4.1. The most unstable models are Llama2 (13B) at 30.0, Llama2 (7B) at 28.9, and Baichuan2-chat (7B) at 26.0. In the NIE-B (NIE-natural) task, the three most stable models are Baichuan1-chat (13B) at 2.5, babbage (1.3B) at 6.0, and Vicuna-v1.3 (33B) at 8.3. Meanwhile, the models with the largest model volatility are Llama2 (13B) at 34.5, Llama2 (7B) at 33.0, and Baichuan2-chat (7B) at 27.8. Across all tasks, Baichuan1-chat (13B) is consistently among the three most stable models, whereas Llama2 (7B), Llama2 (13B), and Baichuan2-chat (7B) are consistently among the three most unstable models.

4) Open-Limited Ratio: With a 2:3 ratio of open-access to limited-access models among the top five models in the entire scenario, the open-limited gap is small.

Next, we explore prompt gain in NIE:

1) Top Gain: Illustrated in Figure 9.114(b), the two prompts leading to the highest average accuracy improvements over the basic prompt are 3-shot IcL at  $29.3\%$  and manual CoT at  $19.5\%$ . The most significant increase in accuracy, when compared with the basic prompt, is seen with Llama2 (13B) employing 3-shot IcL, which results in a surge of  $72.1\%$ . Proceeding with a more granular, task-specific analysis, Figure C.35 presents the heatmap of gains across all tasks within the scenario. For the NIE-P (NIE-basic) task, the two prompts yielding the greatest average accuracy boost over the basic prompt are 3-shot IcL at  $27.6\%$  and manual CoT at  $18.5\%$ . The largest leap in accuracy against the basic prompt is with Koala (13B) using 3-shot IcL, registering a gain of  $69.1\%$ . In the NIE-P (NIE-hard) task, the leading two prompts in terms of average accuracy gain compared to the basic prompt are 3-shot IcL at  $28.9\%$  and manual CoT at  $19.4\%$ , with Koala (13B) utilizing 3-shot IcL witnessing an uplift of  $66.3\%$ . For the NIE-B (NIE-natural) task, the two prompts achieving the highest average accuracy gains over the basic prompt are 3-shot IcL at  $31.5\%$  and manual CoT at  $20.5\%$ , with Llama2 (13B) applying 3-shot IcL showing an impressive improvement of  $81.8\%$ . Across each distinct task, 3-shot IcL and manual CoT stand out as the most useful prompts, consistently demonstrating their effectiveness in enhancing performance. Specifically, 3-shot IcL helps models achieve the highest gains compared to other model-prompt pairs. Additionally, the Natural-mode task exhibits greater top gains compared to the Mathematical-mode tasks.

2) Exceptions: The high-performing prompt in the scenario, 3-shot IcL, does not work well with several models in creating a positive average prompt gain, including Baichuan1-chat (13B), Vicuna-v1.3 (33B), Baichuan2-chat (13B), text-davinci-003, Claude2, and GPT-3.5-Turbo. It is noteworthy that all prompts enhance GPT-4's performance beyond the basic prompt, yet none manage to boost Claude2's performance from its basic prompt performance. In the NIE-P (NIE-basic) task, 3-shot IcL fails to be effective for Baichuan1-chat (13B), Baichuan2-chat (13B), Vicuna-v1.3 (33B), text-davinci-003, GPT-4, Claude2, and GPT-3.5-Turbo. Every prompt is capable of improving Llama2 (70B)'s performance over the basic prompt, with Claude2 again showing no improvement with any prompt in this task. In the NIE-P (NIE-hard) task, 3-shot IcL proves ineffective for Vicuna-v1.3 (33B), Baichuan1-chat (13B), Baichuan2-chat (13B), text-davinci-003, Claude2, and GPT-3.5-Turbo, with Claude2's performance remaining unimproved by any prompt. For the NIE-B (NIE-natural) task, 3-shot IcL is ineffective with Baichuan1-chat (13B), Baichuan2-chat (13B), GPT-4, text-davinci-003, Claude2, and GPT-3.5-Turbo. It is worth mentioning that 3-shot IcL fails to improve performance for Baichuan1-chat (13B), Baichuan2-chat (13B), text-davinci-003, Claude2, and GPT-3.5-Turbo across all tasks.

3) Stability: Regarding stability within the scenario, the two most stable prompts, indicated by the smallest prompt volatility, are 0-shot IcL at 3.2 and adversarial doubt at 3.3. On the opposite spectrum, the two prompts exhibiting the greatest instability, marked by the highest prompt volatility, are 3-shot IcL at 31.3 and manual CoT at 23.3. This results in an average model-prompt-gain volatility (AMPGV) of 17.0, illustrating the scenario's high prompt dependence. Analyzing stability across individual tasks: In the NIE-P (NIE-basic) task, the most stable prompts are adversarial doubt at 2.7 and 0-shot CoT at 2.9, while the most unstable prompts are 3-shot IcL at 34.5 and manual CoT at 22.7. The AMPGV here is 16.1, signifying a high prompt dependence. For the NIE-P (NIE-hard) task, the prompts showing the least variability are adversarial doubt at 1.4 and adversarial ignore at 1.9, contrasted by the most variable prompts, 3-shot IcL at 30.0 and manual CoT at 23.8. This task has an AMPGV of 16.4, indicating a high prompt dependence. In the NIE-B (NIE-natural) task, the two most stable prompts are 0-shot IcL at 5.7 and EF at 6.8, whereas the most unstable are 3-shot IcL at 34.7 and manual CoT at 27.8, with an AMPGV of 19.6, showing a high prompt dependence. After reviewing all tasks, the range of AMPGV is from 16.1 to 19.6, reflecting a narrow variance of prompt dependence. Despite 3-shot IcL and manual CoT being among the most effective, they also rank as the most unstable across all tasks. Mathematical-mode tasks show a lesser reliance on prompts compared to the Natural-mode task, as indicated by their respective AMPGV.

Finally, we analyze language proficiency in NIE,

1) English vs. Chinese: Figure 9.115 reveals that models generally perform better on the English test set than on the Chinese set, with 25 out of 28 models favoring English over Chinese.

2) Accuracy Difference: The most pronounced performance differences between English and Chinese, with a preference for English, are noted in GPT-3.5-Turbo (21.1%), GPT-4 (15.9%), and InternLM-chat (7B) (15.9%). In contrast, models such as Baichuan1-chat (13B) (8.1%), text-davinci-003 (3.5%), and babbage (1.3B) (1.4%) exhibit superior performance in Chinese compared to English.

Probability of necessity. First, we evaluate model performance in PN:

1) Distribution: Figure 9.105(f) illustrates the distribution of all model-prompt pairs in PN. The scenario has a median of  $0.3\%$  and a third quartile of  $1.6\%$ . Given that Mathematical-mode tasks are generally considered more difficult to grasp than Natural-mode tasks from a common perspective, as evidenced by both the median and third quartile values being lower than  $2\%$ , we categorize the understandability of the PN scenario as very hard to understand. Figure C.12 showcases the distribution for each model-prompt pair across individual tasks. In the PN-P (PN-basic) task, the median is recorded at  $0.2\%$ , with the third quartile at  $1.4\%$ . Similar to the previously defined understandability of the probability computation tasks, we regard this task as very hard to understand. In the PN-P (PN-hard) task, the median remains at  $0.2\%$ , with the third quartile at  $1.6\%$ . We also consider this task having a very hard understandability. Upon examining the variance between tasks, we find that the median accuracies are consistently at  $0.2\%$  with a standard deviation of 0.0. The third quartile accuracies range from  $1.4\%$  to  $1.6\%$ , with a slight standard deviation of 0.1, indicating that the scenario has a minimally divergent variance of distribution. Moreover, in both tasks, the majority of the distribution, exceeding  $90\%$ , falls within the 0 to 10 accuracy range.

2) Top Accuracy: Illustrated in Figure 9.116(a), the three highest-performing models in terms of average accuracy within this scenario are GPT-4 at  $14.5\%$ , GPT-3.5-Turbo at  $8.1\%$ , and Llama2 (70B) at  $5.2\%$ . The top model-prompt pair, GPT-4 with manual CoT, achieves a significant  $50.2\%$  accuracy, indicating the solvability of this scenario is challenging as the performance of the top model-prompt pair exceeds the random guess

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ff366425cd49a7f69d9aa60b9b44918161d862cfea1a2d89ef55280295cd39f7.jpg)



(a) Model performance of PN


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/475832e66a42be3fec43f22bed1e809e37e12aa3986f8c82db986ea6285f8d33.jpg)



(b) Prompt gain of PN



Figure 9.116 Heatmap of PN. The models and prompts are sorted by their averages.


yet does not reach  $80\%$ . Figure C.36 displays the top three models' average accuracy for each task. In the PN-P (PN-basic) task, the leading models in average accuracy are GPT-4 at  $13.6\%$ , GPT-3.5-Turbo at  $7.4\%$ , and Llama2 (70B) at  $4.2\%$ , with GPT-4 and manual CoT securing the highest accuracy at  $42.3\%$ . This result indicates the task solvability is challenging as the top model-prompt pair's performance surpasses the random guess but is below  $80\%$ . In the PN-P (PN-hard) task, the top performers in average accuracy are GPT-4 at  $14.3\%$ , GPT-3.5-Turbo at  $8.7\%$ , and Llama2 (70B) at  $5.8\%$ , with GPT-4 and manual CoT reaching the highest at  $58.0\%$ , again suggesting the solvability of the task is challenging as the top model-prompt pair's performance is greater than random guess but falls short of  $80\%$ . Upon comparing the tasks, the variance of solvability is negligible, with the top model's average accuracy varying slightly from  $13.6\%$  to  $14.3\%$  (a  $0.7\%$  difference) and the highest accuracy by the top model-prompt pairs ranging from  $42.3\%$  to  $58.0\%$  (a  $15.7\%$  difference), signifying a considerable variance of model's top performance. GPT-4 not only is the leading model in terms of average performance but also hosts the top model-prompt pairs across all tasks. Similarly, GPT-3.5-Turbo and Llama2 (70B) consistently rank as the second and third most effective models, respectively, in terms of average accuracy across both tasks. As a prompt, manual CoT also hosts top model-prompt pairs across all tasks.

3) Stability: The three most stable models, characterized by the lowest model volatility, are Wizardcoder (15B) with a model volatility of 0.0, text-curie-001 with a model volatility of 0.1, and davinci (175B) with a model volatility of 0.3. Conversely, the three models showing the greatest instability across different prompts, indicated by the highest model volatility, are GPT-4 at 15.2, GPT-3.5-Turbo at 11.6, and text-davinci-003 at 9.8, reflecting their pronounced sensitivity to prompt changes. An analysis of stability across individual tasks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f455b9ccadbc785bda6bfedddaae99d55a838094ef784489930288231ccb1d4a.jpg)



Figure 9.117 Language comparison of PN. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


follows. In the PN-P (PN-basic) task, the most stable models are Wizardcoder (15B) with model volatility of 0.0, text-curie-001 with model volatility of 0.2, and Baichuan1-chat (13B) with model volatility of 0.3. The most unstable models in this task are GPT-4 at 12.6, GPT-3.5-Turbo at 10.9, and text-davinci-003 at 9.0. For the PN-P (PN-hard) task, the top three stable models are Wizardcoder (15B) and text-curie-001, both with model volatility of 0.0, and davinci (175B) with model volatility of 0.3. The models exhibiting the most instability are GPT-4 at 17.9, GPT-3.5-Turbo at 11.6, and text-davinci-001 at 10.4. Across both tasks, Wizardcoder (15B) and text-curie-001 consistently rank as the most and second-most stable models, respectively, while GPT-4 and GPT-3.5-Turbo are the most and second-most unstable models.

4) Open-Limited Ratio: With a 1:4 ratio of open-access to limited-access models among the top five models, the open-limited gap is moderate.

Then, we analyze prompt gain in PN:

1) Top Gain: Illustrated in Figure 9.116(b), the two prompts leading to the most substantial average accuracy improvements over the basic prompt are 3-shot IcL at  $7.2\%$  and manual CoT at  $6.1\%$ . The largest increase in accuracy relative to the basic prompt is achieved by GPT-4 employing manual CoT, with a significant gain of  $43.0\%$ . A more granular, task-specific analysis follows. Figure C.37 presents the heatmap of gains across all tasks within the scenario. In the PN-P (PN-basic) task, the two prompts yielding the greatest average accuracy enhancements over the basic prompt are 3-shot IcL at  $7.3\%$  and manual CoT at  $4.8\%$ . The most substantial improvement in accuracy against the basic prompt is seen with GPT-3.5-Turbo using manual CoT, marking a gain of  $34.5\%$ . In the PN-P (PN-hard) task, the leading two prompts by average accuracy gain over the basic prompt are manual CoT at  $7.4\%$  and 3-shot IcL at  $7.2\%$ , with GPT-4 utilizing manual CoT demonstrating a significant uplift of  $51.7\%$ . The task evaluation shows a preference for manual CoT in enhancing model accuracy.

2) Exceptions: In this scenario, the leading prompt, 3-shot IcL, shows effectiveness for generating positive average prompt gain with nearly all models except Claude2. Every prompt manages to elevate GPT-3.5-Turbo's

performance beyond the basic prompt level. Within the PN-P (PN-basic) task, 3-shot IcL does not yield a positive average prompt gain with Claude2, yet all prompts are successful in boosting GPT-3.5-Turbo's performance from its basic prompt performance. In the PN-P (PN-hard) task, manual CoT fails to enhance the performance for Baichuan1-chat (13B), InternLM-chat (7B), Qwen (14B), text-ada-001, and Llama2 (70B). However, all prompts are capable of improving GPT-3.5-Turbo's performance over the basic prompt. Across both tasks, GPT-3.5-Turbo benefits from all prompts for positive average prompt gain.

3) Stability: The two most stable prompts are adversarial ignore and adversarial doubt, both with a prompt volatility of 0.7. Conversely, the least stable prompts, demonstrated by the highest prompt volatility, are manual CoT at 11.4 and 3-shot IcL at 7.4. The average model-prompt-gain volatility (AMPGV) of 4.4 shows a low prompt dependence within the scenario. Analyzing stability across individual tasks: In the PN-P (PN-basic) task, the most stable prompts, adversarial ignore, and adversarial doubt, both exhibit prompt volatility of 0.6. The least stable prompts are manual CoT at 10.1 and 3-shot IcL at 7. The task shows a low prompt dependence as evidenced by an AMPGV of 3.8. In the PN-P (PN-hard) task, the most stable prompts in terms of stability are adversarial doubt and adversarial ignore, each with a prompt volatility of 0.8. The least stable prompts, showing the largest prompt volatility, are manual CoT at 13.8 and 3-shot IcL at 7.5. The task has a low prompt dependence with an AMPGV of 4.9. Upon reviewing all tasks, the range of AMPGV, indicating the degree of variance of prompt dependence, spans a narrow spectrum from 3.8 to 4.9. Adversarial ignore and adversarial doubt are the most stable prompts, while manual CoT and 3-shot IcL are identified as the most unstable.

Last, we look into language proficiency in PN:

1) English vs. Chinese: Figure 9.117 reveals that models tend to perform better on the English test set compared to the Chinese test set, with 25 out of 28 models exhibiting superior performance in English over Chinese.

2) Accuracy Difference: The most significant differences in accuracy between English and Chinese, with a preference for English, are seen in GPT-4 (12.9%), GPT-3.5-Turbo (7.7%), and Llama2 (70B) (5.6%). On the other hand, models like InternLM-chat (20B) (0.4%), text-curie-001 (0.1%) demonstrate higher proficiency in Chinese than in English.

Probability of sufficiency. Initially, we delve into model performance in PS:

1) Distribution: Figure 9.105(g) showcases the distribution for all model-prompt pairs regarding the PS, with a median calculated at  $0.0\%$  and the third quartile at  $0.4\%$ . Based on subjective assessments (i.e., human understanding of the PS scenario) and the fact that the third quartile for all tasks within this scenario is less than  $0.5\%$ , we subjectively define the understandability of this scenario as very hard. Figure C.13 details the distribution for each model-prompt pair across specific tasks. In the PS-P (PS-basic) task, the median is  $0.1\%$ , and the third quartile is  $0.5\%$ . Due to the challenging nature of Mathematical-mode tasks and the extremely low score of the median and third quartile, we regard the task understandability as very hard. In the PS-P (PS-hard) task, the median is  $0.0\%$ , with the third quartile at  $0.4\%$ . Likewise, we define the task understandability as very hard. Upon evaluating the differences across tasks, it is observed that median and the third quartile accuracies vary slightly from  $0.0\%$  to  $0.1\%$  and from  $0.4\%$  to  $0.5\%$ , both having nearly zero standard deviations. This indicates that the scenario has a minimally divergent variance of distribution. Notably, the PS-P (PS-basic) task exhibits slightly higher scores in both median and third quartile than the PS-P (PS-hard) task. Moreover, in both tasks, a significant majority of model-prompt pairs (over  $90\%$ ) fall within a  $0\%$  to  $10\%$  accuracy range.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8f22a4058b6525197e1dccefd96f36791cd4ee6b31fbaa8c224b2e4caf05a8c6.jpg)



(a) Model performance of PS


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3e8425eb5e4dfc437653e20500e9ba447c3d1e88e1c4751031e6ce75198357dc.jpg)



(b) Prompt gain of PS



Figure 9.118 Heatmap of PS. The models and prompts are sorted by their averages.


2) Top Accuracy: Illustrated in Figure 9.118(a), the leading three models in this scenario based on average accuracy are GPT-4 at  $12.6\%$ , GPT-3.5-Turbo at  $5.8\%$ , and text-davinci-003 at  $4.6\%$ . The top model-prompt pair is GPT-4 with manual CoT, achieving a score of  $46.8\%$ , indicating that the solvability of this scenario is challenging as the top model-prompt pair exceeds the random guess yet does not reach 80. Figure C.38 provides an analysis of the top three models' average accuracy for each specific task. In the PS-P (PS-basic) task, the highest average accuracies are reported for GPT-4 at  $11.9\%$ , GPT-3.5-Turbo at  $5.5\%$ , and Claude2 at  $3.6\%$ , with GPT-4 and manual CoT forming the best top model-prompt pair at  $41.6\%$ . This outcome signifies that the task solvability is challenging as the top model-prompt pair's performance is greater than a random guess but below  $80\%$ . In the PS-P (PS-hard) task, the top performers in average accuracy are GPT-4 at  $12.8\%$ , text-davinci-001 at  $6.3\%$ , and text-davinci-003 also at  $6.3\%$ , with GPT-4 and manual CoT reaching the highest at  $52.1\%$ , again highlighting the task's challenging solvability as the top model-prompt pair's performance surpasses the random guess but remains under  $80\%$ . Upon examining the tasks, the variance of solvability is negligible, with the top model's average accuracy fluctuating slightly from  $11.9\%$  to  $12.8\%$  (a difference of  $0.9\%$ ), and the peak accuracy achieved by top model-prompt pair ranging from  $41.6\%$  to  $52.1\%$  (a difference of  $10.5\%$ ). This indicates a considerable variance of model's top performance. GPT-4 not only stands out as the leading model in terms of average performance but also forms the most efficient model-prompt pairs combining with manual CoT across all tasks.

3) Stability: There are more than three models with zero model volatility in the scenario. Conversely, the models exhibiting the greatest instability across various prompts, indicated by the highest model volatility, are

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1cdb91d8a3e12a3780bc28b75668aa300c2afbb268a3a5ee1425574e26ea7f51.jpg)



Figure 9.119 Language comparison of PS. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


GPT-4 at 14.6, GPT-3.5-Turbo at 13.5, and text-davinci-003 at 11.2, showcasing their significant sensitivity to prompt variations. An analysis of stability across specific tasks is as follows: In the PS-P (PS-basic) task, a number of models achieve model volatility of 0.0, denoting maximum stability. The models facing the greatest instability, demonstrated by the largest model volatility, are GPT-4 at 11.9, GPT-3.5-Turbo at 11.4, and Vicuna-v1.3 (33B) at 6.7. For the PS-P (PS-hard) task, again, several models report model volatility of 0.0, indicating a high level of stability. The most unstable models are text-davinci-002, text-davinci-003, and text-davinci-001, each with a model volatility of 17.5.

4) Open-Limited Ratio: The ratio of open-access to limited-access models among the top five models with the highest average accuracy in the entire scenario is 0:5, indicating a large open-limited gap.

Following this, we evaluate prompt-gain in PS:

1) Top Gain: Illustrated in Figure 9.118(b), the two prompts leading to the highest average accuracy improvements over the basic prompt are manual CoT at  $6.9\%$  and adversarial ignore at  $0.2\%$ . The most significant increase in accuracy compared to the basic prompt is achieved by GPT-3.5-Turbo with manual CoT, registering a gain of  $38.9\%$ . A more detailed, task-specific analysis is conducted next. Figure C.39 presents the heatmap of gains across all tasks in the scenario. In the PS-P (PS-basic) task, the leading two prompts by average accuracy improvement over the basic prompt are manual CoT at  $4.3\%$  and 0-shot IcL at  $0.5\%$ , with the most substantial gain observed with GPT-3.5-Turbo using manual CoT, indicating a rise of  $34.9\%$ . In the PS-P (PS-hard) task, the top two prompts for average accuracy gain over the basic prompt are manual CoT at  $9.5\%$  and adversarial ignore at  $0.2\%$ , with text-davinci-002 employing manual CoT demonstrating the most significant improvement, a leap of  $49.5\%$ . Across both tasks, manual CoT is favored for achieving the highest average model gain and the maximum gain in all model-prompt pairs.

2) Exceptions: The most high-performing prompt in the scenario, manual CoT, shows effectiveness with the majority of models in generating positive average prompt gain, but excluding text-ada-001, Qwen (14B), and Llama2 (70B). Every prompt is capable of enhancing GPT-3.5-Turbo's performance beyond its basic

prompt performance. However, no prompt manages to elevate Qwen (14B)'s performance above the basic prompt. In the PS-P (PS-basic) task, manual CoT cannot give a positive average prompt gain to text-ada-001, text-davinci-001, Qwen (14B), and Llama2 (70B). In the PS-P (PS-hard) task, manual CoT fails to be effective with text-ada-001, Qwen (14B), and Llama2 (70B). All prompts, however, can enhance the GPT-3.5-Turbo's performance over the basic prompt, with Qwen (14B) again showing no improvement from any prompt in the task. Across both tasks, the preferred prompt, manual CoT, does not improve accuracy for text-ada-001 over its basic prompt performance.

3) Stability: Regarding stability within the scenario, the two most stable prompts, exhibiting the smallest prompt volatility, are adversarial doubt at 0.6 and adversarial ignore at 0.7. On the other hand, the most unstable prompts, identified by the largest prompt volatility, are manual CoT at 12.7 and 3-shot IcL at 1.8. The average model-prompt-gain volatility (AMPGV) is 2.9, indicating a low prompt dependence across the scenario. Stability is further assessed on a task-specific basis: For the PS-P (PS-basic) task, the most stable prompts are adversarial doubt and 0-shot CoT, both with a prompt volatility of 0.6. Conversely, the least stable prompts are manual CoT at 9.6 and 0-shot IcL at 2.5. The task showcases a low prompt dependence with an AMPGV of 1.8. In the PS-P (PS-hard) task, the most stable prompts in terms of stability are adversarial doubt and adversarial ignore, each with a prompt volatility of 0.8. The least stable prompts, marked by the highest prompt volatility, are manual CoT at 18.2 and 1-shot IcL at 1.9. The task reveals a low prompt dependence with an AMPGV of 3.9. Upon reviewing all tasks in the scenario, the range of AMPGV, reflecting the variance of prompt dependence, spans a narrow spectrum from 1.8 to 3.9. Adversarial doubt is the most stable prompt across tasks, while manual CoT is consistently the most unstable.

Finally, we measure language proficiency in PS:

1) English vs. Chinese: Figure 9.119 indicates that models generally achieve better results on the English test set compared to the Chinese test set, with 18 out of 28 models showing superior performance in English over Chinese.

2) Accuracy Difference: The most significant performance disparities between English and Chinese, with a preference for English, are seen with GPT-4 (7.2%), GPT-3.5-Turbo (3.4%), and text-davinci-001 (3.1%). On the flip side, text-ada-001 (0.2%) is the only model demonstrating higher proficiency in Chinese relative to English.

Causal explanation generation. Regarding model performance in CEG: 1) Distribution: Figure 9.105(h) illustrates the distribution for all model-prompt pairs, highlighting a median of  $35.0\%$  and a third quartile of  $40.8\%$ . As CEG is not a close-ended scenario, we choose to evaluate its understandability objectively. Considering that most models exhibit stronger performance in processing Natural-mode tasks and the median of the CEG scenario is over  $30\%$ , we categorize its understandability as easy.

2) Top Accuracy: As shown in Figure 9.120(a), Claude2, GPT-3.5-Turbo, and GPT-4 are the top three models by average accuracy. Claude2, using EF, reaches a peak accuracy of  $63.4\%$ , positioning the solvability of this scenario as challenging since the top model-prompt pair does not achieve an accuracy of  $80\%$ . 3) Stability: The models demonstrating the greatest variance in response to different prompts, as indicated by the model volatility described in Section 6.3, include Koala (13B) and Llama2-chat (70B). In contrast, the models with the least variance are InternLM-chat (20B), Baichuan1 (7B), and Qwen (7B). 4) Open-Limited Ratio: Among the top five models, a 2:3 ratio of open-access to limited-access models indicates a small open-limited gap.

Regarding prompt gain in CEG: 1) Top Gain: Figure 9.120(b) points out adversarial doubt and manual CoT as

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c3812dd9e01db422b564d14deeb9818515f881bdc8d39f00fd9a0f160d0f1b1c.jpg)



(a) Model performance of CEG


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/243280cfc7c0b8bad4fa4fea9736504c785c5760791e54409c19f314b6d57a5f.jpg)



(b) Prompt gain of CEG



Figure 9.120 Heatmap of CEG. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5cd97b4438714be0b395d28664af5a93f943d65e8bf5d9c5af5eda8cd31f8b40.jpg)



Figure 9.121 Language comparison of CEG. The dark legend signifies the average performance of the model on an English test set, whereas the light legend denotes the average performance of the model on the Chinese test set. The yellow legend indicates a model trained exclusively on English datasets, while the blue legend represents a model trained on both English and Chinese datasets.


the top two prompts for average accuracy gain over the basic prompt, with Vicuna-v1.3 (33B) using 0-shot IcL showcasing the most considerable increase of  $12.7\%$ . 2) Exceptions: The most high-performing prompt, adversarial doubt, does not align well with models including Koala (13B) and Llama2 (70B) for generating a positive average prompt gain. Nonetheless, all prompts manage to improve the performance of babbage (1.3B) and Qwen (7B) above their basic prompt performance, while most of the models in the Llama2 series are an exception where no prompt leads to enhancement. 3) Stability: The most stable prompts, with the lowest prompt volatility, are 0-shot IcL and adversarial ignore, whereas the least stable prompts are adversarial doubt and manual CoT. This scenario exhibits a medium prompt dependence, as reflected by the average model-prompt-gain volatility (AMPGV) of 5.8.

In terms of language proficiency in CEG, 1) English vs. Chinese: as highlighted in Figure 9.121, the performance of models on the Chinese test set is better than the one on the English test set, with only 2 out of 28 models performing better in English than in Chinese. 2) Accuracy Difference: Significant discrepancies in performance between English and Chinese, favoring English, are observed in models like Koala (13B)  $(5.6\%)$ , and Vicuna-v1.3 (33B)  $(0.3\%)$ . Conversely, models such as Baichuan1-chat (13B)  $(32.2\%)$ , Llama2 (7B)  $(17.6\%)$ , and curie (6.7B)  $(17.5\%)$  show greater proficiency in Chinese compared to English.

# 10 Related Work

If I have seen further it is by standing on the shoulders of Giants.

Isaac Newton, 1675

In this section, we review the foundational efforts associated with the construction of CaLM. Our discussion is organized into four key areas: Advancements in Language Models (Section 10.1), Evaluations of Language Models' General Abilities (Section 10.2), Evaluations of Language Models' Causal Reasoning Abilities (Section 10.3), and Causal Benchmark Datasets (Section 10.4).

# 10.1 Advancements in Language Models

Language models have achieved remarkable success today, reflecting the persistent efforts of numerous research over time (Shannon, 1948; Goldman-Eisler, 1958; Jelinek, 1976, 1998; Rosenfeld, 2000; Bengio et al., 2000; Mikolov et al., 2010; Devlin et al., 2018; Radford et al., 2018; Radford et al.; Raffel et al., 2020; Brown et al., 2020; OpenAI, 2022, 2023; Touvron et al., 2023; Anthropic, 2023; Meta, 2024). Zhao et al. (2023) divide the evolution of language models from the 1990s to today into four primary stages: statistical language models (SLM) from 1990s to 2013, neural language models (NLM) from 2013 to 2018, pre-trained language models (PLM) from 2018 to 2020, and large language models (LLM) from 2020 to now. Moreover, Yang et al. (2023b) provide a clear "evolutionary tree". It outlines the most influential language models from 2018 to now, and classifies them by the model architecture (i.e., non-transformer based, decoder-only, encoder-only, and encoder-decoder). Given that CaLM evaluates only models launched after 2020, we will concentrate our review on the advancements in language models since that year.

The introduction of GPT-3 (Brown et al., 2020) marked a significant advancement in text generation capabilities, demonstrating considerable proficiency and achieving excellent results through in-context learning (Brown et al., 2020; Dong et al., 2022). Following the release of GPT-3, OpenAI introduced InstructGPT (Ouyang et al., 2022) in 2022, building upon GPT-3's foundation to exhibit superior capabilities in reasoning and alignment with humans. Subsequently, in November 2022, the unveiling of ChatGPT (OpenAI, 2022) gained widespread attention for its advanced capabilities in diverse tasks such as story writing, question answering, conversation understanding, and even emotion understanding, code generation, and logical reasoning. This was followed by the launch of GPT-4 (OpenAI, 2023), representing a significant leap forward in artificial intelligence. GPT-4's advanced features cater to a wide range, fostering creativity and innovation by assisting in idea generation, code suggestion, and design conceptualization. While these models remain limited-access, Meta's release of Llama2 (Touvron et al., 2023) marked a notable development in the open-access model landscape. Meta's decision to make the weights and tokenizers of Llama2-series models publicly available is considered a pivotal moment for the open-source community, enabling broader experimentation and customization across various domains. Based on Llama2, Meta recently introduced Llama3 (Meta, 2024), which boasts substantial performance enhancements.[37] We are confident that it will continue to propel the advancement and growth of language models.

# 10.2 Evaluations of Language Models' General Abilities

As language models rapidly evolve, numerous benchmarks have been developed to objectively evaluate their performance. Some benchmarks are widely recognized for their extensive scope. MMLU (Hendrycks et al., 2020) is designed to test if models have extensive world knowledge applicable to multi-task situations. It encompasses 57 tasks across various domains including microeconomics, computer science, and medicine. HELM (Liang et al., 2022) has established an abstract taxonomy that spans scenarios and metrics. Meanwhile, it provides a comprehensive evaluation of language models' capabilities across 16 core scenarios (e.g., question answering, summarization), 21 additional scenarios (e.g., biases, disinformation generation), and 7 metrics (e.g., accuracy, calibration, robustness). It is fair to say that HELM has also played a crucial role in inspiring the development of CaLM. BIG-Bench (Srivastava et al., 2023) is a comprehensive benchmark consisting of 204 tasks, created by 450 authors from 132 different institutions. It focuses on tasks that were thought to exceed the abilities of language models at that time, including areas like math, social biases, and software development. Building on BIG-Bench, BIG-Bench Hard (BBH) is subsequently developed (Suzgun et al., 2023). BBH consists of the 23 most difficult tasks in the BIG-Bench, and solving these tasks generally requires multi-step reasoning. KOLA (Yu et al., 2024) introduces a thorough assessment of language models' world knowledge from the perspective of cognitive abilities, breaking it down into four levels: memorization, understanding, applying, and creating. In addition to the aforementioned efforts, there are numerous other excellent benchmarks that effectively evaluate language models, including GLUE (Wang et al., 2018), SuperGLUE (Wang et al., 2019), GLUE-X (Yang et al., 2023c), PandaLM (Wang et al., 2024b), and Xiezhi (Gu et al., 2024). Given the constraints of space and the continuous development of new benchmarks, it is not feasible to cover all benchmarks comprehensively. However, an effort by Chang et al. has been instrumental in providing a thorough overview of language model evaluations. They have meticulously cataloged current evaluation practices, methods, and benchmarks for language models, and maintain a website<sup>38</sup> to share the latest research findings, ensuring accessibility and up-to-date information for the community.

# 10.3 Evaluations of Language Models' Causal Reasoning Abilities

It was not until 2022 that research began to increasingly focus on evaluating the causal reasoning abilities of language models. These exploratory efforts have inspired our development of CaLM. We will proceed to detail each of these endeavors in turn.

There is already some research focusing on how language models manage causal tasks related to causal discovery. Hobbhahn et al. (2022) investigate how language models understand causal relationships, highlighting that the models' responses are highly Willig et al. (2022) design "intuitive physics" and "causal chain" questions to evaluate language models' causal reasoning abilities. Their findings indicate that while language models are adept at handling commonsense questions, they struggle to infer causal relationships from data. Long et al. (2022) explore the potential of language models to accelerate the construction of causal graphs, demonstrating that these models can assist in generating relatively simple graphs. Gao et al. (2023a) conduct a comprehensive evaluation of GPT-3.5-Turbo's causal reasoning capabilities, focusing primarily on causal scenarios such as PCD, ECI, and CEG. They also experiment with various prompts to enhance the model's performance in these scenarios. Their results show that GPT-3.5-Turbo performs well in the CEG scenario, where it is required to explain causal relationships. However, its performance is less effective in the more complex PCD and ECI scenarios.

In addition to causal discovery, various studies assess language models across the different levels of the causal ladder. Kiciman et al. (2023) conduct a detailed analysis of language models' performance in various causal reasoning tasks (e.g., causal discovery, actual causality, and causal judgments). Their findings suggest that language models can complement human expertise in causal analysis, significantly reducing the manpower needed. Zhang et al. (2023a) evaluate the performance of language models in answering three different types of causal questions (i.e., identifying causal relationships using domain knowledge, discovering new knowledge from data, and quantitative estimating of the consequences of actions). They contend that language models have not yet reached a level where they can independently uncover new knowledge or make critical decisions. Jin et al. (2024) propose a challenging task named CORR2CAUSE, along with a dataset to evaluate whether language models can deal with pure causal inference problems. They reveal the models' deficiencies in causal inference ability and generalizability. Despite considerable efforts, these studies mostly focus on specific causal tasks, and a comprehensive understanding of language models' causal reasoning capabilities remains a challenge.

# 10.4 Causal Benchmark Datasets

Causal datasets can be categorized into two main types based on the underlying causal reasoning tasks they support: datasets for causal inference, which include tasks such as association, intervention, and counterfactual reasoning, and datasets for causal discovery, which focus on identifying causal relationships from data. Within the category of causal inference, there are two distinct subcategories: datasets tailored for inferring causality within causal graphs and datasets designed for inferring causality between specific treatments and outcomes.

Datasets for causal inference within causal graphs. For datasets of this nature, the underlying causal graph of variables is fully or partially provided. The associated task involves solving Rung 1 (associative inference), Rung 2 (intervention inference), and Rung 3 (counterfactual inference) queries based on the provided graph, as well as statistical data and other auxiliary information. An example of such a dataset is the CLADDER dataset (Jin et al., 2023a), which comprises 10k samples primarily intended for assessing the causal reasoning abilities of language models. The data generation process unfolds as follows: 1) A graph is selected from several classic causal graphs (e.g., confounding, mediation, diamond), along with a concrete query type (e.g., conditional probability, ATE, NIE); 2) Symbolic questions (e.g., Abstract Reasoning (AR) (Section 3.3.3), Frontdoor Adjustment Set (FAS) (Section 3.5.3)) and ground-truth answers are obtained through an oracle causal inference engine; 3) A story is sampled for the graph, and the entire question is verbalized. CLADDER exhibits some notable limitations. Firstly, CLADDER has a limited variety of graphs, only consisting of approximately 10 graphs derived from textbooks (Pearl, 2009; Pearl et al., 2016; Peters et al., 2017; Pearl & Mackenzie, 2018; Neal), with each graph containing only three to four nodes. Secondly, the stories are selected from a manually constructed story set of limited size. Thirdly, it only supports the English language. In response to these limitations, we have developed a new dataset that builds upon and enhances CLADDER in various ways. The improvements include a broader variety of graph types, expanded scale, support for both Chinese and English languages, enriching storytelling through LLM-based story generation, and adding a range of causal scenarios, causal tasks, and query types. These improvements significantly extend the dataset's applicability and depth, facilitating more comprehensive research in causal reasoning across diverse contexts.

Datasets for causal inference between specific treatment and outcome. This type of dataset consists of samples containing treatment, outcome, and covariates (also known as features). These samples can be collected from real-world observations, investigations, experiments, or simulations, yet the causal connections between variables, represented by the underlying causal graph, often remain undetermined. The corresponding causal

task typically involves exploring the cause effect of the treatment variable on the outcome variable. The topics explored by datasets of this nature are primarily distributed across medical (e.g., IHDP, Twins, LBIDD, TCGA), social networks (e.g., News, BlogCatalog, Flickr), and personal career development (e.g., Jobs).

Specifically, IHDP is initially compiled by Hill (2011). It utilizes raw data from the Infant Health and Development Program, a randomized controlled study evaluating the effect of specialist home visits on the cognitive test scores of premature infants. In the Twins dataset (Louizos et al., 2017), the treatment variable and outcome variable are the birth weight of twins and mortality in the first year, respectively, and it encompasses 50 covariates such as parental age, education, and health complications. LBIDD (Shimoni et al., 2018) is a semi-synthetic dataset used for ACIC 2018 based on real-world medical measurements taken from Linked Birth and Infant Death Data. In TCGA (The Cancer Genome Atlas) dataset (Weinstein et al., 2013), the treatment options are medication, chemotherapy, and surgery and the outcome is the risk of cancer recurrence after receiving the treatment. The MVICU (Schwab et al., 2020) benchmark assesses patients' responses to various configurations of mechanical ventilation in the intensive care unit. The News dataset (Schwab et al., 2020) consists of 5000 randomly sampled news articles from the NY Times corpus, where the treatment are diverse viewing devices such as smartphones, desktops, and others, the outcome is the reader's opinion of the news item and the samples are news articles that consist of word counts. BlogCatalog and Flickr (Guo et al., 2020) are causal inference datasets with observational data from social networks. The Jobs dataset (LaLonde, 1986) examines the causal effect of job training on income and employment status.

Datasets for causal discovery. At present, the datasets for evaluating the causal discovery capabilities of language models rely solely on semantics. The model employs its pre-existing knowledge and reasoning skills to identify causal relationships from natural language expression. However, there are no datasets specifically crafted for language models to infer causal relationships from data. We focus on introducing the various datasets employed in CaLM. COPA (Roemmele et al., 2011) focuses on determining causal relationships, consisting of a total of 1000 queries. Each query presents a premise along with two potential causes or effects. E-CARE (Du et al., 2022) includes over 21,000 multiple-choice questions centered on causal reasoning. It offers detailed conceptual explanations for each question. CTB (Mirza et al., 2014) contains queries that capture causal relationship between events. The dataset consists of 6,813 events and 318 causal event pairs. ESC (Caselli & Vossen, 2017) represents a novel dataset designed to facilitate the identification of temporal and causal relations. In this dataset, one event elucidates or provides a rationale for the happening of the other event within the duo. MAVEN-ERE (Wang et al., 2022) introduces a substantial collection of 57,992 causal relations, making the task of ERE on it complex and demanding.

# 11 Gaps in CalM

We will start with a detailed review of the four modules of CaLM, examining the aspects that our concrete implementation lacks. Additionally, we will thoroughly summarize the models that have not yet been evaluated in CaLM. This section will be structured from the following five perspectives: Gaps in Causal Targets (Section 11.1), Gaps in Adaptations (Section 11.2), Gaps in Metrics (Section 11.3), Gaps in Errors (Section 11.4), and Gaps in Models (Section 11.5).

# 11.1 Gaps in Causal Targets

Given that a causal target is defined as a tuple composed of (causal task, mode, language), it is essential to begin our analysis by examining the gaps in each of these components.

Gaps in causal tasks. Given that our tasks extend across the four levels of the causal ladder, we will systematically identify gaps within each of the four rungs. (1) Causal discovery. Firstly, as mentioned in Rung 0: Causal Discovery (Section 3.3), our CaLM primarily focuses on pairwise causal discovery. However, for further research and broader applications, evaluating the model's ability to perform causal discovery on full graphs would be highly beneficial. This entails exploring how well the model can uncover causal relationships among multiple variables simultaneously, rather than just pairwise relationships. By expanding our investigation to encompass full-graph causal discovery, we can deepen our understanding of language models' capabilities for complex causal structure inference. Secondly, all of our causal discovery tasks do not involve the Mathematical mode; instead, they focus on identifying causal relationships from the semantic level in the Natural mode or causal graphs provided in a Symbolic mode. However, addressing causal discovery in this manner can be described as "metaphysical" and not fundamentally substantial. A more intrinsic approach would involve evaluating the model's capability to discover causal relationships through computation, deriving insights directly from data. It could be argued that only when models also perform well on this type of task can we say that language models have fundamentally solved the challenge of causal discovery. (2) Association. While our evaluation considers all four rungs of the causal ladder, the Association (Rung 1) has not been a central point. This rung primarily deals with the statistical dependence between random variables, which is calculable from observational data. The lack of emphasis on this level should not be interpreted as diminishing its importance. On the contrary, enhancing the model's performance on association tasks could lead to significant societal benefits. The limited focus on this rung stems from constrained resources, which have restricted our ability to fully explore this aspect. (3) Intervention. We endeavor to comprehensively consider scenarios at this level, yet numerous aspects remain to be explored in the future. For instance, we could think about assigning real-world meanings to variables in tasks typically presented in a Symbolic mode for causal graphs like BAS, FAS, and IV. For instance, in healthcare, understanding the causal pathways between lifestyle choices and disease outcomes could lead to more personalized and effective treatment plans. In economics, accurately identifying the causal impact of policy changes on economic indicators could guide more informed policy-making. By grounding causal inference tasks in real-world contexts, we can ensure that the models we develop are not only technically sophisticated but also practically relevant and ethically sound. (4) Counterfactual. Our study does not evaluate several scenarios, including the probability of necessity and sufficiency (PNS), probability of disablement (PD), and probability of enablement (PE) (Pearl, 2009), because they are not the most fundamental concepts compared to PN and PS. However, it is without a doubt that understanding the capability of language models to grasp these concepts is also important, which we will leave for future exploration.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a7826f28f8c4ec2ad1ea6716bd09738a3dd2ddcb203faafd8ca326e460eb894e.jpg)



Figure 11.1 Example of generation (code causality) (Lu et al., 2024).


Gaps in modes. In this paper, we primarily focus on the evaluation in the text mode. With the advancement in multi-modal language models (Team et al., 2023; OpenAI, 2024), there has been a growing interest in exploring other modes, such as code (Roziere et al., 2023; Li et al., 2023f), image (Li et al., 2023d; Liu et al., 2024a), and video (Li et al., 2023e; Chen et al., 2023a). Lu et al. (2024) provide examples of these modalities in their technical report, as shown in Figures  $11.1\sim 11.3$ . Our framework is designed to be flexible, accommodating various modes, and we plan to gradually incorporate these into our evaluation process.

# Causal Discovery

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1f94eab49f5f3acae3350bcd6f1231cb3b38abe2cac6c0312b8b50588a49b194.jpg)



Question: In the picture, what events are caused by fire?


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/faf334df0e6e4757d19df29a8af402f9b4a79e9a1bcee41e1c5082c18a71d1d6.jpg)


# LLaVA

In the picture, a fire has caused significant damage to a building, resulting in a fire-damaged structure. The fire has also caused a fire hydrant to be opened, which is spraying water onto the scene. Additionally, there are firefighters present, who are working to extinguish the fire and protect the surrounding area.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f87cd4b0db4866758e27119a035243a3a2f40e41a62d53cd1c8478f974d38af2.jpg)


# Gemini Pro

In the picture, the fire caused the building to be engulfed in flames and the firefighters are trying to put out the fire. The fire also caused the roof of the building to collapse.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2a85d3ed6e8af60d71d9eac95771c3d7b89b53ec692f55c3eebc12a954093b7c.jpg)


# GPT-4

The image depicts a severe building fire with active firefighting efforts underway. The fire has fully engulfed part of the building, with flames visibly consuming the roof and upper floors. The intensity of the fire has caused structural damage, as evidenced by the collapsing roof and the flames bursting out of the windows. Firefighters are seen directing water streams towards the flames in an attempt to control and extinguish the fire. The events caused by the fire include:

1. Structural damage to the building, with parts of the roof and upper stories visibly disintegrating.

2. Potential danger to any occupants that might have been inside, although the building appears abandoned.

3. A risk to surrounding buildings due to the potential spread of flames.

4. The engagement of emergency services to address the situation, safeguard the area, and attempt to put out the fire.


Figure 11.2 Example of causal discovery (image causality) (Lu et al., 2024).


Gaps in languages. our evaluations have so far only included Chinese and English. However, given the global adoption of language models, it is imperative to expand our scope to include more languages. Languages such as German and French, among others, should be incorporated into our evaluation framework to ensure broader language coverage and to assess the effectiveness of language models worldwide more comprehensively.

# 11.2 Gaps in Adaptations

With technological advancements, we are witnessing a proliferation of various adaptation strategies. Given that the approach to adaptations we considered in CaLM is limited to prompting, this leaves a wide array of opportunities for further research. (1) Finetuning. This method involves adjusting all the parameters of a pre-trained language model to tailor it for a specific task, which incurs significant resource expenditure. Consequently, the capacity to undertake such extensive adaptation is confined to a relatively small group of well-resourced organizations. (2) Lightweight-finetuning. Due to the enormous number of parameters in language models, finetuning all parameters for downstream tasks requires significant computational resources. To mitigate costs, various lightweight-finetuning methods have been proposed, aiming to adapt the model to downstream tasks by training only a small fraction of the parameters. A representative method among these is LoRA (Hu et al., 2021), which introduces the product of low-rank matrices as trainable parameters alongside the existing weight matrix. This approach effectively captures parameter variations, thereby minimizing computational demand while maintaining strong performance in targeted tasks. LoRA has

# Counterfactual Reasoning

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5021502e80e814bd4d2fbf9feceef0091a2531d9eefa04cde72438a744464934.jpg)


Question: If there were no candles, would the cake fall to the ground?

# Gemini Pro

No, the cake would not fall to the ground if there were no candles. The candles are not supporting the cake. The cake is supported by the plate or surface it is sitting on.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d1f846e6a7f1fc29aa54c2449f656e190693ee0ed132304af758658d00c08285.jpg)


# GPT-4

Based on the frames provided, it appears to be a sequence of images that could be from a video clip showing a group of people and a cake with candles. The presence or absence of candles on a cake would have no effect on the physical state of the cake itself, such as whether it falls to the ground. The cake would only fall to the ground if it were dropped, knocked over, or if the support it was on failed. The candles are simply decorations and do not provide any structural support to the cake.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/834e52102a355247446a72e30f070402858a0b96ebaf362e9aa144698d484daf.jpg)


# LLaVA

No, the cake would not fall to the ground if there were no candles. The cake is placed on a dining table, and the presence of candles is not the only factor that keeps it in place. The table's surface provides support and stability for the cake, preventing it from falling. The candles are typically used for decoration and to celebrate a special occasion, but they do not serve a functional purpose in keeping the cake upright.


Figure 11.3 Example of counterfactual reasoning (video causality) (Lu et al., 2024).


garnered widespread attention in both the corporate and research communities, inspiring a series of related methods including LongLoRA (Chen et al., 2023d), QLoRA (Dettmers et al., 2024), and LoRAFA (Zhang et al., 2023c). (3) **Prompting.** The burgeoning field of language models has increasingly emphasized the efficiency of prompting methods, which forego traditional parameter updates for a streamlined approach. This trend is exemplified by the adoption of prompting strategies such CoT and IcL we employed in CaLM, whose efficacy is substantiated by extensive research. Yao et al. (2024) introduce the Tree of Thoughts (ToT) to overcome the challenges in tasks that demand deep analytical thinking and strategic anticipation. Zhou et al. (2022) develop a method called Least-to-most Prompting, which deconstructs intricate problems into manageable sub-problems, addressing each in succession. Moreover, the field has seen the development of other innovative prompting strategies such as Self-consistency (Wang et al., 2023a) and Progressive-hint prompting (Zheng et al., 2023a). Beyond these specific methods, considerable potential exists for exploring optimal adaptation strategies tailored to various causal targets, models, languages, and other factors. Customizing adaptation techniques to specific causal reasoning tasks or modifying them to align with the characteristics of different language models could substantially enhance their effectiveness. Furthermore, considering diverse linguistic nuances and cultural contexts can enhance their applicability and impact across various domains and populations. Exploring and refining these adaptation approaches is essential for maximizing the utility and robustness of

# Replication Output

# Input:

Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Sslg has a direct effect on gjot. Sslg has a direct effect on hlky. Etat has a direct effect on gjot. Etat has a direct effect on hlky. Gjot has a direct effect on hlky.

Instruction: Consider the natural indirect effect (NIE) of sslg on gjot.

Question: Suppose sslg is held constant and the mediator changes to whatever value it would have attained under sslg changing to be low, would qjot have been more likely to be high?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/7824d5be7a5ea8e04cc6a47d11b29f9da819f879bc77c1b3ad5b52deaed42537.jpg)


{"ANSWER": "Yes", "PROB": "0.1234"}

Ground truth: {"ANSWER": "No", "PROB": "o.0ooo"}


Figure 11.4 Example of replication output.


models in real-world applications.

# 11.3 Gaps in Metrics

While evaluating the performance of language models, we acknowledge certain metrics that are overlooked but can provide valuable insights into the models' capabilities. These metrics go beyond conventional evaluations and shed light on specific scenarios where standard metrics may fall short.

Replication Ratio. To address numerical computation issues, we employ a standardized format that specifies the calculation result at the end of our prompt: "Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB: "0.1234"}." Despite this approach, empirical evidence suggests that several models encounter confusion with {"ANSWER": "Yes", "PROB: "0.1234"}, causing them to replicate the prompt's results (as exemplified in Figure 11.4). In order to assess a model's vulnerability to the prompt, it would be preferable to define replication ratio to measure the tendency of a model to reproduce the prompt's results when confronted with numerical computation challenges. It is calculated by comparing the number of instances where the model correctly generates the expected response in the prescribed JSON format to the total number of instances tested. A higher replication ratio suggests a model's susceptibility to reproducing predefined outcomes rather than independently solving numerical problems.

Fairness. To explore the fairness issue in language models, we consider integrating tasks that involve causal and counterfactual fairness assessments (Kusner et al., 2017), particularly using factors like gender and race as perturbative elements. For example, as shown in Figure 11.5, counterfactual fairness is operationalized by generating counterfactual data through perturbations applied to existing test examples. These perturbations involve modifying terms related to specific groups with alternatives that reflect changes in the speaker's properties (e.g., Standard American English vs. African American English) and subject properties (race and binary gender) within the text. Our approach to measuring counterfactual fairness is limited to text classification and question-answering tasks, ensuring the relevance and validity of the perturbations. While we do not extensively explore these questions in this work, we acknowledge their significance in the technical,

# Counterfactual Fairness

# Input:

To whom did Queen Victoria lament that marriage was a shocking alternative to her mother's prescence? Though queen, as an unmarried young woman Victoria was required by social convention to live with her mother, despite their differences over the Kensington System and her mother's continued reliance on Conroy. Her mother was consigned to a remote apartment in Buckingham Palace, and Victoria often refused to see her. When Victoria complained to Melbourne that her mother's close proximity promised "torment for many years", Melbourne sympathised but said it could be avoided by marriage, which Victoria called a "schocking alternative". Sheshowed interest in Albert's education for the future role he would have to play as her husband, but she resisted attempts to rush her into wedlock.

Question: What was the problem between Queen Victoria and her mother?

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6c6a3499e2ff7fde83f7d5197155f2f64470d92e53d08aced7af5263c425ec19.jpg)


Victoria and her mother had a strained relationship due to their differences over the Kensington System and her mother's continued reliance on Conroy. Victoria was required by social convention to live with her mother, despite their disagreements, which caused her distress and led her to complain to Melbourne that her mother's close proximity promised "torrent for many years"


Figure 11.5 Example of counterfactual fairness.


# Causal Hallucination

# Input:

Event A: Thunder appears in the sky at once.

Event B: The clouds are very thick in the sky.

Question: Is there a causal relationship between Event A and Event B? Answer (Yes or No?):

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ab47f219f022ceb9decc2ad2e5fac1608d4effcfe53e7baf1835e134b3cb21a0.jpg)


Ground truth: No


Figure 11.6 Example of causal hallucination.


social, and political dimensions of language technologies. We emphasize the need to consider norms and values expressed by language agents for a comprehensive understanding of fairness and equity in models.

Reliability. As shown in Figure 11.6, in our experiments, we observe that existing language models often exhibit hallucination issues, characterized by outputs that deviate from established world knowledge or fail to adhere faithfully to provided instructions. Further investigation into these phenomena will contribute to a better understanding of the reliability of language models.

Safety. In the context of causal tasks, the introduction of toxicity - which includes unlawful language, harmful content, pornography, and violence - adds an additional layer of complexity to the study. Previous studies have demonstrated that language models can generate toxic text when prompted, even if the original text is not inherently toxic (Gehman et al., 2020; Dhamala et al., 2021). This includes instances where the generated text contains hateful language directed towards specific groups. Toxicity, in this context, serves as an umbrella term covering related concepts such as hate speech, violent speech, and abusive language. It is essential to recognize the nuanced nature of toxicity, acknowledging that its determination often requires greater contextual understanding and clarity on who determines what constitutes toxic content.

# 11.4 Gaps in Errors

Due to the time constraints, it is impractical to exhaustively cover all possible models and the diverse types of errors they may generate. According to existing research (Liu et al., 2023a; Sawada et al., 2023), several other types of errors to which models are prone include (1) struggling to clarify ambiguous meanings, (2) scope errors (e.g., misattributing the relationship between predicates and subjects), (3) logical errors (e.g., distorting the meaning of statements, assuming a premise without evidence, and denying a hypothesis without justification), (4) incomplete response (e.g., language model only reply to portion of a question and overlook other portion). These types of errors underscore the importance of ongoing research and development efforts aimed at addressing the diverse challenges inherent in language models, thereby enhancing their robustness, reliability, and overall performance across various tasks and domains.

# 11.5 Gaps in Models

In our analysis, the models omitted from evaluation are categorized into two main groups. Firstly, there are models that are accessible to us but not evaluated, primarily because they were released in close proximity to the release of this work. Examples include Gemini Pro (Team et al., 2023), Mistral (Jiang et al., 2023), Llama3 (Meta, 2024), Claude3 (Anthropic, 2024), and newer versions of OpenAI models. We anticipate that the exclusion of these models is temporary and hope to reliably evaluate openly released models in the future.

Another category includes models tailored for specific languages or domains (Liu et al., 2021; Bolton et al., 2022; Azerbayev et al., 2023; Gan et al., 2023), such as FinBERT (Liu et al., 2021) for financial text mining and PubMed GPT (Bolton et al., 2022) for biomedical tasks. These models are designed and trained with a focus on a particular linguistic context, making them specialized for certain applications. Access to these models may be restricted, limiting their utilization in broader linguistic contexts.

# 12 Limitations and Future Work

Although we diligently design, implement, experiment with, and analyze our CaLM to the best of our ability, we must openly admit that our project has limitations and significant potential for improvement. Apart from the discussions presented in Gaps in CaLM (Section 11), a thorough examination of CaLM is essential to fully understand its constraints and to outline the direction for future work. This section is dedicated to this purpose, focusing our analysis branching on two main areas: Limitations of Concrete Implementation (Section 12.1) and Limitations of Evaluation Results (Section 12.2).

# 12.1 Limitations of Concrete Implementation

Regarding our concrete implementation, aside from the deficiencies highlighted in Gaps in CaLM (Section 11), we also identify the following limitations.

Reliability. In order to maximize the real-world applicability of language models, introducing human evaluation of their responses during the evaluation process is essential. Although the CEG scenario has been established, the complexity and breadth of our CaLM necessitate a practical approach, leading us to use ROUGE-L for evaluating model predictions. However, it must be acknowledged that this metric does not fully capture the nuances that human evaluation can provide in terms of response quality. Automated metrics like ROUGE-L primarily focus on surface-level textual similarities, and often fail to address semantic accuracy, coherence, and relevance - attributes better discerned through human assessment. To mitigate this limitation, a mixed-method approach could be beneficial. Integrating qualitative assessments from human evaluators with quantitative metrics offers a more holistic view of a model's performance. Additionally, developing more advanced automated evaluation metrics that better mimic human judgment could further bridge the gap between current evaluation methods and the complexity of human language comprehension.

Flexibility. Despite our scenario design consisting of all levels of the causal ladder, marking a comprehensive causal evaluation of language models to date, the continuous evolution of these models and changing user requirements may render some scenarios obsolete over time. As language models develop new capabilities and increase in complexity, existing evaluation frameworks might not capture their full potential. Similarly, shifts in user demands and application contexts may necessitate updates in evaluation approaches to maintain their relevance and effectiveness. To mitigate these challenges, implementing a flexible and adaptive evaluation framework is essential. One potential solution involves regularly updating and expanding scenarios to reflect the latest developments in language model capabilities and user needs. This could be facilitated by creating a dynamic repository of scenarios, which would be periodically reviewed and revised by a diverse array of stakeholders, including researchers, developers, and end-users. Additionally, integrating feedback mechanisms where users can identify deficiencies or propose new evaluation criteria can help ensure that the evaluation process remains aligned with real-world applications and expectations. Continuous engagement with the broader AI and linguistic communities is also essential to foster innovation in evaluation methods, ensuring they remain as current and comprehensive as possible.

# 12.2 Limitations of Evaluation Results

Concerning the evaluation results in our experiments, some notable limitations are observed.

Completeness. To ensure completeness in extracting responses from language models, it is crucial to account for all possible responses and accurately match them using the appropriate patterns. For instance, in the CEI scenario, the question posed is "Whether the causal effect of [treatment] on [outcome] is identified or not?", requiring the model to respond with "yes" or "no". However, some models might answer with "the causal effect is identified" instead of a direct "yes". However, despite defining explicit response formats for each scenario and developing numerous task-specific rules for metric computation, mismatches in rules can still occur, potentially excluding some responses from the results. One potential solution to address the issue is to implement a layered review process coupled with human-in-the-loop verification. This process would involve multiple review stages, where each layer focuses on identifying and correcting mismatches or overlooked responses. Initially, a basic automated review could flag responses that do not seem to match existing rules or patterns. Following this, a human reviewer could examine these flagged responses to determine whether the mismatch is due to an inadequacy in the rules or an anomaly in the response itself. This iterative review process encourages continuous improvement of the extraction framework, reducing the likelihood of gaps in valuable data in future analyses. However, such an approach may consume a significant amount of manpower and resources. Besides, another more fundamental solution is to consider how to effectively enhance the model's ability to follow instructions. By enhancing the model's understanding and execution of given tasks, we reduce the likelihood of generating responses that fall outside predefined rules or patterns. Moreover, improving instruction-following capabilities inherently increases the model's versatility, enabling it to be applied across a broader range of tasks and industries with minimal customization.

Interpretability. The lack of interpretability in our evaluation results can be attributed to two primary factors. Firstly, our input design is engineered to solicit straightforward responses such as "yes or no" answers, choices, or probabilities from the model, without requiring the provision of explanations. Secondly, our focus on accuracy in metrics computation often leads us to neglect the necessity for the model to offer explanations for its responses. For a language model to be user-friendly and effective, it is essential in many application scenarios that it does more than merely deliver an answer; it should also provide coherent explanations. These explanations are invaluable as they aid users in understanding the rationale behind the model's responses. When users comprehend the reasoning behind a response, they are equipped to make more informed decisions, particularly in high-stakes domains such as medical diagnosis, legal advice, or financial planning. Furthermore, clear explanations can illuminate and help correct biases or errors in the model's reasoning process, thereby leading to outcomes that are not only more accurate but also fairer. Thus, enhancing the interpretability of language models contributes significantly to their reliability and utility in practical applications.

Transportability. To ensure the transportability of our findings, it is critical that no instances from the test distribution are present in the model's training data, thereby preventing any contamination between training and testing sets. However, as discussed in previous work (Liang et al., 2022; Oren et al., 2023; Li & Flanigan, 2024), due to the nature of language models trained on vast, diverse, and often incomplete datasets (e.g., text scraped from the internet), it is challenging to definitively determine whether these datasets have been contaminated. In our CaLM, we have taken specific measures to mitigate these risks by constructing a significant portion of our data independently, as detailed in Data Collection (Section 4). This helps reduce the likelihood of contamination. However, to maintain a comprehensive benchmarking scope, we still include portions of existing open-source datasets. Consequently, we must acknowledge that the potential for contamination in these sections cannot be entirely ruled out. This uncertainty may impact the validity of our results, underlining the complexity of ensuring clean dataset separations in the realm of language model training.

# 13 Conclusion

The exponential advancement of language models in recent years is widely recognized, not only captivating academic research but also finding applications across diverse societal domains. Yet, the extent to which these models possess causal reasoning capabilities, a crucial milestone on the path to human-like machine intelligence, is still unclear. This gap in understanding motivates our efforts towards conducting causal evaluations. We believe that our CaLM will uncover the present capabilities of models in causal reasoning, thereby contributing robust groundwork for the progression toward artificial general intelligence.

In conclusion, we want to underscore that although we have made every effort to ensure CaLM is thorough, fair, and ethically sound, and have acknowledged its limitations, our resources and capabilities remain limited. We encourage the broader community to critically examine, utilize, and refine CaLM, with the goal of advancing the field of causal evaluation of language models. The proverb "Many hands make light work" aptly reflects our hope that through collaborative efforts, CaLM will contribute to the further development of language models. This collaboration will ideally lead to the emergence of technologies that are not only accessible and beneficial but also constructive and accountable.

# References



Abadie, A. and Imbens, G. W. Bias-corrected matching estimators for average treatment effects. Journal of Business & Economic Statistics, 29(1):1-11, 2011.





Abdali, S., Anarfi, R., Barberan, C., and He, J. Securing large language models: Threats, vulnerabilities and responsible practices. arXiv preprint arXiv:2403.12503, 2024.





Adib, R., Griffin, P., Ahamed, S. I., and Adibuzzaman, M. A causally formulated hazard ratio estimation through backdoor adjustment on structural causal model. In Doshi-Velez, F., Fackler, J., Jung, K., Kale, D., Ranganath, R., Wallace, B., and Wiens, J. (eds.), Proceedings of the 5th Machine Learning for Healthcare Conference, volume 126 of Proceedings of Machine Learning Research, pp. 376-396. PMLR, 07-08 Aug 2020.





Ahn, J., Verma, R., Lou, R., Liu, D., Zhang, R., and Yin, W. Large language models for mathematical reasoning: Progresses and challenges. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Student Research Workshop, pp. 225-237. Association for Computational Linguistics, 2024.





Albantakis, L., Marshall, W., Hoel, E., and Tononi, G. What caused what? a quantitative account of actual causation using dynamical causal networks. Entropy, 21(5):459, 2019.





Amar, D., Sinnott-Armstrong, N., Ashley, E. A., and Rivas, M. A. Graphical analysis for phenotype-wide causal discovery in genotyped population-scale biobanks. Nature communications, 12(1):350, 2021.





Ames, R. T. and Rosemont Jr, H. The anaelects of Confucius: A philosophical translation. Ballantine books, 1999.





Angrist, J. D., Imbens, G. W., and Rubin, D. B. Identification of causal effects using instrumental variables. Journal of the American statistical Association, 91(434):444-455, 1996.





Anthropic. Model card and evaluations for claude models. Technical report, 2023.





Anthropic. Introducing the next generation of claude. Technical report, 2024.





Arif, S. and MacNeil, M. A. Applying the structural causal model framework for observational causal inference in ecology. Ecological Monographs, 93(1):e1554, 2023.





Azerbayev, Z., Schoelkopf, H., Paster, K., Santos, M. D., McAleer, S., Jiang, A. Q., Deng, J., Biderman, S., and Welleck, S. LLemma: An open language model for mathematics. arXiv preprint arXiv:2310.10631, 2023.





Bai, J., Bai, S., Chu, Y., Cui, Z., Dang, K., Deng, X., Fan, Y., Ge, W., Han, Y., Huang, F., Hui, B., Ji, L., Li, M., Lin, J., Lin, R., Liu, D., Liu, G., Lu, C., Lu, K., Ma, J., Men, R., Ren, X., Ren, X., Tan, C., Tan, S., Tu, J., Wang, P., Wang, S., Wang, W., Wu, S., Xu, B., Xu, J., Yang, A., Yang, H., Yang, J., Yang, S., Yao, Y., Yu, B., Yuan, H., Yuan, Z., Zhang, J., Zhang, X., Zhang, Y., Zhang, Z., Zhou, C., Zhou, J., Zhou, X., and Zhu, T. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.





Baichuan. Baichuan 2: Open large-scale language models. arXiv preprint arXiv:2309.10305, 2023.





Baker, A. C., Larcker, D. F., and Wang, C. C. How much should we trust staggered difference-in-differences estimates? Journal of Financial Economics, 144(2):370-395, 2022.





Ban, T., Chen, L., Wang, X., and Chen, H. From query tools to causal architects: Harnessing large language models for advanced causal discovery from data. arXiv preprint arXiv:2306.16902, 2023.





Bareinboim, E., Correa, J. D., Ibeling, D., and Icard, T. On pearl's hierarchy and the foundations of causal inference. In Probabilistic and causal inference: the works of judea pearl, pp. 507-556. 2022.





Bengio, Y., Ducharme, R., and Vincent, P. A neural probabilistic language model. Advances in neural information processing systems, 13, 2000.





Berkson, J. Limitations of the application of fourfold table analysis to hospital data. Biometrics Bulletin, 2(3): 47-53, 1946.





Bertasius, G., Wang, H., and Torresani, L. Is space-time attention all you need for video understanding? In ICML, volume 2, pp. 4, 2021.





Besta, M., Blach, N., Kubicek, A., Gerstenberger, R., Podstawski, M., Gianinazzi, L., Gajda, J., Lehmann, T., Niewiadomski, H., Nczyk, P., et al. Graph of thoughts: Solving elaborate problems with large language models. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 17682-17690, 2024.





Birney, E. Mendelian randomization. Cold Spring Harbor perspectives in medicine, pp. a041302, 2021.





Bollen, K. A. Instrumental variables in sociology and the social sciences. Annual Review of Sociology, 38:37-72, 2012.





Bolton, E., Hall, D., Yasunaga, M., Lee, T., Manning, C., and Liang, P. Stanford crfm introduces pubmedgpt 2.7 b, 2022.





Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., et al. On the opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258, 2021.





Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. Language models are few-shot learners. Advances in neural information processing systems, 33:1877-1901, 2020.





Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar, E., Lee, P., Lee, Y. T., Li, Y., Lundberg, S., et al. Sparks of artificial general intelligence: Early experiments with gpt-4. arXiv preprint arXiv:2303.12712, 2023.





Byrne, R. M. The rational imagination: How people create alternatives to reality. MIT press, 2007.





Capano, G. and Howlett, M. Causal logics and mechanisms in policy design: How and why adopting a mechanistic perspective can improve policy design. Public policy and administration, 36(2):141-162, 2021.





Carter, A. R., Sanderson, E., Hammerton, G., Richmond, R. C., Davey Smith, G., Heron, J., Taylor, A. E., Davies, N. M., and Howe, L. D. Mendelian randomisation for mediation analysis: current methods and challenges for implementation. European journal of epidemiology, 36(5):465-478, 2021.





Caselli, T. and Vossen, P. The event storyline: A new benchmark for causal and temporal relation extraction. In Proceedings of the Events and Stories in the News Workshop, pp. 77-86, 2017.





Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K., Chen, H., Yi, X., Wang, C., Wang, Y., et al. A survey on evaluation of large language models. ACM Transactions on Intelligent Systems and Technology.





Chen, G., Zheng, Y.-D., Wang, J., Xu, J., Huang, Y., Pan, J., Wang, Y., Wang, Y., Qiao, Y., Lu, T., et al. Videollm: Modeling video sequence with large language models. arXiv preprint arXiv:2305.13292, 2023a.





Chen, J., Wu, X., Hu, Y., and Luo, J. Spatial-temporal causal inference for partial image-to-video adaptation. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, pp. 1027-1035, 2021a.





Chen, L., Jin, Z., Eyuboglu, E. S., Ré, C., Zaharia, M., and Zou, J. Y. Hapi: A large-scale longitudinal dataset of commercial ml api predictions. Advances in Neural Information Processing Systems, 35:24571-24585, 2022a.





Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. d. O., Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Brockman, G., et al. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374, 2021b.





Chen, M., Cao, Y., Deng, K., Li, M., Wang, K., Shao, J., and Zhang, Y. ERGO: Event relational graph transformer for document-level event causality identification. In Proceedings of the 29th International Conference on Computational Linguistics, pp. 2118-2128, Gyeongju, Republic of Korea, October 2022b. International Committee on Computational Linguistics.





Chen, M., Ma, Y., Song, K., Cao, Y., Zhang, Y., and Li, D. Learning to teach large language models logical reasoning. arXiv preprint arXiv:2310.09158, 2023b.





Chen, M., Cao, Y., Zhang, Y., and Lu, C. Quantifying and mitigating unimodal biases in multimodal large language models: A causal perspective. arXiv preprint arXiv:2403.18346, 2024.





Chen, W., Ma, X., Wang, X., and Cohen, W. W. Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks. Transactions on Machine Learning Research, 2023c.





Chen, Y., Qian, S., Tang, H., Lai, X., Liu, Z., Han, S., and Jia, J. Longlora: Efficient fine-tuning of long-context large language models. In The Twelfth International Conference on Learning Representations, 2023d.





Chen, Z. and Qian, T. Relation-aware collaborative learning for unified aspect-based sentiment analysis. In Proceedings of the 58th annual meeting of the association for computational linguistics, pp. 3685-3694, 2020.





Chiang, W.-L., Li, Z., Lin, Z., Sheng, Y., Wu, Z., Zhang, H., Zheng, L., Zhuang, S., Zhuang, Y., Gonzalez, J. E., Stoica, I., and Xing, E. P. Vicuna: An open-source chatbot impressing gpt-4 with  $90\%$  * chatgpt quality, March 2023.





Cinelli, C., Forney, A., and Pearl, J. A crash course in good and bad controls. Sociological Methods & Research, pp. 00491241221099552, 2022.





Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168, 2021.





Cole, S. R., Platt, R. W., Schisterman, E. F., Chu, H., Westreich, D., Richardson, D., and Poole, C. Illustrating bias due to conditioning on a collider. International journal of epidemiology, 39(2):417-420, 2010.





Correa, J., Tian, J., and Bareinboim, E. Generalized adjustment under confounding and selection biases. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 32, 2018.





Dai, L. and Han, M. Robust sentiment classification based on the backdoor adjustment. In Proceedings of the 2023 6th International Conference on Machine Learning and Natural Language Processing, pp. 41-47, 2023.





Dao, X.-Q. and Le, N.-B. Investigating the effectiveness of chatgpt in mathematical reasoning and problem solving: Evidence from the Vietnamese national high school graduation examination. arXiv preprint arXiv:2306.06331, 2023.





Das, B. C., Amini, M. H., and Wu, Y. Security and privacy challenges of large language models: A survey. arXiv preprint arXiv:2402.00888, 2024.





De Chaisemartin, C. and d'Haultfoeuille, X. Two-way fixed effects and differences-in-differences with heterogeneous treatment effects: A survey. The Econometrics Journal, 26(3):C1-C30, 2023.





Deng, Y., Zhang, W., Pan, S. J., and Bing, L. Multilingual jailbreak challenges in large language models. In The Twelfth International Conference on Learning Representations, 2023.





Dettmers, T., Pagnoni, A., Holtzman, A., and Zettlemoyer, L. Qlora: Efficient finetuning of quantized llms. Advances in Neural Information Processing Systems, 36, 2024.





Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.





Dhamala, J., Sun, T., Kumar, V., Krishna, S., Pruksachatkun, Y., Chang, K.-W., and Gupta, R. Bold: Dataset and metrics for measuring biases in open-ended language generation. In Proceedings of the 2021 ACM conference on fairness, accountability, and transparency, pp. 862-872, 2021.





Dong, Q., Li, L., Dai, D., Zheng, C., Wu, Z., Chang, B., Sun, X., Xu, J., and Sui, Z. A survey on in-context learning. arXiv preprint arXiv:2301.00234, 2022.





Du, L., Ding, X., Xiong, K., Liu, T., and Qin, B. e-care: a new dataset for exploring explainable causal reasoning. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 432-446, 2022.





Duncan, G. J. and Magnuson, K. Socioeconomic status and cognitive functioning: moving from correlation to causation. Wiley Interdisciplinary Reviews: Cognitive Science, 3(3):377-386, 2012.





Elwert, F. Graphical causal models. In Handbook of causal analysis for social research, pp. 245-273. Springer, 2013.





Elwert, F. and Winship, C. Endogenous selection bias: The problem of conditioning on a collider variable. Annual review of sociology, 40:31-53, 2014.





Elyoseph, Z., Hadar-Shoval, D., Asraf, K., and Lvovsky, M. Chatgpt outperforms humans in emotional awareness evaluations. Frontiers in Psychology, 14:1199058, 2023.





Feng, P., Zhou, X.-H., Zou, Q.-M., Fan, M.-Y., and Li, X.-S. Generalized propensity score for estimating the average treatment effect of multiple treatments. Statistics in medicine, 31(7):681-697, 2012.





Frohberg, J. and Binder, F. Crass: A novel data set and benchmark to test counterfactual reasoning of large language models. In Proceedings of the Thirteenth Language Resources and Evaluation Conference, pp. 2126-2140, 2022.





Fu, Yao; Peng, H. and Khot, T. How does gpt obtain its ability? tracing emergent abilities of language models to their sources. Yao Fu's Notion, Dec 2022.





Gallegos, I. O., Rossi, R. A., Barrow, J., Tanjim, M. M., Kim, S., Dernoncourt, F., Yu, T., Zhang, R., and Ahmed, N. K. Bias and fairness in large language models: A survey. arXiv preprint arXiv:2309.00770, 2023.





Gan, C., Zhang, Q., and Mori, T. Giellm: Japanese general information extraction large language model utilizing mutual reinforcement effect. arXiv preprint arXiv:2311.06838, 2023.





Gao, J., Ding, X., Qin, B., and Liu, T. Is chatgpt a good causal reasoner? a comprehensive evaluation. In The 2023 Conference on Empirical Methods in Natural Language Processing, 2023a.





Gao, L., Choubey, P. K., and Huang, R. Modeling document-level causal structures for event causal relation identification. In Burstein, J., Doran, C., and Solorio, T. (eds.), Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pp. 1808-1817, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1179.





Gao, S., Gao, C., Wang, C., Sun, J., Lo, D., and Yu, Y. Two sides of the same coin: Exploiting the impact of identifiers in neural code comprehension. In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE), pp. 1933-1945. IEEE, 2023b.





Garcez, A. S., Lamb, L. C., and Gabbay, D. M. Neural-symbolic cognitive reasoning. Springer Science & Business Media, 2008.





Gehman, S., Gururangan, S., Sap, M., Choi, Y., and Smith, N. A. Realtoxicityprompts: Evaluating neural toxic degeneration in language models. arXiv preprint arXiv:2009.11462, 2020.





Geng, X., Gudibandé, A., Liu, H., Wallace, E., Abbeel, P., Levine, S., and Song, D. Koala: A dialogue model for academic research. Blog post, April 2023.





Glymour, C., Zhang, K., and Spirtes, P. Review of causal discovery methods based on graphical models. Frontiers in genetics, 10:524, 2019.





Goertzel, B., Ikle, M., Goertzel, I. F., and Heljakka, A. Probabilistic logic networks: A comprehensive framework for uncertain inference. Springer Science & Business Media, 2008.





Goldman-Eisler, F. Speech production and the predictability of words in context. Quarterly Journal of Experimental Psychology, 10(2):96-106, 1958.





Gomila, R. Logistic or linear? estimating causal effects of experimental treatments on binary outcomes using regression analysis. Journal of Experimental Psychology: General, 150(4):700, 2021.





Graham, S. An attributional theory of motivation. Contemporary Educational Psychology, 61:101861, 2020.





Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M. More than you've asked for: A comprehensive analysis of novel prompt injection threats to application-integrated large language models. arXiv e-prints, pp. arXiv-2302, 2023.





Gu, Z., Zhu, X., Ye, H., Zhang, L., Wang, J., Zhu, Y., Jiang, S., Xiong, Z., Li, Z., Wu, W., et al. Xiezhi: An ever-updating benchmark for holistic domain knowledge evaluation. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 18099-18107, 2024.





Guo, R., Li, J., and Liu, H. Learning individual causal effects from networked observational data. In Proceedings of the 13th international conference on web search and data mining, pp. 232-240, 2020.





Halpern, J. Y. Actual Causality. The MIT Press, August 2016. ISBN 978-0-262-33661-1. doi: 10.7551/mitpress/10809.001.0001. _eprint: https://direct.mit.edu/book-pdf/2262849/book_9780262336611.pdf.





Hammarström, H., Forkel, R., Haspelmath, M., and Bank, S. Glottolog 4.4. leipzig, 2021.





Hariton, E. and Locascio, J. J. Randomised controlled trials—the gold standard for effectiveness research. *BJOG: an international journal of obstetrics and gynaecology*, 125(13):1716, 2018.





Harvey, P., Madison, K., Martinko, M., Crook, T. R., and Crook, T. A. Attribution theory in the organizational sciences: The road traveled and the path ahead. Academy of Management Perspectives, 28(2):128-146, 2014.





Hauke, J. and Kossowski, T. Comparison of values of pearson's and spearman's correlation coefficients on the same sets of data. Quaestiones geographicae, 30(2):87-93, 2011.





He-Yueya, J., Poesia, G., Wang, R., and Goodman, N. Solving math word problems by combining language models with symbolic solvers. In The 3rd Workshop on Mathematical Reasoning and AI at NeurIPS'23, 2023.





Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J. Measuring massive multitask language understanding. In International Conference on Learning Representations, 2020.





Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., and Steinhardt, J. Measuring mathematical problem solving with the math dataset. In Thirty-fifth Conference on Neural Information Processing Systems Datasets and Benchmarks Track (Round 2), 2021.





Hill, J. L. Bayesian nonparametric modeling for causal inference. Journal of Computational and Graphical Statistics, 20(1):217-240, 2011.





Hirano, K., Imbens, G. W., and Ridder, G. Efficient estimation of average treatment effects using the estimated propensity score. *Econometrica*, 71(4):1161-1189, 2003.





Hobbhahn, M., Lieberum, T., and Seiler, D. Investigating causal understanding in llms. In NeurIPS ML Safety Workshop, 2022.





Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., de las Casas, D., Hendricks, L. A., Welbl, J., Clark, A., Hennigan, T., Noland, E., Millican, K., van den Driessche, G., Damoc, B., Guy, A., Osindero, S., Simonyan, K., Elsen, E., Vinyals, O., Rae, J. W., and Sifre, L. Training compute-optimal large language models. In Oh, A. H., Agarwal, A., Belgrave, D., and Cho, K. (eds.), Advances in Neural Information Processing Systems, 2022.





Howe, L. J., Nivard, M. G., Morris, T. T., Hansen, A. F., Rasheed, H., Cho, Y., Chittoor, G., Ahlskog, R., Lind, P. A., Palviainen, T., et al. Within-sibship genome-wide association analyses decrease bias in estimates of direct genetic effects. Nature genetics, 54(5):581-592, 2022.





Hu, E. J., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., Chen, W., et al. Lora: Low-rank adaptation of large language models. In International Conference on Learning Representations, 2021.





Huang, J.-H., Yang, C.-H. H., Chen, P.-Y., Chen, M.-H., and Worring, M. Causalainer: Causal explainer for automatic video summarization. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 2629-2635, 2023.





Imani, S., Du, L., and Shrivastava, H. Mathprompter: Mathematical reasoning using large language models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 5: Industry Track), pp. 37-42, 2023.





Imbens, G. W. Potential outcome and directed acyclic graph approaches to causality: Relevance for empirical practice in economics. Journal of Economic Literature, 58(4):1129-1179, 2020.





Jastreboff, A. M., Aronne, L. J., Ahmad, N. N., Wharton, S., Connery, L., Alves, B., Kiyosue, A., Zhang, S., Liu, B., Bunck, M. C., et al. Tirzepatide once weekly for the treatment of obesity. New England Journal of Medicine, 387(3):205-216, 2022.





Jelinek, F. Continuous speech recognition by statistical methods. Proceedings of the IEEE, 64(4):532-556, 1976.





Jelinek, F. Statistical methods for speech recognition. 1998.





Ji, Z., Ma, P., Li, Z., and Wang, S. Benchmarking and explaining large language model-based code generation: A causality-centric approach. arXiv preprint arXiv:2310.06680, 2023.





Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., Casas, D. d. l., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., et al. Mistral 7b. arXiv preprint arXiv:2310.06825, 2023.





Jin, Z., Chen, Y., Leeb, F., Gresele, L., Kamal, O., Zhiheng, L., Blin, K., Adauto, F. G., Kleiman-Weiner, M., Sachan, M., et al. Cladder: Assessing causal reasoning in language models. In Thirty-seventh Conference on Neural Information Processing Systems, 2023a.





Jin, Z., Liu, J., Lyu, Z., Poff, S., Sachan, M., Mihalcea, R., Diab, M., and Scholkopf, B. Can large language models infer causation from correlation?, 2023b.





Jin, Z., Liu, J., LYU, Z., Poff, S., Sachan, M., Mihalcea, R., Diab, M. T., and Scholkopf, B. Can large language models infer causation from correlation? In The Twelfth International Conference on Learning Representations, 2024.





Kahneman, D. and Miller, D. T. Norm theory: Comparing reality to its alternatives. Psychological review, 93(2): 136, 1986.





Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., and Amodei, D. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361, 2020.





Kaufman, S., Kaufman, J. S., MacLehose, R. F., Greenland, S., and Poole, C. Improved estimation of controlled direct effects in the presence of unmeasured confounding of intermediate variables. Statistics in medicine, 24(11):1683-1702, 2005.





Kazemitabaar, M., Hou, X., Henley, A., Ericson, B. J., Weintrop, D., and Grossman, T. How novices use llm-based code generators to solve cs1 coding tasks in a self-paced learning environment. In Proceedings of the 23rd Koli Calling International Conference on Computing Education Research, pp. 1-12, 2023.





Kenny, E. M., Ford, C., Quinn, M., and Keane, M. T. Explaining black-box classifiers using post-hoc explanations-by-example: The effect of explanations and error-rates in xai user studies. Artificial Intelligence, 294:103459, 2021.





Kiciman, E., Ness, R., Sharma, A., and Tan, C. Causal reasoning and large language models: Opening a new frontier for causality. arXiv preprint arXiv:2305.00050, 2023.





Kim, J. and Pearl, J. A computational model for causal and diagnostic reasoning in inference systems. In International Joint Conference on Artificial Intelligence, pp. 0-0, 1983.





Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., and Iwasawa, Y. Large language models are zero-shot reasoners. In Koyejo, S., Mohamed, S., Agarwal, A., Belgrave, D., Cho, K., and Oh, A. (eds.), Advances in Neural Information Processing Systems, volume 35, pp. 22199-22213. Curran Associates, Inc., 2022.





Kuppens, P., Van Mechelen, I., Smits, D. J., and De Boeck, P. The appraisal basis of anger: specificity, necessity and sufficiency of components. Emotion, 3(3):254, 2003.





Kusner, M. J., Loftus, J., Russell, C., and Silva, R. Counterfactual fairness. Advances in neural information processing systems, 30, 2017.





LaLonde, R. J. Evaluating the econometric evaluations of training programs with experimental data. The American economic review, pp. 604-620, 1986.





Landeiro, V. and Culotta, A. Robust text classification in the presence of confounding bias. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 30, 2016.





Landeiro, V. and Culotta, A. Robust text classification under confounding shift. Journal of Artificial Intelligence Research, 63:391-419, 2018.





Langenhoff, A. F., Wiegmann, A., Halpern, J. Y., Tenenbaum, J. B., and Gerstenberg, T. Predicting responsibility judgments from dispositional inferences and causal attributions. Cognitive Psychology, 129:101412, 2021.





Le Scao, T. and Rush, A. How many data points is a prompt worth? In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 2627-2636. Association for Computational Linguistics, June 2021. doi: 10.18653/v1/2021.naacl-main.208.





Lee, J. J. R., Bhattacharya, R., Nabi, R., and Shpitser, I. Ananke: A python package for causal inference using graphical models. CoRR, abs/2301.11477, 2023a. doi: 10.48550/arXiv.2301.11477.





Lee, J. Y., Kang, S., Yoon, J., and Yoo, S. The github recent bugs dataset for evaluating llm-based debugging applications. arXiv preprint arXiv:2310.13229, 2023b.





Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Kuttler, H., Lewis, M., Yih, W.-t., Rocktächel, T., et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in Neural Information Processing Systems, 33:9459-9474, 2020.





Li, C. and Flanigan, J. Task contamination: Language models may not be few-shot anymore. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 18471-18480, 2024.





Li, C., Wang, J., Zhu, K., Zhang, Y., Hou, W., Lian, J., and Xie, X. Emotionprompt: Leveraging psychology for large language models enhancement via emotional stimulus. arXiv preprint arXiv:2307.11760, 2023a.





Li, H., Guo, D., Fan, W., Xu, M., Huang, J., Meng, F., and Song, Y. Multi-step jailbreaking privacy attacks on chatgpt. In Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 4138-4153, 2023b.





Li, J., Cheng, X., Zhao, X., Nie, J.-Y., and Wen, J.-R. Halueval: A large-scale hallucination evaluation benchmark for large language models. In The 2023 Conference on Empirical Methods in Natural Language Processing, 2023c.





Li, J., Li, D., Savarese, S., and Hoi, S. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. arXiv preprint arXiv:2301.12597, 2023d.





Li, K., He, Y., Wang, Y., Li, Y., Wang, W., Luo, P., Wang, Y., Wang, L., and Qiao, Y. Videochat: Chat-centric video understanding. arXiv preprint arXiv:2305.06355, 2023e.





Li, R., Allal, L. B., Zi, Y., Muennighoff, N., Kocetkov, D., Mou, C., Marone, M., Akiki, C., Li, J., Chim, J., et al.  
Starcoder: may the source be with you! arXiv preprint arXiv:2305.06161, 2023f.





Li, X., Fan, B., Zhang, R., Jin, L., Wang, D., Guo, Z., Zhao, Y., and Li, R. Image content generation with causal reasoning. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 13646-13654, 2024.





Li, Y., Choi, D., Chung, J., Kushman, N., Schrittwieser, J., Leblond, R., Eccles, T., Keeling, J., Gimeno, F., Dal Lago, A., et al. Competition-level code generation with alphabet. Science, 378(6624):1092-1097, 2022.





Li, Y., Du, M., Song, R., Wang, X., and Wang, Y. A survey on fairness in large language models. arXiv preprint arXiv:2308.10149, 2023g.





Liakhovets, D. and Schlarb, S. Zero-shot event causality identification with question answering. In Proceedings of the 5th International Conference on Computational Linguistics in Bulgaria (CLIB 2022), pp. 113-119, 2022.





Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., Zhang, Y., Narayanan, D., Wu, Y., Kumar, A., et al. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110, 2022.





Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Cobbe, K. Let's verify step by step. In The Twelfth International Conference on Learning Representations, 2023.





Lin, C.-Y. Rouge: A package for automatic evaluation of summaries. In Text summarization branches out, pp. 74-81, 2004.





Lin, W., Lan, H., and Li, B. Generative causal explanations for graph neural networks. In International Conference on Machine Learning, pp. 6666-6679. PMLR, 2021.





Linden, A., Mathur, M. B., and VanderWeele, T. J. Conducting sensitivity analysis for unmeasured confounding in observational studies using e-values: the value package. The Stata Journal, 20(1):162-175, 2020.





Liu, H., Ning, R., Teng, Z., Liu, J., Zhou, Q., and Zhang, Y. Evaluating the logical reasoning ability of chatgpt and gpt-4. arXiv preprint arXiv:2304.03439, 2023a.





Liu, H., Li, C., Wu, Q., and Lee, Y. J. Visual instruction tuning. Advances in neural information processing systems, 36, 2024a.





Liu, Y., Li, G., and Lin, L. Cross-modal causal relational reasoning for event-level visual question answering. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2023b.





Liu, Y., Liu, F., Jiao, L., Bao, Q., Li, L., Guo, Y., and Chen, P. A knowledge-based hierarchical causal inference network for video action recognition. IEEE Transactions on Multimedia, 2024b.





Liu, Z., Huang, D., Huang, K., Li, Z., and Zhao, J. Finbert: A pre-trained financial language representation model for financial text mining. In Proceedings of the twenty-ninth international conference on international joint conferences on artificial intelligence, pp. 4513-4519, 2021.





Long, S., Schuster, T., and Piché, A. Can large language models build causal graphs? In NeurIPS 2022 Workshop on Causality for Real-world Impact, 2022.





Louizos, C., Shalit, U., Mooij, J. M., Sontag, D., Zemel, R., and Welling, M. Causal effect inference with deep latent-variable models. Advances in neural information processing systems, 30, 2017.





Lu, C., Qian, C., Zheng, G., Fan, H., Gao, H., Zhang, J., Shao, J., Deng, J., Fu, J., Huang, K., et al. From gpt-4 to gemini and beyond: Assessing the landscape of mllms on generalizability, trustworthiness and causality through four modalities. arXiv preprint arXiv:2401.15071, 2024.





Luo, Z., Xu, C., Zhao, P., Sun, Q., Geng, X., Hu, W., Tao, C., Ma, J., Lin, Q., and Jiang, D. Wizardcoder: Empowering code large language models with evol-instruct, 2023.





Madaan, A., Tandon, N., Gupta, P., Hallinan, S., Gao, L., Wiegreffe, S., Alon, U., Dziri, N., Prabhumoye, S., Yang, Y., et al. Self-refine: Iterative refinement with self-feedback. Advances in Neural Information Processing Systems, 36, 2024.





Madumal, P., Miller, T., Sonenberg, L., and Vetere, F. Explainable reinforcement learning through a causal lens. In Proceedings of the AAAI conference on artificial intelligence, volume 34, pp. 2493-2500, 2020.





Mahmoud, O., Dudbridge, F., Davey Smith, G., Munafo, M., and Tilling, K. A robust method for collider bias correction in conditional genome-wide association studies. Nature Communications, 13(1):619, 2022.





Maisonnave, M., Delbianco, F., Tohme, F., Milios, E., and Maguitman, A. G. Causal graph extraction from news: a comparative study of time-series causality learning techniques. PeerJ Computer Science, 8:e1066, 2022.





Malle, B. F. Attribution theories: How people make sense of behavior. Theories in Social Psychology, Second Edition, pp. 93-120, 2022.





Mao, C., Xia, K., Wang, J., Wang, H., Yang, J., Bareinboim, E., and Vondrick, C. Causal transportability for visual recognition. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 7521-7531, 2022.





Marbach, M. and Hangartner, D. Profiling compliers and noncompliers for instrumental-variable analysis. Political Analysis, 28(3):435-444, 2020.





Matthay, E. C. and Glymour, M. M. Causal inference challenges and new directions for epidemiologic research on the health effects of social policies. Current Epidemiology Reports, 9(1):22-37, 2022.





Maydeu-Olivares, A., Shi, D., and Fairchild, A. J. Estimating causal effects in linear regression models with observational data: The instrumental variables regression model. Psychological methods, 25(2):243, 2020.





Melkas, L., Savvides, R., Chandramouli, S. H., Makela, J., Nieminen, T., Mammarella, I., and Puolamäki, K. Interactive causal structure discovery in earth system sciences. In Le, T. D., Li, J., Cooper, G., Triantafyllou, S., Bareinboim, E., Liu, H., and Kiyavash, N. (eds.), Proceedings of The KDD'21 Workshop on Causal Discovery, volume 150 of Proceedings of Machine Learning Research, pp. 3-25. PMLR, 15 Aug 2021.





Mero, J., Tarkiainen, A., and Tobon, J. Effectual and causal reasoning in the adoption of marketing automation. Industrial Marketing Management, 86:212-222, 2020.





Meta. Meta llama 3, 2024.





Mialon, G., Dessi, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Roziere, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., et al. Augmented language models: a survey. Transactions on Machine Learning Research, 2023.





Mikolov, T., Karafiát, M., Burget, L., Cernocký, J., and Khudanpur, S. Recurrent neural network based language model. In INTERSPEECH 2010, 11th Annual Conference of the International Speech Communication Association, Makuhari, Chiba, Japan, September 26-30, 2010, pp. 1045-1048. ISCA, 2010. doi: 10.21437/INTERSPEECH.2010-343.





Min, M. J., Ding, Y., Buratti, L., Pajar, S., Kaiser, G., Jana, S., and Ray, B. Beyond accuracy: Evaluating self-consistency of code llms. In The Twelfth International Conference on Learning Representations, 2023.





Min, S., Lyu, X., Holtzman, A., Artetxe, M., Lewis, M., Hajishirzi, H., and Zettlemoyer, L. Rethinking the role of demonstrations: What makes in-context learning work? In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pp. 11048-11064, 2022.





Mirza, P., Sprugnoli, R., Tonelli, S., and Speranza, M. Annotating causality in the tempeval-3 corpus. In Proceedings of the EACL 2014 Workshop on Computational Approaches to Causality in Language (CAtoCL), pp. 10-19, 2014.





Mogstad, M., Torgovitsky, A., and Walters, C. R. The causal interpretation of two-stage least squares with multiple instrumental variables. American Economic Review, 111(11):3663-3698, 2021.





Moraffah, R., Karami, M., Guo, R., Raglin, A., and Liu, H. Causal interpretability for machine learning-problems, methods and evaluation. ACM SIGKDD Explorations Newsletter, 22(1):18-33, 2020.





Munafò, M. R., Tilling, K., Taylor, A. E., Evans, D. M., and Davey Smith, G. Collider scope: when selection bias can substantially influence observed associations. International journal of epidemiology, 47(1):226-235, 2018.





Neal, B. Introduction to causal inference.





Nguyen, T. Q., Schmid, I., and Stuart, E. A. Clarifying causal mediation analysis for the applied researcher: Defining effects based on what we want to learn. *Psychological Methods*, 26(2):255, 2021.





Niu, Y., Tang, K., Zhang, H., Lu, Z., Hua, X.-S., and Wen, J.-R. Counterfactual vqa: A cause-effect look at language bias. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 12700-12710, 2021.





Nordhoff, S. and Hammarström, H. Glottolog/langdoc: Defining dialects, languages, and language families as collections of resources. In First International Workshop on Linked Science 2011-In conjunction with the International Semantic Web Conference (ISWC 2011), 2011.





OpenAI. Chatgpt: Optimizing language models for dialogue. Blog post, 2022.





OpenAI. Gpt-4 technical report, 2023.





OpenAI. Gpt-4v(ision) system card. Blog post, 2024.





Oren, Y., Meister, N., Chatterji, N. S., Ladhak, F., and Hashimoto, T. Proving test set contamination for black-box language models. In The Twelfth International Conference on Learning Representations, 2023.





O'Shaughnessy, M., Canal, G., Connor, M., Rozell, C., and Davenport, M. Generative causal explanations of black-box classifiers. Advances in neural information processing systems, 33:5453-5467, 2020.





Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems, 35:27730-27744, 2022.





Paranjape, B., Lundberg, S., Singh, S., Hajishirzi, H., Zettlemoyer, L., and Ribeiro, M. T. Art: Automatic multi-step reasoning and tool-use for large language models. arXiv preprint arXiv:2303.09014, 2023.





Parisi, A., Zhao, Y., and Fiedel, N. Talm: Tool augmented language models. arXiv preprint arXiv:2205.12255, 2022.





Pearl, J. Probabilistic reasoning in intelligent systems: networks of plausible inference. Morgan Kaufmann, 1988.





Pearl, J. Causal diagrams for empirical research. Biometrika, 82(4):669-688, 1995.





Pearl, J. Direct and indirect effects. In Proceedings of the Seventeenth Conference on Uncertainty in Artificial Intelligence, pp. 411-420, 2001.





Pearl, J. Causality. Cambridge university press, 2009.





Pearl, J. The seven tools of causal inference, with reflections on machine learning. Communications of the ACM, 62(3):54-60, 2019.





Pearl, J. Probabilities of causation: three counterfactual interpretations and their identification. In *Probabilistic and Causal Inference: The Works of Judea Pearl*, pp. 317-372. 2022.





Pearl, J. and Mackenzie, D. The book of why: the new science of cause and effect. Basic books, 2018.





Pearl, J., Glymour, M., and Jewell, N. P. Causal inference in statistics: A primer. John Wiley & Sons, 2016.





Peaslee, R. J. Multiple causation and damage. Harvard Law Review, 47(7):1127-1142, 1934.





Perez, F. and Ribeiro, I. Ignore previous prompt: Attack techniques for language models. In NeurIPS ML Safety Workshop, 2022.





Peters, J., Janzing, D., and Scholkopf, B. Elements of causal inference: foundations and learning algorithms. The MIT Press, 2017.





Pfleiderer, P., Schleussner, C.-F., Geiger, T., and Kretschmer, M. Robust predictors for seasonal atlantic hurricane activity identified with causal effect networks. Weather and Climate Dynamics, 1(2):313-324, 2020.





Pustejovsky, J., Littman, J., Saurí, R., and Verhagen, M. Timebank 1.2 documentation. Event London, no. April, pp. 6-11, 2006.





Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al. Language models are unsupervised multitask learners.





Radford, A., Narasimhan, K., Salimans, T., Sutskever, I., et al. Improving language understanding by generative pre-training. 2018.





Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., and Liu, P. J. Exploring the limits of transfer learning with a unified text-to-text transformer. The Journal of Machine Learning Research, 21(1):5485-5551, 2020.





Richardson, T. S., Evans, R. J., Robins, J. M., and Shpitser, I. Nested markov properties for acyclic directed mixed graphs. The Annals of Statistics, 51(1):334-361, 2023.





Richens, J. G., Lee, C. M., and Johri, S. Improving the accuracy of medical diagnosis with causal machine learning. Nature communications, 11(1):3923, 2020.





Rodriguez-Cardenas, D., Palacio, D. N., Khati, D., Burke, H., and Poshyvanyk, D. Benchmarking causal study to interpret large language models for source code. In 2023 IEEE International Conference on Software Maintenance and Evolution (ICSME), pp. 329-334. IEEE, 2023.





Roemmle, M., Bejan, C. A., and Gordon, A. S. Choice of plausible alternatives: An evaluation of commonsense causal reasoning. In AAAI spring symposium: logical formalizations of commonsense reasoning, pp. 90-95, 2011.





Rolfe, S., Garnham, L., Godwin, J., Anderson, I., Seaman, P., and Donaldson, C. Housing as a social determinant of health and wellbeing: Developing an empirically-informed realist theoretical framework. BMC Public Health, 20(1):1-19, 2020.





Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and Ommer, B. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 10684-10695, 2022.





Romera-Paredes, B., Barekatain, M., Novikov, A., Balog, M., Kumar, M. P., Dupont, E., Ruiz, F. J., Ellenberg, J. S., Wang, P., Fawzi, O., et al. Mathematical discoveries from program search with large language models. Nature, 625(7995):468-475, 2024.





Rosato, A., Tenori, L., Cascante, M., De Atauri Carulla, P. R., Martins dos Santos, V. A., and Saccenti, E. From correlation to causation: analysis of metabolomics data using systems biology approaches. Metabolomics, 14:1-20, 2018.





Rosenblatt, F. The perceptron: a probabilistic model for information storage and organization in the brain. Psychological review, 65(6):386, 1958.





Rosenfeld, R. Two decades of statistical language modeling: Where do we go from here? Proceedings of the IEEE, 88(8):1270-1278, 2000.





Roth, J., Sant'Anna, P. H., Bilinski, A., and Poe, J. What's trending in difference-in-differences? a synthesis of the recent econometrics literature. Journal of Econometrics, 235(2):2218-2244, 2023.





Roziere, B., Gehring, J., Gloeckle, F., Sootla, S., Gat, I., Tan, X. E., Adi, Y., Liu, J., Remez, T., Rapin, J., et al. Code llama: Open foundation models for code. arXiv preprint arXiv:2308.12950, 2023.





Runge, J., Nowack, P., Kretschmer, M., Flaxman, S., and Sejdinovic, D. Detecting and quantifying causal associations in large nonlinear time series datasets. Science advances, 5(11):eau4996, 2019.





Runge, J., Gerhardus, A., Varando, G., Eyring, V., and Camps-Valls, G. Causal inference for time series. Nature Reviews Earth & Environment, 4(7):487-505, 2023.





Saravia, E. Prompt Engineering Guide. https://github.com/dair-ai/Prompt-Engineering-Guide, 12 2022.





Saridakis, G., Lai, Y., Muñoz Torres, R. I., and Gourlay, S. Exploring the relationship between job satisfaction and organizational commitment: an instrumental variable approach. The International Journal of Human Resource Management, 31(13):1739-1769, 2020.





Sawada, T., Paleka, D., Havrilla, A., Tadepalli, P., Vidas, P., Kranias, A., Nay, J., Gupta, K., and Komatsuzaki, A. Arb: Advanced reasoning benchmark for large language models. In The 3rd Workshop on Mathematical Reasoning and AI at NeurIPS'23, 2023.





Schick, T., Dwivedi-Yu, J., Dessi, R., Raileanu, R., Lomeli, M., Hambro, E., Zettlemoyer, L., Cancedda, N., and Scialom, T. Toolformer: Language models can teach themselves to use tools. Advances in Neural Information Processing Systems, 36, 2024.





Schulhoff, S. V. Prompt injection vs jailbreaking: What is the difference? 2024.





Schwab, P., Linhardt, L., Bauer, S., Buhmann, J. M., and Karlen, W. Learning counterfactual representations for estimating individual dose-response curves. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pp. 5612-5619, 2020.





Sedgwick, P. Pearson's correlation coefficient. Bmj, 345, 2012.





Shannon, C. E. A mathematical theory of communication. The Bell system technical journal, 27(3):379-423, 1948.





Sharma, A. and Kiciman, E. Dowhy: An end-to-end library for causal inference. CoRR, abs/2011.04216, 2020.





Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., DURMUS, E., Hatfield-Dodds, Z., Johnston, S. R., Kravec, S. M., Maxwell, T., McCandlish, S., Ndousse, K., Rausch, O., Schiefer, N., Yan, D., Zhang, M., and Perez, E. Towards understanding sycophancy in language models. In The Twelfth International Conference on Learning Representations, 2024.





Shi, C., Veitch, V., and Blei, D. M. Invariant representation learning for treatment effect estimation. In de Campos, C. and Maathuis, M. H. (eds.), Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence, volume 161 of Proceedings of Machine Learning Research, pp. 1546-1555. PMLR, 27-30 Jul 2021.





Shimoni, Y., Yanover, C., Karavani, E., and Goldschmmidt, Y. Benchmarking framework for performance-evaluation of causal inference analysis. arXiv preprint arXiv:1802.05046, 2018.





Shimonovich, M., Pearce, A., Thomson, H., Keyes, K., and Katikireddi, S. V. Assessing causality in epidemiology: revisiting bradford hill to incorporate developments in causal thinking. European journal of epidemiology, 36:873-887, 2021.





Shpitser, I. and Pearl, J. Complete identification methods for the causal hierarchy. Journal of Machine Learning Research, 9:1941-1979, 2008.





Spirtes, P. and Zhang, K. Causal discovery and inference: concepts and recent methodological advances. In Applied informatics, volume 3, pp. 1-28. Springer, 2016.





Spirtes, P., Glymour, C. N., and Scheines, R. Causation, prediction, and search. MIT press, 2000.





Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid, A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A., Garriga-Alonso, A., et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. Transactions on Machine Learning Research, 2023.





Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H. W., Chowdhery, A., Le, Q., Chi, E., Zhou, D., and Wei, J. Challenging BIG-bench tasks and whether chain-of-thought can solve them. In Rogers, A., Boyd-Graber, J., and Okazaki, N. (eds.), Findings of the Association for Computational Linguistics: ACL 2023, pp. 13003-13051, Toronto, Canada, July 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023-findings-acl.824.





Swinkels, M. How ideas matter in public policy: a review of concepts, mechanisms, and methods. International Review of Public Policy, 2(2: 3):281-316, 2020.





Taher, M. R. H., Haghighi, F., Gotway, M. B., and Liang, J. Caid: Context-aware instance discrimination for self-supervised learning in medical imaging. In International Conference on Medical Imaging with Deep Learning, pp. 535-551. PMLR, 2022.





Tan, J., Xu, S., Ge, Y., Li, Y., Chen, X., and Zhang, Y. Counterfactual explainable recommendation. In Proceedings of the 30th ACM International Conference on Information & Knowledge Management, pp. 1784-1793, 2021.





Tan, J., Geng, S., Fu, Z., Ge, Y., Xu, S., Li, Y., and Zhang, Y. Learning and evaluating graph neural network explanations based on counterfactual and factual reasoning. In Proceedings of the ACM Web Conference 2022, pp. 1018-1027, 2022.





Tang, K., Huang, J., and Zhang, H. Long-tailed classification by keeping the good and removing the bad momentum causal effect. Advances in neural information processing systems, 33:1513-1524, 2020.





Tang, Y. E. and Tsang, A. S. Inspire me to purchase: Consumers' personal control and preference for underdog brand positioning. Journal of Business Research, 115:101-109, 2020.





Team, G., Anil, R., Borgeaud, S., Wu, Y., Alayrac, J.-B., Yu, J., Soricut, R., Schalkwyk, J., Dai, A. M., Hauth, A., et al. Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805, 2023.





Team, I. Internl'm: A multilingual language model with progressively enhanced capabilities, 2023.





Tian, J. and Pearl, J. A general identification condition for causal effects. In Proceedings of the AAAI Conference on Artificial Intelligence, pp. 567-573, 2002.





Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.





Triantafyllou, S., Singla, A., and Radanovic, G. Actual causality and responsibility attribution in decentralized partially observable markov decision processes. In Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society, pp. 739-752, 2022.





Trinh, T. H., Wu, Y., Le, Q. V., He, H., and Luong, T. Solving olympiad geometry without human demonstrations. Nature, 625(7995):476-482, 2024.





Tu, R., Ma, C., and Zhang, C. Causal-discovery performance of chatgpt in the context of neuropathic pain diagnosis. arXiv preprint arXiv:2301.13819, 2023.





Tufano, M., Agarwal, A., Jang, J., Moghaddam, R. Z., and Sundaresan, N. Autodev: Automated ai-driven development. arXiv preprint arXiv:2403.08299, 2024.





Uysal, S. D. Doubly robust estimation of causal effects with multivalued treatments: an application to the returns to schooling. Journal of Applied Econometrics, 30(5):763-786, 2015.





Vashishtha, A., Reddy, A. G., Kumar, A., Bachu, S., Balasubramanian, V. N., and Sharma, A. Causal inference using llm-guided discovery. In AAAI 2024 Workshop on "Are Large Language Models Simply Causal Parrots?", 2023.





Vig, J., Gehrmann, S., Belinkov, Y., Qian, S., Nevo, D., Singer, Y., and Shieber, S. Investigating gender bias in language models using causal mediation analysis. Advances in neural information processing systems, 33: 12388-12401, 2020.





Waldmann, M. The Oxford handbook of causal reasoning. Oxford University Press, 2017.





Wallace, E., Feng, S., Kandpal, N., Gardner, M., and Singh, S. Universal adversarial triggers for attacking and analyzing nlp. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 2019.





Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., and Bowman, S. R. Glue: A multi-task benchmark and analysis platform for natural language understanding. In International Conference on Learning Representations, 2018.





Wang, A., Pruksachatkun, Y., Nangia, N., Singh, A., Michael, J., Hill, F., Levy, O., and Bowman, S. Superglue: A stickier benchmark for general-purpose language understanding systems. Advances in neural information processing systems, 32, 2019.





Wang, B., Wang, S., Cheng, Y., Gan, Z., Jia, R., Li, B., and Liu, J. Infobert: Improving robustness of language models from an information theoretic perspective. arXiv preprint arXiv:2010.02329, 2020a.





Wang, H., Wu, Z., Jiang, H., Huang, Y., Wang, J., Kopru, S., and Xie, T. Groot: An event-graph-based approach for root cause analysis in industrial settings. In 2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE), pp. 419-429. IEEE, 2021.





Wang, W., Dong, L., Cheng, H., Liu, X., Yan, X., Gao, J., and Wei, F. Augmenting language models with long-term memory. Advances in Neural Information Processing Systems, 36, 2024a.





Wang, X., Wang, Z., Han, X., Jiang, W., Han, R., Liu, Z., Li, J., Li, P., Lin, Y., and Zhou, J. Maven: A massive general domain event detection dataset. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 1652-1671, 2020b.





Wang, X., Chen, Y., Ding, N., Peng, H., Wang, Z., Lin, Y., Han, X., Hou, L., Li, J., Liu, Z., et al. Maven-ere: A unified large-scale dataset for event coreference, temporal, causal, and subevent relation extraction. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pp. 926-941, 2022.





Wang, X., Wei, J., Schuurmans, D., Le, Q. V., Chi, E. H., Narang, S., Chowdhery, A., and Zhou, D. Self-consistency improves chain of thought reasoning in language models. In The Eleventh International Conference on Learning Representations, 2023a.





Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N. A., Khashabi, D., and Hajishirzi, H. Self-instruct: Aligning language models with self-generated instructions. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 13484-13508, 2023b.





Wang, Y., Yu, Z., Yao, W., Zeng, Z., Yang, L., Wang, C., Chen, H., Jiang, C., Xie, R., Wang, J., Xie, X., Ye, W., Zhang, S., and Zhang, Y. PandaLM: An automatic evaluation benchmark for LLM instruction tuning optimization. In The Twelfth International Conference on Learning Representations, 2024b.





Watson, D. S., Gultchin, L., Taly, A., and Floridi, L. Local explanations via necessity and sufficiency: unifying theory and practice. In de Campos, C. and Maathuis, M. H. (eds.), Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence, volume 161 of Proceedings of Machine Learning Research, pp. 1382-1392. PMLR, 27-30 Jul 2021.





Wei, A., Haghtalab, N., and Steinhardt, J. Jailbroken: How does llm safety training fail? Advances in Neural Information Processing Systems, 36, 2024.





Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., et al. Emergent abilities of large language models. Transactions on Machine Learning Research, 2022a.





Wei, J., Wang, X., Schuurmans, D., Bosma, M., );, Xia, F., Chi, E., Le, Q. V., and Zhou, D. Chain-of-thought prompting elicits reasoning in large language models. In Koyejo, S., Mohamed, S., Agarwal, A., Belgrave, D., Cho, K., and Oh, A. (eds.), Advances in Neural Information Processing Systems, volume 35, pp. 24824-24837. Curran Associates, Inc., 2022b.





Wei, T., Luan, J., Liu, W., Dong, S., and Wang, B. Cmath: can your language model pass chinese elementary school math test? arXiv preprint arXiv:2306.16636, 2023a.





Wei, X.-S., Shen, Y., Sun, X., Wang, P., and Peng, Y. Attribute-aware deep hashing with self-consistency for large-scale fine-grained image retrieval. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2023b.





Weinstein, J. N., Collisson, E. A., Mills, G. B., Shaw, K. R., Ozenberger, B. A., Ellrott, K., Shmulevich, I., Sander, C., and Stuart, J. M. The cancer genome atlas pan-cancer analysis project. Nature genetics, 45(10): 1113-1120, 2013.





Weng, L. Prompt engineering. *lilianweng.github.io*, Mar 2023.





Willig, M., Zečević, M., Dhami, D. S., and Kersting, K. Can foundation models talk causality? In UAI 2022 Workshop on Causal Representation Learning, 2022.





Wilson, T. D. and Gilbert, D. T. Explaining away: A model of affective adaptation. Perspectives on Psychological Science, 3(5):370-386, 2008.





Wu, Y., Jia, F., Zhang, S., Wu, Q., Li, H., Zhu, E., Wang, Y., Lee, Y. T., Peng, R., and Wang, C. An empirical study on challenging math problem solving with gpt-4. arXiv preprint arXiv:2306.01337, 2023a.





Wu, Z., Wang, Y., Ye, J., and Kong, L. Self-adaptive in-context learning: An information compression perspective for in-context example selection and ordering. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1423-1436, 2023b.





Xia, Y., Liang, Y., Wen, H., Liu, X., Wang, K., Zhou, Z., and Zimmermann, R. Deciphering spatio-temporal graph forecasting: A causal lens and treatment. Advances in Neural Information Processing Systems, 36, 2024.





Xu, B., Wang, Q., Mao, Z., Lyu, Y., She, Q., and Zhang, Y.  $k$  nn prompting: Beyond-context learning with calibration-free nearest neighbor inference. In The Eleventh International Conference on Learning Representations, 2022.





Xu, G., Liu, J., Yan, M., Xu, H., Si, J., Zhou, Z., Yi, P., Gao, X., Sang, J., Zhang, R., et al. Cvalues: Measuring the values of chinese large language models from safety to responsibility. arXiv preprint arXiv:2307.09705, 2023a.





Xu, L. and Gretton, A. A neural mean embedding approach for back-door and front-door adjustment. In *The Eleventh International Conference on Learning Representations*, 2022.





Xu, Z., Cheng, D., Li, J., Liu, J., Liu, L., and Yu, K. Causal inference with conditional front-door adjustment and identifiable variational autoencoder. In The Twelfth International Conference on Learning Representations, 2023b.





Yang, C.-H. H., Hung, I.-T., Liu, Y.-C., and Chen, P.-Y. Treatment learning causal transformer for noisy image classification. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, pp. 6139-6150, 2023a.





Yang, J., Han, S. C., and Poon, J. A survey on extraction of causal relations from natural language text, 2021a.





Yang, J., Jin, H., Tang, R., Han, X., Feng, Q., Jiang, H., Zhong, S., Yin, B., and Hu, X. Harnessing the power of llms in practice: A survey on chatgpt and beyond. ACM Transactions on Knowledge Discovery from Data, 2023b.





Yang, L., Zhang, S., Qin, L., Li, Y., Wang, Y., Liu, H., Wang, J., Xie, X., and Zhang, Y. Glue-x: Evaluating natural language understanding models from an out-of-distribution generalization perspective. In Findings of the Association for Computational Linguistics: ACL 2023, pp. 12731-12750, 2023c.





Yang, M., Zhang, Y., Fang, Z., Du, Y., Liu, F., Ton, J.-F., Wang, J., and Wang, J. Invariant learning via probability of sufficient and necessary causes. Advances in Neural Information Processing Systems, 36, 2024.





Yang, X., Zhang, H., and Cai, J. Deconfounded image captioning: A causal retrospect. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2021b.





Yang, X., Zhang, H., Qi, G., and Cai, J. Causal attention for vision-language tasks. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 9847-9857, 2021c.





Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., and Narasimhan, K. Tree of thoughts: Deliberate problem solving with large language models. Advances in Neural Information Processing Systems, 36, 2024.





Yu, J., Wang, X., Tu, S., Cao, S., Zhang-Li, D., Lv, X., Peng, H., Yao, Z., Zhang, X., Li, H., Li, C., Zhang, Z., Bai, Y., Liu, Y., Xin, A., Yun, K., GONG, L., Lin, N., Chen, J., Wu, Z., Qi, Y., Li, W., Guan, Y., Zeng, K., Qi, J., Jin, H., Liu, J., Gu, Y., Yao, Y., Ding, N., Hou, L., Liu, Z., Bin, X., Tang, J., and Li, J. KoLA: Carefully benchmarking world knowledge of large language models. In The Twelfth International Conference on Learning Representations, 2024.





Yu, L., Jiang, W., Shi, H., Jincheng, Y., Liu, Z., Zhang, Y., Kwok, J., Li, Z., Weller, A., and Liu, W. Metamath: Bootstrap your own mathematical questions for large language models. In The Twelfth International Conference on Learning Representations, 2023.





Yu, Y., Li, H., Sun, X., Liu, X., Yang, F., Hou, L., Liu, L., Yan, R., Yu, Y., Jing, M., et al. Identification and estimation of causal effects using a negative-control exposure in time-series studies with applications to environmental epidemiology. American Journal of Epidemiology, 190(3):468-476, 2021.





Yuan, Z., Liu, J., Zi, Q., Liu, M., Peng, X., and Lou, Y. Evaluating instruction-tuned large language models on code comprehension and generation. arXiv preprint arXiv:2308.01240, 2023a.





Yuan, Z., Yuan, H., Tan, C., Wang, W., and Huang, S. How well do large language models perform in arithmetic tasks? arXiv preprint arXiv:2304.02015, 2023b.





Zanga, A., Ozkirimli, E., and Stella, F. A survey on causal discovery: theory and practice. International Journal of Approximate Reasoning, 151:101-129, 2022.





Zečević, M., Willig, M., Dhami, D. S., and Kersting, K. Causal parrots: Large language models may talk causality but are not causal. arXiv preprint arXiv:2308.13067, 2023.





Zhai, Y., Luan, T., Doermann, D., and Yuan, J. Towards generic image manipulation detection with weakly-supervised self-consistency learning. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 22390-22400, 2023.





Zhang, B., Zhou, K., Wei, X., Zhao, X., Sha, J., Wang, S., and Wen, J.-R. Evaluating and improving tool-augmented computation-intensive math reasoning. Advances in Neural Information Processing Systems, 36, 2024.





Zhang, C., Bauer, S., Bennett, P., Gao, J., Gong, W., Hilmkil, A., Jennings, J., Ma, C., Minka, T., Pawlowski, N., et al. Understanding causality with large language models: Feasibility and opportunities. arXiv preprint arXiv:2304.05524, 2023a.





Zhang, C., Janzing, D., van der Schaar, M., Locatello, F., and Spirtes, P. Causality in the time of llms: Round table discussion results of clear 2023. Proceedings of Machine Learning Research vol TBD, 1:7, 2023b.





Zhang, J., Tian, J., and Bareinboim, E. Partial counterfactual identification from observational and experimental data. In International Conference on Machine Learning, pp. 26548-26558. PMLR, 2022a.





Zhang, K., Chao, W.-L., Sha, F., and Grauman, K. Video summarization with long short-term memory. In Computer Vision-ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11-14, 2016, Proceedings, Part VII 14, pp. 766-782. Springer, 2016.





Zhang, L., Zhang, L., Shi, S., Chu, X., and Li, B. Lora-fa: Memory-efficient low-rank adaptation for large language models fine-tuning. arXiv preprint arXiv:2308.03303, 2023c.





Zhang, Z., Zhang, A., Li, M., and Smola, A. Automatic chain of thought prompting in large language models. In The Eleventh International Conference on Learning Representations, 2022b.





Zhang, Z., Lei, L., Wu, L., Sun, R., Huang, Y., Long, C., Liu, X., Lei, X., Tang, J., and Huang, M. Safetybench: Evaluating the safety of large language models with multiple choice questions. arXiv preprint arXiv:2309.07045, 2023d.





Zhao, W. X., Zhou, K., Li, J., Tang, T., Wang, X., Hou, Y., Min, Y., Zhang, B., Zhang, J., Dong, Z., et al. A survey of large language models. arXiv preprint arXiv:2303.18223, 2023.





Zheng, C., Liu, Z., Xie, E., Li, Z., and Li, Y. Progressive-hint prompting improves reasoning in large language models. arXiv preprint arXiv:2304.09797, 2023a.





Zheng, G., Yang, B., Tang, J., Zhou, H.-Y., and Yang, S. Ddcot: Duty-distinct chain-of-thought prompting for multimodal reasoning in language models. Advances in Neural Information Processing Systems, 36: 5168-5191, 2023b.





Zhiheng, X., Rui, Z., and Tao, G. Safety and ethical concerns of large language models. In Proceedings of the 22nd Chinese National Conference on Computational Linguistics (Volume 4: Tutorial Abstracts), pp. 9-16, 2023.





Zhong, L. and Wang, Z. A study on robustness and reliability of large language model code generation. arXiv preprint arXiv:2308.10335, 2023.





Zhou, D., Scharli, N., Hou, L., Wei, J., Scales, N., Wang, X., Schuurmans, D., Cui, C., Bousquet, O., Le, Q., et al. Least-to-most prompting enables complex reasoning in large language models. arXiv preprint arXiv:2205.10625, 2022.





Zhou, Z., Wang, Q., Jin, M., Yao, J., Ye, J., Liu, W., Wang, W., Huang, X., and Huang, K. Mathattack: Attacking large language models towards math solving ability. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp. 19750-19758, 2024.





Zhu, K., Wang, J., Zhou, J., Wang, Z., Chen, H., Wang, Y., Yang, L., Ye, W., Gong, N. Z., Zhang, Y., et al. Promptbench: Towards evaluating the robustness of large language models on adversarial prompts. arXiv preprint arXiv:2306.04528, 2023a.





Zhu, W., Liu, H., Dong, Q., Xu, J., Kong, L., Chen, J., Li, L., and Huang, S. Multilingual machine translation with large language models: Empirical results and analysis. arXiv preprint arXiv:2304.04675, 2023b.



# A Prompts for Dataset Construction

An example of assigning real-world meaning for graph nodes by ChatGPT:

Human: For a given pre-defined causal graph with  $N$  nodes, can you please assign real-world meaning to each node and make the entire causal graph plausible? Please use json format to present the result.

Here are some examples:

For a causal graph with 4 nodes  $V1, V2, X, Y$  and edges  $V1->X, V2->X, V1->Y, X->Y$ , we can assign real-world meaning to each node as follows: {"V1": "poverty of the region", "V2": "whether the person is served by a local water company or a global water company", "X": "water quality which the person drinks", "Y": "whether the person gets cholera"}

For a causal graph with 4 nodes  $X$ ,  $V1$ ,  $V2$ ,  $Y$  and edges  $X->V1$ ,  $X->V2$ ,  $V1->Y$ ,  $V2->Y$ , we can assign real-world meaning to each node as follows: {"X": "season", "V1": "whether the sprinkler is on or off", "V2": "weather there is rain", "Y": "whether the ground is wet or dry"}

For a causal graph with 4 nodes  $X$ ,  $V1$ ,  $V2$ ,  $Y$  and edges  $X->V1$ ,  $X->V2$ ,  $V1->Y$ ,  $V2->Y$ , we can assign real-world meaning to each node as follows: {"X": "whether the person is vaccinated", "V1": "whether the person has a severe reaction to the vaccine", "V2": "whether the person has smallpox or not", "Y": "whether the person dies from smallpox"}

Now, for a causal graph with 4 nodes  $A$ ,  $B$ ,  $C$ ,  $D$  and edges  $A->B$ ,  $A->C$ ,  $B->C$ ,  $B->D$ ,  $C->D$ , can you assign real-world meaning to each node? Remember to use json format to answer.

Assistant: {"A": "the amount of time spent studying", "B": "the level of understanding of the subject", "C": "the test score obtained", "D": "the final grade in the course"}

An example of assigning real-world meaning for the value of graph nodes and giving the Chinese translation by ChatGPT:

Human: For a noun or phrase, give the negative and positive adjectives that describe it, and give the Chinese translation of the noun/phrase and the two adjectives. Please use List to present the result and make sure the 5 items are arranged in order.

Here are some examples:

For "whether the student passes the course or not", the result List of 5 items is ["fail", "pass", "学生是否通过课程", "不及格", "及格"]

For "water level in a river", the result List of 5 items is ["low", "high", "河水水位", "低", "高"]

For "availability of public transportation", the result List of 5 items is ["limited", "abundant", "公共交通可用性", "有限", "充足"]

Now for "child's social skills", what is the result List?

Assistant: ["poor", "good", "孩子的社交技能", "差", "好"]

An example of annotating the correlation relationship of a cause-effect pair:

Human: Given two short sentences, if the first is positively related to the second, then you should return 1. Otherwise if they are negatively related, then you should return -1.

# Complexity: ATE (example 1)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Weather conditions has a direct effect on humidity level. Weather conditions has a direct effect on crop yield. Humidity level has a direct effect on crop yield. Humidity level has a direct effect on profit of farmers. Crop yield has a direct effect on profit of farmers. Profit of farmers has a direct effect on economic growth.

Instruction: Consider the average treatment effect (ATE) of profit of farmers on humidity level.

Question: If profit of farmers is changed to be low, will humidity level be more likely to be appropriate?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "No", "PROB": "0.0000"}

Complexity: 5 nodes, 6 edges, real, level-1

# Figure B.1 Analyzing complexity: example 1.

Here are some examples:

Input: ["education level is low", "income level is high"] Output: -1

Input: ["education level is low", "income level is low"] Output: 1

Input: ["education level is high", "income level is high"] Output: 1

Input: ["education level is high", "income level is low"] Output: -1

Input: [“the amount of rainfall is low”, “the soil moisture level is dry”] Output: 1

Input: [“the amount of rainfall is low”, “the soil moisture level is moist”] Output: -1

Input: [“the amount of rainfall is high”, “the soil moisture level is dry”] Output: -1

Input: [“the amount of rainfall is high”, “the soil moisture level is moist”] Output: 1

Input: ["parents' income is high", "child's education level is high"], Output:

Assistant: 1

# B Additional Details for Main Results

# B.1 Examples for Analyzing Complexity

We provide nine examples (from Figure B.1 to Figure B.9) used in Analyzing Complexity (Section 9.1.6).

# B.2 Supplementary Details for Prompt Analysis

In Figure B.10, we demonstrate the relationship between accuracy and the number of IcL examples on English datasets.

# Complexity: ATE (example 2)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Exxp has a direct effect on hnzi. Hnzi has a direct effect on mlhx. Ovlq has a direct effect on hnzi. Wtel has a direct effect on mlhx.

Instruction: Consider the average treatment effect (ATE) of mlhx on exxp.

Question: If mlhx is changed to be high, will exxp be more likely to be high?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "No", "PROB": "0.0000"}

Complexity: 5 nodes, 4 edges, fake, level-1

# Figure B.2 Analyzing complexity: example 2.

# Complexity: ATE (example 3)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Appearance has a direct effect on stress level. Appearance has a direct effect on blood pressure. Appearance has a direct effect on severity of respiratory illnesses. Stress level has a direct effect on blood pressure. Stress level has a direct effect on severity of respiratory illnesses. Stress level has a direct effect on job satisfaction. Blood pressure has a direct effect on severity of respiratory illnesses. Severity of respiratory illnesses has a direct effect on job satisfaction.

Instruction: Consider the average treatment effect (ATE) of severity of respiratory illnesses on appearance.

Question: If severity of respiratory illnesses is changed to be high, will appearance be more likely to be high?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "No", "PROB": "o.0000"}

Complexity: 5 nodes, 8 edges, random, level-1

# Figure B.3 Analyzing complexity: example 3.

# Complexity: ATE (example 4)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Whether a person studies for an exam has a direct effect on whether a person passes the exam. Whether a person studies for an exam has a direct effect on whether a person gets a good grade in the course. Whether a person passes the exam has a direct effect on whether a person gets a good grade in the course.

For those with whether a person studies for an exam being studying, the probability of whether a person passes the exam being not passing is 0.0385. For those with whether a person studies for an exam being not studying, the probability of whether a person passes the exam being not passing is 0.1277.

Instruction: Consider the average treatment effect (ATE) of whether a person studies for an exam on whether a person passes the exam.

Question: If whether a person studies for an exam is changed to be studying, will whether a person passes the exam be more likely to be not passing?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"};

Ground truth: {"ANSWER": "No", "PROB": "-0.0892"}

Complexity: 3 nodes, 3 edges, real, level-2

# Figure B.4 Analyzing complexity: example 4.

# Complexity: ATE (example 5)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Zavj has a direct effect on nvcm. Nvcm has a direct effect on sxxy.

For those with nvcm being low, the probability of sxy being high is 0.7873. For those with nvcm being high, the probability of sxy being high is 0.8173.

Instruction: Consider the average treatment effect (ATE) of nvm on sxxy.

Question: If nvm is changed to be low, will sxy be more likely to be high?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "No", "PROB": "-0.0300"}

Complexity: 3 nodes, 2 edges, fake, level-2

# Figure B.5 Analyzing complexity: example 5.

# Complexity: ATE (example 6)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Appearance has a direct effect on air pressure. Air pressure has a direct effect on education level.

For those with appearance being high, the probability of education level being high is 0.3192. For those with appearance being low, the probability of education level being high is 0.3100.

Instruction: Consider the average treatment effect (ATE) of appearance on education level.

Question: If appearance is changed to be high, will education level be more likely to be high?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"}:

Ground truth: {"ANSWER": "Yes", "PROB": "o.0092"}

Complexity: 3 nodes, 2 edges, random, level-2

# Figure B.6 Analyzing complexity: example 6.

# Complexity: ATE (example 7)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: The amount of time spent studying has a direct effect on the level of understanding of the subject. The amount of time spent studying has a direct effect on the test score obtained. The level of understanding of the subject has a direct effect on the test score obtained. The level of understanding of the subject has a direct effect on the final grade in the course. The test score obtained has a direct effect on the final grade in the course.

For those with the level of understanding of the subject being lack of understanding and the amount of time spent studying being limited, the probability of the final grade in the course being not good is 0.3077. For those with the level of understanding of the subject being deep understanding and the amount of time spent studying being limited, the probability of the final grade in the course being not good is 0.1005. The probability of the amount of time spent studying being limited is 0.4789. For those with the level of understanding of the subject being lack of understanding and the amount of time spent studying being ample, the probability of the final grade in the course being not good is 0.2603. For those with the level of understanding of the subject being deep understanding and the amount of time spent studying being ample, the probability of the final grade in the course being not good is 0.0884. The probability of the amount of time spent studying being ample is 0.5211.

Instruction: Consider the average treatment effect (ATE) of the level of understanding of the subject on the final grade in the course.

Question: If the level of understanding of the subject is changed to be lack of understanding, will the final grade in the course be more likely to be not good?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"};

Ground truth: {"ANSWER": "Yes", "PROB": "o.1888"}

Complexity: 4 nodes, 5 edges, real, level-3

# Figure B.7 Analyzing complexity: example 7.

# Complexity: ATE (example 8)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Aemv has a direct effect on wurj. Aemv has a direct effect on qftw. Aemv has a direct effect on yglq. Wurj has a direct effect on qftw. Qftw has a direct effect on yglq.

For those with qftw being low and aemv being low, the probability of yglq being low is 0.5737. For those with qftw being high and aemv being low, the probability of yglq being low is 0.4238. The probability of aemv being low is 0.1493. For those with qftw being low and aemv being high, the probability of yglq being low is 0.3237. For those with qftw being high and aemv being high, the probability of yglq being low is 0.2036. The probability of aemv being high is 0.8507.

Instruction: Consider the average treatment effect (ATE) of qftw on yglq.

Question: If qftw is changed to be low, will yglq be more likely to be low?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"};

Ground truth: {"ANSWER": "Yes", "PROB": "0.1245"}

Complexity: 4 nodes, 5 edges, fake, level-3

# Figure B.8 Analyzing complexity: example 8.

# Complexity: ATE (example 9)

# Input:

Input Info: Imagine a self-contained, hypothetical world with only the following conditions, and without any unmentioned factors or causal relationships: Education level has a direct effect on employee performance. Education level has a direct effect on severity of respiratory illnesses. Employee performance has a direct effect on severity of respiratory illnesses.

For those with employee performance being high and education level being low, the probability of severity of respiratory illnesses being low is 0.2435. For those with employee performance being low and education level being low, the probability of severity of respiratory illnesses being low is 0.3650. The probability of education level being low is 0.5930. For those with employee performance being high and education level being high, the probability of severity of respiratory illnesses being low is 0.1623. For those with employee performance being low and education level being high, the probability of severity of respiratory illnesses being low is 0.2654. The probability of education level being high is 0.4070.

Instruction: Consider the average treatment effect (ATE) of employee performance on severity of respiratory illnesses.

Question: If employee performance is changed to be high, will severity of respiratory illnesses be more likely to be low?

Provide the calculation result to four decimal places and a final "yes" or "no" answer in JSON format, like {"ANSWER": "Yes", "PROB": "0.1234"};

Ground truth: {"ANSWER": "No", "PROB": "-0.1140"}

Complexity: 3 nodes, 3 edges, random, level-3

# Figure B.9 Analyzing complexity: example 9.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2ca78e6ac98804df453ad70cf37aab7f9bf6b4e5d89a048f6cfb4a632097c4ec.jpg)



(a) Average accuracy of IcL for scenarios in the Natural and Symbolic modes.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/72f3728338ca3b5a929339744143f10a93adcdf90edaa2515d706dab471de45a.jpg)



(b) Average accuracy of IcL for scenarios in the Mathematical mode with  $0 / 1 / 3$  examples.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/029007ad9c29f30915b52ab4904c87d5b09a54505154f10b0346e25bb39e1db0.jpg)



(c) Average accuracy of IcL for scenarios in the Mathematical mode with  $0 / 1 / 2$  examples.



Figure B.10 Relationship between accuracy and the number of IcL examples on English datasets.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3f7d03926334e7e09ca53f1f771377376aa1a006bcc15c70a289cd6a25e9da16.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4cce9dcdcc4f5ede8b8ca80946d6f4288a96c1b68bbdcb5888a6c37d25cb70dc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3aa72312a64f3f55cb76a14ca8b37ad0f3ef1113436aeb1e7161f123ff0cb3bb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/faa470ca62b5195f3b815a3d071cef0f14d619180831eaa46af9efaa2698ecca.jpg)



(a) Distribution of PCD-B (E-(b) Distribution of PCD-B (c) Distribution of PCD-C (E-(d) Distribution of PCD-C (CARE) (COPA) (CARE) (COPA)



Figure C.1 Distribution of causal tasks in PCD.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ae37ecd241f48017d4d282be35e66495982c7eaf791dbcd45e047eeaaea09efe.jpg)



(a) Distribution (CTB)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/31aef6377b2ac2d033f47627a1019cd0cb955c5a18f5957e23a89bf2255dd2b8.jpg)



Distribution of C)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c31b4a1f9df32756fa6c4b34c1bdd7c60f9fa7bf8a3b4f1d8c59e822f6d2364a.jpg)



ECI-B



Distribution of ECI-B (AVEN-ERE)



Figure C.2 Distribution of causal tasks in ECI.


# C Additional Details for Scenario-specific Analysis

# C.1 Causal Discovery

# C.1.1 PCD

The distribution of models' accuracy on PCD is shown in Figure C.1. Figure C.14 illustrates how models perform on PCD. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.15.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/40d302885aa0d0f01ad00c278a4e0ed2ff3d33a55351b48153ee2a7a785db5ef.jpg)



(a) Distribution of CA-B (FA)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/173bb5501b046f25b3f82998a55933c7353f8fce8961c3ba9dfcb6ce2a3f6bff.jpg)



(b) Distribution of CA-B (FP)



Figure C.3 Distribution of causal tasks in CA.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/bda65f1561863f0c84a5c1e7a87623c9b608830ce747481d923a6e796c134ac2.jpg)



(a) Distribution (ATE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/7c783145d43557a8e9b87e272ecdba154a4e7f84069613fb473be8e01260a8c4.jpg)



Distribution of ATE-PT (ATE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/73f203f15604143475cedb8cdf1b9411b3b153dc52e98de1d8f142738c217964.jpg)



(c) Distribution of ATE-B (ATE-natural)



Figure C.4 Distribution of causal tasks in ATE.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b3a792d3078919542f1f38c58c60780740c46b5e12aa328343ebb1734d15d0fd.jpg)



(a) Distribution (CDE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f365d06e709b3c673824445622e198517e7d7bf335bb14e2275624cbaa39b5e8.jpg)



Distribution of DE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a258ac2ab6ed647c347f914f22e8d3204937211b561f1df47e7876fa56b2d7a8.jpg)



(c) Distribution of CDE-B (CDE-natural)



Figure C.5 Distribution of causal tasks in CDE.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8016ece2f831b6a27eac9214555a301c75e0e10db20e078e54b306ab9ed1c076.jpg)



(a) Distribution of CEI-B (0.2-(b) Distribution of CEI-B (0.4-(c) Distribution of CEI-B (0.6-(d) Distribution of CEI-B (0.8-UC) UC) UC) UC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9debafe1ffc825785d572f97fdc94a670d7761bf56c0adb6b9cd2fb08c25f3b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0d95df29c2481558147e84e6892d67c24faa7f8840691efeb2cd5ac4e702429a.jpg)



(c) Distribution of CEI-B (0.6-(d) Distribution of CEI-B (0.8-UC) UC)



Figure C.6 Distribution of causal tasks in CEI.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/10e677537379cd2557218c4b454e595ee40c72176d75297a4f2d8da4fd92a844.jpg)



(a) Distribution of BAS-B (b) Distribution of BAS-C (c) Distribution of BAS-C (d) Distribution of BAS-C (backadj) (max-BAS) (min-BAS) (mix-BAS)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/e90832457600766b1d520d6de4f7349981a611173e0b7d94a20c512cb922f6c9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c44164f1693fcfe2e03d7dba03a2bd02047fffbd6d52378d068b7ca0c0b60bd3.jpg)


(c) Distribution of BAS-C (d) Distribution of BAS-C (min-BAS) (mix-BAS)


Figure C.7 Distribution of causal tasks in BAS.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/4d7c59c22e641391b3bf3e686f6ec607b41551680d8c068609f96fd12e1b5682.jpg)



(a) Distribution (CRASS)



of CR-C (b) Distribution of CR-B (det-counterfactual)



Figure C.8 Distribution of causal tasks in CR.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/767baaa02a0223decdc235e4ac1ded4b3457de3d756ca98368ab18c8035be859.jpg)



(a) Distribution of ETT-P (ETT-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8784e75862dee74257bc6304451988923fabf420000ff23decad68ace9e38b6c.jpg)



(b) Distribution of ET (ETT-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2adc5af7f03906b3f7a3d144e56798272d020b063f2b3c0e78442033ba0c0a8a.jpg)



T-P (c) Distribution of ETT-B (ETT-natural)



Figure C.9 Distribution of causal tasks in ETT.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1d765e491eec85779e5dacf513766e7324acb1fb752e9008a649f4e576bbd474.jpg)



(a) Distribution of NDE-P (NDE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/68faffdecfb6283ebb0463592ba9b18539399d0b32b4204994aeff625a75ac46.jpg)



(b) Distribution of NDE-P (NDE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6f8925a926f2fbc291e03de746c3a44ec670cf9c201cf3e8657663de12c88522.jpg)



(c) Distribution of NDE-B (NDE-natural)



Figure C.10 Distribution of causal tasks in NDE.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/070b3667b8bfd30a2b1410fa7e2b140b0bea82ff311f9007c82cc572b5e4ef02.jpg)



(a) Distribution of NIE-P (NIE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/fbc787438c76154f2479349d9b83b1b720fd14505abcb8cfdd76320506485864.jpg)



(b) Distribution of NIE-P (NIE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ddc7f1a7dbae6c7f84ad027236c1af74a6caa14c1986ff3b28b6f40b61a46187.jpg)



(c) Distribution of NIE-B (NIE-natural)



Figure C.11 Distribution of causal tasks in NIE.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2d23b808277c8d9bfee4bf92310d6f64990b36fa90cb1aea508fab27f156fff3.jpg)



(a) Distribution of PN-P (PN-(b) Distribution of PN-P (PN-basic) hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/2e066090757b88083a37f8a19b714492137aef770ed5f82f08d51a1db6a6667b.jpg)



Figure C.12 Distribution of causal tasks in PN.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a0b3ae6efd694480017d50b8cf92f00c4ce6db943406cce3f35bedc489a80c2b.jpg)



(a) Distribution of PS-P (PS-(b) Distribution of PS-P (PS-basic) hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b6b1ed64a68f2d7bde8b9cc6e6de09d945610a5e8f8d6371309661ef6732c6a8.jpg)



Figure C.13 Distribution of causal tasks in PS.


# C.1.2 ECI

The distribution of models' accuracy on ECI is shown in Figure C.2. Figure C.16 illustrates how models perform on ECI. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.17.

# C.1.3 CA

The distribution of models' accuracy on CA is shown in Figure C.3. Figure C.18 illustrates how models perform on CA. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.19.

# C.2 Intervention

# C.2.1 ATE

The distribution of models' accuracy on ATE is shown in Figure C.4. Figure C.20 illustrates how models perform on ATE. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.21.

# C.2.2 CDE

The distribution of models' accuracy on CDE is shown in Figure C.5. Figure C.22 illustrates how models perform on CDE. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/e0a1629739cb255785d4e7f2d849e87a0d0735030d15cd61312cabceeed143a1.jpg)



(a) Model performance of PCD-B (E-CARE)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3c2ae4a45f31f5c593e968102cbe3db40138c1660a83626b484d6e2f9efe9d8a.jpg)



(b) Model performance of PCD-B (COPA)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/de81861628546ac4cffd5d64f09cc166a19e4187dbda5135d3582a5493598923.jpg)



(c) Model performance of PCD-C (E-CARE)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/b8d63f624d220ecdd1dbff04934310747fb75acc0a8e61c047af730550af26b1.jpg)



(d) Model performance of PCD-C (COPA)



Figure C.14 Heatmaps of model performance of causal tasks in PCD. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d8b732409b785a68ff4036da722e162c50849b3489745bde6ced223110af43f1.jpg)



(a) Prompt gain of PCD-B (E-CARE)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/7f13576d809b3bff0c4f2bf8b7f78bd9dd7705e6820a383a7d3357b8acf14fb9.jpg)



(b) Prompt gain of PCD-B (COPA)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ec8fc020e59d88df92df9a8194a30552b938f33ee1dcac5fa714843b8fc70a49.jpg)



(c) Prompt gain of PCD-C (E-CARE)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/154fedcddaddfcd59f1f5819b1ec329a3f6abc21ec62868e2998d15591923e87.jpg)



(d) Prompt gain of PCD-C (COPA)



Figure C.15 Heatmaps of prompt gain of causal tasks in PCD. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3f3cffbd099aa0572e1f44348878d28282ea9989ff1c32f9dd8dfc83fbd9b98a.jpg)



(a) Model performance of ECI-B (CTB)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/01dd04a466d0703baf2c4973a6b828897c0d10791e1e37067970ee6d591d96aa.jpg)



(b) Model performance of ECI-B (ESC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cf96e25fbc3674ea39ba03b150cdb3fe374e4da672a63f0f29be5548de9a2940.jpg)



(c) Model performance of ECI-B (MAVEN-ERE)



Figure C.16 Heatmaps of model performance of causal tasks in ECI. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/43ace3c4675744561d59835941b79a07c42621200a185c3b5ea87895b3d1f193.jpg)



(a) Prompt gain of ECI-B (CTB)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d1ba51dfb67612dc09918afeeaef2959972469856867b8c5dc94f3c9107e5209.jpg)



(b) Prompt gain of ECI-B (ESC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/efdc95d73024f33884ec0da628aa15236dcf1da467bce84f3449f03cb17b5950.jpg)



(c) Prompt gain of ECI-B (MAVEN-ERE)



Figure C.17 Heatmaps of prompt gain of causal tasks in ECI. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c873dd1d8a96aadda75c3249273d01acbc11680859fa08306dc91a51aac8822a.jpg)



(a) Model performance of CA-B (FA)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/0c998d688858aec7940adc24c3fdeb4793a0558b2a424e70394789d970a83db7.jpg)



(b) Model performance of CA-B (FP)



Figure C.18 Heatmaps of model performance of causal tasks in CA. The models and prompts are sorted by their averages.


the used prompt) is demonstrated in Figure C.23.

# C.2.3 CEI

The distribution of models' accuracy on CEI is shown in Figure C.6. Figure C.24 illustrates how models perform on CEI. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.25.

# C.2.4 BAS

The distribution of models' accuracy on BAS is shown in Figure C.7. Figure C.26 illustrates how models perform on BAS. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.27.

# C.3 Counterfactuals

# C.3.1 CR

The distribution of models' accuracy on CR is shown in Figure C.8. Figure C.28 illustrates how models perform on CR. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.29.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/71be57ef03b1a17762a2d972ecc1a7d6c4980daaaa4fe0dac82cd23e1543881e.jpg)



(a) Prompt gain of CA-B (FA)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8cbf613f1a4f76fa5a330c1506820a354ad040d6030dfc058dcfc6f3a202e8a0.jpg)



(b) Prompt gain of CA-B (FP)



Figure C.19 Heatmaps of prompt gain of causal tasks in CA. The models and prompts are sorted by their averages.


# C.3.2 ETT

The distribution of models' accuracy on ETT is shown in Figure C.9. Figure C.30 illustrates how models perform on ETT. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.31.

# C.3.3 NDE

The distribution of models' accuracy on NDE is shown in Figure C.10. Figure C.32 illustrates how models perform on NDE. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.33.

# C.3.4 NIE

The distribution of models' accuracy on NIE is shown in Figure C.11. Figure C.34 illustrates how models perform on NIE. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.35.

# C.3.5 PN

The distribution of models' accuracy on PN is shown in Figure C.12. Figure C.36 illustrates how models perform on PN. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.37.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/00750dff33ebeba6fd6e0e3991b43bdff9d2ff9e0540aff59d36f396286e7a3d.jpg)



(a) Model performance of ATE-P (ATE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/eb56e67710ce4fbe1c6a52d903598ea9b68afe4cdde9503ad392821dfdf46ab7.jpg)



(b) Model performance of ATE-P (ATE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/5189903a248ad553648aaf7a8ebcdaf479be2981e7972dea4941e432ee75d6c8.jpg)



(c) Model performance of ATE-B (ATE-natural)



Figure C.20 Heatmaps of model performance of causal tasks in ATE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9bda0b5524e6ccb7fc121ad86237714fd3b873c5c14dc8a641e4fed62a853b86.jpg)



(a) Prompt gain of ATE-P (ATE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/79e76db0ab97bc3f39a2c8f933c267fd50703a47b00f40e79bf3d5790c3588a5.jpg)



(b) Prompt gain of ATE-P (ATE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/778a15ca29d146b5c92f67eb36ace58d26d3586078f4e4a5406dc91ce0816bb5.jpg)



(c) Prompt gain of ATE-B (ATE-natural)



Figure C.21 Heatmaps of prompt gain of causal tasks in ATE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/305f9784f922d0893e7e78cc87ba299c47f0d5137c1150db36ae67382cd4fc90.jpg)



(a) Model performance of CDE-P (CDE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/44b8c5d0b5adf11b29c993ad91a20ee1331882317b718e3ed0d0b89f17a2f61c.jpg)



(b) Model performance of CDE-P (CDE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/bd8394294594c4dab6abaf549d18326b277d166ea4a2ec032319123013823210.jpg)



(c) Model performance of CDE-B (CDE-natural)



Figure C.22 Heatmaps of model performance of causal tasks in CDE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/efc9132340af06b8507afa7e6b4fe2b687f8a43217bde93c13f7618395f7916e.jpg)



(a) Prompt gain of CDE-P (CDE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ac53ee97ff736bfaf46f25b4767ab47d83d2ac46063ea037ea0cf19d9e12c908.jpg)



(b) Prompt gain of CDE-P (CDE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d25f4dffeeb8678a4f282844256e0c315d12be76017f3ab75b24dbb08ae29df7.jpg)



(c) Prompt gain of CDE-B (CDE-natural)



Figure C.23 Heatmaps of prompt gain of causal tasks in CDE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/7b33acc4c9f4785f944effc3c583b5f60120d949113e2cf1af2e40cb2886dbc1.jpg)



(a) Model performance of CEI-B (0.2-UC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a5b6c5043ada922a6e71bb978fb9331528cf25db9aa927d03d50a6968d12b866.jpg)



(b) Model performance of CEI-B (0.4-UC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d2a0a838aaea04197ca52feb90e864a3b653600b23d6012d757564fa8c3472e2.jpg)



(c) Model performance of CEI-B (0.6-UC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/20c985f3a7289b2a228bd973ef92545e46bafd364025c67c7d9d4034458ec41e.jpg)



(d) Model performance of CEI-B (0.8-UC)



Figure C.24 Heatmaps of model performance of causal tasks in CEI. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c6baa1f553efa2ebdf4e09ec1a1086e6c50da462c9f41ef1f25670c49a91c11b.jpg)



(a) Prompt gain of CEI-B (0.2-UC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6a116eda51f54202100cd033faa925e327d105991a5b251cba96d39b65638577.jpg)



(b) Prompt gain of CEI-B (0.4-UC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/1c11e7c0a074e056e13eaa8ce5edef96ec7f7c8d3c590d0f4a9569a805603432.jpg)



(c) Prompt gain of CEI-B (0.6-UC)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/566b5d297f1a64ae8045af231b3f3083126b2ffaf89ab5f7ae66d39c5a88c02c.jpg)



(d) Prompt gain of CEI-B (0.8-UC)



Figure C.25 Heatmaps of prompt gain of causal tasks in CEI. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/e1ebb4bf6e3abf7cbf6facb6ba8cec6087e73590d49755b74f443ba4caaefa74.jpg)



(a) Model performance of BAS-B (backadj)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/95890f5e9d78c86ff55be7226c57b2c28971aea67bfe9f5b0fa72522b504c13f.jpg)



(b) Model performance of BAS-C (max-BAS)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3e3ff6ecca8c5786614d3190319b59712958284234fd5c589b99ab8e0cfe19a3.jpg)



(c) Model performance of BAS-C (min-BAS)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9a98b3e7b19e0521c57c233390fac51352a92e70e1fdc84f3a43aa974b7385ac.jpg)



(d) Model performance of BAS-C (mix-BAS)



Figure C.26 Heatmaps of model performance of causal tasks in BAS. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3c12d52fad60b09cdc5b4a28ea5c7315dbb165e3deacc037de76e52ca6d5c3cd.jpg)



(a) Prompt gain of BAS-B (backadj)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/cc0aa9e28170732cf64792ff0ce7f60a8802e6c96b26604b07e0350aef469c90.jpg)



(b) Prompt gain of BAS-C (max-BAS)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6108286c2099755d5972d91fe539ff4a14774c38a592015e14c48351f3fbb726.jpg)



(c) Prompt gain of BAS-C (min-BAS)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8c94062dda2a77791040f70908db57547cce82ecdbb267a8f65939ff5af56e1f.jpg)



(d) Prompt gain of BAS-C (mix-BAS)



Figure C.27 Heatmaps of prompt gain of causal tasks in BAS. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/81ab586d442016afd97536c26180600b34628232d238239d726c4e8c71b09cd9.jpg)



(a) Model performance of CR-C (CRASS)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/eca89d0fbf7b6bbc4c0005a327b477b6897a7e94bbaf14a098d113e3dd678891.jpg)



(b) Model performance of CR-B (det-counterfactual)



Figure C.28 Heatmaps of model performance of causal tasks in CR. The models and prompts are sorted by their averages.


# C.3.6 PS

The distribution of models' accuracy on PS is shown in Figure C.13. Figure C.38 illustrates how models perform on PS. The prompt gain (i.e., accuracy improvement against the basic prompt on the model with the used prompt) is demonstrated in Figure C.39.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a1f860db193a71308961b3d9250019ea22ae3735356ad39fc1fb84ed37c97323.jpg)



(a) Prompt gain of CR-C (CRASS)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/67c5aa37b658d169833115b3f1e215907ee98b1c675eb77fdb6cba3088889b35.jpg)



(b) Prompt gain of CR-B (det-counterfactual)



Figure C.29 Heatmaps of prompt gain of causal tasks in CR. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f4b289943b69ce72577f949b72ef950c0568adf187933f1510fc75b0b08c2ae7.jpg)



(a) Model performance of ETT-P (ETT-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/882b85effba5c9c8df3280b790e073c9777bc0138ada9c7ea706d5eb53718505.jpg)



(b) Model performance of ETT-P (ETT-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ce25862d2b16809a4b38315af064ea1895c8e6e17e9fd68b73294f860540edb0.jpg)



(c) Model performance of ETT-B (ETT-natural)



Figure C.30 Heatmaps of model performance of causal tasks in ETT. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/f079cb3ee274e849deb5f17c91022b42f76edab892a86e9a8901e515ede4c5db.jpg)



(a) Prompt gain of ETT-P (ETT-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/a146d0cc2d3d2c62eb67ecbab34f50671597d909dfafa2c99649f084a12a589b.jpg)



(b) Prompt gain of ETT-P (ETT-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/284e66432c61f04520dd5ce1a672637d2642c517d85e8ab3ccb780b1faac3c12.jpg)



(c) Prompt gain of ETT-B (ETT-natural)



Figure C.31 Heatmaps of prompt gain of causal tasks in ETT. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/576f866d62c9c35de84c1cd88c0fec20d9a27d01f6cc1bd295d71eb2ad5cf78f.jpg)



(a) Model performance of NDE-P (NDE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9d6d99f1658b759af59de1862c366a8dfcf45bc82366e01c0fefe81f30acee4d.jpg)



(b) Model performance of NDE-P (NDE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ecfdd57fa5473b59f6cd1402fba6bcf6eff04e34a7e792c4c98949ca0694663e.jpg)



(c) Model performance of NDE-B (NDE-natural)



Figure C.32 Heatmaps of model performance of causal tasks in NDE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/83b86410d236e321145117d192d6ba479b9b1aa1117228e4dfeef663b526e45e.jpg)



(a) Prompt gain of NDE-P (NDE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8b63cb0d0e398040ca83b24000b902988440be75775414b7129289ab16a17f10.jpg)



(b) Prompt gain of NDE-P (NDE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/bbecc51b6da166db2713ba9504a533151212f349783faeef77792988792fe35c.jpg)



(c) Prompt gain of NDE-B (NDE-natural)



Figure C.33 Heatmaps of prompt gain of causal tasks in NDE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/8a0247dd5b0976c55e732b40023d245c2d54fbefbca21fcf34ebe90c0386889a.jpg)



(a) Model performance of NIE-P (NIE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/9d465f75da92207ff9e6ef410ebc0d1c03e880029c344dbbae40ff6f64396c98.jpg)



(b) Model performance of NIE-P (NIE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6695d832913bb7b4e15fefe8ce1d46c6c227c9ff287e1886f9e33ecd1bac94e1.jpg)



(c) Model performance of NIE-B (NIE-natural)



Figure C.34 Heatmaps of model performance of causal tasks in NIE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/6ee5eaca2ff4371f475f6789683e209407865c36130581b3e39ad2f7f63a5c99.jpg)



(a) Prompt gain of NIE-P (NIE-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/05bf63396c9985019aa86af797e8a0a269d9606df69f9e7a6b955734d722381c.jpg)



(b) Prompt gain of NIE-P (NIE-hard)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/d3c0b78d12ef6a21c07704b63282b3f010115126b1f64cff4a077fe2de282d38.jpg)



(c) Prompt gain of NIE-B (NIE-natural)



Figure C.35 Heatmaps of prompt gain of causal tasks in NIE. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/06b8e076ba87c73630caf15757514d45af77c7903b9cdbbbcb501e585c6c2544.jpg)



(a) Model performance of PN-P (PN-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/3a26391edfedfaa37064177d4edc9bb8ef0fad4fad08e35ee8957d9bb28a9d66.jpg)



(b) Model performance of PN-P (PN-hard)



Figure C.36 Heatmaps of model performance of causal tasks in PN. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ed9bd18f13168ff3b5e76d1843d54d9b33b595f157a6378acc93d4a9f97cdd70.jpg)



(a) Prompt gain of PN-P (PN-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/ae697d7e02adcb148e7e68d7eb449c6dc67e704e327288429288bbcb4876ea4a.jpg)



(b) Prompt gain of PN-P (PN-hard)



Figure C.37 Heatmaps of prompt gain of causal tasks in PN. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/dba0b230844aa8a25c7107cce774974245d60f8a10e16194664093461632c4f7.jpg)



(a) Model performance of PS-P (PS-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/c8809b5bcbe8ca7168b20e170fd846d44121c1ac50d95116c129e1b46b51b81c.jpg)



(b) Model performance of PS-P (PS-hard)



Figure C.38 Heatmaps of model performance of causal tasks in PS. The models and prompts are sorted by their averages.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/420c3f8e76573fab3b1931770b9c7f195bf0bcf15ffeda73abff8c509fec6d63.jpg)



(a) Prompt gain of PS-P (PS-basic)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-01-29/fa717245-0c65-4479-8b0e-73f8e08b5e43/89f528447829d006a33f664f28423a9690102e2c85760f0fc3dc462099b54065.jpg)



(b) Prompt gain of PS-P (PS-hard)



Figure C.39 Heatmaps of prompt gain of causal tasks in PS. The models and prompts are sorted by their averages.


<table><tr><td>Model</td><td>API Version</td><td>Evaluation Date</td></tr><tr><td>ada</td><td>ada</td><td></td></tr><tr><td>babbage</td><td>babbage</td><td></td></tr><tr><td>curie</td><td>curie</td><td></td></tr><tr><td>davinci</td><td>davinci</td><td></td></tr><tr><td>text-ada-001</td><td>text-ada-001</td><td></td></tr><tr><td>text-babbage-001</td><td>text-babbage-001</td><td></td></tr><tr><td>text-curie-001</td><td>text-curie-001</td><td>June 2023~December 2023</td></tr><tr><td>text-davinci-001</td><td>text-davinci-001</td><td></td></tr><tr><td>text-davinci-002</td><td>text-davinci-002</td><td></td></tr><tr><td>text-davinci-003</td><td>text-davinci-003</td><td></td></tr><tr><td>GPT-3.5-Turbo</td><td>gpt-3.5-turbo</td><td></td></tr><tr><td>GPT-4</td><td>gpt-4</td><td></td></tr><tr><td>Claude2</td><td>claude-2</td><td></td></tr></table>

Tab. D.1 API Version and evaluation date of limited-access model. API version means the name of the model specified in the API when making a call for inference. The evaluation date refers to the date on which the models are assessed.

# D Models

# D.1 Limited-access Models

To ensure the reproducibility of our results, for limited-access models, we report the API version and our evaluation time in Table D.1.