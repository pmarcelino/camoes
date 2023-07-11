# Introduction

The objective of this project is to develop an **automated essay scoring system** using Large Language Models (LLMs). This system aims to assist teachers in evaluating and scoring essays based on specific criteria, including grammar, coherence, and argumentation. The Portuguese National Exam criteria will serve as the standard for assessment. Furthermore, the system will provide constructive feedback to help students enhance their writing skills. This tool is dedicated to **teachers**, inspired by the valuable contributions of my parents, who were teachers themselves.

# Project description

The automated essay scoring system will leverage the capabilities of Large Language Models, such as GPT-3.5, to provide a practical solution for essay evaluation. The system will consider multiple factors while assessing essays, ensuring a comprehensive evaluation process. The primary focus will be on the following criteria:

Grammar: The system will analyze the essays for grammatical accuracy, including proper sentence structure, word usage, punctuation, and spelling. It will identify errors and provide suggestions for improvement.

Coherence: Coherence refers to the logical flow of ideas and how well the essay connects various paragraphs and sections. The system will evaluate the clarity of the essay's structure, transitions between ideas, and the overall cohesion of the content.

Argumentation: The system will assess the effectiveness of the essay's arguments, evaluating the strength of supporting evidence, logical reasoning, and the ability to present a persuasive case. It will consider the clarity and coherence of the essay's thesis statement.

The scoring system will be trained on a large corpus of essays, leveraging the power of machine learning to recognize patterns and assess essays based on the established criteria. This training process will involve providing the system with a set of human-scored essays to learn from, enabling it to make accurate predictions about the quality of new essays.

Once an essay is evaluated, the system will provide an overall score based on the predefined criteria. It will also generate detailed feedback highlighting specific strengths and weaknesses. The feedback will include suggestions for improvement, alternative sentence structures, and examples of better word choices. This feedback aims to guide students in developing their writing skills and addressing areas that require attention.

# Data

Data was downloaded from [here](https://www.examesnacionais.com.pt/exames-nacionais-12-ano.php), which includes all Portuguese exams - both the 1st and 2nd phases - along with the corresponding correction criteria from 2008 to 2022.

Answers were generated artificially using GPT-4.
