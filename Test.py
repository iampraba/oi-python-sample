
from ClientSideException import ZOIException
from Operations import *
from RestClient import ZOIRestClient


class MyClass(object):
    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def configure_way1():  # Using in-built Setters
        try:
            config_obj = ZOIRestClient.get_instance()
            config_obj.set_apikey("2ae438cf864488657cc9754a27daa480")
            config_obj.set_writer_api_base_url("https://api.office-integrator.com/writer/officeapi/")
            config_obj.set_sheet_api_base_url("https://api.office-integrator.com/sheet/officeapi/")
            config_obj.set_show_api_base_url("https://api.office-integrator.com/show/officeapi/")
            config_obj.initialize()
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def configure_way2():  # Passing the entire configuration as a dictionary
        try:
            config_obj = ZOIRestClient.get_instance()
            user_config = {
                "apikey": "2ae438cf864488657cc9754a27daa480",
                "writer_api_base_url": "https://api.office-integrator.com/writer/officeapi/",
                "sheet_api_base_url": "https://api.office-integrator.com/sheet/officeapi/",
                "show_api_base_url": "https://api.office-integrator.com/show/officeapi/"
            }
            config_obj.initialize(user_config)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def configure_way3():  # Passing the configuration file
        try:
            config_obj = ZOIRestClient.get_instance()
            config_obj.upload_configuration_file("Sample_Documents/configuration.json")
            config_obj.initialize()
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def create_document():
        try:
            create_doc = CreateDocument.get_instance()
            create_doc.set_callback_settings("save_format", "docx")
            create_doc.set_callback_settings("save_url", "https://domain.com/save.php")
            create_doc.set_callback_settings("context_info", "additional doc or user info")

            # ALTERNATE WAYS TO PASS ON THE CONFIGURATION - SAME APPLIES FOR ALL METHODS IN THIS SDK

            # create_doc.set_bulk_callback_settings(save_format_or_list="docx", save_url="https://domain.com/save.php", context_info="additional doc or user info")
            # create_doc.set_bulk_callback_settings("docx", save_url="https://domain.com/save.php")
            # create_doc.set_bulk_callback_settings(save_url="https://domain.com/save.php")

            # my_callback_settings = [
            #     "docx",
            #     "https://domain.com/save.php",
            #     "additional doc or user info"
            # ]
            # create_doc.set_bulk_callback_settings(my_callback_settings)

            response = create_doc.create_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def edit_document():
        try:
            edit_doc = EditDocument.get_instance()
            edit_doc.set_callback_settings("save_format", "docx")
            edit_doc.set_callback_settings("save_url", "https://domain.com/save.php")
            edit_doc.set_callback_settings("context_info", "additional doc or user info")
            edit_doc.upload_document("document", "Sample_Documents/Sample_Upload_document.docx")
            response = edit_doc.edit_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def co_edit_document():
        try:
            edit_doc = CoEditDocument.get_instance()
            edit_doc.set_callback_settings("save_format", "docx")
            edit_doc.set_callback_settings("save_url", "https://domain.com/save.php")
            edit_doc.set_callback_settings("context_info", "additional doc or user info")
            edit_doc.upload_document("document", "Sample_Documents/Sample_Upload_document.docx")
            response = edit_doc.co_edit_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def preview_document():
        try:
            preview_doc = PreviewDocument.get_instance()
            preview_doc.set_lang("en")
            preview_doc.upload_document("document", "Sample_Documents/Sample_Upload_document.docx")
            response = preview_doc.preview_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def watermark_document():
        try:
            watermark_doc = WatermarkDocument.get_instance()
            watermark_doc.set_watermark_settings("type", "text")
            watermark_doc.set_watermark_settings("opacity", "0.5")
            watermark_doc.set_watermark_settings("text", "Zoho Corporation Private Limited, Chennai.")
            watermark_doc.upload_document("document", "Sample_Documents/watermark_source_document.docx")
            response = watermark_doc.watermark_document()
            response_headers = response.response_headers
            for key in response_headers:
                print("{0}: {1}".format(key, response_headers[key]))
            with open("./output/" + "watermark_" + response.file_name, "wb") as f:
                f.write(response.file_content)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def create_template():
        try:
            create_template = CreateTemplate.get_instance()
            create_template.set_callback_settings("save_format", "docx")
            create_template.set_callback_settings("save_url", "https://domain.com/save.php")
            create_template.set_callback_settings("context_info", "additional doc or user info")
            create_template.upload_document("merge_data_json_content", "Sample_Documents/merge_data.json")
            response = create_template.create_template()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def get_fields():
        try:
            get_fields = GetFields.get_instance()
            get_fields.upload_document("file_content", "Sample_Documents/Merge_templete.docx")
            response = get_fields.get_fields()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def merge_and_deliver_via_webhook():
        try:
            merge_deliver = MergeAndDeliver.get_instance()
            merge_deliver.set_output_format("pdf")
            merge_deliver.set_webhook("invoke_url", "https://domain.com/xyz.php")
            merge_deliver.set_webhook("invoke_period", "oncomplete")
            merge_deliver.set_merge_to("separatedoc")
            merge_deliver.upload_document("file_content", "Sample_Documents/Merge_templete.docx")
            merge_deliver.upload_document("merge_data_json_content", "Sample_Documents/merge_data.json")
            response = merge_deliver.merge_and_deliver()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def merge_and_download():
        try:
            merge_download = MergeAndDownload.get_instance()
            merge_download.set_output_format("pdf")
            merge_download.upload_document("file_content", "Sample_Documents/Merge_templete.docx")
            merge_download.upload_document("merge_data_json_content", "Sample_Documents/merge_data.json")
            response = merge_download.merge_and_download()
            response_headers = response.response_headers
            for key in response_headers:
                print("{0}: {1}".format(key, response_headers[key]))
            with open("./output/" + response.file_name, "wb") as f:
                f.write(response.file_content)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def convert_document():
        try:
            convert_document = ConvertDocument.get_instance()
            convert_document.set_format("pdf")
            convert_document.upload_document("document", "Sample_Documents/Sample_Upload_document.docx")
            response = convert_document.convert_document()
            response_headers = response.response_headers
            for key in response_headers:
                print("{0}: {1}".format(key, response_headers[key]))
            with open("./output/" + response.file_name, "wb") as f:
                f.write(response.file_content)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def compare_document():
        try:
            compare_document = CompareDocuments.get_instance()
            compare_document.upload_document("document1", "Sample_Documents/Document1.docx")
            compare_document.upload_document("document2", "Sample_Documents/Document2.docx")
            compare_document.set_title("Doc1_and_Doc2")
            response = compare_document.compare_documents()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def create_spreadsheet():
        try:
            create_sheet = CreateSpreadsheet.get_instance()
            create_sheet.set_callback_settings("save_format", "xlsx")
            create_sheet.set_callback_settings("save_url", "https://zylker.com/save.php")
            create_sheet.set_callback_settings("context_info", "additional doc or user info")
            response = create_sheet.create_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def edit_spreadsheet():
        try:
            edit_sheet = EditSpreadsheet.get_instance()
            edit_sheet.set_callback_settings("save_format", "xlsx")
            edit_sheet.set_callback_settings("save_url", "https://zylker.com/save.php")
            edit_sheet.set_callback_settings("context_info", "additional doc or user info")
            edit_sheet.upload_document("document", "Sample_Documents/Sample_Upload_Sheet.xlsx")
            response = edit_sheet.edit_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def co_edit_spreadsheet():
        try:
            co_edit_sheet = CoEditSpreadsheet.get_instance()
            co_edit_sheet.set_callback_settings("save_format", "xlsx")
            co_edit_sheet.set_callback_settings("save_url", "https://zylker.com/save.php")
            co_edit_sheet.set_callback_settings("context_info", "additional doc or user info")
            co_edit_sheet.upload_document("document", "Sample_Documents/Sample_Upload_Sheet.xlsx")
            response = co_edit_sheet.co_edit_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def preview_spreadsheet():
        try:
            preview_sheet = PreviewSpreadsheet.get_instance()
            preview_sheet.upload_document("document", "Sample_Documents/Sample_Upload_Sheet.xlsx")
            response = preview_sheet.preview_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def create_presentation():
        try:
            create_show = CreatePresentation.get_instance()
            create_show.set_callback_settings("save_format", "pptx")
            create_show.set_callback_settings("save_url", "https://domain.com/save.php")
            create_show.set_callback_settings("context_info", "additional doc or user info")
            response = create_show.create_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def edit_presentation():
        try:
            edit_show = EditPresentation.get_instance()
            edit_show.set_callback_settings("save_format", "pptx")
            edit_show.set_callback_settings("save_url", "https://domain.com/save.php")
            edit_show.set_callback_settings("context_info", "additional doc or user info")
            edit_show.upload_document("document", "Sample_Documents/Sample_Upload_Show.pptx")
            response = edit_show.edit_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def co_edit_presentation():
        try:
            co_edit_show = CoEditPresentation.get_instance()
            co_edit_show.set_callback_settings("save_format", "pptx")
            co_edit_show.set_callback_settings("save_url", "https://domain.com/save.php")
            co_edit_show.set_callback_settings("context_info", "additional doc or user info")
            co_edit_show.upload_document("document", "Sample_Documents/Sample_Upload_Show.pptx")
            response = co_edit_show.co_edit_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def preview_presentation():
        try:
            preview_show = PreviewPresentation.get_instance()
            preview_show.upload_document("document", "Sample_Documents/Sample_Upload_Show.pptx")
            response = preview_show.preview_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def convert_presentation():
        try:
            convert_show = ConvertPresentation.get_instance()
            convert_show.upload_document("document", "Sample_Documents/Sample_Upload_Show.pptx")
            convert_show.set_format("pdf")
            response = convert_show.convert_presentation()
            response_headers = response.response_headers
            for key in response_headers:
                print("{0}: {1}".format(key, response_headers[key]))
            with open("./output/" + response.file_name, "wb") as f:
                f.write(response.file_content)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def delete_document():
        try:
            delete_document = Delete.get_instance()
            # delete_document.set_document_id("")  # Actual set document id call
            delete_document.set_document_id(input("Enter the document ID to delete: "))  # Used ONLY for demonstration
            response = delete_document.delete_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def delete_document_session():
        try:
            delete_document = Delete.get_instance()
            # delete_document.set_session_id("")  # Actual set session id call
            delete_document.set_session_id(input("Enter the session ID to Delete: "))  # Used ONLY for demonstration
            response = delete_document.delete_document_session()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)


