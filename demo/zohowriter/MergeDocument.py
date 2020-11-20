from controllers.APIHelper import APIResponse, FileAPIResponse
from controllers.ClientSideException import ZOIException
from controllers.Operations import MergeAndDownload
from controllers.RestClient import ZOIRestClient


def configure():
    """
    Passing the entire configuration as a dictionary
    """
    try:
        config_obj = ZOIRestClient.get_instance()
        user_config = {
            "apikey": "2ae438cf864488657cc9754a27daa480",
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


def sample_1():
    try:
        oi_demo_obj = MergeAndDownload.get_instance()

        oi_demo_obj.set_output_format("docx")

        oi_demo_obj.upload_document("file_content", "../files/ZohoWriter_MergeTemplate.docx")
        # oi_demo_obj.set_file_url("URL")

        merge_data_1 = {
            "name": "Amelia",
            "email": "amelia@zylker.com"
        }
        merge_data_2 = {
            "name": "Sylvia",
            "email": "sylvia@zylker.com"
        }
        oi_demo_obj.add_merge_data(merge_data_1)
        oi_demo_obj.add_merge_data(merge_data_2)

        # oi_demo_obj.set_password("***")

        response = oi_demo_obj.merge_and_download()
        if isinstance(response, APIResponse):
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        elif isinstance(response, FileAPIResponse):
            output_file_name = "conversion_" + response.file_name
            output_file_name = output_file_name.replace("\"", "")
            with open(output_file_name, "wb") as f:
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


def sample_2():
    try:
        oi_demo_obj = MergeAndDownload.get_instance()

        oi_demo_obj.set_output_format("pdf")

        oi_demo_obj.upload_document("file_content", "../files/ZohoWriter_MergeTemplate.docx")
        # oi_demo_obj.set_file_url("URL")

        oi_demo_obj.upload_document("merge_data_json_content", "../files/merge_data.json")
        # oi_demo_obj.upload_document("merge_data_csv_content", "PATH_TO_CSV_FILE")

        # oi_demo_obj.set_password("***")

        response = oi_demo_obj.merge_and_download()
        if isinstance(response, APIResponse):
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        elif isinstance(response, FileAPIResponse):
            output_file_name = "conversion_" + response.file_name
            output_file_name = output_file_name.replace("\"", "")
            with open(output_file_name, "wb") as f:
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


def sample_3():
    try:
        oi_demo_obj = MergeAndDownload.get_instance()

        oi_demo_obj.set_output_format("docx")

        oi_demo_obj.upload_document("file_content", "../files/ZohoWriter_MergeTemplate.docx")
        # oi_demo_obj.set_file_url("URL")

        merge_data = [
            {
                "name": "Amelia",
                "email": "amelia@zylker.com"
            },
            {
                "name": "Sylvia",
                "email": "sylvia@zylker.com"
            }
        ]
        oi_demo_obj.add_merge_data(merge_data)
        # oi_demo_obj.set_merge_data_csv_url("URL")
        # oi_demo_obj.set_merge_data_json_url("URL")

        # oi_demo_obj.set_password("***")

        response = oi_demo_obj.merge_and_download()
        if isinstance(response, APIResponse):
            response_json = response.response_json
            for key in response_json:
                print("{0}: {1}".format(key, response_json[key]))
        elif isinstance(response, FileAPIResponse):
            output_file_name = "conversion_" + response.file_name
            output_file_name = output_file_name.replace("\"", "")
            with open(output_file_name, "wb") as f:
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


if __name__ == '__main__':
    configure()
    print()
    sample_1()
    print()
    sample_2()
    print()
    sample_3()
