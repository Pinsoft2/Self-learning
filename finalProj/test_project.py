from io import BytesIO
from docx import Document
import pytest
from ..project import handle_uploaded_document, export_modified_document, UploadedDocument


@pytest.mark.django_db
def test_handle_uploaded_document():
    # Mock the request
    request = MockRequest(
        action='Upload & Replace',
        files={'document': BytesIO(b'Sample Document')},
        post={'old_word': 'old', 'new_word': 'new'}
    )

    # Call the handle_uploaded_document function
    result = handle_uploaded_document(request.FILES['document'], request.POST.get('old_word'), request.POST.get('new_word'))

    # Check if the result contains the expected keys
    assert 'upload_completed' in result
    assert 'old_word' in result
    assert 'new_word' in result
    assert 'modified_doc' in result
    assert 'new_document_id' in result

@pytest.mark.django_db
def test_export_modified_document(monkeypatch):
    # Mocking UploadedDocument.objects.last() for testing
    def mock_last():
        return MockUploadedDocument()

    # Apply the monkeypatch for UploadedDocument.objects.last()
    monkeypatch.setattr(UploadedDocument.objects, 'last', mock_last)

    # Call the export_modified_document function
    result = export_modified_document()

    # Check if the result contains the expected keys
    assert 'modified_doc' in result
    assert 'new_file_name' in result
