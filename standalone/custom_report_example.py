from sapiopylib.rest.DataMgmtService import DataMgmtServer
from sapiopylib.rest.User import SapioUser
from sapiopylib.rest.pojo.CustomReport import RawReportTerm, CompositeReportTerm, ReportColumn, RawTermOperation, \
    CompositeTermOperation, CustomReportCriteria
from sapiopylib.rest.pojo.datatype.FieldDefinition import FieldType

# Create a user object which contains the connection information to Sapio
user = SapioUser(url='https://ginkgo.exemplareln.com/webservice/api',
                 api_token='58molhdq4787kcvpx8y30ma28t0mf5ams00ko9pngnhmogbaly')

# Get the various managers to perform actions in Sapio
report_manager = DataMgmtServer.get_custom_report_manager(user)

# Query for 100 samples getting their name and record ID, and also include their project's name
sample_term = RawReportTerm('Sample', 'RecordId', RawTermOperation.GREATER_THAN_OR_EQUAL_OPERATOR, '0')
project_term = RawReportTerm('Project', 'RecordId', RawTermOperation.GREATER_THAN_OR_EQUAL_OPERATOR, '0')
root_term = CompositeReportTerm(sample_term, CompositeTermOperation.AND_OPERATOR, project_term)
column_list = [ReportColumn('Sample', 'OtherSampleId', FieldType.STRING),
               ReportColumn('Sample', 'RecordId', FieldType.LONG),
               ReportColumn('Project', 'ProjectId', FieldType.STRING)]
request = CustomReportCriteria(column_list, root_term, page_size=100, page_number=0)
report = report_manager.run_custom_report(request)
data_frame = report.get_data_frame()
print(data_frame)

# Call a search by name
print('Calling Samples and Projects report')
report = report_manager.run_system_report_by_name('Samples and Projects', 100, 0)
data_frame = report.get_data_frame()
print(data_frame)
