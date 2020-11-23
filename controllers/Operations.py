from controllers.RestClient import ZOIConfigUtil
from controllers.Utility import CommonUtil


class DocumentModel:

    def __init__(self):

        # Dictionary (or) JSON - type Parameters
        self.api_end_point = None
        self.callback_settings = None
        self.document_defaults = None
        self.editor_settings = None
        self.permissions = None
        self.document_info = None
        self.user_info = None
        self.ui_options = None
        self.watermark_settings = None
        self.merge_data = None
        self.webhook = None
        self.output_options = None

        # Universal Attachments Holder
        self.document = None

        # Plain String - type Parameters
        self.title = None
        self.lang = None
        self.format = None
        self.output_format = None
        self.merge_to = None
        self.password = None

        # URL Parameters
        self.url = None
        self.file_url = None
        self.merge_data_csv_url = None
        self.merge_data_json_url = None
        self.url1 = None
        self.url2 = None

        # For Internal Handling
        self.isCreate = False
        self.isCreateTemplate = False
        self.isDocument = False
        self.isURL = False

    def upload_document(self, document_name=None, path_to_document=None):
        if self.isURL:
            self.isURL = False
            self.url = None
        self.isDocument = True
        if self.document is None:
            self.document = dict()
        self.document[document_name] = path_to_document