if __name__ == "__main__":
    obj = MyClass()

    # obj.configure_way1()

    # obj.configure_way2()

    obj.configure_way3()

    print("STARTING ZOHO WRITER SDK...\n")

    input("\nPress Enter To Test Create New Document API:\n")

    obj.create_document()

    input("\nPress Enter To Test Edit Existing Document API:\n")

    obj.edit_document()

    input("\nPress Enter To Test Co-Edit Session API:\n")

    obj.co_edit_document()

    input("\nPress Enter To Test Preview Document API:\n")

    obj.preview_document()

    input("\nPress Enter To Test Watermark Document API:\n")

    obj.watermark_document()

    input("\nPress Enter To Test Create Template API:\n")  # *****

    obj.create_template()  # *****

    input("\nPress Enter To Test Get Fields API:\n")

    obj.get_fields()

    input("\nPress Enter To Test Merge and Deliver via Webhook API:\n")

    obj.merge_and_deliver_via_webhook()

    input("\nPress Enter To Test Merge and Download API:\n")  # *****

    obj.merge_and_download()  # *****

    input("\nPress Enter To Test Conversion API API:\n")
    
    obj.convert_document()

    input("\nPress Enter To Test Comparison API API:\n")

    obj.compare_document()

    input("\nPress Enter To Test Create Spreadsheet API:\n")

    obj.create_spreadsheet()

    input("\nPress Enter To Test Edit Spreadsheet API:\n")

    obj.edit_spreadsheet()

    input("\nPress Enter To Test Co-Edit Spreadsheet API:\n")
    
    obj.co_edit_spreadsheet()

    input("\nPress Enter To Test Preview Spreadsheet API:\n")

    obj.preview_spreadsheet()

    input("\nPress Enter To Test Create Presentation API:\n")

    obj.create_presentation()

    input("\nPress Enter To Test Edit Presentation API:\n")

    obj.edit_presentation()

    input("\nPress Enter To Test Co-Edit Presentation API:\n")

    obj.co_edit_presentation()

    input("\nPress Enter To Test Preview Presentation API:\n")

    obj.preview_presentation()

    input("\nPress Enter To Test Convert Presentation API:\n")  # *****

    obj.convert_presentation()  # *****
    
    input("\nPress Enter To Test Delete Document API:\n")

    obj.delete_document()
    
    input("\nPress Enter To Test Delete Session API:\n")

    obj.delete_document_session()
