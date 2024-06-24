# Language Translator

## Overview of this project
Language Translator is a robust application that uses the Google API to provide translation services. The application not only translates text into different languages but also offers audio output for the translations. This project leverages SQLite as the database to manage and store various aspects of the translation service.

## Features
- Translate text between multiple languages using Google API.
- Generate audio output for translations.
- Manage user feedback.
- Maintain a history of translations.
- Calculate and store the cost of translations.
- Support for multiple target languages.

## Database Structure
The project uses an SQLite database with the following tables:

1. **user**
   - Stores information about users of the application.
   - Columns: `user_id`, `username`, `email`, `password`, `created_at`

2. **feedback**
   - Stores user feedback on translations.
   - Columns: `feedback_id`, `user_id`, `translation_id`, `rating`, `comments`, `created_at`

3. **target_language**
   - Stores information about the languages available for translation.
   - Columns: `language_id`, `language_name`, `language_code`

4. **translation_cost**
   - Stores the cost associated with translations.
   - Columns: `cost_id`, `language_id`, `cost_per_word`

5. **translationhistory**
   - Stores a history of translations performed by users.
   - Columns: `history_id`, `user_id`, `source_text`, `translated_text`, `source_language`, `target_language`, `translation_date`, `cost_id`

## Setup and Installation
To set up and run the Language Translator project, follow these steps:

1. **Clone the repository:**

2. **Install the required dependencies:**
- Ensure you have Python and pip installed.
- Install necessary packages:
  ```
  pip install -r requirements.txt
  ```

3. **Set up the database:**
- Run the provided script to create and populate the database tables.

4. **Configure the Google API:**
- Obtain API credentials from Google Cloud.
- Set up the API key in your project configuration.

5. **Run the application:**

## Usage
- Navigate to the application in your web browser.
- Enter text to translate, select the target language, and get the translation along with audio output.
- View translation history and manage feedback.

## Contribution
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or feedback, please contact [your-email@example.com].

---

*Thank you for using Language Translator! We hope it serves your translation needs efficiently.*

