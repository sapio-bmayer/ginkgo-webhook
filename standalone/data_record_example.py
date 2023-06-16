from sapiopylib.rest.DataMgmtService import DataMgmtServer
from sapiopylib.rest.User import SapioUser
from sapiopylib.rest.pojo.DataRecordPaging import DataRecordPojoPageCriteria

# Create a user object which contains the connection information to Sapio
user = SapioUser(url='https://ginkgo.exemplareln.com/webservice/api',
                 api_token='58molhdq4787kcvpx8y30ma28t0mf5ams00ko9pngnhmogbaly')

# Get the various managers to perform actions in Sapio
data_record_manager = DataMgmtServer.get_data_record_manager(user)

# Query for the first 100 sample
sample_records_result = data_record_manager.query_all_records_of_type('Sample',
                                                                      DataRecordPojoPageCriteria(page_size=100))
sample_records = sample_records_result.result_list
print(len(sample_records))

# Create a new record in Sapio
new_sample_fields_list = [{'OtherSampleId': 'Test'}]
new_sample_records = data_record_manager.add_data_records_with_data('Sample', new_sample_fields_list)
print(new_sample_records[0].get_field_value('OtherSampleId') + ": " + str(new_sample_records[0].get_record_id()))

# Delete a record in Sapio
data_record_manager.delete_data_record_list(new_sample_records)
