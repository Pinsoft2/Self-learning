import re
from io import BytesIO
from docx import Document

def handle_document(file_path, old_word, new_word):
    doc = Document(file_path)
    for paragraph in doc.paragraphs:
        paragraph.text = re.sub(r'\b%s\b' % re.escape(old_word), new_word, paragraph.text)

    modified_doc = BytesIO()
    doc.save(modified_doc)
    modified_doc.seek(0)
    return modified_doc


def export_modified_document(modified_doc, export_path):
    with open(export_path, 'wb') as modified_file:
        modified_file.write(modified_doc.getvalue())
    return export_path

def upload_document():
    file_path = input("Enter the path of the document file: ")
    return file_path

def get_replacement_words():
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")
    return old_word, new_word

def main():
    uploaded_doc_path = upload_document()
    if uploaded_doc_path:
        old_word, new_word = get_replacement_words()

        modified_doc = handle_document(uploaded_doc_path, old_word, new_word)
        export_path = input("Enter the export path for the modified document (including file name and extension): ")

        exported_path = export_modified_document(modified_doc, export_path)

        print(f"Modified document exported to: {exported_path}")
    else:
        print("No document uploaded.")

if __name__ == "__main__":
    main()
