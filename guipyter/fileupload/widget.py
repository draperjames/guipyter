import base64
import ipywidgets
import traitlets


class FileUploadWidget(ipywidgets.DOMWidget):
    '''File Upload Widget.

    This widget provides file upload using `FileReader`:

    https://developer.mozilla.org/en-US/docs/Web/API/FileReader
    https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications

    Attributes
    ----------
    file_name : str
        Uploaded file name.

    data : bytes
        Uploaded data as bytes.

    data_base64 : bytes
        Uploaded data as bytes base 64.
    '''
    _view_name = traitlets.Unicode('FileUploadView').tag(sync=True)
    _view_module = traitlets.Unicode('fileupload').tag(sync=True)
    # Set defaults for traitlet attributes.
    label = traitlets.Unicode(help='Label on button.').tag(sync=True)
    file_name = traitlets.Unicode(help='File name of `data`.').tag(sync=True)
    # File size in bytes
    file_size = traitlets.CInt(help='Size of `data`.').tag(sync=True)
    data_base64 = traitlets.Unicode(help='File content, base64 encoded.').tag(sync=True)
    data = traitlets.Bytes(help='File content.')

    def __init__(self, label="Browse", *args, **kwargs):
        """Initialize a the FileUploadWidget

        Parameters
        ----------
        label : str
            Label for the button.
        """

        super(FileUploadWidget, self).__init__(*args, **kwargs)
        self._dom_classes += ('widget_item', 'btn-group')
        self.label = label

    def _data_base64_changed(self, *args):
        self.data = base64.b64decode(self.data_base64.split(',', 1)[1])
