from controllers.APIHelper import APIResponse, FileAPIResponse
from controllers.ClientSideException import ZOIException
from controllers.Operations import *
from controllers.RestClient import ZOIRestClient


class MyClass(object):
    created_document_id = ""
    created_session_id = ""

    collaboration_document_id = None

    shouldSaveAsFile = "N"

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def configure_way1():  # Using in-built Setters
        try:
            config_obj = ZOIRestClient.get_instance()

            config_obj.set_apikey("98b1a012ba17d011b8e61737ebb5c171")
            config_obj.set_writer_api_base_url("https://api.office-integrator.com/writer/officeapi/")
            config_obj.set_sheet_api_base_url("https://api.office-integrator.com/sheet/officeapi/")
            config_obj.set_show_api_base_url("https://api.office-integrator.com/show/officeapi/")

            config_obj.initialize()

            # Used for demonstration only
            from controllers.RestClient import ZOIConfigUtil
            for key in ZOIConfigUtil.config_prop_dict:
                print("{0}: {1}".format(key, ZOIConfigUtil.config_prop_dict[key]))
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
                "apikey": "5a529635640132330906a23a42b38ede",
                "writer_api_base_url": "https://api.office-integrator.com/writer/officeapi/",
                "sheet_api_base_url": "https://api.office-integrator.com/sheet/officeapi/",
                "show_api_base_url": "https://api.office-integrator.com/show/officeapi/"
            }

            config_obj.initialize(user_config)

            # Used for demonstration only
            from controllers.RestClient import ZOIConfigUtil
            for key in ZOIConfigUtil.config_prop_dict:
                print("{0}: {1}".format(key, ZOIConfigUtil.config_prop_dict[key]))
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

            config_obj.upload_configuration_file("configurations/AppConfiguration.json")

            config_obj.initialize()

            # Used for demonstration only
            from controllers.RestClient import ZOIConfigUtil
            for key in ZOIConfigUtil.config_prop_dict:
                print("{0}: {1}".format(key, ZOIConfigUtil.config_prop_dict[key]))
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

            response = create_doc.create_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CreateDocument", response_json)

            # To demonstrate collaboration and deletion features
            MyClass.collaboration_document_id = response_json["document_id"]
            MyClass.created_document_id = response_json["document_id"]
            MyClass.created_session_id = response_json["session_id"]
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def edit_document():
        try:
            print("In response, Navigate to the document using \"document_url\" and start editing your document.\n")

            edit_doc = EditDocument.get_instance()

            edit_doc.upload_document("document", "demo/files/ZohoWriter.docx")

            edit_doc.set_callback_settings("save_format", "docx")
            edit_doc.set_callback_settings("save_url", "https://domain.com/save.php")

            response = edit_doc.edit_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("EditDocument", response_json)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def co_edit_document():
        try:
            co_edit_doc = CoEditDocument.get_instance()

            print("Using created document ID: " + str(
                MyClass.collaboration_document_id) + ". Share the \"document_url\" in response to collaborators\n")

            co_edit_doc.upload_document("document", "demo/files/ZohoShow.pptx")

            co_edit_doc.set_callback_settings("save_format", "docx")
            co_edit_doc.set_callback_settings("save_url", "https://domain.com/save.php")

            co_edit_doc.set_document_info("document_id", MyClass.collaboration_document_id)

            response = co_edit_doc.co_edit_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CoEditDocument", response_json)
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

            preview_doc.upload_document("document", "demo/files/ZohoWriter.docx")

            response = preview_doc.preview_document()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("PreviewDocument", response_json)
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

            watermark_doc.upload_document("document", "demo/files/ZohoWriter_Watermark.docx")

            watermark_doc.set_watermark_settings("type", "text")
            watermark_doc.set_watermark_settings("text", "Office Integrator")

            response = watermark_doc.watermark_document()
            if isinstance(response, APIResponse):
                response_json = response.response_json
                for key in response_json:
                    print("{0}: {1}".format(key, response_json[key]))

                # To save API response as JSON file
                MyClass.save_response_as_json_file("WatermarkDocumentError", response_json)
            elif isinstance(response, FileAPIResponse):
                output_file_name = "watermark_" + response.file_name
                with open("./demo/output/" + output_file_name, "wb") as f:
                    f.write(response.file_content)
                print("\nWatermark output file saved in output folder with filename : " + output_file_name)
            else:
                print(str(response))
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

            create_template.upload_document("merge_data_json_content", "demo/files/merge_data.json")

            response = create_template.create_template()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CreateTemplate", response_json)
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

            get_fields.upload_document("file_content", "demo/files/ZohoWriter_MergeTemplate.docx")

            response = get_fields.get_fields()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("GetFields", response_json)
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

            merge_deliver.upload_document("file_content", "demo/files/ZohoWriter_MergeTemplate.docx")

            merge_deliver.set_webhook("invoke_url", "https://domain.com/xyz.php")
            merge_deliver.set_webhook("invoke_period", "oncomplete")

            merge_deliver.set_merge_to("separatedoc")

            merge_deliver.upload_document("merge_data_json_content", "demo/files/merge_data.json")

            response = merge_deliver.merge_and_deliver()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("MergeAndDeliver", response_json)
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

            merge_download.upload_document("file_content", "demo/files/ZohoWriter_MergeTemplate.docx")

            merge_download.upload_document("merge_data_json_content", "demo/files/merge_data.json")

            response = merge_download.merge_and_download()
            if isinstance(response, APIResponse):
                response_json = response.response_json
                for key in response_json:
                    print("{0}: {1}".format(key, response_json[key]))

                # To save API response as JSON file
                MyClass.save_response_as_json_file("MergeAndDownloadError", response_json)
            elif isinstance(response, FileAPIResponse):
                output_file_name = "conversion_" + response.file_name
                output_file_name = output_file_name.replace("\"", "")
                with open("./demo/output/" + output_file_name, "wb") as f:
                    f.write(response.file_content)
                print("Merged document stored in output folder with filename : " + output_file_name)
            else:
                print(str(response))
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

            convert_document.upload_document("document", "demo/files/ZohoWriter.docx")

            convert_document.set_output_options("format", "docx")
            convert_document.set_output_options("document_name", "Untitled")

            response = convert_document.convert_document()
            if isinstance(response, APIResponse):
                response_json = response.response_json
                for key in response_json:
                    print("{0}: {1}".format(key, response_json[key]))

                # To save API response as JSON file
                MyClass.save_response_as_json_file("ConvertDocumentError", response_json)
            elif isinstance(response, FileAPIResponse):
                output_file_name = "conversion_" + response.file_name
                with open("./demo/output/" + output_file_name, "wb") as f:
                    f.write(response.file_content)
                print("Converted document stored in output folder with filename : " + output_file_name)
            else:
                print(str(response))
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

            compare_document.upload_document("document1", "demo/files/CompareDocument1.docx")

            compare_document.upload_document("document2", "demo/files/CompareDocument2.docx")

            response = compare_document.compare_documents()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CompareDocument", response_json)
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

            response = create_sheet.create_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CreateSpreadsheet", response_json)

            # To demonstrate collaboration and deletion features
            MyClass.collaboration_document_id = response_json["document_id"]
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

            edit_sheet.upload_document("document", "demo/files/ZohoSheet.xlsx")

            edit_sheet.set_callback_settings("save_format", "xlsx")
            edit_sheet.set_callback_settings("save_url", "https://zylker.com/save.php")

            response = edit_sheet.edit_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("EditSpreadsheet", response_json)
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

            print("Using created sheet ID: " + str(
                MyClass.collaboration_document_id) + ". Share the \"document_url\" in response to collaborators\n")

            co_edit_sheet.upload_document("document", "demo/files/ZohoSheet.xlsx")

            co_edit_sheet.set_callback_settings("save_format", "xlsx")
            co_edit_sheet.set_callback_settings("save_url", "https://zylker.com/save.php")

            # co_edit_sheet.set_document_info("document_id", MyClass.collaboration_document_id)

            response = co_edit_sheet.co_edit_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CoEditSpreadsheet", response_json)
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

            preview_sheet.upload_document("document", "demo/files/ZohoSheet.xlsx")

            response = preview_sheet.preview_spreadsheet()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("PreviewSpreadsheet", response_json)
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

            response = create_show.create_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CreatePresentation", response_json)

            # To demonstrate collaboration and deletion features
            MyClass.collaboration_document_id = response_json["document_id"]
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

            edit_show.upload_document("document", "demo/files/ZohoShow.pptx")

            edit_show.set_callback_settings("save_format", "pptx")
            edit_show.set_callback_settings("save_url", "https://domain.com/save.php")

            response = edit_show.edit_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("EditPresentation", response_json)
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

            print("Using created show ID: " + str(
                MyClass.collaboration_document_id) + ". Share the \"document_url\" in response to collaborators\n")

            # co_edit_show.upload_document("document", "demo/files/ZohoShow.pptx")

            co_edit_show.set_callback_settings("save_format", "pptx")
            co_edit_show.set_callback_settings("save_url", "https://domain.com/save.php")

            co_edit_show.set_document_info("document_id", MyClass.collaboration_document_id)

            response = co_edit_show.co_edit_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("CoEditPresentation", response_json)
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

            preview_show.upload_document("document", "demo/files/ZohoShow.pptx")

            response = preview_show.preview_presentation()
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("PreviewPresentation", response_json)
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

            convert_show.upload_document("document", "demo/files/ZohoShow.pptx")
            convert_show.set_format("pdf")

            response = convert_show.convert_presentation()
            if isinstance(response, APIResponse):
                response_json = response.response_json
                for key in response_json:
                    print("{0}: {1}".format(key, response_json[key]))

                # To save API response as JSON file
                MyClass.save_response_as_json_file("ConvertPresentationError", response_json)
            elif isinstance(response, FileAPIResponse):
                output_file_name = "conversion_" + response.file_name
                output_file_name = output_file_name.replace("\"", "")
                with open("./demo/output/" + output_file_name, "wb") as f:
                    f.write(response.file_content)
                print("Converted document stored in output folder with filename : " + output_file_name)
            else:
                print(str(response))
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

            # delete_writer_document.set_document_id("")  # Actual set document id call
            service_id = int(input("Choose a service: \n1) Writer\t2) Sheet\t3) Show"))
            if service_id == 1:
                # USED FOR DEMONSTRATION ONLY
                response_json = CreateDocument.get_instance().create_document().response_json
                document_id = response_json["document_id"]
                # document_delete_url = response_json["document_delete_url"]

                delete_document.set_document_id(document_id)
                # delete_document.set_document_delete_url(document_delete_url)

                response = delete_document.delete_writer_document()
            elif service_id == 2:
                # USED FOR DEMONSTRATION ONLY
                response_json = CreateSpreadsheet.get_instance().create_spreadsheet().response_json
                document_id = response_json["document_id"]
                # document_delete_url = response_json["document_delete_url"]

                delete_document.set_document_id(document_id)
                # delete_document.set_document_delete_url(document_delete_url)

                response = delete_document.delete_sheet_document()
            elif service_id == 3:
                # USED FOR DEMONSTRATION ONLY
                response_json = CreatePresentation.get_instance().create_presentation().response_json
                document_id = response_json["document_id"]
                # document_delete_url = response_json["document_delete_url"]

                delete_document.set_document_id(document_id)
                # delete_document.set_document_delete_url(document_delete_url)

                response = delete_document.delete_show_document()
            else:
                print("Invalid Service ID")
                return
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("DeleteDocument", response_json)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def delete_session():
        try:
            delete_session = Delete.get_instance()
            # delete_session.set_session_id("")  # Actual set session id call
            service_id = int(input("Choose a service: \n1) Writer\t2) Sheet\t3) Show"))
            if service_id == 1:
                # USED FOR DEMONSTRATION ONLY
                response_json = CreateDocument.get_instance().create_document().response_json
                session_id = response_json["session_id"]
                # session_delete_url = response_json["session_delete_url"]

                delete_session.set_session_id(session_id)
                # delete_session.set_session_delete_url(session_delete_url)

                response = delete_session.delete_writer_session()
            elif service_id == 2:
                # USED FOR DEMONSTRATION ONLY
                response_json = CreateSpreadsheet.get_instance().create_spreadsheet().response_json
                session_id = response_json["session_id"]
                # session_delete_url = response_json["session_delete_url"]

                delete_session.set_session_id(session_id)
                # delete_session.set_session_delete_url(session_delete_url)

                response = delete_session.delete_sheet_session()
            elif service_id == 3:
                # USED FOR DEMONSTRATION ONLY
                response_json = CreatePresentation.get_instance().create_presentation().response_json
                session_id = response_json["session_id"]
                # session_delete_url = response_json["session_delete_url"]

                delete_session.set_session_id(session_id)
                # delete_session.set_session_delete_url(session_delete_url)

                response = delete_session.delete_show_session()
            else:
                print("Invalid Service ID")
                return
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))

            # To save API response as JSON file
            MyClass.save_response_as_json_file("DeleteSession", response_json)
        except ZOIException as ex:
            print(ex.status_code)
            print(ex.error_code)
            print(ex.error_message)
            print(ex.error_details)
            print(ex.error_content)

    @staticmethod
    def save_response_as_json_file(api_name, response_json):  # Just to save response as JSON file in output folder
        import json
        with open("demo/api_response/" + api_name + "_response.json", "w") as f:
            json.dump(response_json, f, default=lambda o: o.__dict__, sort_keys=True, indent=4)


