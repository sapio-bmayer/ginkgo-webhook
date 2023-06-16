from typing import Dict

from sapiopylib.rest.DataMgmtService import DataMgmtServer
from sapiopylib.rest.User import SapioUser
from sapiopylib.rest.pojo.datatype.FieldDefinition import AbstractVeloxFieldDefinition

# Create a user object which contains the connection information to Sapio
user = SapioUser(url='https://ginkgo.exemplareln.com/webservice/api',
                 api_token='58molhdq4787kcvpx8y30ma28t0mf5ams00ko9pngnhmogbaly')

# Get the various managers to perform actions in Sapio
data_type_manager = DataMgmtServer.get_data_type_manager(user)

# Get the sample data type information
sample_definition = data_type_manager.get_data_type_definition('Sample')
print(sample_definition.plural_display_name)

# Get the fields for the sample data type
field_definition_list = data_type_manager.get_field_definition_list('Sample')
field_name_to_definition: Dict[str, AbstractVeloxFieldDefinition] =\
    {definition.get_data_field_name(): definition for definition in field_definition_list}
print(field_name_to_definition.keys())

other_sample_id_definition = field_name_to_definition['OtherSampleId']
print(other_sample_id_definition.display_name)