class CreateDocument(DocumentModel):

    def __init__(self, is_create):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document"

        self.isCreate = is_create

    @staticmethod
    def get_instance():
        return CreateDocument(is_create=True)

    def set_callback_settings(self, key, value):
        if self.callback_settings is None:
            self.callback_settings = dict()
        self.callback_settings[key] = value

    def set_document_defaults(self, key, value):
        if self.document_defaults is None:
            self.document_defaults = dict()
        self.document_defaults[key] = value

    def set_editor_settings(self, key, value):
        if self.editor_settings is None:
            self.editor_settings = dict()
        self.editor_settings[key] = value

    def set_permissions(self, key, value):
        if self.permissions is None:
            self.permissions = dict()
        self.permissions[key] = CommonUtil.true_false_utility(value)

    def set_document_info(self, key, value):
        if self.document_info is None:
            self.document_info = dict()
        self.document_info[key] = value

    def set_user_info(self, key, value):
        if self.user_info is None:
            self.user_info = dict()
        self.user_info[key] = value

    def set_ui_options(self, key, value):
        if not self.isCreateTemplate:
            if self.ui_options is None:
                self.ui_options = dict()
            self.ui_options[key] = value

    def set_bulk_callback_settings(self, save_format=None, save_url=None, http_method_type=None, retries=None,
                                   timeout=None, save_url_params=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(save_format, dict):
            self.callback_settings = save_format

        # If Settings are individually passed as separate arguments
        else:
            if self.callback_settings is None:
                self.callback_settings = dict()
            if save_format is not None:
                self.callback_settings["save_format"] = save_format
            if save_url is not None:
                self.callback_settings["save_url"] = save_url
            if http_method_type is not None:
                self.callback_settings["http_method_type"] = http_method_type
            if retries is not None:
                self.callback_settings["retries"] = retries
            if timeout is not None:
                self.callback_settings["timeout"] = timeout
            if save_url_params is not None:
                self.callback_settings["save_url_params"] = save_url_params

    def set_bulk_document_defaults(self, orientation=None, paper_size=None, font_name=None,
                                   font_size=None, track_changes=None, margin=None):
        if self.isCreate:
            # If Settings are passed as a list with preferred settings
            if isinstance(orientation, dict):
                self.document_defaults = orientation

            # If Settings are individually passed as separate arguments
            else:
                if self.document_defaults is None:
                    self.document_defaults = dict()
                if orientation is not None:
                    self.document_defaults["orientation"] = orientation
                if paper_size is not None:
                    self.document_defaults["paper_size"] = paper_size
                if font_name is not None:
                    self.document_defaults["font_name"] = font_name
                if font_size is not None:
                    self.document_defaults["font_size"] = font_size
                if track_changes is not None:
                    self.document_defaults["track_changes"] = track_changes
                if margin is not None:
                    self.document_defaults["margin"] = margin

    def set_bulk_editor_settings(self, unit=None, language=None, view=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(unit, dict):
            self.editor_settings = unit

        # If Settings are individually passed as separate arguments
        else:
            if self.editor_settings is None:
                self.editor_settings = dict()
            if unit is not None:
                self.editor_settings["unit"] = unit
            if language is not None:
                self.editor_settings["language"] = language
            if view is not None:
                self.editor_settings["view"] = view

    def set_bulk_permissions(self, document_export=None, document_print=None, document_edit=None,
                             review_changes_resolve=None, review_comment=None, collab_chat=None,
                             document_pausecollaboration=None, document_fill=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_export, dict):
            self.permissions = document_export

        # If Settings are individually passed as separate arguments
        else:
            if self.permissions is None:
                self.permissions = dict()
            if document_export is not None:
                self.permissions["document.export"] = CommonUtil.true_false_utility(document_export)
            if document_print is not None:
                self.permissions["document.print"] = CommonUtil.true_false_utility(document_print)
            if document_edit is not None:
                self.permissions["document.edit"] = CommonUtil.true_false_utility(document_edit)
            if review_changes_resolve is not None:
                self.permissions["review.changes.resolve"] = CommonUtil.true_false_utility(review_changes_resolve)
            if review_comment is not None:
                self.permissions["review.comment"] = CommonUtil.true_false_utility(review_comment)
            if collab_chat is not None:
                self.permissions["collab.chat"] = CommonUtil.true_false_utility(collab_chat)
            if document_pausecollaboration is not None:
                self.permissions["document.pausecollaboration"] = CommonUtil.true_false_utility(
                    document_pausecollaboration)
            if document_fill is not None:
                self.permissions["document.fill"] = CommonUtil.true_false_utility(document_fill)

    def set_bulk_document_info(self, document_name=None, document_id=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_name, dict):
            self.document_info = document_name

        # If Settings are individually passed as separate arguments
        else:
            if self.document_info is None:
                self.document_info = dict()
            if document_name is not None:
                self.document_info["document_name"] = document_name
            if document_id is not None:
                self.document_info["document_id"] = document_id

    def set_bulk_user_info(self, user_id=None, display_name=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(user_id, dict):
            self.user_info = user_id

        # If Settings are individually passed as separate arguments
        else:
            if self.user_info is None:
                self.user_info = dict()
            if user_id is not None:
                self.user_info["user_id"] = user_id
            if display_name is not None:
                self.user_info["display_name"] = display_name

    def set_bulk_ui_options(self, save_button=None, chat_panel=None):

        if not self.isCreateTemplate:
            # If Settings are passed as a list with preferred settings
            if isinstance(save_button, dict):
                self.ui_options = save_button

            # If Settings are individually passed as separate arguments
            else:
                if self.ui_options is None:
                    self.ui_options = dict()
                if save_button is not None:
                    self.ui_options["save_button"] = save_button
                if chat_panel is not None:
                    self.ui_options["chat_panel"] = None

    def create_document(self):
        if not self.isCreateTemplate:
            try:
                from controllers.Handler import ZOIAPIHandler
            except ImportError:
                from .Handler import ZOIAPIHandler

            return ZOIAPIHandler.get_instance(self).writer_request_handler()


class EditDocument(CreateDocument):

    def __init__(self):
        super().__init__(is_create=False)

    @staticmethod
    def get_instance():
        return EditDocument()

    def set_url(self, value):
        if self.isDocument:
            self.isDocument = False
            self.document = None
        self.isURL = True
        self.url = value

    def edit_document(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler

        return ZOIAPIHandler.get_instance(self).writer_request_handler()

    def upload_edit_document(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("document", path_to_document)


class CoEditDocument(EditDocument):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_instance():
        return CoEditDocument()

    def co_edit_document(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()


class PreviewDocument(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/preview"

    @staticmethod
    def get_instance():
        return PreviewDocument()

    def set_lang(self, value):
        self.lang = value

    def set_url(self, value):
        if self.isDocument:
            self.document = None
        self.isURL = True
        self.url = value

    def preview_document(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()
        else:
            return "No Supported Document Uploaded to edit!"

    def upload_preview_document(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("document", path_to_document)


class WatermarkDocument(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/watermark"

    @staticmethod
    def get_instance():
        return WatermarkDocument()

    def set_url(self, value):
        if self.isDocument:
            self.document = None
        self.isURL = True
        self.url = value

    def set_watermark_settings(self, key, value):
        if self.watermark_settings is None:
            self.watermark_settings = dict()
        self.watermark_settings[key] = value

    def set_bulk_watermark_settings(self, type=None, text=None, orientation=None, font_name=None,
                                    font_size=None, font_color=None, opacity=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(type, dict):
            self.watermark_settings = type

        # If Settings are individually passed as separate arguments
        else:
            if self.watermark_settings is None:
                self.watermark_settings = dict()
            if type is not None:
                self.watermark_settings["type"] = type
            if text is not None:
                self.watermark_settings["text"] = text
            if orientation is not None:
                self.watermark_settings["orientation"] = orientation
            if font_name is not None:
                self.watermark_settings["font_name"] = font_name
            if font_size is not None:
                self.watermark_settings["font_size"] = font_size
            if font_color is not None:
                self.watermark_settings["font_color"] = font_color
            if opacity is not None:
                self.watermark_settings["opacity"] = opacity

    def watermark_document(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()
        else:
            return "No Supported Document Uploaded to edit!"

    def upload_watermark_document(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("document", path_to_document)


class CreateTemplate(CreateDocument):

    def __init__(self):
        super().__init__(is_create=False)
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "template"
        self.isCreateTemplate = True

    @staticmethod
    def get_instance():
        return CreateTemplate()

    def set_url(self, value):
        self.url = value

    def create_template(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()

    def upload_merge_data_csv_content(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("merge_data_csv_content", path_to_document)

    def upload_merge_data_json_content(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("merge_data_json_content", path_to_document)

    def upload_template_document(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("document", path_to_document)


class GetFields(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "fields"

    @staticmethod
    def get_instance():
        return GetFields()

    def set_file_url(self, value):
        self.file_url = value

    def get_fields(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()

    def upload_file_content(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("file_content", path_to_document)


class MergeAndDeliver(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/merge/webhook"

    @staticmethod
    def get_instance():
        return MergeAndDeliver()

    def set_file_url(self, value):
        self.file_url = value

    def set_merge_to(self, value):
        self.merge_to = value

    def set_merge_data_csv_url(self, value):
        self.merge_data_csv_url = value

    def set_merge_data_json_url(self, value):
        self.merge_data_json_url = value

    def set_output_format(self, value):
        self.output_format = value

    def set_password(self, value):
        self.password = value

    def set_webhook(self, key, value):
        if self.webhook is None:
            self.webhook = dict()
        self.webhook[key] = value

    def add_merge_data(self, value):
        if self.merge_data is None:
            self.merge_data = dict()
            self.merge_data["data"] = []
        if isinstance(value, dict):
            self.merge_data["data"].append(value)
        elif isinstance(value, list):
            self.merge_data["data"].extend(value)

    def get_fields(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()

    def upload_file_content(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("file_content", path_to_document)

    def set_bulk_webhook_settings(self, invoke_url=None, invoke_period=None):
        # If Settings are passed as a list with preferred settings
        if isinstance(invoke_url, dict):
            self.webhook = invoke_url

        # If Settings are individually passed as separate arguments
        else:
            if self.webhook is None:
                self.webhook = dict()
            if invoke_url is not None:
                self.webhook["invoke_url"] = invoke_url
            if invoke_period is not None:
                self.webhook["invoke_period"] = invoke_period

    def merge_and_deliver(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()


class MergeAndDownload(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/merge/download"

    @staticmethod
    def get_instance():
        return MergeAndDownload()

    def set_file_url(self, value):
        self.file_url = value

    def set_merge_data_csv_url(self, value):
        self.merge_data_csv_url = value

    def set_merge_data_json_url(self, value):
        self.merge_data_json_url = value

    def set_output_format(self, value):
        self.output_format = value

    def set_password(self, value):
        self.password = value

    def set_merge_data(self, key, value):
        if self.merge_data is None:
            self.merge_data = dict()
        self.merge_data[key] = value

    def upload_file_content(self, path_to_document=None):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("file_content", path_to_document)

    def merge_and_download(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()


class ConvertDocument(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/convert"

    @staticmethod
    def get_instance():
        return ConvertDocument()

    def set_url(self, value):
        if self.isDocument:
            self.document = None
        self.isURL = True
        self.url = value

    def upload_document_to_convert(self, path_to_document):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("document", path_to_document)

    def set_output_options(self, key, value):
        if self.output_options is None:
            self.output_options = dict()
        self.output_options[key] = value

    def set_password(self, value):
        self.password = value

    def set_bulk_output_options(self, format=None, document_name=None, password=None, include_changes=None,
                                include_comments=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(format, dict):
            self.output_options = format

        # If Settings are individually passed as separate arguments
        else:
            if self.output_options is None:
                self.output_options = dict()
            if format is not None:
                self.output_options["format"] = format
            if document_name is not None:
                self.output_options["document_name"] = document_name
            if password is not None:
                self.output_options["password"] = password
            if include_changes is not None:
                self.output_options["include_changes"] = include_changes
            if include_comments is not None:
                self.output_options["include_comments"] = include_comments

    def convert_document(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()


class CompareDocuments(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/compare"

    @staticmethod
    def get_instance():
        return CompareDocuments()

    def set_url1(self, value):
        self.url1 = value

    def set_url2(self, value):
        self.url2 = value

    def set_title(self, value):
        self.title = value

    def set_lang(self, value):
        self.lang = value

    def upload_document1(self, path_to_document):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("document1", path_to_document)

    def upload_document2(self, path_to_document):
        if path_to_document is not None and path_to_document != "":
            self.upload_document("document2", path_to_document)

    def compare_documents(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()


class SheetShowModel(object):

    def __init__(self):

        # Dictionary (or) JSON - type Parameters
        self.api_end_point = None
        self.callback_settings = None
        self.editor_settings = None
        self.permissions = None
        self.document_info = None
        self.user_info = None

        # Universal Attachments Holder
        self.document = None
        # self.document = dict()

        # Plain String - type Parameters
        self.url = None
        self.language = None
        self.format = None

        # For Internal Handling
        self.isDocument = None
        self.isURL = None

    def set_callback_settings(self, key, value):
        if self.callback_settings is None:
            self.callback_settings = dict()
        self.callback_settings[key] = value

    def set_editor_settings(self, key, value):
        if self.editor_settings is None:
            self.editor_settings = dict()
        self.editor_settings[key] = value

    def set_permissions(self, key, value):
        if self.permissions is None:
            self.permissions = dict()
        self.permissions[key] = CommonUtil.true_false_utility(value)

    def set_document_info(self, key, value):
        if self.document_info is None:
            self.document_info = dict()
        self.document_info[key] = value

    def set_user_info(self, key, value):
        if self.user_info is None:
            self.user_info = dict()
        self.user_info[key] = value

    def set_url(self, value):
        if self.isDocument:
            self.isDocument = False
            self.document = None
        self.isURL = True
        self.url = value

    def set_language(self, value):
        self.language = value

    def set_format(self, value):
        self.format = value

    def set_bulk_callback_settings(self, save_format=None, save_url=None, context_info=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(save_format, dict):
            self.callback_settings = save_format

        # If Settings are individually passed as separate arguments
        else:
            if self.callback_settings is None:
                self.callback_settings = dict()
            if save_format is not None:
                self.callback_settings["save_format"] = save_format
            if save_url is not None:
                self.callback_settings["save_url"] = save_url
            if context_info is not None:
                self.callback_settings["context_info"] = context_info

    def set_bulk_editor_settings(self, language=None, country=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(language, dict):
            self.editor_settings = language

        # If Settings are individually passed as separate arguments
        else:
            if self.editor_settings is None:
                self.editor_settings = dict()
            if language is not None:
                self.editor_settings["language"] = language
            if country is not None:
                self.editor_settings["country"] = country

    def set_bulk_permissions(self, document_export=None, document_print=None, document_edit=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_export, dict):
            self.permissions = document_export

        # If Settings are individually passed as separate arguments
        else:
            if self.permissions is None:
                self.permissions = dict()
            if document_export is not None:
                self.permissions["document.export"] = CommonUtil.true_false_utility(document_export)
            if document_print is not None:
                self.permissions["document.print"] = CommonUtil.true_false_utility(document_print)
            if document_edit is not None:
                self.permissions["document.edit"] = CommonUtil.true_false_utility(document_edit)

    def set_bulk_document_info(self, document_name=None, document_id=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_name, dict):
            self.document_info = document_name

        # If Settings are individually passed as separate arguments
        else:
            if self.document_info is None:
                self.document_info = dict()
            if document_name is not None:
                self.document_info["document_name"] = document_name
            if document_id is not None:
                self.document_info["document_id"] = document_id

    def set_bulk_user_info(self, user_id=None, display_name=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(user_id, dict):
            self.user_info = user_id

        # If Settings are individually passed as separate arguments
        else:
            if self.user_info is None:
                self.user_info = dict()
            if user_id is not None:
                self.user_info["user_id"] = user_id
            if display_name is not None:
                self.user_info["display_name"] = display_name

    def upload_document(self, param_name=None, path_to_document=None):
        if self.document is None:
            self.document = dict()
        self.document[param_name] = path_to_document


class CreateSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet"

    @staticmethod
    def get_instance():
        return CreateSpreadsheet()

    def create_spreadsheet(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class EditSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet"

    @staticmethod
    def get_instance():
        return EditSpreadsheet()

    def edit_spreadsheet(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class CoEditSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet"

    @staticmethod
    def get_instance():
        return CoEditSpreadsheet()

    def co_edit_spreadsheet(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class PreviewSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet/preview"

    @staticmethod
    def get_instance():
        return PreviewSpreadsheet()

    def preview_spreadsheet(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class CreatePresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation"

    @staticmethod
    def get_instance():
        return CreatePresentation()

    def create_presentation(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class EditPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation"

    @staticmethod
    def get_instance():
        return EditPresentation()

    def edit_presentation(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class CoEditPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation"

    @staticmethod
    def get_instance():
        return CoEditPresentation()

    def co_edit_presentation(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class PreviewPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation/preview"

    @staticmethod
    def get_instance():
        return PreviewPresentation()

    def preview_presentation(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class ConvertPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation/convert"

    @staticmethod
    def get_instance():
        return ConvertPresentation()

    def convert_presentation(self):
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class Delete(object):

    def __init__(self):

        self.api_end_point = None
        self.document_id = None
        self.session_id = None
        self.document_delete_url = None
        self.session_delete_url = None

    @staticmethod
    def get_instance():
        return Delete()

    def set_document_id(self, value):
        if self.document_delete_url is not None:
            self.document_delete_url = None
        self.document_id = value

    def set_session_id(self, value):
        if self.session_delete_url is not None:
            self.session_delete_url = None
        self.session_id = value

    def set_document_delete_url(self, value):
        if self.document_id is not None:
            self.document_id = None
        self.document_delete_url = value

    def set_session_delete_url(self, value):
        if self.session_id is not None:
            self.session_id = None
        self.session_delete_url = value

    def delete_writer_document(self):
        if self.document_delete_url is not None:
            self.api_end_point = self.document_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/" + self.document_id
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_writer_session(self):
        if self.session_delete_url is not None:
            self.api_end_point = self.session_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "session/" + self.session_id
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_sheet_document(self):
        if self.document_delete_url is not None:
            self.api_end_point = self.document_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet/" + self.document_id
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_sheet_session(self):
        if self.session_delete_url is not None:
            self.api_end_point = self.session_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "session/" + self.session_id
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_show_document(self):
        if self.document_delete_url is not None:
            self.api_end_point = self.document_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation/" + self.document_id
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_show_session(self):
        if self.session_delete_url is not None:
            self.api_end_point = self.session_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "session/" + self.session_id
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_document(self, service_id=None):
        if self.document_delete_url is not None:
            self.api_end_point = self.document_delete_url
        else:
            if service_id == 1:
                self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/" + self.document_id
            elif service_id == 2:
                self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet/" + self.document_id
            elif service_id == 3:
                self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation/" + self.document_id
            else:
                return
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_session(self, service_id=None):
        if self.session_delete_url is not None:
            self.api_end_point = self.session_delete_url
        else:
            if service_id == 1:
                self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "session/" + self.session_id
            elif service_id == 2:
                self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "session/" + self.session_id
            elif service_id == 3:
                self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "session/" + self.session_id
            else:
                return
        try:
            from controllers.Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()
