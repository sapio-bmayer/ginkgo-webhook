from typing import Dict

from sapiopylib.rest.DataMgmtService import DataMgmtServer
from sapiopylib.rest.User import SapioUser
from sapiopylib.rest.pojo.DataRecord import DataRecord
from sapiopylib.rest.pojo.eln.ExperimentEntry import ExperimentEntry

# Create a user object which contains the connection information to Sapio
user = SapioUser(url='https://ginkgo.exemplareln.com/webservice/api',
                 api_token='58molhdq4787kcvpx8y30ma28t0mf5ams00ko9pngnhmogbaly')

# Get the various managers to perform actions in Sapio
eln_manager = DataMgmtServer.get_eln_manager(user)
data_record_manager = DataMgmtServer.get_data_record_manager(user)

# Get an experiment by ID. Normally, this ID would be stored on a record so it can be retrieved quickly.
demo_experiment = eln_manager.get_eln_experiment_by_id(6779)
print(demo_experiment.notebook_experiment_name)

# Get the entries of this experiment
entries = eln_manager.get_experiment_entry_list(demo_experiment.notebook_experiment_id,
                                                to_retrieve_field_definitions=False)
name_to_entry: Dict[str, ExperimentEntry] = {entry.entry_name: entry for entry in entries}
print(name_to_entry.keys())

# Get the records of the 'Plasmid Tracking' entry
plasmid_tracking_entry = name_to_entry['Plasmid Tracking']
plasmid_tracking_records_result = eln_manager.get_data_records_for_entry(demo_experiment.notebook_experiment_id,
                                                                         plasmid_tracking_entry.entry_id)
plasmid_tracking_records = plasmid_tracking_records_result.result_list
print(len(plasmid_tracking_records))

# Add a record to 'Plasmid Tracking' entry
new_plasmid_tracking_record = data_record_manager.add_data_record(plasmid_tracking_entry.data_type_name)
plasmid_tracking_record_to_add = DataRecord(new_plasmid_tracking_record.get_data_type_name(),
                                            new_plasmid_tracking_record.get_record_id(), {})
eln_manager.add_records_to_table_entry(demo_experiment.notebook_experiment_id, plasmid_tracking_entry.entry_id,
                                       [plasmid_tracking_record_to_add])

# Check that they were added
plasmid_tracking_records_result = eln_manager.get_data_records_for_entry(demo_experiment.notebook_experiment_id,
                                                                         plasmid_tracking_entry.entry_id)
plasmid_tracking_records = plasmid_tracking_records_result.result_list
print(len(plasmid_tracking_records))

# Remove the added record
data_record_manager.delete_data_record(plasmid_tracking_record_to_add)
