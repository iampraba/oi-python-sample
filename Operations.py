
from Handler import DocumentDefaultsHandler, SheetDefaultsHandler, ShowDefaultsHandler
from Utility import CommonUtil, ZOIConfigUtil


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
        self.isMergeAndDeliver = False

    def upload_document(self, documentName=None, pathToDocument=None):
        if self.isURL:
            self.isURL = False
            self.url = None
        self.isDocument = True
        if self.document is None:
            self.document = dict()
        self.document[documentName] = pathToDocument


class CreateDocument(DocumentModel):

    def __init__(self, isCreate):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document"

        self.isCreate = isCreate

        # Initializing parameters with Defaults
        if self.isCreate and not self.isCreateTemplate:
            DocumentDefaultsHandler.set_default_create_document_settings(self)

    @staticmethod
    def get_instance():
        return CreateDocument(isCreate=True)

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
        self.permissions[key] = CommonUtil.TrueFalseUtility(value)

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

    def set_bulk_callback_settings(self, save_format_or_list=None, save_url=None, context_info=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(save_format_or_list, list):
            CommonUtil.ListDictionaryUtility(save_format_or_list, self.callback_settings)

        # If Settings are individually passed as separate arguments
        else:
            if save_format_or_list is not None:
                self.callback_settings["save_format"] = save_format_or_list
            if save_url is not None:
                self.callback_settings["save_url"] = save_url
            if context_info is not None:
                self.callback_settings["context_info"] = context_info

    def set_bulk_document_defaults(self, orientation_or_track_changes_or_list=None, paper_size=None, font_name=None,
                                   font_size=None, track_changes=None, margin=None):
        if self.isCreate:
            # If Settings are passed as a list with preferred settings
            if isinstance(orientation_or_track_changes_or_list, list):
                CommonUtil.ListDictionaryUtility(orientation_or_track_changes_or_list, self.document_defaults)

            # If Settings are individually passed as separate arguments
            else:
                if orientation_or_track_changes_or_list is not None:
                    self.document_defaults["orientation"] = orientation_or_track_changes_or_list
                if paper_size is not None:
                    self.document_defaults["paper_size"] = paper_size
                if font_name is not None:
                    self.document_defaults["font_name"] = font_name
                if font_size is not None:
                    self.document_defaults["font_size"] = font_size
                if track_changes is not None:
                    self.document_defaults["track_changes"] = track_changes
                if margin is not None:
                    for margin_value, dict_key in zip(margin, self.document_defaults["margin"].keys()):
                        self.document_defaults["margin"][dict_key] = margin_value

    def set_bulk_editor_settings(self, unit_or_list=None, language=None, view=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(unit_or_list, list):
            CommonUtil.ListDictionaryUtility(unit_or_list, self.editor_settings)

        # If Settings are individually passed as separate arguments
        else:
            if unit_or_list is not None:
                self.editor_settings["unit"] = unit_or_list
            if language is not None:
                self.editor_settings["language"] = language
            if view is not None:
                self.editor_settings["view"] = view

    def set_bulk_permissions(self, document_export_or_list=None, document_print=None, document_edit=None,
                             review_changes_resolve=None, review_comment=None, collab_chat=None,
                             document_pausecollaboration=None, document_fill=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_export_or_list, list):
            CommonUtil.ListDictionaryUtility(document_export_or_list, self.permissions)

        # If Settings are individually passed as separate arguments
        else:
            if document_export_or_list is not None:
                self.permissions["document.export"] = CommonUtil.TrueFalseUtility(document_export_or_list)
            if document_print is not None:
                self.permissions["document.print"] = CommonUtil.TrueFalseUtility(document_print)
            if document_edit is not None:
                self.permissions["document.edit"] = CommonUtil.TrueFalseUtility(document_edit)
            if review_changes_resolve is not None:
                self.permissions["review.changes.resolve"] = CommonUtil.TrueFalseUtility(review_changes_resolve)
            if review_comment is not None:
                self.permissions["review.comment"] = CommonUtil.TrueFalseUtility(review_comment)
            if collab_chat is not None:
                self.permissions["collab.chat"] = CommonUtil.TrueFalseUtility(collab_chat)
            if document_pausecollaboration is not None:
                self.permissions["document.pausecollaboration"] = CommonUtil.TrueFalseUtility(
                    document_pausecollaboration)
            if document_fill is not None:
                self.permissions["document.fill"] = CommonUtil.TrueFalseUtility(document_fill)

    def set_bulk_document_info(self, document_name_or_list=None, document_id=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_name_or_list, list):
            CommonUtil.ListDictionaryUtility(document_name_or_list, self.document_info)

        # If Settings are individually passed as separate arguments
        else:
            if document_name_or_list is not None:
                self.document_info["document_name"] = document_name_or_list
            if document_id is not None:
                self.document_info["document_id"] = document_id

    def set_bulk_user_info(self, user_id_or_list, display_name):

        # If Settings are passed as a list with preferred settings
        if isinstance(user_id_or_list, list):
            CommonUtil.ListDictionaryUtility(user_id_or_list, self.user_info)

        # If Settings are individually passed as separate arguments
        else:
            if user_id_or_list is not None:
                self.user_info["user_id"] = user_id_or_list
            if display_name is not None:
                self.user_info["display_name"] = display_name

    def set_bulk_ui_options(self, save_button_or_list=None, chat_panel=None):

        if not self.isCreateTemplate:
            # If Settings are passed as a list with preferred settings
            if isinstance(save_button_or_list, list):
                CommonUtil.ListDictionaryUtility(save_button_or_list, self.ui_options)

            # If Settings are individually passed as separate arguments
            else:
                if save_button_or_list is not None:
                    self.ui_options["save_button"] = save_button_or_list
                if chat_panel is not None:
                    self.ui_options["chat_panel"] = None

    def create_document(self):
        if not self.isCreateTemplate:
            try:
                from Handler import ZOIAPIHandler
            except ImportError:
                from .Handler import ZOIAPIHandler

            return ZOIAPIHandler.get_instance(self).writer_request_handler()


class EditDocument(CreateDocument):

    def __init__(self):
        super().__init__(isCreate=False)

        # Initializing parameters with Defaults
        DocumentDefaultsHandler.set_default_edit_document_settings(self)

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
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()
        else:
            return "No Supported Document Uploaded to edit!"

    def upload_edit_document(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("document", pathToDocument)


class CoEditDocument(EditDocument):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_instance():
        return CoEditDocument()

    def co_edit_document(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()
        else:
            return "No Supported Document Uploaded to edit!"


class PreviewDocument(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/preview"

        DocumentDefaultsHandler.set_default_preview_document_settings(self)

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
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()
        else:
            return "No Supported Document Uploaded to edit!"

    def upload_preview_document(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("document", pathToDocument)


class WatermarkDocument(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/watermark"

        DocumentDefaultsHandler.set_default_watermark_settings(self)

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

    def set_bulk_watermark_settings(self, text_or_list=None, text_type=None, orientation=None, font_name=None,
                                    font_size=None, font_color=None, opacity=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(text_or_list, list):
            CommonUtil.ListDictionaryUtility(text_or_list, self.callback_settings)

        # If Settings are individually passed as separate arguments
        if text_or_list is not None:
            self.watermark_settings["text"] = text_or_list
        if text_type is not None:
            self.watermark_settings["type"] = text_type
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
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()
        else:
            return "No Supported Document Uploaded to edit!"

    def upload_watermark_document(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("document", pathToDocument)


class CreateTemplate(CreateDocument):

    def __init__(self):
        super().__init__(isCreate=False)
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "template"
        self.isCreateTemplate = True

        DocumentDefaultsHandler.set_default_create_template_settings(self)

    @staticmethod
    def get_instance():
        return CreateTemplate()

    def set_url(self, value):
        self.url = value

    def create_template(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()

    def upload_merge_data_csv_content(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("merge_data_csv_content", pathToDocument)

    def upload_merge_data_json_content(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("merge_data_json_content", pathToDocument)

    def upload_template_document(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("document", pathToDocument)


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
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()

    def upload_file_content(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("file_content", pathToDocument)


class MergeAndDeliver(DocumentModel):

    def __init__(self, isMergeAndDeliver):
        super().__init__()
        self.isMergeAndDeliver = isMergeAndDeliver
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/merge/webhook"

        DocumentDefaultsHandler.set_default_merge_and_deliver_via_webhook(self)

    @staticmethod
    def get_instance():
        return MergeAndDeliver(isMergeAndDeliver=True)

    def set_file_url(self, value):
        self.file_url = value

    def set_merge_to(self, value):
        if self.isMergeAndDeliver:
            self.merge_to = value
        else:
            print("Invalid Parameters!")

    def set_merge_data_csv_url(self, value):
        self.merge_data_csv_url = value

    def set_merge_data_json_url(self, value):
        self.merge_data_json_url = value

    def set_output_format(self, value):
        self.output_format = value

    def set_password(self, value):
        self.password = value

    def set_webhook(self, key, value):
        if self.isMergeAndDeliver:
            if self.webhook is None:
                self.webhook = dict()
            self.webhook[key] = value
        else:
            print("Invalid Parameters")

    def set_merge_data(self, key, value):
        if self.merge_data is None:
            self.merge_data = dict()
        self.merge_data[key] = value

    def get_fields(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()

    def upload_file_content(self, pathToDocument=None):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("file_content", pathToDocument)

    def set_bulk_webhook_settings(self, invoke_url_or_list=None, invoke_period=None):
        if self.isMergeAndDeliver:
            # If Settings are passed as a list with preferred settings
            if isinstance(invoke_url_or_list, list):
                CommonUtil.ListDictionaryUtility(invoke_url_or_list, self.callback_settings)

            # If Settings are individually passed as separate arguments
            if invoke_url_or_list is not None:
                self.webhook["invoke_url"] = invoke_url_or_list
            if invoke_period is not None:
                self.webhook["invoke_period"] = invoke_period
        else:
            print("Invalid Parameters!")

    def merge_and_deliver(self):
        if self.isMergeAndDeliver:
            try:
                from Handler import ZOIAPIHandler
            except ImportError:
                from .Handler import ZOIAPIHandler
            return ZOIAPIHandler.get_instance(self).writer_request_handler()
        else:
            print("Invalid Method Call!")


class MergeAndDownload(MergeAndDeliver):

    def __init__(self, isMergeAndDeliver):
        super().__init__(isMergeAndDeliver)
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/merge/download"

        DocumentDefaultsHandler.set_default_merge_and_download_settings(self)

    @staticmethod
    def get_instance():
        return MergeAndDownload(isMergeAndDeliver=False)

    def merge_and_download(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).writer_request_handler()


class ConvertDocument(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/convert"

        DocumentDefaultsHandler.set_default_convert_document_settings(self)

    @staticmethod
    def get_instance():
        return ConvertDocument()

    def set_format(self, value):
        self.format = value

    def set_url(self, value):
        if self.isDocument:
            self.document = None
        self.isURL = True
        self.url = value

    def upload_document_to_convert(self, pathToDocument):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("document", pathToDocument)

    def convert_document(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        if self.isDocument or self.isURL:
            return ZOIAPIHandler.get_instance(self).writer_request_handler()


class CompareDocuments(DocumentModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/compare"

        DocumentDefaultsHandler.set_default_compare_document_settings(self)

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

    def upload_document1(self, pathToDocument):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("document1", pathToDocument)

    def upload_document2(self, pathToDocument):
        if pathToDocument is not None and pathToDocument != "":
            self.upload_document("document2", pathToDocument)

    def compare_documents(self):
        try:
            from Handler import ZOIAPIHandler
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
        self.permissions[key] = CommonUtil.TrueFalseUtility(value)

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

    def set_bulk_callback_settings(self, save_format_or_list=None, save_url=None, context_info=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(save_format_or_list, list):
            CommonUtil.ListDictionaryUtility(save_format_or_list, self.callback_settings)

        # If Settings are individually passed as separate arguments
        else:
            if save_format_or_list is not None:
                self.callback_settings["save_format"] = save_format_or_list
            if save_url is not None:
                self.callback_settings["save_url"] = save_url
            if context_info is not None:
                self.callback_settings["context_info"] = context_info

    def set_bulk_editor_settings(self, language_or_list=None, country=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(language_or_list, list):
            CommonUtil.ListDictionaryUtility(language_or_list, self.editor_settings)

        # If Settings are individually passed as separate arguments
        else:
            if language_or_list is not None:
                self.editor_settings["language"] = language_or_list
            if country is not None:
                self.editor_settings["country"] = country

    def set_bulk_permissions(self, document_export_or_list=None, document_print=None, document_edit=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_export_or_list, list):
            CommonUtil.ListDictionaryUtility(document_export_or_list, self.permissions)

        # If Settings are individually passed as separate arguments
        else:
            if document_export_or_list is not None:
                self.permissions["document.export"] = CommonUtil.TrueFalseUtility(document_export_or_list)
            if document_print is not None:
                self.permissions["document.print"] = CommonUtil.TrueFalseUtility(document_print)
            if document_edit is not None:
                self.permissions["document.edit"] = CommonUtil.TrueFalseUtility(document_edit)

    def set_bulk_document_info(self, document_name_or_list=None, document_id=None):

        # If Settings are passed as a list with preferred settings
        if isinstance(document_name_or_list, list):
            CommonUtil.ListDictionaryUtility(document_name_or_list, self.document_info)

        # If Settings are individually passed as separate arguments
        else:
            if document_name_or_list is not None:
                self.document_info["document_name"] = document_name_or_list
            if document_id is not None:
                self.document_info["document_id"] = document_id

    def upload_document(self, documentName=None, pathToDocument=None):
        if self.document is None:
            self.document = dict()
        self.document[documentName] = pathToDocument


class CreateSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet"

        SheetDefaultsHandler.set_default_create_spreadsheet_settings(self)

    @staticmethod
    def get_instance():
        return CreateSpreadsheet()

    def create_spreadsheet(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class EditSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet"

        SheetDefaultsHandler.set_default_edit_spreadsheet_settings(self)

    @staticmethod
    def get_instance():
        return EditSpreadsheet()

    def edit_spreadsheet(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class CoEditSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet"

        SheetDefaultsHandler.set_default_co_edit_spreadsheet_settings(self)

    @staticmethod
    def get_instance():
        return CoEditSpreadsheet()

    def co_edit_spreadsheet(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class PreviewSpreadsheet(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet/preview"

        SheetDefaultsHandler.set_default_preview_spreadsheet_settings(self)

    @staticmethod
    def get_instance():
        return PreviewSpreadsheet()

    def preview_spreadsheet(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class CreatePresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation"

        ShowDefaultsHandler.set_default_create_presentation_settings(self)

    @staticmethod
    def get_instance():
        return CreatePresentation()

    def create_presentation(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class EditPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation"

        ShowDefaultsHandler.set_default_edit_presentation_settings(self)

    @staticmethod
    def get_instance():
        return EditPresentation()

    def edit_presentation(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class CoEditPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation"

        ShowDefaultsHandler.set_default_co_edit_presentation_settings(self)

    @staticmethod
    def get_instance():
        return CoEditPresentation()

    def co_edit_presentation(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class PreviewPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation/preview"

        ShowDefaultsHandler.set_default_preview_presentation_settings(self)

    @staticmethod
    def get_instance():
        return PreviewPresentation()

    def preview_presentation(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class ConvertPresentation(SheetShowModel):

    def __init__(self):
        super().__init__()
        self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation/convert"

        ShowDefaultsHandler.set_default_conversion_api_settings(self)

    @staticmethod
    def get_instance():
        return ConvertPresentation()

    def convert_presentation(self):
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).sheet_show_request_handler()


class Delete(object):

    def __init__(self):

        self.api_end_point = None
        self.document_id = None
        self.session_id = None

    @staticmethod
    def get_instance():
        return Delete()

    def set_document_id(self, value):
        self.document_id = value

    def set_session_id(self, value):
        self.session_id = value

    def delete_document(self, document_delete_url=None):
        if document_delete_url is not None:
            self.api_end_point = document_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "document/" + self.document_id
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_document_session(self, session_delete_url=None):
        if session_delete_url is not None:
            self.api_end_point = session_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "session/" + self.session_id
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_sheet(self, document_delete_url=None):
        if document_delete_url is not None:
            self.api_end_point = document_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "spreadsheet/" + self.document_id
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_sheet_session(self, session_delete_url=None):
        if session_delete_url is not None:
            self.api_end_point = session_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_sheet_api_base_url() + "session/" + self.session_id
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_show(self, document_delete_url=None):
        if document_delete_url is not None:
            self.api_end_point = document_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_show_api_base_url() + "presentation/" + self.document_id
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()

    def delete_show_session(self, session_delete_url=None):
        if session_delete_url is not None:
            self.api_end_point = session_delete_url
        else:
            self.api_end_point = ZOIConfigUtil.get_writer_api_base_url() + "session/" + self.session_id
        try:
            from Handler import ZOIAPIHandler
        except ImportError:
            from .Handler import ZOIAPIHandler
        return ZOIAPIHandler.get_instance(self).delete_request_handler()
