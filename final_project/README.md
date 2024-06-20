# JJ No Fish
#### Video Demo:  <https://www.youtube.com/watch?v=kuz0dl_NoR4>
#### Description:
*Background*
I have been suffering from a rare phobia called Ommetaphobia.
> Ommetaphobia (or rarely oculophobia) is an irrational fear of eyes. This phobia can cause distress and discomfort when exposed to visual stimuli containing eyes or eye-related images.

My exact symptom is that I dont like fish. I cant look at a live fish, a fish video or a fish picture. When ever I see a fish image or 1 second clip in a video, it feels like a jump scare. I have always wished to be able to filter out information that I dont want and replace with safe contents, therefore JJ No Fish ver 1.0. I wish as the actual extension of this simple mechanism, the future versions would be able to filter out images, frames inside videos and etc.

## Purpose
The purpose of this project is to develop a supportive application for individuals coping with specific phobias or triggers. The application aims to alleviate anxiety and discomfort by allowing users to modify documents, replacing particular words or phrases that act as triggers with more comfortable alternatives.

## The Need for the Application
Individuals with certain phobias, like Ommetaphobia, often struggle with encountering specific words, images, or stimuli related to their fear. Such encounters can induce anxiety, stress, or even panic attacks. By creating an application that enables users to customize their content by replacing triggering elements within documents, we aim to empower individuals to navigate their environment with reduced distress.

## How It Works
The application primarily focuses on modifying text documents. Users can upload a document of their choice and specify the word or phrase they wish to replace. The application then processes the document using regular expressions to accurately identify and replace occurrences of the specified word(s) within the document's paragraphs. Once modified, users can export the updated document to a location of their choice.

## Code Explanation:

### `handle_document(file_path, old_word, new_word)`
This function utilizes the `docx` library to modify a document by replacing occurrences of a particular word (`old_word`) with another word (`new_word`). It employs regular expressions (`re.sub`) to ensure precise word replacements within the document paragraphs.

### `export_modified_document(modified_doc, export_path)`
This function exports the modified document by writing its content to a specified export path, ensuring that the changes made through `handle_document` are saved.

### `upload_document()`
This function prompts the user to input the path of the document file they wish to modify within the application.

### `get_replacement_words()`
This function requests the user to enter the word they want to replace (`old_word`) and the new word (`new_word`) that will substitute it within the document.

### `main()`
The main function orchestrates the application flow by initiating the process of uploading a document, obtaining replacement words, executing document modification using `handle_document`, specifying an export path for the modified document, and finally exporting the updated document to the specified path.

## Usage
To use this application:
1. Run the script.
2. Enter the path of the document file. (Note: **here please copy and paste your full path including the documen itself, e.g. /workspaces/user/final_project/document/document.docx**)
3. Input the word to replace and the new word.
4. Specify the export path for the modified document (Note: **including the file name and extension, e.g. "/workspaces/users/final_project/modified_document/modified_document.docx"**).

## Example Usage
```python
if __name__ == "__main__":
    main()
