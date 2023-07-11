# Goal

Create an automated essay scoring system using prompt engineering techniques. Train a language model to evaluate and score essays based on specific criteria, such as grammar, coherence, and argumentation. Design a prompt structure that allows the model to analyze the essays comprehensively and provide constructive feedback. Implement a user interface where students can submit their essays and receive instant scores and feedback for improvement.

# Instructions

1. Project Overview:
   - The goal of this capstone project is to create an automated essay scoring system using prompt engineering techniques.
   - The system should be able to evaluate and score essays based on specific criteria, such as grammar, coherence, and argumentation.
   - Additionally, the system should provide constructive feedback to help students improve their writing skills.
   - You will design a prompt structure that allows the language model to comprehensively analyze essays.

2. Setting up the Environment:
   - Ensure you have access to a machine with sufficient computational resources, preferably with a GPU.
   - Install the necessary software dependencies, including Python and the required libraries (e.g., TensorFlow, PyTorch, or Hugging Face's Transformers).
   - Set up a virtual environment to keep your project dependencies isolated.

3. Data Collection:
   - Obtain a dataset of essays for training and evaluation purposes.
   - The dataset should include essays with scores or annotations for the specific criteria you plan to evaluate.
   - You may consider using publicly available essay datasets or reach out to educational institutions for potential collaborations.

4. Data Preprocessing:
   - Preprocess the essay dataset to ensure it is suitable for training the language model.
   - Perform tasks such as tokenization, lowercasing, removing stop words, and handling special characters or punctuation.
   - Split the dataset into training, validation, and testing sets to assess the model's performance.

5. Language Model Selection:
   - Choose a language model architecture that is suitable for natural language processing tasks.
   - Options include models like GPT-3, BERT, or any other state-of-the-art models available at the time of implementation.

6. Prompt Engineering:
   - Design a prompt structure that guides the language model to evaluate essays comprehensively.
   - The prompt should address specific criteria, such as grammar, coherence, argumentation, or any other relevant aspects of essay evaluation.
   - Use LangChain to implement the prompt structure.

7. Evaluation and Iteration:
   - Experiment with different prompt designs to determine the most effective approach for your scoring system.
   - Evaluate the performance of your automated essay scoring system using appropriate evaluation metrics.
   - Assess the system's effectiveness in scoring essays accurately and providing constructive feedback.
   - Analyze any limitations or biases in the system and brainstorm potential solutions for improvement.
   - Iterate on the system design, prompt structure, or training approach based on the evaluation results.

8. Language Model Training (optional):
   - Fine-tune the selected language model on your essay dataset, considering the scoring criteria as your training objective.
   - Experiment with different hyperparameters and training configurations to optimize the model's performance.

9. User Interface Development:
   - Develop a user interface where students can submit their essays and receive instant scores and feedback.
   - The interface should be intuitive and user-friendly, allowing for easy essay submission and result display.
   - Consider using web development technologies like HTML, CSS, and JavaScript for the user interface implementation.
   - Connect the user interface with the automated scoring system, ensuring seamless integration and real-time feedback.

10. Documentation and Presentation:
    - Create comprehensive documentation that describes the project's architecture, methodology, and implementation details.
    - Include instructions on how to set up and run the automated essay scoring system.
    - Prepare a presentation summarizing your project, highlighting the challenges faced, solutions implemented, and results achieved.
    - Clearly explain the benefits and limitations of your system and discuss potential future enhancements.

11. Finalize and Submit the Project:
    - Review and revise your project documentation, ensuring it is complete and well-organized.
    - Make sure your code is properly commented and follows best practices for readability and maintainability.
    - Double-check that your automated essay scoring system and user interface are fully functional and bug-free.
    - Publish your project on GitHub, including the documentation and presentation.

# Project Rubric

1. Problem Definition:
   [x] Clearly defined problem statement for building an automated essay scoring system.
   [x] Specified evaluation criteria, including grammar, coherence, argumentation, and any additional factors.
   [x] Identified target audience for the system (e.g., students, teachers, educational institutions).

2. Data Collection:
   [x] Compiled a dataset of exams and corresponding correction criteria.
   [ ] Obtained a dataset of exam essay questions and corresponding correction criteria.
   [ ] Gathered a dataset of essays manually scored by human evaluators.
   [ ] Included scores assigned by human evaluators for each essay.

3. Data Preprocessing:
   [ ] Cleaned the dataset by removing irrelevant information and formatting inconsistencies.
   [ ] Performed text preprocessing tasks such as tokenization, lowercasing, removing stop words, and applying stemming or lemmatization.
   [ ] Extracted relevant features from the essays, such as word counts, sentence lengths, and linguistic or stylistic features.

4. Prompt Engineering:
   [ ] Designed a prompt structure covering the evaluation criteria.
   [ ] Broke down the prompt into sub-questions or guidelines for comprehensive essay analysis.
   [ ] Ensured clear instructions and expectations for the essays to be scored.

5. Evaluation and Iteration:
   [ ] Evaluated the system's performance using the testing set.
   [ ] Measured accuracy, precision, recall, and other relevant evaluation metrics.
   [ ] Collected user feedback to assess system usability and effectiveness.

6. Language Model Training (optional):
   [ ] Selected an appropriate language model architecture for training.
   [ ] Split the dataset into training, validation, and testing sets.
   [ ] Trained the language model using the training set and optimized it with suitable loss function and evaluation metrics.
   [ ] Monitored and fine-tuned the model's performance on the validation set.

7. User Interface Development:
   [ ] Built a user interface for essay submission, scoring, and feedback.
   [ ] Designed a user-friendly form for inputting essays and selecting relevant options.
   [ ] Integrated the trained model into the user interface for processing and generating scores and feedback.
   [ ] Displayed scores and feedback in a clear and understandable format.

8. Iterative Improvement:
   [ ] Analyzed system strengths and weaknesses based on evaluation results and user feedback.
   [ ] Identified areas for improvement, such as enhancing the prompt structure, adding evaluation criteria, or refining the scoring algorithm.
   [ ] Iterated on the system, making necessary updates and enhancements.

9. Documentation and Presentation:
   [ ] Documented the entire process, including data collection, preprocessing, model architecture, training, UI development, and evaluation.
   [ ] Provided clear instructions for system usage and score/feedback interpretation.
   [ ] Prepared a presentation or report summarizing the project, findings, challenges, and lessons learned.

10. Conclusion:
    [ ] Summarized achievements of the automated essay scoring system and its potential applications.
    [ ] Discussed limitations and future directions for improvement.