if __name__ == "__main__":
    obj = MyClass()

    # obj.configure_way1()

    # obj.configure_way2()

    obj.configure_way3()

    print("STARTING ZOHO OFFICE INTEGRATION SDK...\n")

    input("\nPress Enter To Test Create New Document API:\n")

    obj.create_document()

    input("\nPress Enter To Test Edit Existing Document API:\n")

    obj.edit_document()

    input("\nPress Enter To Test Co-Edit session for above document:\n")

    obj.co_edit_document()

    input("\nPress Enter To Test Preview Document API:\n")

    obj.preview_document()

    input("\nPress Enter To Test Watermark Document API:\n")

    print("Water mark input document taken from files folder. ")

    obj.watermark_document()

    input("\nPress Enter To Test Create Template API:\n")

    obj.create_template()

    input("\nPress Enter To Test Get Fields API(Merged fields in document will be returned as response):\n")

    print("Input document with merge fields: demo/files/ZohoWriter_MergeTemplate.docx")

    obj.get_fields()

    input("\nPress Enter To Test Merge and Deliver via Webhook API:\n")

    obj.merge_and_deliver_via_webhook()

    input("\nPress Enter To Test Merge and Download API:\n")

    obj.merge_and_download()

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

    """input("\nPress Enter To Test Preview Spreadsheet API:\n")

    obj.preview_spreadsheet()"""

    input("\nPress Enter To Test Create Presentation API:\n")

    obj.create_presentation()

    input("\nPress Enter To Test Edit Presentation API:\n")

    obj.edit_presentation()

    input("\nPress Enter To Test Co-Edit Presentation API:\n")

    obj.co_edit_presentation()

    input("\nPress Enter To Test Preview Presentation API:\n")

    obj.preview_presentation()

    input("\nPress Enter To Test Convert Presentation API:\n")

    obj.convert_presentation()

    input("\nPress Enter To Test Delete Document API:\n")

    obj.delete_document()

    input("\nPress Enter To Test Delete Session API:\n")

    obj.delete_session()
