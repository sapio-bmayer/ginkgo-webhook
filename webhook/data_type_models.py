from sapiopylib.rest.pojo.datatype.FieldDefinition import FieldType
from sapiopylib.rest.utils.recordmodel.RecordModelWrapper import WrappedRecordModel, WrapperField
from sapiopylib.rest.pojo.DateRange import DateRange
from typing import Optional


class AccessionConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type AccessionConfig
    Data Type Display Name: Accession Configuration (Accession Configurations)
    Fields: AccessionOnCreate, CustomPluginClassPath, DataFieldName, DataTypeField, IsGlobal, NumberOfDigits, PrefixField, StartNumber, SuffixField
    Accession configuration can be used to modify default accessioning behaviors for out-of-box plugins from Sapio Sciences. Convenient methods can be found in AccessioningWithConfigManager class to accession according to the configuration. All Sapio plugins who accession samples should use this util for accessioning.
    """
    DATA_TYPE_NAME: str = 'AccessionConfig'
    ACCESSIONONCREATE__FIELD_NAME: WrapperField = WrapperField("AccessionOnCreate", FieldType.BOOLEAN)
    CUSTOMPLUGINCLASSPATH__FIELD_NAME: WrapperField = WrapperField("CustomPluginClassPath", FieldType.STRING)
    DATAFIELDNAME__FIELD_NAME: WrapperField = WrapperField("DataFieldName", FieldType.SELECTION)
    DATATYPEFIELD__FIELD_NAME: WrapperField = WrapperField("DataTypeField", FieldType.SELECTION)
    ISGLOBAL__FIELD_NAME: WrapperField = WrapperField("IsGlobal", FieldType.BOOLEAN)
    NUMBEROFDIGITS__FIELD_NAME: WrapperField = WrapperField("NumberOfDigits", FieldType.INTEGER)
    PREFIXFIELD__FIELD_NAME: WrapperField = WrapperField("PrefixField", FieldType.STRING)
    STARTNUMBER__FIELD_NAME: WrapperField = WrapperField("StartNumber", FieldType.INTEGER)
    SUFFIXFIELD__FIELD_NAME: WrapperField = WrapperField("SuffixField", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AccessionOnCreate_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AccessionOnCreate' on this record model
        """
        self.set_field_value(self.ACCESSIONONCREATE__FIELD_NAME.field_name, value)

    def get_AccessionOnCreate_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AccessionOnCreate' from this record model
        """
        return self.get_field_value(self.ACCESSIONONCREATE__FIELD_NAME.field_name)

    def set_CustomPluginClassPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomPluginClassPath' on this record model
        """
        self.set_field_value(self.CUSTOMPLUGINCLASSPATH__FIELD_NAME.field_name, value)

    def get_CustomPluginClassPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomPluginClassPath' from this record model
        """
        return self.get_field_value(self.CUSTOMPLUGINCLASSPATH__FIELD_NAME.field_name)

    def set_DataFieldName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataFieldName' on this record model
        """
        self.set_field_value(self.DATAFIELDNAME__FIELD_NAME.field_name, value)

    def get_DataFieldName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataFieldName' from this record model
        """
        return self.get_field_value(self.DATAFIELDNAME__FIELD_NAME.field_name)

    def set_DataTypeField_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataTypeField' on this record model
        """
        self.set_field_value(self.DATATYPEFIELD__FIELD_NAME.field_name, value)

    def get_DataTypeField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataTypeField' from this record model
        """
        return self.get_field_value(self.DATATYPEFIELD__FIELD_NAME.field_name)

    def set_IsGlobal_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsGlobal' on this record model
        """
        self.set_field_value(self.ISGLOBAL__FIELD_NAME.field_name, value)

    def get_IsGlobal_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsGlobal' from this record model
        """
        return self.get_field_value(self.ISGLOBAL__FIELD_NAME.field_name)

    def set_NumberOfDigits_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumberOfDigits' on this record model
        """
        self.set_field_value(self.NUMBEROFDIGITS__FIELD_NAME.field_name, value)

    def get_NumberOfDigits_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumberOfDigits' from this record model
        """
        return self.get_field_value(self.NUMBEROFDIGITS__FIELD_NAME.field_name)

    def set_PrefixField_field(self, value: Optional[str]):
        """
        Set data field with field name 'PrefixField' on this record model
        """
        self.set_field_value(self.PREFIXFIELD__FIELD_NAME.field_name, value)

    def get_PrefixField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PrefixField' from this record model
        """
        return self.get_field_value(self.PREFIXFIELD__FIELD_NAME.field_name)

    def set_StartNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'StartNumber' on this record model
        """
        self.set_field_value(self.STARTNUMBER__FIELD_NAME.field_name, value)

    def get_StartNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StartNumber' from this record model
        """
        return self.get_field_value(self.STARTNUMBER__FIELD_NAME.field_name)

    def set_SuffixField_field(self, value: Optional[str]):
        """
        Set data field with field name 'SuffixField' on this record model
        """
        self.set_field_value(self.SUFFIXFIELD__FIELD_NAME.field_name, value)

    def get_SuffixField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SuffixField' from this record model
        """
        return self.get_field_value(self.SUFFIXFIELD__FIELD_NAME.field_name)


class AnalysisStatusModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type AnalysisStatus
    Data Type Display Name: Analysis Status (Analysis Statuses)
    Fields: Invocation, Script, Status
    """
    DATA_TYPE_NAME: str = 'AnalysisStatus'
    INVOCATION__FIELD_NAME: WrapperField = WrapperField("Invocation", FieldType.PICKLIST)
    SCRIPT__FIELD_NAME: WrapperField = WrapperField("Script", FieldType.STRING)
    STATUS__FIELD_NAME: WrapperField = WrapperField("Status", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Invocation_field(self, value: Optional[str]):
        """
        Set data field with field name 'Invocation' on this record model
        """
        self.set_field_value(self.INVOCATION__FIELD_NAME.field_name, value)

    def get_Invocation_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Invocation' from this record model
        """
        return self.get_field_value(self.INVOCATION__FIELD_NAME.field_name)

    def set_Script_field(self, value: Optional[str]):
        """
        Set data field with field name 'Script' on this record model
        """
        self.set_field_value(self.SCRIPT__FIELD_NAME.field_name, value)

    def get_Script_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Script' from this record model
        """
        return self.get_field_value(self.SCRIPT__FIELD_NAME.field_name)

    def set_Status_field(self, value: Optional[str]):
        """
        Set data field with field name 'Status' on this record model
        """
        self.set_field_value(self.STATUS__FIELD_NAME.field_name, value)

    def get_Status_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Status' from this record model
        """
        return self.get_field_value(self.STATUS__FIELD_NAME.field_name)


class AssignedProcessModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type AssignedProcess
    Data Type Display Name: Assigned Process (Assigned Processes)
    Fields: AwaitingRequestApproval, CompletedDate, DoNotProceed, HasBeenReprocessed, OtherSampleId, ProcessName, ProcessStepNumber, ProcessTAT, Reprocessing, RequestRecordId, SampleId, SampleRecordId, ScheduledDate, SourceAssignedProcessIds, Status, TurnAroundHours, TurnAroundMinutes
    """
    DATA_TYPE_NAME: str = 'AssignedProcess'
    AWAITINGREQUESTAPPROVAL__FIELD_NAME: WrapperField = WrapperField("AwaitingRequestApproval", FieldType.BOOLEAN)
    COMPLETEDDATE__FIELD_NAME: WrapperField = WrapperField("CompletedDate", FieldType.DATE)
    DONOTPROCEED__FIELD_NAME: WrapperField = WrapperField("DoNotProceed", FieldType.BOOLEAN)
    HASBEENREPROCESSED__FIELD_NAME: WrapperField = WrapperField("HasBeenReprocessed", FieldType.BOOLEAN)
    OTHERSAMPLEID__FIELD_NAME: WrapperField = WrapperField("OtherSampleId", FieldType.STRING)
    PROCESSNAME__FIELD_NAME: WrapperField = WrapperField("ProcessName", FieldType.SELECTION)
    PROCESSSTEPNUMBER__FIELD_NAME: WrapperField = WrapperField("ProcessStepNumber", FieldType.LONG)
    PROCESSTAT__FIELD_NAME: WrapperField = WrapperField("ProcessTAT", FieldType.DOUBLE)
    REPROCESSING__FIELD_NAME: WrapperField = WrapperField("Reprocessing", FieldType.BOOLEAN)
    REQUESTRECORDID__FIELD_NAME: WrapperField = WrapperField("RequestRecordId", FieldType.LONG)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)
    SAMPLERECORDID__FIELD_NAME: WrapperField = WrapperField("SampleRecordId", FieldType.LONG)
    SCHEDULEDDATE__FIELD_NAME: WrapperField = WrapperField("ScheduledDate", FieldType.DATE)
    SOURCEASSIGNEDPROCESSIDS__FIELD_NAME: WrapperField = WrapperField("SourceAssignedProcessIds", FieldType.STRING)
    STATUS__FIELD_NAME: WrapperField = WrapperField("Status", FieldType.SELECTION)
    TURNAROUNDHOURS__FIELD_NAME: WrapperField = WrapperField("TurnAroundHours", FieldType.LONG)
    TURNAROUNDMINUTES__FIELD_NAME: WrapperField = WrapperField("TurnAroundMinutes", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AwaitingRequestApproval_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AwaitingRequestApproval' on this record model
        """
        self.set_field_value(self.AWAITINGREQUESTAPPROVAL__FIELD_NAME.field_name, value)

    def get_AwaitingRequestApproval_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AwaitingRequestApproval' from this record model
        """
        return self.get_field_value(self.AWAITINGREQUESTAPPROVAL__FIELD_NAME.field_name)

    def set_CompletedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'CompletedDate' on this record model
        """
        self.set_field_value(self.COMPLETEDDATE__FIELD_NAME.field_name, value)

    def get_CompletedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CompletedDate' from this record model
        """
        return self.get_field_value(self.COMPLETEDDATE__FIELD_NAME.field_name)

    def set_DoNotProceed_field(self, value: Optional[bool]):
        """
        Set data field with field name 'DoNotProceed' on this record model
        """
        self.set_field_value(self.DONOTPROCEED__FIELD_NAME.field_name, value)

    def get_DoNotProceed_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'DoNotProceed' from this record model
        """
        return self.get_field_value(self.DONOTPROCEED__FIELD_NAME.field_name)

    def set_HasBeenReprocessed_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HasBeenReprocessed' on this record model
        """
        self.set_field_value(self.HASBEENREPROCESSED__FIELD_NAME.field_name, value)

    def get_HasBeenReprocessed_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HasBeenReprocessed' from this record model
        """
        return self.get_field_value(self.HASBEENREPROCESSED__FIELD_NAME.field_name)

    def set_OtherSampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'OtherSampleId' on this record model
        """
        self.set_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name, value)

    def get_OtherSampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OtherSampleId' from this record model
        """
        return self.get_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name)

    def set_ProcessName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProcessName' on this record model
        """
        self.set_field_value(self.PROCESSNAME__FIELD_NAME.field_name, value)

    def get_ProcessName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProcessName' from this record model
        """
        return self.get_field_value(self.PROCESSNAME__FIELD_NAME.field_name)

    def set_ProcessStepNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'ProcessStepNumber' on this record model
        """
        self.set_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name, value)

    def get_ProcessStepNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ProcessStepNumber' from this record model
        """
        return self.get_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name)

    def set_ProcessTAT_field(self, value: Optional[float]):
        """
        Set data field with field name 'ProcessTAT' on this record model
        """
        self.set_field_value(self.PROCESSTAT__FIELD_NAME.field_name, value)

    def get_ProcessTAT_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ProcessTAT' from this record model
        """
        return self.get_field_value(self.PROCESSTAT__FIELD_NAME.field_name)

    def set_Reprocessing_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Reprocessing' on this record model
        """
        self.set_field_value(self.REPROCESSING__FIELD_NAME.field_name, value)

    def get_Reprocessing_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Reprocessing' from this record model
        """
        return self.get_field_value(self.REPROCESSING__FIELD_NAME.field_name)

    def set_RequestRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'RequestRecordId' on this record model
        """
        self.set_field_value(self.REQUESTRECORDID__FIELD_NAME.field_name, value)

    def get_RequestRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RequestRecordId' from this record model
        """
        return self.get_field_value(self.REQUESTRECORDID__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)

    def set_SampleRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'SampleRecordId' on this record model
        """
        self.set_field_value(self.SAMPLERECORDID__FIELD_NAME.field_name, value)

    def get_SampleRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SampleRecordId' from this record model
        """
        return self.get_field_value(self.SAMPLERECORDID__FIELD_NAME.field_name)

    def set_ScheduledDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ScheduledDate' on this record model
        """
        self.set_field_value(self.SCHEDULEDDATE__FIELD_NAME.field_name, value)

    def get_ScheduledDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ScheduledDate' from this record model
        """
        return self.get_field_value(self.SCHEDULEDDATE__FIELD_NAME.field_name)

    def set_SourceAssignedProcessIds_field(self, value: Optional[str]):
        """
        Set data field with field name 'SourceAssignedProcessIds' on this record model
        """
        self.set_field_value(self.SOURCEASSIGNEDPROCESSIDS__FIELD_NAME.field_name, value)

    def get_SourceAssignedProcessIds_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SourceAssignedProcessIds' from this record model
        """
        return self.get_field_value(self.SOURCEASSIGNEDPROCESSIDS__FIELD_NAME.field_name)

    def set_Status_field(self, value: Optional[str]):
        """
        Set data field with field name 'Status' on this record model
        """
        self.set_field_value(self.STATUS__FIELD_NAME.field_name, value)

    def get_Status_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Status' from this record model
        """
        return self.get_field_value(self.STATUS__FIELD_NAME.field_name)

    def set_TurnAroundHours_field(self, value: Optional[int]):
        """
        Set data field with field name 'TurnAroundHours' on this record model
        """
        self.set_field_value(self.TURNAROUNDHOURS__FIELD_NAME.field_name, value)

    def get_TurnAroundHours_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TurnAroundHours' from this record model
        """
        return self.get_field_value(self.TURNAROUNDHOURS__FIELD_NAME.field_name)

    def set_TurnAroundMinutes_field(self, value: Optional[int]):
        """
        Set data field with field name 'TurnAroundMinutes' on this record model
        """
        self.set_field_value(self.TURNAROUNDMINUTES__FIELD_NAME.field_name, value)

    def get_TurnAroundMinutes_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TurnAroundMinutes' from this record model
        """
        return self.get_field_value(self.TURNAROUNDMINUTES__FIELD_NAME.field_name)


class AttachmentModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Attachment
    Data Type Display Name: Attachment (Attachments)
    Fields: AttachmentId, Comments, Description, FilePath, IsGeneratedByReportBuilder, MultiParentLink118, MultiParentLink172, MultiParentLink174, MultiParentLink207, MultiParentLink208, VeloxCurrentVersion, VersionNumber
    Data type for document attachments
    """
    DATA_TYPE_NAME: str = 'Attachment'
    ATTACHMENTID__FIELD_NAME: WrapperField = WrapperField("AttachmentId", FieldType.STRING)
    COMMENTS__FIELD_NAME: WrapperField = WrapperField("Comments", FieldType.STRING)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    ISGENERATEDBYREPORTBUILDER__FIELD_NAME: WrapperField = WrapperField("IsGeneratedByReportBuilder", FieldType.BOOLEAN)
    MULTIPARENTLINK118__FIELD_NAME: WrapperField = WrapperField("MultiParentLink118", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK172__FIELD_NAME: WrapperField = WrapperField("MultiParentLink172", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK174__FIELD_NAME: WrapperField = WrapperField("MultiParentLink174", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK207__FIELD_NAME: WrapperField = WrapperField("MultiParentLink207", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK208__FIELD_NAME: WrapperField = WrapperField("MultiParentLink208", FieldType.MULTIPARENTLINK)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)
    VERSIONNUMBER__FIELD_NAME: WrapperField = WrapperField("VersionNumber", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AttachmentId_field(self, value: Optional[str]):
        """
        Set data field with field name 'AttachmentId' on this record model
        """
        self.set_field_value(self.ATTACHMENTID__FIELD_NAME.field_name, value)

    def get_AttachmentId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AttachmentId' from this record model
        """
        return self.get_field_value(self.ATTACHMENTID__FIELD_NAME.field_name)

    def set_Comments_field(self, value: Optional[str]):
        """
        Set data field with field name 'Comments' on this record model
        """
        self.set_field_value(self.COMMENTS__FIELD_NAME.field_name, value)

    def get_Comments_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Comments' from this record model
        """
        return self.get_field_value(self.COMMENTS__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_IsGeneratedByReportBuilder_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsGeneratedByReportBuilder' on this record model
        """
        self.set_field_value(self.ISGENERATEDBYREPORTBUILDER__FIELD_NAME.field_name, value)

    def get_IsGeneratedByReportBuilder_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsGeneratedByReportBuilder' from this record model
        """
        return self.get_field_value(self.ISGENERATEDBYREPORTBUILDER__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)

    def set_VersionNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'VersionNumber' on this record model
        """
        self.set_field_value(self.VERSIONNUMBER__FIELD_NAME.field_name, value)

    def get_VersionNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VersionNumber' from this record model
        """
        return self.get_field_value(self.VERSIONNUMBER__FIELD_NAME.field_name)


class AWSSageMakerClientConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type AWSSageMakerClientConfig
    Data Type Display Name: AWS SageMaker Client Configuration (AWS SageMaker Client Configurations)
    Fields: AccessKeyId, Region, SecretKey
    """
    DATA_TYPE_NAME: str = 'AWSSageMakerClientConfig'
    ACCESSKEYID__FIELD_NAME: WrapperField = WrapperField("AccessKeyId", FieldType.STRING)
    REGION__FIELD_NAME: WrapperField = WrapperField("Region", FieldType.STRING)
    SECRETKEY__FIELD_NAME: WrapperField = WrapperField("SecretKey", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AccessKeyId_field(self, value: Optional[str]):
        """
        Set data field with field name 'AccessKeyId' on this record model
        """
        self.set_field_value(self.ACCESSKEYID__FIELD_NAME.field_name, value)

    def get_AccessKeyId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AccessKeyId' from this record model
        """
        return self.get_field_value(self.ACCESSKEYID__FIELD_NAME.field_name)

    def set_Region_field(self, value: Optional[str]):
        """
        Set data field with field name 'Region' on this record model
        """
        self.set_field_value(self.REGION__FIELD_NAME.field_name, value)

    def get_Region_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Region' from this record model
        """
        return self.get_field_value(self.REGION__FIELD_NAME.field_name)

    def set_SecretKey_field(self, value: Optional[str]):
        """
        Set data field with field name 'SecretKey' on this record model
        """
        self.set_field_value(self.SECRETKEY__FIELD_NAME.field_name, value)

    def get_SecretKey_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SecretKey' from this record model
        """
        return self.get_field_value(self.SECRETKEY__FIELD_NAME.field_name)


class BarcodeConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type BarcodeConfig
    Data Type Display Name: Barcode Configuration (Barcode Configurations)
    Fields: BarcodeConfigName, CustomPluginClassPath, DataType, DefaultPrinter, Field1, Field2, Field3, Field4, Field5, Field6, Field7, Field8, Field9, Field10
    The Barcode Configurations Data Type
    """
    DATA_TYPE_NAME: str = 'BarcodeConfig'
    BARCODECONFIGNAME__FIELD_NAME: WrapperField = WrapperField("BarcodeConfigName", FieldType.STRING)
    CUSTOMPLUGINCLASSPATH__FIELD_NAME: WrapperField = WrapperField("CustomPluginClassPath", FieldType.STRING)
    DATATYPE__FIELD_NAME: WrapperField = WrapperField("DataType", FieldType.SELECTION)
    DEFAULTPRINTER__FIELD_NAME: WrapperField = WrapperField("DefaultPrinter", FieldType.SELECTION)
    FIELD1__FIELD_NAME: WrapperField = WrapperField("Field1", FieldType.SELECTION)
    FIELD2__FIELD_NAME: WrapperField = WrapperField("Field2", FieldType.SELECTION)
    FIELD3__FIELD_NAME: WrapperField = WrapperField("Field3", FieldType.SELECTION)
    FIELD4__FIELD_NAME: WrapperField = WrapperField("Field4", FieldType.SELECTION)
    FIELD5__FIELD_NAME: WrapperField = WrapperField("Field5", FieldType.SELECTION)
    FIELD6__FIELD_NAME: WrapperField = WrapperField("Field6", FieldType.SELECTION)
    FIELD7__FIELD_NAME: WrapperField = WrapperField("Field7", FieldType.SELECTION)
    FIELD8__FIELD_NAME: WrapperField = WrapperField("Field8", FieldType.SELECTION)
    FIELD9__FIELD_NAME: WrapperField = WrapperField("Field9", FieldType.SELECTION)
    FIELD10__FIELD_NAME: WrapperField = WrapperField("Field10", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_BarcodeConfigName_field(self, value: Optional[str]):
        """
        Set data field with field name 'BarcodeConfigName' on this record model
        """
        self.set_field_value(self.BARCODECONFIGNAME__FIELD_NAME.field_name, value)

    def get_BarcodeConfigName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BarcodeConfigName' from this record model
        """
        return self.get_field_value(self.BARCODECONFIGNAME__FIELD_NAME.field_name)

    def set_CustomPluginClassPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomPluginClassPath' on this record model
        """
        self.set_field_value(self.CUSTOMPLUGINCLASSPATH__FIELD_NAME.field_name, value)

    def get_CustomPluginClassPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomPluginClassPath' from this record model
        """
        return self.get_field_value(self.CUSTOMPLUGINCLASSPATH__FIELD_NAME.field_name)

    def set_DataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataType' on this record model
        """
        self.set_field_value(self.DATATYPE__FIELD_NAME.field_name, value)

    def get_DataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataType' from this record model
        """
        return self.get_field_value(self.DATATYPE__FIELD_NAME.field_name)

    def set_DefaultPrinter_field(self, value: Optional[str]):
        """
        Set data field with field name 'DefaultPrinter' on this record model
        """
        self.set_field_value(self.DEFAULTPRINTER__FIELD_NAME.field_name, value)

    def get_DefaultPrinter_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DefaultPrinter' from this record model
        """
        return self.get_field_value(self.DEFAULTPRINTER__FIELD_NAME.field_name)

    def set_Field1_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field1' on this record model
        """
        self.set_field_value(self.FIELD1__FIELD_NAME.field_name, value)

    def get_Field1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field1' from this record model
        """
        return self.get_field_value(self.FIELD1__FIELD_NAME.field_name)

    def set_Field2_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field2' on this record model
        """
        self.set_field_value(self.FIELD2__FIELD_NAME.field_name, value)

    def get_Field2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field2' from this record model
        """
        return self.get_field_value(self.FIELD2__FIELD_NAME.field_name)

    def set_Field3_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field3' on this record model
        """
        self.set_field_value(self.FIELD3__FIELD_NAME.field_name, value)

    def get_Field3_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field3' from this record model
        """
        return self.get_field_value(self.FIELD3__FIELD_NAME.field_name)

    def set_Field4_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field4' on this record model
        """
        self.set_field_value(self.FIELD4__FIELD_NAME.field_name, value)

    def get_Field4_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field4' from this record model
        """
        return self.get_field_value(self.FIELD4__FIELD_NAME.field_name)

    def set_Field5_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field5' on this record model
        """
        self.set_field_value(self.FIELD5__FIELD_NAME.field_name, value)

    def get_Field5_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field5' from this record model
        """
        return self.get_field_value(self.FIELD5__FIELD_NAME.field_name)

    def set_Field6_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field6' on this record model
        """
        self.set_field_value(self.FIELD6__FIELD_NAME.field_name, value)

    def get_Field6_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field6' from this record model
        """
        return self.get_field_value(self.FIELD6__FIELD_NAME.field_name)

    def set_Field7_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field7' on this record model
        """
        self.set_field_value(self.FIELD7__FIELD_NAME.field_name, value)

    def get_Field7_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field7' from this record model
        """
        return self.get_field_value(self.FIELD7__FIELD_NAME.field_name)

    def set_Field8_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field8' on this record model
        """
        self.set_field_value(self.FIELD8__FIELD_NAME.field_name, value)

    def get_Field8_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field8' from this record model
        """
        return self.get_field_value(self.FIELD8__FIELD_NAME.field_name)

    def set_Field9_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field9' on this record model
        """
        self.set_field_value(self.FIELD9__FIELD_NAME.field_name, value)

    def get_Field9_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field9' from this record model
        """
        return self.get_field_value(self.FIELD9__FIELD_NAME.field_name)

    def set_Field10_field(self, value: Optional[str]):
        """
        Set data field with field name 'Field10' on this record model
        """
        self.set_field_value(self.FIELD10__FIELD_NAME.field_name, value)

    def get_Field10_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Field10' from this record model
        """
        return self.get_field_value(self.FIELD10__FIELD_NAME.field_name)


class BatchModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Batch
    Data Type Display Name: Batch (Batches)
    Fields: AssignedTo, BatchId, BatchName, ExemplarBatchStatus, NumberOfSamples, PriorityLevel, StartDate, WorkflowName
    """
    DATA_TYPE_NAME: str = 'Batch'
    ASSIGNEDTO__FIELD_NAME: WrapperField = WrapperField("AssignedTo", FieldType.SELECTION)
    BATCHID__FIELD_NAME: WrapperField = WrapperField("BatchId", FieldType.STRING)
    BATCHNAME__FIELD_NAME: WrapperField = WrapperField("BatchName", FieldType.STRING)
    EXEMPLARBATCHSTATUS__FIELD_NAME: WrapperField = WrapperField("ExemplarBatchStatus", FieldType.SELECTION)
    NUMBEROFSAMPLES__FIELD_NAME: WrapperField = WrapperField("NumberOfSamples", FieldType.LONG)
    PRIORITYLEVEL__FIELD_NAME: WrapperField = WrapperField("PriorityLevel", FieldType.PICKLIST)
    STARTDATE__FIELD_NAME: WrapperField = WrapperField("StartDate", FieldType.DATE)
    WORKFLOWNAME__FIELD_NAME: WrapperField = WrapperField("WorkflowName", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AssignedTo_field(self, value: Optional[str]):
        """
        Set data field with field name 'AssignedTo' on this record model
        """
        self.set_field_value(self.ASSIGNEDTO__FIELD_NAME.field_name, value)

    def get_AssignedTo_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AssignedTo' from this record model
        """
        return self.get_field_value(self.ASSIGNEDTO__FIELD_NAME.field_name)

    def set_BatchId_field(self, value: Optional[str]):
        """
        Set data field with field name 'BatchId' on this record model
        """
        self.set_field_value(self.BATCHID__FIELD_NAME.field_name, value)

    def get_BatchId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BatchId' from this record model
        """
        return self.get_field_value(self.BATCHID__FIELD_NAME.field_name)

    def set_BatchName_field(self, value: Optional[str]):
        """
        Set data field with field name 'BatchName' on this record model
        """
        self.set_field_value(self.BATCHNAME__FIELD_NAME.field_name, value)

    def get_BatchName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BatchName' from this record model
        """
        return self.get_field_value(self.BATCHNAME__FIELD_NAME.field_name)

    def set_ExemplarBatchStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExemplarBatchStatus' on this record model
        """
        self.set_field_value(self.EXEMPLARBATCHSTATUS__FIELD_NAME.field_name, value)

    def get_ExemplarBatchStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExemplarBatchStatus' from this record model
        """
        return self.get_field_value(self.EXEMPLARBATCHSTATUS__FIELD_NAME.field_name)

    def set_NumberOfSamples_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumberOfSamples' on this record model
        """
        self.set_field_value(self.NUMBEROFSAMPLES__FIELD_NAME.field_name, value)

    def get_NumberOfSamples_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumberOfSamples' from this record model
        """
        return self.get_field_value(self.NUMBEROFSAMPLES__FIELD_NAME.field_name)

    def set_PriorityLevel_field(self, value: Optional[str]):
        """
        Set data field with field name 'PriorityLevel' on this record model
        """
        self.set_field_value(self.PRIORITYLEVEL__FIELD_NAME.field_name, value)

    def get_PriorityLevel_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PriorityLevel' from this record model
        """
        return self.get_field_value(self.PRIORITYLEVEL__FIELD_NAME.field_name)

    def set_StartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'StartDate' on this record model
        """
        self.set_field_value(self.STARTDATE__FIELD_NAME.field_name, value)

    def get_StartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StartDate' from this record model
        """
        return self.get_field_value(self.STARTDATE__FIELD_NAME.field_name)

    def set_WorkflowName_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowName' on this record model
        """
        self.set_field_value(self.WORKFLOWNAME__FIELD_NAME.field_name, value)

    def get_WorkflowName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowName' from this record model
        """
        return self.get_field_value(self.WORKFLOWNAME__FIELD_NAME.field_name)


class CDLConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type CDLConfig
    Data Type Display Name: Complex Data Loader Config (Complex Data Loader Configs)
    Fields: ConfigurationName, DataTypeName, DataTypeRules, DataTypeRules2, ExplicitlyMapped, IdentifierType, Options, Options2
    """
    DATA_TYPE_NAME: str = 'CDLConfig'
    CONFIGURATIONNAME__FIELD_NAME: WrapperField = WrapperField("ConfigurationName", FieldType.STRING)
    DATATYPENAME__FIELD_NAME: WrapperField = WrapperField("DataTypeName", FieldType.SELECTION)
    DATATYPERULES__FIELD_NAME: WrapperField = WrapperField("DataTypeRules", FieldType.SELECTION)
    DATATYPERULES2__FIELD_NAME: WrapperField = WrapperField("DataTypeRules2", FieldType.SELECTION)
    EXPLICITLYMAPPED__FIELD_NAME: WrapperField = WrapperField("ExplicitlyMapped", FieldType.BOOLEAN)
    IDENTIFIERTYPE__FIELD_NAME: WrapperField = WrapperField("IdentifierType", FieldType.SELECTION)
    OPTIONS__FIELD_NAME: WrapperField = WrapperField("Options", FieldType.SELECTION)
    OPTIONS2__FIELD_NAME: WrapperField = WrapperField("Options2", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ConfigurationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConfigurationName' on this record model
        """
        self.set_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name, value)

    def get_ConfigurationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConfigurationName' from this record model
        """
        return self.get_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name)

    def set_DataTypeName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataTypeName' on this record model
        """
        self.set_field_value(self.DATATYPENAME__FIELD_NAME.field_name, value)

    def get_DataTypeName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataTypeName' from this record model
        """
        return self.get_field_value(self.DATATYPENAME__FIELD_NAME.field_name)

    def set_DataTypeRules_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataTypeRules' on this record model
        """
        self.set_field_value(self.DATATYPERULES__FIELD_NAME.field_name, value)

    def get_DataTypeRules_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataTypeRules' from this record model
        """
        return self.get_field_value(self.DATATYPERULES__FIELD_NAME.field_name)

    def set_DataTypeRules2_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataTypeRules2' on this record model
        """
        self.set_field_value(self.DATATYPERULES2__FIELD_NAME.field_name, value)

    def get_DataTypeRules2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataTypeRules2' from this record model
        """
        return self.get_field_value(self.DATATYPERULES2__FIELD_NAME.field_name)

    def set_ExplicitlyMapped_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ExplicitlyMapped' on this record model
        """
        self.set_field_value(self.EXPLICITLYMAPPED__FIELD_NAME.field_name, value)

    def get_ExplicitlyMapped_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ExplicitlyMapped' from this record model
        """
        return self.get_field_value(self.EXPLICITLYMAPPED__FIELD_NAME.field_name)

    def set_IdentifierType_field(self, value: Optional[str]):
        """
        Set data field with field name 'IdentifierType' on this record model
        """
        self.set_field_value(self.IDENTIFIERTYPE__FIELD_NAME.field_name, value)

    def get_IdentifierType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IdentifierType' from this record model
        """
        return self.get_field_value(self.IDENTIFIERTYPE__FIELD_NAME.field_name)

    def set_Options_field(self, value: Optional[str]):
        """
        Set data field with field name 'Options' on this record model
        """
        self.set_field_value(self.OPTIONS__FIELD_NAME.field_name, value)

    def get_Options_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Options' from this record model
        """
        return self.get_field_value(self.OPTIONS__FIELD_NAME.field_name)

    def set_Options2_field(self, value: Optional[str]):
        """
        Set data field with field name 'Options2' on this record model
        """
        self.set_field_value(self.OPTIONS2__FIELD_NAME.field_name, value)

    def get_Options2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Options2' from this record model
        """
        return self.get_field_value(self.OPTIONS2__FIELD_NAME.field_name)


class CDLFieldMapModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type CDLFieldMap
    Data Type Display Name: Complex Data Loader Field Mapping (Complex Data Loader Field Mappings)
    Fields: ConfigurationName, DataTypeName, FieldRules, FieldRules2, FieldType, FromHeader, IdentifiedBy, IsListField, Options, Options2, ToField
    """
    DATA_TYPE_NAME: str = 'CDLFieldMap'
    CONFIGURATIONNAME__FIELD_NAME: WrapperField = WrapperField("ConfigurationName", FieldType.STRING)
    DATATYPENAME__FIELD_NAME: WrapperField = WrapperField("DataTypeName", FieldType.SELECTION)
    FIELDRULES__FIELD_NAME: WrapperField = WrapperField("FieldRules", FieldType.SELECTION)
    FIELDRULES2__FIELD_NAME: WrapperField = WrapperField("FieldRules2", FieldType.SELECTION)
    FIELDTYPE__FIELD_NAME: WrapperField = WrapperField("FieldType", FieldType.SELECTION)
    FROMHEADER__FIELD_NAME: WrapperField = WrapperField("FromHeader", FieldType.SELECTION)
    IDENTIFIEDBY__FIELD_NAME: WrapperField = WrapperField("IdentifiedBy", FieldType.STRING)
    ISLISTFIELD__FIELD_NAME: WrapperField = WrapperField("IsListField", FieldType.BOOLEAN)
    OPTIONS__FIELD_NAME: WrapperField = WrapperField("Options", FieldType.SELECTION)
    OPTIONS2__FIELD_NAME: WrapperField = WrapperField("Options2", FieldType.SELECTION)
    TOFIELD__FIELD_NAME: WrapperField = WrapperField("ToField", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ConfigurationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConfigurationName' on this record model
        """
        self.set_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name, value)

    def get_ConfigurationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConfigurationName' from this record model
        """
        return self.get_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name)

    def set_DataTypeName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataTypeName' on this record model
        """
        self.set_field_value(self.DATATYPENAME__FIELD_NAME.field_name, value)

    def get_DataTypeName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataTypeName' from this record model
        """
        return self.get_field_value(self.DATATYPENAME__FIELD_NAME.field_name)

    def set_FieldRules_field(self, value: Optional[str]):
        """
        Set data field with field name 'FieldRules' on this record model
        """
        self.set_field_value(self.FIELDRULES__FIELD_NAME.field_name, value)

    def get_FieldRules_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FieldRules' from this record model
        """
        return self.get_field_value(self.FIELDRULES__FIELD_NAME.field_name)

    def set_FieldRules2_field(self, value: Optional[str]):
        """
        Set data field with field name 'FieldRules2' on this record model
        """
        self.set_field_value(self.FIELDRULES2__FIELD_NAME.field_name, value)

    def get_FieldRules2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FieldRules2' from this record model
        """
        return self.get_field_value(self.FIELDRULES2__FIELD_NAME.field_name)

    def set_FieldType_field(self, value: Optional[str]):
        """
        Set data field with field name 'FieldType' on this record model
        """
        self.set_field_value(self.FIELDTYPE__FIELD_NAME.field_name, value)

    def get_FieldType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FieldType' from this record model
        """
        return self.get_field_value(self.FIELDTYPE__FIELD_NAME.field_name)

    def set_FromHeader_field(self, value: Optional[str]):
        """
        Set data field with field name 'FromHeader' on this record model
        """
        self.set_field_value(self.FROMHEADER__FIELD_NAME.field_name, value)

    def get_FromHeader_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FromHeader' from this record model
        """
        return self.get_field_value(self.FROMHEADER__FIELD_NAME.field_name)

    def set_IdentifiedBy_field(self, value: Optional[str]):
        """
        Set data field with field name 'IdentifiedBy' on this record model
        """
        self.set_field_value(self.IDENTIFIEDBY__FIELD_NAME.field_name, value)

    def get_IdentifiedBy_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IdentifiedBy' from this record model
        """
        return self.get_field_value(self.IDENTIFIEDBY__FIELD_NAME.field_name)

    def set_IsListField_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsListField' on this record model
        """
        self.set_field_value(self.ISLISTFIELD__FIELD_NAME.field_name, value)

    def get_IsListField_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsListField' from this record model
        """
        return self.get_field_value(self.ISLISTFIELD__FIELD_NAME.field_name)

    def set_Options_field(self, value: Optional[str]):
        """
        Set data field with field name 'Options' on this record model
        """
        self.set_field_value(self.OPTIONS__FIELD_NAME.field_name, value)

    def get_Options_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Options' from this record model
        """
        return self.get_field_value(self.OPTIONS__FIELD_NAME.field_name)

    def set_Options2_field(self, value: Optional[str]):
        """
        Set data field with field name 'Options2' on this record model
        """
        self.set_field_value(self.OPTIONS2__FIELD_NAME.field_name, value)

    def get_Options2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Options2' from this record model
        """
        return self.get_field_value(self.OPTIONS2__FIELD_NAME.field_name)

    def set_ToField_field(self, value: Optional[str]):
        """
        Set data field with field name 'ToField' on this record model
        """
        self.set_field_value(self.TOFIELD__FIELD_NAME.field_name, value)

    def get_ToField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ToField' from this record model
        """
        return self.get_field_value(self.TOFIELD__FIELD_NAME.field_name)


class CDLFileFieldModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type CDLFileField
    Data Type Display Name: Complex Data Loader File Field Header (Complex Data Loader File Field Headers)
    Fields: ConfigurationName, FileFieldHeader
    These records represent the field headers that were found in the example file.  These records are used by the plugin backing the selection list to the header field on the Complex Data Loader Field Mapping records.
    """
    DATA_TYPE_NAME: str = 'CDLFileField'
    CONFIGURATIONNAME__FIELD_NAME: WrapperField = WrapperField("ConfigurationName", FieldType.STRING)
    FILEFIELDHEADER__FIELD_NAME: WrapperField = WrapperField("FileFieldHeader", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ConfigurationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConfigurationName' on this record model
        """
        self.set_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name, value)

    def get_ConfigurationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConfigurationName' from this record model
        """
        return self.get_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name)

    def set_FileFieldHeader_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileFieldHeader' on this record model
        """
        self.set_field_value(self.FILEFIELDHEADER__FIELD_NAME.field_name, value)

    def get_FileFieldHeader_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileFieldHeader' from this record model
        """
        return self.get_field_value(self.FILEFIELDHEADER__FIELD_NAME.field_name)


class CDLGroupingConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type CDLGroupingConfig
    Data Type Display Name: Complex Data Loader Grouping Config (Complex Data Loader Grouping Configs)
    Fields: ConfigurationName, FileParser
    """
    DATA_TYPE_NAME: str = 'CDLGroupingConfig'
    CONFIGURATIONNAME__FIELD_NAME: WrapperField = WrapperField("ConfigurationName", FieldType.STRING)
    FILEPARSER__FIELD_NAME: WrapperField = WrapperField("FileParser", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ConfigurationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConfigurationName' on this record model
        """
        self.set_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name, value)

    def get_ConfigurationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConfigurationName' from this record model
        """
        return self.get_field_value(self.CONFIGURATIONNAME__FIELD_NAME.field_name)

    def set_FileParser_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileParser' on this record model
        """
        self.set_field_value(self.FILEPARSER__FIELD_NAME.field_name, value)

    def get_FileParser_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileParser' from this record model
        """
        return self.get_field_value(self.FILEPARSER__FIELD_NAME.field_name)


class ClientConfigurationsModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ClientConfigurations
    Data Type Display Name: Client Configurations (Client Configurations)
    Fields: BillingPortalUrl, ClientConfig1, COMWebServiceAccountName, COMWebServiceApiKey, COMWebServiceGuid, COMWebServiceUrl, ReportingUserPassword, ReportingWebServiceHost, ReportingWebServiceName, ReportingWebServicePort, ReportingWebServiceUserName, SampleSheetPath, SampleSheetPathForPacBio
    Client specific configurations.
    """
    DATA_TYPE_NAME: str = 'ClientConfigurations'
    BILLINGPORTALURL__FIELD_NAME: WrapperField = WrapperField("BillingPortalUrl", FieldType.STRING)
    CLIENTCONFIG1__FIELD_NAME: WrapperField = WrapperField("ClientConfig1", FieldType.STRING)
    COMWEBSERVICEACCOUNTNAME__FIELD_NAME: WrapperField = WrapperField("COMWebServiceAccountName", FieldType.STRING)
    COMWEBSERVICEAPIKEY__FIELD_NAME: WrapperField = WrapperField("COMWebServiceApiKey", FieldType.STRING)
    COMWEBSERVICEGUID__FIELD_NAME: WrapperField = WrapperField("COMWebServiceGuid", FieldType.STRING)
    COMWEBSERVICEURL__FIELD_NAME: WrapperField = WrapperField("COMWebServiceUrl", FieldType.STRING)
    REPORTINGUSERPASSWORD__FIELD_NAME: WrapperField = WrapperField("ReportingUserPassword", FieldType.STRING)
    REPORTINGWEBSERVICEHOST__FIELD_NAME: WrapperField = WrapperField("ReportingWebServiceHost", FieldType.STRING)
    REPORTINGWEBSERVICENAME__FIELD_NAME: WrapperField = WrapperField("ReportingWebServiceName", FieldType.STRING)
    REPORTINGWEBSERVICEPORT__FIELD_NAME: WrapperField = WrapperField("ReportingWebServicePort", FieldType.INTEGER)
    REPORTINGWEBSERVICEUSERNAME__FIELD_NAME: WrapperField = WrapperField("ReportingWebServiceUserName", FieldType.STRING)
    SAMPLESHEETPATH__FIELD_NAME: WrapperField = WrapperField("SampleSheetPath", FieldType.STRING)
    SAMPLESHEETPATHFORPACBIO__FIELD_NAME: WrapperField = WrapperField("SampleSheetPathForPacBio", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_BillingPortalUrl_field(self, value: Optional[str]):
        """
        Set data field with field name 'BillingPortalUrl' on this record model
        """
        self.set_field_value(self.BILLINGPORTALURL__FIELD_NAME.field_name, value)

    def get_BillingPortalUrl_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BillingPortalUrl' from this record model
        """
        return self.get_field_value(self.BILLINGPORTALURL__FIELD_NAME.field_name)

    def set_ClientConfig1_field(self, value: Optional[str]):
        """
        Set data field with field name 'ClientConfig1' on this record model
        """
        self.set_field_value(self.CLIENTCONFIG1__FIELD_NAME.field_name, value)

    def get_ClientConfig1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ClientConfig1' from this record model
        """
        return self.get_field_value(self.CLIENTCONFIG1__FIELD_NAME.field_name)

    def set_COMWebServiceAccountName_field(self, value: Optional[str]):
        """
        Set data field with field name 'COMWebServiceAccountName' on this record model
        """
        self.set_field_value(self.COMWEBSERVICEACCOUNTNAME__FIELD_NAME.field_name, value)

    def get_COMWebServiceAccountName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'COMWebServiceAccountName' from this record model
        """
        return self.get_field_value(self.COMWEBSERVICEACCOUNTNAME__FIELD_NAME.field_name)

    def set_COMWebServiceApiKey_field(self, value: Optional[str]):
        """
        Set data field with field name 'COMWebServiceApiKey' on this record model
        """
        self.set_field_value(self.COMWEBSERVICEAPIKEY__FIELD_NAME.field_name, value)

    def get_COMWebServiceApiKey_field(self) -> Optional[str]:
        """
        Get data field value with field name 'COMWebServiceApiKey' from this record model
        """
        return self.get_field_value(self.COMWEBSERVICEAPIKEY__FIELD_NAME.field_name)

    def set_COMWebServiceGuid_field(self, value: Optional[str]):
        """
        Set data field with field name 'COMWebServiceGuid' on this record model
        """
        self.set_field_value(self.COMWEBSERVICEGUID__FIELD_NAME.field_name, value)

    def get_COMWebServiceGuid_field(self) -> Optional[str]:
        """
        Get data field value with field name 'COMWebServiceGuid' from this record model
        """
        return self.get_field_value(self.COMWEBSERVICEGUID__FIELD_NAME.field_name)

    def set_COMWebServiceUrl_field(self, value: Optional[str]):
        """
        Set data field with field name 'COMWebServiceUrl' on this record model
        """
        self.set_field_value(self.COMWEBSERVICEURL__FIELD_NAME.field_name, value)

    def get_COMWebServiceUrl_field(self) -> Optional[str]:
        """
        Get data field value with field name 'COMWebServiceUrl' from this record model
        """
        return self.get_field_value(self.COMWEBSERVICEURL__FIELD_NAME.field_name)

    def set_ReportingUserPassword_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReportingUserPassword' on this record model
        """
        self.set_field_value(self.REPORTINGUSERPASSWORD__FIELD_NAME.field_name, value)

    def get_ReportingUserPassword_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReportingUserPassword' from this record model
        """
        return self.get_field_value(self.REPORTINGUSERPASSWORD__FIELD_NAME.field_name)

    def set_ReportingWebServiceHost_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReportingWebServiceHost' on this record model
        """
        self.set_field_value(self.REPORTINGWEBSERVICEHOST__FIELD_NAME.field_name, value)

    def get_ReportingWebServiceHost_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReportingWebServiceHost' from this record model
        """
        return self.get_field_value(self.REPORTINGWEBSERVICEHOST__FIELD_NAME.field_name)

    def set_ReportingWebServiceName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReportingWebServiceName' on this record model
        """
        self.set_field_value(self.REPORTINGWEBSERVICENAME__FIELD_NAME.field_name, value)

    def get_ReportingWebServiceName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReportingWebServiceName' from this record model
        """
        return self.get_field_value(self.REPORTINGWEBSERVICENAME__FIELD_NAME.field_name)

    def set_ReportingWebServicePort_field(self, value: Optional[int]):
        """
        Set data field with field name 'ReportingWebServicePort' on this record model
        """
        self.set_field_value(self.REPORTINGWEBSERVICEPORT__FIELD_NAME.field_name, value)

    def get_ReportingWebServicePort_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ReportingWebServicePort' from this record model
        """
        return self.get_field_value(self.REPORTINGWEBSERVICEPORT__FIELD_NAME.field_name)

    def set_ReportingWebServiceUserName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReportingWebServiceUserName' on this record model
        """
        self.set_field_value(self.REPORTINGWEBSERVICEUSERNAME__FIELD_NAME.field_name, value)

    def get_ReportingWebServiceUserName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReportingWebServiceUserName' from this record model
        """
        return self.get_field_value(self.REPORTINGWEBSERVICEUSERNAME__FIELD_NAME.field_name)

    def set_SampleSheetPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleSheetPath' on this record model
        """
        self.set_field_value(self.SAMPLESHEETPATH__FIELD_NAME.field_name, value)

    def get_SampleSheetPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleSheetPath' from this record model
        """
        return self.get_field_value(self.SAMPLESHEETPATH__FIELD_NAME.field_name)

    def set_SampleSheetPathForPacBio_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleSheetPathForPacBio' on this record model
        """
        self.set_field_value(self.SAMPLESHEETPATHFORPACBIO__FIELD_NAME.field_name, value)

    def get_SampleSheetPathForPacBio_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleSheetPathForPacBio' from this record model
        """
        return self.get_field_value(self.SAMPLESHEETPATHFORPACBIO__FIELD_NAME.field_name)


class ClusterDetailModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ClusterDetail
    Data Type Display Name: Tile Details (Tile Details)
    Fields: Aligned, AlignedPM, ClusterDensity, ClusterPassingFilter, ClusterPercentFilter, ColRead, DensityPlusMinus, Lane, LaneCol, PassedClustersInAllTiles, PassingPlusMinus, PFPercentPM, Tiles, TotalClustersInAllTiles
     <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'ClusterDetail'
    ALIGNED__FIELD_NAME: WrapperField = WrapperField("Aligned", FieldType.DOUBLE)
    ALIGNEDPM__FIELD_NAME: WrapperField = WrapperField("AlignedPM", FieldType.DOUBLE)
    CLUSTERDENSITY__FIELD_NAME: WrapperField = WrapperField("ClusterDensity", FieldType.DOUBLE)
    CLUSTERPASSINGFILTER__FIELD_NAME: WrapperField = WrapperField("ClusterPassingFilter", FieldType.DOUBLE)
    CLUSTERPERCENTFILTER__FIELD_NAME: WrapperField = WrapperField("ClusterPercentFilter", FieldType.DOUBLE)
    COLREAD__FIELD_NAME: WrapperField = WrapperField("ColRead", FieldType.STRING)
    DENSITYPLUSMINUS__FIELD_NAME: WrapperField = WrapperField("DensityPlusMinus", FieldType.DOUBLE)
    LANE__FIELD_NAME: WrapperField = WrapperField("Lane", FieldType.LONG)
    LANECOL__FIELD_NAME: WrapperField = WrapperField("LaneCol", FieldType.STRING)
    PASSEDCLUSTERSINALLTILES__FIELD_NAME: WrapperField = WrapperField("PassedClustersInAllTiles", FieldType.DOUBLE)
    PASSINGPLUSMINUS__FIELD_NAME: WrapperField = WrapperField("PassingPlusMinus", FieldType.DOUBLE)
    PFPERCENTPM__FIELD_NAME: WrapperField = WrapperField("PFPercentPM", FieldType.DOUBLE)
    TILES__FIELD_NAME: WrapperField = WrapperField("Tiles", FieldType.INTEGER)
    TOTALCLUSTERSINALLTILES__FIELD_NAME: WrapperField = WrapperField("TotalClustersInAllTiles", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Aligned_field(self, value: Optional[float]):
        """
        Set data field with field name 'Aligned' on this record model
        """
        self.set_field_value(self.ALIGNED__FIELD_NAME.field_name, value)

    def get_Aligned_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Aligned' from this record model
        """
        return self.get_field_value(self.ALIGNED__FIELD_NAME.field_name)

    def set_AlignedPM_field(self, value: Optional[float]):
        """
        Set data field with field name 'AlignedPM' on this record model
        """
        self.set_field_value(self.ALIGNEDPM__FIELD_NAME.field_name, value)

    def get_AlignedPM_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AlignedPM' from this record model
        """
        return self.get_field_value(self.ALIGNEDPM__FIELD_NAME.field_name)

    def set_ClusterDensity_field(self, value: Optional[float]):
        """
        Set data field with field name 'ClusterDensity' on this record model
        """
        self.set_field_value(self.CLUSTERDENSITY__FIELD_NAME.field_name, value)

    def get_ClusterDensity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ClusterDensity' from this record model
        """
        return self.get_field_value(self.CLUSTERDENSITY__FIELD_NAME.field_name)

    def set_ClusterPassingFilter_field(self, value: Optional[float]):
        """
        Set data field with field name 'ClusterPassingFilter' on this record model
        """
        self.set_field_value(self.CLUSTERPASSINGFILTER__FIELD_NAME.field_name, value)

    def get_ClusterPassingFilter_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ClusterPassingFilter' from this record model
        """
        return self.get_field_value(self.CLUSTERPASSINGFILTER__FIELD_NAME.field_name)

    def set_ClusterPercentFilter_field(self, value: Optional[float]):
        """
        Set data field with field name 'ClusterPercentFilter' on this record model
        """
        self.set_field_value(self.CLUSTERPERCENTFILTER__FIELD_NAME.field_name, value)

    def get_ClusterPercentFilter_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ClusterPercentFilter' from this record model
        """
        return self.get_field_value(self.CLUSTERPERCENTFILTER__FIELD_NAME.field_name)

    def set_ColRead_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColRead' on this record model
        """
        self.set_field_value(self.COLREAD__FIELD_NAME.field_name, value)

    def get_ColRead_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColRead' from this record model
        """
        return self.get_field_value(self.COLREAD__FIELD_NAME.field_name)

    def set_DensityPlusMinus_field(self, value: Optional[float]):
        """
        Set data field with field name 'DensityPlusMinus' on this record model
        """
        self.set_field_value(self.DENSITYPLUSMINUS__FIELD_NAME.field_name, value)

    def get_DensityPlusMinus_field(self) -> Optional[float]:
        """
        Get data field value with field name 'DensityPlusMinus' from this record model
        """
        return self.get_field_value(self.DENSITYPLUSMINUS__FIELD_NAME.field_name)

    def set_Lane_field(self, value: Optional[int]):
        """
        Set data field with field name 'Lane' on this record model
        """
        self.set_field_value(self.LANE__FIELD_NAME.field_name, value)

    def get_Lane_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Lane' from this record model
        """
        return self.get_field_value(self.LANE__FIELD_NAME.field_name)

    def set_LaneCol_field(self, value: Optional[str]):
        """
        Set data field with field name 'LaneCol' on this record model
        """
        self.set_field_value(self.LANECOL__FIELD_NAME.field_name, value)

    def get_LaneCol_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LaneCol' from this record model
        """
        return self.get_field_value(self.LANECOL__FIELD_NAME.field_name)

    def set_PassedClustersInAllTiles_field(self, value: Optional[float]):
        """
        Set data field with field name 'PassedClustersInAllTiles' on this record model
        """
        self.set_field_value(self.PASSEDCLUSTERSINALLTILES__FIELD_NAME.field_name, value)

    def get_PassedClustersInAllTiles_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PassedClustersInAllTiles' from this record model
        """
        return self.get_field_value(self.PASSEDCLUSTERSINALLTILES__FIELD_NAME.field_name)

    def set_PassingPlusMinus_field(self, value: Optional[float]):
        """
        Set data field with field name 'PassingPlusMinus' on this record model
        """
        self.set_field_value(self.PASSINGPLUSMINUS__FIELD_NAME.field_name, value)

    def get_PassingPlusMinus_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PassingPlusMinus' from this record model
        """
        return self.get_field_value(self.PASSINGPLUSMINUS__FIELD_NAME.field_name)

    def set_PFPercentPM_field(self, value: Optional[float]):
        """
        Set data field with field name 'PFPercentPM' on this record model
        """
        self.set_field_value(self.PFPERCENTPM__FIELD_NAME.field_name, value)

    def get_PFPercentPM_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PFPercentPM' from this record model
        """
        return self.get_field_value(self.PFPERCENTPM__FIELD_NAME.field_name)

    def set_Tiles_field(self, value: Optional[int]):
        """
        Set data field with field name 'Tiles' on this record model
        """
        self.set_field_value(self.TILES__FIELD_NAME.field_name, value)

    def get_Tiles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Tiles' from this record model
        """
        return self.get_field_value(self.TILES__FIELD_NAME.field_name)

    def set_TotalClustersInAllTiles_field(self, value: Optional[float]):
        """
        Set data field with field name 'TotalClustersInAllTiles' on this record model
        """
        self.set_field_value(self.TOTALCLUSTERSINALLTILES__FIELD_NAME.field_name, value)

    def get_TotalClustersInAllTiles_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TotalClustersInAllTiles' from this record model
        """
        return self.get_field_value(self.TOTALCLUSTERSINALLTILES__FIELD_NAME.field_name)


class CompoundModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Compound
    Data Type Display Name: Compound (Compounds)
    Fields: CAS, Charge, ChemBLId, cLogP, ConsumableType, ExactMass, ExpirationDate, Formula, GHSCautionCode, GHSHazardCode, GHSPictoCode, GHSSignal, inchi, IsGHSClassified, LotNumber, MolecularWeight, PolarSurfaceArea, PubchemCid, RegistryId, SMILES, SubstanceClass, TotalHBondCount
    """
    DATA_TYPE_NAME: str = 'Compound'
    CAS__FIELD_NAME: WrapperField = WrapperField("CAS", FieldType.STRING)
    CHARGE__FIELD_NAME: WrapperField = WrapperField("Charge", FieldType.INTEGER)
    CHEMBLID__FIELD_NAME: WrapperField = WrapperField("ChemBLId", FieldType.STRING)
    CLOGP__FIELD_NAME: WrapperField = WrapperField("cLogP", FieldType.DOUBLE)
    CONSUMABLETYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableType", FieldType.SELECTION)
    EXACTMASS__FIELD_NAME: WrapperField = WrapperField("ExactMass", FieldType.DOUBLE)
    EXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("ExpirationDate", FieldType.DATE)
    FORMULA__FIELD_NAME: WrapperField = WrapperField("Formula", FieldType.STRING)
    GHSCAUTIONCODE__FIELD_NAME: WrapperField = WrapperField("GHSCautionCode", FieldType.STRING)
    GHSHAZARDCODE__FIELD_NAME: WrapperField = WrapperField("GHSHazardCode", FieldType.STRING)
    GHSPICTOCODE__FIELD_NAME: WrapperField = WrapperField("GHSPictoCode", FieldType.STRING)
    GHSSIGNAL__FIELD_NAME: WrapperField = WrapperField("GHSSignal", FieldType.STRING)
    INCHI__FIELD_NAME: WrapperField = WrapperField("inchi", FieldType.STRING)
    ISGHSCLASSIFIED__FIELD_NAME: WrapperField = WrapperField("IsGHSClassified", FieldType.BOOLEAN)
    LOTNUMBER__FIELD_NAME: WrapperField = WrapperField("LotNumber", FieldType.STRING)
    MOLECULARWEIGHT__FIELD_NAME: WrapperField = WrapperField("MolecularWeight", FieldType.DOUBLE)
    POLARSURFACEAREA__FIELD_NAME: WrapperField = WrapperField("PolarSurfaceArea", FieldType.DOUBLE)
    PUBCHEMCID__FIELD_NAME: WrapperField = WrapperField("PubchemCid", FieldType.INTEGER)
    REGISTRYID__FIELD_NAME: WrapperField = WrapperField("RegistryId", FieldType.STRING)
    SMILES__FIELD_NAME: WrapperField = WrapperField("SMILES", FieldType.STRING)
    SUBSTANCECLASS__FIELD_NAME: WrapperField = WrapperField("SubstanceClass", FieldType.STRING)
    TOTALHBONDCOUNT__FIELD_NAME: WrapperField = WrapperField("TotalHBondCount", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_CAS_field(self, value: Optional[str]):
        """
        Set data field with field name 'CAS' on this record model
        """
        self.set_field_value(self.CAS__FIELD_NAME.field_name, value)

    def get_CAS_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CAS' from this record model
        """
        return self.get_field_value(self.CAS__FIELD_NAME.field_name)

    def set_Charge_field(self, value: Optional[int]):
        """
        Set data field with field name 'Charge' on this record model
        """
        self.set_field_value(self.CHARGE__FIELD_NAME.field_name, value)

    def get_Charge_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Charge' from this record model
        """
        return self.get_field_value(self.CHARGE__FIELD_NAME.field_name)

    def set_ChemBLId_field(self, value: Optional[str]):
        """
        Set data field with field name 'ChemBLId' on this record model
        """
        self.set_field_value(self.CHEMBLID__FIELD_NAME.field_name, value)

    def get_ChemBLId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ChemBLId' from this record model
        """
        return self.get_field_value(self.CHEMBLID__FIELD_NAME.field_name)

    def set_cLogP_field(self, value: Optional[float]):
        """
        Set data field with field name 'cLogP' on this record model
        """
        self.set_field_value(self.CLOGP__FIELD_NAME.field_name, value)

    def get_cLogP_field(self) -> Optional[float]:
        """
        Get data field value with field name 'cLogP' from this record model
        """
        return self.get_field_value(self.CLOGP__FIELD_NAME.field_name)

    def set_ConsumableType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableType' on this record model
        """
        self.set_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name, value)

    def get_ConsumableType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableType' from this record model
        """
        return self.get_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name)

    def set_ExactMass_field(self, value: Optional[float]):
        """
        Set data field with field name 'ExactMass' on this record model
        """
        self.set_field_value(self.EXACTMASS__FIELD_NAME.field_name, value)

    def get_ExactMass_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ExactMass' from this record model
        """
        return self.get_field_value(self.EXACTMASS__FIELD_NAME.field_name)

    def set_ExpirationDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ExpirationDate' on this record model
        """
        self.set_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_ExpirationDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ExpirationDate' from this record model
        """
        return self.get_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name)

    def set_Formula_field(self, value: Optional[str]):
        """
        Set data field with field name 'Formula' on this record model
        """
        self.set_field_value(self.FORMULA__FIELD_NAME.field_name, value)

    def get_Formula_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Formula' from this record model
        """
        return self.get_field_value(self.FORMULA__FIELD_NAME.field_name)

    def set_GHSCautionCode_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSCautionCode' on this record model
        """
        self.set_field_value(self.GHSCAUTIONCODE__FIELD_NAME.field_name, value)

    def get_GHSCautionCode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSCautionCode' from this record model
        """
        return self.get_field_value(self.GHSCAUTIONCODE__FIELD_NAME.field_name)

    def set_GHSHazardCode_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSHazardCode' on this record model
        """
        self.set_field_value(self.GHSHAZARDCODE__FIELD_NAME.field_name, value)

    def get_GHSHazardCode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSHazardCode' from this record model
        """
        return self.get_field_value(self.GHSHAZARDCODE__FIELD_NAME.field_name)

    def set_GHSPictoCode_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSPictoCode' on this record model
        """
        self.set_field_value(self.GHSPICTOCODE__FIELD_NAME.field_name, value)

    def get_GHSPictoCode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSPictoCode' from this record model
        """
        return self.get_field_value(self.GHSPICTOCODE__FIELD_NAME.field_name)

    def set_GHSSignal_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSSignal' on this record model
        """
        self.set_field_value(self.GHSSIGNAL__FIELD_NAME.field_name, value)

    def get_GHSSignal_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSSignal' from this record model
        """
        return self.get_field_value(self.GHSSIGNAL__FIELD_NAME.field_name)

    def set_inchi_field(self, value: Optional[str]):
        """
        Set data field with field name 'inchi' on this record model
        """
        self.set_field_value(self.INCHI__FIELD_NAME.field_name, value)

    def get_inchi_field(self) -> Optional[str]:
        """
        Get data field value with field name 'inchi' from this record model
        """
        return self.get_field_value(self.INCHI__FIELD_NAME.field_name)

    def set_IsGHSClassified_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsGHSClassified' on this record model
        """
        self.set_field_value(self.ISGHSCLASSIFIED__FIELD_NAME.field_name, value)

    def get_IsGHSClassified_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsGHSClassified' from this record model
        """
        return self.get_field_value(self.ISGHSCLASSIFIED__FIELD_NAME.field_name)

    def set_LotNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'LotNumber' on this record model
        """
        self.set_field_value(self.LOTNUMBER__FIELD_NAME.field_name, value)

    def get_LotNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LotNumber' from this record model
        """
        return self.get_field_value(self.LOTNUMBER__FIELD_NAME.field_name)

    def set_MolecularWeight_field(self, value: Optional[float]):
        """
        Set data field with field name 'MolecularWeight' on this record model
        """
        self.set_field_value(self.MOLECULARWEIGHT__FIELD_NAME.field_name, value)

    def get_MolecularWeight_field(self) -> Optional[float]:
        """
        Get data field value with field name 'MolecularWeight' from this record model
        """
        return self.get_field_value(self.MOLECULARWEIGHT__FIELD_NAME.field_name)

    def set_PolarSurfaceArea_field(self, value: Optional[float]):
        """
        Set data field with field name 'PolarSurfaceArea' on this record model
        """
        self.set_field_value(self.POLARSURFACEAREA__FIELD_NAME.field_name, value)

    def get_PolarSurfaceArea_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PolarSurfaceArea' from this record model
        """
        return self.get_field_value(self.POLARSURFACEAREA__FIELD_NAME.field_name)

    def set_PubchemCid_field(self, value: Optional[int]):
        """
        Set data field with field name 'PubchemCid' on this record model
        """
        self.set_field_value(self.PUBCHEMCID__FIELD_NAME.field_name, value)

    def get_PubchemCid_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PubchemCid' from this record model
        """
        return self.get_field_value(self.PUBCHEMCID__FIELD_NAME.field_name)

    def set_RegistryId_field(self, value: Optional[str]):
        """
        Set data field with field name 'RegistryId' on this record model
        """
        self.set_field_value(self.REGISTRYID__FIELD_NAME.field_name, value)

    def get_RegistryId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RegistryId' from this record model
        """
        return self.get_field_value(self.REGISTRYID__FIELD_NAME.field_name)

    def set_SMILES_field(self, value: Optional[str]):
        """
        Set data field with field name 'SMILES' on this record model
        """
        self.set_field_value(self.SMILES__FIELD_NAME.field_name, value)

    def get_SMILES_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SMILES' from this record model
        """
        return self.get_field_value(self.SMILES__FIELD_NAME.field_name)

    def set_SubstanceClass_field(self, value: Optional[str]):
        """
        Set data field with field name 'SubstanceClass' on this record model
        """
        self.set_field_value(self.SUBSTANCECLASS__FIELD_NAME.field_name, value)

    def get_SubstanceClass_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SubstanceClass' from this record model
        """
        return self.get_field_value(self.SUBSTANCECLASS__FIELD_NAME.field_name)

    def set_TotalHBondCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'TotalHBondCount' on this record model
        """
        self.set_field_value(self.TOTALHBONDCOUNT__FIELD_NAME.field_name, value)

    def get_TotalHBondCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TotalHBondCount' from this record model
        """
        return self.get_field_value(self.TOTALHBONDCOUNT__FIELD_NAME.field_name)


class CompoundPartModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type CompoundPart
    Data Type Display Name: Compound Part (Compound Parts)
    Fields: CAS, Charge, ChemBLId, cLogP, ConsumableType, EditLock, ExactMass, Formula, GHSCautionCode, GHSHazardCode, GHSPictoCode, GHSSignal, inchi, INCHIShadow, IsGHSClassified, MOL, MolecularWeight, molregno, PolarSurfaceArea, PubchemCid, QuantityOnHand, QuantityPerItem, RegistryId, ReorderLevelQuantity, Salts, SMILES, SMILESShadow, SubstanceClass, TotalHBondCount, Units
    """
    DATA_TYPE_NAME: str = 'CompoundPart'
    CAS__FIELD_NAME: WrapperField = WrapperField("CAS", FieldType.STRING)
    CHARGE__FIELD_NAME: WrapperField = WrapperField("Charge", FieldType.INTEGER)
    CHEMBLID__FIELD_NAME: WrapperField = WrapperField("ChemBLId", FieldType.STRING)
    CLOGP__FIELD_NAME: WrapperField = WrapperField("cLogP", FieldType.DOUBLE)
    CONSUMABLETYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableType", FieldType.SELECTION)
    EDITLOCK__FIELD_NAME: WrapperField = WrapperField("EditLock", FieldType.BOOLEAN)
    EXACTMASS__FIELD_NAME: WrapperField = WrapperField("ExactMass", FieldType.DOUBLE)
    FORMULA__FIELD_NAME: WrapperField = WrapperField("Formula", FieldType.STRING)
    GHSCAUTIONCODE__FIELD_NAME: WrapperField = WrapperField("GHSCautionCode", FieldType.STRING)
    GHSHAZARDCODE__FIELD_NAME: WrapperField = WrapperField("GHSHazardCode", FieldType.STRING)
    GHSPICTOCODE__FIELD_NAME: WrapperField = WrapperField("GHSPictoCode", FieldType.STRING)
    GHSSIGNAL__FIELD_NAME: WrapperField = WrapperField("GHSSignal", FieldType.STRING)
    INCHI__FIELD_NAME: WrapperField = WrapperField("inchi", FieldType.STRING)
    INCHISHADOW__FIELD_NAME: WrapperField = WrapperField("INCHIShadow", FieldType.STRING)
    ISGHSCLASSIFIED__FIELD_NAME: WrapperField = WrapperField("IsGHSClassified", FieldType.BOOLEAN)
    MOL__FIELD_NAME: WrapperField = WrapperField("MOL", FieldType.STRING)
    MOLECULARWEIGHT__FIELD_NAME: WrapperField = WrapperField("MolecularWeight", FieldType.DOUBLE)
    MOLREGNO__FIELD_NAME: WrapperField = WrapperField("molregno", FieldType.LONG)
    POLARSURFACEAREA__FIELD_NAME: WrapperField = WrapperField("PolarSurfaceArea", FieldType.DOUBLE)
    PUBCHEMCID__FIELD_NAME: WrapperField = WrapperField("PubchemCid", FieldType.INTEGER)
    QUANTITYONHAND__FIELD_NAME: WrapperField = WrapperField("QuantityOnHand", FieldType.DOUBLE)
    QUANTITYPERITEM__FIELD_NAME: WrapperField = WrapperField("QuantityPerItem", FieldType.DOUBLE)
    REGISTRYID__FIELD_NAME: WrapperField = WrapperField("RegistryId", FieldType.STRING)
    REORDERLEVELQUANTITY__FIELD_NAME: WrapperField = WrapperField("ReorderLevelQuantity", FieldType.DOUBLE)
    SALTS__FIELD_NAME: WrapperField = WrapperField("Salts", FieldType.STRING)
    SMILES__FIELD_NAME: WrapperField = WrapperField("SMILES", FieldType.STRING)
    SMILESSHADOW__FIELD_NAME: WrapperField = WrapperField("SMILESShadow", FieldType.STRING)
    SUBSTANCECLASS__FIELD_NAME: WrapperField = WrapperField("SubstanceClass", FieldType.STRING)
    TOTALHBONDCOUNT__FIELD_NAME: WrapperField = WrapperField("TotalHBondCount", FieldType.INTEGER)
    UNITS__FIELD_NAME: WrapperField = WrapperField("Units", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_CAS_field(self, value: Optional[str]):
        """
        Set data field with field name 'CAS' on this record model
        """
        self.set_field_value(self.CAS__FIELD_NAME.field_name, value)

    def get_CAS_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CAS' from this record model
        """
        return self.get_field_value(self.CAS__FIELD_NAME.field_name)

    def set_Charge_field(self, value: Optional[int]):
        """
        Set data field with field name 'Charge' on this record model
        """
        self.set_field_value(self.CHARGE__FIELD_NAME.field_name, value)

    def get_Charge_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Charge' from this record model
        """
        return self.get_field_value(self.CHARGE__FIELD_NAME.field_name)

    def set_ChemBLId_field(self, value: Optional[str]):
        """
        Set data field with field name 'ChemBLId' on this record model
        """
        self.set_field_value(self.CHEMBLID__FIELD_NAME.field_name, value)

    def get_ChemBLId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ChemBLId' from this record model
        """
        return self.get_field_value(self.CHEMBLID__FIELD_NAME.field_name)

    def set_cLogP_field(self, value: Optional[float]):
        """
        Set data field with field name 'cLogP' on this record model
        """
        self.set_field_value(self.CLOGP__FIELD_NAME.field_name, value)

    def get_cLogP_field(self) -> Optional[float]:
        """
        Get data field value with field name 'cLogP' from this record model
        """
        return self.get_field_value(self.CLOGP__FIELD_NAME.field_name)

    def set_ConsumableType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableType' on this record model
        """
        self.set_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name, value)

    def get_ConsumableType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableType' from this record model
        """
        return self.get_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name)

    def set_EditLock_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EditLock' on this record model
        """
        self.set_field_value(self.EDITLOCK__FIELD_NAME.field_name, value)

    def get_EditLock_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EditLock' from this record model
        """
        return self.get_field_value(self.EDITLOCK__FIELD_NAME.field_name)

    def set_ExactMass_field(self, value: Optional[float]):
        """
        Set data field with field name 'ExactMass' on this record model
        """
        self.set_field_value(self.EXACTMASS__FIELD_NAME.field_name, value)

    def get_ExactMass_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ExactMass' from this record model
        """
        return self.get_field_value(self.EXACTMASS__FIELD_NAME.field_name)

    def set_Formula_field(self, value: Optional[str]):
        """
        Set data field with field name 'Formula' on this record model
        """
        self.set_field_value(self.FORMULA__FIELD_NAME.field_name, value)

    def get_Formula_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Formula' from this record model
        """
        return self.get_field_value(self.FORMULA__FIELD_NAME.field_name)

    def set_GHSCautionCode_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSCautionCode' on this record model
        """
        self.set_field_value(self.GHSCAUTIONCODE__FIELD_NAME.field_name, value)

    def get_GHSCautionCode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSCautionCode' from this record model
        """
        return self.get_field_value(self.GHSCAUTIONCODE__FIELD_NAME.field_name)

    def set_GHSHazardCode_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSHazardCode' on this record model
        """
        self.set_field_value(self.GHSHAZARDCODE__FIELD_NAME.field_name, value)

    def get_GHSHazardCode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSHazardCode' from this record model
        """
        return self.get_field_value(self.GHSHAZARDCODE__FIELD_NAME.field_name)

    def set_GHSPictoCode_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSPictoCode' on this record model
        """
        self.set_field_value(self.GHSPICTOCODE__FIELD_NAME.field_name, value)

    def get_GHSPictoCode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSPictoCode' from this record model
        """
        return self.get_field_value(self.GHSPICTOCODE__FIELD_NAME.field_name)

    def set_GHSSignal_field(self, value: Optional[str]):
        """
        Set data field with field name 'GHSSignal' on this record model
        """
        self.set_field_value(self.GHSSIGNAL__FIELD_NAME.field_name, value)

    def get_GHSSignal_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GHSSignal' from this record model
        """
        return self.get_field_value(self.GHSSIGNAL__FIELD_NAME.field_name)

    def set_inchi_field(self, value: Optional[str]):
        """
        Set data field with field name 'inchi' on this record model
        """
        self.set_field_value(self.INCHI__FIELD_NAME.field_name, value)

    def get_inchi_field(self) -> Optional[str]:
        """
        Get data field value with field name 'inchi' from this record model
        """
        return self.get_field_value(self.INCHI__FIELD_NAME.field_name)

    def set_INCHIShadow_field(self, value: Optional[str]):
        """
        Set data field with field name 'INCHIShadow' on this record model
        """
        self.set_field_value(self.INCHISHADOW__FIELD_NAME.field_name, value)

    def get_INCHIShadow_field(self) -> Optional[str]:
        """
        Get data field value with field name 'INCHIShadow' from this record model
        """
        return self.get_field_value(self.INCHISHADOW__FIELD_NAME.field_name)

    def set_IsGHSClassified_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsGHSClassified' on this record model
        """
        self.set_field_value(self.ISGHSCLASSIFIED__FIELD_NAME.field_name, value)

    def get_IsGHSClassified_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsGHSClassified' from this record model
        """
        return self.get_field_value(self.ISGHSCLASSIFIED__FIELD_NAME.field_name)

    def set_MOL_field(self, value: Optional[str]):
        """
        Set data field with field name 'MOL' on this record model
        """
        self.set_field_value(self.MOL__FIELD_NAME.field_name, value)

    def get_MOL_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MOL' from this record model
        """
        return self.get_field_value(self.MOL__FIELD_NAME.field_name)

    def set_MolecularWeight_field(self, value: Optional[float]):
        """
        Set data field with field name 'MolecularWeight' on this record model
        """
        self.set_field_value(self.MOLECULARWEIGHT__FIELD_NAME.field_name, value)

    def get_MolecularWeight_field(self) -> Optional[float]:
        """
        Get data field value with field name 'MolecularWeight' from this record model
        """
        return self.get_field_value(self.MOLECULARWEIGHT__FIELD_NAME.field_name)

    def set_molregno_field(self, value: Optional[int]):
        """
        Set data field with field name 'molregno' on this record model
        """
        self.set_field_value(self.MOLREGNO__FIELD_NAME.field_name, value)

    def get_molregno_field(self) -> Optional[int]:
        """
        Get data field value with field name 'molregno' from this record model
        """
        return self.get_field_value(self.MOLREGNO__FIELD_NAME.field_name)

    def set_PolarSurfaceArea_field(self, value: Optional[float]):
        """
        Set data field with field name 'PolarSurfaceArea' on this record model
        """
        self.set_field_value(self.POLARSURFACEAREA__FIELD_NAME.field_name, value)

    def get_PolarSurfaceArea_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PolarSurfaceArea' from this record model
        """
        return self.get_field_value(self.POLARSURFACEAREA__FIELD_NAME.field_name)

    def set_PubchemCid_field(self, value: Optional[int]):
        """
        Set data field with field name 'PubchemCid' on this record model
        """
        self.set_field_value(self.PUBCHEMCID__FIELD_NAME.field_name, value)

    def get_PubchemCid_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PubchemCid' from this record model
        """
        return self.get_field_value(self.PUBCHEMCID__FIELD_NAME.field_name)

    def set_QuantityOnHand_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityOnHand' on this record model
        """
        self.set_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name, value)

    def get_QuantityOnHand_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityOnHand' from this record model
        """
        return self.get_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name)

    def set_QuantityPerItem_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityPerItem' on this record model
        """
        self.set_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name, value)

    def get_QuantityPerItem_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityPerItem' from this record model
        """
        return self.get_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name)

    def set_RegistryId_field(self, value: Optional[str]):
        """
        Set data field with field name 'RegistryId' on this record model
        """
        self.set_field_value(self.REGISTRYID__FIELD_NAME.field_name, value)

    def get_RegistryId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RegistryId' from this record model
        """
        return self.get_field_value(self.REGISTRYID__FIELD_NAME.field_name)

    def set_ReorderLevelQuantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'ReorderLevelQuantity' on this record model
        """
        self.set_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name, value)

    def get_ReorderLevelQuantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ReorderLevelQuantity' from this record model
        """
        return self.get_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name)

    def set_Salts_field(self, value: Optional[str]):
        """
        Set data field with field name 'Salts' on this record model
        """
        self.set_field_value(self.SALTS__FIELD_NAME.field_name, value)

    def get_Salts_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Salts' from this record model
        """
        return self.get_field_value(self.SALTS__FIELD_NAME.field_name)

    def set_SMILES_field(self, value: Optional[str]):
        """
        Set data field with field name 'SMILES' on this record model
        """
        self.set_field_value(self.SMILES__FIELD_NAME.field_name, value)

    def get_SMILES_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SMILES' from this record model
        """
        return self.get_field_value(self.SMILES__FIELD_NAME.field_name)

    def set_SMILESShadow_field(self, value: Optional[str]):
        """
        Set data field with field name 'SMILESShadow' on this record model
        """
        self.set_field_value(self.SMILESSHADOW__FIELD_NAME.field_name, value)

    def get_SMILESShadow_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SMILESShadow' from this record model
        """
        return self.get_field_value(self.SMILESSHADOW__FIELD_NAME.field_name)

    def set_SubstanceClass_field(self, value: Optional[str]):
        """
        Set data field with field name 'SubstanceClass' on this record model
        """
        self.set_field_value(self.SUBSTANCECLASS__FIELD_NAME.field_name, value)

    def get_SubstanceClass_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SubstanceClass' from this record model
        """
        return self.get_field_value(self.SUBSTANCECLASS__FIELD_NAME.field_name)

    def set_TotalHBondCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'TotalHBondCount' on this record model
        """
        self.set_field_value(self.TOTALHBONDCOUNT__FIELD_NAME.field_name, value)

    def get_TotalHBondCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TotalHBondCount' from this record model
        """
        return self.get_field_value(self.TOTALHBONDCOUNT__FIELD_NAME.field_name)

    def set_Units_field(self, value: Optional[str]):
        """
        Set data field with field name 'Units' on this record model
        """
        self.set_field_value(self.UNITS__FIELD_NAME.field_name, value)

    def get_Units_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Units' from this record model
        """
        return self.get_field_value(self.UNITS__FIELD_NAME.field_name)


class CompoundSaltConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type CompoundSaltConfig
    Data Type Display Name: Compound Salt Config (Compound Salt Configs)
    Fields: SaltId, SaltSMARTS
    The corporate compound salt database. This will be a list of SMARTS expressions that will be used for desalting when importing a compound part.
    """
    DATA_TYPE_NAME: str = 'CompoundSaltConfig'
    SALTID__FIELD_NAME: WrapperField = WrapperField("SaltId", FieldType.STRING)
    SALTSMARTS__FIELD_NAME: WrapperField = WrapperField("SaltSMARTS", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_SaltId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SaltId' on this record model
        """
        self.set_field_value(self.SALTID__FIELD_NAME.field_name, value)

    def get_SaltId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SaltId' from this record model
        """
        return self.get_field_value(self.SALTID__FIELD_NAME.field_name)

    def set_SaltSMARTS_field(self, value: Optional[str]):
        """
        Set data field with field name 'SaltSMARTS' on this record model
        """
        self.set_field_value(self.SALTSMARTS__FIELD_NAME.field_name, value)

    def get_SaltSMARTS_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SaltSMARTS' from this record model
        """
        return self.get_field_value(self.SALTSMARTS__FIELD_NAME.field_name)


class ConsumableModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Consumable
    Data Type Display Name: Reagent Part (Reagent Parts)
    Fields: ConsumableClassification, ConsumableName, ConsumableType, Description, EditConsumableType, PartNumber, QuantityOnHand, QuantityPerItem, ReorderLevelQuantity, Units, Vendor
    General definition of a consumable object.
    """
    DATA_TYPE_NAME: str = 'Consumable'
    CONSUMABLECLASSIFICATION__FIELD_NAME: WrapperField = WrapperField("ConsumableClassification", FieldType.SELECTION)
    CONSUMABLENAME__FIELD_NAME: WrapperField = WrapperField("ConsumableName", FieldType.AUTO_ACCESSION)
    CONSUMABLETYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableType", FieldType.SELECTION)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    EDITCONSUMABLETYPE__FIELD_NAME: WrapperField = WrapperField("EditConsumableType", FieldType.BOOLEAN)
    PARTNUMBER__FIELD_NAME: WrapperField = WrapperField("PartNumber", FieldType.STRING)
    QUANTITYONHAND__FIELD_NAME: WrapperField = WrapperField("QuantityOnHand", FieldType.DOUBLE)
    QUANTITYPERITEM__FIELD_NAME: WrapperField = WrapperField("QuantityPerItem", FieldType.DOUBLE)
    REORDERLEVELQUANTITY__FIELD_NAME: WrapperField = WrapperField("ReorderLevelQuantity", FieldType.DOUBLE)
    UNITS__FIELD_NAME: WrapperField = WrapperField("Units", FieldType.PICKLIST)
    VENDOR__FIELD_NAME: WrapperField = WrapperField("Vendor", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ConsumableClassification_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableClassification' on this record model
        """
        self.set_field_value(self.CONSUMABLECLASSIFICATION__FIELD_NAME.field_name, value)

    def get_ConsumableClassification_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableClassification' from this record model
        """
        return self.get_field_value(self.CONSUMABLECLASSIFICATION__FIELD_NAME.field_name)

    def set_ConsumableName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableName' on this record model
        """
        self.set_field_value(self.CONSUMABLENAME__FIELD_NAME.field_name, value)

    def get_ConsumableName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableName' from this record model
        """
        return self.get_field_value(self.CONSUMABLENAME__FIELD_NAME.field_name)

    def set_ConsumableType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableType' on this record model
        """
        self.set_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name, value)

    def get_ConsumableType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableType' from this record model
        """
        return self.get_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_EditConsumableType_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EditConsumableType' on this record model
        """
        self.set_field_value(self.EDITCONSUMABLETYPE__FIELD_NAME.field_name, value)

    def get_EditConsumableType_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EditConsumableType' from this record model
        """
        return self.get_field_value(self.EDITCONSUMABLETYPE__FIELD_NAME.field_name)

    def set_PartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PartNumber' on this record model
        """
        self.set_field_value(self.PARTNUMBER__FIELD_NAME.field_name, value)

    def get_PartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PartNumber' from this record model
        """
        return self.get_field_value(self.PARTNUMBER__FIELD_NAME.field_name)

    def set_QuantityOnHand_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityOnHand' on this record model
        """
        self.set_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name, value)

    def get_QuantityOnHand_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityOnHand' from this record model
        """
        return self.get_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name)

    def set_QuantityPerItem_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityPerItem' on this record model
        """
        self.set_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name, value)

    def get_QuantityPerItem_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityPerItem' from this record model
        """
        return self.get_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name)

    def set_ReorderLevelQuantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'ReorderLevelQuantity' on this record model
        """
        self.set_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name, value)

    def get_ReorderLevelQuantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ReorderLevelQuantity' from this record model
        """
        return self.get_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name)

    def set_Units_field(self, value: Optional[str]):
        """
        Set data field with field name 'Units' on this record model
        """
        self.set_field_value(self.UNITS__FIELD_NAME.field_name, value)

    def get_Units_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Units' from this record model
        """
        return self.get_field_value(self.UNITS__FIELD_NAME.field_name)

    def set_Vendor_field(self, value: Optional[str]):
        """
        Set data field with field name 'Vendor' on this record model
        """
        self.set_field_value(self.VENDOR__FIELD_NAME.field_name, value)

    def get_Vendor_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Vendor' from this record model
        """
        return self.get_field_value(self.VENDOR__FIELD_NAME.field_name)


class ConsumableItemModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ConsumableItem
    Data Type Display Name: Reagent (Reagents)
    Fields: ColPosition, ConsumableName, ConsumableType, ExpirationDate, Expired, KitLotNumbers, LotNumber, LotNumberDefined, PartNumber, RowPosition, StorageLocationBarcode, StorageUnitPath, Validated, ValidationDate, ValidationExperimentId, ValidationTechician
    Detailed representation of a more specific consumable object.
    """
    DATA_TYPE_NAME: str = 'ConsumableItem'
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    CONSUMABLENAME__FIELD_NAME: WrapperField = WrapperField("ConsumableName", FieldType.STRING)
    CONSUMABLETYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableType", FieldType.SELECTION)
    EXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("ExpirationDate", FieldType.DATE)
    EXPIRED__FIELD_NAME: WrapperField = WrapperField("Expired", FieldType.BOOLEAN)
    KITLOTNUMBERS__FIELD_NAME: WrapperField = WrapperField("KitLotNumbers", FieldType.STRING)
    LOTNUMBER__FIELD_NAME: WrapperField = WrapperField("LotNumber", FieldType.STRING)
    LOTNUMBERDEFINED__FIELD_NAME: WrapperField = WrapperField("LotNumberDefined", FieldType.BOOLEAN)
    PARTNUMBER__FIELD_NAME: WrapperField = WrapperField("PartNumber", FieldType.STRING)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    STORAGELOCATIONBARCODE__FIELD_NAME: WrapperField = WrapperField("StorageLocationBarcode", FieldType.SELECTION)
    STORAGEUNITPATH__FIELD_NAME: WrapperField = WrapperField("StorageUnitPath", FieldType.STRING)
    VALIDATED__FIELD_NAME: WrapperField = WrapperField("Validated", FieldType.BOOLEAN)
    VALIDATIONDATE__FIELD_NAME: WrapperField = WrapperField("ValidationDate", FieldType.DATE)
    VALIDATIONEXPERIMENTID__FIELD_NAME: WrapperField = WrapperField("ValidationExperimentId", FieldType.STRING)
    VALIDATIONTECHICIAN__FIELD_NAME: WrapperField = WrapperField("ValidationTechician", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_ConsumableName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableName' on this record model
        """
        self.set_field_value(self.CONSUMABLENAME__FIELD_NAME.field_name, value)

    def get_ConsumableName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableName' from this record model
        """
        return self.get_field_value(self.CONSUMABLENAME__FIELD_NAME.field_name)

    def set_ConsumableType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableType' on this record model
        """
        self.set_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name, value)

    def get_ConsumableType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableType' from this record model
        """
        return self.get_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name)

    def set_ExpirationDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ExpirationDate' on this record model
        """
        self.set_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_ExpirationDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ExpirationDate' from this record model
        """
        return self.get_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name)

    def set_Expired_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Expired' on this record model
        """
        self.set_field_value(self.EXPIRED__FIELD_NAME.field_name, value)

    def get_Expired_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Expired' from this record model
        """
        return self.get_field_value(self.EXPIRED__FIELD_NAME.field_name)

    def set_KitLotNumbers_field(self, value: Optional[str]):
        """
        Set data field with field name 'KitLotNumbers' on this record model
        """
        self.set_field_value(self.KITLOTNUMBERS__FIELD_NAME.field_name, value)

    def get_KitLotNumbers_field(self) -> Optional[str]:
        """
        Get data field value with field name 'KitLotNumbers' from this record model
        """
        return self.get_field_value(self.KITLOTNUMBERS__FIELD_NAME.field_name)

    def set_LotNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'LotNumber' on this record model
        """
        self.set_field_value(self.LOTNUMBER__FIELD_NAME.field_name, value)

    def get_LotNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LotNumber' from this record model
        """
        return self.get_field_value(self.LOTNUMBER__FIELD_NAME.field_name)

    def set_LotNumberDefined_field(self, value: Optional[bool]):
        """
        Set data field with field name 'LotNumberDefined' on this record model
        """
        self.set_field_value(self.LOTNUMBERDEFINED__FIELD_NAME.field_name, value)

    def get_LotNumberDefined_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'LotNumberDefined' from this record model
        """
        return self.get_field_value(self.LOTNUMBERDEFINED__FIELD_NAME.field_name)

    def set_PartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PartNumber' on this record model
        """
        self.set_field_value(self.PARTNUMBER__FIELD_NAME.field_name, value)

    def get_PartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PartNumber' from this record model
        """
        return self.get_field_value(self.PARTNUMBER__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_StorageLocationBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageLocationBarcode' on this record model
        """
        self.set_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name, value)

    def get_StorageLocationBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageLocationBarcode' from this record model
        """
        return self.get_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name)

    def set_StorageUnitPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitPath' on this record model
        """
        self.set_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name, value)

    def get_StorageUnitPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitPath' from this record model
        """
        return self.get_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name)

    def set_Validated_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Validated' on this record model
        """
        self.set_field_value(self.VALIDATED__FIELD_NAME.field_name, value)

    def get_Validated_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Validated' from this record model
        """
        return self.get_field_value(self.VALIDATED__FIELD_NAME.field_name)

    def set_ValidationDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ValidationDate' on this record model
        """
        self.set_field_value(self.VALIDATIONDATE__FIELD_NAME.field_name, value)

    def get_ValidationDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ValidationDate' from this record model
        """
        return self.get_field_value(self.VALIDATIONDATE__FIELD_NAME.field_name)

    def set_ValidationExperimentId_field(self, value: Optional[str]):
        """
        Set data field with field name 'ValidationExperimentId' on this record model
        """
        self.set_field_value(self.VALIDATIONEXPERIMENTID__FIELD_NAME.field_name, value)

    def get_ValidationExperimentId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ValidationExperimentId' from this record model
        """
        return self.get_field_value(self.VALIDATIONEXPERIMENTID__FIELD_NAME.field_name)

    def set_ValidationTechician_field(self, value: Optional[str]):
        """
        Set data field with field name 'ValidationTechician' on this record model
        """
        self.set_field_value(self.VALIDATIONTECHICIAN__FIELD_NAME.field_name, value)

    def get_ValidationTechician_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ValidationTechician' from this record model
        """
        return self.get_field_value(self.VALIDATIONTECHICIAN__FIELD_NAME.field_name)


class ConsumableLotUsageModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ConsumableLotUsage
    Data Type Display Name: Consumable Lot Usage (Consumable Lot Usages)
    Fields: ActiveTaskId, BarcodeFieldName, ConsumableBarcode, ElnId, ExpRecordId, LotNumber, LotNumberFieldName, LotRecordId, QuantityUsed
    Data type used in workflows to allow memory of what is used.
    """
    DATA_TYPE_NAME: str = 'ConsumableLotUsage'
    ACTIVETASKID__FIELD_NAME: WrapperField = WrapperField("ActiveTaskId", FieldType.LONG)
    BARCODEFIELDNAME__FIELD_NAME: WrapperField = WrapperField("BarcodeFieldName", FieldType.STRING)
    CONSUMABLEBARCODE__FIELD_NAME: WrapperField = WrapperField("ConsumableBarcode", FieldType.STRING)
    ELNID__FIELD_NAME: WrapperField = WrapperField("ElnId", FieldType.STRING)
    EXPRECORDID__FIELD_NAME: WrapperField = WrapperField("ExpRecordId", FieldType.LONG)
    LOTNUMBER__FIELD_NAME: WrapperField = WrapperField("LotNumber", FieldType.STRING)
    LOTNUMBERFIELDNAME__FIELD_NAME: WrapperField = WrapperField("LotNumberFieldName", FieldType.STRING)
    LOTRECORDID__FIELD_NAME: WrapperField = WrapperField("LotRecordId", FieldType.LONG)
    QUANTITYUSED__FIELD_NAME: WrapperField = WrapperField("QuantityUsed", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActiveTaskId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ActiveTaskId' on this record model
        """
        self.set_field_value(self.ACTIVETASKID__FIELD_NAME.field_name, value)

    def get_ActiveTaskId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ActiveTaskId' from this record model
        """
        return self.get_field_value(self.ACTIVETASKID__FIELD_NAME.field_name)

    def set_BarcodeFieldName_field(self, value: Optional[str]):
        """
        Set data field with field name 'BarcodeFieldName' on this record model
        """
        self.set_field_value(self.BARCODEFIELDNAME__FIELD_NAME.field_name, value)

    def get_BarcodeFieldName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BarcodeFieldName' from this record model
        """
        return self.get_field_value(self.BARCODEFIELDNAME__FIELD_NAME.field_name)

    def set_ConsumableBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableBarcode' on this record model
        """
        self.set_field_value(self.CONSUMABLEBARCODE__FIELD_NAME.field_name, value)

    def get_ConsumableBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableBarcode' from this record model
        """
        return self.get_field_value(self.CONSUMABLEBARCODE__FIELD_NAME.field_name)

    def set_ElnId_field(self, value: Optional[str]):
        """
        Set data field with field name 'ElnId' on this record model
        """
        self.set_field_value(self.ELNID__FIELD_NAME.field_name, value)

    def get_ElnId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ElnId' from this record model
        """
        return self.get_field_value(self.ELNID__FIELD_NAME.field_name)

    def set_ExpRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ExpRecordId' on this record model
        """
        self.set_field_value(self.EXPRECORDID__FIELD_NAME.field_name, value)

    def get_ExpRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ExpRecordId' from this record model
        """
        return self.get_field_value(self.EXPRECORDID__FIELD_NAME.field_name)

    def set_LotNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'LotNumber' on this record model
        """
        self.set_field_value(self.LOTNUMBER__FIELD_NAME.field_name, value)

    def get_LotNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LotNumber' from this record model
        """
        return self.get_field_value(self.LOTNUMBER__FIELD_NAME.field_name)

    def set_LotNumberFieldName_field(self, value: Optional[str]):
        """
        Set data field with field name 'LotNumberFieldName' on this record model
        """
        self.set_field_value(self.LOTNUMBERFIELDNAME__FIELD_NAME.field_name, value)

    def get_LotNumberFieldName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LotNumberFieldName' from this record model
        """
        return self.get_field_value(self.LOTNUMBERFIELDNAME__FIELD_NAME.field_name)

    def set_LotRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'LotRecordId' on this record model
        """
        self.set_field_value(self.LOTRECORDID__FIELD_NAME.field_name, value)

    def get_LotRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LotRecordId' from this record model
        """
        return self.get_field_value(self.LOTRECORDID__FIELD_NAME.field_name)

    def set_QuantityUsed_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityUsed' on this record model
        """
        self.set_field_value(self.QUANTITYUSED__FIELD_NAME.field_name, value)

    def get_QuantityUsed_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityUsed' from this record model
        """
        return self.get_field_value(self.QUANTITYUSED__FIELD_NAME.field_name)


class DirectoryModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Directory
    Data Type Display Name: Directory (Directories)
    Fields: DirectoryName
    """
    DATA_TYPE_NAME: str = 'Directory'
    DIRECTORYNAME__FIELD_NAME: WrapperField = WrapperField("DirectoryName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DirectoryName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DirectoryName' on this record model
        """
        self.set_field_value(self.DIRECTORYNAME__FIELD_NAME.field_name, value)

    def get_DirectoryName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DirectoryName' from this record model
        """
        return self.get_field_value(self.DIRECTORYNAME__FIELD_NAME.field_name)


class ELNExperimentModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ELNExperiment
    Data Type Display Name: Experiment (Experiments)
    Fields: DataTypeId, TemplateExperimentName, TemplateVersion, VeloxCompletedBy, VeloxDateCompleted, VeloxExperimentStatus, VELOXOWNER
    Data type to represent the base E-Notebook data type.
    """
    DATA_TYPE_NAME: str = 'ELNExperiment'
    DATATYPEID__FIELD_NAME: WrapperField = WrapperField("DataTypeId", FieldType.LONG)
    TEMPLATEEXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("TemplateExperimentName", FieldType.STRING)
    TEMPLATEVERSION__FIELD_NAME: WrapperField = WrapperField("TemplateVersion", FieldType.LONG)
    VELOXCOMPLETEDBY__FIELD_NAME: WrapperField = WrapperField("VeloxCompletedBy", FieldType.STRING)
    VELOXDATECOMPLETED__FIELD_NAME: WrapperField = WrapperField("VeloxDateCompleted", FieldType.DATE)
    VELOXEXPERIMENTSTATUS__FIELD_NAME: WrapperField = WrapperField("VeloxExperimentStatus", FieldType.STRING)
    VELOXOWNER__FIELD_NAME: WrapperField = WrapperField("VELOXOWNER", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DataTypeId_field(self, value: Optional[int]):
        """
        Set data field with field name 'DataTypeId' on this record model
        """
        self.set_field_value(self.DATATYPEID__FIELD_NAME.field_name, value)

    def get_DataTypeId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DataTypeId' from this record model
        """
        return self.get_field_value(self.DATATYPEID__FIELD_NAME.field_name)

    def set_TemplateExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateExperimentName' on this record model
        """
        self.set_field_value(self.TEMPLATEEXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_TemplateExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateExperimentName' from this record model
        """
        return self.get_field_value(self.TEMPLATEEXPERIMENTNAME__FIELD_NAME.field_name)

    def set_TemplateVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'TemplateVersion' on this record model
        """
        self.set_field_value(self.TEMPLATEVERSION__FIELD_NAME.field_name, value)

    def get_TemplateVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TemplateVersion' from this record model
        """
        return self.get_field_value(self.TEMPLATEVERSION__FIELD_NAME.field_name)

    def set_VeloxCompletedBy_field(self, value: Optional[str]):
        """
        Set data field with field name 'VeloxCompletedBy' on this record model
        """
        self.set_field_value(self.VELOXCOMPLETEDBY__FIELD_NAME.field_name, value)

    def get_VeloxCompletedBy_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VeloxCompletedBy' from this record model
        """
        return self.get_field_value(self.VELOXCOMPLETEDBY__FIELD_NAME.field_name)

    def set_VeloxDateCompleted_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxDateCompleted' on this record model
        """
        self.set_field_value(self.VELOXDATECOMPLETED__FIELD_NAME.field_name, value)

    def get_VeloxDateCompleted_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxDateCompleted' from this record model
        """
        return self.get_field_value(self.VELOXDATECOMPLETED__FIELD_NAME.field_name)

    def set_VeloxExperimentStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'VeloxExperimentStatus' on this record model
        """
        self.set_field_value(self.VELOXEXPERIMENTSTATUS__FIELD_NAME.field_name, value)

    def get_VeloxExperimentStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VeloxExperimentStatus' from this record model
        """
        return self.get_field_value(self.VELOXEXPERIMENTSTATUS__FIELD_NAME.field_name)

    def set_VELOXOWNER_field(self, value: Optional[str]):
        """
        Set data field with field name 'VELOXOWNER' on this record model
        """
        self.set_field_value(self.VELOXOWNER__FIELD_NAME.field_name, value)

    def get_VELOXOWNER_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VELOXOWNER' from this record model
        """
        return self.get_field_value(self.VELOXOWNER__FIELD_NAME.field_name)


class ELNExperimentDetailModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ELNExperimentDetail
    Data Type Display Name: Experiment Detail (Experiment Details)
    Fields: DataTypeId
    Data type to represent the base E-Notebook data type to represent the experiment details.
    """
    DATA_TYPE_NAME: str = 'ELNExperimentDetail'
    DATATYPEID__FIELD_NAME: WrapperField = WrapperField("DataTypeId", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DataTypeId_field(self, value: Optional[int]):
        """
        Set data field with field name 'DataTypeId' on this record model
        """
        self.set_field_value(self.DATATYPEID__FIELD_NAME.field_name, value)

    def get_DataTypeId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DataTypeId' from this record model
        """
        return self.get_field_value(self.DATATYPEID__FIELD_NAME.field_name)


class ELNSampleDetailModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ELNSampleDetail
    Data Type Display Name: Sample Detail (Sample Details)
    Fields: DataTypeId, OtherSampleId, SampleId
    Data type to represent the base E-Notebook data type to represent the sample level details.
    """
    DATA_TYPE_NAME: str = 'ELNSampleDetail'
    DATATYPEID__FIELD_NAME: WrapperField = WrapperField("DataTypeId", FieldType.LONG)
    OTHERSAMPLEID__FIELD_NAME: WrapperField = WrapperField("OtherSampleId", FieldType.STRING)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DataTypeId_field(self, value: Optional[int]):
        """
        Set data field with field name 'DataTypeId' on this record model
        """
        self.set_field_value(self.DATATYPEID__FIELD_NAME.field_name, value)

    def get_DataTypeId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DataTypeId' from this record model
        """
        return self.get_field_value(self.DATATYPEID__FIELD_NAME.field_name)

    def set_OtherSampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'OtherSampleId' on this record model
        """
        self.set_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name, value)

    def get_OtherSampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OtherSampleId' from this record model
        """
        return self.get_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)


class ELNTextEntryDetailModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ELNTextEntryDetail
    Data Type Display Name: ELN Text Entry Detail (ELN Text Entry Details)
    Fields: FilePath, TextField, VeloxCurrentVersion
    This data type is used to store the latest PDF file that has been generated from a given notebook.
    """
    DATA_TYPE_NAME: str = 'ELNTextEntryDetail'
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    TEXTFIELD__FIELD_NAME: WrapperField = WrapperField("TextField", FieldType.STRING)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_TextField_field(self, value: Optional[str]):
        """
        Set data field with field name 'TextField' on this record model
        """
        self.set_field_value(self.TEXTFIELD__FIELD_NAME.field_name, value)

    def get_TextField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TextField' from this record model
        """
        return self.get_field_value(self.TEXTFIELD__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class EmailModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Email
    Data Type Display Name: Email (Emails)
    Fields: AddressedTo, Body, CarbonCopy, SentDate, SentFrom, Subject
    """
    DATA_TYPE_NAME: str = 'Email'
    ADDRESSEDTO__FIELD_NAME: WrapperField = WrapperField("AddressedTo", FieldType.STRING)
    BODY__FIELD_NAME: WrapperField = WrapperField("Body", FieldType.STRING)
    CARBONCOPY__FIELD_NAME: WrapperField = WrapperField("CarbonCopy", FieldType.STRING)
    SENTDATE__FIELD_NAME: WrapperField = WrapperField("SentDate", FieldType.DATE)
    SENTFROM__FIELD_NAME: WrapperField = WrapperField("SentFrom", FieldType.STRING)
    SUBJECT__FIELD_NAME: WrapperField = WrapperField("Subject", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AddressedTo_field(self, value: Optional[str]):
        """
        Set data field with field name 'AddressedTo' on this record model
        """
        self.set_field_value(self.ADDRESSEDTO__FIELD_NAME.field_name, value)

    def get_AddressedTo_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AddressedTo' from this record model
        """
        return self.get_field_value(self.ADDRESSEDTO__FIELD_NAME.field_name)

    def set_Body_field(self, value: Optional[str]):
        """
        Set data field with field name 'Body' on this record model
        """
        self.set_field_value(self.BODY__FIELD_NAME.field_name, value)

    def get_Body_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Body' from this record model
        """
        return self.get_field_value(self.BODY__FIELD_NAME.field_name)

    def set_CarbonCopy_field(self, value: Optional[str]):
        """
        Set data field with field name 'CarbonCopy' on this record model
        """
        self.set_field_value(self.CARBONCOPY__FIELD_NAME.field_name, value)

    def get_CarbonCopy_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CarbonCopy' from this record model
        """
        return self.get_field_value(self.CARBONCOPY__FIELD_NAME.field_name)

    def set_SentDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'SentDate' on this record model
        """
        self.set_field_value(self.SENTDATE__FIELD_NAME.field_name, value)

    def get_SentDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SentDate' from this record model
        """
        return self.get_field_value(self.SENTDATE__FIELD_NAME.field_name)

    def set_SentFrom_field(self, value: Optional[str]):
        """
        Set data field with field name 'SentFrom' on this record model
        """
        self.set_field_value(self.SENTFROM__FIELD_NAME.field_name, value)

    def get_SentFrom_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SentFrom' from this record model
        """
        return self.get_field_value(self.SENTFROM__FIELD_NAME.field_name)

    def set_Subject_field(self, value: Optional[str]):
        """
        Set data field with field name 'Subject' on this record model
        """
        self.set_field_value(self.SUBJECT__FIELD_NAME.field_name, value)

    def get_Subject_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Subject' from this record model
        """
        return self.get_field_value(self.SUBJECT__FIELD_NAME.field_name)


class EnbAttachmentThumbnailModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type EnbAttachmentThumbnail
    Data Type Display Name: E-Notebook Attachment Thumbnail (E-Notebook Attachment Thumbnails)
    Fields: FilePath, PageNumber, ResolutionHeight, ResolutionWidth, SinglePage, VeloxCurrentVersion
    An attachment that stores a cached thumbnail of a page from a document attached to an Experiment entry.
    """
    DATA_TYPE_NAME: str = 'EnbAttachmentThumbnail'
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    PAGENUMBER__FIELD_NAME: WrapperField = WrapperField("PageNumber", FieldType.INTEGER)
    RESOLUTIONHEIGHT__FIELD_NAME: WrapperField = WrapperField("ResolutionHeight", FieldType.INTEGER)
    RESOLUTIONWIDTH__FIELD_NAME: WrapperField = WrapperField("ResolutionWidth", FieldType.INTEGER)
    SINGLEPAGE__FIELD_NAME: WrapperField = WrapperField("SinglePage", FieldType.BOOLEAN)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_PageNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'PageNumber' on this record model
        """
        self.set_field_value(self.PAGENUMBER__FIELD_NAME.field_name, value)

    def get_PageNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PageNumber' from this record model
        """
        return self.get_field_value(self.PAGENUMBER__FIELD_NAME.field_name)

    def set_ResolutionHeight_field(self, value: Optional[int]):
        """
        Set data field with field name 'ResolutionHeight' on this record model
        """
        self.set_field_value(self.RESOLUTIONHEIGHT__FIELD_NAME.field_name, value)

    def get_ResolutionHeight_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ResolutionHeight' from this record model
        """
        return self.get_field_value(self.RESOLUTIONHEIGHT__FIELD_NAME.field_name)

    def set_ResolutionWidth_field(self, value: Optional[int]):
        """
        Set data field with field name 'ResolutionWidth' on this record model
        """
        self.set_field_value(self.RESOLUTIONWIDTH__FIELD_NAME.field_name, value)

    def get_ResolutionWidth_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ResolutionWidth' from this record model
        """
        return self.get_field_value(self.RESOLUTIONWIDTH__FIELD_NAME.field_name)

    def set_SinglePage_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SinglePage' on this record model
        """
        self.set_field_value(self.SINGLEPAGE__FIELD_NAME.field_name, value)

    def get_SinglePage_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SinglePage' from this record model
        """
        return self.get_field_value(self.SINGLEPAGE__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class ErrorMetricModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ErrorMetric
    Data Type Display Name: Error Metric (Error Metrics)
    Fields: ColRead, ErrorRate, Lane, LaneCol, PlusMinus
     <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'ErrorMetric'
    COLREAD__FIELD_NAME: WrapperField = WrapperField("ColRead", FieldType.STRING)
    ERRORRATE__FIELD_NAME: WrapperField = WrapperField("ErrorRate", FieldType.DOUBLE)
    LANE__FIELD_NAME: WrapperField = WrapperField("Lane", FieldType.LONG)
    LANECOL__FIELD_NAME: WrapperField = WrapperField("LaneCol", FieldType.STRING)
    PLUSMINUS__FIELD_NAME: WrapperField = WrapperField("PlusMinus", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColRead_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColRead' on this record model
        """
        self.set_field_value(self.COLREAD__FIELD_NAME.field_name, value)

    def get_ColRead_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColRead' from this record model
        """
        return self.get_field_value(self.COLREAD__FIELD_NAME.field_name)

    def set_ErrorRate_field(self, value: Optional[float]):
        """
        Set data field with field name 'ErrorRate' on this record model
        """
        self.set_field_value(self.ERRORRATE__FIELD_NAME.field_name, value)

    def get_ErrorRate_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ErrorRate' from this record model
        """
        return self.get_field_value(self.ERRORRATE__FIELD_NAME.field_name)

    def set_Lane_field(self, value: Optional[int]):
        """
        Set data field with field name 'Lane' on this record model
        """
        self.set_field_value(self.LANE__FIELD_NAME.field_name, value)

    def get_Lane_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Lane' from this record model
        """
        return self.get_field_value(self.LANE__FIELD_NAME.field_name)

    def set_LaneCol_field(self, value: Optional[str]):
        """
        Set data field with field name 'LaneCol' on this record model
        """
        self.set_field_value(self.LANECOL__FIELD_NAME.field_name, value)

    def get_LaneCol_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LaneCol' from this record model
        """
        return self.get_field_value(self.LANECOL__FIELD_NAME.field_name)

    def set_PlusMinus_field(self, value: Optional[float]):
        """
        Set data field with field name 'PlusMinus' on this record model
        """
        self.set_field_value(self.PLUSMINUS__FIELD_NAME.field_name, value)

    def get_PlusMinus_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PlusMinus' from this record model
        """
        return self.get_field_value(self.PLUSMINUS__FIELD_NAME.field_name)


class EventModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Event
    Data Type Display Name: Event (Event)
    Fields: Comments, EndDateTime, EventDescription, EventName, EventStatus, ReminderDateTime, ReminderSent, StartDateTime, UserName
    """
    DATA_TYPE_NAME: str = 'Event'
    COMMENTS__FIELD_NAME: WrapperField = WrapperField("Comments", FieldType.STRING)
    ENDDATETIME__FIELD_NAME: WrapperField = WrapperField("EndDateTime", FieldType.DATE)
    EVENTDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("EventDescription", FieldType.STRING)
    EVENTNAME__FIELD_NAME: WrapperField = WrapperField("EventName", FieldType.STRING)
    EVENTSTATUS__FIELD_NAME: WrapperField = WrapperField("EventStatus", FieldType.PICKLIST)
    REMINDERDATETIME__FIELD_NAME: WrapperField = WrapperField("ReminderDateTime", FieldType.DATE)
    REMINDERSENT__FIELD_NAME: WrapperField = WrapperField("ReminderSent", FieldType.BOOLEAN)
    STARTDATETIME__FIELD_NAME: WrapperField = WrapperField("StartDateTime", FieldType.DATE)
    USERNAME__FIELD_NAME: WrapperField = WrapperField("UserName", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Comments_field(self, value: Optional[str]):
        """
        Set data field with field name 'Comments' on this record model
        """
        self.set_field_value(self.COMMENTS__FIELD_NAME.field_name, value)

    def get_Comments_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Comments' from this record model
        """
        return self.get_field_value(self.COMMENTS__FIELD_NAME.field_name)

    def set_EndDateTime_field(self, value: Optional[int]):
        """
        Set data field with field name 'EndDateTime' on this record model
        """
        self.set_field_value(self.ENDDATETIME__FIELD_NAME.field_name, value)

    def get_EndDateTime_field(self) -> Optional[int]:
        """
        Get data field value with field name 'EndDateTime' from this record model
        """
        return self.get_field_value(self.ENDDATETIME__FIELD_NAME.field_name)

    def set_EventDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'EventDescription' on this record model
        """
        self.set_field_value(self.EVENTDESCRIPTION__FIELD_NAME.field_name, value)

    def get_EventDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EventDescription' from this record model
        """
        return self.get_field_value(self.EVENTDESCRIPTION__FIELD_NAME.field_name)

    def set_EventName_field(self, value: Optional[str]):
        """
        Set data field with field name 'EventName' on this record model
        """
        self.set_field_value(self.EVENTNAME__FIELD_NAME.field_name, value)

    def get_EventName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EventName' from this record model
        """
        return self.get_field_value(self.EVENTNAME__FIELD_NAME.field_name)

    def set_EventStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'EventStatus' on this record model
        """
        self.set_field_value(self.EVENTSTATUS__FIELD_NAME.field_name, value)

    def get_EventStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EventStatus' from this record model
        """
        return self.get_field_value(self.EVENTSTATUS__FIELD_NAME.field_name)

    def set_ReminderDateTime_field(self, value: Optional[int]):
        """
        Set data field with field name 'ReminderDateTime' on this record model
        """
        self.set_field_value(self.REMINDERDATETIME__FIELD_NAME.field_name, value)

    def get_ReminderDateTime_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ReminderDateTime' from this record model
        """
        return self.get_field_value(self.REMINDERDATETIME__FIELD_NAME.field_name)

    def set_ReminderSent_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ReminderSent' on this record model
        """
        self.set_field_value(self.REMINDERSENT__FIELD_NAME.field_name, value)

    def get_ReminderSent_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ReminderSent' from this record model
        """
        return self.get_field_value(self.REMINDERSENT__FIELD_NAME.field_name)

    def set_StartDateTime_field(self, value: Optional[int]):
        """
        Set data field with field name 'StartDateTime' on this record model
        """
        self.set_field_value(self.STARTDATETIME__FIELD_NAME.field_name, value)

    def get_StartDateTime_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StartDateTime' from this record model
        """
        return self.get_field_value(self.STARTDATETIME__FIELD_NAME.field_name)

    def set_UserName_field(self, value: Optional[str]):
        """
        Set data field with field name 'UserName' on this record model
        """
        self.set_field_value(self.USERNAME__FIELD_NAME.field_name, value)

    def get_UserName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UserName' from this record model
        """
        return self.get_field_value(self.USERNAME__FIELD_NAME.field_name)


class ExemplarConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ExemplarConfig
    Data Type Display Name: Sapio Configurations (Sapio Configurations)
    Fields: ActiveNotebooksInWorkQueue, AddAllUserAsCandidate, AddAllUserAsCandidateHelp, AddConsumablesToExperiments, AdditionalInstMaintEmails, AdditionalNotificationEmails, AdditionalQCMailingList, AlwaysLaunchInstMaintWorkflow, ApproverVisibleRoleType, AssignToProcessUserGroupList, AuthenticationRequired, BAMaxRegions, BAParseSelection, BARegions, BroadcastMaintAlert, BroadcastMaintUsers, CanModifyExistingVSMTPItems, ConfigureInstrumentFileField, ConsumableDataTypes, ConsumableDirectories, ConsumableTrackingAttribute, ConsumableTypeMaxTemp, CoolingStorageUnitTypes, CreateInWorkflow, DefaultELNExperimentGroupRoles, DefaultELNExperimentRoles, DefaultELNExperimentRolesHelp, DefineConsumableDataTypes, DefineConsumableDirectories, Delimiter, ELNCreateSmplExtentionMultiSel, ELNImportSamplesOverride, Email, EnableAutoLotPopulation, EnableBaselineSampleRec, EnableDND, EnableElnRoleCandidates, EnableMultiTenantDashboards, EnforceConsumableDirectory, EnforceExpiration, EnforceSufficientQuantity, ENotebookSignoffGroups, ENotebookSignoffGroupsHelp, EnumerateStorage, EsignEmailOwnerNotebookUnlock, EsignSendEmailOnDecision, EsignSendEmailOnEntryUnlock, EsignSendEmailOnNotebookUnlock, EsigRequireAllAuthor, EsigRequireAllAuthorHelp, ExperimentBannerExpFields, ExperimentBannerParentFields, ExportExemplarConfigButton, ExportFullConfigButton, ExportSelectedConfigButton, ExportStaticConfigurations, FARegions, GenerateItemBarcode, ImportBackupConfigButton, ImportBaseLineDescription, ImportExemplarConfigButton, ImportExportExemplarConfigText, ImportExportSystemConfigsText, ImportSystemConfigButton, MainDataTypeSelectionList, MatManEnableFeatureExt, MmSampleFieldsToDisplay, MultiLayerPlatePoolIfSameType, NewConsumableDirName, NotificationUsers, NotifyMaintTechnicians, OverrideGroups, PlasmidDataType, PlateDesignerPrimaryTypes, PlateScanToMatch, Port, PreNotificationInterval, PrintConsumableBarcode, QCMailingList, QuantityTracking, ReagentLotScanToMatch, RecordReportAccessGroups, RecordReportDataTypeList, RecordStorageEvents, ReqPortalManifestFieldNames, RequireESignature, RestrictAccessByLocation, ReviewerVisibleRoleType, S3AccessKeyId, S3SecretAcessKey, SaasMaxNumOfSamplesPerTrans, SaasMaxSamples, SaasMode, SampleReceivingEmails, SampleReceivingUserMenu, SampleScanToMatch, SampleSheetPath, SampleTypeMaximumTemperature, SDMSRootPath, SecureSocketLayer, SendTestMail, SMTPServer, SmtpUsername, StorageUnitViewerFillByConfig, SystemPassword, TemperatureEnforcement, TLSEnabled, TLSRequired, UseRequestDefaultLayout, VerificationTypes, ViiPlateSize, WitnessVisibleRoleType, WriteQCInputFileToUser
    """
    DATA_TYPE_NAME: str = 'ExemplarConfig'
    ACTIVENOTEBOOKSINWORKQUEUE__FIELD_NAME: WrapperField = WrapperField("ActiveNotebooksInWorkQueue", FieldType.BOOLEAN)
    ADDALLUSERASCANDIDATE__FIELD_NAME: WrapperField = WrapperField("AddAllUserAsCandidate", FieldType.BOOLEAN)
    ADDALLUSERASCANDIDATEHELP__FIELD_NAME: WrapperField = WrapperField("AddAllUserAsCandidateHelp", FieldType.STRING)
    ADDCONSUMABLESTOEXPERIMENTS__FIELD_NAME: WrapperField = WrapperField("AddConsumablesToExperiments", FieldType.BOOLEAN)
    ADDITIONALINSTMAINTEMAILS__FIELD_NAME: WrapperField = WrapperField("AdditionalInstMaintEmails", FieldType.STRING)
    ADDITIONALNOTIFICATIONEMAILS__FIELD_NAME: WrapperField = WrapperField("AdditionalNotificationEmails", FieldType.STRING)
    ADDITIONALQCMAILINGLIST__FIELD_NAME: WrapperField = WrapperField("AdditionalQCMailingList", FieldType.STRING)
    ALWAYSLAUNCHINSTMAINTWORKFLOW__FIELD_NAME: WrapperField = WrapperField("AlwaysLaunchInstMaintWorkflow", FieldType.BOOLEAN)
    APPROVERVISIBLEROLETYPE__FIELD_NAME: WrapperField = WrapperField("ApproverVisibleRoleType", FieldType.BOOLEAN)
    ASSIGNTOPROCESSUSERGROUPLIST__FIELD_NAME: WrapperField = WrapperField("AssignToProcessUserGroupList", FieldType.SELECTION)
    AUTHENTICATIONREQUIRED__FIELD_NAME: WrapperField = WrapperField("AuthenticationRequired", FieldType.BOOLEAN)
    BAMAXREGIONS__FIELD_NAME: WrapperField = WrapperField("BAMaxRegions", FieldType.SHORT)
    BAPARSESELECTION__FIELD_NAME: WrapperField = WrapperField("BAParseSelection", FieldType.PICKLIST)
    BAREGIONS__FIELD_NAME: WrapperField = WrapperField("BARegions", FieldType.SHORT)
    BROADCASTMAINTALERT__FIELD_NAME: WrapperField = WrapperField("BroadcastMaintAlert", FieldType.BOOLEAN)
    BROADCASTMAINTUSERS__FIELD_NAME: WrapperField = WrapperField("BroadcastMaintUsers", FieldType.SELECTION)
    CANMODIFYEXISTINGVSMTPITEMS__FIELD_NAME: WrapperField = WrapperField("CanModifyExistingVSMTPItems", FieldType.BOOLEAN)
    CONFIGUREINSTRUMENTFILEFIELD__FIELD_NAME: WrapperField = WrapperField("ConfigureInstrumentFileField", FieldType.ACTION)
    CONSUMABLEDATATYPES__FIELD_NAME: WrapperField = WrapperField("ConsumableDataTypes", FieldType.STRING)
    CONSUMABLEDIRECTORIES__FIELD_NAME: WrapperField = WrapperField("ConsumableDirectories", FieldType.STRING)
    CONSUMABLETRACKINGATTRIBUTE__FIELD_NAME: WrapperField = WrapperField("ConsumableTrackingAttribute", FieldType.PICKLIST)
    CONSUMABLETYPEMAXTEMP__FIELD_NAME: WrapperField = WrapperField("ConsumableTypeMaxTemp", FieldType.STRING)
    COOLINGSTORAGEUNITTYPES__FIELD_NAME: WrapperField = WrapperField("CoolingStorageUnitTypes", FieldType.SELECTION)
    CREATEINWORKFLOW__FIELD_NAME: WrapperField = WrapperField("CreateInWorkflow", FieldType.BOOLEAN)
    DEFAULTELNEXPERIMENTGROUPROLES__FIELD_NAME: WrapperField = WrapperField("DefaultELNExperimentGroupRoles", FieldType.SELECTION)
    DEFAULTELNEXPERIMENTROLES__FIELD_NAME: WrapperField = WrapperField("DefaultELNExperimentRoles", FieldType.SELECTION)
    DEFAULTELNEXPERIMENTROLESHELP__FIELD_NAME: WrapperField = WrapperField("DefaultELNExperimentRolesHelp", FieldType.STRING)
    DEFINECONSUMABLEDATATYPES__FIELD_NAME: WrapperField = WrapperField("DefineConsumableDataTypes", FieldType.ACTION)
    DEFINECONSUMABLEDIRECTORIES__FIELD_NAME: WrapperField = WrapperField("DefineConsumableDirectories", FieldType.ACTION)
    DELIMITER__FIELD_NAME: WrapperField = WrapperField("Delimiter", FieldType.STRING)
    ELNCREATESMPLEXTENTIONMULTISEL__FIELD_NAME: WrapperField = WrapperField("ELNCreateSmplExtentionMultiSel", FieldType.BOOLEAN)
    ELNIMPORTSAMPLESOVERRIDE__FIELD_NAME: WrapperField = WrapperField("ELNImportSamplesOverride", FieldType.STRING)
    EMAIL__FIELD_NAME: WrapperField = WrapperField("Email", FieldType.STRING)
    ENABLEAUTOLOTPOPULATION__FIELD_NAME: WrapperField = WrapperField("EnableAutoLotPopulation", FieldType.BOOLEAN)
    ENABLEBASELINESAMPLEREC__FIELD_NAME: WrapperField = WrapperField("EnableBaselineSampleRec", FieldType.BOOLEAN)
    ENABLEDND__FIELD_NAME: WrapperField = WrapperField("EnableDND", FieldType.BOOLEAN)
    ENABLEELNROLECANDIDATES__FIELD_NAME: WrapperField = WrapperField("EnableElnRoleCandidates", FieldType.BOOLEAN)
    ENABLEMULTITENANTDASHBOARDS__FIELD_NAME: WrapperField = WrapperField("EnableMultiTenantDashboards", FieldType.BOOLEAN)
    ENFORCECONSUMABLEDIRECTORY__FIELD_NAME: WrapperField = WrapperField("EnforceConsumableDirectory", FieldType.BOOLEAN)
    ENFORCEEXPIRATION__FIELD_NAME: WrapperField = WrapperField("EnforceExpiration", FieldType.BOOLEAN)
    ENFORCESUFFICIENTQUANTITY__FIELD_NAME: WrapperField = WrapperField("EnforceSufficientQuantity", FieldType.BOOLEAN)
    ENOTEBOOKSIGNOFFGROUPS__FIELD_NAME: WrapperField = WrapperField("ENotebookSignoffGroups", FieldType.SELECTION)
    ENOTEBOOKSIGNOFFGROUPSHELP__FIELD_NAME: WrapperField = WrapperField("ENotebookSignoffGroupsHelp", FieldType.STRING)
    ENUMERATESTORAGE__FIELD_NAME: WrapperField = WrapperField("EnumerateStorage", FieldType.BOOLEAN)
    ESIGNEMAILOWNERNOTEBOOKUNLOCK__FIELD_NAME: WrapperField = WrapperField("EsignEmailOwnerNotebookUnlock", FieldType.BOOLEAN)
    ESIGNSENDEMAILONDECISION__FIELD_NAME: WrapperField = WrapperField("EsignSendEmailOnDecision", FieldType.BOOLEAN)
    ESIGNSENDEMAILONENTRYUNLOCK__FIELD_NAME: WrapperField = WrapperField("EsignSendEmailOnEntryUnlock", FieldType.BOOLEAN)
    ESIGNSENDEMAILONNOTEBOOKUNLOCK__FIELD_NAME: WrapperField = WrapperField("EsignSendEmailOnNotebookUnlock", FieldType.BOOLEAN)
    ESIGREQUIREALLAUTHOR__FIELD_NAME: WrapperField = WrapperField("EsigRequireAllAuthor", FieldType.BOOLEAN)
    ESIGREQUIREALLAUTHORHELP__FIELD_NAME: WrapperField = WrapperField("EsigRequireAllAuthorHelp", FieldType.STRING)
    EXPERIMENTBANNEREXPFIELDS__FIELD_NAME: WrapperField = WrapperField("ExperimentBannerExpFields", FieldType.SELECTION)
    EXPERIMENTBANNERPARENTFIELDS__FIELD_NAME: WrapperField = WrapperField("ExperimentBannerParentFields", FieldType.SELECTION)
    EXPORTEXEMPLARCONFIGBUTTON__FIELD_NAME: WrapperField = WrapperField("ExportExemplarConfigButton", FieldType.ACTION)
    EXPORTFULLCONFIGBUTTON__FIELD_NAME: WrapperField = WrapperField("ExportFullConfigButton", FieldType.ACTION)
    EXPORTSELECTEDCONFIGBUTTON__FIELD_NAME: WrapperField = WrapperField("ExportSelectedConfigButton", FieldType.ACTION)
    EXPORTSTATICCONFIGURATIONS__FIELD_NAME: WrapperField = WrapperField("ExportStaticConfigurations", FieldType.ACTION)
    FAREGIONS__FIELD_NAME: WrapperField = WrapperField("FARegions", FieldType.INTEGER)
    GENERATEITEMBARCODE__FIELD_NAME: WrapperField = WrapperField("GenerateItemBarcode", FieldType.BOOLEAN)
    IMPORTBACKUPCONFIGBUTTON__FIELD_NAME: WrapperField = WrapperField("ImportBackupConfigButton", FieldType.ACTION)
    IMPORTBASELINEDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("ImportBaseLineDescription", FieldType.STRING)
    IMPORTEXEMPLARCONFIGBUTTON__FIELD_NAME: WrapperField = WrapperField("ImportExemplarConfigButton", FieldType.ACTION)
    IMPORTEXPORTEXEMPLARCONFIGTEXT__FIELD_NAME: WrapperField = WrapperField("ImportExportExemplarConfigText", FieldType.STRING)
    IMPORTEXPORTSYSTEMCONFIGSTEXT__FIELD_NAME: WrapperField = WrapperField("ImportExportSystemConfigsText", FieldType.STRING)
    IMPORTSYSTEMCONFIGBUTTON__FIELD_NAME: WrapperField = WrapperField("ImportSystemConfigButton", FieldType.ACTION)
    MAINDATATYPESELECTIONLIST__FIELD_NAME: WrapperField = WrapperField("MainDataTypeSelectionList", FieldType.SELECTION)
    MATMANENABLEFEATUREEXT__FIELD_NAME: WrapperField = WrapperField("MatManEnableFeatureExt", FieldType.BOOLEAN)
    MMSAMPLEFIELDSTODISPLAY__FIELD_NAME: WrapperField = WrapperField("MmSampleFieldsToDisplay", FieldType.SELECTION)
    MULTILAYERPLATEPOOLIFSAMETYPE__FIELD_NAME: WrapperField = WrapperField("MultiLayerPlatePoolIfSameType", FieldType.BOOLEAN)
    NEWCONSUMABLEDIRNAME__FIELD_NAME: WrapperField = WrapperField("NewConsumableDirName", FieldType.STRING)
    NOTIFICATIONUSERS__FIELD_NAME: WrapperField = WrapperField("NotificationUsers", FieldType.SELECTION)
    NOTIFYMAINTTECHNICIANS__FIELD_NAME: WrapperField = WrapperField("NotifyMaintTechnicians", FieldType.BOOLEAN)
    OVERRIDEGROUPS__FIELD_NAME: WrapperField = WrapperField("OverrideGroups", FieldType.SELECTION)
    PLASMIDDATATYPE__FIELD_NAME: WrapperField = WrapperField("PlasmidDataType", FieldType.SELECTION)
    PLATEDESIGNERPRIMARYTYPES__FIELD_NAME: WrapperField = WrapperField("PlateDesignerPrimaryTypes", FieldType.SELECTION)
    PLATESCANTOMATCH__FIELD_NAME: WrapperField = WrapperField("PlateScanToMatch", FieldType.SELECTION)
    PORT__FIELD_NAME: WrapperField = WrapperField("Port", FieldType.INTEGER)
    PRENOTIFICATIONINTERVAL__FIELD_NAME: WrapperField = WrapperField("PreNotificationInterval", FieldType.LONG)
    PRINTCONSUMABLEBARCODE__FIELD_NAME: WrapperField = WrapperField("PrintConsumableBarcode", FieldType.BOOLEAN)
    QCMAILINGLIST__FIELD_NAME: WrapperField = WrapperField("QCMailingList", FieldType.SELECTION)
    QUANTITYTRACKING__FIELD_NAME: WrapperField = WrapperField("QuantityTracking", FieldType.BOOLEAN)
    REAGENTLOTSCANTOMATCH__FIELD_NAME: WrapperField = WrapperField("ReagentLotScanToMatch", FieldType.SELECTION)
    RECORDREPORTACCESSGROUPS__FIELD_NAME: WrapperField = WrapperField("RecordReportAccessGroups", FieldType.SELECTION)
    RECORDREPORTDATATYPELIST__FIELD_NAME: WrapperField = WrapperField("RecordReportDataTypeList", FieldType.SELECTION)
    RECORDSTORAGEEVENTS__FIELD_NAME: WrapperField = WrapperField("RecordStorageEvents", FieldType.BOOLEAN)
    REQPORTALMANIFESTFIELDNAMES__FIELD_NAME: WrapperField = WrapperField("ReqPortalManifestFieldNames", FieldType.SELECTION)
    REQUIREESIGNATURE__FIELD_NAME: WrapperField = WrapperField("RequireESignature", FieldType.BOOLEAN)
    RESTRICTACCESSBYLOCATION__FIELD_NAME: WrapperField = WrapperField("RestrictAccessByLocation", FieldType.BOOLEAN)
    REVIEWERVISIBLEROLETYPE__FIELD_NAME: WrapperField = WrapperField("ReviewerVisibleRoleType", FieldType.BOOLEAN)
    S3ACCESSKEYID__FIELD_NAME: WrapperField = WrapperField("S3AccessKeyId", FieldType.STRING)
    S3SECRETACESSKEY__FIELD_NAME: WrapperField = WrapperField("S3SecretAcessKey", FieldType.STRING)
    SAASMAXNUMOFSAMPLESPERTRANS__FIELD_NAME: WrapperField = WrapperField("SaasMaxNumOfSamplesPerTrans", FieldType.LONG)
    SAASMAXSAMPLES__FIELD_NAME: WrapperField = WrapperField("SaasMaxSamples", FieldType.LONG)
    SAASMODE__FIELD_NAME: WrapperField = WrapperField("SaasMode", FieldType.BOOLEAN)
    SAMPLERECEIVINGEMAILS__FIELD_NAME: WrapperField = WrapperField("SampleReceivingEmails", FieldType.STRING)
    SAMPLERECEIVINGUSERMENU__FIELD_NAME: WrapperField = WrapperField("SampleReceivingUserMenu", FieldType.SELECTION)
    SAMPLESCANTOMATCH__FIELD_NAME: WrapperField = WrapperField("SampleScanToMatch", FieldType.SELECTION)
    SAMPLESHEETPATH__FIELD_NAME: WrapperField = WrapperField("SampleSheetPath", FieldType.STRING)
    SAMPLETYPEMAXIMUMTEMPERATURE__FIELD_NAME: WrapperField = WrapperField("SampleTypeMaximumTemperature", FieldType.STRING)
    SDMSROOTPATH__FIELD_NAME: WrapperField = WrapperField("SDMSRootPath", FieldType.STRING)
    SECURESOCKETLAYER__FIELD_NAME: WrapperField = WrapperField("SecureSocketLayer", FieldType.BOOLEAN)
    SENDTESTMAIL__FIELD_NAME: WrapperField = WrapperField("SendTestMail", FieldType.ACTION)
    SMTPSERVER__FIELD_NAME: WrapperField = WrapperField("SMTPServer", FieldType.STRING)
    SMTPUSERNAME__FIELD_NAME: WrapperField = WrapperField("SmtpUsername", FieldType.STRING)
    STORAGEUNITVIEWERFILLBYCONFIG__FIELD_NAME: WrapperField = WrapperField("StorageUnitViewerFillByConfig", FieldType.PICKLIST)
    SYSTEMPASSWORD__FIELD_NAME: WrapperField = WrapperField("SystemPassword", FieldType.STRING)
    TEMPERATUREENFORCEMENT__FIELD_NAME: WrapperField = WrapperField("TemperatureEnforcement", FieldType.PICKLIST)
    TLSENABLED__FIELD_NAME: WrapperField = WrapperField("TLSEnabled", FieldType.BOOLEAN)
    TLSREQUIRED__FIELD_NAME: WrapperField = WrapperField("TLSRequired", FieldType.BOOLEAN)
    USEREQUESTDEFAULTLAYOUT__FIELD_NAME: WrapperField = WrapperField("UseRequestDefaultLayout", FieldType.BOOLEAN)
    VERIFICATIONTYPES__FIELD_NAME: WrapperField = WrapperField("VerificationTypes", FieldType.PICKLIST)
    VIIPLATESIZE__FIELD_NAME: WrapperField = WrapperField("ViiPlateSize", FieldType.PICKLIST)
    WITNESSVISIBLEROLETYPE__FIELD_NAME: WrapperField = WrapperField("WitnessVisibleRoleType", FieldType.BOOLEAN)
    WRITEQCINPUTFILETOUSER__FIELD_NAME: WrapperField = WrapperField("WriteQCInputFileToUser", FieldType.BOOLEAN)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActiveNotebooksInWorkQueue_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ActiveNotebooksInWorkQueue' on this record model
        """
        self.set_field_value(self.ACTIVENOTEBOOKSINWORKQUEUE__FIELD_NAME.field_name, value)

    def get_ActiveNotebooksInWorkQueue_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ActiveNotebooksInWorkQueue' from this record model
        """
        return self.get_field_value(self.ACTIVENOTEBOOKSINWORKQUEUE__FIELD_NAME.field_name)

    def set_AddAllUserAsCandidate_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AddAllUserAsCandidate' on this record model
        """
        self.set_field_value(self.ADDALLUSERASCANDIDATE__FIELD_NAME.field_name, value)

    def get_AddAllUserAsCandidate_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AddAllUserAsCandidate' from this record model
        """
        return self.get_field_value(self.ADDALLUSERASCANDIDATE__FIELD_NAME.field_name)

    def set_AddAllUserAsCandidateHelp_field(self, value: Optional[str]):
        """
        Set data field with field name 'AddAllUserAsCandidateHelp' on this record model
        """
        self.set_field_value(self.ADDALLUSERASCANDIDATEHELP__FIELD_NAME.field_name, value)

    def get_AddAllUserAsCandidateHelp_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AddAllUserAsCandidateHelp' from this record model
        """
        return self.get_field_value(self.ADDALLUSERASCANDIDATEHELP__FIELD_NAME.field_name)

    def set_AddConsumablesToExperiments_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AddConsumablesToExperiments' on this record model
        """
        self.set_field_value(self.ADDCONSUMABLESTOEXPERIMENTS__FIELD_NAME.field_name, value)

    def get_AddConsumablesToExperiments_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AddConsumablesToExperiments' from this record model
        """
        return self.get_field_value(self.ADDCONSUMABLESTOEXPERIMENTS__FIELD_NAME.field_name)

    def set_AdditionalInstMaintEmails_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdditionalInstMaintEmails' on this record model
        """
        self.set_field_value(self.ADDITIONALINSTMAINTEMAILS__FIELD_NAME.field_name, value)

    def get_AdditionalInstMaintEmails_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdditionalInstMaintEmails' from this record model
        """
        return self.get_field_value(self.ADDITIONALINSTMAINTEMAILS__FIELD_NAME.field_name)

    def set_AdditionalNotificationEmails_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdditionalNotificationEmails' on this record model
        """
        self.set_field_value(self.ADDITIONALNOTIFICATIONEMAILS__FIELD_NAME.field_name, value)

    def get_AdditionalNotificationEmails_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdditionalNotificationEmails' from this record model
        """
        return self.get_field_value(self.ADDITIONALNOTIFICATIONEMAILS__FIELD_NAME.field_name)

    def set_AdditionalQCMailingList_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdditionalQCMailingList' on this record model
        """
        self.set_field_value(self.ADDITIONALQCMAILINGLIST__FIELD_NAME.field_name, value)

    def get_AdditionalQCMailingList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdditionalQCMailingList' from this record model
        """
        return self.get_field_value(self.ADDITIONALQCMAILINGLIST__FIELD_NAME.field_name)

    def set_AlwaysLaunchInstMaintWorkflow_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AlwaysLaunchInstMaintWorkflow' on this record model
        """
        self.set_field_value(self.ALWAYSLAUNCHINSTMAINTWORKFLOW__FIELD_NAME.field_name, value)

    def get_AlwaysLaunchInstMaintWorkflow_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AlwaysLaunchInstMaintWorkflow' from this record model
        """
        return self.get_field_value(self.ALWAYSLAUNCHINSTMAINTWORKFLOW__FIELD_NAME.field_name)

    def set_ApproverVisibleRoleType_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ApproverVisibleRoleType' on this record model
        """
        self.set_field_value(self.APPROVERVISIBLEROLETYPE__FIELD_NAME.field_name, value)

    def get_ApproverVisibleRoleType_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ApproverVisibleRoleType' from this record model
        """
        return self.get_field_value(self.APPROVERVISIBLEROLETYPE__FIELD_NAME.field_name)

    def set_AssignToProcessUserGroupList_field(self, value: Optional[str]):
        """
        Set data field with field name 'AssignToProcessUserGroupList' on this record model
        """
        self.set_field_value(self.ASSIGNTOPROCESSUSERGROUPLIST__FIELD_NAME.field_name, value)

    def get_AssignToProcessUserGroupList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AssignToProcessUserGroupList' from this record model
        """
        return self.get_field_value(self.ASSIGNTOPROCESSUSERGROUPLIST__FIELD_NAME.field_name)

    def set_AuthenticationRequired_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AuthenticationRequired' on this record model
        """
        self.set_field_value(self.AUTHENTICATIONREQUIRED__FIELD_NAME.field_name, value)

    def get_AuthenticationRequired_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AuthenticationRequired' from this record model
        """
        return self.get_field_value(self.AUTHENTICATIONREQUIRED__FIELD_NAME.field_name)

    def set_BAMaxRegions_field(self, value: Optional[int]):
        """
        Set data field with field name 'BAMaxRegions' on this record model
        """
        self.set_field_value(self.BAMAXREGIONS__FIELD_NAME.field_name, value)

    def get_BAMaxRegions_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BAMaxRegions' from this record model
        """
        return self.get_field_value(self.BAMAXREGIONS__FIELD_NAME.field_name)

    def set_BAParseSelection_field(self, value: Optional[str]):
        """
        Set data field with field name 'BAParseSelection' on this record model
        """
        self.set_field_value(self.BAPARSESELECTION__FIELD_NAME.field_name, value)

    def get_BAParseSelection_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BAParseSelection' from this record model
        """
        return self.get_field_value(self.BAPARSESELECTION__FIELD_NAME.field_name)

    def set_BARegions_field(self, value: Optional[int]):
        """
        Set data field with field name 'BARegions' on this record model
        """
        self.set_field_value(self.BAREGIONS__FIELD_NAME.field_name, value)

    def get_BARegions_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BARegions' from this record model
        """
        return self.get_field_value(self.BAREGIONS__FIELD_NAME.field_name)

    def set_BroadcastMaintAlert_field(self, value: Optional[bool]):
        """
        Set data field with field name 'BroadcastMaintAlert' on this record model
        """
        self.set_field_value(self.BROADCASTMAINTALERT__FIELD_NAME.field_name, value)

    def get_BroadcastMaintAlert_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'BroadcastMaintAlert' from this record model
        """
        return self.get_field_value(self.BROADCASTMAINTALERT__FIELD_NAME.field_name)

    def set_BroadcastMaintUsers_field(self, value: Optional[str]):
        """
        Set data field with field name 'BroadcastMaintUsers' on this record model
        """
        self.set_field_value(self.BROADCASTMAINTUSERS__FIELD_NAME.field_name, value)

    def get_BroadcastMaintUsers_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BroadcastMaintUsers' from this record model
        """
        return self.get_field_value(self.BROADCASTMAINTUSERS__FIELD_NAME.field_name)

    def set_CanModifyExistingVSMTPItems_field(self, value: Optional[bool]):
        """
        Set data field with field name 'CanModifyExistingVSMTPItems' on this record model
        """
        self.set_field_value(self.CANMODIFYEXISTINGVSMTPITEMS__FIELD_NAME.field_name, value)

    def get_CanModifyExistingVSMTPItems_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'CanModifyExistingVSMTPItems' from this record model
        """
        return self.get_field_value(self.CANMODIFYEXISTINGVSMTPITEMS__FIELD_NAME.field_name)

    def set_ConsumableDataTypes_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableDataTypes' on this record model
        """
        self.set_field_value(self.CONSUMABLEDATATYPES__FIELD_NAME.field_name, value)

    def get_ConsumableDataTypes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableDataTypes' from this record model
        """
        return self.get_field_value(self.CONSUMABLEDATATYPES__FIELD_NAME.field_name)

    def set_ConsumableDirectories_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableDirectories' on this record model
        """
        self.set_field_value(self.CONSUMABLEDIRECTORIES__FIELD_NAME.field_name, value)

    def get_ConsumableDirectories_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableDirectories' from this record model
        """
        return self.get_field_value(self.CONSUMABLEDIRECTORIES__FIELD_NAME.field_name)

    def set_ConsumableTrackingAttribute_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableTrackingAttribute' on this record model
        """
        self.set_field_value(self.CONSUMABLETRACKINGATTRIBUTE__FIELD_NAME.field_name, value)

    def get_ConsumableTrackingAttribute_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableTrackingAttribute' from this record model
        """
        return self.get_field_value(self.CONSUMABLETRACKINGATTRIBUTE__FIELD_NAME.field_name)

    def set_ConsumableTypeMaxTemp_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableTypeMaxTemp' on this record model
        """
        self.set_field_value(self.CONSUMABLETYPEMAXTEMP__FIELD_NAME.field_name, value)

    def get_ConsumableTypeMaxTemp_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableTypeMaxTemp' from this record model
        """
        return self.get_field_value(self.CONSUMABLETYPEMAXTEMP__FIELD_NAME.field_name)

    def set_CoolingStorageUnitTypes_field(self, value: Optional[str]):
        """
        Set data field with field name 'CoolingStorageUnitTypes' on this record model
        """
        self.set_field_value(self.COOLINGSTORAGEUNITTYPES__FIELD_NAME.field_name, value)

    def get_CoolingStorageUnitTypes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CoolingStorageUnitTypes' from this record model
        """
        return self.get_field_value(self.COOLINGSTORAGEUNITTYPES__FIELD_NAME.field_name)

    def set_CreateInWorkflow_field(self, value: Optional[bool]):
        """
        Set data field with field name 'CreateInWorkflow' on this record model
        """
        self.set_field_value(self.CREATEINWORKFLOW__FIELD_NAME.field_name, value)

    def get_CreateInWorkflow_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'CreateInWorkflow' from this record model
        """
        return self.get_field_value(self.CREATEINWORKFLOW__FIELD_NAME.field_name)

    def set_DefaultELNExperimentGroupRoles_field(self, value: Optional[str]):
        """
        Set data field with field name 'DefaultELNExperimentGroupRoles' on this record model
        """
        self.set_field_value(self.DEFAULTELNEXPERIMENTGROUPROLES__FIELD_NAME.field_name, value)

    def get_DefaultELNExperimentGroupRoles_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DefaultELNExperimentGroupRoles' from this record model
        """
        return self.get_field_value(self.DEFAULTELNEXPERIMENTGROUPROLES__FIELD_NAME.field_name)

    def set_DefaultELNExperimentRoles_field(self, value: Optional[str]):
        """
        Set data field with field name 'DefaultELNExperimentRoles' on this record model
        """
        self.set_field_value(self.DEFAULTELNEXPERIMENTROLES__FIELD_NAME.field_name, value)

    def get_DefaultELNExperimentRoles_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DefaultELNExperimentRoles' from this record model
        """
        return self.get_field_value(self.DEFAULTELNEXPERIMENTROLES__FIELD_NAME.field_name)

    def set_DefaultELNExperimentRolesHelp_field(self, value: Optional[str]):
        """
        Set data field with field name 'DefaultELNExperimentRolesHelp' on this record model
        """
        self.set_field_value(self.DEFAULTELNEXPERIMENTROLESHELP__FIELD_NAME.field_name, value)

    def get_DefaultELNExperimentRolesHelp_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DefaultELNExperimentRolesHelp' from this record model
        """
        return self.get_field_value(self.DEFAULTELNEXPERIMENTROLESHELP__FIELD_NAME.field_name)

    def set_Delimiter_field(self, value: Optional[str]):
        """
        Set data field with field name 'Delimiter' on this record model
        """
        self.set_field_value(self.DELIMITER__FIELD_NAME.field_name, value)

    def get_Delimiter_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Delimiter' from this record model
        """
        return self.get_field_value(self.DELIMITER__FIELD_NAME.field_name)

    def set_ELNCreateSmplExtentionMultiSel_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ELNCreateSmplExtentionMultiSel' on this record model
        """
        self.set_field_value(self.ELNCREATESMPLEXTENTIONMULTISEL__FIELD_NAME.field_name, value)

    def get_ELNCreateSmplExtentionMultiSel_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ELNCreateSmplExtentionMultiSel' from this record model
        """
        return self.get_field_value(self.ELNCREATESMPLEXTENTIONMULTISEL__FIELD_NAME.field_name)

    def set_ELNImportSamplesOverride_field(self, value: Optional[str]):
        """
        Set data field with field name 'ELNImportSamplesOverride' on this record model
        """
        self.set_field_value(self.ELNIMPORTSAMPLESOVERRIDE__FIELD_NAME.field_name, value)

    def get_ELNImportSamplesOverride_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ELNImportSamplesOverride' from this record model
        """
        return self.get_field_value(self.ELNIMPORTSAMPLESOVERRIDE__FIELD_NAME.field_name)

    def set_Email_field(self, value: Optional[str]):
        """
        Set data field with field name 'Email' on this record model
        """
        self.set_field_value(self.EMAIL__FIELD_NAME.field_name, value)

    def get_Email_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Email' from this record model
        """
        return self.get_field_value(self.EMAIL__FIELD_NAME.field_name)

    def set_EnableAutoLotPopulation_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableAutoLotPopulation' on this record model
        """
        self.set_field_value(self.ENABLEAUTOLOTPOPULATION__FIELD_NAME.field_name, value)

    def get_EnableAutoLotPopulation_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableAutoLotPopulation' from this record model
        """
        return self.get_field_value(self.ENABLEAUTOLOTPOPULATION__FIELD_NAME.field_name)

    def set_EnableBaselineSampleRec_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableBaselineSampleRec' on this record model
        """
        self.set_field_value(self.ENABLEBASELINESAMPLEREC__FIELD_NAME.field_name, value)

    def get_EnableBaselineSampleRec_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableBaselineSampleRec' from this record model
        """
        return self.get_field_value(self.ENABLEBASELINESAMPLEREC__FIELD_NAME.field_name)

    def set_EnableDND_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableDND' on this record model
        """
        self.set_field_value(self.ENABLEDND__FIELD_NAME.field_name, value)

    def get_EnableDND_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableDND' from this record model
        """
        return self.get_field_value(self.ENABLEDND__FIELD_NAME.field_name)

    def set_EnableElnRoleCandidates_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableElnRoleCandidates' on this record model
        """
        self.set_field_value(self.ENABLEELNROLECANDIDATES__FIELD_NAME.field_name, value)

    def get_EnableElnRoleCandidates_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableElnRoleCandidates' from this record model
        """
        return self.get_field_value(self.ENABLEELNROLECANDIDATES__FIELD_NAME.field_name)

    def set_EnableMultiTenantDashboards_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableMultiTenantDashboards' on this record model
        """
        self.set_field_value(self.ENABLEMULTITENANTDASHBOARDS__FIELD_NAME.field_name, value)

    def get_EnableMultiTenantDashboards_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableMultiTenantDashboards' from this record model
        """
        return self.get_field_value(self.ENABLEMULTITENANTDASHBOARDS__FIELD_NAME.field_name)

    def set_EnforceConsumableDirectory_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnforceConsumableDirectory' on this record model
        """
        self.set_field_value(self.ENFORCECONSUMABLEDIRECTORY__FIELD_NAME.field_name, value)

    def get_EnforceConsumableDirectory_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnforceConsumableDirectory' from this record model
        """
        return self.get_field_value(self.ENFORCECONSUMABLEDIRECTORY__FIELD_NAME.field_name)

    def set_EnforceExpiration_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnforceExpiration' on this record model
        """
        self.set_field_value(self.ENFORCEEXPIRATION__FIELD_NAME.field_name, value)

    def get_EnforceExpiration_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnforceExpiration' from this record model
        """
        return self.get_field_value(self.ENFORCEEXPIRATION__FIELD_NAME.field_name)

    def set_EnforceSufficientQuantity_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnforceSufficientQuantity' on this record model
        """
        self.set_field_value(self.ENFORCESUFFICIENTQUANTITY__FIELD_NAME.field_name, value)

    def get_EnforceSufficientQuantity_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnforceSufficientQuantity' from this record model
        """
        return self.get_field_value(self.ENFORCESUFFICIENTQUANTITY__FIELD_NAME.field_name)

    def set_ENotebookSignoffGroups_field(self, value: Optional[str]):
        """
        Set data field with field name 'ENotebookSignoffGroups' on this record model
        """
        self.set_field_value(self.ENOTEBOOKSIGNOFFGROUPS__FIELD_NAME.field_name, value)

    def get_ENotebookSignoffGroups_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ENotebookSignoffGroups' from this record model
        """
        return self.get_field_value(self.ENOTEBOOKSIGNOFFGROUPS__FIELD_NAME.field_name)

    def set_ENotebookSignoffGroupsHelp_field(self, value: Optional[str]):
        """
        Set data field with field name 'ENotebookSignoffGroupsHelp' on this record model
        """
        self.set_field_value(self.ENOTEBOOKSIGNOFFGROUPSHELP__FIELD_NAME.field_name, value)

    def get_ENotebookSignoffGroupsHelp_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ENotebookSignoffGroupsHelp' from this record model
        """
        return self.get_field_value(self.ENOTEBOOKSIGNOFFGROUPSHELP__FIELD_NAME.field_name)

    def set_EnumerateStorage_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnumerateStorage' on this record model
        """
        self.set_field_value(self.ENUMERATESTORAGE__FIELD_NAME.field_name, value)

    def get_EnumerateStorage_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnumerateStorage' from this record model
        """
        return self.get_field_value(self.ENUMERATESTORAGE__FIELD_NAME.field_name)

    def set_EsignEmailOwnerNotebookUnlock_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EsignEmailOwnerNotebookUnlock' on this record model
        """
        self.set_field_value(self.ESIGNEMAILOWNERNOTEBOOKUNLOCK__FIELD_NAME.field_name, value)

    def get_EsignEmailOwnerNotebookUnlock_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EsignEmailOwnerNotebookUnlock' from this record model
        """
        return self.get_field_value(self.ESIGNEMAILOWNERNOTEBOOKUNLOCK__FIELD_NAME.field_name)

    def set_EsignSendEmailOnDecision_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EsignSendEmailOnDecision' on this record model
        """
        self.set_field_value(self.ESIGNSENDEMAILONDECISION__FIELD_NAME.field_name, value)

    def get_EsignSendEmailOnDecision_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EsignSendEmailOnDecision' from this record model
        """
        return self.get_field_value(self.ESIGNSENDEMAILONDECISION__FIELD_NAME.field_name)

    def set_EsignSendEmailOnEntryUnlock_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EsignSendEmailOnEntryUnlock' on this record model
        """
        self.set_field_value(self.ESIGNSENDEMAILONENTRYUNLOCK__FIELD_NAME.field_name, value)

    def get_EsignSendEmailOnEntryUnlock_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EsignSendEmailOnEntryUnlock' from this record model
        """
        return self.get_field_value(self.ESIGNSENDEMAILONENTRYUNLOCK__FIELD_NAME.field_name)

    def set_EsignSendEmailOnNotebookUnlock_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EsignSendEmailOnNotebookUnlock' on this record model
        """
        self.set_field_value(self.ESIGNSENDEMAILONNOTEBOOKUNLOCK__FIELD_NAME.field_name, value)

    def get_EsignSendEmailOnNotebookUnlock_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EsignSendEmailOnNotebookUnlock' from this record model
        """
        return self.get_field_value(self.ESIGNSENDEMAILONNOTEBOOKUNLOCK__FIELD_NAME.field_name)

    def set_EsigRequireAllAuthor_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EsigRequireAllAuthor' on this record model
        """
        self.set_field_value(self.ESIGREQUIREALLAUTHOR__FIELD_NAME.field_name, value)

    def get_EsigRequireAllAuthor_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EsigRequireAllAuthor' from this record model
        """
        return self.get_field_value(self.ESIGREQUIREALLAUTHOR__FIELD_NAME.field_name)

    def set_EsigRequireAllAuthorHelp_field(self, value: Optional[str]):
        """
        Set data field with field name 'EsigRequireAllAuthorHelp' on this record model
        """
        self.set_field_value(self.ESIGREQUIREALLAUTHORHELP__FIELD_NAME.field_name, value)

    def get_EsigRequireAllAuthorHelp_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EsigRequireAllAuthorHelp' from this record model
        """
        return self.get_field_value(self.ESIGREQUIREALLAUTHORHELP__FIELD_NAME.field_name)

    def set_ExperimentBannerExpFields_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentBannerExpFields' on this record model
        """
        self.set_field_value(self.EXPERIMENTBANNEREXPFIELDS__FIELD_NAME.field_name, value)

    def get_ExperimentBannerExpFields_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentBannerExpFields' from this record model
        """
        return self.get_field_value(self.EXPERIMENTBANNEREXPFIELDS__FIELD_NAME.field_name)

    def set_ExperimentBannerParentFields_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentBannerParentFields' on this record model
        """
        self.set_field_value(self.EXPERIMENTBANNERPARENTFIELDS__FIELD_NAME.field_name, value)

    def get_ExperimentBannerParentFields_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentBannerParentFields' from this record model
        """
        return self.get_field_value(self.EXPERIMENTBANNERPARENTFIELDS__FIELD_NAME.field_name)

    def set_FARegions_field(self, value: Optional[int]):
        """
        Set data field with field name 'FARegions' on this record model
        """
        self.set_field_value(self.FAREGIONS__FIELD_NAME.field_name, value)

    def get_FARegions_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FARegions' from this record model
        """
        return self.get_field_value(self.FAREGIONS__FIELD_NAME.field_name)

    def set_GenerateItemBarcode_field(self, value: Optional[bool]):
        """
        Set data field with field name 'GenerateItemBarcode' on this record model
        """
        self.set_field_value(self.GENERATEITEMBARCODE__FIELD_NAME.field_name, value)

    def get_GenerateItemBarcode_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'GenerateItemBarcode' from this record model
        """
        return self.get_field_value(self.GENERATEITEMBARCODE__FIELD_NAME.field_name)

    def set_ImportBaseLineDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'ImportBaseLineDescription' on this record model
        """
        self.set_field_value(self.IMPORTBASELINEDESCRIPTION__FIELD_NAME.field_name, value)

    def get_ImportBaseLineDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ImportBaseLineDescription' from this record model
        """
        return self.get_field_value(self.IMPORTBASELINEDESCRIPTION__FIELD_NAME.field_name)

    def set_ImportExportExemplarConfigText_field(self, value: Optional[str]):
        """
        Set data field with field name 'ImportExportExemplarConfigText' on this record model
        """
        self.set_field_value(self.IMPORTEXPORTEXEMPLARCONFIGTEXT__FIELD_NAME.field_name, value)

    def get_ImportExportExemplarConfigText_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ImportExportExemplarConfigText' from this record model
        """
        return self.get_field_value(self.IMPORTEXPORTEXEMPLARCONFIGTEXT__FIELD_NAME.field_name)

    def set_ImportExportSystemConfigsText_field(self, value: Optional[str]):
        """
        Set data field with field name 'ImportExportSystemConfigsText' on this record model
        """
        self.set_field_value(self.IMPORTEXPORTSYSTEMCONFIGSTEXT__FIELD_NAME.field_name, value)

    def get_ImportExportSystemConfigsText_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ImportExportSystemConfigsText' from this record model
        """
        return self.get_field_value(self.IMPORTEXPORTSYSTEMCONFIGSTEXT__FIELD_NAME.field_name)

    def set_MainDataTypeSelectionList_field(self, value: Optional[str]):
        """
        Set data field with field name 'MainDataTypeSelectionList' on this record model
        """
        self.set_field_value(self.MAINDATATYPESELECTIONLIST__FIELD_NAME.field_name, value)

    def get_MainDataTypeSelectionList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MainDataTypeSelectionList' from this record model
        """
        return self.get_field_value(self.MAINDATATYPESELECTIONLIST__FIELD_NAME.field_name)

    def set_MatManEnableFeatureExt_field(self, value: Optional[bool]):
        """
        Set data field with field name 'MatManEnableFeatureExt' on this record model
        """
        self.set_field_value(self.MATMANENABLEFEATUREEXT__FIELD_NAME.field_name, value)

    def get_MatManEnableFeatureExt_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'MatManEnableFeatureExt' from this record model
        """
        return self.get_field_value(self.MATMANENABLEFEATUREEXT__FIELD_NAME.field_name)

    def set_MmSampleFieldsToDisplay_field(self, value: Optional[str]):
        """
        Set data field with field name 'MmSampleFieldsToDisplay' on this record model
        """
        self.set_field_value(self.MMSAMPLEFIELDSTODISPLAY__FIELD_NAME.field_name, value)

    def get_MmSampleFieldsToDisplay_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MmSampleFieldsToDisplay' from this record model
        """
        return self.get_field_value(self.MMSAMPLEFIELDSTODISPLAY__FIELD_NAME.field_name)

    def set_MultiLayerPlatePoolIfSameType_field(self, value: Optional[bool]):
        """
        Set data field with field name 'MultiLayerPlatePoolIfSameType' on this record model
        """
        self.set_field_value(self.MULTILAYERPLATEPOOLIFSAMETYPE__FIELD_NAME.field_name, value)

    def get_MultiLayerPlatePoolIfSameType_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'MultiLayerPlatePoolIfSameType' from this record model
        """
        return self.get_field_value(self.MULTILAYERPLATEPOOLIFSAMETYPE__FIELD_NAME.field_name)

    def set_NewConsumableDirName_field(self, value: Optional[str]):
        """
        Set data field with field name 'NewConsumableDirName' on this record model
        """
        self.set_field_value(self.NEWCONSUMABLEDIRNAME__FIELD_NAME.field_name, value)

    def get_NewConsumableDirName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NewConsumableDirName' from this record model
        """
        return self.get_field_value(self.NEWCONSUMABLEDIRNAME__FIELD_NAME.field_name)

    def set_NotificationUsers_field(self, value: Optional[str]):
        """
        Set data field with field name 'NotificationUsers' on this record model
        """
        self.set_field_value(self.NOTIFICATIONUSERS__FIELD_NAME.field_name, value)

    def get_NotificationUsers_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NotificationUsers' from this record model
        """
        return self.get_field_value(self.NOTIFICATIONUSERS__FIELD_NAME.field_name)

    def set_NotifyMaintTechnicians_field(self, value: Optional[bool]):
        """
        Set data field with field name 'NotifyMaintTechnicians' on this record model
        """
        self.set_field_value(self.NOTIFYMAINTTECHNICIANS__FIELD_NAME.field_name, value)

    def get_NotifyMaintTechnicians_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'NotifyMaintTechnicians' from this record model
        """
        return self.get_field_value(self.NOTIFYMAINTTECHNICIANS__FIELD_NAME.field_name)

    def set_OverrideGroups_field(self, value: Optional[str]):
        """
        Set data field with field name 'OverrideGroups' on this record model
        """
        self.set_field_value(self.OVERRIDEGROUPS__FIELD_NAME.field_name, value)

    def get_OverrideGroups_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OverrideGroups' from this record model
        """
        return self.get_field_value(self.OVERRIDEGROUPS__FIELD_NAME.field_name)

    def set_PlasmidDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlasmidDataType' on this record model
        """
        self.set_field_value(self.PLASMIDDATATYPE__FIELD_NAME.field_name, value)

    def get_PlasmidDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlasmidDataType' from this record model
        """
        return self.get_field_value(self.PLASMIDDATATYPE__FIELD_NAME.field_name)

    def set_PlateDesignerPrimaryTypes_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlateDesignerPrimaryTypes' on this record model
        """
        self.set_field_value(self.PLATEDESIGNERPRIMARYTYPES__FIELD_NAME.field_name, value)

    def get_PlateDesignerPrimaryTypes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlateDesignerPrimaryTypes' from this record model
        """
        return self.get_field_value(self.PLATEDESIGNERPRIMARYTYPES__FIELD_NAME.field_name)

    def set_PlateScanToMatch_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlateScanToMatch' on this record model
        """
        self.set_field_value(self.PLATESCANTOMATCH__FIELD_NAME.field_name, value)

    def get_PlateScanToMatch_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlateScanToMatch' from this record model
        """
        return self.get_field_value(self.PLATESCANTOMATCH__FIELD_NAME.field_name)

    def set_Port_field(self, value: Optional[int]):
        """
        Set data field with field name 'Port' on this record model
        """
        self.set_field_value(self.PORT__FIELD_NAME.field_name, value)

    def get_Port_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Port' from this record model
        """
        return self.get_field_value(self.PORT__FIELD_NAME.field_name)

    def set_PreNotificationInterval_field(self, value: Optional[int]):
        """
        Set data field with field name 'PreNotificationInterval' on this record model
        """
        self.set_field_value(self.PRENOTIFICATIONINTERVAL__FIELD_NAME.field_name, value)

    def get_PreNotificationInterval_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PreNotificationInterval' from this record model
        """
        return self.get_field_value(self.PRENOTIFICATIONINTERVAL__FIELD_NAME.field_name)

    def set_PrintConsumableBarcode_field(self, value: Optional[bool]):
        """
        Set data field with field name 'PrintConsumableBarcode' on this record model
        """
        self.set_field_value(self.PRINTCONSUMABLEBARCODE__FIELD_NAME.field_name, value)

    def get_PrintConsumableBarcode_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'PrintConsumableBarcode' from this record model
        """
        return self.get_field_value(self.PRINTCONSUMABLEBARCODE__FIELD_NAME.field_name)

    def set_QCMailingList_field(self, value: Optional[str]):
        """
        Set data field with field name 'QCMailingList' on this record model
        """
        self.set_field_value(self.QCMAILINGLIST__FIELD_NAME.field_name, value)

    def get_QCMailingList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'QCMailingList' from this record model
        """
        return self.get_field_value(self.QCMAILINGLIST__FIELD_NAME.field_name)

    def set_QuantityTracking_field(self, value: Optional[bool]):
        """
        Set data field with field name 'QuantityTracking' on this record model
        """
        self.set_field_value(self.QUANTITYTRACKING__FIELD_NAME.field_name, value)

    def get_QuantityTracking_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'QuantityTracking' from this record model
        """
        return self.get_field_value(self.QUANTITYTRACKING__FIELD_NAME.field_name)

    def set_ReagentLotScanToMatch_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentLotScanToMatch' on this record model
        """
        self.set_field_value(self.REAGENTLOTSCANTOMATCH__FIELD_NAME.field_name, value)

    def get_ReagentLotScanToMatch_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentLotScanToMatch' from this record model
        """
        return self.get_field_value(self.REAGENTLOTSCANTOMATCH__FIELD_NAME.field_name)

    def set_RecordReportAccessGroups_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecordReportAccessGroups' on this record model
        """
        self.set_field_value(self.RECORDREPORTACCESSGROUPS__FIELD_NAME.field_name, value)

    def get_RecordReportAccessGroups_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecordReportAccessGroups' from this record model
        """
        return self.get_field_value(self.RECORDREPORTACCESSGROUPS__FIELD_NAME.field_name)

    def set_RecordReportDataTypeList_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecordReportDataTypeList' on this record model
        """
        self.set_field_value(self.RECORDREPORTDATATYPELIST__FIELD_NAME.field_name, value)

    def get_RecordReportDataTypeList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecordReportDataTypeList' from this record model
        """
        return self.get_field_value(self.RECORDREPORTDATATYPELIST__FIELD_NAME.field_name)

    def set_RecordStorageEvents_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RecordStorageEvents' on this record model
        """
        self.set_field_value(self.RECORDSTORAGEEVENTS__FIELD_NAME.field_name, value)

    def get_RecordStorageEvents_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RecordStorageEvents' from this record model
        """
        return self.get_field_value(self.RECORDSTORAGEEVENTS__FIELD_NAME.field_name)

    def set_ReqPortalManifestFieldNames_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReqPortalManifestFieldNames' on this record model
        """
        self.set_field_value(self.REQPORTALMANIFESTFIELDNAMES__FIELD_NAME.field_name, value)

    def get_ReqPortalManifestFieldNames_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReqPortalManifestFieldNames' from this record model
        """
        return self.get_field_value(self.REQPORTALMANIFESTFIELDNAMES__FIELD_NAME.field_name)

    def set_RequireESignature_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RequireESignature' on this record model
        """
        self.set_field_value(self.REQUIREESIGNATURE__FIELD_NAME.field_name, value)

    def get_RequireESignature_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RequireESignature' from this record model
        """
        return self.get_field_value(self.REQUIREESIGNATURE__FIELD_NAME.field_name)

    def set_RestrictAccessByLocation_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RestrictAccessByLocation' on this record model
        """
        self.set_field_value(self.RESTRICTACCESSBYLOCATION__FIELD_NAME.field_name, value)

    def get_RestrictAccessByLocation_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RestrictAccessByLocation' from this record model
        """
        return self.get_field_value(self.RESTRICTACCESSBYLOCATION__FIELD_NAME.field_name)

    def set_ReviewerVisibleRoleType_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ReviewerVisibleRoleType' on this record model
        """
        self.set_field_value(self.REVIEWERVISIBLEROLETYPE__FIELD_NAME.field_name, value)

    def get_ReviewerVisibleRoleType_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ReviewerVisibleRoleType' from this record model
        """
        return self.get_field_value(self.REVIEWERVISIBLEROLETYPE__FIELD_NAME.field_name)

    def set_S3AccessKeyId_field(self, value: Optional[str]):
        """
        Set data field with field name 'S3AccessKeyId' on this record model
        """
        self.set_field_value(self.S3ACCESSKEYID__FIELD_NAME.field_name, value)

    def get_S3AccessKeyId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'S3AccessKeyId' from this record model
        """
        return self.get_field_value(self.S3ACCESSKEYID__FIELD_NAME.field_name)

    def set_S3SecretAcessKey_field(self, value: Optional[str]):
        """
        Set data field with field name 'S3SecretAcessKey' on this record model
        """
        self.set_field_value(self.S3SECRETACESSKEY__FIELD_NAME.field_name, value)

    def get_S3SecretAcessKey_field(self) -> Optional[str]:
        """
        Get data field value with field name 'S3SecretAcessKey' from this record model
        """
        return self.get_field_value(self.S3SECRETACESSKEY__FIELD_NAME.field_name)

    def set_SaasMaxNumOfSamplesPerTrans_field(self, value: Optional[int]):
        """
        Set data field with field name 'SaasMaxNumOfSamplesPerTrans' on this record model
        """
        self.set_field_value(self.SAASMAXNUMOFSAMPLESPERTRANS__FIELD_NAME.field_name, value)

    def get_SaasMaxNumOfSamplesPerTrans_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SaasMaxNumOfSamplesPerTrans' from this record model
        """
        return self.get_field_value(self.SAASMAXNUMOFSAMPLESPERTRANS__FIELD_NAME.field_name)

    def set_SaasMaxSamples_field(self, value: Optional[int]):
        """
        Set data field with field name 'SaasMaxSamples' on this record model
        """
        self.set_field_value(self.SAASMAXSAMPLES__FIELD_NAME.field_name, value)

    def get_SaasMaxSamples_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SaasMaxSamples' from this record model
        """
        return self.get_field_value(self.SAASMAXSAMPLES__FIELD_NAME.field_name)

    def set_SaasMode_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SaasMode' on this record model
        """
        self.set_field_value(self.SAASMODE__FIELD_NAME.field_name, value)

    def get_SaasMode_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SaasMode' from this record model
        """
        return self.get_field_value(self.SAASMODE__FIELD_NAME.field_name)

    def set_SampleReceivingEmails_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleReceivingEmails' on this record model
        """
        self.set_field_value(self.SAMPLERECEIVINGEMAILS__FIELD_NAME.field_name, value)

    def get_SampleReceivingEmails_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleReceivingEmails' from this record model
        """
        return self.get_field_value(self.SAMPLERECEIVINGEMAILS__FIELD_NAME.field_name)

    def set_SampleReceivingUserMenu_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleReceivingUserMenu' on this record model
        """
        self.set_field_value(self.SAMPLERECEIVINGUSERMENU__FIELD_NAME.field_name, value)

    def get_SampleReceivingUserMenu_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleReceivingUserMenu' from this record model
        """
        return self.get_field_value(self.SAMPLERECEIVINGUSERMENU__FIELD_NAME.field_name)

    def set_SampleScanToMatch_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleScanToMatch' on this record model
        """
        self.set_field_value(self.SAMPLESCANTOMATCH__FIELD_NAME.field_name, value)

    def get_SampleScanToMatch_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleScanToMatch' from this record model
        """
        return self.get_field_value(self.SAMPLESCANTOMATCH__FIELD_NAME.field_name)

    def set_SampleSheetPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleSheetPath' on this record model
        """
        self.set_field_value(self.SAMPLESHEETPATH__FIELD_NAME.field_name, value)

    def get_SampleSheetPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleSheetPath' from this record model
        """
        return self.get_field_value(self.SAMPLESHEETPATH__FIELD_NAME.field_name)

    def set_SampleTypeMaximumTemperature_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleTypeMaximumTemperature' on this record model
        """
        self.set_field_value(self.SAMPLETYPEMAXIMUMTEMPERATURE__FIELD_NAME.field_name, value)

    def get_SampleTypeMaximumTemperature_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleTypeMaximumTemperature' from this record model
        """
        return self.get_field_value(self.SAMPLETYPEMAXIMUMTEMPERATURE__FIELD_NAME.field_name)

    def set_SDMSRootPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'SDMSRootPath' on this record model
        """
        self.set_field_value(self.SDMSROOTPATH__FIELD_NAME.field_name, value)

    def get_SDMSRootPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SDMSRootPath' from this record model
        """
        return self.get_field_value(self.SDMSROOTPATH__FIELD_NAME.field_name)

    def set_SecureSocketLayer_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SecureSocketLayer' on this record model
        """
        self.set_field_value(self.SECURESOCKETLAYER__FIELD_NAME.field_name, value)

    def get_SecureSocketLayer_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SecureSocketLayer' from this record model
        """
        return self.get_field_value(self.SECURESOCKETLAYER__FIELD_NAME.field_name)

    def set_SMTPServer_field(self, value: Optional[str]):
        """
        Set data field with field name 'SMTPServer' on this record model
        """
        self.set_field_value(self.SMTPSERVER__FIELD_NAME.field_name, value)

    def get_SMTPServer_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SMTPServer' from this record model
        """
        return self.get_field_value(self.SMTPSERVER__FIELD_NAME.field_name)

    def set_SmtpUsername_field(self, value: Optional[str]):
        """
        Set data field with field name 'SmtpUsername' on this record model
        """
        self.set_field_value(self.SMTPUSERNAME__FIELD_NAME.field_name, value)

    def get_SmtpUsername_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SmtpUsername' from this record model
        """
        return self.get_field_value(self.SMTPUSERNAME__FIELD_NAME.field_name)

    def set_StorageUnitViewerFillByConfig_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitViewerFillByConfig' on this record model
        """
        self.set_field_value(self.STORAGEUNITVIEWERFILLBYCONFIG__FIELD_NAME.field_name, value)

    def get_StorageUnitViewerFillByConfig_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitViewerFillByConfig' from this record model
        """
        return self.get_field_value(self.STORAGEUNITVIEWERFILLBYCONFIG__FIELD_NAME.field_name)

    def set_SystemPassword_field(self, value: Optional[str]):
        """
        Set data field with field name 'SystemPassword' on this record model
        """
        self.set_field_value(self.SYSTEMPASSWORD__FIELD_NAME.field_name, value)

    def get_SystemPassword_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SystemPassword' from this record model
        """
        return self.get_field_value(self.SYSTEMPASSWORD__FIELD_NAME.field_name)

    def set_TemperatureEnforcement_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemperatureEnforcement' on this record model
        """
        self.set_field_value(self.TEMPERATUREENFORCEMENT__FIELD_NAME.field_name, value)

    def get_TemperatureEnforcement_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemperatureEnforcement' from this record model
        """
        return self.get_field_value(self.TEMPERATUREENFORCEMENT__FIELD_NAME.field_name)

    def set_TLSEnabled_field(self, value: Optional[bool]):
        """
        Set data field with field name 'TLSEnabled' on this record model
        """
        self.set_field_value(self.TLSENABLED__FIELD_NAME.field_name, value)

    def get_TLSEnabled_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'TLSEnabled' from this record model
        """
        return self.get_field_value(self.TLSENABLED__FIELD_NAME.field_name)

    def set_TLSRequired_field(self, value: Optional[bool]):
        """
        Set data field with field name 'TLSRequired' on this record model
        """
        self.set_field_value(self.TLSREQUIRED__FIELD_NAME.field_name, value)

    def get_TLSRequired_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'TLSRequired' from this record model
        """
        return self.get_field_value(self.TLSREQUIRED__FIELD_NAME.field_name)

    def set_UseRequestDefaultLayout_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UseRequestDefaultLayout' on this record model
        """
        self.set_field_value(self.USEREQUESTDEFAULTLAYOUT__FIELD_NAME.field_name, value)

    def get_UseRequestDefaultLayout_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UseRequestDefaultLayout' from this record model
        """
        return self.get_field_value(self.USEREQUESTDEFAULTLAYOUT__FIELD_NAME.field_name)

    def set_VerificationTypes_field(self, value: Optional[str]):
        """
        Set data field with field name 'VerificationTypes' on this record model
        """
        self.set_field_value(self.VERIFICATIONTYPES__FIELD_NAME.field_name, value)

    def get_VerificationTypes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VerificationTypes' from this record model
        """
        return self.get_field_value(self.VERIFICATIONTYPES__FIELD_NAME.field_name)

    def set_ViiPlateSize_field(self, value: Optional[str]):
        """
        Set data field with field name 'ViiPlateSize' on this record model
        """
        self.set_field_value(self.VIIPLATESIZE__FIELD_NAME.field_name, value)

    def get_ViiPlateSize_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ViiPlateSize' from this record model
        """
        return self.get_field_value(self.VIIPLATESIZE__FIELD_NAME.field_name)

    def set_WitnessVisibleRoleType_field(self, value: Optional[bool]):
        """
        Set data field with field name 'WitnessVisibleRoleType' on this record model
        """
        self.set_field_value(self.WITNESSVISIBLEROLETYPE__FIELD_NAME.field_name, value)

    def get_WitnessVisibleRoleType_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'WitnessVisibleRoleType' from this record model
        """
        return self.get_field_value(self.WITNESSVISIBLEROLETYPE__FIELD_NAME.field_name)

    def set_WriteQCInputFileToUser_field(self, value: Optional[bool]):
        """
        Set data field with field name 'WriteQCInputFileToUser' on this record model
        """
        self.set_field_value(self.WRITEQCINPUTFILETOUSER__FIELD_NAME.field_name, value)

    def get_WriteQCInputFileToUser_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'WriteQCInputFileToUser' from this record model
        """
        return self.get_field_value(self.WRITEQCINPUTFILETOUSER__FIELD_NAME.field_name)


class ExemplarLabNotebookPDFModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ExemplarLabNotebookPDF
    Data Type Display Name: Sapio Lab Notebook PDF (Sapio Lab Notebook PDFs)
    Fields: FilePath, VeloxCurrentVersion
    This data type is used to store the latest PDF file that has been generated from a given notebook.
    """
    DATA_TYPE_NAME: str = 'ExemplarLabNotebookPDF'
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class ExemplarSDMSFileModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ExemplarSDMSFile
    Data Type Display Name: SDMS File (SDMS Files)
    Fields: FileCreationDate, FileHash, FileLastModifiedDate, FilePath, FileSize, FileSourcePath, InstrumentType, VeloxCurrentVersion
    These are potentially very large files that will be stored as SDMS file. They will be retrieved through streamed download.
    """
    DATA_TYPE_NAME: str = 'ExemplarSDMSFile'
    FILECREATIONDATE__FIELD_NAME: WrapperField = WrapperField("FileCreationDate", FieldType.DATE)
    FILEHASH__FIELD_NAME: WrapperField = WrapperField("FileHash", FieldType.STRING)
    FILELASTMODIFIEDDATE__FIELD_NAME: WrapperField = WrapperField("FileLastModifiedDate", FieldType.DATE)
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    FILESIZE__FIELD_NAME: WrapperField = WrapperField("FileSize", FieldType.LONG)
    FILESOURCEPATH__FIELD_NAME: WrapperField = WrapperField("FileSourcePath", FieldType.STRING)
    INSTRUMENTTYPE__FIELD_NAME: WrapperField = WrapperField("InstrumentType", FieldType.STRING)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FileCreationDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'FileCreationDate' on this record model
        """
        self.set_field_value(self.FILECREATIONDATE__FIELD_NAME.field_name, value)

    def get_FileCreationDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FileCreationDate' from this record model
        """
        return self.get_field_value(self.FILECREATIONDATE__FIELD_NAME.field_name)

    def set_FileHash_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileHash' on this record model
        """
        self.set_field_value(self.FILEHASH__FIELD_NAME.field_name, value)

    def get_FileHash_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileHash' from this record model
        """
        return self.get_field_value(self.FILEHASH__FIELD_NAME.field_name)

    def set_FileLastModifiedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'FileLastModifiedDate' on this record model
        """
        self.set_field_value(self.FILELASTMODIFIEDDATE__FIELD_NAME.field_name, value)

    def get_FileLastModifiedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FileLastModifiedDate' from this record model
        """
        return self.get_field_value(self.FILELASTMODIFIEDDATE__FIELD_NAME.field_name)

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_FileSize_field(self, value: Optional[int]):
        """
        Set data field with field name 'FileSize' on this record model
        """
        self.set_field_value(self.FILESIZE__FIELD_NAME.field_name, value)

    def get_FileSize_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FileSize' from this record model
        """
        return self.get_field_value(self.FILESIZE__FIELD_NAME.field_name)

    def set_FileSourcePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileSourcePath' on this record model
        """
        self.set_field_value(self.FILESOURCEPATH__FIELD_NAME.field_name, value)

    def get_FileSourcePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileSourcePath' from this record model
        """
        return self.get_field_value(self.FILESOURCEPATH__FIELD_NAME.field_name)

    def set_InstrumentType_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentType' on this record model
        """
        self.set_field_value(self.INSTRUMENTTYPE__FIELD_NAME.field_name, value)

    def get_InstrumentType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentType' from this record model
        """
        return self.get_field_value(self.INSTRUMENTTYPE__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class ExperimentGroupModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ExperimentGroup
    Data Type Display Name: Experiment Group (Experiment Groups)
    Fields: GroupMonth, GroupYear
    """
    DATA_TYPE_NAME: str = 'ExperimentGroup'
    GROUPMONTH__FIELD_NAME: WrapperField = WrapperField("GroupMonth", FieldType.PICKLIST)
    GROUPYEAR__FIELD_NAME: WrapperField = WrapperField("GroupYear", FieldType.SHORT)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_GroupMonth_field(self, value: Optional[str]):
        """
        Set data field with field name 'GroupMonth' on this record model
        """
        self.set_field_value(self.GROUPMONTH__FIELD_NAME.field_name, value)

    def get_GroupMonth_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GroupMonth' from this record model
        """
        return self.get_field_value(self.GROUPMONTH__FIELD_NAME.field_name)

    def set_GroupYear_field(self, value: Optional[int]):
        """
        Set data field with field name 'GroupYear' on this record model
        """
        self.set_field_value(self.GROUPYEAR__FIELD_NAME.field_name, value)

    def get_GroupYear_field(self) -> Optional[int]:
        """
        Get data field value with field name 'GroupYear' from this record model
        """
        return self.get_field_value(self.GROUPYEAR__FIELD_NAME.field_name)


class ExpoentialDecayModelModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ExpoentialDecayModel
    Data Type Display Name: Exponential Decay Model (Exponential Decay Models)
    Fields: c, d, e, EntryName, Formula, MultiParentLink207, RSE, RSEDOF, RSquared, SeriesName, SourceEntryId
    Exponential Decay follows this formula:

Y = c + (d-c) exp(-x/e)
    """
    DATA_TYPE_NAME: str = 'ExpoentialDecayModel'
    C__FIELD_NAME: WrapperField = WrapperField("c", FieldType.DOUBLE)
    D__FIELD_NAME: WrapperField = WrapperField("d", FieldType.DOUBLE)
    E__FIELD_NAME: WrapperField = WrapperField("e", FieldType.DOUBLE)
    ENTRYNAME__FIELD_NAME: WrapperField = WrapperField("EntryName", FieldType.STRING)
    FORMULA__FIELD_NAME: WrapperField = WrapperField("Formula", FieldType.STRING)
    MULTIPARENTLINK207__FIELD_NAME: WrapperField = WrapperField("MultiParentLink207", FieldType.MULTIPARENTLINK)
    RSE__FIELD_NAME: WrapperField = WrapperField("RSE", FieldType.DOUBLE)
    RSEDOF__FIELD_NAME: WrapperField = WrapperField("RSEDOF", FieldType.DOUBLE)
    RSQUARED__FIELD_NAME: WrapperField = WrapperField("RSquared", FieldType.DOUBLE)
    SERIESNAME__FIELD_NAME: WrapperField = WrapperField("SeriesName", FieldType.STRING)
    SOURCEENTRYID__FIELD_NAME: WrapperField = WrapperField("SourceEntryId", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_c_field(self, value: Optional[float]):
        """
        Set data field with field name 'c' on this record model
        """
        self.set_field_value(self.C__FIELD_NAME.field_name, value)

    def get_c_field(self) -> Optional[float]:
        """
        Get data field value with field name 'c' from this record model
        """
        return self.get_field_value(self.C__FIELD_NAME.field_name)

    def set_d_field(self, value: Optional[float]):
        """
        Set data field with field name 'd' on this record model
        """
        self.set_field_value(self.D__FIELD_NAME.field_name, value)

    def get_d_field(self) -> Optional[float]:
        """
        Get data field value with field name 'd' from this record model
        """
        return self.get_field_value(self.D__FIELD_NAME.field_name)

    def set_e_field(self, value: Optional[float]):
        """
        Set data field with field name 'e' on this record model
        """
        self.set_field_value(self.E__FIELD_NAME.field_name, value)

    def get_e_field(self) -> Optional[float]:
        """
        Get data field value with field name 'e' from this record model
        """
        return self.get_field_value(self.E__FIELD_NAME.field_name)

    def set_EntryName_field(self, value: Optional[str]):
        """
        Set data field with field name 'EntryName' on this record model
        """
        self.set_field_value(self.ENTRYNAME__FIELD_NAME.field_name, value)

    def get_EntryName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EntryName' from this record model
        """
        return self.get_field_value(self.ENTRYNAME__FIELD_NAME.field_name)

    def set_Formula_field(self, value: Optional[str]):
        """
        Set data field with field name 'Formula' on this record model
        """
        self.set_field_value(self.FORMULA__FIELD_NAME.field_name, value)

    def get_Formula_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Formula' from this record model
        """
        return self.get_field_value(self.FORMULA__FIELD_NAME.field_name)

    def set_RSE_field(self, value: Optional[float]):
        """
        Set data field with field name 'RSE' on this record model
        """
        self.set_field_value(self.RSE__FIELD_NAME.field_name, value)

    def get_RSE_field(self) -> Optional[float]:
        """
        Get data field value with field name 'RSE' from this record model
        """
        return self.get_field_value(self.RSE__FIELD_NAME.field_name)

    def set_RSEDOF_field(self, value: Optional[float]):
        """
        Set data field with field name 'RSEDOF' on this record model
        """
        self.set_field_value(self.RSEDOF__FIELD_NAME.field_name, value)

    def get_RSEDOF_field(self) -> Optional[float]:
        """
        Get data field value with field name 'RSEDOF' from this record model
        """
        return self.get_field_value(self.RSEDOF__FIELD_NAME.field_name)

    def set_RSquared_field(self, value: Optional[float]):
        """
        Set data field with field name 'RSquared' on this record model
        """
        self.set_field_value(self.RSQUARED__FIELD_NAME.field_name, value)

    def get_RSquared_field(self) -> Optional[float]:
        """
        Get data field value with field name 'RSquared' from this record model
        """
        return self.get_field_value(self.RSQUARED__FIELD_NAME.field_name)

    def set_SeriesName_field(self, value: Optional[str]):
        """
        Set data field with field name 'SeriesName' on this record model
        """
        self.set_field_value(self.SERIESNAME__FIELD_NAME.field_name, value)

    def get_SeriesName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SeriesName' from this record model
        """
        return self.get_field_value(self.SERIESNAME__FIELD_NAME.field_name)

    def set_SourceEntryId_field(self, value: Optional[int]):
        """
        Set data field with field name 'SourceEntryId' on this record model
        """
        self.set_field_value(self.SOURCEENTRYID__FIELD_NAME.field_name, value)

    def get_SourceEntryId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SourceEntryId' from this record model
        """
        return self.get_field_value(self.SOURCEENTRYID__FIELD_NAME.field_name)


class FailedSampleDetailsModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FailedSampleDetails
    Data Type Display Name: Failure Details (Failure Details)
    Fields: ActiveTaskName, ActiveWorkflowName, FailureStatus, OtherSampleId, SampleId
    """
    DATA_TYPE_NAME: str = 'FailedSampleDetails'
    ACTIVETASKNAME__FIELD_NAME: WrapperField = WrapperField("ActiveTaskName", FieldType.STRING)
    ACTIVEWORKFLOWNAME__FIELD_NAME: WrapperField = WrapperField("ActiveWorkflowName", FieldType.STRING)
    FAILURESTATUS__FIELD_NAME: WrapperField = WrapperField("FailureStatus", FieldType.PICKLIST)
    OTHERSAMPLEID__FIELD_NAME: WrapperField = WrapperField("OtherSampleId", FieldType.STRING)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActiveTaskName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ActiveTaskName' on this record model
        """
        self.set_field_value(self.ACTIVETASKNAME__FIELD_NAME.field_name, value)

    def get_ActiveTaskName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ActiveTaskName' from this record model
        """
        return self.get_field_value(self.ACTIVETASKNAME__FIELD_NAME.field_name)

    def set_ActiveWorkflowName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ActiveWorkflowName' on this record model
        """
        self.set_field_value(self.ACTIVEWORKFLOWNAME__FIELD_NAME.field_name, value)

    def get_ActiveWorkflowName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ActiveWorkflowName' from this record model
        """
        return self.get_field_value(self.ACTIVEWORKFLOWNAME__FIELD_NAME.field_name)

    def set_FailureStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'FailureStatus' on this record model
        """
        self.set_field_value(self.FAILURESTATUS__FIELD_NAME.field_name, value)

    def get_FailureStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FailureStatus' from this record model
        """
        return self.get_field_value(self.FAILURESTATUS__FIELD_NAME.field_name)

    def set_OtherSampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'OtherSampleId' on this record model
        """
        self.set_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name, value)

    def get_OtherSampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OtherSampleId' from this record model
        """
        return self.get_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)


class FCSFileModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FCSFile
    Data Type Display Name: Flow Cytometry Standard File (Flow Cytometry Standard Files)
    Fields: FilePath, IsDataComplete, IsMetadataLoaded, IsTopLevel, PercentCellsToParentLevel, PercentCellsToTopLevel, RootFCSRecordId, TotalNumberOfCells, VeloxCurrentVersion
    """
    DATA_TYPE_NAME: str = 'FCSFile'
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    ISDATACOMPLETE__FIELD_NAME: WrapperField = WrapperField("IsDataComplete", FieldType.BOOLEAN)
    ISMETADATALOADED__FIELD_NAME: WrapperField = WrapperField("IsMetadataLoaded", FieldType.BOOLEAN)
    ISTOPLEVEL__FIELD_NAME: WrapperField = WrapperField("IsTopLevel", FieldType.BOOLEAN)
    PERCENTCELLSTOPARENTLEVEL__FIELD_NAME: WrapperField = WrapperField("PercentCellsToParentLevel", FieldType.DOUBLE)
    PERCENTCELLSTOTOPLEVEL__FIELD_NAME: WrapperField = WrapperField("PercentCellsToTopLevel", FieldType.DOUBLE)
    ROOTFCSRECORDID__FIELD_NAME: WrapperField = WrapperField("RootFCSRecordId", FieldType.LONG)
    TOTALNUMBEROFCELLS__FIELD_NAME: WrapperField = WrapperField("TotalNumberOfCells", FieldType.LONG)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_IsDataComplete_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsDataComplete' on this record model
        """
        self.set_field_value(self.ISDATACOMPLETE__FIELD_NAME.field_name, value)

    def get_IsDataComplete_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsDataComplete' from this record model
        """
        return self.get_field_value(self.ISDATACOMPLETE__FIELD_NAME.field_name)

    def set_IsMetadataLoaded_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsMetadataLoaded' on this record model
        """
        self.set_field_value(self.ISMETADATALOADED__FIELD_NAME.field_name, value)

    def get_IsMetadataLoaded_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsMetadataLoaded' from this record model
        """
        return self.get_field_value(self.ISMETADATALOADED__FIELD_NAME.field_name)

    def set_IsTopLevel_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsTopLevel' on this record model
        """
        self.set_field_value(self.ISTOPLEVEL__FIELD_NAME.field_name, value)

    def get_IsTopLevel_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsTopLevel' from this record model
        """
        return self.get_field_value(self.ISTOPLEVEL__FIELD_NAME.field_name)

    def set_PercentCellsToParentLevel_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentCellsToParentLevel' on this record model
        """
        self.set_field_value(self.PERCENTCELLSTOPARENTLEVEL__FIELD_NAME.field_name, value)

    def get_PercentCellsToParentLevel_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentCellsToParentLevel' from this record model
        """
        return self.get_field_value(self.PERCENTCELLSTOPARENTLEVEL__FIELD_NAME.field_name)

    def set_PercentCellsToTopLevel_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentCellsToTopLevel' on this record model
        """
        self.set_field_value(self.PERCENTCELLSTOTOPLEVEL__FIELD_NAME.field_name, value)

    def get_PercentCellsToTopLevel_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentCellsToTopLevel' from this record model
        """
        return self.get_field_value(self.PERCENTCELLSTOTOPLEVEL__FIELD_NAME.field_name)

    def set_RootFCSRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'RootFCSRecordId' on this record model
        """
        self.set_field_value(self.ROOTFCSRECORDID__FIELD_NAME.field_name, value)

    def get_RootFCSRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RootFCSRecordId' from this record model
        """
        return self.get_field_value(self.ROOTFCSRECORDID__FIELD_NAME.field_name)

    def set_TotalNumberOfCells_field(self, value: Optional[int]):
        """
        Set data field with field name 'TotalNumberOfCells' on this record model
        """
        self.set_field_value(self.TOTALNUMBEROFCELLS__FIELD_NAME.field_name, value)

    def get_TotalNumberOfCells_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TotalNumberOfCells' from this record model
        """
        return self.get_field_value(self.TOTALNUMBEROFCELLS__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class FCSStatisticModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FCSStatistic
    Data Type Display Name: Flow Cytometry Statistic (Flow Cytometry Statistic)
    Fields: ChannelName, NumericValue, StatName
    A statistic record for FCS file, usually for a specific channel so they are not suited directly added to the FCSFile record.
    """
    DATA_TYPE_NAME: str = 'FCSStatistic'
    CHANNELNAME__FIELD_NAME: WrapperField = WrapperField("ChannelName", FieldType.STRING)
    NUMERICVALUE__FIELD_NAME: WrapperField = WrapperField("NumericValue", FieldType.DOUBLE)
    STATNAME__FIELD_NAME: WrapperField = WrapperField("StatName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ChannelName' on this record model
        """
        self.set_field_value(self.CHANNELNAME__FIELD_NAME.field_name, value)

    def get_ChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ChannelName' from this record model
        """
        return self.get_field_value(self.CHANNELNAME__FIELD_NAME.field_name)

    def set_NumericValue_field(self, value: Optional[float]):
        """
        Set data field with field name 'NumericValue' on this record model
        """
        self.set_field_value(self.NUMERICVALUE__FIELD_NAME.field_name, value)

    def get_NumericValue_field(self) -> Optional[float]:
        """
        Get data field value with field name 'NumericValue' from this record model
        """
        return self.get_field_value(self.NUMERICVALUE__FIELD_NAME.field_name)

    def set_StatName_field(self, value: Optional[str]):
        """
        Set data field with field name 'StatName' on this record model
        """
        self.set_field_value(self.STATNAME__FIELD_NAME.field_name, value)

    def get_StatName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StatName' from this record model
        """
        return self.get_field_value(self.STATNAME__FIELD_NAME.field_name)


class FileBridgeConnectionModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FileBridgeConnection
    Data Type Display Name: File Bridge Connection (File Bridge Connections)
    Fields: AesKey, AgentRoot, AuthToken, ConnectionName, ProxyHost, ProxyPort
    This data type describes the configuration of a File Bridge Connection to be used by Exemplar.
    """
    DATA_TYPE_NAME: str = 'FileBridgeConnection'
    AESKEY__FIELD_NAME: WrapperField = WrapperField("AesKey", FieldType.STRING)
    AGENTROOT__FIELD_NAME: WrapperField = WrapperField("AgentRoot", FieldType.STRING)
    AUTHTOKEN__FIELD_NAME: WrapperField = WrapperField("AuthToken", FieldType.STRING)
    CONNECTIONNAME__FIELD_NAME: WrapperField = WrapperField("ConnectionName", FieldType.STRING)
    PROXYHOST__FIELD_NAME: WrapperField = WrapperField("ProxyHost", FieldType.STRING)
    PROXYPORT__FIELD_NAME: WrapperField = WrapperField("ProxyPort", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AesKey_field(self, value: Optional[str]):
        """
        Set data field with field name 'AesKey' on this record model
        """
        self.set_field_value(self.AESKEY__FIELD_NAME.field_name, value)

    def get_AesKey_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AesKey' from this record model
        """
        return self.get_field_value(self.AESKEY__FIELD_NAME.field_name)

    def set_AgentRoot_field(self, value: Optional[str]):
        """
        Set data field with field name 'AgentRoot' on this record model
        """
        self.set_field_value(self.AGENTROOT__FIELD_NAME.field_name, value)

    def get_AgentRoot_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AgentRoot' from this record model
        """
        return self.get_field_value(self.AGENTROOT__FIELD_NAME.field_name)

    def set_AuthToken_field(self, value: Optional[str]):
        """
        Set data field with field name 'AuthToken' on this record model
        """
        self.set_field_value(self.AUTHTOKEN__FIELD_NAME.field_name, value)

    def get_AuthToken_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AuthToken' from this record model
        """
        return self.get_field_value(self.AUTHTOKEN__FIELD_NAME.field_name)

    def set_ConnectionName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConnectionName' on this record model
        """
        self.set_field_value(self.CONNECTIONNAME__FIELD_NAME.field_name, value)

    def get_ConnectionName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConnectionName' from this record model
        """
        return self.get_field_value(self.CONNECTIONNAME__FIELD_NAME.field_name)

    def set_ProxyHost_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProxyHost' on this record model
        """
        self.set_field_value(self.PROXYHOST__FIELD_NAME.field_name, value)

    def get_ProxyHost_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProxyHost' from this record model
        """
        return self.get_field_value(self.PROXYHOST__FIELD_NAME.field_name)

    def set_ProxyPort_field(self, value: Optional[int]):
        """
        Set data field with field name 'ProxyPort' on this record model
        """
        self.set_field_value(self.PROXYPORT__FIELD_NAME.field_name, value)

    def get_ProxyPort_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ProxyPort' from this record model
        """
        return self.get_field_value(self.PROXYPORT__FIELD_NAME.field_name)


class FlowAIRunResultModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowAIRunResult
    Data Type Display Name: FlowAI Run result (FlowAI Run Results)
    Fields: alphaFR, decompFR, FilePath, max_cptFS, outlier_binsFS, pen_valueFS, second_fractionFR, sideFM, VeloxCurrentVersion
    """
    DATA_TYPE_NAME: str = 'FlowAIRunResult'
    ALPHAFR__FIELD_NAME: WrapperField = WrapperField("alphaFR", FieldType.DOUBLE)
    DECOMPFR__FIELD_NAME: WrapperField = WrapperField("decompFR", FieldType.BOOLEAN)
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    MAX_CPTFS__FIELD_NAME: WrapperField = WrapperField("max_cptFS", FieldType.INTEGER)
    OUTLIER_BINSFS__FIELD_NAME: WrapperField = WrapperField("outlier_binsFS", FieldType.BOOLEAN)
    PEN_VALUEFS__FIELD_NAME: WrapperField = WrapperField("pen_valueFS", FieldType.STRING)
    SECOND_FRACTIONFR__FIELD_NAME: WrapperField = WrapperField("second_fractionFR", FieldType.DOUBLE)
    SIDEFM__FIELD_NAME: WrapperField = WrapperField("sideFM", FieldType.PICKLIST)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_alphaFR_field(self, value: Optional[float]):
        """
        Set data field with field name 'alphaFR' on this record model
        """
        self.set_field_value(self.ALPHAFR__FIELD_NAME.field_name, value)

    def get_alphaFR_field(self) -> Optional[float]:
        """
        Get data field value with field name 'alphaFR' from this record model
        """
        return self.get_field_value(self.ALPHAFR__FIELD_NAME.field_name)

    def set_decompFR_field(self, value: Optional[bool]):
        """
        Set data field with field name 'decompFR' on this record model
        """
        self.set_field_value(self.DECOMPFR__FIELD_NAME.field_name, value)

    def get_decompFR_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'decompFR' from this record model
        """
        return self.get_field_value(self.DECOMPFR__FIELD_NAME.field_name)

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_max_cptFS_field(self, value: Optional[int]):
        """
        Set data field with field name 'max_cptFS' on this record model
        """
        self.set_field_value(self.MAX_CPTFS__FIELD_NAME.field_name, value)

    def get_max_cptFS_field(self) -> Optional[int]:
        """
        Get data field value with field name 'max_cptFS' from this record model
        """
        return self.get_field_value(self.MAX_CPTFS__FIELD_NAME.field_name)

    def set_outlier_binsFS_field(self, value: Optional[bool]):
        """
        Set data field with field name 'outlier_binsFS' on this record model
        """
        self.set_field_value(self.OUTLIER_BINSFS__FIELD_NAME.field_name, value)

    def get_outlier_binsFS_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'outlier_binsFS' from this record model
        """
        return self.get_field_value(self.OUTLIER_BINSFS__FIELD_NAME.field_name)

    def set_pen_valueFS_field(self, value: Optional[str]):
        """
        Set data field with field name 'pen_valueFS' on this record model
        """
        self.set_field_value(self.PEN_VALUEFS__FIELD_NAME.field_name, value)

    def get_pen_valueFS_field(self) -> Optional[str]:
        """
        Get data field value with field name 'pen_valueFS' from this record model
        """
        return self.get_field_value(self.PEN_VALUEFS__FIELD_NAME.field_name)

    def set_second_fractionFR_field(self, value: Optional[float]):
        """
        Set data field with field name 'second_fractionFR' on this record model
        """
        self.set_field_value(self.SECOND_FRACTIONFR__FIELD_NAME.field_name, value)

    def get_second_fractionFR_field(self) -> Optional[float]:
        """
        Get data field value with field name 'second_fractionFR' from this record model
        """
        return self.get_field_value(self.SECOND_FRACTIONFR__FIELD_NAME.field_name)

    def set_sideFM_field(self, value: Optional[str]):
        """
        Set data field with field name 'sideFM' on this record model
        """
        self.set_field_value(self.SIDEFM__FIELD_NAME.field_name, value)

    def get_sideFM_field(self) -> Optional[str]:
        """
        Get data field value with field name 'sideFM' from this record model
        """
        return self.get_field_value(self.SIDEFM__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class FlowCellModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowCell
    Data Type Display Name: Flow Cell (Flow Cells)
    Fields: ColPosition, FlowcellId, RowPosition, StorageLocationBarcode, StorageUnitPath
    """
    DATA_TYPE_NAME: str = 'FlowCell'
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    FLOWCELLID__FIELD_NAME: WrapperField = WrapperField("FlowcellId", FieldType.STRING)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    STORAGELOCATIONBARCODE__FIELD_NAME: WrapperField = WrapperField("StorageLocationBarcode", FieldType.SELECTION)
    STORAGEUNITPATH__FIELD_NAME: WrapperField = WrapperField("StorageUnitPath", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_FlowcellId_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowcellId' on this record model
        """
        self.set_field_value(self.FLOWCELLID__FIELD_NAME.field_name, value)

    def get_FlowcellId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowcellId' from this record model
        """
        return self.get_field_value(self.FLOWCELLID__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_StorageLocationBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageLocationBarcode' on this record model
        """
        self.set_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name, value)

    def get_StorageLocationBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageLocationBarcode' from this record model
        """
        return self.get_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name)

    def set_StorageUnitPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitPath' on this record model
        """
        self.set_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name, value)

    def get_StorageUnitPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitPath' from this record model
        """
        return self.get_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name)


class FlowCellLaneModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowCellLane
    Data Type Display Name: Flow Cell Lane (Flow Cell Lanes)
    Fields: ExpRecId, FlowcellId, LaneNum, MultiParentLink207
    """
    DATA_TYPE_NAME: str = 'FlowCellLane'
    EXPRECID__FIELD_NAME: WrapperField = WrapperField("ExpRecId", FieldType.LONG)
    FLOWCELLID__FIELD_NAME: WrapperField = WrapperField("FlowcellId", FieldType.STRING)
    LANENUM__FIELD_NAME: WrapperField = WrapperField("LaneNum", FieldType.LONG)
    MULTIPARENTLINK207__FIELD_NAME: WrapperField = WrapperField("MultiParentLink207", FieldType.MULTIPARENTLINK)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ExpRecId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ExpRecId' on this record model
        """
        self.set_field_value(self.EXPRECID__FIELD_NAME.field_name, value)

    def get_ExpRecId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ExpRecId' from this record model
        """
        return self.get_field_value(self.EXPRECID__FIELD_NAME.field_name)

    def set_FlowcellId_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowcellId' on this record model
        """
        self.set_field_value(self.FLOWCELLID__FIELD_NAME.field_name, value)

    def get_FlowcellId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowcellId' from this record model
        """
        return self.get_field_value(self.FLOWCELLID__FIELD_NAME.field_name)

    def set_LaneNum_field(self, value: Optional[int]):
        """
        Set data field with field name 'LaneNum' on this record model
        """
        self.set_field_value(self.LANENUM__FIELD_NAME.field_name, value)

    def get_LaneNum_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LaneNum' from this record model
        """
        return self.get_field_value(self.LANENUM__FIELD_NAME.field_name)


class FlowClustClusterModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowClustCluster
    Data Type Display Name: FlowClust Cluster (FlowClust Clusters)
    Fields: ClusterNum, ColorHTML, ColorName, UserAnnotation
    """
    DATA_TYPE_NAME: str = 'FlowClustCluster'
    CLUSTERNUM__FIELD_NAME: WrapperField = WrapperField("ClusterNum", FieldType.STRING)
    COLORHTML__FIELD_NAME: WrapperField = WrapperField("ColorHTML", FieldType.STRING)
    COLORNAME__FIELD_NAME: WrapperField = WrapperField("ColorName", FieldType.STRING)
    USERANNOTATION__FIELD_NAME: WrapperField = WrapperField("UserAnnotation", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ClusterNum_field(self, value: Optional[str]):
        """
        Set data field with field name 'ClusterNum' on this record model
        """
        self.set_field_value(self.CLUSTERNUM__FIELD_NAME.field_name, value)

    def get_ClusterNum_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ClusterNum' from this record model
        """
        return self.get_field_value(self.CLUSTERNUM__FIELD_NAME.field_name)

    def set_ColorHTML_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColorHTML' on this record model
        """
        self.set_field_value(self.COLORHTML__FIELD_NAME.field_name, value)

    def get_ColorHTML_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColorHTML' from this record model
        """
        return self.get_field_value(self.COLORHTML__FIELD_NAME.field_name)

    def set_ColorName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColorName' on this record model
        """
        self.set_field_value(self.COLORNAME__FIELD_NAME.field_name, value)

    def get_ColorName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColorName' from this record model
        """
        return self.get_field_value(self.COLORNAME__FIELD_NAME.field_name)

    def set_UserAnnotation_field(self, value: Optional[str]):
        """
        Set data field with field name 'UserAnnotation' on this record model
        """
        self.set_field_value(self.USERANNOTATION__FIELD_NAME.field_name, value)

    def get_UserAnnotation_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UserAnnotation' from this record model
        """
        return self.get_field_value(self.USERANNOTATION__FIELD_NAME.field_name)


class FlowClustConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowClustConfig
    Data Type Display Name: FlowClust Config (FlowClust Configs)
    Fields: BInit, ChannelConfigJSON, ClusterGroupName, criterion, FilePath, IsDataComplete, lam, LLevel, maxcount, MaxEMIterations, mincount, nu, nuest, NumberOfClusters, randomStart, seed, tol, tolInit, trans, VeloxCurrentVersion, zcutoff
    Sets up a FlowClust clustering package configurations.
    """
    DATA_TYPE_NAME: str = 'FlowClustConfig'
    BINIT__FIELD_NAME: WrapperField = WrapperField("BInit", FieldType.INTEGER)
    CHANNELCONFIGJSON__FIELD_NAME: WrapperField = WrapperField("ChannelConfigJSON", FieldType.STRING)
    CLUSTERGROUPNAME__FIELD_NAME: WrapperField = WrapperField("ClusterGroupName", FieldType.STRING)
    CRITERION__FIELD_NAME: WrapperField = WrapperField("criterion", FieldType.PICKLIST)
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    ISDATACOMPLETE__FIELD_NAME: WrapperField = WrapperField("IsDataComplete", FieldType.BOOLEAN)
    LAM__FIELD_NAME: WrapperField = WrapperField("lam", FieldType.DOUBLE)
    LLEVEL__FIELD_NAME: WrapperField = WrapperField("LLevel", FieldType.DOUBLE)
    MAXCOUNT__FIELD_NAME: WrapperField = WrapperField("maxcount", FieldType.INTEGER)
    MAXEMITERATIONS__FIELD_NAME: WrapperField = WrapperField("MaxEMIterations", FieldType.INTEGER)
    MINCOUNT__FIELD_NAME: WrapperField = WrapperField("mincount", FieldType.INTEGER)
    NU__FIELD_NAME: WrapperField = WrapperField("nu", FieldType.INTEGER)
    NUEST__FIELD_NAME: WrapperField = WrapperField("nuest", FieldType.PICKLIST)
    NUMBEROFCLUSTERS__FIELD_NAME: WrapperField = WrapperField("NumberOfClusters", FieldType.INTEGER)
    RANDOMSTART__FIELD_NAME: WrapperField = WrapperField("randomStart", FieldType.INTEGER)
    SEED__FIELD_NAME: WrapperField = WrapperField("seed", FieldType.INTEGER)
    TOL__FIELD_NAME: WrapperField = WrapperField("tol", FieldType.DOUBLE)
    TOLINIT__FIELD_NAME: WrapperField = WrapperField("tolInit", FieldType.DOUBLE)
    TRANS__FIELD_NAME: WrapperField = WrapperField("trans", FieldType.PICKLIST)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)
    ZCUTOFF__FIELD_NAME: WrapperField = WrapperField("zcutoff", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_BInit_field(self, value: Optional[int]):
        """
        Set data field with field name 'BInit' on this record model
        """
        self.set_field_value(self.BINIT__FIELD_NAME.field_name, value)

    def get_BInit_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BInit' from this record model
        """
        return self.get_field_value(self.BINIT__FIELD_NAME.field_name)

    def set_ChannelConfigJSON_field(self, value: Optional[str]):
        """
        Set data field with field name 'ChannelConfigJSON' on this record model
        """
        self.set_field_value(self.CHANNELCONFIGJSON__FIELD_NAME.field_name, value)

    def get_ChannelConfigJSON_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ChannelConfigJSON' from this record model
        """
        return self.get_field_value(self.CHANNELCONFIGJSON__FIELD_NAME.field_name)

    def set_ClusterGroupName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ClusterGroupName' on this record model
        """
        self.set_field_value(self.CLUSTERGROUPNAME__FIELD_NAME.field_name, value)

    def get_ClusterGroupName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ClusterGroupName' from this record model
        """
        return self.get_field_value(self.CLUSTERGROUPNAME__FIELD_NAME.field_name)

    def set_criterion_field(self, value: Optional[str]):
        """
        Set data field with field name 'criterion' on this record model
        """
        self.set_field_value(self.CRITERION__FIELD_NAME.field_name, value)

    def get_criterion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'criterion' from this record model
        """
        return self.get_field_value(self.CRITERION__FIELD_NAME.field_name)

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_IsDataComplete_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsDataComplete' on this record model
        """
        self.set_field_value(self.ISDATACOMPLETE__FIELD_NAME.field_name, value)

    def get_IsDataComplete_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsDataComplete' from this record model
        """
        return self.get_field_value(self.ISDATACOMPLETE__FIELD_NAME.field_name)

    def set_lam_field(self, value: Optional[float]):
        """
        Set data field with field name 'lam' on this record model
        """
        self.set_field_value(self.LAM__FIELD_NAME.field_name, value)

    def get_lam_field(self) -> Optional[float]:
        """
        Get data field value with field name 'lam' from this record model
        """
        return self.get_field_value(self.LAM__FIELD_NAME.field_name)

    def set_LLevel_field(self, value: Optional[float]):
        """
        Set data field with field name 'LLevel' on this record model
        """
        self.set_field_value(self.LLEVEL__FIELD_NAME.field_name, value)

    def get_LLevel_field(self) -> Optional[float]:
        """
        Get data field value with field name 'LLevel' from this record model
        """
        return self.get_field_value(self.LLEVEL__FIELD_NAME.field_name)

    def set_maxcount_field(self, value: Optional[int]):
        """
        Set data field with field name 'maxcount' on this record model
        """
        self.set_field_value(self.MAXCOUNT__FIELD_NAME.field_name, value)

    def get_maxcount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'maxcount' from this record model
        """
        return self.get_field_value(self.MAXCOUNT__FIELD_NAME.field_name)

    def set_MaxEMIterations_field(self, value: Optional[int]):
        """
        Set data field with field name 'MaxEMIterations' on this record model
        """
        self.set_field_value(self.MAXEMITERATIONS__FIELD_NAME.field_name, value)

    def get_MaxEMIterations_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MaxEMIterations' from this record model
        """
        return self.get_field_value(self.MAXEMITERATIONS__FIELD_NAME.field_name)

    def set_mincount_field(self, value: Optional[int]):
        """
        Set data field with field name 'mincount' on this record model
        """
        self.set_field_value(self.MINCOUNT__FIELD_NAME.field_name, value)

    def get_mincount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'mincount' from this record model
        """
        return self.get_field_value(self.MINCOUNT__FIELD_NAME.field_name)

    def set_nu_field(self, value: Optional[int]):
        """
        Set data field with field name 'nu' on this record model
        """
        self.set_field_value(self.NU__FIELD_NAME.field_name, value)

    def get_nu_field(self) -> Optional[int]:
        """
        Get data field value with field name 'nu' from this record model
        """
        return self.get_field_value(self.NU__FIELD_NAME.field_name)

    def set_nuest_field(self, value: Optional[str]):
        """
        Set data field with field name 'nuest' on this record model
        """
        self.set_field_value(self.NUEST__FIELD_NAME.field_name, value)

    def get_nuest_field(self) -> Optional[str]:
        """
        Get data field value with field name 'nuest' from this record model
        """
        return self.get_field_value(self.NUEST__FIELD_NAME.field_name)

    def set_NumberOfClusters_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumberOfClusters' on this record model
        """
        self.set_field_value(self.NUMBEROFCLUSTERS__FIELD_NAME.field_name, value)

    def get_NumberOfClusters_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumberOfClusters' from this record model
        """
        return self.get_field_value(self.NUMBEROFCLUSTERS__FIELD_NAME.field_name)

    def set_randomStart_field(self, value: Optional[int]):
        """
        Set data field with field name 'randomStart' on this record model
        """
        self.set_field_value(self.RANDOMSTART__FIELD_NAME.field_name, value)

    def get_randomStart_field(self) -> Optional[int]:
        """
        Get data field value with field name 'randomStart' from this record model
        """
        return self.get_field_value(self.RANDOMSTART__FIELD_NAME.field_name)

    def set_seed_field(self, value: Optional[int]):
        """
        Set data field with field name 'seed' on this record model
        """
        self.set_field_value(self.SEED__FIELD_NAME.field_name, value)

    def get_seed_field(self) -> Optional[int]:
        """
        Get data field value with field name 'seed' from this record model
        """
        return self.get_field_value(self.SEED__FIELD_NAME.field_name)

    def set_tol_field(self, value: Optional[float]):
        """
        Set data field with field name 'tol' on this record model
        """
        self.set_field_value(self.TOL__FIELD_NAME.field_name, value)

    def get_tol_field(self) -> Optional[float]:
        """
        Get data field value with field name 'tol' from this record model
        """
        return self.get_field_value(self.TOL__FIELD_NAME.field_name)

    def set_tolInit_field(self, value: Optional[float]):
        """
        Set data field with field name 'tolInit' on this record model
        """
        self.set_field_value(self.TOLINIT__FIELD_NAME.field_name, value)

    def get_tolInit_field(self) -> Optional[float]:
        """
        Get data field value with field name 'tolInit' from this record model
        """
        return self.get_field_value(self.TOLINIT__FIELD_NAME.field_name)

    def set_trans_field(self, value: Optional[str]):
        """
        Set data field with field name 'trans' on this record model
        """
        self.set_field_value(self.TRANS__FIELD_NAME.field_name, value)

    def get_trans_field(self) -> Optional[str]:
        """
        Get data field value with field name 'trans' from this record model
        """
        return self.get_field_value(self.TRANS__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)

    def set_zcutoff_field(self, value: Optional[float]):
        """
        Set data field with field name 'zcutoff' on this record model
        """
        self.set_field_value(self.ZCUTOFF__FIELD_NAME.field_name, value)

    def get_zcutoff_field(self) -> Optional[float]:
        """
        Get data field value with field name 'zcutoff' from this record model
        """
        return self.get_field_value(self.ZCUTOFF__FIELD_NAME.field_name)


class FlowCompensationMatrixDatumModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowCompensationMatrixDatum
    Data Type Display Name: Flow Compensation Matrix Datum (Flow Compensation Matrix Data)
    Fields: ColumnChannelName, ColumnIndex, CompensationValue, RowChannelName, RowIndex
    Individual flow compensation matrix data value in the matrix.
    """
    DATA_TYPE_NAME: str = 'FlowCompensationMatrixDatum'
    COLUMNCHANNELNAME__FIELD_NAME: WrapperField = WrapperField("ColumnChannelName", FieldType.STRING)
    COLUMNINDEX__FIELD_NAME: WrapperField = WrapperField("ColumnIndex", FieldType.INTEGER)
    COMPENSATIONVALUE__FIELD_NAME: WrapperField = WrapperField("CompensationValue", FieldType.DOUBLE)
    ROWCHANNELNAME__FIELD_NAME: WrapperField = WrapperField("RowChannelName", FieldType.STRING)
    ROWINDEX__FIELD_NAME: WrapperField = WrapperField("RowIndex", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColumnChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColumnChannelName' on this record model
        """
        self.set_field_value(self.COLUMNCHANNELNAME__FIELD_NAME.field_name, value)

    def get_ColumnChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColumnChannelName' from this record model
        """
        return self.get_field_value(self.COLUMNCHANNELNAME__FIELD_NAME.field_name)

    def set_ColumnIndex_field(self, value: Optional[int]):
        """
        Set data field with field name 'ColumnIndex' on this record model
        """
        self.set_field_value(self.COLUMNINDEX__FIELD_NAME.field_name, value)

    def get_ColumnIndex_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ColumnIndex' from this record model
        """
        return self.get_field_value(self.COLUMNINDEX__FIELD_NAME.field_name)

    def set_CompensationValue_field(self, value: Optional[float]):
        """
        Set data field with field name 'CompensationValue' on this record model
        """
        self.set_field_value(self.COMPENSATIONVALUE__FIELD_NAME.field_name, value)

    def get_CompensationValue_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CompensationValue' from this record model
        """
        return self.get_field_value(self.COMPENSATIONVALUE__FIELD_NAME.field_name)

    def set_RowChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowChannelName' on this record model
        """
        self.set_field_value(self.ROWCHANNELNAME__FIELD_NAME.field_name, value)

    def get_RowChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowChannelName' from this record model
        """
        return self.get_field_value(self.ROWCHANNELNAME__FIELD_NAME.field_name)

    def set_RowIndex_field(self, value: Optional[int]):
        """
        Set data field with field name 'RowIndex' on this record model
        """
        self.set_field_value(self.ROWINDEX__FIELD_NAME.field_name, value)

    def get_RowIndex_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RowIndex' from this record model
        """
        return self.get_field_value(self.ROWINDEX__FIELD_NAME.field_name)


class FlowCompensationMatrixInfoModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowCompensationMatrixInfo
    Data Type Display Name: Flow Compensation Matrix Info (Flow Compensation Matrix Info)
    Fields: ChannelNameList, MatrixName
    Contains the info about the matrix itself.

The parents of this matrix are those that are used to create this info file. There can be more than one parent.

This is not directly linked to children FCS files. It will be linked through FlowCompMatrixApplication type.
    """
    DATA_TYPE_NAME: str = 'FlowCompensationMatrixInfo'
    CHANNELNAMELIST__FIELD_NAME: WrapperField = WrapperField("ChannelNameList", FieldType.STRING)
    MATRIXNAME__FIELD_NAME: WrapperField = WrapperField("MatrixName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ChannelNameList_field(self, value: Optional[str]):
        """
        Set data field with field name 'ChannelNameList' on this record model
        """
        self.set_field_value(self.CHANNELNAMELIST__FIELD_NAME.field_name, value)

    def get_ChannelNameList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ChannelNameList' from this record model
        """
        return self.get_field_value(self.CHANNELNAMELIST__FIELD_NAME.field_name)

    def set_MatrixName_field(self, value: Optional[str]):
        """
        Set data field with field name 'MatrixName' on this record model
        """
        self.set_field_value(self.MATRIXNAME__FIELD_NAME.field_name, value)

    def get_MatrixName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MatrixName' from this record model
        """
        return self.get_field_value(self.MATRIXNAME__FIELD_NAME.field_name)


class FlowCompMatrixApplicationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowCompMatrixApplication
    Data Type Display Name: Flow Comp Matrix Application (Flow Comp Matrix Applications)
    Fields: MatrixInfoRecordId
    Apply a flow cyto compensation matrix for a target (parent FCS) file, against a matrix info.
    """
    DATA_TYPE_NAME: str = 'FlowCompMatrixApplication'
    MATRIXINFORECORDID__FIELD_NAME: WrapperField = WrapperField("MatrixInfoRecordId", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_MatrixInfoRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'MatrixInfoRecordId' on this record model
        """
        self.set_field_value(self.MATRIXINFORECORDID__FIELD_NAME.field_name, value)

    def get_MatrixInfoRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MatrixInfoRecordId' from this record model
        """
        return self.get_field_value(self.MATRIXINFORECORDID__FIELD_NAME.field_name)


class FlowCytoFileTemplateModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowCytoFileTemplate
    Data Type Display Name: Flow Cyto File Template (Flow Cyto File Templates)
    Fields: TemplateData, TemplateDescription, TemplateName
    Describes a saved gating and compensation strategy for a flow cytometry file.
    """
    DATA_TYPE_NAME: str = 'FlowCytoFileTemplate'
    TEMPLATEDATA__FIELD_NAME: WrapperField = WrapperField("TemplateData", FieldType.STRING)
    TEMPLATEDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("TemplateDescription", FieldType.STRING)
    TEMPLATENAME__FIELD_NAME: WrapperField = WrapperField("TemplateName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_TemplateData_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateData' on this record model
        """
        self.set_field_value(self.TEMPLATEDATA__FIELD_NAME.field_name, value)

    def get_TemplateData_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateData' from this record model
        """
        return self.get_field_value(self.TEMPLATEDATA__FIELD_NAME.field_name)

    def set_TemplateDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateDescription' on this record model
        """
        self.set_field_value(self.TEMPLATEDESCRIPTION__FIELD_NAME.field_name, value)

    def get_TemplateDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateDescription' from this record model
        """
        return self.get_field_value(self.TEMPLATEDESCRIPTION__FIELD_NAME.field_name)

    def set_TemplateName_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateName' on this record model
        """
        self.set_field_value(self.TEMPLATENAME__FIELD_NAME.field_name, value)

    def get_TemplateName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateName' from this record model
        """
        return self.get_field_value(self.TEMPLATENAME__FIELD_NAME.field_name)


class FlowCytometryChannelInfoModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowCytometryChannelInfo
    Data Type Display Name: Flow Cytometry Channel Info (Flow Cytometry Channel Info)
    Fields: Annotation, AxisMax, AxisMin, AxisRange, ChannelName, TransformLogicleA, TransformLogicleM, TransformLogicleTop, TransformLogicleW, TransformMethod, TransformVarA, TransformVarB
    """
    DATA_TYPE_NAME: str = 'FlowCytometryChannelInfo'
    ANNOTATION__FIELD_NAME: WrapperField = WrapperField("Annotation", FieldType.STRING)
    AXISMAX__FIELD_NAME: WrapperField = WrapperField("AxisMax", FieldType.DOUBLE)
    AXISMIN__FIELD_NAME: WrapperField = WrapperField("AxisMin", FieldType.DOUBLE)
    AXISRANGE__FIELD_NAME: WrapperField = WrapperField("AxisRange", FieldType.DOUBLE)
    CHANNELNAME__FIELD_NAME: WrapperField = WrapperField("ChannelName", FieldType.STRING)
    TRANSFORMLOGICLEA__FIELD_NAME: WrapperField = WrapperField("TransformLogicleA", FieldType.DOUBLE)
    TRANSFORMLOGICLEM__FIELD_NAME: WrapperField = WrapperField("TransformLogicleM", FieldType.DOUBLE)
    TRANSFORMLOGICLETOP__FIELD_NAME: WrapperField = WrapperField("TransformLogicleTop", FieldType.DOUBLE)
    TRANSFORMLOGICLEW__FIELD_NAME: WrapperField = WrapperField("TransformLogicleW", FieldType.DOUBLE)
    TRANSFORMMETHOD__FIELD_NAME: WrapperField = WrapperField("TransformMethod", FieldType.PICKLIST)
    TRANSFORMVARA__FIELD_NAME: WrapperField = WrapperField("TransformVarA", FieldType.DOUBLE)
    TRANSFORMVARB__FIELD_NAME: WrapperField = WrapperField("TransformVarB", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Annotation_field(self, value: Optional[str]):
        """
        Set data field with field name 'Annotation' on this record model
        """
        self.set_field_value(self.ANNOTATION__FIELD_NAME.field_name, value)

    def get_Annotation_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Annotation' from this record model
        """
        return self.get_field_value(self.ANNOTATION__FIELD_NAME.field_name)

    def set_AxisMax_field(self, value: Optional[float]):
        """
        Set data field with field name 'AxisMax' on this record model
        """
        self.set_field_value(self.AXISMAX__FIELD_NAME.field_name, value)

    def get_AxisMax_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AxisMax' from this record model
        """
        return self.get_field_value(self.AXISMAX__FIELD_NAME.field_name)

    def set_AxisMin_field(self, value: Optional[float]):
        """
        Set data field with field name 'AxisMin' on this record model
        """
        self.set_field_value(self.AXISMIN__FIELD_NAME.field_name, value)

    def get_AxisMin_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AxisMin' from this record model
        """
        return self.get_field_value(self.AXISMIN__FIELD_NAME.field_name)

    def set_AxisRange_field(self, value: Optional[float]):
        """
        Set data field with field name 'AxisRange' on this record model
        """
        self.set_field_value(self.AXISRANGE__FIELD_NAME.field_name, value)

    def get_AxisRange_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AxisRange' from this record model
        """
        return self.get_field_value(self.AXISRANGE__FIELD_NAME.field_name)

    def set_ChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ChannelName' on this record model
        """
        self.set_field_value(self.CHANNELNAME__FIELD_NAME.field_name, value)

    def get_ChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ChannelName' from this record model
        """
        return self.get_field_value(self.CHANNELNAME__FIELD_NAME.field_name)

    def set_TransformLogicleA_field(self, value: Optional[float]):
        """
        Set data field with field name 'TransformLogicleA' on this record model
        """
        self.set_field_value(self.TRANSFORMLOGICLEA__FIELD_NAME.field_name, value)

    def get_TransformLogicleA_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TransformLogicleA' from this record model
        """
        return self.get_field_value(self.TRANSFORMLOGICLEA__FIELD_NAME.field_name)

    def set_TransformLogicleM_field(self, value: Optional[float]):
        """
        Set data field with field name 'TransformLogicleM' on this record model
        """
        self.set_field_value(self.TRANSFORMLOGICLEM__FIELD_NAME.field_name, value)

    def get_TransformLogicleM_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TransformLogicleM' from this record model
        """
        return self.get_field_value(self.TRANSFORMLOGICLEM__FIELD_NAME.field_name)

    def set_TransformLogicleTop_field(self, value: Optional[float]):
        """
        Set data field with field name 'TransformLogicleTop' on this record model
        """
        self.set_field_value(self.TRANSFORMLOGICLETOP__FIELD_NAME.field_name, value)

    def get_TransformLogicleTop_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TransformLogicleTop' from this record model
        """
        return self.get_field_value(self.TRANSFORMLOGICLETOP__FIELD_NAME.field_name)

    def set_TransformLogicleW_field(self, value: Optional[float]):
        """
        Set data field with field name 'TransformLogicleW' on this record model
        """
        self.set_field_value(self.TRANSFORMLOGICLEW__FIELD_NAME.field_name, value)

    def get_TransformLogicleW_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TransformLogicleW' from this record model
        """
        return self.get_field_value(self.TRANSFORMLOGICLEW__FIELD_NAME.field_name)

    def set_TransformMethod_field(self, value: Optional[str]):
        """
        Set data field with field name 'TransformMethod' on this record model
        """
        self.set_field_value(self.TRANSFORMMETHOD__FIELD_NAME.field_name, value)

    def get_TransformMethod_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TransformMethod' from this record model
        """
        return self.get_field_value(self.TRANSFORMMETHOD__FIELD_NAME.field_name)

    def set_TransformVarA_field(self, value: Optional[float]):
        """
        Set data field with field name 'TransformVarA' on this record model
        """
        self.set_field_value(self.TRANSFORMVARA__FIELD_NAME.field_name, value)

    def get_TransformVarA_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TransformVarA' from this record model
        """
        return self.get_field_value(self.TRANSFORMVARA__FIELD_NAME.field_name)

    def set_TransformVarB_field(self, value: Optional[float]):
        """
        Set data field with field name 'TransformVarB' on this record model
        """
        self.set_field_value(self.TRANSFORMVARB__FIELD_NAME.field_name, value)

    def get_TransformVarB_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TransformVarB' from this record model
        """
        return self.get_field_value(self.TRANSFORMVARB__FIELD_NAME.field_name)


class FlowDensityGateModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowDensityGate
    Data Type Display Name: Flow Density Gate (Flow Density Gates)
    Fields: IsPositiveX, IsPositiveY, PercentileX, PercentileY, ShapeJSON, UserAnnotation, XChannelName, YChannelName
    """
    DATA_TYPE_NAME: str = 'FlowDensityGate'
    ISPOSITIVEX__FIELD_NAME: WrapperField = WrapperField("IsPositiveX", FieldType.BOOLEAN)
    ISPOSITIVEY__FIELD_NAME: WrapperField = WrapperField("IsPositiveY", FieldType.BOOLEAN)
    PERCENTILEX__FIELD_NAME: WrapperField = WrapperField("PercentileX", FieldType.DOUBLE)
    PERCENTILEY__FIELD_NAME: WrapperField = WrapperField("PercentileY", FieldType.DOUBLE)
    SHAPEJSON__FIELD_NAME: WrapperField = WrapperField("ShapeJSON", FieldType.STRING)
    USERANNOTATION__FIELD_NAME: WrapperField = WrapperField("UserAnnotation", FieldType.STRING)
    XCHANNELNAME__FIELD_NAME: WrapperField = WrapperField("XChannelName", FieldType.STRING)
    YCHANNELNAME__FIELD_NAME: WrapperField = WrapperField("YChannelName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_IsPositiveX_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsPositiveX' on this record model
        """
        self.set_field_value(self.ISPOSITIVEX__FIELD_NAME.field_name, value)

    def get_IsPositiveX_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsPositiveX' from this record model
        """
        return self.get_field_value(self.ISPOSITIVEX__FIELD_NAME.field_name)

    def set_IsPositiveY_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsPositiveY' on this record model
        """
        self.set_field_value(self.ISPOSITIVEY__FIELD_NAME.field_name, value)

    def get_IsPositiveY_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsPositiveY' from this record model
        """
        return self.get_field_value(self.ISPOSITIVEY__FIELD_NAME.field_name)

    def set_PercentileX_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentileX' on this record model
        """
        self.set_field_value(self.PERCENTILEX__FIELD_NAME.field_name, value)

    def get_PercentileX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentileX' from this record model
        """
        return self.get_field_value(self.PERCENTILEX__FIELD_NAME.field_name)

    def set_PercentileY_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentileY' on this record model
        """
        self.set_field_value(self.PERCENTILEY__FIELD_NAME.field_name, value)

    def get_PercentileY_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentileY' from this record model
        """
        return self.get_field_value(self.PERCENTILEY__FIELD_NAME.field_name)

    def set_ShapeJSON_field(self, value: Optional[str]):
        """
        Set data field with field name 'ShapeJSON' on this record model
        """
        self.set_field_value(self.SHAPEJSON__FIELD_NAME.field_name, value)

    def get_ShapeJSON_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ShapeJSON' from this record model
        """
        return self.get_field_value(self.SHAPEJSON__FIELD_NAME.field_name)

    def set_UserAnnotation_field(self, value: Optional[str]):
        """
        Set data field with field name 'UserAnnotation' on this record model
        """
        self.set_field_value(self.USERANNOTATION__FIELD_NAME.field_name, value)

    def get_UserAnnotation_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UserAnnotation' from this record model
        """
        return self.get_field_value(self.USERANNOTATION__FIELD_NAME.field_name)

    def set_XChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'XChannelName' on this record model
        """
        self.set_field_value(self.XCHANNELNAME__FIELD_NAME.field_name, value)

    def get_XChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'XChannelName' from this record model
        """
        return self.get_field_value(self.XCHANNELNAME__FIELD_NAME.field_name)

    def set_YChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'YChannelName' on this record model
        """
        self.set_field_value(self.YCHANNELNAME__FIELD_NAME.field_name, value)

    def get_YChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'YChannelName' from this record model
        """
        return self.get_field_value(self.YCHANNELNAME__FIELD_NAME.field_name)


class FlowDensityGatingStrategyModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowDensityGatingStrategy
    Data Type Display Name: Flow Density Gating Strategy (Flow Density Gating Strategies)
    Fields: FilePath, IsEvaluated, IsPositiveX, IsPositiveY, PercentileX, PercentileY, VeloxCurrentVersion, XAxisChannel, YAxisChannel
    """
    DATA_TYPE_NAME: str = 'FlowDensityGatingStrategy'
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    ISEVALUATED__FIELD_NAME: WrapperField = WrapperField("IsEvaluated", FieldType.BOOLEAN)
    ISPOSITIVEX__FIELD_NAME: WrapperField = WrapperField("IsPositiveX", FieldType.BOOLEAN)
    ISPOSITIVEY__FIELD_NAME: WrapperField = WrapperField("IsPositiveY", FieldType.BOOLEAN)
    PERCENTILEX__FIELD_NAME: WrapperField = WrapperField("PercentileX", FieldType.DOUBLE)
    PERCENTILEY__FIELD_NAME: WrapperField = WrapperField("PercentileY", FieldType.DOUBLE)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)
    XAXISCHANNEL__FIELD_NAME: WrapperField = WrapperField("XAxisChannel", FieldType.SELECTION)
    YAXISCHANNEL__FIELD_NAME: WrapperField = WrapperField("YAxisChannel", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_IsEvaluated_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsEvaluated' on this record model
        """
        self.set_field_value(self.ISEVALUATED__FIELD_NAME.field_name, value)

    def get_IsEvaluated_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsEvaluated' from this record model
        """
        return self.get_field_value(self.ISEVALUATED__FIELD_NAME.field_name)

    def set_IsPositiveX_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsPositiveX' on this record model
        """
        self.set_field_value(self.ISPOSITIVEX__FIELD_NAME.field_name, value)

    def get_IsPositiveX_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsPositiveX' from this record model
        """
        return self.get_field_value(self.ISPOSITIVEX__FIELD_NAME.field_name)

    def set_IsPositiveY_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsPositiveY' on this record model
        """
        self.set_field_value(self.ISPOSITIVEY__FIELD_NAME.field_name, value)

    def get_IsPositiveY_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsPositiveY' from this record model
        """
        return self.get_field_value(self.ISPOSITIVEY__FIELD_NAME.field_name)

    def set_PercentileX_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentileX' on this record model
        """
        self.set_field_value(self.PERCENTILEX__FIELD_NAME.field_name, value)

    def get_PercentileX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentileX' from this record model
        """
        return self.get_field_value(self.PERCENTILEX__FIELD_NAME.field_name)

    def set_PercentileY_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentileY' on this record model
        """
        self.set_field_value(self.PERCENTILEY__FIELD_NAME.field_name, value)

    def get_PercentileY_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentileY' from this record model
        """
        return self.get_field_value(self.PERCENTILEY__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)

    def set_XAxisChannel_field(self, value: Optional[str]):
        """
        Set data field with field name 'XAxisChannel' on this record model
        """
        self.set_field_value(self.XAXISCHANNEL__FIELD_NAME.field_name, value)

    def get_XAxisChannel_field(self) -> Optional[str]:
        """
        Get data field value with field name 'XAxisChannel' from this record model
        """
        return self.get_field_value(self.XAXISCHANNEL__FIELD_NAME.field_name)

    def set_YAxisChannel_field(self, value: Optional[str]):
        """
        Set data field with field name 'YAxisChannel' on this record model
        """
        self.set_field_value(self.YAXISCHANNEL__FIELD_NAME.field_name, value)

    def get_YAxisChannel_field(self) -> Optional[str]:
        """
        Get data field value with field name 'YAxisChannel' from this record model
        """
        return self.get_field_value(self.YAXISCHANNEL__FIELD_NAME.field_name)


class FlowManualGateModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FlowManualGate
    Data Type Display Name: Flow Manual Gate (Flow Manual Gates)
    Fields: IsNegated, ShapeID, ShapeJSON, ShapeType, UserAnnotation, XChannelName, YChannelName
    """
    DATA_TYPE_NAME: str = 'FlowManualGate'
    ISNEGATED__FIELD_NAME: WrapperField = WrapperField("IsNegated", FieldType.BOOLEAN)
    SHAPEID__FIELD_NAME: WrapperField = WrapperField("ShapeID", FieldType.LONG)
    SHAPEJSON__FIELD_NAME: WrapperField = WrapperField("ShapeJSON", FieldType.STRING)
    SHAPETYPE__FIELD_NAME: WrapperField = WrapperField("ShapeType", FieldType.STRING)
    USERANNOTATION__FIELD_NAME: WrapperField = WrapperField("UserAnnotation", FieldType.STRING)
    XCHANNELNAME__FIELD_NAME: WrapperField = WrapperField("XChannelName", FieldType.STRING)
    YCHANNELNAME__FIELD_NAME: WrapperField = WrapperField("YChannelName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_IsNegated_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsNegated' on this record model
        """
        self.set_field_value(self.ISNEGATED__FIELD_NAME.field_name, value)

    def get_IsNegated_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsNegated' from this record model
        """
        return self.get_field_value(self.ISNEGATED__FIELD_NAME.field_name)

    def set_ShapeID_field(self, value: Optional[int]):
        """
        Set data field with field name 'ShapeID' on this record model
        """
        self.set_field_value(self.SHAPEID__FIELD_NAME.field_name, value)

    def get_ShapeID_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ShapeID' from this record model
        """
        return self.get_field_value(self.SHAPEID__FIELD_NAME.field_name)

    def set_ShapeJSON_field(self, value: Optional[str]):
        """
        Set data field with field name 'ShapeJSON' on this record model
        """
        self.set_field_value(self.SHAPEJSON__FIELD_NAME.field_name, value)

    def get_ShapeJSON_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ShapeJSON' from this record model
        """
        return self.get_field_value(self.SHAPEJSON__FIELD_NAME.field_name)

    def set_ShapeType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ShapeType' on this record model
        """
        self.set_field_value(self.SHAPETYPE__FIELD_NAME.field_name, value)

    def get_ShapeType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ShapeType' from this record model
        """
        return self.get_field_value(self.SHAPETYPE__FIELD_NAME.field_name)

    def set_UserAnnotation_field(self, value: Optional[str]):
        """
        Set data field with field name 'UserAnnotation' on this record model
        """
        self.set_field_value(self.USERANNOTATION__FIELD_NAME.field_name, value)

    def get_UserAnnotation_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UserAnnotation' from this record model
        """
        return self.get_field_value(self.USERANNOTATION__FIELD_NAME.field_name)

    def set_XChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'XChannelName' on this record model
        """
        self.set_field_value(self.XCHANNELNAME__FIELD_NAME.field_name, value)

    def get_XChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'XChannelName' from this record model
        """
        return self.get_field_value(self.XCHANNELNAME__FIELD_NAME.field_name)

    def set_YChannelName_field(self, value: Optional[str]):
        """
        Set data field with field name 'YChannelName' on this record model
        """
        self.set_field_value(self.YCHANNELNAME__FIELD_NAME.field_name, value)

    def get_YChannelName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'YChannelName' from this record model
        """
        return self.get_field_value(self.YCHANNELNAME__FIELD_NAME.field_name)


class FourPLLModelModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type FourPLLModel
    Data Type Display Name: Four Parameter Logistic Regression (Four Parameter Logistic Regressions)
    Fields: b, c, d, e, ED10, ED50, ED90, ED95, EntryName, MultiParentLink207, RSquared, SeriesName, SourceEntryId
    Records advanced curve viewer's four parameter logistic regression result, when measuring sample data.
    """
    DATA_TYPE_NAME: str = 'FourPLLModel'
    B__FIELD_NAME: WrapperField = WrapperField("b", FieldType.DOUBLE)
    C__FIELD_NAME: WrapperField = WrapperField("c", FieldType.DOUBLE)
    D__FIELD_NAME: WrapperField = WrapperField("d", FieldType.DOUBLE)
    E__FIELD_NAME: WrapperField = WrapperField("e", FieldType.DOUBLE)
    ED10__FIELD_NAME: WrapperField = WrapperField("ED10", FieldType.DOUBLE)
    ED50__FIELD_NAME: WrapperField = WrapperField("ED50", FieldType.DOUBLE)
    ED90__FIELD_NAME: WrapperField = WrapperField("ED90", FieldType.DOUBLE)
    ED95__FIELD_NAME: WrapperField = WrapperField("ED95", FieldType.DOUBLE)
    ENTRYNAME__FIELD_NAME: WrapperField = WrapperField("EntryName", FieldType.STRING)
    MULTIPARENTLINK207__FIELD_NAME: WrapperField = WrapperField("MultiParentLink207", FieldType.MULTIPARENTLINK)
    RSQUARED__FIELD_NAME: WrapperField = WrapperField("RSquared", FieldType.DOUBLE)
    SERIESNAME__FIELD_NAME: WrapperField = WrapperField("SeriesName", FieldType.STRING)
    SOURCEENTRYID__FIELD_NAME: WrapperField = WrapperField("SourceEntryId", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_b_field(self, value: Optional[float]):
        """
        Set data field with field name 'b' on this record model
        """
        self.set_field_value(self.B__FIELD_NAME.field_name, value)

    def get_b_field(self) -> Optional[float]:
        """
        Get data field value with field name 'b' from this record model
        """
        return self.get_field_value(self.B__FIELD_NAME.field_name)

    def set_c_field(self, value: Optional[float]):
        """
        Set data field with field name 'c' on this record model
        """
        self.set_field_value(self.C__FIELD_NAME.field_name, value)

    def get_c_field(self) -> Optional[float]:
        """
        Get data field value with field name 'c' from this record model
        """
        return self.get_field_value(self.C__FIELD_NAME.field_name)

    def set_d_field(self, value: Optional[float]):
        """
        Set data field with field name 'd' on this record model
        """
        self.set_field_value(self.D__FIELD_NAME.field_name, value)

    def get_d_field(self) -> Optional[float]:
        """
        Get data field value with field name 'd' from this record model
        """
        return self.get_field_value(self.D__FIELD_NAME.field_name)

    def set_e_field(self, value: Optional[float]):
        """
        Set data field with field name 'e' on this record model
        """
        self.set_field_value(self.E__FIELD_NAME.field_name, value)

    def get_e_field(self) -> Optional[float]:
        """
        Get data field value with field name 'e' from this record model
        """
        return self.get_field_value(self.E__FIELD_NAME.field_name)

    def set_ED10_field(self, value: Optional[float]):
        """
        Set data field with field name 'ED10' on this record model
        """
        self.set_field_value(self.ED10__FIELD_NAME.field_name, value)

    def get_ED10_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ED10' from this record model
        """
        return self.get_field_value(self.ED10__FIELD_NAME.field_name)

    def set_ED50_field(self, value: Optional[float]):
        """
        Set data field with field name 'ED50' on this record model
        """
        self.set_field_value(self.ED50__FIELD_NAME.field_name, value)

    def get_ED50_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ED50' from this record model
        """
        return self.get_field_value(self.ED50__FIELD_NAME.field_name)

    def set_ED90_field(self, value: Optional[float]):
        """
        Set data field with field name 'ED90' on this record model
        """
        self.set_field_value(self.ED90__FIELD_NAME.field_name, value)

    def get_ED90_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ED90' from this record model
        """
        return self.get_field_value(self.ED90__FIELD_NAME.field_name)

    def set_ED95_field(self, value: Optional[float]):
        """
        Set data field with field name 'ED95' on this record model
        """
        self.set_field_value(self.ED95__FIELD_NAME.field_name, value)

    def get_ED95_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ED95' from this record model
        """
        return self.get_field_value(self.ED95__FIELD_NAME.field_name)

    def set_EntryName_field(self, value: Optional[str]):
        """
        Set data field with field name 'EntryName' on this record model
        """
        self.set_field_value(self.ENTRYNAME__FIELD_NAME.field_name, value)

    def get_EntryName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EntryName' from this record model
        """
        return self.get_field_value(self.ENTRYNAME__FIELD_NAME.field_name)

    def set_RSquared_field(self, value: Optional[float]):
        """
        Set data field with field name 'RSquared' on this record model
        """
        self.set_field_value(self.RSQUARED__FIELD_NAME.field_name, value)

    def get_RSquared_field(self) -> Optional[float]:
        """
        Get data field value with field name 'RSquared' from this record model
        """
        return self.get_field_value(self.RSQUARED__FIELD_NAME.field_name)

    def set_SeriesName_field(self, value: Optional[str]):
        """
        Set data field with field name 'SeriesName' on this record model
        """
        self.set_field_value(self.SERIESNAME__FIELD_NAME.field_name, value)

    def get_SeriesName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SeriesName' from this record model
        """
        return self.get_field_value(self.SERIESNAME__FIELD_NAME.field_name)

    def set_SourceEntryId_field(self, value: Optional[int]):
        """
        Set data field with field name 'SourceEntryId' on this record model
        """
        self.set_field_value(self.SOURCEENTRYID__FIELD_NAME.field_name, value)

    def get_SourceEntryId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SourceEntryId' from this record model
        """
        return self.get_field_value(self.SOURCEENTRYID__FIELD_NAME.field_name)


class HiSeqFirstBaseReportModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type HiSeqFirstBaseReport
    Data Type Display Name: HiSeq First Base Report (HiSeq First Base Reports)
    Fields: A_Focus_Score, A_Intensity, C_Focus_Score, C_Intensity, ClusterDensity, G_Focus_Score, G_Intensity, Lane, Surface, T_Focus_Score, T_Intensity
     <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'HiSeqFirstBaseReport'
    A_FOCUS_SCORE__FIELD_NAME: WrapperField = WrapperField("A_Focus_Score", FieldType.DOUBLE)
    A_INTENSITY__FIELD_NAME: WrapperField = WrapperField("A_Intensity", FieldType.DOUBLE)
    C_FOCUS_SCORE__FIELD_NAME: WrapperField = WrapperField("C_Focus_Score", FieldType.DOUBLE)
    C_INTENSITY__FIELD_NAME: WrapperField = WrapperField("C_Intensity", FieldType.DOUBLE)
    CLUSTERDENSITY__FIELD_NAME: WrapperField = WrapperField("ClusterDensity", FieldType.DOUBLE)
    G_FOCUS_SCORE__FIELD_NAME: WrapperField = WrapperField("G_Focus_Score", FieldType.DOUBLE)
    G_INTENSITY__FIELD_NAME: WrapperField = WrapperField("G_Intensity", FieldType.DOUBLE)
    LANE__FIELD_NAME: WrapperField = WrapperField("Lane", FieldType.STRING)
    SURFACE__FIELD_NAME: WrapperField = WrapperField("Surface", FieldType.STRING)
    T_FOCUS_SCORE__FIELD_NAME: WrapperField = WrapperField("T_Focus_Score", FieldType.DOUBLE)
    T_INTENSITY__FIELD_NAME: WrapperField = WrapperField("T_Intensity", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_A_Focus_Score_field(self, value: Optional[float]):
        """
        Set data field with field name 'A_Focus_Score' on this record model
        """
        self.set_field_value(self.A_FOCUS_SCORE__FIELD_NAME.field_name, value)

    def get_A_Focus_Score_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A_Focus_Score' from this record model
        """
        return self.get_field_value(self.A_FOCUS_SCORE__FIELD_NAME.field_name)

    def set_A_Intensity_field(self, value: Optional[float]):
        """
        Set data field with field name 'A_Intensity' on this record model
        """
        self.set_field_value(self.A_INTENSITY__FIELD_NAME.field_name, value)

    def get_A_Intensity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A_Intensity' from this record model
        """
        return self.get_field_value(self.A_INTENSITY__FIELD_NAME.field_name)

    def set_C_Focus_Score_field(self, value: Optional[float]):
        """
        Set data field with field name 'C_Focus_Score' on this record model
        """
        self.set_field_value(self.C_FOCUS_SCORE__FIELD_NAME.field_name, value)

    def get_C_Focus_Score_field(self) -> Optional[float]:
        """
        Get data field value with field name 'C_Focus_Score' from this record model
        """
        return self.get_field_value(self.C_FOCUS_SCORE__FIELD_NAME.field_name)

    def set_C_Intensity_field(self, value: Optional[float]):
        """
        Set data field with field name 'C_Intensity' on this record model
        """
        self.set_field_value(self.C_INTENSITY__FIELD_NAME.field_name, value)

    def get_C_Intensity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'C_Intensity' from this record model
        """
        return self.get_field_value(self.C_INTENSITY__FIELD_NAME.field_name)

    def set_ClusterDensity_field(self, value: Optional[float]):
        """
        Set data field with field name 'ClusterDensity' on this record model
        """
        self.set_field_value(self.CLUSTERDENSITY__FIELD_NAME.field_name, value)

    def get_ClusterDensity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ClusterDensity' from this record model
        """
        return self.get_field_value(self.CLUSTERDENSITY__FIELD_NAME.field_name)

    def set_G_Focus_Score_field(self, value: Optional[float]):
        """
        Set data field with field name 'G_Focus_Score' on this record model
        """
        self.set_field_value(self.G_FOCUS_SCORE__FIELD_NAME.field_name, value)

    def get_G_Focus_Score_field(self) -> Optional[float]:
        """
        Get data field value with field name 'G_Focus_Score' from this record model
        """
        return self.get_field_value(self.G_FOCUS_SCORE__FIELD_NAME.field_name)

    def set_G_Intensity_field(self, value: Optional[float]):
        """
        Set data field with field name 'G_Intensity' on this record model
        """
        self.set_field_value(self.G_INTENSITY__FIELD_NAME.field_name, value)

    def get_G_Intensity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'G_Intensity' from this record model
        """
        return self.get_field_value(self.G_INTENSITY__FIELD_NAME.field_name)

    def set_Lane_field(self, value: Optional[str]):
        """
        Set data field with field name 'Lane' on this record model
        """
        self.set_field_value(self.LANE__FIELD_NAME.field_name, value)

    def get_Lane_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Lane' from this record model
        """
        return self.get_field_value(self.LANE__FIELD_NAME.field_name)

    def set_Surface_field(self, value: Optional[str]):
        """
        Set data field with field name 'Surface' on this record model
        """
        self.set_field_value(self.SURFACE__FIELD_NAME.field_name, value)

    def get_Surface_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Surface' from this record model
        """
        return self.get_field_value(self.SURFACE__FIELD_NAME.field_name)

    def set_T_Focus_Score_field(self, value: Optional[float]):
        """
        Set data field with field name 'T_Focus_Score' on this record model
        """
        self.set_field_value(self.T_FOCUS_SCORE__FIELD_NAME.field_name, value)

    def get_T_Focus_Score_field(self) -> Optional[float]:
        """
        Get data field value with field name 'T_Focus_Score' from this record model
        """
        return self.get_field_value(self.T_FOCUS_SCORE__FIELD_NAME.field_name)

    def set_T_Intensity_field(self, value: Optional[float]):
        """
        Set data field with field name 'T_Intensity' on this record model
        """
        self.set_field_value(self.T_INTENSITY__FIELD_NAME.field_name, value)

    def get_T_Intensity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'T_Intensity' from this record model
        """
        return self.get_field_value(self.T_INTENSITY__FIELD_NAME.field_name)


class IllSeqReadModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IllSeqRead
    Data Type Display Name: Illumina Sequencing Read (Illumina Sequencing Reads)
    Fields: IsIndexedRead, NumCycles
    """
    DATA_TYPE_NAME: str = 'IllSeqRead'
    ISINDEXEDREAD__FIELD_NAME: WrapperField = WrapperField("IsIndexedRead", FieldType.BOOLEAN)
    NUMCYCLES__FIELD_NAME: WrapperField = WrapperField("NumCycles", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_IsIndexedRead_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsIndexedRead' on this record model
        """
        self.set_field_value(self.ISINDEXEDREAD__FIELD_NAME.field_name, value)

    def get_IsIndexedRead_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsIndexedRead' from this record model
        """
        return self.get_field_value(self.ISINDEXEDREAD__FIELD_NAME.field_name)

    def set_NumCycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumCycles' on this record model
        """
        self.set_field_value(self.NUMCYCLES__FIELD_NAME.field_name, value)

    def get_NumCycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumCycles' from this record model
        """
        return self.get_field_value(self.NUMCYCLES__FIELD_NAME.field_name)


class IlluminaHiSeqRunParametersModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaHiSeqRunParameters
    Data Type Display Name: Illumina HiSeq Run Parameters (Illumina HiSeq Run Parameters')
    Fields: AdapterPlate, AlignToPhiXLane, ApplicationName, ApplicationVersion, AutoTiltOnce, Barcode, BaseSpaceRunId, BaseSpaceRunMonitoringOnly, BaseSpaceTempFolder, BaseSpaceUseBaseSpace, BaseSpaceUsername, CameraDriver, CameraFirmware, CanEditRunMode, ChemistryVersion, ComputerName, ControlLane, CopyImages, CPLDVersion, CVGainPosLocked, CVGainStart, DitherSize, EnableAnalysis, EnableAutoCenter, EnableBasecalling, EnableCameraLogging, EnableLft, EnableNotifications, ExperimentName, FCPosition, FirstBaseConfirmation, Flowcell, FocusCameraFirmware, FocusMethod, FPGAVersion, HotPixel, IGain, IHistory, ImageHeight, ImageWidth, IndexQuantity, IndexRead, IndexSerialNumber, IntensityCeiling, IsNew50Cycle, IsNew200Cycle, KeepIntensityFiles, LaneLength, MaxInitialZJumpHalfUm, MaxSubsequentZJumpHalfUm, MockRun, MotorDelayFrames, NumAnalysisThreads, NumberCyclesRemaining, NumberOfInitialZJumps, NumSwaths, NumTilesPerSwath, Offset, OutputFolder, PeQuantity, PerformPreRunFluidicsCheck, PeriodicSave, PeSerialNumber, Prime, PromptForPeReagents, Read1, Read2, RecipeFragmentVersion, Rehyb, Resume, ResumeCycle, RTAVersion, RunID, RunMode, RunStartDate, SampleSheet, SbsQuantity, SbsSerialNumber, ScanID, ScannerID, ScanNumber, SelectedSection_1, SelectedSection_2, SelectedSection_3, SelectedSection_4, SelectedSection_5, SelectedSection_6, SelectedSection_7, SelectedSection_8, SelectedSurface, SlideHolder, SupportMultipleSurfacesInUI, SwathScanMode, TempFolder, TemplateCycleCount, TileHeight, TileWidth, UseExistingRecipe, Username, WorkFlowType
     <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'IlluminaHiSeqRunParameters'
    ADAPTERPLATE__FIELD_NAME: WrapperField = WrapperField("AdapterPlate", FieldType.STRING)
    ALIGNTOPHIXLANE__FIELD_NAME: WrapperField = WrapperField("AlignToPhiXLane", FieldType.STRING)
    APPLICATIONNAME__FIELD_NAME: WrapperField = WrapperField("ApplicationName", FieldType.STRING)
    APPLICATIONVERSION__FIELD_NAME: WrapperField = WrapperField("ApplicationVersion", FieldType.STRING)
    AUTOTILTONCE__FIELD_NAME: WrapperField = WrapperField("AutoTiltOnce", FieldType.BOOLEAN)
    BARCODE__FIELD_NAME: WrapperField = WrapperField("Barcode", FieldType.STRING)
    BASESPACERUNID__FIELD_NAME: WrapperField = WrapperField("BaseSpaceRunId", FieldType.STRING)
    BASESPACERUNMONITORINGONLY__FIELD_NAME: WrapperField = WrapperField("BaseSpaceRunMonitoringOnly", FieldType.BOOLEAN)
    BASESPACETEMPFOLDER__FIELD_NAME: WrapperField = WrapperField("BaseSpaceTempFolder", FieldType.STRING)
    BASESPACEUSEBASESPACE__FIELD_NAME: WrapperField = WrapperField("BaseSpaceUseBaseSpace", FieldType.BOOLEAN)
    BASESPACEUSERNAME__FIELD_NAME: WrapperField = WrapperField("BaseSpaceUsername", FieldType.STRING)
    CAMERADRIVER__FIELD_NAME: WrapperField = WrapperField("CameraDriver", FieldType.STRING)
    CAMERAFIRMWARE__FIELD_NAME: WrapperField = WrapperField("CameraFirmware", FieldType.STRING)
    CANEDITRUNMODE__FIELD_NAME: WrapperField = WrapperField("CanEditRunMode", FieldType.BOOLEAN)
    CHEMISTRYVERSION__FIELD_NAME: WrapperField = WrapperField("ChemistryVersion", FieldType.STRING)
    COMPUTERNAME__FIELD_NAME: WrapperField = WrapperField("ComputerName", FieldType.STRING)
    CONTROLLANE__FIELD_NAME: WrapperField = WrapperField("ControlLane", FieldType.STRING)
    COPYIMAGES__FIELD_NAME: WrapperField = WrapperField("CopyImages", FieldType.BOOLEAN)
    CPLDVERSION__FIELD_NAME: WrapperField = WrapperField("CPLDVersion", FieldType.STRING)
    CVGAINPOSLOCKED__FIELD_NAME: WrapperField = WrapperField("CVGainPosLocked", FieldType.STRING)
    CVGAINSTART__FIELD_NAME: WrapperField = WrapperField("CVGainStart", FieldType.STRING)
    DITHERSIZE__FIELD_NAME: WrapperField = WrapperField("DitherSize", FieldType.STRING)
    ENABLEANALYSIS__FIELD_NAME: WrapperField = WrapperField("EnableAnalysis", FieldType.BOOLEAN)
    ENABLEAUTOCENTER__FIELD_NAME: WrapperField = WrapperField("EnableAutoCenter", FieldType.BOOLEAN)
    ENABLEBASECALLING__FIELD_NAME: WrapperField = WrapperField("EnableBasecalling", FieldType.BOOLEAN)
    ENABLECAMERALOGGING__FIELD_NAME: WrapperField = WrapperField("EnableCameraLogging", FieldType.BOOLEAN)
    ENABLELFT__FIELD_NAME: WrapperField = WrapperField("EnableLft", FieldType.BOOLEAN)
    ENABLENOTIFICATIONS__FIELD_NAME: WrapperField = WrapperField("EnableNotifications", FieldType.BOOLEAN)
    EXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("ExperimentName", FieldType.STRING)
    FCPOSITION__FIELD_NAME: WrapperField = WrapperField("FCPosition", FieldType.STRING)
    FIRSTBASECONFIRMATION__FIELD_NAME: WrapperField = WrapperField("FirstBaseConfirmation", FieldType.STRING)
    FLOWCELL__FIELD_NAME: WrapperField = WrapperField("Flowcell", FieldType.STRING)
    FOCUSCAMERAFIRMWARE__FIELD_NAME: WrapperField = WrapperField("FocusCameraFirmware", FieldType.STRING)
    FOCUSMETHOD__FIELD_NAME: WrapperField = WrapperField("FocusMethod", FieldType.STRING)
    FPGAVERSION__FIELD_NAME: WrapperField = WrapperField("FPGAVersion", FieldType.STRING)
    HOTPIXEL__FIELD_NAME: WrapperField = WrapperField("HotPixel", FieldType.STRING)
    IGAIN__FIELD_NAME: WrapperField = WrapperField("IGain", FieldType.STRING)
    IHISTORY__FIELD_NAME: WrapperField = WrapperField("IHistory", FieldType.STRING)
    IMAGEHEIGHT__FIELD_NAME: WrapperField = WrapperField("ImageHeight", FieldType.STRING)
    IMAGEWIDTH__FIELD_NAME: WrapperField = WrapperField("ImageWidth", FieldType.STRING)
    INDEXQUANTITY__FIELD_NAME: WrapperField = WrapperField("IndexQuantity", FieldType.DOUBLE)
    INDEXREAD__FIELD_NAME: WrapperField = WrapperField("IndexRead", FieldType.STRING)
    INDEXSERIALNUMBER__FIELD_NAME: WrapperField = WrapperField("IndexSerialNumber", FieldType.SELECTION)
    INTENSITYCEILING__FIELD_NAME: WrapperField = WrapperField("IntensityCeiling", FieldType.STRING)
    ISNEW50CYCLE__FIELD_NAME: WrapperField = WrapperField("IsNew50Cycle", FieldType.BOOLEAN)
    ISNEW200CYCLE__FIELD_NAME: WrapperField = WrapperField("IsNew200Cycle", FieldType.BOOLEAN)
    KEEPINTENSITYFILES__FIELD_NAME: WrapperField = WrapperField("KeepIntensityFiles", FieldType.STRING)
    LANELENGTH__FIELD_NAME: WrapperField = WrapperField("LaneLength", FieldType.STRING)
    MAXINITIALZJUMPHALFUM__FIELD_NAME: WrapperField = WrapperField("MaxInitialZJumpHalfUm", FieldType.STRING)
    MAXSUBSEQUENTZJUMPHALFUM__FIELD_NAME: WrapperField = WrapperField("MaxSubsequentZJumpHalfUm", FieldType.STRING)
    MOCKRUN__FIELD_NAME: WrapperField = WrapperField("MockRun", FieldType.BOOLEAN)
    MOTORDELAYFRAMES__FIELD_NAME: WrapperField = WrapperField("MotorDelayFrames", FieldType.STRING)
    NUMANALYSISTHREADS__FIELD_NAME: WrapperField = WrapperField("NumAnalysisThreads", FieldType.STRING)
    NUMBERCYCLESREMAINING__FIELD_NAME: WrapperField = WrapperField("NumberCyclesRemaining", FieldType.LONG)
    NUMBEROFINITIALZJUMPS__FIELD_NAME: WrapperField = WrapperField("NumberOfInitialZJumps", FieldType.STRING)
    NUMSWATHS__FIELD_NAME: WrapperField = WrapperField("NumSwaths", FieldType.STRING)
    NUMTILESPERSWATH__FIELD_NAME: WrapperField = WrapperField("NumTilesPerSwath", FieldType.STRING)
    OFFSET__FIELD_NAME: WrapperField = WrapperField("Offset", FieldType.STRING)
    OUTPUTFOLDER__FIELD_NAME: WrapperField = WrapperField("OutputFolder", FieldType.STRING)
    PEQUANTITY__FIELD_NAME: WrapperField = WrapperField("PeQuantity", FieldType.DOUBLE)
    PERFORMPRERUNFLUIDICSCHECK__FIELD_NAME: WrapperField = WrapperField("PerformPreRunFluidicsCheck", FieldType.BOOLEAN)
    PERIODICSAVE__FIELD_NAME: WrapperField = WrapperField("PeriodicSave", FieldType.STRING)
    PESERIALNUMBER__FIELD_NAME: WrapperField = WrapperField("PeSerialNumber", FieldType.SELECTION)
    PRIME__FIELD_NAME: WrapperField = WrapperField("Prime", FieldType.BOOLEAN)
    PROMPTFORPEREAGENTS__FIELD_NAME: WrapperField = WrapperField("PromptForPeReagents", FieldType.BOOLEAN)
    READ1__FIELD_NAME: WrapperField = WrapperField("Read1", FieldType.STRING)
    READ2__FIELD_NAME: WrapperField = WrapperField("Read2", FieldType.STRING)
    RECIPEFRAGMENTVERSION__FIELD_NAME: WrapperField = WrapperField("RecipeFragmentVersion", FieldType.STRING)
    REHYB__FIELD_NAME: WrapperField = WrapperField("Rehyb", FieldType.STRING)
    RESUME__FIELD_NAME: WrapperField = WrapperField("Resume", FieldType.BOOLEAN)
    RESUMECYCLE__FIELD_NAME: WrapperField = WrapperField("ResumeCycle", FieldType.STRING)
    RTAVERSION__FIELD_NAME: WrapperField = WrapperField("RTAVersion", FieldType.STRING)
    RUNID__FIELD_NAME: WrapperField = WrapperField("RunID", FieldType.STRING)
    RUNMODE__FIELD_NAME: WrapperField = WrapperField("RunMode", FieldType.STRING)
    RUNSTARTDATE__FIELD_NAME: WrapperField = WrapperField("RunStartDate", FieldType.DATE)
    SAMPLESHEET__FIELD_NAME: WrapperField = WrapperField("SampleSheet", FieldType.STRING)
    SBSQUANTITY__FIELD_NAME: WrapperField = WrapperField("SbsQuantity", FieldType.DOUBLE)
    SBSSERIALNUMBER__FIELD_NAME: WrapperField = WrapperField("SbsSerialNumber", FieldType.SELECTION)
    SCANID__FIELD_NAME: WrapperField = WrapperField("ScanID", FieldType.STRING)
    SCANNERID__FIELD_NAME: WrapperField = WrapperField("ScannerID", FieldType.STRING)
    SCANNUMBER__FIELD_NAME: WrapperField = WrapperField("ScanNumber", FieldType.LONG)
    SELECTEDSECTION_1__FIELD_NAME: WrapperField = WrapperField("SelectedSection_1", FieldType.STRING)
    SELECTEDSECTION_2__FIELD_NAME: WrapperField = WrapperField("SelectedSection_2", FieldType.STRING)
    SELECTEDSECTION_3__FIELD_NAME: WrapperField = WrapperField("SelectedSection_3", FieldType.STRING)
    SELECTEDSECTION_4__FIELD_NAME: WrapperField = WrapperField("SelectedSection_4", FieldType.STRING)
    SELECTEDSECTION_5__FIELD_NAME: WrapperField = WrapperField("SelectedSection_5", FieldType.STRING)
    SELECTEDSECTION_6__FIELD_NAME: WrapperField = WrapperField("SelectedSection_6", FieldType.STRING)
    SELECTEDSECTION_7__FIELD_NAME: WrapperField = WrapperField("SelectedSection_7", FieldType.STRING)
    SELECTEDSECTION_8__FIELD_NAME: WrapperField = WrapperField("SelectedSection_8", FieldType.STRING)
    SELECTEDSURFACE__FIELD_NAME: WrapperField = WrapperField("SelectedSurface", FieldType.STRING)
    SLIDEHOLDER__FIELD_NAME: WrapperField = WrapperField("SlideHolder", FieldType.STRING)
    SUPPORTMULTIPLESURFACESINUI__FIELD_NAME: WrapperField = WrapperField("SupportMultipleSurfacesInUI", FieldType.BOOLEAN)
    SWATHSCANMODE__FIELD_NAME: WrapperField = WrapperField("SwathScanMode", FieldType.STRING)
    TEMPFOLDER__FIELD_NAME: WrapperField = WrapperField("TempFolder", FieldType.STRING)
    TEMPLATECYCLECOUNT__FIELD_NAME: WrapperField = WrapperField("TemplateCycleCount", FieldType.STRING)
    TILEHEIGHT__FIELD_NAME: WrapperField = WrapperField("TileHeight", FieldType.STRING)
    TILEWIDTH__FIELD_NAME: WrapperField = WrapperField("TileWidth", FieldType.STRING)
    USEEXISTINGRECIPE__FIELD_NAME: WrapperField = WrapperField("UseExistingRecipe", FieldType.BOOLEAN)
    USERNAME__FIELD_NAME: WrapperField = WrapperField("Username", FieldType.STRING)
    WORKFLOWTYPE__FIELD_NAME: WrapperField = WrapperField("WorkFlowType", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AdapterPlate_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdapterPlate' on this record model
        """
        self.set_field_value(self.ADAPTERPLATE__FIELD_NAME.field_name, value)

    def get_AdapterPlate_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdapterPlate' from this record model
        """
        return self.get_field_value(self.ADAPTERPLATE__FIELD_NAME.field_name)

    def set_AlignToPhiXLane_field(self, value: Optional[str]):
        """
        Set data field with field name 'AlignToPhiXLane' on this record model
        """
        self.set_field_value(self.ALIGNTOPHIXLANE__FIELD_NAME.field_name, value)

    def get_AlignToPhiXLane_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AlignToPhiXLane' from this record model
        """
        return self.get_field_value(self.ALIGNTOPHIXLANE__FIELD_NAME.field_name)

    def set_ApplicationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApplicationName' on this record model
        """
        self.set_field_value(self.APPLICATIONNAME__FIELD_NAME.field_name, value)

    def get_ApplicationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApplicationName' from this record model
        """
        return self.get_field_value(self.APPLICATIONNAME__FIELD_NAME.field_name)

    def set_ApplicationVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApplicationVersion' on this record model
        """
        self.set_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name, value)

    def get_ApplicationVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApplicationVersion' from this record model
        """
        return self.get_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name)

    def set_AutoTiltOnce_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AutoTiltOnce' on this record model
        """
        self.set_field_value(self.AUTOTILTONCE__FIELD_NAME.field_name, value)

    def get_AutoTiltOnce_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AutoTiltOnce' from this record model
        """
        return self.get_field_value(self.AUTOTILTONCE__FIELD_NAME.field_name)

    def set_Barcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'Barcode' on this record model
        """
        self.set_field_value(self.BARCODE__FIELD_NAME.field_name, value)

    def get_Barcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Barcode' from this record model
        """
        return self.get_field_value(self.BARCODE__FIELD_NAME.field_name)

    def set_BaseSpaceRunId_field(self, value: Optional[str]):
        """
        Set data field with field name 'BaseSpaceRunId' on this record model
        """
        self.set_field_value(self.BASESPACERUNID__FIELD_NAME.field_name, value)

    def get_BaseSpaceRunId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BaseSpaceRunId' from this record model
        """
        return self.get_field_value(self.BASESPACERUNID__FIELD_NAME.field_name)

    def set_BaseSpaceRunMonitoringOnly_field(self, value: Optional[bool]):
        """
        Set data field with field name 'BaseSpaceRunMonitoringOnly' on this record model
        """
        self.set_field_value(self.BASESPACERUNMONITORINGONLY__FIELD_NAME.field_name, value)

    def get_BaseSpaceRunMonitoringOnly_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'BaseSpaceRunMonitoringOnly' from this record model
        """
        return self.get_field_value(self.BASESPACERUNMONITORINGONLY__FIELD_NAME.field_name)

    def set_BaseSpaceTempFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'BaseSpaceTempFolder' on this record model
        """
        self.set_field_value(self.BASESPACETEMPFOLDER__FIELD_NAME.field_name, value)

    def get_BaseSpaceTempFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BaseSpaceTempFolder' from this record model
        """
        return self.get_field_value(self.BASESPACETEMPFOLDER__FIELD_NAME.field_name)

    def set_BaseSpaceUseBaseSpace_field(self, value: Optional[bool]):
        """
        Set data field with field name 'BaseSpaceUseBaseSpace' on this record model
        """
        self.set_field_value(self.BASESPACEUSEBASESPACE__FIELD_NAME.field_name, value)

    def get_BaseSpaceUseBaseSpace_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'BaseSpaceUseBaseSpace' from this record model
        """
        return self.get_field_value(self.BASESPACEUSEBASESPACE__FIELD_NAME.field_name)

    def set_BaseSpaceUsername_field(self, value: Optional[str]):
        """
        Set data field with field name 'BaseSpaceUsername' on this record model
        """
        self.set_field_value(self.BASESPACEUSERNAME__FIELD_NAME.field_name, value)

    def get_BaseSpaceUsername_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BaseSpaceUsername' from this record model
        """
        return self.get_field_value(self.BASESPACEUSERNAME__FIELD_NAME.field_name)

    def set_CameraDriver_field(self, value: Optional[str]):
        """
        Set data field with field name 'CameraDriver' on this record model
        """
        self.set_field_value(self.CAMERADRIVER__FIELD_NAME.field_name, value)

    def get_CameraDriver_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CameraDriver' from this record model
        """
        return self.get_field_value(self.CAMERADRIVER__FIELD_NAME.field_name)

    def set_CameraFirmware_field(self, value: Optional[str]):
        """
        Set data field with field name 'CameraFirmware' on this record model
        """
        self.set_field_value(self.CAMERAFIRMWARE__FIELD_NAME.field_name, value)

    def get_CameraFirmware_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CameraFirmware' from this record model
        """
        return self.get_field_value(self.CAMERAFIRMWARE__FIELD_NAME.field_name)

    def set_CanEditRunMode_field(self, value: Optional[bool]):
        """
        Set data field with field name 'CanEditRunMode' on this record model
        """
        self.set_field_value(self.CANEDITRUNMODE__FIELD_NAME.field_name, value)

    def get_CanEditRunMode_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'CanEditRunMode' from this record model
        """
        return self.get_field_value(self.CANEDITRUNMODE__FIELD_NAME.field_name)

    def set_ChemistryVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'ChemistryVersion' on this record model
        """
        self.set_field_value(self.CHEMISTRYVERSION__FIELD_NAME.field_name, value)

    def get_ChemistryVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ChemistryVersion' from this record model
        """
        return self.get_field_value(self.CHEMISTRYVERSION__FIELD_NAME.field_name)

    def set_ComputerName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ComputerName' on this record model
        """
        self.set_field_value(self.COMPUTERNAME__FIELD_NAME.field_name, value)

    def get_ComputerName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ComputerName' from this record model
        """
        return self.get_field_value(self.COMPUTERNAME__FIELD_NAME.field_name)

    def set_ControlLane_field(self, value: Optional[str]):
        """
        Set data field with field name 'ControlLane' on this record model
        """
        self.set_field_value(self.CONTROLLANE__FIELD_NAME.field_name, value)

    def get_ControlLane_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ControlLane' from this record model
        """
        return self.get_field_value(self.CONTROLLANE__FIELD_NAME.field_name)

    def set_CopyImages_field(self, value: Optional[bool]):
        """
        Set data field with field name 'CopyImages' on this record model
        """
        self.set_field_value(self.COPYIMAGES__FIELD_NAME.field_name, value)

    def get_CopyImages_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'CopyImages' from this record model
        """
        return self.get_field_value(self.COPYIMAGES__FIELD_NAME.field_name)

    def set_CPLDVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'CPLDVersion' on this record model
        """
        self.set_field_value(self.CPLDVERSION__FIELD_NAME.field_name, value)

    def get_CPLDVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CPLDVersion' from this record model
        """
        return self.get_field_value(self.CPLDVERSION__FIELD_NAME.field_name)

    def set_CVGainPosLocked_field(self, value: Optional[str]):
        """
        Set data field with field name 'CVGainPosLocked' on this record model
        """
        self.set_field_value(self.CVGAINPOSLOCKED__FIELD_NAME.field_name, value)

    def get_CVGainPosLocked_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CVGainPosLocked' from this record model
        """
        return self.get_field_value(self.CVGAINPOSLOCKED__FIELD_NAME.field_name)

    def set_CVGainStart_field(self, value: Optional[str]):
        """
        Set data field with field name 'CVGainStart' on this record model
        """
        self.set_field_value(self.CVGAINSTART__FIELD_NAME.field_name, value)

    def get_CVGainStart_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CVGainStart' from this record model
        """
        return self.get_field_value(self.CVGAINSTART__FIELD_NAME.field_name)

    def set_DitherSize_field(self, value: Optional[str]):
        """
        Set data field with field name 'DitherSize' on this record model
        """
        self.set_field_value(self.DITHERSIZE__FIELD_NAME.field_name, value)

    def get_DitherSize_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DitherSize' from this record model
        """
        return self.get_field_value(self.DITHERSIZE__FIELD_NAME.field_name)

    def set_EnableAnalysis_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableAnalysis' on this record model
        """
        self.set_field_value(self.ENABLEANALYSIS__FIELD_NAME.field_name, value)

    def get_EnableAnalysis_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableAnalysis' from this record model
        """
        return self.get_field_value(self.ENABLEANALYSIS__FIELD_NAME.field_name)

    def set_EnableAutoCenter_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableAutoCenter' on this record model
        """
        self.set_field_value(self.ENABLEAUTOCENTER__FIELD_NAME.field_name, value)

    def get_EnableAutoCenter_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableAutoCenter' from this record model
        """
        return self.get_field_value(self.ENABLEAUTOCENTER__FIELD_NAME.field_name)

    def set_EnableBasecalling_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableBasecalling' on this record model
        """
        self.set_field_value(self.ENABLEBASECALLING__FIELD_NAME.field_name, value)

    def get_EnableBasecalling_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableBasecalling' from this record model
        """
        return self.get_field_value(self.ENABLEBASECALLING__FIELD_NAME.field_name)

    def set_EnableCameraLogging_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableCameraLogging' on this record model
        """
        self.set_field_value(self.ENABLECAMERALOGGING__FIELD_NAME.field_name, value)

    def get_EnableCameraLogging_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableCameraLogging' from this record model
        """
        return self.get_field_value(self.ENABLECAMERALOGGING__FIELD_NAME.field_name)

    def set_EnableLft_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableLft' on this record model
        """
        self.set_field_value(self.ENABLELFT__FIELD_NAME.field_name, value)

    def get_EnableLft_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableLft' from this record model
        """
        return self.get_field_value(self.ENABLELFT__FIELD_NAME.field_name)

    def set_EnableNotifications_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableNotifications' on this record model
        """
        self.set_field_value(self.ENABLENOTIFICATIONS__FIELD_NAME.field_name, value)

    def get_EnableNotifications_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableNotifications' from this record model
        """
        return self.get_field_value(self.ENABLENOTIFICATIONS__FIELD_NAME.field_name)

    def set_ExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentName' on this record model
        """
        self.set_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_ExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentName' from this record model
        """
        return self.get_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name)

    def set_FCPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'FCPosition' on this record model
        """
        self.set_field_value(self.FCPOSITION__FIELD_NAME.field_name, value)

    def get_FCPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FCPosition' from this record model
        """
        return self.get_field_value(self.FCPOSITION__FIELD_NAME.field_name)

    def set_FirstBaseConfirmation_field(self, value: Optional[str]):
        """
        Set data field with field name 'FirstBaseConfirmation' on this record model
        """
        self.set_field_value(self.FIRSTBASECONFIRMATION__FIELD_NAME.field_name, value)

    def get_FirstBaseConfirmation_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FirstBaseConfirmation' from this record model
        """
        return self.get_field_value(self.FIRSTBASECONFIRMATION__FIELD_NAME.field_name)

    def set_Flowcell_field(self, value: Optional[str]):
        """
        Set data field with field name 'Flowcell' on this record model
        """
        self.set_field_value(self.FLOWCELL__FIELD_NAME.field_name, value)

    def get_Flowcell_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Flowcell' from this record model
        """
        return self.get_field_value(self.FLOWCELL__FIELD_NAME.field_name)

    def set_FocusCameraFirmware_field(self, value: Optional[str]):
        """
        Set data field with field name 'FocusCameraFirmware' on this record model
        """
        self.set_field_value(self.FOCUSCAMERAFIRMWARE__FIELD_NAME.field_name, value)

    def get_FocusCameraFirmware_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FocusCameraFirmware' from this record model
        """
        return self.get_field_value(self.FOCUSCAMERAFIRMWARE__FIELD_NAME.field_name)

    def set_FocusMethod_field(self, value: Optional[str]):
        """
        Set data field with field name 'FocusMethod' on this record model
        """
        self.set_field_value(self.FOCUSMETHOD__FIELD_NAME.field_name, value)

    def get_FocusMethod_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FocusMethod' from this record model
        """
        return self.get_field_value(self.FOCUSMETHOD__FIELD_NAME.field_name)

    def set_FPGAVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'FPGAVersion' on this record model
        """
        self.set_field_value(self.FPGAVERSION__FIELD_NAME.field_name, value)

    def get_FPGAVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FPGAVersion' from this record model
        """
        return self.get_field_value(self.FPGAVERSION__FIELD_NAME.field_name)

    def set_HotPixel_field(self, value: Optional[str]):
        """
        Set data field with field name 'HotPixel' on this record model
        """
        self.set_field_value(self.HOTPIXEL__FIELD_NAME.field_name, value)

    def get_HotPixel_field(self) -> Optional[str]:
        """
        Get data field value with field name 'HotPixel' from this record model
        """
        return self.get_field_value(self.HOTPIXEL__FIELD_NAME.field_name)

    def set_IGain_field(self, value: Optional[str]):
        """
        Set data field with field name 'IGain' on this record model
        """
        self.set_field_value(self.IGAIN__FIELD_NAME.field_name, value)

    def get_IGain_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IGain' from this record model
        """
        return self.get_field_value(self.IGAIN__FIELD_NAME.field_name)

    def set_IHistory_field(self, value: Optional[str]):
        """
        Set data field with field name 'IHistory' on this record model
        """
        self.set_field_value(self.IHISTORY__FIELD_NAME.field_name, value)

    def get_IHistory_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IHistory' from this record model
        """
        return self.get_field_value(self.IHISTORY__FIELD_NAME.field_name)

    def set_ImageHeight_field(self, value: Optional[str]):
        """
        Set data field with field name 'ImageHeight' on this record model
        """
        self.set_field_value(self.IMAGEHEIGHT__FIELD_NAME.field_name, value)

    def get_ImageHeight_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ImageHeight' from this record model
        """
        return self.get_field_value(self.IMAGEHEIGHT__FIELD_NAME.field_name)

    def set_ImageWidth_field(self, value: Optional[str]):
        """
        Set data field with field name 'ImageWidth' on this record model
        """
        self.set_field_value(self.IMAGEWIDTH__FIELD_NAME.field_name, value)

    def get_ImageWidth_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ImageWidth' from this record model
        """
        return self.get_field_value(self.IMAGEWIDTH__FIELD_NAME.field_name)

    def set_IndexQuantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'IndexQuantity' on this record model
        """
        self.set_field_value(self.INDEXQUANTITY__FIELD_NAME.field_name, value)

    def get_IndexQuantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'IndexQuantity' from this record model
        """
        return self.get_field_value(self.INDEXQUANTITY__FIELD_NAME.field_name)

    def set_IndexRead_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexRead' on this record model
        """
        self.set_field_value(self.INDEXREAD__FIELD_NAME.field_name, value)

    def get_IndexRead_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexRead' from this record model
        """
        return self.get_field_value(self.INDEXREAD__FIELD_NAME.field_name)

    def set_IndexSerialNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexSerialNumber' on this record model
        """
        self.set_field_value(self.INDEXSERIALNUMBER__FIELD_NAME.field_name, value)

    def get_IndexSerialNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexSerialNumber' from this record model
        """
        return self.get_field_value(self.INDEXSERIALNUMBER__FIELD_NAME.field_name)

    def set_IntensityCeiling_field(self, value: Optional[str]):
        """
        Set data field with field name 'IntensityCeiling' on this record model
        """
        self.set_field_value(self.INTENSITYCEILING__FIELD_NAME.field_name, value)

    def get_IntensityCeiling_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IntensityCeiling' from this record model
        """
        return self.get_field_value(self.INTENSITYCEILING__FIELD_NAME.field_name)

    def set_IsNew50Cycle_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsNew50Cycle' on this record model
        """
        self.set_field_value(self.ISNEW50CYCLE__FIELD_NAME.field_name, value)

    def get_IsNew50Cycle_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsNew50Cycle' from this record model
        """
        return self.get_field_value(self.ISNEW50CYCLE__FIELD_NAME.field_name)

    def set_IsNew200Cycle_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsNew200Cycle' on this record model
        """
        self.set_field_value(self.ISNEW200CYCLE__FIELD_NAME.field_name, value)

    def get_IsNew200Cycle_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsNew200Cycle' from this record model
        """
        return self.get_field_value(self.ISNEW200CYCLE__FIELD_NAME.field_name)

    def set_KeepIntensityFiles_field(self, value: Optional[str]):
        """
        Set data field with field name 'KeepIntensityFiles' on this record model
        """
        self.set_field_value(self.KEEPINTENSITYFILES__FIELD_NAME.field_name, value)

    def get_KeepIntensityFiles_field(self) -> Optional[str]:
        """
        Get data field value with field name 'KeepIntensityFiles' from this record model
        """
        return self.get_field_value(self.KEEPINTENSITYFILES__FIELD_NAME.field_name)

    def set_LaneLength_field(self, value: Optional[str]):
        """
        Set data field with field name 'LaneLength' on this record model
        """
        self.set_field_value(self.LANELENGTH__FIELD_NAME.field_name, value)

    def get_LaneLength_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LaneLength' from this record model
        """
        return self.get_field_value(self.LANELENGTH__FIELD_NAME.field_name)

    def set_MaxInitialZJumpHalfUm_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaxInitialZJumpHalfUm' on this record model
        """
        self.set_field_value(self.MAXINITIALZJUMPHALFUM__FIELD_NAME.field_name, value)

    def get_MaxInitialZJumpHalfUm_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaxInitialZJumpHalfUm' from this record model
        """
        return self.get_field_value(self.MAXINITIALZJUMPHALFUM__FIELD_NAME.field_name)

    def set_MaxSubsequentZJumpHalfUm_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaxSubsequentZJumpHalfUm' on this record model
        """
        self.set_field_value(self.MAXSUBSEQUENTZJUMPHALFUM__FIELD_NAME.field_name, value)

    def get_MaxSubsequentZJumpHalfUm_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaxSubsequentZJumpHalfUm' from this record model
        """
        return self.get_field_value(self.MAXSUBSEQUENTZJUMPHALFUM__FIELD_NAME.field_name)

    def set_MockRun_field(self, value: Optional[bool]):
        """
        Set data field with field name 'MockRun' on this record model
        """
        self.set_field_value(self.MOCKRUN__FIELD_NAME.field_name, value)

    def get_MockRun_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'MockRun' from this record model
        """
        return self.get_field_value(self.MOCKRUN__FIELD_NAME.field_name)

    def set_MotorDelayFrames_field(self, value: Optional[str]):
        """
        Set data field with field name 'MotorDelayFrames' on this record model
        """
        self.set_field_value(self.MOTORDELAYFRAMES__FIELD_NAME.field_name, value)

    def get_MotorDelayFrames_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MotorDelayFrames' from this record model
        """
        return self.get_field_value(self.MOTORDELAYFRAMES__FIELD_NAME.field_name)

    def set_NumAnalysisThreads_field(self, value: Optional[str]):
        """
        Set data field with field name 'NumAnalysisThreads' on this record model
        """
        self.set_field_value(self.NUMANALYSISTHREADS__FIELD_NAME.field_name, value)

    def get_NumAnalysisThreads_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NumAnalysisThreads' from this record model
        """
        return self.get_field_value(self.NUMANALYSISTHREADS__FIELD_NAME.field_name)

    def set_NumberCyclesRemaining_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumberCyclesRemaining' on this record model
        """
        self.set_field_value(self.NUMBERCYCLESREMAINING__FIELD_NAME.field_name, value)

    def get_NumberCyclesRemaining_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumberCyclesRemaining' from this record model
        """
        return self.get_field_value(self.NUMBERCYCLESREMAINING__FIELD_NAME.field_name)

    def set_NumberOfInitialZJumps_field(self, value: Optional[str]):
        """
        Set data field with field name 'NumberOfInitialZJumps' on this record model
        """
        self.set_field_value(self.NUMBEROFINITIALZJUMPS__FIELD_NAME.field_name, value)

    def get_NumberOfInitialZJumps_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NumberOfInitialZJumps' from this record model
        """
        return self.get_field_value(self.NUMBEROFINITIALZJUMPS__FIELD_NAME.field_name)

    def set_NumSwaths_field(self, value: Optional[str]):
        """
        Set data field with field name 'NumSwaths' on this record model
        """
        self.set_field_value(self.NUMSWATHS__FIELD_NAME.field_name, value)

    def get_NumSwaths_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NumSwaths' from this record model
        """
        return self.get_field_value(self.NUMSWATHS__FIELD_NAME.field_name)

    def set_NumTilesPerSwath_field(self, value: Optional[str]):
        """
        Set data field with field name 'NumTilesPerSwath' on this record model
        """
        self.set_field_value(self.NUMTILESPERSWATH__FIELD_NAME.field_name, value)

    def get_NumTilesPerSwath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NumTilesPerSwath' from this record model
        """
        return self.get_field_value(self.NUMTILESPERSWATH__FIELD_NAME.field_name)

    def set_Offset_field(self, value: Optional[str]):
        """
        Set data field with field name 'Offset' on this record model
        """
        self.set_field_value(self.OFFSET__FIELD_NAME.field_name, value)

    def get_Offset_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Offset' from this record model
        """
        return self.get_field_value(self.OFFSET__FIELD_NAME.field_name)

    def set_OutputFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'OutputFolder' on this record model
        """
        self.set_field_value(self.OUTPUTFOLDER__FIELD_NAME.field_name, value)

    def get_OutputFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OutputFolder' from this record model
        """
        return self.get_field_value(self.OUTPUTFOLDER__FIELD_NAME.field_name)

    def set_PeQuantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'PeQuantity' on this record model
        """
        self.set_field_value(self.PEQUANTITY__FIELD_NAME.field_name, value)

    def get_PeQuantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PeQuantity' from this record model
        """
        return self.get_field_value(self.PEQUANTITY__FIELD_NAME.field_name)

    def set_PerformPreRunFluidicsCheck_field(self, value: Optional[bool]):
        """
        Set data field with field name 'PerformPreRunFluidicsCheck' on this record model
        """
        self.set_field_value(self.PERFORMPRERUNFLUIDICSCHECK__FIELD_NAME.field_name, value)

    def get_PerformPreRunFluidicsCheck_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'PerformPreRunFluidicsCheck' from this record model
        """
        return self.get_field_value(self.PERFORMPRERUNFLUIDICSCHECK__FIELD_NAME.field_name)

    def set_PeriodicSave_field(self, value: Optional[str]):
        """
        Set data field with field name 'PeriodicSave' on this record model
        """
        self.set_field_value(self.PERIODICSAVE__FIELD_NAME.field_name, value)

    def get_PeriodicSave_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PeriodicSave' from this record model
        """
        return self.get_field_value(self.PERIODICSAVE__FIELD_NAME.field_name)

    def set_PeSerialNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PeSerialNumber' on this record model
        """
        self.set_field_value(self.PESERIALNUMBER__FIELD_NAME.field_name, value)

    def get_PeSerialNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PeSerialNumber' from this record model
        """
        return self.get_field_value(self.PESERIALNUMBER__FIELD_NAME.field_name)

    def set_Prime_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Prime' on this record model
        """
        self.set_field_value(self.PRIME__FIELD_NAME.field_name, value)

    def get_Prime_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Prime' from this record model
        """
        return self.get_field_value(self.PRIME__FIELD_NAME.field_name)

    def set_PromptForPeReagents_field(self, value: Optional[bool]):
        """
        Set data field with field name 'PromptForPeReagents' on this record model
        """
        self.set_field_value(self.PROMPTFORPEREAGENTS__FIELD_NAME.field_name, value)

    def get_PromptForPeReagents_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'PromptForPeReagents' from this record model
        """
        return self.get_field_value(self.PROMPTFORPEREAGENTS__FIELD_NAME.field_name)

    def set_Read1_field(self, value: Optional[str]):
        """
        Set data field with field name 'Read1' on this record model
        """
        self.set_field_value(self.READ1__FIELD_NAME.field_name, value)

    def get_Read1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Read1' from this record model
        """
        return self.get_field_value(self.READ1__FIELD_NAME.field_name)

    def set_Read2_field(self, value: Optional[str]):
        """
        Set data field with field name 'Read2' on this record model
        """
        self.set_field_value(self.READ2__FIELD_NAME.field_name, value)

    def get_Read2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Read2' from this record model
        """
        return self.get_field_value(self.READ2__FIELD_NAME.field_name)

    def set_RecipeFragmentVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecipeFragmentVersion' on this record model
        """
        self.set_field_value(self.RECIPEFRAGMENTVERSION__FIELD_NAME.field_name, value)

    def get_RecipeFragmentVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecipeFragmentVersion' from this record model
        """
        return self.get_field_value(self.RECIPEFRAGMENTVERSION__FIELD_NAME.field_name)

    def set_Rehyb_field(self, value: Optional[str]):
        """
        Set data field with field name 'Rehyb' on this record model
        """
        self.set_field_value(self.REHYB__FIELD_NAME.field_name, value)

    def get_Rehyb_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Rehyb' from this record model
        """
        return self.get_field_value(self.REHYB__FIELD_NAME.field_name)

    def set_Resume_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Resume' on this record model
        """
        self.set_field_value(self.RESUME__FIELD_NAME.field_name, value)

    def get_Resume_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Resume' from this record model
        """
        return self.get_field_value(self.RESUME__FIELD_NAME.field_name)

    def set_ResumeCycle_field(self, value: Optional[str]):
        """
        Set data field with field name 'ResumeCycle' on this record model
        """
        self.set_field_value(self.RESUMECYCLE__FIELD_NAME.field_name, value)

    def get_ResumeCycle_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ResumeCycle' from this record model
        """
        return self.get_field_value(self.RESUMECYCLE__FIELD_NAME.field_name)

    def set_RTAVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'RTAVersion' on this record model
        """
        self.set_field_value(self.RTAVERSION__FIELD_NAME.field_name, value)

    def get_RTAVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RTAVersion' from this record model
        """
        return self.get_field_value(self.RTAVERSION__FIELD_NAME.field_name)

    def set_RunID_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunID' on this record model
        """
        self.set_field_value(self.RUNID__FIELD_NAME.field_name, value)

    def get_RunID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunID' from this record model
        """
        return self.get_field_value(self.RUNID__FIELD_NAME.field_name)

    def set_RunMode_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunMode' on this record model
        """
        self.set_field_value(self.RUNMODE__FIELD_NAME.field_name, value)

    def get_RunMode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunMode' from this record model
        """
        return self.get_field_value(self.RUNMODE__FIELD_NAME.field_name)

    def set_RunStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunStartDate' on this record model
        """
        self.set_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name, value)

    def get_RunStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunStartDate' from this record model
        """
        return self.get_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name)

    def set_SampleSheet_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleSheet' on this record model
        """
        self.set_field_value(self.SAMPLESHEET__FIELD_NAME.field_name, value)

    def get_SampleSheet_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleSheet' from this record model
        """
        return self.get_field_value(self.SAMPLESHEET__FIELD_NAME.field_name)

    def set_SbsQuantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'SbsQuantity' on this record model
        """
        self.set_field_value(self.SBSQUANTITY__FIELD_NAME.field_name, value)

    def get_SbsQuantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'SbsQuantity' from this record model
        """
        return self.get_field_value(self.SBSQUANTITY__FIELD_NAME.field_name)

    def set_SbsSerialNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'SbsSerialNumber' on this record model
        """
        self.set_field_value(self.SBSSERIALNUMBER__FIELD_NAME.field_name, value)

    def get_SbsSerialNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SbsSerialNumber' from this record model
        """
        return self.get_field_value(self.SBSSERIALNUMBER__FIELD_NAME.field_name)

    def set_ScanID_field(self, value: Optional[str]):
        """
        Set data field with field name 'ScanID' on this record model
        """
        self.set_field_value(self.SCANID__FIELD_NAME.field_name, value)

    def get_ScanID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ScanID' from this record model
        """
        return self.get_field_value(self.SCANID__FIELD_NAME.field_name)

    def set_ScannerID_field(self, value: Optional[str]):
        """
        Set data field with field name 'ScannerID' on this record model
        """
        self.set_field_value(self.SCANNERID__FIELD_NAME.field_name, value)

    def get_ScannerID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ScannerID' from this record model
        """
        return self.get_field_value(self.SCANNERID__FIELD_NAME.field_name)

    def set_ScanNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'ScanNumber' on this record model
        """
        self.set_field_value(self.SCANNUMBER__FIELD_NAME.field_name, value)

    def get_ScanNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ScanNumber' from this record model
        """
        return self.get_field_value(self.SCANNUMBER__FIELD_NAME.field_name)

    def set_SelectedSection_1_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_1' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_1__FIELD_NAME.field_name, value)

    def get_SelectedSection_1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_1' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_1__FIELD_NAME.field_name)

    def set_SelectedSection_2_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_2' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_2__FIELD_NAME.field_name, value)

    def get_SelectedSection_2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_2' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_2__FIELD_NAME.field_name)

    def set_SelectedSection_3_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_3' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_3__FIELD_NAME.field_name, value)

    def get_SelectedSection_3_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_3' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_3__FIELD_NAME.field_name)

    def set_SelectedSection_4_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_4' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_4__FIELD_NAME.field_name, value)

    def get_SelectedSection_4_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_4' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_4__FIELD_NAME.field_name)

    def set_SelectedSection_5_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_5' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_5__FIELD_NAME.field_name, value)

    def get_SelectedSection_5_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_5' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_5__FIELD_NAME.field_name)

    def set_SelectedSection_6_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_6' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_6__FIELD_NAME.field_name, value)

    def get_SelectedSection_6_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_6' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_6__FIELD_NAME.field_name)

    def set_SelectedSection_7_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_7' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_7__FIELD_NAME.field_name, value)

    def get_SelectedSection_7_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_7' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_7__FIELD_NAME.field_name)

    def set_SelectedSection_8_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSection_8' on this record model
        """
        self.set_field_value(self.SELECTEDSECTION_8__FIELD_NAME.field_name, value)

    def get_SelectedSection_8_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSection_8' from this record model
        """
        return self.get_field_value(self.SELECTEDSECTION_8__FIELD_NAME.field_name)

    def set_SelectedSurface_field(self, value: Optional[str]):
        """
        Set data field with field name 'SelectedSurface' on this record model
        """
        self.set_field_value(self.SELECTEDSURFACE__FIELD_NAME.field_name, value)

    def get_SelectedSurface_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SelectedSurface' from this record model
        """
        return self.get_field_value(self.SELECTEDSURFACE__FIELD_NAME.field_name)

    def set_SlideHolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'SlideHolder' on this record model
        """
        self.set_field_value(self.SLIDEHOLDER__FIELD_NAME.field_name, value)

    def get_SlideHolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SlideHolder' from this record model
        """
        return self.get_field_value(self.SLIDEHOLDER__FIELD_NAME.field_name)

    def set_SupportMultipleSurfacesInUI_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SupportMultipleSurfacesInUI' on this record model
        """
        self.set_field_value(self.SUPPORTMULTIPLESURFACESINUI__FIELD_NAME.field_name, value)

    def get_SupportMultipleSurfacesInUI_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SupportMultipleSurfacesInUI' from this record model
        """
        return self.get_field_value(self.SUPPORTMULTIPLESURFACESINUI__FIELD_NAME.field_name)

    def set_SwathScanMode_field(self, value: Optional[str]):
        """
        Set data field with field name 'SwathScanMode' on this record model
        """
        self.set_field_value(self.SWATHSCANMODE__FIELD_NAME.field_name, value)

    def get_SwathScanMode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SwathScanMode' from this record model
        """
        return self.get_field_value(self.SWATHSCANMODE__FIELD_NAME.field_name)

    def set_TempFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'TempFolder' on this record model
        """
        self.set_field_value(self.TEMPFOLDER__FIELD_NAME.field_name, value)

    def get_TempFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TempFolder' from this record model
        """
        return self.get_field_value(self.TEMPFOLDER__FIELD_NAME.field_name)

    def set_TemplateCycleCount_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateCycleCount' on this record model
        """
        self.set_field_value(self.TEMPLATECYCLECOUNT__FIELD_NAME.field_name, value)

    def get_TemplateCycleCount_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateCycleCount' from this record model
        """
        return self.get_field_value(self.TEMPLATECYCLECOUNT__FIELD_NAME.field_name)

    def set_TileHeight_field(self, value: Optional[str]):
        """
        Set data field with field name 'TileHeight' on this record model
        """
        self.set_field_value(self.TILEHEIGHT__FIELD_NAME.field_name, value)

    def get_TileHeight_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TileHeight' from this record model
        """
        return self.get_field_value(self.TILEHEIGHT__FIELD_NAME.field_name)

    def set_TileWidth_field(self, value: Optional[str]):
        """
        Set data field with field name 'TileWidth' on this record model
        """
        self.set_field_value(self.TILEWIDTH__FIELD_NAME.field_name, value)

    def get_TileWidth_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TileWidth' from this record model
        """
        return self.get_field_value(self.TILEWIDTH__FIELD_NAME.field_name)

    def set_UseExistingRecipe_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UseExistingRecipe' on this record model
        """
        self.set_field_value(self.USEEXISTINGRECIPE__FIELD_NAME.field_name, value)

    def get_UseExistingRecipe_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UseExistingRecipe' from this record model
        """
        return self.get_field_value(self.USEEXISTINGRECIPE__FIELD_NAME.field_name)

    def set_Username_field(self, value: Optional[str]):
        """
        Set data field with field name 'Username' on this record model
        """
        self.set_field_value(self.USERNAME__FIELD_NAME.field_name, value)

    def get_Username_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Username' from this record model
        """
        return self.get_field_value(self.USERNAME__FIELD_NAME.field_name)

    def set_WorkFlowType_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkFlowType' on this record model
        """
        self.set_field_value(self.WORKFLOWTYPE__FIELD_NAME.field_name, value)

    def get_WorkFlowType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkFlowType' from this record model
        """
        return self.get_field_value(self.WORKFLOWTYPE__FIELD_NAME.field_name)


class IlluminaMiSeqRunParametersModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaMiSeqRunParameters
    Data Type Display Name: Illumina MiSeq Run Parameters (Illumina MiSeq Run Parameters')
    Fields: AfterRunWashMethod, AnalysisFolder, ApplicationName, ApplicationVersion, Chemistry, CloudRunId, CloudUsername, CopyManifests, EnableAnalysis, EnableCloud, ExperimentName, FlowcellExpirationDate, FlowcellPartNumber, FlowcellSerialNumber, FocusMethod, FPGAVersion, ILMNOnlyRecipeFolder, ManifestFolder, MCSVersion, MostRecentWashType, NumLanes, NumSwaths, NumTilesPerSwath, OutputFolder, PR2BottleExpirationDate, PR2BottlePartNumber, PR2BottleSerialNumber, ReagentKitExpirationDate, ReagentKitPartNumber, ReagentKitSerialNumber, ReagentKitVersion, RecipeFolder, Resumable, RTAVersion, RunID, RunNumber, RunStartDate, SampleSheetFolder, SampleSheetName, SaveFocusImages, SaveScanImages, ScannerID, SendInstrumentHealthToILMN, SupportMultipleSurfacesInUI, SurfaceToScan, TempFolder, Username
     <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'IlluminaMiSeqRunParameters'
    AFTERRUNWASHMETHOD__FIELD_NAME: WrapperField = WrapperField("AfterRunWashMethod", FieldType.STRING)
    ANALYSISFOLDER__FIELD_NAME: WrapperField = WrapperField("AnalysisFolder", FieldType.STRING)
    APPLICATIONNAME__FIELD_NAME: WrapperField = WrapperField("ApplicationName", FieldType.STRING)
    APPLICATIONVERSION__FIELD_NAME: WrapperField = WrapperField("ApplicationVersion", FieldType.STRING)
    CHEMISTRY__FIELD_NAME: WrapperField = WrapperField("Chemistry", FieldType.STRING)
    CLOUDRUNID__FIELD_NAME: WrapperField = WrapperField("CloudRunId", FieldType.STRING)
    CLOUDUSERNAME__FIELD_NAME: WrapperField = WrapperField("CloudUsername", FieldType.STRING)
    COPYMANIFESTS__FIELD_NAME: WrapperField = WrapperField("CopyManifests", FieldType.BOOLEAN)
    ENABLEANALYSIS__FIELD_NAME: WrapperField = WrapperField("EnableAnalysis", FieldType.BOOLEAN)
    ENABLECLOUD__FIELD_NAME: WrapperField = WrapperField("EnableCloud", FieldType.BOOLEAN)
    EXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("ExperimentName", FieldType.STRING)
    FLOWCELLEXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("FlowcellExpirationDate", FieldType.STRING)
    FLOWCELLPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("FlowcellPartNumber", FieldType.STRING)
    FLOWCELLSERIALNUMBER__FIELD_NAME: WrapperField = WrapperField("FlowcellSerialNumber", FieldType.STRING)
    FOCUSMETHOD__FIELD_NAME: WrapperField = WrapperField("FocusMethod", FieldType.STRING)
    FPGAVERSION__FIELD_NAME: WrapperField = WrapperField("FPGAVersion", FieldType.STRING)
    ILMNONLYRECIPEFOLDER__FIELD_NAME: WrapperField = WrapperField("ILMNOnlyRecipeFolder", FieldType.STRING)
    MANIFESTFOLDER__FIELD_NAME: WrapperField = WrapperField("ManifestFolder", FieldType.STRING)
    MCSVERSION__FIELD_NAME: WrapperField = WrapperField("MCSVersion", FieldType.STRING)
    MOSTRECENTWASHTYPE__FIELD_NAME: WrapperField = WrapperField("MostRecentWashType", FieldType.STRING)
    NUMLANES__FIELD_NAME: WrapperField = WrapperField("NumLanes", FieldType.LONG)
    NUMSWATHS__FIELD_NAME: WrapperField = WrapperField("NumSwaths", FieldType.LONG)
    NUMTILESPERSWATH__FIELD_NAME: WrapperField = WrapperField("NumTilesPerSwath", FieldType.LONG)
    OUTPUTFOLDER__FIELD_NAME: WrapperField = WrapperField("OutputFolder", FieldType.STRING)
    PR2BOTTLEEXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("PR2BottleExpirationDate", FieldType.STRING)
    PR2BOTTLEPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("PR2BottlePartNumber", FieldType.STRING)
    PR2BOTTLESERIALNUMBER__FIELD_NAME: WrapperField = WrapperField("PR2BottleSerialNumber", FieldType.STRING)
    REAGENTKITEXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("ReagentKitExpirationDate", FieldType.STRING)
    REAGENTKITPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("ReagentKitPartNumber", FieldType.STRING)
    REAGENTKITSERIALNUMBER__FIELD_NAME: WrapperField = WrapperField("ReagentKitSerialNumber", FieldType.STRING)
    REAGENTKITVERSION__FIELD_NAME: WrapperField = WrapperField("ReagentKitVersion", FieldType.STRING)
    RECIPEFOLDER__FIELD_NAME: WrapperField = WrapperField("RecipeFolder", FieldType.STRING)
    RESUMABLE__FIELD_NAME: WrapperField = WrapperField("Resumable", FieldType.BOOLEAN)
    RTAVERSION__FIELD_NAME: WrapperField = WrapperField("RTAVersion", FieldType.STRING)
    RUNID__FIELD_NAME: WrapperField = WrapperField("RunID", FieldType.STRING)
    RUNNUMBER__FIELD_NAME: WrapperField = WrapperField("RunNumber", FieldType.LONG)
    RUNSTARTDATE__FIELD_NAME: WrapperField = WrapperField("RunStartDate", FieldType.DATE)
    SAMPLESHEETFOLDER__FIELD_NAME: WrapperField = WrapperField("SampleSheetFolder", FieldType.STRING)
    SAMPLESHEETNAME__FIELD_NAME: WrapperField = WrapperField("SampleSheetName", FieldType.STRING)
    SAVEFOCUSIMAGES__FIELD_NAME: WrapperField = WrapperField("SaveFocusImages", FieldType.BOOLEAN)
    SAVESCANIMAGES__FIELD_NAME: WrapperField = WrapperField("SaveScanImages", FieldType.BOOLEAN)
    SCANNERID__FIELD_NAME: WrapperField = WrapperField("ScannerID", FieldType.STRING)
    SENDINSTRUMENTHEALTHTOILMN__FIELD_NAME: WrapperField = WrapperField("SendInstrumentHealthToILMN", FieldType.BOOLEAN)
    SUPPORTMULTIPLESURFACESINUI__FIELD_NAME: WrapperField = WrapperField("SupportMultipleSurfacesInUI", FieldType.BOOLEAN)
    SURFACETOSCAN__FIELD_NAME: WrapperField = WrapperField("SurfaceToScan", FieldType.STRING)
    TEMPFOLDER__FIELD_NAME: WrapperField = WrapperField("TempFolder", FieldType.STRING)
    USERNAME__FIELD_NAME: WrapperField = WrapperField("Username", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AfterRunWashMethod_field(self, value: Optional[str]):
        """
        Set data field with field name 'AfterRunWashMethod' on this record model
        """
        self.set_field_value(self.AFTERRUNWASHMETHOD__FIELD_NAME.field_name, value)

    def get_AfterRunWashMethod_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AfterRunWashMethod' from this record model
        """
        return self.get_field_value(self.AFTERRUNWASHMETHOD__FIELD_NAME.field_name)

    def set_AnalysisFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'AnalysisFolder' on this record model
        """
        self.set_field_value(self.ANALYSISFOLDER__FIELD_NAME.field_name, value)

    def get_AnalysisFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AnalysisFolder' from this record model
        """
        return self.get_field_value(self.ANALYSISFOLDER__FIELD_NAME.field_name)

    def set_ApplicationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApplicationName' on this record model
        """
        self.set_field_value(self.APPLICATIONNAME__FIELD_NAME.field_name, value)

    def get_ApplicationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApplicationName' from this record model
        """
        return self.get_field_value(self.APPLICATIONNAME__FIELD_NAME.field_name)

    def set_ApplicationVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApplicationVersion' on this record model
        """
        self.set_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name, value)

    def get_ApplicationVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApplicationVersion' from this record model
        """
        return self.get_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name)

    def set_Chemistry_field(self, value: Optional[str]):
        """
        Set data field with field name 'Chemistry' on this record model
        """
        self.set_field_value(self.CHEMISTRY__FIELD_NAME.field_name, value)

    def get_Chemistry_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Chemistry' from this record model
        """
        return self.get_field_value(self.CHEMISTRY__FIELD_NAME.field_name)

    def set_CloudRunId_field(self, value: Optional[str]):
        """
        Set data field with field name 'CloudRunId' on this record model
        """
        self.set_field_value(self.CLOUDRUNID__FIELD_NAME.field_name, value)

    def get_CloudRunId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CloudRunId' from this record model
        """
        return self.get_field_value(self.CLOUDRUNID__FIELD_NAME.field_name)

    def set_CloudUsername_field(self, value: Optional[str]):
        """
        Set data field with field name 'CloudUsername' on this record model
        """
        self.set_field_value(self.CLOUDUSERNAME__FIELD_NAME.field_name, value)

    def get_CloudUsername_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CloudUsername' from this record model
        """
        return self.get_field_value(self.CLOUDUSERNAME__FIELD_NAME.field_name)

    def set_CopyManifests_field(self, value: Optional[bool]):
        """
        Set data field with field name 'CopyManifests' on this record model
        """
        self.set_field_value(self.COPYMANIFESTS__FIELD_NAME.field_name, value)

    def get_CopyManifests_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'CopyManifests' from this record model
        """
        return self.get_field_value(self.COPYMANIFESTS__FIELD_NAME.field_name)

    def set_EnableAnalysis_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableAnalysis' on this record model
        """
        self.set_field_value(self.ENABLEANALYSIS__FIELD_NAME.field_name, value)

    def get_EnableAnalysis_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableAnalysis' from this record model
        """
        return self.get_field_value(self.ENABLEANALYSIS__FIELD_NAME.field_name)

    def set_EnableCloud_field(self, value: Optional[bool]):
        """
        Set data field with field name 'EnableCloud' on this record model
        """
        self.set_field_value(self.ENABLECLOUD__FIELD_NAME.field_name, value)

    def get_EnableCloud_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'EnableCloud' from this record model
        """
        return self.get_field_value(self.ENABLECLOUD__FIELD_NAME.field_name)

    def set_ExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentName' on this record model
        """
        self.set_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_ExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentName' from this record model
        """
        return self.get_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name)

    def set_FlowcellExpirationDate_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowcellExpirationDate' on this record model
        """
        self.set_field_value(self.FLOWCELLEXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_FlowcellExpirationDate_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowcellExpirationDate' from this record model
        """
        return self.get_field_value(self.FLOWCELLEXPIRATIONDATE__FIELD_NAME.field_name)

    def set_FlowcellPartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowcellPartNumber' on this record model
        """
        self.set_field_value(self.FLOWCELLPARTNUMBER__FIELD_NAME.field_name, value)

    def get_FlowcellPartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowcellPartNumber' from this record model
        """
        return self.get_field_value(self.FLOWCELLPARTNUMBER__FIELD_NAME.field_name)

    def set_FlowcellSerialNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowcellSerialNumber' on this record model
        """
        self.set_field_value(self.FLOWCELLSERIALNUMBER__FIELD_NAME.field_name, value)

    def get_FlowcellSerialNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowcellSerialNumber' from this record model
        """
        return self.get_field_value(self.FLOWCELLSERIALNUMBER__FIELD_NAME.field_name)

    def set_FocusMethod_field(self, value: Optional[str]):
        """
        Set data field with field name 'FocusMethod' on this record model
        """
        self.set_field_value(self.FOCUSMETHOD__FIELD_NAME.field_name, value)

    def get_FocusMethod_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FocusMethod' from this record model
        """
        return self.get_field_value(self.FOCUSMETHOD__FIELD_NAME.field_name)

    def set_FPGAVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'FPGAVersion' on this record model
        """
        self.set_field_value(self.FPGAVERSION__FIELD_NAME.field_name, value)

    def get_FPGAVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FPGAVersion' from this record model
        """
        return self.get_field_value(self.FPGAVERSION__FIELD_NAME.field_name)

    def set_ILMNOnlyRecipeFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'ILMNOnlyRecipeFolder' on this record model
        """
        self.set_field_value(self.ILMNONLYRECIPEFOLDER__FIELD_NAME.field_name, value)

    def get_ILMNOnlyRecipeFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ILMNOnlyRecipeFolder' from this record model
        """
        return self.get_field_value(self.ILMNONLYRECIPEFOLDER__FIELD_NAME.field_name)

    def set_ManifestFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'ManifestFolder' on this record model
        """
        self.set_field_value(self.MANIFESTFOLDER__FIELD_NAME.field_name, value)

    def get_ManifestFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ManifestFolder' from this record model
        """
        return self.get_field_value(self.MANIFESTFOLDER__FIELD_NAME.field_name)

    def set_MCSVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'MCSVersion' on this record model
        """
        self.set_field_value(self.MCSVERSION__FIELD_NAME.field_name, value)

    def get_MCSVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MCSVersion' from this record model
        """
        return self.get_field_value(self.MCSVERSION__FIELD_NAME.field_name)

    def set_MostRecentWashType_field(self, value: Optional[str]):
        """
        Set data field with field name 'MostRecentWashType' on this record model
        """
        self.set_field_value(self.MOSTRECENTWASHTYPE__FIELD_NAME.field_name, value)

    def get_MostRecentWashType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MostRecentWashType' from this record model
        """
        return self.get_field_value(self.MOSTRECENTWASHTYPE__FIELD_NAME.field_name)

    def set_NumLanes_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumLanes' on this record model
        """
        self.set_field_value(self.NUMLANES__FIELD_NAME.field_name, value)

    def get_NumLanes_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumLanes' from this record model
        """
        return self.get_field_value(self.NUMLANES__FIELD_NAME.field_name)

    def set_NumSwaths_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumSwaths' on this record model
        """
        self.set_field_value(self.NUMSWATHS__FIELD_NAME.field_name, value)

    def get_NumSwaths_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumSwaths' from this record model
        """
        return self.get_field_value(self.NUMSWATHS__FIELD_NAME.field_name)

    def set_NumTilesPerSwath_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumTilesPerSwath' on this record model
        """
        self.set_field_value(self.NUMTILESPERSWATH__FIELD_NAME.field_name, value)

    def get_NumTilesPerSwath_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumTilesPerSwath' from this record model
        """
        return self.get_field_value(self.NUMTILESPERSWATH__FIELD_NAME.field_name)

    def set_OutputFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'OutputFolder' on this record model
        """
        self.set_field_value(self.OUTPUTFOLDER__FIELD_NAME.field_name, value)

    def get_OutputFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OutputFolder' from this record model
        """
        return self.get_field_value(self.OUTPUTFOLDER__FIELD_NAME.field_name)

    def set_PR2BottleExpirationDate_field(self, value: Optional[str]):
        """
        Set data field with field name 'PR2BottleExpirationDate' on this record model
        """
        self.set_field_value(self.PR2BOTTLEEXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_PR2BottleExpirationDate_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PR2BottleExpirationDate' from this record model
        """
        return self.get_field_value(self.PR2BOTTLEEXPIRATIONDATE__FIELD_NAME.field_name)

    def set_PR2BottlePartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PR2BottlePartNumber' on this record model
        """
        self.set_field_value(self.PR2BOTTLEPARTNUMBER__FIELD_NAME.field_name, value)

    def get_PR2BottlePartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PR2BottlePartNumber' from this record model
        """
        return self.get_field_value(self.PR2BOTTLEPARTNUMBER__FIELD_NAME.field_name)

    def set_PR2BottleSerialNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PR2BottleSerialNumber' on this record model
        """
        self.set_field_value(self.PR2BOTTLESERIALNUMBER__FIELD_NAME.field_name, value)

    def get_PR2BottleSerialNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PR2BottleSerialNumber' from this record model
        """
        return self.get_field_value(self.PR2BOTTLESERIALNUMBER__FIELD_NAME.field_name)

    def set_ReagentKitExpirationDate_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentKitExpirationDate' on this record model
        """
        self.set_field_value(self.REAGENTKITEXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_ReagentKitExpirationDate_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentKitExpirationDate' from this record model
        """
        return self.get_field_value(self.REAGENTKITEXPIRATIONDATE__FIELD_NAME.field_name)

    def set_ReagentKitPartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentKitPartNumber' on this record model
        """
        self.set_field_value(self.REAGENTKITPARTNUMBER__FIELD_NAME.field_name, value)

    def get_ReagentKitPartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentKitPartNumber' from this record model
        """
        return self.get_field_value(self.REAGENTKITPARTNUMBER__FIELD_NAME.field_name)

    def set_ReagentKitSerialNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentKitSerialNumber' on this record model
        """
        self.set_field_value(self.REAGENTKITSERIALNUMBER__FIELD_NAME.field_name, value)

    def get_ReagentKitSerialNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentKitSerialNumber' from this record model
        """
        return self.get_field_value(self.REAGENTKITSERIALNUMBER__FIELD_NAME.field_name)

    def set_ReagentKitVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentKitVersion' on this record model
        """
        self.set_field_value(self.REAGENTKITVERSION__FIELD_NAME.field_name, value)

    def get_ReagentKitVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentKitVersion' from this record model
        """
        return self.get_field_value(self.REAGENTKITVERSION__FIELD_NAME.field_name)

    def set_RecipeFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecipeFolder' on this record model
        """
        self.set_field_value(self.RECIPEFOLDER__FIELD_NAME.field_name, value)

    def get_RecipeFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecipeFolder' from this record model
        """
        return self.get_field_value(self.RECIPEFOLDER__FIELD_NAME.field_name)

    def set_Resumable_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Resumable' on this record model
        """
        self.set_field_value(self.RESUMABLE__FIELD_NAME.field_name, value)

    def get_Resumable_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Resumable' from this record model
        """
        return self.get_field_value(self.RESUMABLE__FIELD_NAME.field_name)

    def set_RTAVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'RTAVersion' on this record model
        """
        self.set_field_value(self.RTAVERSION__FIELD_NAME.field_name, value)

    def get_RTAVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RTAVersion' from this record model
        """
        return self.get_field_value(self.RTAVERSION__FIELD_NAME.field_name)

    def set_RunID_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunID' on this record model
        """
        self.set_field_value(self.RUNID__FIELD_NAME.field_name, value)

    def get_RunID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunID' from this record model
        """
        return self.get_field_value(self.RUNID__FIELD_NAME.field_name)

    def set_RunNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunNumber' on this record model
        """
        self.set_field_value(self.RUNNUMBER__FIELD_NAME.field_name, value)

    def get_RunNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunNumber' from this record model
        """
        return self.get_field_value(self.RUNNUMBER__FIELD_NAME.field_name)

    def set_RunStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunStartDate' on this record model
        """
        self.set_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name, value)

    def get_RunStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunStartDate' from this record model
        """
        return self.get_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name)

    def set_SampleSheetFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleSheetFolder' on this record model
        """
        self.set_field_value(self.SAMPLESHEETFOLDER__FIELD_NAME.field_name, value)

    def get_SampleSheetFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleSheetFolder' from this record model
        """
        return self.get_field_value(self.SAMPLESHEETFOLDER__FIELD_NAME.field_name)

    def set_SampleSheetName_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleSheetName' on this record model
        """
        self.set_field_value(self.SAMPLESHEETNAME__FIELD_NAME.field_name, value)

    def get_SampleSheetName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleSheetName' from this record model
        """
        return self.get_field_value(self.SAMPLESHEETNAME__FIELD_NAME.field_name)

    def set_SaveFocusImages_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SaveFocusImages' on this record model
        """
        self.set_field_value(self.SAVEFOCUSIMAGES__FIELD_NAME.field_name, value)

    def get_SaveFocusImages_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SaveFocusImages' from this record model
        """
        return self.get_field_value(self.SAVEFOCUSIMAGES__FIELD_NAME.field_name)

    def set_SaveScanImages_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SaveScanImages' on this record model
        """
        self.set_field_value(self.SAVESCANIMAGES__FIELD_NAME.field_name, value)

    def get_SaveScanImages_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SaveScanImages' from this record model
        """
        return self.get_field_value(self.SAVESCANIMAGES__FIELD_NAME.field_name)

    def set_ScannerID_field(self, value: Optional[str]):
        """
        Set data field with field name 'ScannerID' on this record model
        """
        self.set_field_value(self.SCANNERID__FIELD_NAME.field_name, value)

    def get_ScannerID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ScannerID' from this record model
        """
        return self.get_field_value(self.SCANNERID__FIELD_NAME.field_name)

    def set_SendInstrumentHealthToILMN_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SendInstrumentHealthToILMN' on this record model
        """
        self.set_field_value(self.SENDINSTRUMENTHEALTHTOILMN__FIELD_NAME.field_name, value)

    def get_SendInstrumentHealthToILMN_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SendInstrumentHealthToILMN' from this record model
        """
        return self.get_field_value(self.SENDINSTRUMENTHEALTHTOILMN__FIELD_NAME.field_name)

    def set_SupportMultipleSurfacesInUI_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SupportMultipleSurfacesInUI' on this record model
        """
        self.set_field_value(self.SUPPORTMULTIPLESURFACESINUI__FIELD_NAME.field_name, value)

    def get_SupportMultipleSurfacesInUI_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SupportMultipleSurfacesInUI' from this record model
        """
        return self.get_field_value(self.SUPPORTMULTIPLESURFACESINUI__FIELD_NAME.field_name)

    def set_SurfaceToScan_field(self, value: Optional[str]):
        """
        Set data field with field name 'SurfaceToScan' on this record model
        """
        self.set_field_value(self.SURFACETOSCAN__FIELD_NAME.field_name, value)

    def get_SurfaceToScan_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SurfaceToScan' from this record model
        """
        return self.get_field_value(self.SURFACETOSCAN__FIELD_NAME.field_name)

    def set_TempFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'TempFolder' on this record model
        """
        self.set_field_value(self.TEMPFOLDER__FIELD_NAME.field_name, value)

    def get_TempFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TempFolder' from this record model
        """
        return self.get_field_value(self.TEMPFOLDER__FIELD_NAME.field_name)

    def set_Username_field(self, value: Optional[str]):
        """
        Set data field with field name 'Username' on this record model
        """
        self.set_field_value(self.USERNAME__FIELD_NAME.field_name, value)

    def get_Username_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Username' from this record model
        """
        return self.get_field_value(self.USERNAME__FIELD_NAME.field_name)


class IlluminaMiSeqSSSettingsModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaMiSeqSSSettings
    Data Type Display Name: Illumina MiSeq Sample Sheet Settings (Illumina MiSeq Sample Sheet Settings)
    Fields: Adapter, AdapterRead2, AdapterTrimmingStringency, Aligner, Assay, BaitManifestFileName, CustomAmpliconAlignerMaxIndel, CustomIndexPrimerMix, CustomRead1PrimerMix, CustomRead2PrimerMix, CyclesRead1, CyclesRead2, Description, EnrichmentMaxRegionStatistics, ExcludeRegionsManifestA, ExperimentName, FilterOutSingleStrandVariants, FlagPCRDuplicates, IndexReads, InvestigatorName, Kmer, MinimumCoverageDepth, OutputGenomeVCF, PercentTilesToScan, PicardHSmetrics, QualityScoreTrim, ReadType, ReagentCartridgeBarcode, ReverseComplement, RunDate, StitchReads, TaxonomyFile, VariantCaller, VariantFilterQualityCutoff, Workflow
    """
    DATA_TYPE_NAME: str = 'IlluminaMiSeqSSSettings'
    ADAPTER__FIELD_NAME: WrapperField = WrapperField("Adapter", FieldType.STRING)
    ADAPTERREAD2__FIELD_NAME: WrapperField = WrapperField("AdapterRead2", FieldType.STRING)
    ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME: WrapperField = WrapperField("AdapterTrimmingStringency", FieldType.STRING)
    ALIGNER__FIELD_NAME: WrapperField = WrapperField("Aligner", FieldType.STRING)
    ASSAY__FIELD_NAME: WrapperField = WrapperField("Assay", FieldType.STRING)
    BAITMANIFESTFILENAME__FIELD_NAME: WrapperField = WrapperField("BaitManifestFileName", FieldType.STRING)
    CUSTOMAMPLICONALIGNERMAXINDEL__FIELD_NAME: WrapperField = WrapperField("CustomAmpliconAlignerMaxIndel", FieldType.STRING)
    CUSTOMINDEXPRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomIndexPrimerMix", FieldType.STRING)
    CUSTOMREAD1PRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomRead1PrimerMix", FieldType.STRING)
    CUSTOMREAD2PRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomRead2PrimerMix", FieldType.STRING)
    CYCLESREAD1__FIELD_NAME: WrapperField = WrapperField("CyclesRead1", FieldType.INTEGER)
    CYCLESREAD2__FIELD_NAME: WrapperField = WrapperField("CyclesRead2", FieldType.INTEGER)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    ENRICHMENTMAXREGIONSTATISTICS__FIELD_NAME: WrapperField = WrapperField("EnrichmentMaxRegionStatistics", FieldType.STRING)
    EXCLUDEREGIONSMANIFESTA__FIELD_NAME: WrapperField = WrapperField("ExcludeRegionsManifestA", FieldType.STRING)
    EXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("ExperimentName", FieldType.STRING)
    FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME: WrapperField = WrapperField("FilterOutSingleStrandVariants", FieldType.STRING)
    FLAGPCRDUPLICATES__FIELD_NAME: WrapperField = WrapperField("FlagPCRDuplicates", FieldType.BOOLEAN)
    INDEXREADS__FIELD_NAME: WrapperField = WrapperField("IndexReads", FieldType.SHORT)
    INVESTIGATORNAME__FIELD_NAME: WrapperField = WrapperField("InvestigatorName", FieldType.STRING)
    KMER__FIELD_NAME: WrapperField = WrapperField("Kmer", FieldType.STRING)
    MINIMUMCOVERAGEDEPTH__FIELD_NAME: WrapperField = WrapperField("MinimumCoverageDepth", FieldType.STRING)
    OUTPUTGENOMEVCF__FIELD_NAME: WrapperField = WrapperField("OutputGenomeVCF", FieldType.BOOLEAN)
    PERCENTTILESTOSCAN__FIELD_NAME: WrapperField = WrapperField("PercentTilesToScan", FieldType.STRING)
    PICARDHSMETRICS__FIELD_NAME: WrapperField = WrapperField("PicardHSmetrics", FieldType.BOOLEAN)
    QUALITYSCORETRIM__FIELD_NAME: WrapperField = WrapperField("QualityScoreTrim", FieldType.STRING)
    READTYPE__FIELD_NAME: WrapperField = WrapperField("ReadType", FieldType.PICKLIST)
    REAGENTCARTRIDGEBARCODE__FIELD_NAME: WrapperField = WrapperField("ReagentCartridgeBarcode", FieldType.STRING)
    REVERSECOMPLEMENT__FIELD_NAME: WrapperField = WrapperField("ReverseComplement", FieldType.BOOLEAN)
    RUNDATE__FIELD_NAME: WrapperField = WrapperField("RunDate", FieldType.DATE)
    STITCHREADS__FIELD_NAME: WrapperField = WrapperField("StitchReads", FieldType.BOOLEAN)
    TAXONOMYFILE__FIELD_NAME: WrapperField = WrapperField("TaxonomyFile", FieldType.STRING)
    VARIANTCALLER__FIELD_NAME: WrapperField = WrapperField("VariantCaller", FieldType.STRING)
    VARIANTFILTERQUALITYCUTOFF__FIELD_NAME: WrapperField = WrapperField("VariantFilterQualityCutoff", FieldType.STRING)
    WORKFLOW__FIELD_NAME: WrapperField = WrapperField("Workflow", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Adapter_field(self, value: Optional[str]):
        """
        Set data field with field name 'Adapter' on this record model
        """
        self.set_field_value(self.ADAPTER__FIELD_NAME.field_name, value)

    def get_Adapter_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Adapter' from this record model
        """
        return self.get_field_value(self.ADAPTER__FIELD_NAME.field_name)

    def set_AdapterRead2_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdapterRead2' on this record model
        """
        self.set_field_value(self.ADAPTERREAD2__FIELD_NAME.field_name, value)

    def get_AdapterRead2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdapterRead2' from this record model
        """
        return self.get_field_value(self.ADAPTERREAD2__FIELD_NAME.field_name)

    def set_AdapterTrimmingStringency_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdapterTrimmingStringency' on this record model
        """
        self.set_field_value(self.ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME.field_name, value)

    def get_AdapterTrimmingStringency_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdapterTrimmingStringency' from this record model
        """
        return self.get_field_value(self.ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME.field_name)

    def set_Aligner_field(self, value: Optional[str]):
        """
        Set data field with field name 'Aligner' on this record model
        """
        self.set_field_value(self.ALIGNER__FIELD_NAME.field_name, value)

    def get_Aligner_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Aligner' from this record model
        """
        return self.get_field_value(self.ALIGNER__FIELD_NAME.field_name)

    def set_Assay_field(self, value: Optional[str]):
        """
        Set data field with field name 'Assay' on this record model
        """
        self.set_field_value(self.ASSAY__FIELD_NAME.field_name, value)

    def get_Assay_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Assay' from this record model
        """
        return self.get_field_value(self.ASSAY__FIELD_NAME.field_name)

    def set_BaitManifestFileName_field(self, value: Optional[str]):
        """
        Set data field with field name 'BaitManifestFileName' on this record model
        """
        self.set_field_value(self.BAITMANIFESTFILENAME__FIELD_NAME.field_name, value)

    def get_BaitManifestFileName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BaitManifestFileName' from this record model
        """
        return self.get_field_value(self.BAITMANIFESTFILENAME__FIELD_NAME.field_name)

    def set_CustomAmpliconAlignerMaxIndel_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomAmpliconAlignerMaxIndel' on this record model
        """
        self.set_field_value(self.CUSTOMAMPLICONALIGNERMAXINDEL__FIELD_NAME.field_name, value)

    def get_CustomAmpliconAlignerMaxIndel_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomAmpliconAlignerMaxIndel' from this record model
        """
        return self.get_field_value(self.CUSTOMAMPLICONALIGNERMAXINDEL__FIELD_NAME.field_name)

    def set_CustomIndexPrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomIndexPrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMINDEXPRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomIndexPrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomIndexPrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMINDEXPRIMERMIX__FIELD_NAME.field_name)

    def set_CustomRead1PrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomRead1PrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMREAD1PRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomRead1PrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomRead1PrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMREAD1PRIMERMIX__FIELD_NAME.field_name)

    def set_CustomRead2PrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomRead2PrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMREAD2PRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomRead2PrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomRead2PrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMREAD2PRIMERMIX__FIELD_NAME.field_name)

    def set_CyclesRead1_field(self, value: Optional[int]):
        """
        Set data field with field name 'CyclesRead1' on this record model
        """
        self.set_field_value(self.CYCLESREAD1__FIELD_NAME.field_name, value)

    def get_CyclesRead1_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CyclesRead1' from this record model
        """
        return self.get_field_value(self.CYCLESREAD1__FIELD_NAME.field_name)

    def set_CyclesRead2_field(self, value: Optional[int]):
        """
        Set data field with field name 'CyclesRead2' on this record model
        """
        self.set_field_value(self.CYCLESREAD2__FIELD_NAME.field_name, value)

    def get_CyclesRead2_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CyclesRead2' from this record model
        """
        return self.get_field_value(self.CYCLESREAD2__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_EnrichmentMaxRegionStatistics_field(self, value: Optional[str]):
        """
        Set data field with field name 'EnrichmentMaxRegionStatistics' on this record model
        """
        self.set_field_value(self.ENRICHMENTMAXREGIONSTATISTICS__FIELD_NAME.field_name, value)

    def get_EnrichmentMaxRegionStatistics_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EnrichmentMaxRegionStatistics' from this record model
        """
        return self.get_field_value(self.ENRICHMENTMAXREGIONSTATISTICS__FIELD_NAME.field_name)

    def set_ExcludeRegionsManifestA_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExcludeRegionsManifestA' on this record model
        """
        self.set_field_value(self.EXCLUDEREGIONSMANIFESTA__FIELD_NAME.field_name, value)

    def get_ExcludeRegionsManifestA_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExcludeRegionsManifestA' from this record model
        """
        return self.get_field_value(self.EXCLUDEREGIONSMANIFESTA__FIELD_NAME.field_name)

    def set_ExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentName' on this record model
        """
        self.set_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_ExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentName' from this record model
        """
        return self.get_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name)

    def set_FilterOutSingleStrandVariants_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilterOutSingleStrandVariants' on this record model
        """
        self.set_field_value(self.FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME.field_name, value)

    def get_FilterOutSingleStrandVariants_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilterOutSingleStrandVariants' from this record model
        """
        return self.get_field_value(self.FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME.field_name)

    def set_FlagPCRDuplicates_field(self, value: Optional[bool]):
        """
        Set data field with field name 'FlagPCRDuplicates' on this record model
        """
        self.set_field_value(self.FLAGPCRDUPLICATES__FIELD_NAME.field_name, value)

    def get_FlagPCRDuplicates_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'FlagPCRDuplicates' from this record model
        """
        return self.get_field_value(self.FLAGPCRDUPLICATES__FIELD_NAME.field_name)

    def set_IndexReads_field(self, value: Optional[int]):
        """
        Set data field with field name 'IndexReads' on this record model
        """
        self.set_field_value(self.INDEXREADS__FIELD_NAME.field_name, value)

    def get_IndexReads_field(self) -> Optional[int]:
        """
        Get data field value with field name 'IndexReads' from this record model
        """
        return self.get_field_value(self.INDEXREADS__FIELD_NAME.field_name)

    def set_InvestigatorName_field(self, value: Optional[str]):
        """
        Set data field with field name 'InvestigatorName' on this record model
        """
        self.set_field_value(self.INVESTIGATORNAME__FIELD_NAME.field_name, value)

    def get_InvestigatorName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InvestigatorName' from this record model
        """
        return self.get_field_value(self.INVESTIGATORNAME__FIELD_NAME.field_name)

    def set_Kmer_field(self, value: Optional[str]):
        """
        Set data field with field name 'Kmer' on this record model
        """
        self.set_field_value(self.KMER__FIELD_NAME.field_name, value)

    def get_Kmer_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Kmer' from this record model
        """
        return self.get_field_value(self.KMER__FIELD_NAME.field_name)

    def set_MinimumCoverageDepth_field(self, value: Optional[str]):
        """
        Set data field with field name 'MinimumCoverageDepth' on this record model
        """
        self.set_field_value(self.MINIMUMCOVERAGEDEPTH__FIELD_NAME.field_name, value)

    def get_MinimumCoverageDepth_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MinimumCoverageDepth' from this record model
        """
        return self.get_field_value(self.MINIMUMCOVERAGEDEPTH__FIELD_NAME.field_name)

    def set_OutputGenomeVCF_field(self, value: Optional[bool]):
        """
        Set data field with field name 'OutputGenomeVCF' on this record model
        """
        self.set_field_value(self.OUTPUTGENOMEVCF__FIELD_NAME.field_name, value)

    def get_OutputGenomeVCF_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'OutputGenomeVCF' from this record model
        """
        return self.get_field_value(self.OUTPUTGENOMEVCF__FIELD_NAME.field_name)

    def set_PercentTilesToScan_field(self, value: Optional[str]):
        """
        Set data field with field name 'PercentTilesToScan' on this record model
        """
        self.set_field_value(self.PERCENTTILESTOSCAN__FIELD_NAME.field_name, value)

    def get_PercentTilesToScan_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PercentTilesToScan' from this record model
        """
        return self.get_field_value(self.PERCENTTILESTOSCAN__FIELD_NAME.field_name)

    def set_PicardHSmetrics_field(self, value: Optional[bool]):
        """
        Set data field with field name 'PicardHSmetrics' on this record model
        """
        self.set_field_value(self.PICARDHSMETRICS__FIELD_NAME.field_name, value)

    def get_PicardHSmetrics_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'PicardHSmetrics' from this record model
        """
        return self.get_field_value(self.PICARDHSMETRICS__FIELD_NAME.field_name)

    def set_QualityScoreTrim_field(self, value: Optional[str]):
        """
        Set data field with field name 'QualityScoreTrim' on this record model
        """
        self.set_field_value(self.QUALITYSCORETRIM__FIELD_NAME.field_name, value)

    def get_QualityScoreTrim_field(self) -> Optional[str]:
        """
        Get data field value with field name 'QualityScoreTrim' from this record model
        """
        return self.get_field_value(self.QUALITYSCORETRIM__FIELD_NAME.field_name)

    def set_ReadType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReadType' on this record model
        """
        self.set_field_value(self.READTYPE__FIELD_NAME.field_name, value)

    def get_ReadType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReadType' from this record model
        """
        return self.get_field_value(self.READTYPE__FIELD_NAME.field_name)

    def set_ReagentCartridgeBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentCartridgeBarcode' on this record model
        """
        self.set_field_value(self.REAGENTCARTRIDGEBARCODE__FIELD_NAME.field_name, value)

    def get_ReagentCartridgeBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentCartridgeBarcode' from this record model
        """
        return self.get_field_value(self.REAGENTCARTRIDGEBARCODE__FIELD_NAME.field_name)

    def set_ReverseComplement_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ReverseComplement' on this record model
        """
        self.set_field_value(self.REVERSECOMPLEMENT__FIELD_NAME.field_name, value)

    def get_ReverseComplement_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ReverseComplement' from this record model
        """
        return self.get_field_value(self.REVERSECOMPLEMENT__FIELD_NAME.field_name)

    def set_RunDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunDate' on this record model
        """
        self.set_field_value(self.RUNDATE__FIELD_NAME.field_name, value)

    def get_RunDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunDate' from this record model
        """
        return self.get_field_value(self.RUNDATE__FIELD_NAME.field_name)

    def set_StitchReads_field(self, value: Optional[bool]):
        """
        Set data field with field name 'StitchReads' on this record model
        """
        self.set_field_value(self.STITCHREADS__FIELD_NAME.field_name, value)

    def get_StitchReads_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'StitchReads' from this record model
        """
        return self.get_field_value(self.STITCHREADS__FIELD_NAME.field_name)

    def set_TaxonomyFile_field(self, value: Optional[str]):
        """
        Set data field with field name 'TaxonomyFile' on this record model
        """
        self.set_field_value(self.TAXONOMYFILE__FIELD_NAME.field_name, value)

    def get_TaxonomyFile_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TaxonomyFile' from this record model
        """
        return self.get_field_value(self.TAXONOMYFILE__FIELD_NAME.field_name)

    def set_VariantCaller_field(self, value: Optional[str]):
        """
        Set data field with field name 'VariantCaller' on this record model
        """
        self.set_field_value(self.VARIANTCALLER__FIELD_NAME.field_name, value)

    def get_VariantCaller_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VariantCaller' from this record model
        """
        return self.get_field_value(self.VARIANTCALLER__FIELD_NAME.field_name)

    def set_VariantFilterQualityCutoff_field(self, value: Optional[str]):
        """
        Set data field with field name 'VariantFilterQualityCutoff' on this record model
        """
        self.set_field_value(self.VARIANTFILTERQUALITYCUTOFF__FIELD_NAME.field_name, value)

    def get_VariantFilterQualityCutoff_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VariantFilterQualityCutoff' from this record model
        """
        return self.get_field_value(self.VARIANTFILTERQUALITYCUTOFF__FIELD_NAME.field_name)

    def set_Workflow_field(self, value: Optional[str]):
        """
        Set data field with field name 'Workflow' on this record model
        """
        self.set_field_value(self.WORKFLOW__FIELD_NAME.field_name, value)

    def get_Workflow_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Workflow' from this record model
        """
        return self.get_field_value(self.WORKFLOW__FIELD_NAME.field_name)


class IlluminaNextGenConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaNextGenConfig
    Data Type Display Name: Illumina Next-Gen Configuration (Illumina Next-Gen Configurations)
    Fields: AssociatedProcessName, Description, MultiplexInstructions, RunType
    Configuration fields required for the Illumina Next-Gen Sequencing request form
    """
    DATA_TYPE_NAME: str = 'IlluminaNextGenConfig'
    ASSOCIATEDPROCESSNAME__FIELD_NAME: WrapperField = WrapperField("AssociatedProcessName", FieldType.STRING)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    MULTIPLEXINSTRUCTIONS__FIELD_NAME: WrapperField = WrapperField("MultiplexInstructions", FieldType.SELECTION)
    RUNTYPE__FIELD_NAME: WrapperField = WrapperField("RunType", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AssociatedProcessName_field(self, value: Optional[str]):
        """
        Set data field with field name 'AssociatedProcessName' on this record model
        """
        self.set_field_value(self.ASSOCIATEDPROCESSNAME__FIELD_NAME.field_name, value)

    def get_AssociatedProcessName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AssociatedProcessName' from this record model
        """
        return self.get_field_value(self.ASSOCIATEDPROCESSNAME__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_MultiplexInstructions_field(self, value: Optional[str]):
        """
        Set data field with field name 'MultiplexInstructions' on this record model
        """
        self.set_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name, value)

    def get_MultiplexInstructions_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MultiplexInstructions' from this record model
        """
        return self.get_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name)

    def set_RunType_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunType' on this record model
        """
        self.set_field_value(self.RUNTYPE__FIELD_NAME.field_name, value)

    def get_RunType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunType' from this record model
        """
        return self.get_field_value(self.RUNTYPE__FIELD_NAME.field_name)


class IlluminaNextSeqRunParametersModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaNextSeqRunParameters
    Data Type Display Name: Illumina NextSeq Run Parameters (Illumina NextSeq Run Parameters')
    Fields: AnalysisWorkflowType, ApplicationName, ApplicationVersion, BaseSpaceRunId, BaseSpaceRunMode, Chemistry, ComputerName, CustomReadOnePrimer, CustomReadTwoPrimer, ExperimentName, FlowCellSerial, FocusMethod, Index1Read, Index2Read, InstrumentID, IsPairedEnd, LanePerSection, LibraryID, NumLanes, NumSwaths, NumTilesPerSwath, OutputFolder, PR2BottleSerial, Read1, Read2, ReagentKitSerial, RecipeFolder, RKitSerialEnteredInBaseSpace, RTAVersion, RunFolder, RunID, RunManagementType, RunNumber, RunStartDate, SaveFocusImages, SaveScanImages, SectionPerLane, SelectiveSave, SeqCompletedWithoutErrors, SequencingCompletedOrAborted, SequencingStarted, SupportMultipleSurfacesInUI, SurfaceToScan, UsesCustomIndexPrimer, UsesCustomPrimer1, UsesCustomPrimer2
     <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'IlluminaNextSeqRunParameters'
    ANALYSISWORKFLOWTYPE__FIELD_NAME: WrapperField = WrapperField("AnalysisWorkflowType", FieldType.STRING)
    APPLICATIONNAME__FIELD_NAME: WrapperField = WrapperField("ApplicationName", FieldType.STRING)
    APPLICATIONVERSION__FIELD_NAME: WrapperField = WrapperField("ApplicationVersion", FieldType.STRING)
    BASESPACERUNID__FIELD_NAME: WrapperField = WrapperField("BaseSpaceRunId", FieldType.STRING)
    BASESPACERUNMODE__FIELD_NAME: WrapperField = WrapperField("BaseSpaceRunMode", FieldType.STRING)
    CHEMISTRY__FIELD_NAME: WrapperField = WrapperField("Chemistry", FieldType.STRING)
    COMPUTERNAME__FIELD_NAME: WrapperField = WrapperField("ComputerName", FieldType.STRING)
    CUSTOMREADONEPRIMER__FIELD_NAME: WrapperField = WrapperField("CustomReadOnePrimer", FieldType.STRING)
    CUSTOMREADTWOPRIMER__FIELD_NAME: WrapperField = WrapperField("CustomReadTwoPrimer", FieldType.STRING)
    EXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("ExperimentName", FieldType.STRING)
    FLOWCELLSERIAL__FIELD_NAME: WrapperField = WrapperField("FlowCellSerial", FieldType.STRING)
    FOCUSMETHOD__FIELD_NAME: WrapperField = WrapperField("FocusMethod", FieldType.STRING)
    INDEX1READ__FIELD_NAME: WrapperField = WrapperField("Index1Read", FieldType.LONG)
    INDEX2READ__FIELD_NAME: WrapperField = WrapperField("Index2Read", FieldType.LONG)
    INSTRUMENTID__FIELD_NAME: WrapperField = WrapperField("InstrumentID", FieldType.STRING)
    ISPAIREDEND__FIELD_NAME: WrapperField = WrapperField("IsPairedEnd", FieldType.BOOLEAN)
    LANEPERSECTION__FIELD_NAME: WrapperField = WrapperField("LanePerSection", FieldType.LONG)
    LIBRARYID__FIELD_NAME: WrapperField = WrapperField("LibraryID", FieldType.STRING)
    NUMLANES__FIELD_NAME: WrapperField = WrapperField("NumLanes", FieldType.LONG)
    NUMSWATHS__FIELD_NAME: WrapperField = WrapperField("NumSwaths", FieldType.LONG)
    NUMTILESPERSWATH__FIELD_NAME: WrapperField = WrapperField("NumTilesPerSwath", FieldType.LONG)
    OUTPUTFOLDER__FIELD_NAME: WrapperField = WrapperField("OutputFolder", FieldType.STRING)
    PR2BOTTLESERIAL__FIELD_NAME: WrapperField = WrapperField("PR2BottleSerial", FieldType.STRING)
    READ1__FIELD_NAME: WrapperField = WrapperField("Read1", FieldType.LONG)
    READ2__FIELD_NAME: WrapperField = WrapperField("Read2", FieldType.LONG)
    REAGENTKITSERIAL__FIELD_NAME: WrapperField = WrapperField("ReagentKitSerial", FieldType.STRING)
    RECIPEFOLDER__FIELD_NAME: WrapperField = WrapperField("RecipeFolder", FieldType.STRING)
    RKITSERIALENTEREDINBASESPACE__FIELD_NAME: WrapperField = WrapperField("RKitSerialEnteredInBaseSpace", FieldType.BOOLEAN)
    RTAVERSION__FIELD_NAME: WrapperField = WrapperField("RTAVersion", FieldType.STRING)
    RUNFOLDER__FIELD_NAME: WrapperField = WrapperField("RunFolder", FieldType.STRING)
    RUNID__FIELD_NAME: WrapperField = WrapperField("RunID", FieldType.STRING)
    RUNMANAGEMENTTYPE__FIELD_NAME: WrapperField = WrapperField("RunManagementType", FieldType.STRING)
    RUNNUMBER__FIELD_NAME: WrapperField = WrapperField("RunNumber", FieldType.LONG)
    RUNSTARTDATE__FIELD_NAME: WrapperField = WrapperField("RunStartDate", FieldType.DATE)
    SAVEFOCUSIMAGES__FIELD_NAME: WrapperField = WrapperField("SaveFocusImages", FieldType.BOOLEAN)
    SAVESCANIMAGES__FIELD_NAME: WrapperField = WrapperField("SaveScanImages", FieldType.BOOLEAN)
    SECTIONPERLANE__FIELD_NAME: WrapperField = WrapperField("SectionPerLane", FieldType.LONG)
    SELECTIVESAVE__FIELD_NAME: WrapperField = WrapperField("SelectiveSave", FieldType.BOOLEAN)
    SEQCOMPLETEDWITHOUTERRORS__FIELD_NAME: WrapperField = WrapperField("SeqCompletedWithoutErrors", FieldType.BOOLEAN)
    SEQUENCINGCOMPLETEDORABORTED__FIELD_NAME: WrapperField = WrapperField("SequencingCompletedOrAborted", FieldType.BOOLEAN)
    SEQUENCINGSTARTED__FIELD_NAME: WrapperField = WrapperField("SequencingStarted", FieldType.BOOLEAN)
    SUPPORTMULTIPLESURFACESINUI__FIELD_NAME: WrapperField = WrapperField("SupportMultipleSurfacesInUI", FieldType.BOOLEAN)
    SURFACETOSCAN__FIELD_NAME: WrapperField = WrapperField("SurfaceToScan", FieldType.STRING)
    USESCUSTOMINDEXPRIMER__FIELD_NAME: WrapperField = WrapperField("UsesCustomIndexPrimer", FieldType.BOOLEAN)
    USESCUSTOMPRIMER1__FIELD_NAME: WrapperField = WrapperField("UsesCustomPrimer1", FieldType.BOOLEAN)
    USESCUSTOMPRIMER2__FIELD_NAME: WrapperField = WrapperField("UsesCustomPrimer2", FieldType.BOOLEAN)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AnalysisWorkflowType_field(self, value: Optional[str]):
        """
        Set data field with field name 'AnalysisWorkflowType' on this record model
        """
        self.set_field_value(self.ANALYSISWORKFLOWTYPE__FIELD_NAME.field_name, value)

    def get_AnalysisWorkflowType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AnalysisWorkflowType' from this record model
        """
        return self.get_field_value(self.ANALYSISWORKFLOWTYPE__FIELD_NAME.field_name)

    def set_ApplicationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApplicationName' on this record model
        """
        self.set_field_value(self.APPLICATIONNAME__FIELD_NAME.field_name, value)

    def get_ApplicationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApplicationName' from this record model
        """
        return self.get_field_value(self.APPLICATIONNAME__FIELD_NAME.field_name)

    def set_ApplicationVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApplicationVersion' on this record model
        """
        self.set_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name, value)

    def get_ApplicationVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApplicationVersion' from this record model
        """
        return self.get_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name)

    def set_BaseSpaceRunId_field(self, value: Optional[str]):
        """
        Set data field with field name 'BaseSpaceRunId' on this record model
        """
        self.set_field_value(self.BASESPACERUNID__FIELD_NAME.field_name, value)

    def get_BaseSpaceRunId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BaseSpaceRunId' from this record model
        """
        return self.get_field_value(self.BASESPACERUNID__FIELD_NAME.field_name)

    def set_BaseSpaceRunMode_field(self, value: Optional[str]):
        """
        Set data field with field name 'BaseSpaceRunMode' on this record model
        """
        self.set_field_value(self.BASESPACERUNMODE__FIELD_NAME.field_name, value)

    def get_BaseSpaceRunMode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BaseSpaceRunMode' from this record model
        """
        return self.get_field_value(self.BASESPACERUNMODE__FIELD_NAME.field_name)

    def set_Chemistry_field(self, value: Optional[str]):
        """
        Set data field with field name 'Chemistry' on this record model
        """
        self.set_field_value(self.CHEMISTRY__FIELD_NAME.field_name, value)

    def get_Chemistry_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Chemistry' from this record model
        """
        return self.get_field_value(self.CHEMISTRY__FIELD_NAME.field_name)

    def set_ComputerName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ComputerName' on this record model
        """
        self.set_field_value(self.COMPUTERNAME__FIELD_NAME.field_name, value)

    def get_ComputerName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ComputerName' from this record model
        """
        return self.get_field_value(self.COMPUTERNAME__FIELD_NAME.field_name)

    def set_CustomReadOnePrimer_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomReadOnePrimer' on this record model
        """
        self.set_field_value(self.CUSTOMREADONEPRIMER__FIELD_NAME.field_name, value)

    def get_CustomReadOnePrimer_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomReadOnePrimer' from this record model
        """
        return self.get_field_value(self.CUSTOMREADONEPRIMER__FIELD_NAME.field_name)

    def set_CustomReadTwoPrimer_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomReadTwoPrimer' on this record model
        """
        self.set_field_value(self.CUSTOMREADTWOPRIMER__FIELD_NAME.field_name, value)

    def get_CustomReadTwoPrimer_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomReadTwoPrimer' from this record model
        """
        return self.get_field_value(self.CUSTOMREADTWOPRIMER__FIELD_NAME.field_name)

    def set_ExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentName' on this record model
        """
        self.set_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_ExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentName' from this record model
        """
        return self.get_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name)

    def set_FlowCellSerial_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowCellSerial' on this record model
        """
        self.set_field_value(self.FLOWCELLSERIAL__FIELD_NAME.field_name, value)

    def get_FlowCellSerial_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowCellSerial' from this record model
        """
        return self.get_field_value(self.FLOWCELLSERIAL__FIELD_NAME.field_name)

    def set_FocusMethod_field(self, value: Optional[str]):
        """
        Set data field with field name 'FocusMethod' on this record model
        """
        self.set_field_value(self.FOCUSMETHOD__FIELD_NAME.field_name, value)

    def get_FocusMethod_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FocusMethod' from this record model
        """
        return self.get_field_value(self.FOCUSMETHOD__FIELD_NAME.field_name)

    def set_Index1Read_field(self, value: Optional[int]):
        """
        Set data field with field name 'Index1Read' on this record model
        """
        self.set_field_value(self.INDEX1READ__FIELD_NAME.field_name, value)

    def get_Index1Read_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Index1Read' from this record model
        """
        return self.get_field_value(self.INDEX1READ__FIELD_NAME.field_name)

    def set_Index2Read_field(self, value: Optional[int]):
        """
        Set data field with field name 'Index2Read' on this record model
        """
        self.set_field_value(self.INDEX2READ__FIELD_NAME.field_name, value)

    def get_Index2Read_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Index2Read' from this record model
        """
        return self.get_field_value(self.INDEX2READ__FIELD_NAME.field_name)

    def set_InstrumentID_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentID' on this record model
        """
        self.set_field_value(self.INSTRUMENTID__FIELD_NAME.field_name, value)

    def get_InstrumentID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentID' from this record model
        """
        return self.get_field_value(self.INSTRUMENTID__FIELD_NAME.field_name)

    def set_IsPairedEnd_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsPairedEnd' on this record model
        """
        self.set_field_value(self.ISPAIREDEND__FIELD_NAME.field_name, value)

    def get_IsPairedEnd_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsPairedEnd' from this record model
        """
        return self.get_field_value(self.ISPAIREDEND__FIELD_NAME.field_name)

    def set_LanePerSection_field(self, value: Optional[int]):
        """
        Set data field with field name 'LanePerSection' on this record model
        """
        self.set_field_value(self.LANEPERSECTION__FIELD_NAME.field_name, value)

    def get_LanePerSection_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LanePerSection' from this record model
        """
        return self.get_field_value(self.LANEPERSECTION__FIELD_NAME.field_name)

    def set_LibraryID_field(self, value: Optional[str]):
        """
        Set data field with field name 'LibraryID' on this record model
        """
        self.set_field_value(self.LIBRARYID__FIELD_NAME.field_name, value)

    def get_LibraryID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LibraryID' from this record model
        """
        return self.get_field_value(self.LIBRARYID__FIELD_NAME.field_name)

    def set_NumLanes_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumLanes' on this record model
        """
        self.set_field_value(self.NUMLANES__FIELD_NAME.field_name, value)

    def get_NumLanes_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumLanes' from this record model
        """
        return self.get_field_value(self.NUMLANES__FIELD_NAME.field_name)

    def set_NumSwaths_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumSwaths' on this record model
        """
        self.set_field_value(self.NUMSWATHS__FIELD_NAME.field_name, value)

    def get_NumSwaths_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumSwaths' from this record model
        """
        return self.get_field_value(self.NUMSWATHS__FIELD_NAME.field_name)

    def set_NumTilesPerSwath_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumTilesPerSwath' on this record model
        """
        self.set_field_value(self.NUMTILESPERSWATH__FIELD_NAME.field_name, value)

    def get_NumTilesPerSwath_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumTilesPerSwath' from this record model
        """
        return self.get_field_value(self.NUMTILESPERSWATH__FIELD_NAME.field_name)

    def set_OutputFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'OutputFolder' on this record model
        """
        self.set_field_value(self.OUTPUTFOLDER__FIELD_NAME.field_name, value)

    def get_OutputFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OutputFolder' from this record model
        """
        return self.get_field_value(self.OUTPUTFOLDER__FIELD_NAME.field_name)

    def set_PR2BottleSerial_field(self, value: Optional[str]):
        """
        Set data field with field name 'PR2BottleSerial' on this record model
        """
        self.set_field_value(self.PR2BOTTLESERIAL__FIELD_NAME.field_name, value)

    def get_PR2BottleSerial_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PR2BottleSerial' from this record model
        """
        return self.get_field_value(self.PR2BOTTLESERIAL__FIELD_NAME.field_name)

    def set_Read1_field(self, value: Optional[int]):
        """
        Set data field with field name 'Read1' on this record model
        """
        self.set_field_value(self.READ1__FIELD_NAME.field_name, value)

    def get_Read1_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Read1' from this record model
        """
        return self.get_field_value(self.READ1__FIELD_NAME.field_name)

    def set_Read2_field(self, value: Optional[int]):
        """
        Set data field with field name 'Read2' on this record model
        """
        self.set_field_value(self.READ2__FIELD_NAME.field_name, value)

    def get_Read2_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Read2' from this record model
        """
        return self.get_field_value(self.READ2__FIELD_NAME.field_name)

    def set_ReagentKitSerial_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentKitSerial' on this record model
        """
        self.set_field_value(self.REAGENTKITSERIAL__FIELD_NAME.field_name, value)

    def get_ReagentKitSerial_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentKitSerial' from this record model
        """
        return self.get_field_value(self.REAGENTKITSERIAL__FIELD_NAME.field_name)

    def set_RecipeFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecipeFolder' on this record model
        """
        self.set_field_value(self.RECIPEFOLDER__FIELD_NAME.field_name, value)

    def get_RecipeFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecipeFolder' from this record model
        """
        return self.get_field_value(self.RECIPEFOLDER__FIELD_NAME.field_name)

    def set_RKitSerialEnteredInBaseSpace_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RKitSerialEnteredInBaseSpace' on this record model
        """
        self.set_field_value(self.RKITSERIALENTEREDINBASESPACE__FIELD_NAME.field_name, value)

    def get_RKitSerialEnteredInBaseSpace_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RKitSerialEnteredInBaseSpace' from this record model
        """
        return self.get_field_value(self.RKITSERIALENTEREDINBASESPACE__FIELD_NAME.field_name)

    def set_RTAVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'RTAVersion' on this record model
        """
        self.set_field_value(self.RTAVERSION__FIELD_NAME.field_name, value)

    def get_RTAVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RTAVersion' from this record model
        """
        return self.get_field_value(self.RTAVERSION__FIELD_NAME.field_name)

    def set_RunFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunFolder' on this record model
        """
        self.set_field_value(self.RUNFOLDER__FIELD_NAME.field_name, value)

    def get_RunFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunFolder' from this record model
        """
        return self.get_field_value(self.RUNFOLDER__FIELD_NAME.field_name)

    def set_RunID_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunID' on this record model
        """
        self.set_field_value(self.RUNID__FIELD_NAME.field_name, value)

    def get_RunID_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunID' from this record model
        """
        return self.get_field_value(self.RUNID__FIELD_NAME.field_name)

    def set_RunManagementType_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunManagementType' on this record model
        """
        self.set_field_value(self.RUNMANAGEMENTTYPE__FIELD_NAME.field_name, value)

    def get_RunManagementType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunManagementType' from this record model
        """
        return self.get_field_value(self.RUNMANAGEMENTTYPE__FIELD_NAME.field_name)

    def set_RunNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunNumber' on this record model
        """
        self.set_field_value(self.RUNNUMBER__FIELD_NAME.field_name, value)

    def get_RunNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunNumber' from this record model
        """
        return self.get_field_value(self.RUNNUMBER__FIELD_NAME.field_name)

    def set_RunStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunStartDate' on this record model
        """
        self.set_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name, value)

    def get_RunStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunStartDate' from this record model
        """
        return self.get_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name)

    def set_SaveFocusImages_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SaveFocusImages' on this record model
        """
        self.set_field_value(self.SAVEFOCUSIMAGES__FIELD_NAME.field_name, value)

    def get_SaveFocusImages_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SaveFocusImages' from this record model
        """
        return self.get_field_value(self.SAVEFOCUSIMAGES__FIELD_NAME.field_name)

    def set_SaveScanImages_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SaveScanImages' on this record model
        """
        self.set_field_value(self.SAVESCANIMAGES__FIELD_NAME.field_name, value)

    def get_SaveScanImages_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SaveScanImages' from this record model
        """
        return self.get_field_value(self.SAVESCANIMAGES__FIELD_NAME.field_name)

    def set_SectionPerLane_field(self, value: Optional[int]):
        """
        Set data field with field name 'SectionPerLane' on this record model
        """
        self.set_field_value(self.SECTIONPERLANE__FIELD_NAME.field_name, value)

    def get_SectionPerLane_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SectionPerLane' from this record model
        """
        return self.get_field_value(self.SECTIONPERLANE__FIELD_NAME.field_name)

    def set_SelectiveSave_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SelectiveSave' on this record model
        """
        self.set_field_value(self.SELECTIVESAVE__FIELD_NAME.field_name, value)

    def get_SelectiveSave_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SelectiveSave' from this record model
        """
        return self.get_field_value(self.SELECTIVESAVE__FIELD_NAME.field_name)

    def set_SeqCompletedWithoutErrors_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SeqCompletedWithoutErrors' on this record model
        """
        self.set_field_value(self.SEQCOMPLETEDWITHOUTERRORS__FIELD_NAME.field_name, value)

    def get_SeqCompletedWithoutErrors_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SeqCompletedWithoutErrors' from this record model
        """
        return self.get_field_value(self.SEQCOMPLETEDWITHOUTERRORS__FIELD_NAME.field_name)

    def set_SequencingCompletedOrAborted_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SequencingCompletedOrAborted' on this record model
        """
        self.set_field_value(self.SEQUENCINGCOMPLETEDORABORTED__FIELD_NAME.field_name, value)

    def get_SequencingCompletedOrAborted_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SequencingCompletedOrAborted' from this record model
        """
        return self.get_field_value(self.SEQUENCINGCOMPLETEDORABORTED__FIELD_NAME.field_name)

    def set_SequencingStarted_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SequencingStarted' on this record model
        """
        self.set_field_value(self.SEQUENCINGSTARTED__FIELD_NAME.field_name, value)

    def get_SequencingStarted_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SequencingStarted' from this record model
        """
        return self.get_field_value(self.SEQUENCINGSTARTED__FIELD_NAME.field_name)

    def set_SupportMultipleSurfacesInUI_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SupportMultipleSurfacesInUI' on this record model
        """
        self.set_field_value(self.SUPPORTMULTIPLESURFACESINUI__FIELD_NAME.field_name, value)

    def get_SupportMultipleSurfacesInUI_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SupportMultipleSurfacesInUI' from this record model
        """
        return self.get_field_value(self.SUPPORTMULTIPLESURFACESINUI__FIELD_NAME.field_name)

    def set_SurfaceToScan_field(self, value: Optional[str]):
        """
        Set data field with field name 'SurfaceToScan' on this record model
        """
        self.set_field_value(self.SURFACETOSCAN__FIELD_NAME.field_name, value)

    def get_SurfaceToScan_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SurfaceToScan' from this record model
        """
        return self.get_field_value(self.SURFACETOSCAN__FIELD_NAME.field_name)

    def set_UsesCustomIndexPrimer_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UsesCustomIndexPrimer' on this record model
        """
        self.set_field_value(self.USESCUSTOMINDEXPRIMER__FIELD_NAME.field_name, value)

    def get_UsesCustomIndexPrimer_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UsesCustomIndexPrimer' from this record model
        """
        return self.get_field_value(self.USESCUSTOMINDEXPRIMER__FIELD_NAME.field_name)

    def set_UsesCustomPrimer1_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UsesCustomPrimer1' on this record model
        """
        self.set_field_value(self.USESCUSTOMPRIMER1__FIELD_NAME.field_name, value)

    def get_UsesCustomPrimer1_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UsesCustomPrimer1' from this record model
        """
        return self.get_field_value(self.USESCUSTOMPRIMER1__FIELD_NAME.field_name)

    def set_UsesCustomPrimer2_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UsesCustomPrimer2' on this record model
        """
        self.set_field_value(self.USESCUSTOMPRIMER2__FIELD_NAME.field_name, value)

    def get_UsesCustomPrimer2_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UsesCustomPrimer2' from this record model
        """
        return self.get_field_value(self.USESCUSTOMPRIMER2__FIELD_NAME.field_name)


class IlluminaNextSeqSSSettingsModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaNextSeqSSSettings
    Data Type Display Name: Illumina NextSeq Sample Sheet Settings (Illumina NextSeq Sample Sheet Settings)
    Fields: Adapter, AdapterRead2, AdapterTrimmingStringency, Assay, CustomIndexPrimerMix, CustomRead1PrimerMix, CustomRead2PrimerMix, CyclesRead1, CyclesRead2, DateUnix, Description, ExperimentName, FilterOutSingleStrandVariants, IndexReads, InvestigatorName, PercentTilesToScan, QualityScoreTrim, ReadType, ReagentCartridgeBarcode, StitchReads, Workflow
    """
    DATA_TYPE_NAME: str = 'IlluminaNextSeqSSSettings'
    ADAPTER__FIELD_NAME: WrapperField = WrapperField("Adapter", FieldType.STRING)
    ADAPTERREAD2__FIELD_NAME: WrapperField = WrapperField("AdapterRead2", FieldType.STRING)
    ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME: WrapperField = WrapperField("AdapterTrimmingStringency", FieldType.STRING)
    ASSAY__FIELD_NAME: WrapperField = WrapperField("Assay", FieldType.STRING)
    CUSTOMINDEXPRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomIndexPrimerMix", FieldType.STRING)
    CUSTOMREAD1PRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomRead1PrimerMix", FieldType.STRING)
    CUSTOMREAD2PRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomRead2PrimerMix", FieldType.STRING)
    CYCLESREAD1__FIELD_NAME: WrapperField = WrapperField("CyclesRead1", FieldType.INTEGER)
    CYCLESREAD2__FIELD_NAME: WrapperField = WrapperField("CyclesRead2", FieldType.INTEGER)
    DATEUNIX__FIELD_NAME: WrapperField = WrapperField("DateUnix", FieldType.DATE)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    EXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("ExperimentName", FieldType.STRING)
    FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME: WrapperField = WrapperField("FilterOutSingleStrandVariants", FieldType.STRING)
    INDEXREADS__FIELD_NAME: WrapperField = WrapperField("IndexReads", FieldType.SHORT)
    INVESTIGATORNAME__FIELD_NAME: WrapperField = WrapperField("InvestigatorName", FieldType.STRING)
    PERCENTTILESTOSCAN__FIELD_NAME: WrapperField = WrapperField("PercentTilesToScan", FieldType.STRING)
    QUALITYSCORETRIM__FIELD_NAME: WrapperField = WrapperField("QualityScoreTrim", FieldType.STRING)
    READTYPE__FIELD_NAME: WrapperField = WrapperField("ReadType", FieldType.PICKLIST)
    REAGENTCARTRIDGEBARCODE__FIELD_NAME: WrapperField = WrapperField("ReagentCartridgeBarcode", FieldType.STRING)
    STITCHREADS__FIELD_NAME: WrapperField = WrapperField("StitchReads", FieldType.BOOLEAN)
    WORKFLOW__FIELD_NAME: WrapperField = WrapperField("Workflow", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Adapter_field(self, value: Optional[str]):
        """
        Set data field with field name 'Adapter' on this record model
        """
        self.set_field_value(self.ADAPTER__FIELD_NAME.field_name, value)

    def get_Adapter_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Adapter' from this record model
        """
        return self.get_field_value(self.ADAPTER__FIELD_NAME.field_name)

    def set_AdapterRead2_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdapterRead2' on this record model
        """
        self.set_field_value(self.ADAPTERREAD2__FIELD_NAME.field_name, value)

    def get_AdapterRead2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdapterRead2' from this record model
        """
        return self.get_field_value(self.ADAPTERREAD2__FIELD_NAME.field_name)

    def set_AdapterTrimmingStringency_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdapterTrimmingStringency' on this record model
        """
        self.set_field_value(self.ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME.field_name, value)

    def get_AdapterTrimmingStringency_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdapterTrimmingStringency' from this record model
        """
        return self.get_field_value(self.ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME.field_name)

    def set_Assay_field(self, value: Optional[str]):
        """
        Set data field with field name 'Assay' on this record model
        """
        self.set_field_value(self.ASSAY__FIELD_NAME.field_name, value)

    def get_Assay_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Assay' from this record model
        """
        return self.get_field_value(self.ASSAY__FIELD_NAME.field_name)

    def set_CustomIndexPrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomIndexPrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMINDEXPRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomIndexPrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomIndexPrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMINDEXPRIMERMIX__FIELD_NAME.field_name)

    def set_CustomRead1PrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomRead1PrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMREAD1PRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomRead1PrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomRead1PrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMREAD1PRIMERMIX__FIELD_NAME.field_name)

    def set_CustomRead2PrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomRead2PrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMREAD2PRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomRead2PrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomRead2PrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMREAD2PRIMERMIX__FIELD_NAME.field_name)

    def set_CyclesRead1_field(self, value: Optional[int]):
        """
        Set data field with field name 'CyclesRead1' on this record model
        """
        self.set_field_value(self.CYCLESREAD1__FIELD_NAME.field_name, value)

    def get_CyclesRead1_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CyclesRead1' from this record model
        """
        return self.get_field_value(self.CYCLESREAD1__FIELD_NAME.field_name)

    def set_CyclesRead2_field(self, value: Optional[int]):
        """
        Set data field with field name 'CyclesRead2' on this record model
        """
        self.set_field_value(self.CYCLESREAD2__FIELD_NAME.field_name, value)

    def get_CyclesRead2_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CyclesRead2' from this record model
        """
        return self.get_field_value(self.CYCLESREAD2__FIELD_NAME.field_name)

    def set_DateUnix_field(self, value: Optional[int]):
        """
        Set data field with field name 'DateUnix' on this record model
        """
        self.set_field_value(self.DATEUNIX__FIELD_NAME.field_name, value)

    def get_DateUnix_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DateUnix' from this record model
        """
        return self.get_field_value(self.DATEUNIX__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_ExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentName' on this record model
        """
        self.set_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_ExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentName' from this record model
        """
        return self.get_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name)

    def set_FilterOutSingleStrandVariants_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilterOutSingleStrandVariants' on this record model
        """
        self.set_field_value(self.FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME.field_name, value)

    def get_FilterOutSingleStrandVariants_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilterOutSingleStrandVariants' from this record model
        """
        return self.get_field_value(self.FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME.field_name)

    def set_IndexReads_field(self, value: Optional[int]):
        """
        Set data field with field name 'IndexReads' on this record model
        """
        self.set_field_value(self.INDEXREADS__FIELD_NAME.field_name, value)

    def get_IndexReads_field(self) -> Optional[int]:
        """
        Get data field value with field name 'IndexReads' from this record model
        """
        return self.get_field_value(self.INDEXREADS__FIELD_NAME.field_name)

    def set_InvestigatorName_field(self, value: Optional[str]):
        """
        Set data field with field name 'InvestigatorName' on this record model
        """
        self.set_field_value(self.INVESTIGATORNAME__FIELD_NAME.field_name, value)

    def get_InvestigatorName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InvestigatorName' from this record model
        """
        return self.get_field_value(self.INVESTIGATORNAME__FIELD_NAME.field_name)

    def set_PercentTilesToScan_field(self, value: Optional[str]):
        """
        Set data field with field name 'PercentTilesToScan' on this record model
        """
        self.set_field_value(self.PERCENTTILESTOSCAN__FIELD_NAME.field_name, value)

    def get_PercentTilesToScan_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PercentTilesToScan' from this record model
        """
        return self.get_field_value(self.PERCENTTILESTOSCAN__FIELD_NAME.field_name)

    def set_QualityScoreTrim_field(self, value: Optional[str]):
        """
        Set data field with field name 'QualityScoreTrim' on this record model
        """
        self.set_field_value(self.QUALITYSCORETRIM__FIELD_NAME.field_name, value)

    def get_QualityScoreTrim_field(self) -> Optional[str]:
        """
        Get data field value with field name 'QualityScoreTrim' from this record model
        """
        return self.get_field_value(self.QUALITYSCORETRIM__FIELD_NAME.field_name)

    def set_ReadType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReadType' on this record model
        """
        self.set_field_value(self.READTYPE__FIELD_NAME.field_name, value)

    def get_ReadType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReadType' from this record model
        """
        return self.get_field_value(self.READTYPE__FIELD_NAME.field_name)

    def set_ReagentCartridgeBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentCartridgeBarcode' on this record model
        """
        self.set_field_value(self.REAGENTCARTRIDGEBARCODE__FIELD_NAME.field_name, value)

    def get_ReagentCartridgeBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentCartridgeBarcode' from this record model
        """
        return self.get_field_value(self.REAGENTCARTRIDGEBARCODE__FIELD_NAME.field_name)

    def set_StitchReads_field(self, value: Optional[bool]):
        """
        Set data field with field name 'StitchReads' on this record model
        """
        self.set_field_value(self.STITCHREADS__FIELD_NAME.field_name, value)

    def get_StitchReads_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'StitchReads' from this record model
        """
        return self.get_field_value(self.STITCHREADS__FIELD_NAME.field_name)

    def set_Workflow_field(self, value: Optional[str]):
        """
        Set data field with field name 'Workflow' on this record model
        """
        self.set_field_value(self.WORKFLOW__FIELD_NAME.field_name, value)

    def get_Workflow_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Workflow' from this record model
        """
        return self.get_field_value(self.WORKFLOW__FIELD_NAME.field_name)


class IlluminaNovaSeqRunParametersModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaNovaSeqRunParameters
    Data Type Display Name: Illumina NovaSeq Run Parameters (Illumina NovaSeq Run Parameters)
    Fields: Application, ApplicationVersion, AttachmentFile, Autocenter, BiDirectionalScanning, BufferExpirationdate, BufferLotNumber, BufferNumberOfCyclesRemaining, BufferPartNumber, BufferRssi, BufferSerialBarcode, BufferStartDate, BufferSupportedModes, CeLinuxRunFolder, CeMountRunFolder, ClusterCycleKit, ClusterExpirationdate, ClusterLotNumber, ClusterNumberOfCyclesRemaining, ClusterPartNumber, ClusterRssi, ClusterSerialBarcode, ClusterStartDate, ClusterSupportedModes, ExperimentName, FlowCellExpirationdate, FlowCellLotNumber, FlowCellMode, FlowCellNumberOfReuseRemaining, FlowCellPartNumber, FlowCellRssi, FlowCellSerialBarcode, FlowCellStartDate, FlowCellSupportedModes, IndexRead1NumberOfCycles, IndexRead2NumberOfCycles, InstrumentName, IsRehyb, LibraryTubeExpirationdate, LibraryTubeLotNumber, LibraryTubePartNumber, LibraryTubeRssi, LibraryTubeSerialBarcode, LibraryTubeStartDate, LibraryTubeSupportedModes, OutputRunFolder, PlannedIndex1ReadCycles, PlannedIndex2ReadCycles, PlannedRead1Cycles, PlannedRead2Cycles, PlatformType, PreRunFolder, Read1NumberOfCycles, Read2NumberOfCycles, ReadType, RecipeFilePath, RecipeVersion, RtaRawRunFolder, RtaVersion, RunId, RunNumber, RunStartDate, SbcRunFolder, SbsCycleKit, SbsExpirationdate, SbsLotNumber, SbsNumberOfCyclesRemaining, SbsNumberOfCyclesSupported, SbsPartNumber, SbsRssi, SbsSerialBarcode, SbsStartDate, SbsSupportedModes, SendIlluminaHealthData, Side, Surface, UcsRunId, UcsVersion, UseCustomIndexRead1Primer, UseCustomRead1Primer, UseCustomRead2Primer
     <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'IlluminaNovaSeqRunParameters'
    APPLICATION__FIELD_NAME: WrapperField = WrapperField("Application", FieldType.STRING)
    APPLICATIONVERSION__FIELD_NAME: WrapperField = WrapperField("ApplicationVersion", FieldType.STRING)
    ATTACHMENTFILE__FIELD_NAME: WrapperField = WrapperField("AttachmentFile", FieldType.STRING)
    AUTOCENTER__FIELD_NAME: WrapperField = WrapperField("Autocenter", FieldType.BOOLEAN)
    BIDIRECTIONALSCANNING__FIELD_NAME: WrapperField = WrapperField("BiDirectionalScanning", FieldType.BOOLEAN)
    BUFFEREXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("BufferExpirationdate", FieldType.DATE)
    BUFFERLOTNUMBER__FIELD_NAME: WrapperField = WrapperField("BufferLotNumber", FieldType.INTEGER)
    BUFFERNUMBEROFCYCLESREMAINING__FIELD_NAME: WrapperField = WrapperField("BufferNumberOfCyclesRemaining", FieldType.INTEGER)
    BUFFERPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("BufferPartNumber", FieldType.INTEGER)
    BUFFERRSSI__FIELD_NAME: WrapperField = WrapperField("BufferRssi", FieldType.INTEGER)
    BUFFERSERIALBARCODE__FIELD_NAME: WrapperField = WrapperField("BufferSerialBarcode", FieldType.STRING)
    BUFFERSTARTDATE__FIELD_NAME: WrapperField = WrapperField("BufferStartDate", FieldType.DATE)
    BUFFERSUPPORTEDMODES__FIELD_NAME: WrapperField = WrapperField("BufferSupportedModes", FieldType.STRING)
    CELINUXRUNFOLDER__FIELD_NAME: WrapperField = WrapperField("CeLinuxRunFolder", FieldType.STRING)
    CEMOUNTRUNFOLDER__FIELD_NAME: WrapperField = WrapperField("CeMountRunFolder", FieldType.STRING)
    CLUSTERCYCLEKIT__FIELD_NAME: WrapperField = WrapperField("ClusterCycleKit", FieldType.INTEGER)
    CLUSTEREXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("ClusterExpirationdate", FieldType.DATE)
    CLUSTERLOTNUMBER__FIELD_NAME: WrapperField = WrapperField("ClusterLotNumber", FieldType.INTEGER)
    CLUSTERNUMBEROFCYCLESREMAINING__FIELD_NAME: WrapperField = WrapperField("ClusterNumberOfCyclesRemaining", FieldType.INTEGER)
    CLUSTERPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("ClusterPartNumber", FieldType.STRING)
    CLUSTERRSSI__FIELD_NAME: WrapperField = WrapperField("ClusterRssi", FieldType.INTEGER)
    CLUSTERSERIALBARCODE__FIELD_NAME: WrapperField = WrapperField("ClusterSerialBarcode", FieldType.STRING)
    CLUSTERSTARTDATE__FIELD_NAME: WrapperField = WrapperField("ClusterStartDate", FieldType.DATE)
    CLUSTERSUPPORTEDMODES__FIELD_NAME: WrapperField = WrapperField("ClusterSupportedModes", FieldType.STRING)
    EXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("ExperimentName", FieldType.STRING)
    FLOWCELLEXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("FlowCellExpirationdate", FieldType.DATE)
    FLOWCELLLOTNUMBER__FIELD_NAME: WrapperField = WrapperField("FlowCellLotNumber", FieldType.INTEGER)
    FLOWCELLMODE__FIELD_NAME: WrapperField = WrapperField("FlowCellMode", FieldType.STRING)
    FLOWCELLNUMBEROFREUSEREMAINING__FIELD_NAME: WrapperField = WrapperField("FlowCellNumberOfReuseRemaining", FieldType.INTEGER)
    FLOWCELLPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("FlowCellPartNumber", FieldType.STRING)
    FLOWCELLRSSI__FIELD_NAME: WrapperField = WrapperField("FlowCellRssi", FieldType.INTEGER)
    FLOWCELLSERIALBARCODE__FIELD_NAME: WrapperField = WrapperField("FlowCellSerialBarcode", FieldType.STRING)
    FLOWCELLSTARTDATE__FIELD_NAME: WrapperField = WrapperField("FlowCellStartDate", FieldType.DATE)
    FLOWCELLSUPPORTEDMODES__FIELD_NAME: WrapperField = WrapperField("FlowCellSupportedModes", FieldType.STRING)
    INDEXREAD1NUMBEROFCYCLES__FIELD_NAME: WrapperField = WrapperField("IndexRead1NumberOfCycles", FieldType.INTEGER)
    INDEXREAD2NUMBEROFCYCLES__FIELD_NAME: WrapperField = WrapperField("IndexRead2NumberOfCycles", FieldType.INTEGER)
    INSTRUMENTNAME__FIELD_NAME: WrapperField = WrapperField("InstrumentName", FieldType.STRING)
    ISREHYB__FIELD_NAME: WrapperField = WrapperField("IsRehyb", FieldType.BOOLEAN)
    LIBRARYTUBEEXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("LibraryTubeExpirationdate", FieldType.DATE)
    LIBRARYTUBELOTNUMBER__FIELD_NAME: WrapperField = WrapperField("LibraryTubeLotNumber", FieldType.INTEGER)
    LIBRARYTUBEPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("LibraryTubePartNumber", FieldType.INTEGER)
    LIBRARYTUBERSSI__FIELD_NAME: WrapperField = WrapperField("LibraryTubeRssi", FieldType.INTEGER)
    LIBRARYTUBESERIALBARCODE__FIELD_NAME: WrapperField = WrapperField("LibraryTubeSerialBarcode", FieldType.STRING)
    LIBRARYTUBESTARTDATE__FIELD_NAME: WrapperField = WrapperField("LibraryTubeStartDate", FieldType.DATE)
    LIBRARYTUBESUPPORTEDMODES__FIELD_NAME: WrapperField = WrapperField("LibraryTubeSupportedModes", FieldType.STRING)
    OUTPUTRUNFOLDER__FIELD_NAME: WrapperField = WrapperField("OutputRunFolder", FieldType.STRING)
    PLANNEDINDEX1READCYCLES__FIELD_NAME: WrapperField = WrapperField("PlannedIndex1ReadCycles", FieldType.INTEGER)
    PLANNEDINDEX2READCYCLES__FIELD_NAME: WrapperField = WrapperField("PlannedIndex2ReadCycles", FieldType.INTEGER)
    PLANNEDREAD1CYCLES__FIELD_NAME: WrapperField = WrapperField("PlannedRead1Cycles", FieldType.INTEGER)
    PLANNEDREAD2CYCLES__FIELD_NAME: WrapperField = WrapperField("PlannedRead2Cycles", FieldType.INTEGER)
    PLATFORMTYPE__FIELD_NAME: WrapperField = WrapperField("PlatformType", FieldType.STRING)
    PRERUNFOLDER__FIELD_NAME: WrapperField = WrapperField("PreRunFolder", FieldType.STRING)
    READ1NUMBEROFCYCLES__FIELD_NAME: WrapperField = WrapperField("Read1NumberOfCycles", FieldType.INTEGER)
    READ2NUMBEROFCYCLES__FIELD_NAME: WrapperField = WrapperField("Read2NumberOfCycles", FieldType.INTEGER)
    READTYPE__FIELD_NAME: WrapperField = WrapperField("ReadType", FieldType.STRING)
    RECIPEFILEPATH__FIELD_NAME: WrapperField = WrapperField("RecipeFilePath", FieldType.STRING)
    RECIPEVERSION__FIELD_NAME: WrapperField = WrapperField("RecipeVersion", FieldType.STRING)
    RTARAWRUNFOLDER__FIELD_NAME: WrapperField = WrapperField("RtaRawRunFolder", FieldType.STRING)
    RTAVERSION__FIELD_NAME: WrapperField = WrapperField("RtaVersion", FieldType.STRING)
    RUNID__FIELD_NAME: WrapperField = WrapperField("RunId", FieldType.STRING)
    RUNNUMBER__FIELD_NAME: WrapperField = WrapperField("RunNumber", FieldType.INTEGER)
    RUNSTARTDATE__FIELD_NAME: WrapperField = WrapperField("RunStartDate", FieldType.STRING)
    SBCRUNFOLDER__FIELD_NAME: WrapperField = WrapperField("SbcRunFolder", FieldType.STRING)
    SBSCYCLEKIT__FIELD_NAME: WrapperField = WrapperField("SbsCycleKit", FieldType.INTEGER)
    SBSEXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("SbsExpirationdate", FieldType.DATE)
    SBSLOTNUMBER__FIELD_NAME: WrapperField = WrapperField("SbsLotNumber", FieldType.INTEGER)
    SBSNUMBEROFCYCLESREMAINING__FIELD_NAME: WrapperField = WrapperField("SbsNumberOfCyclesRemaining", FieldType.INTEGER)
    SBSNUMBEROFCYCLESSUPPORTED__FIELD_NAME: WrapperField = WrapperField("SbsNumberOfCyclesSupported", FieldType.INTEGER)
    SBSPARTNUMBER__FIELD_NAME: WrapperField = WrapperField("SbsPartNumber", FieldType.STRING)
    SBSRSSI__FIELD_NAME: WrapperField = WrapperField("SbsRssi", FieldType.INTEGER)
    SBSSERIALBARCODE__FIELD_NAME: WrapperField = WrapperField("SbsSerialBarcode", FieldType.STRING)
    SBSSTARTDATE__FIELD_NAME: WrapperField = WrapperField("SbsStartDate", FieldType.DATE)
    SBSSUPPORTEDMODES__FIELD_NAME: WrapperField = WrapperField("SbsSupportedModes", FieldType.STRING)
    SENDILLUMINAHEALTHDATA__FIELD_NAME: WrapperField = WrapperField("SendIlluminaHealthData", FieldType.BOOLEAN)
    SIDE__FIELD_NAME: WrapperField = WrapperField("Side", FieldType.STRING)
    SURFACE__FIELD_NAME: WrapperField = WrapperField("Surface", FieldType.STRING)
    UCSRUNID__FIELD_NAME: WrapperField = WrapperField("UcsRunId", FieldType.STRING)
    UCSVERSION__FIELD_NAME: WrapperField = WrapperField("UcsVersion", FieldType.STRING)
    USECUSTOMINDEXREAD1PRIMER__FIELD_NAME: WrapperField = WrapperField("UseCustomIndexRead1Primer", FieldType.BOOLEAN)
    USECUSTOMREAD1PRIMER__FIELD_NAME: WrapperField = WrapperField("UseCustomRead1Primer", FieldType.BOOLEAN)
    USECUSTOMREAD2PRIMER__FIELD_NAME: WrapperField = WrapperField("UseCustomRead2Primer", FieldType.BOOLEAN)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Application_field(self, value: Optional[str]):
        """
        Set data field with field name 'Application' on this record model
        """
        self.set_field_value(self.APPLICATION__FIELD_NAME.field_name, value)

    def get_Application_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Application' from this record model
        """
        return self.get_field_value(self.APPLICATION__FIELD_NAME.field_name)

    def set_ApplicationVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApplicationVersion' on this record model
        """
        self.set_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name, value)

    def get_ApplicationVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApplicationVersion' from this record model
        """
        return self.get_field_value(self.APPLICATIONVERSION__FIELD_NAME.field_name)

    def set_AttachmentFile_field(self, value: Optional[str]):
        """
        Set data field with field name 'AttachmentFile' on this record model
        """
        self.set_field_value(self.ATTACHMENTFILE__FIELD_NAME.field_name, value)

    def get_AttachmentFile_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AttachmentFile' from this record model
        """
        return self.get_field_value(self.ATTACHMENTFILE__FIELD_NAME.field_name)

    def set_Autocenter_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Autocenter' on this record model
        """
        self.set_field_value(self.AUTOCENTER__FIELD_NAME.field_name, value)

    def get_Autocenter_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Autocenter' from this record model
        """
        return self.get_field_value(self.AUTOCENTER__FIELD_NAME.field_name)

    def set_BiDirectionalScanning_field(self, value: Optional[bool]):
        """
        Set data field with field name 'BiDirectionalScanning' on this record model
        """
        self.set_field_value(self.BIDIRECTIONALSCANNING__FIELD_NAME.field_name, value)

    def get_BiDirectionalScanning_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'BiDirectionalScanning' from this record model
        """
        return self.get_field_value(self.BIDIRECTIONALSCANNING__FIELD_NAME.field_name)

    def set_BufferExpirationdate_field(self, value: Optional[int]):
        """
        Set data field with field name 'BufferExpirationdate' on this record model
        """
        self.set_field_value(self.BUFFEREXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_BufferExpirationdate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BufferExpirationdate' from this record model
        """
        return self.get_field_value(self.BUFFEREXPIRATIONDATE__FIELD_NAME.field_name)

    def set_BufferLotNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'BufferLotNumber' on this record model
        """
        self.set_field_value(self.BUFFERLOTNUMBER__FIELD_NAME.field_name, value)

    def get_BufferLotNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BufferLotNumber' from this record model
        """
        return self.get_field_value(self.BUFFERLOTNUMBER__FIELD_NAME.field_name)

    def set_BufferNumberOfCyclesRemaining_field(self, value: Optional[int]):
        """
        Set data field with field name 'BufferNumberOfCyclesRemaining' on this record model
        """
        self.set_field_value(self.BUFFERNUMBEROFCYCLESREMAINING__FIELD_NAME.field_name, value)

    def get_BufferNumberOfCyclesRemaining_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BufferNumberOfCyclesRemaining' from this record model
        """
        return self.get_field_value(self.BUFFERNUMBEROFCYCLESREMAINING__FIELD_NAME.field_name)

    def set_BufferPartNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'BufferPartNumber' on this record model
        """
        self.set_field_value(self.BUFFERPARTNUMBER__FIELD_NAME.field_name, value)

    def get_BufferPartNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BufferPartNumber' from this record model
        """
        return self.get_field_value(self.BUFFERPARTNUMBER__FIELD_NAME.field_name)

    def set_BufferRssi_field(self, value: Optional[int]):
        """
        Set data field with field name 'BufferRssi' on this record model
        """
        self.set_field_value(self.BUFFERRSSI__FIELD_NAME.field_name, value)

    def get_BufferRssi_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BufferRssi' from this record model
        """
        return self.get_field_value(self.BUFFERRSSI__FIELD_NAME.field_name)

    def set_BufferSerialBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'BufferSerialBarcode' on this record model
        """
        self.set_field_value(self.BUFFERSERIALBARCODE__FIELD_NAME.field_name, value)

    def get_BufferSerialBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BufferSerialBarcode' from this record model
        """
        return self.get_field_value(self.BUFFERSERIALBARCODE__FIELD_NAME.field_name)

    def set_BufferStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'BufferStartDate' on this record model
        """
        self.set_field_value(self.BUFFERSTARTDATE__FIELD_NAME.field_name, value)

    def get_BufferStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BufferStartDate' from this record model
        """
        return self.get_field_value(self.BUFFERSTARTDATE__FIELD_NAME.field_name)

    def set_BufferSupportedModes_field(self, value: Optional[str]):
        """
        Set data field with field name 'BufferSupportedModes' on this record model
        """
        self.set_field_value(self.BUFFERSUPPORTEDMODES__FIELD_NAME.field_name, value)

    def get_BufferSupportedModes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BufferSupportedModes' from this record model
        """
        return self.get_field_value(self.BUFFERSUPPORTEDMODES__FIELD_NAME.field_name)

    def set_CeLinuxRunFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'CeLinuxRunFolder' on this record model
        """
        self.set_field_value(self.CELINUXRUNFOLDER__FIELD_NAME.field_name, value)

    def get_CeLinuxRunFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CeLinuxRunFolder' from this record model
        """
        return self.get_field_value(self.CELINUXRUNFOLDER__FIELD_NAME.field_name)

    def set_CeMountRunFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'CeMountRunFolder' on this record model
        """
        self.set_field_value(self.CEMOUNTRUNFOLDER__FIELD_NAME.field_name, value)

    def get_CeMountRunFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CeMountRunFolder' from this record model
        """
        return self.get_field_value(self.CEMOUNTRUNFOLDER__FIELD_NAME.field_name)

    def set_ClusterCycleKit_field(self, value: Optional[int]):
        """
        Set data field with field name 'ClusterCycleKit' on this record model
        """
        self.set_field_value(self.CLUSTERCYCLEKIT__FIELD_NAME.field_name, value)

    def get_ClusterCycleKit_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ClusterCycleKit' from this record model
        """
        return self.get_field_value(self.CLUSTERCYCLEKIT__FIELD_NAME.field_name)

    def set_ClusterExpirationdate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ClusterExpirationdate' on this record model
        """
        self.set_field_value(self.CLUSTEREXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_ClusterExpirationdate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ClusterExpirationdate' from this record model
        """
        return self.get_field_value(self.CLUSTEREXPIRATIONDATE__FIELD_NAME.field_name)

    def set_ClusterLotNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'ClusterLotNumber' on this record model
        """
        self.set_field_value(self.CLUSTERLOTNUMBER__FIELD_NAME.field_name, value)

    def get_ClusterLotNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ClusterLotNumber' from this record model
        """
        return self.get_field_value(self.CLUSTERLOTNUMBER__FIELD_NAME.field_name)

    def set_ClusterNumberOfCyclesRemaining_field(self, value: Optional[int]):
        """
        Set data field with field name 'ClusterNumberOfCyclesRemaining' on this record model
        """
        self.set_field_value(self.CLUSTERNUMBEROFCYCLESREMAINING__FIELD_NAME.field_name, value)

    def get_ClusterNumberOfCyclesRemaining_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ClusterNumberOfCyclesRemaining' from this record model
        """
        return self.get_field_value(self.CLUSTERNUMBEROFCYCLESREMAINING__FIELD_NAME.field_name)

    def set_ClusterPartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'ClusterPartNumber' on this record model
        """
        self.set_field_value(self.CLUSTERPARTNUMBER__FIELD_NAME.field_name, value)

    def get_ClusterPartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ClusterPartNumber' from this record model
        """
        return self.get_field_value(self.CLUSTERPARTNUMBER__FIELD_NAME.field_name)

    def set_ClusterRssi_field(self, value: Optional[int]):
        """
        Set data field with field name 'ClusterRssi' on this record model
        """
        self.set_field_value(self.CLUSTERRSSI__FIELD_NAME.field_name, value)

    def get_ClusterRssi_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ClusterRssi' from this record model
        """
        return self.get_field_value(self.CLUSTERRSSI__FIELD_NAME.field_name)

    def set_ClusterSerialBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'ClusterSerialBarcode' on this record model
        """
        self.set_field_value(self.CLUSTERSERIALBARCODE__FIELD_NAME.field_name, value)

    def get_ClusterSerialBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ClusterSerialBarcode' from this record model
        """
        return self.get_field_value(self.CLUSTERSERIALBARCODE__FIELD_NAME.field_name)

    def set_ClusterStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ClusterStartDate' on this record model
        """
        self.set_field_value(self.CLUSTERSTARTDATE__FIELD_NAME.field_name, value)

    def get_ClusterStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ClusterStartDate' from this record model
        """
        return self.get_field_value(self.CLUSTERSTARTDATE__FIELD_NAME.field_name)

    def set_ClusterSupportedModes_field(self, value: Optional[str]):
        """
        Set data field with field name 'ClusterSupportedModes' on this record model
        """
        self.set_field_value(self.CLUSTERSUPPORTEDMODES__FIELD_NAME.field_name, value)

    def get_ClusterSupportedModes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ClusterSupportedModes' from this record model
        """
        return self.get_field_value(self.CLUSTERSUPPORTEDMODES__FIELD_NAME.field_name)

    def set_ExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentName' on this record model
        """
        self.set_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_ExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentName' from this record model
        """
        return self.get_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name)

    def set_FlowCellExpirationdate_field(self, value: Optional[int]):
        """
        Set data field with field name 'FlowCellExpirationdate' on this record model
        """
        self.set_field_value(self.FLOWCELLEXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_FlowCellExpirationdate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FlowCellExpirationdate' from this record model
        """
        return self.get_field_value(self.FLOWCELLEXPIRATIONDATE__FIELD_NAME.field_name)

    def set_FlowCellLotNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'FlowCellLotNumber' on this record model
        """
        self.set_field_value(self.FLOWCELLLOTNUMBER__FIELD_NAME.field_name, value)

    def get_FlowCellLotNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FlowCellLotNumber' from this record model
        """
        return self.get_field_value(self.FLOWCELLLOTNUMBER__FIELD_NAME.field_name)

    def set_FlowCellMode_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowCellMode' on this record model
        """
        self.set_field_value(self.FLOWCELLMODE__FIELD_NAME.field_name, value)

    def get_FlowCellMode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowCellMode' from this record model
        """
        return self.get_field_value(self.FLOWCELLMODE__FIELD_NAME.field_name)

    def set_FlowCellNumberOfReuseRemaining_field(self, value: Optional[int]):
        """
        Set data field with field name 'FlowCellNumberOfReuseRemaining' on this record model
        """
        self.set_field_value(self.FLOWCELLNUMBEROFREUSEREMAINING__FIELD_NAME.field_name, value)

    def get_FlowCellNumberOfReuseRemaining_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FlowCellNumberOfReuseRemaining' from this record model
        """
        return self.get_field_value(self.FLOWCELLNUMBEROFREUSEREMAINING__FIELD_NAME.field_name)

    def set_FlowCellPartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowCellPartNumber' on this record model
        """
        self.set_field_value(self.FLOWCELLPARTNUMBER__FIELD_NAME.field_name, value)

    def get_FlowCellPartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowCellPartNumber' from this record model
        """
        return self.get_field_value(self.FLOWCELLPARTNUMBER__FIELD_NAME.field_name)

    def set_FlowCellRssi_field(self, value: Optional[int]):
        """
        Set data field with field name 'FlowCellRssi' on this record model
        """
        self.set_field_value(self.FLOWCELLRSSI__FIELD_NAME.field_name, value)

    def get_FlowCellRssi_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FlowCellRssi' from this record model
        """
        return self.get_field_value(self.FLOWCELLRSSI__FIELD_NAME.field_name)

    def set_FlowCellSerialBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowCellSerialBarcode' on this record model
        """
        self.set_field_value(self.FLOWCELLSERIALBARCODE__FIELD_NAME.field_name, value)

    def get_FlowCellSerialBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowCellSerialBarcode' from this record model
        """
        return self.get_field_value(self.FLOWCELLSERIALBARCODE__FIELD_NAME.field_name)

    def set_FlowCellStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'FlowCellStartDate' on this record model
        """
        self.set_field_value(self.FLOWCELLSTARTDATE__FIELD_NAME.field_name, value)

    def get_FlowCellStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'FlowCellStartDate' from this record model
        """
        return self.get_field_value(self.FLOWCELLSTARTDATE__FIELD_NAME.field_name)

    def set_FlowCellSupportedModes_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowCellSupportedModes' on this record model
        """
        self.set_field_value(self.FLOWCELLSUPPORTEDMODES__FIELD_NAME.field_name, value)

    def get_FlowCellSupportedModes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowCellSupportedModes' from this record model
        """
        return self.get_field_value(self.FLOWCELLSUPPORTEDMODES__FIELD_NAME.field_name)

    def set_IndexRead1NumberOfCycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'IndexRead1NumberOfCycles' on this record model
        """
        self.set_field_value(self.INDEXREAD1NUMBEROFCYCLES__FIELD_NAME.field_name, value)

    def get_IndexRead1NumberOfCycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'IndexRead1NumberOfCycles' from this record model
        """
        return self.get_field_value(self.INDEXREAD1NUMBEROFCYCLES__FIELD_NAME.field_name)

    def set_IndexRead2NumberOfCycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'IndexRead2NumberOfCycles' on this record model
        """
        self.set_field_value(self.INDEXREAD2NUMBEROFCYCLES__FIELD_NAME.field_name, value)

    def get_IndexRead2NumberOfCycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'IndexRead2NumberOfCycles' from this record model
        """
        return self.get_field_value(self.INDEXREAD2NUMBEROFCYCLES__FIELD_NAME.field_name)

    def set_InstrumentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentName' on this record model
        """
        self.set_field_value(self.INSTRUMENTNAME__FIELD_NAME.field_name, value)

    def get_InstrumentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentName' from this record model
        """
        return self.get_field_value(self.INSTRUMENTNAME__FIELD_NAME.field_name)

    def set_IsRehyb_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsRehyb' on this record model
        """
        self.set_field_value(self.ISREHYB__FIELD_NAME.field_name, value)

    def get_IsRehyb_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsRehyb' from this record model
        """
        return self.get_field_value(self.ISREHYB__FIELD_NAME.field_name)

    def set_LibraryTubeExpirationdate_field(self, value: Optional[int]):
        """
        Set data field with field name 'LibraryTubeExpirationdate' on this record model
        """
        self.set_field_value(self.LIBRARYTUBEEXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_LibraryTubeExpirationdate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LibraryTubeExpirationdate' from this record model
        """
        return self.get_field_value(self.LIBRARYTUBEEXPIRATIONDATE__FIELD_NAME.field_name)

    def set_LibraryTubeLotNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'LibraryTubeLotNumber' on this record model
        """
        self.set_field_value(self.LIBRARYTUBELOTNUMBER__FIELD_NAME.field_name, value)

    def get_LibraryTubeLotNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LibraryTubeLotNumber' from this record model
        """
        return self.get_field_value(self.LIBRARYTUBELOTNUMBER__FIELD_NAME.field_name)

    def set_LibraryTubePartNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'LibraryTubePartNumber' on this record model
        """
        self.set_field_value(self.LIBRARYTUBEPARTNUMBER__FIELD_NAME.field_name, value)

    def get_LibraryTubePartNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LibraryTubePartNumber' from this record model
        """
        return self.get_field_value(self.LIBRARYTUBEPARTNUMBER__FIELD_NAME.field_name)

    def set_LibraryTubeRssi_field(self, value: Optional[int]):
        """
        Set data field with field name 'LibraryTubeRssi' on this record model
        """
        self.set_field_value(self.LIBRARYTUBERSSI__FIELD_NAME.field_name, value)

    def get_LibraryTubeRssi_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LibraryTubeRssi' from this record model
        """
        return self.get_field_value(self.LIBRARYTUBERSSI__FIELD_NAME.field_name)

    def set_LibraryTubeSerialBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'LibraryTubeSerialBarcode' on this record model
        """
        self.set_field_value(self.LIBRARYTUBESERIALBARCODE__FIELD_NAME.field_name, value)

    def get_LibraryTubeSerialBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LibraryTubeSerialBarcode' from this record model
        """
        return self.get_field_value(self.LIBRARYTUBESERIALBARCODE__FIELD_NAME.field_name)

    def set_LibraryTubeStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'LibraryTubeStartDate' on this record model
        """
        self.set_field_value(self.LIBRARYTUBESTARTDATE__FIELD_NAME.field_name, value)

    def get_LibraryTubeStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LibraryTubeStartDate' from this record model
        """
        return self.get_field_value(self.LIBRARYTUBESTARTDATE__FIELD_NAME.field_name)

    def set_LibraryTubeSupportedModes_field(self, value: Optional[str]):
        """
        Set data field with field name 'LibraryTubeSupportedModes' on this record model
        """
        self.set_field_value(self.LIBRARYTUBESUPPORTEDMODES__FIELD_NAME.field_name, value)

    def get_LibraryTubeSupportedModes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LibraryTubeSupportedModes' from this record model
        """
        return self.get_field_value(self.LIBRARYTUBESUPPORTEDMODES__FIELD_NAME.field_name)

    def set_OutputRunFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'OutputRunFolder' on this record model
        """
        self.set_field_value(self.OUTPUTRUNFOLDER__FIELD_NAME.field_name, value)

    def get_OutputRunFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OutputRunFolder' from this record model
        """
        return self.get_field_value(self.OUTPUTRUNFOLDER__FIELD_NAME.field_name)

    def set_PlannedIndex1ReadCycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlannedIndex1ReadCycles' on this record model
        """
        self.set_field_value(self.PLANNEDINDEX1READCYCLES__FIELD_NAME.field_name, value)

    def get_PlannedIndex1ReadCycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlannedIndex1ReadCycles' from this record model
        """
        return self.get_field_value(self.PLANNEDINDEX1READCYCLES__FIELD_NAME.field_name)

    def set_PlannedIndex2ReadCycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlannedIndex2ReadCycles' on this record model
        """
        self.set_field_value(self.PLANNEDINDEX2READCYCLES__FIELD_NAME.field_name, value)

    def get_PlannedIndex2ReadCycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlannedIndex2ReadCycles' from this record model
        """
        return self.get_field_value(self.PLANNEDINDEX2READCYCLES__FIELD_NAME.field_name)

    def set_PlannedRead1Cycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlannedRead1Cycles' on this record model
        """
        self.set_field_value(self.PLANNEDREAD1CYCLES__FIELD_NAME.field_name, value)

    def get_PlannedRead1Cycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlannedRead1Cycles' from this record model
        """
        return self.get_field_value(self.PLANNEDREAD1CYCLES__FIELD_NAME.field_name)

    def set_PlannedRead2Cycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlannedRead2Cycles' on this record model
        """
        self.set_field_value(self.PLANNEDREAD2CYCLES__FIELD_NAME.field_name, value)

    def get_PlannedRead2Cycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlannedRead2Cycles' from this record model
        """
        return self.get_field_value(self.PLANNEDREAD2CYCLES__FIELD_NAME.field_name)

    def set_PlatformType_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlatformType' on this record model
        """
        self.set_field_value(self.PLATFORMTYPE__FIELD_NAME.field_name, value)

    def get_PlatformType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlatformType' from this record model
        """
        return self.get_field_value(self.PLATFORMTYPE__FIELD_NAME.field_name)

    def set_PreRunFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'PreRunFolder' on this record model
        """
        self.set_field_value(self.PRERUNFOLDER__FIELD_NAME.field_name, value)

    def get_PreRunFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PreRunFolder' from this record model
        """
        return self.get_field_value(self.PRERUNFOLDER__FIELD_NAME.field_name)

    def set_Read1NumberOfCycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'Read1NumberOfCycles' on this record model
        """
        self.set_field_value(self.READ1NUMBEROFCYCLES__FIELD_NAME.field_name, value)

    def get_Read1NumberOfCycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Read1NumberOfCycles' from this record model
        """
        return self.get_field_value(self.READ1NUMBEROFCYCLES__FIELD_NAME.field_name)

    def set_Read2NumberOfCycles_field(self, value: Optional[int]):
        """
        Set data field with field name 'Read2NumberOfCycles' on this record model
        """
        self.set_field_value(self.READ2NUMBEROFCYCLES__FIELD_NAME.field_name, value)

    def get_Read2NumberOfCycles_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Read2NumberOfCycles' from this record model
        """
        return self.get_field_value(self.READ2NUMBEROFCYCLES__FIELD_NAME.field_name)

    def set_ReadType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReadType' on this record model
        """
        self.set_field_value(self.READTYPE__FIELD_NAME.field_name, value)

    def get_ReadType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReadType' from this record model
        """
        return self.get_field_value(self.READTYPE__FIELD_NAME.field_name)

    def set_RecipeFilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecipeFilePath' on this record model
        """
        self.set_field_value(self.RECIPEFILEPATH__FIELD_NAME.field_name, value)

    def get_RecipeFilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecipeFilePath' from this record model
        """
        return self.get_field_value(self.RECIPEFILEPATH__FIELD_NAME.field_name)

    def set_RecipeVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecipeVersion' on this record model
        """
        self.set_field_value(self.RECIPEVERSION__FIELD_NAME.field_name, value)

    def get_RecipeVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecipeVersion' from this record model
        """
        return self.get_field_value(self.RECIPEVERSION__FIELD_NAME.field_name)

    def set_RtaRawRunFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'RtaRawRunFolder' on this record model
        """
        self.set_field_value(self.RTARAWRUNFOLDER__FIELD_NAME.field_name, value)

    def get_RtaRawRunFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RtaRawRunFolder' from this record model
        """
        return self.get_field_value(self.RTARAWRUNFOLDER__FIELD_NAME.field_name)

    def set_RtaVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'RtaVersion' on this record model
        """
        self.set_field_value(self.RTAVERSION__FIELD_NAME.field_name, value)

    def get_RtaVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RtaVersion' from this record model
        """
        return self.get_field_value(self.RTAVERSION__FIELD_NAME.field_name)

    def set_RunId_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunId' on this record model
        """
        self.set_field_value(self.RUNID__FIELD_NAME.field_name, value)

    def get_RunId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunId' from this record model
        """
        return self.get_field_value(self.RUNID__FIELD_NAME.field_name)

    def set_RunNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunNumber' on this record model
        """
        self.set_field_value(self.RUNNUMBER__FIELD_NAME.field_name, value)

    def get_RunNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunNumber' from this record model
        """
        return self.get_field_value(self.RUNNUMBER__FIELD_NAME.field_name)

    def set_RunStartDate_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunStartDate' on this record model
        """
        self.set_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name, value)

    def get_RunStartDate_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunStartDate' from this record model
        """
        return self.get_field_value(self.RUNSTARTDATE__FIELD_NAME.field_name)

    def set_SbcRunFolder_field(self, value: Optional[str]):
        """
        Set data field with field name 'SbcRunFolder' on this record model
        """
        self.set_field_value(self.SBCRUNFOLDER__FIELD_NAME.field_name, value)

    def get_SbcRunFolder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SbcRunFolder' from this record model
        """
        return self.get_field_value(self.SBCRUNFOLDER__FIELD_NAME.field_name)

    def set_SbsCycleKit_field(self, value: Optional[int]):
        """
        Set data field with field name 'SbsCycleKit' on this record model
        """
        self.set_field_value(self.SBSCYCLEKIT__FIELD_NAME.field_name, value)

    def get_SbsCycleKit_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SbsCycleKit' from this record model
        """
        return self.get_field_value(self.SBSCYCLEKIT__FIELD_NAME.field_name)

    def set_SbsExpirationdate_field(self, value: Optional[int]):
        """
        Set data field with field name 'SbsExpirationdate' on this record model
        """
        self.set_field_value(self.SBSEXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_SbsExpirationdate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SbsExpirationdate' from this record model
        """
        return self.get_field_value(self.SBSEXPIRATIONDATE__FIELD_NAME.field_name)

    def set_SbsLotNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'SbsLotNumber' on this record model
        """
        self.set_field_value(self.SBSLOTNUMBER__FIELD_NAME.field_name, value)

    def get_SbsLotNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SbsLotNumber' from this record model
        """
        return self.get_field_value(self.SBSLOTNUMBER__FIELD_NAME.field_name)

    def set_SbsNumberOfCyclesRemaining_field(self, value: Optional[int]):
        """
        Set data field with field name 'SbsNumberOfCyclesRemaining' on this record model
        """
        self.set_field_value(self.SBSNUMBEROFCYCLESREMAINING__FIELD_NAME.field_name, value)

    def get_SbsNumberOfCyclesRemaining_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SbsNumberOfCyclesRemaining' from this record model
        """
        return self.get_field_value(self.SBSNUMBEROFCYCLESREMAINING__FIELD_NAME.field_name)

    def set_SbsNumberOfCyclesSupported_field(self, value: Optional[int]):
        """
        Set data field with field name 'SbsNumberOfCyclesSupported' on this record model
        """
        self.set_field_value(self.SBSNUMBEROFCYCLESSUPPORTED__FIELD_NAME.field_name, value)

    def get_SbsNumberOfCyclesSupported_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SbsNumberOfCyclesSupported' from this record model
        """
        return self.get_field_value(self.SBSNUMBEROFCYCLESSUPPORTED__FIELD_NAME.field_name)

    def set_SbsPartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'SbsPartNumber' on this record model
        """
        self.set_field_value(self.SBSPARTNUMBER__FIELD_NAME.field_name, value)

    def get_SbsPartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SbsPartNumber' from this record model
        """
        return self.get_field_value(self.SBSPARTNUMBER__FIELD_NAME.field_name)

    def set_SbsRssi_field(self, value: Optional[int]):
        """
        Set data field with field name 'SbsRssi' on this record model
        """
        self.set_field_value(self.SBSRSSI__FIELD_NAME.field_name, value)

    def get_SbsRssi_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SbsRssi' from this record model
        """
        return self.get_field_value(self.SBSRSSI__FIELD_NAME.field_name)

    def set_SbsSerialBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'SbsSerialBarcode' on this record model
        """
        self.set_field_value(self.SBSSERIALBARCODE__FIELD_NAME.field_name, value)

    def get_SbsSerialBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SbsSerialBarcode' from this record model
        """
        return self.get_field_value(self.SBSSERIALBARCODE__FIELD_NAME.field_name)

    def set_SbsStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'SbsStartDate' on this record model
        """
        self.set_field_value(self.SBSSTARTDATE__FIELD_NAME.field_name, value)

    def get_SbsStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SbsStartDate' from this record model
        """
        return self.get_field_value(self.SBSSTARTDATE__FIELD_NAME.field_name)

    def set_SbsSupportedModes_field(self, value: Optional[str]):
        """
        Set data field with field name 'SbsSupportedModes' on this record model
        """
        self.set_field_value(self.SBSSUPPORTEDMODES__FIELD_NAME.field_name, value)

    def get_SbsSupportedModes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SbsSupportedModes' from this record model
        """
        return self.get_field_value(self.SBSSUPPORTEDMODES__FIELD_NAME.field_name)

    def set_SendIlluminaHealthData_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SendIlluminaHealthData' on this record model
        """
        self.set_field_value(self.SENDILLUMINAHEALTHDATA__FIELD_NAME.field_name, value)

    def get_SendIlluminaHealthData_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SendIlluminaHealthData' from this record model
        """
        return self.get_field_value(self.SENDILLUMINAHEALTHDATA__FIELD_NAME.field_name)

    def set_Side_field(self, value: Optional[str]):
        """
        Set data field with field name 'Side' on this record model
        """
        self.set_field_value(self.SIDE__FIELD_NAME.field_name, value)

    def get_Side_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Side' from this record model
        """
        return self.get_field_value(self.SIDE__FIELD_NAME.field_name)

    def set_Surface_field(self, value: Optional[str]):
        """
        Set data field with field name 'Surface' on this record model
        """
        self.set_field_value(self.SURFACE__FIELD_NAME.field_name, value)

    def get_Surface_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Surface' from this record model
        """
        return self.get_field_value(self.SURFACE__FIELD_NAME.field_name)

    def set_UcsRunId_field(self, value: Optional[str]):
        """
        Set data field with field name 'UcsRunId' on this record model
        """
        self.set_field_value(self.UCSRUNID__FIELD_NAME.field_name, value)

    def get_UcsRunId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UcsRunId' from this record model
        """
        return self.get_field_value(self.UCSRUNID__FIELD_NAME.field_name)

    def set_UcsVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'UcsVersion' on this record model
        """
        self.set_field_value(self.UCSVERSION__FIELD_NAME.field_name, value)

    def get_UcsVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UcsVersion' from this record model
        """
        return self.get_field_value(self.UCSVERSION__FIELD_NAME.field_name)

    def set_UseCustomIndexRead1Primer_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UseCustomIndexRead1Primer' on this record model
        """
        self.set_field_value(self.USECUSTOMINDEXREAD1PRIMER__FIELD_NAME.field_name, value)

    def get_UseCustomIndexRead1Primer_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UseCustomIndexRead1Primer' from this record model
        """
        return self.get_field_value(self.USECUSTOMINDEXREAD1PRIMER__FIELD_NAME.field_name)

    def set_UseCustomRead1Primer_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UseCustomRead1Primer' on this record model
        """
        self.set_field_value(self.USECUSTOMREAD1PRIMER__FIELD_NAME.field_name, value)

    def get_UseCustomRead1Primer_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UseCustomRead1Primer' from this record model
        """
        return self.get_field_value(self.USECUSTOMREAD1PRIMER__FIELD_NAME.field_name)

    def set_UseCustomRead2Primer_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UseCustomRead2Primer' on this record model
        """
        self.set_field_value(self.USECUSTOMREAD2PRIMER__FIELD_NAME.field_name, value)

    def get_UseCustomRead2Primer_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UseCustomRead2Primer' from this record model
        """
        return self.get_field_value(self.USECUSTOMREAD2PRIMER__FIELD_NAME.field_name)


class IlluminaNovaSeqSSSettingsModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaNovaSeqSSSettings
    Data Type Display Name: Illumina NovaSeq Sample Sheet Settings (Illumina NovaSeq Sample Sheet Settings)
    Fields: Adapter, AdapterRead2, AdapterTrimmingStringency, Assay, CustomIndexPrimerMix, CustomRead1PrimerMix, CustomRead2PrimerMix, CyclesRead1, CyclesRead2, DateUnix, Description, ExperimentName, FilterOutSingleStrandVariants, IndexReads, InvestigatorName, PercentTilesToScan, QualityScoreTrim, ReadType, ReagentCartridgeBarcode, StitchReads, Workflow
    """
    DATA_TYPE_NAME: str = 'IlluminaNovaSeqSSSettings'
    ADAPTER__FIELD_NAME: WrapperField = WrapperField("Adapter", FieldType.STRING)
    ADAPTERREAD2__FIELD_NAME: WrapperField = WrapperField("AdapterRead2", FieldType.STRING)
    ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME: WrapperField = WrapperField("AdapterTrimmingStringency", FieldType.STRING)
    ASSAY__FIELD_NAME: WrapperField = WrapperField("Assay", FieldType.STRING)
    CUSTOMINDEXPRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomIndexPrimerMix", FieldType.STRING)
    CUSTOMREAD1PRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomRead1PrimerMix", FieldType.STRING)
    CUSTOMREAD2PRIMERMIX__FIELD_NAME: WrapperField = WrapperField("CustomRead2PrimerMix", FieldType.STRING)
    CYCLESREAD1__FIELD_NAME: WrapperField = WrapperField("CyclesRead1", FieldType.INTEGER)
    CYCLESREAD2__FIELD_NAME: WrapperField = WrapperField("CyclesRead2", FieldType.INTEGER)
    DATEUNIX__FIELD_NAME: WrapperField = WrapperField("DateUnix", FieldType.DATE)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    EXPERIMENTNAME__FIELD_NAME: WrapperField = WrapperField("ExperimentName", FieldType.STRING)
    FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME: WrapperField = WrapperField("FilterOutSingleStrandVariants", FieldType.STRING)
    INDEXREADS__FIELD_NAME: WrapperField = WrapperField("IndexReads", FieldType.SHORT)
    INVESTIGATORNAME__FIELD_NAME: WrapperField = WrapperField("InvestigatorName", FieldType.STRING)
    PERCENTTILESTOSCAN__FIELD_NAME: WrapperField = WrapperField("PercentTilesToScan", FieldType.STRING)
    QUALITYSCORETRIM__FIELD_NAME: WrapperField = WrapperField("QualityScoreTrim", FieldType.STRING)
    READTYPE__FIELD_NAME: WrapperField = WrapperField("ReadType", FieldType.PICKLIST)
    REAGENTCARTRIDGEBARCODE__FIELD_NAME: WrapperField = WrapperField("ReagentCartridgeBarcode", FieldType.STRING)
    STITCHREADS__FIELD_NAME: WrapperField = WrapperField("StitchReads", FieldType.BOOLEAN)
    WORKFLOW__FIELD_NAME: WrapperField = WrapperField("Workflow", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Adapter_field(self, value: Optional[str]):
        """
        Set data field with field name 'Adapter' on this record model
        """
        self.set_field_value(self.ADAPTER__FIELD_NAME.field_name, value)

    def get_Adapter_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Adapter' from this record model
        """
        return self.get_field_value(self.ADAPTER__FIELD_NAME.field_name)

    def set_AdapterRead2_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdapterRead2' on this record model
        """
        self.set_field_value(self.ADAPTERREAD2__FIELD_NAME.field_name, value)

    def get_AdapterRead2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdapterRead2' from this record model
        """
        return self.get_field_value(self.ADAPTERREAD2__FIELD_NAME.field_name)

    def set_AdapterTrimmingStringency_field(self, value: Optional[str]):
        """
        Set data field with field name 'AdapterTrimmingStringency' on this record model
        """
        self.set_field_value(self.ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME.field_name, value)

    def get_AdapterTrimmingStringency_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AdapterTrimmingStringency' from this record model
        """
        return self.get_field_value(self.ADAPTERTRIMMINGSTRINGENCY__FIELD_NAME.field_name)

    def set_Assay_field(self, value: Optional[str]):
        """
        Set data field with field name 'Assay' on this record model
        """
        self.set_field_value(self.ASSAY__FIELD_NAME.field_name, value)

    def get_Assay_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Assay' from this record model
        """
        return self.get_field_value(self.ASSAY__FIELD_NAME.field_name)

    def set_CustomIndexPrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomIndexPrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMINDEXPRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomIndexPrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomIndexPrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMINDEXPRIMERMIX__FIELD_NAME.field_name)

    def set_CustomRead1PrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomRead1PrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMREAD1PRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomRead1PrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomRead1PrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMREAD1PRIMERMIX__FIELD_NAME.field_name)

    def set_CustomRead2PrimerMix_field(self, value: Optional[str]):
        """
        Set data field with field name 'CustomRead2PrimerMix' on this record model
        """
        self.set_field_value(self.CUSTOMREAD2PRIMERMIX__FIELD_NAME.field_name, value)

    def get_CustomRead2PrimerMix_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CustomRead2PrimerMix' from this record model
        """
        return self.get_field_value(self.CUSTOMREAD2PRIMERMIX__FIELD_NAME.field_name)

    def set_CyclesRead1_field(self, value: Optional[int]):
        """
        Set data field with field name 'CyclesRead1' on this record model
        """
        self.set_field_value(self.CYCLESREAD1__FIELD_NAME.field_name, value)

    def get_CyclesRead1_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CyclesRead1' from this record model
        """
        return self.get_field_value(self.CYCLESREAD1__FIELD_NAME.field_name)

    def set_CyclesRead2_field(self, value: Optional[int]):
        """
        Set data field with field name 'CyclesRead2' on this record model
        """
        self.set_field_value(self.CYCLESREAD2__FIELD_NAME.field_name, value)

    def get_CyclesRead2_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CyclesRead2' from this record model
        """
        return self.get_field_value(self.CYCLESREAD2__FIELD_NAME.field_name)

    def set_DateUnix_field(self, value: Optional[int]):
        """
        Set data field with field name 'DateUnix' on this record model
        """
        self.set_field_value(self.DATEUNIX__FIELD_NAME.field_name, value)

    def get_DateUnix_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DateUnix' from this record model
        """
        return self.get_field_value(self.DATEUNIX__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_ExperimentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExperimentName' on this record model
        """
        self.set_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name, value)

    def get_ExperimentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExperimentName' from this record model
        """
        return self.get_field_value(self.EXPERIMENTNAME__FIELD_NAME.field_name)

    def set_FilterOutSingleStrandVariants_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilterOutSingleStrandVariants' on this record model
        """
        self.set_field_value(self.FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME.field_name, value)

    def get_FilterOutSingleStrandVariants_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilterOutSingleStrandVariants' from this record model
        """
        return self.get_field_value(self.FILTEROUTSINGLESTRANDVARIANTS__FIELD_NAME.field_name)

    def set_IndexReads_field(self, value: Optional[int]):
        """
        Set data field with field name 'IndexReads' on this record model
        """
        self.set_field_value(self.INDEXREADS__FIELD_NAME.field_name, value)

    def get_IndexReads_field(self) -> Optional[int]:
        """
        Get data field value with field name 'IndexReads' from this record model
        """
        return self.get_field_value(self.INDEXREADS__FIELD_NAME.field_name)

    def set_InvestigatorName_field(self, value: Optional[str]):
        """
        Set data field with field name 'InvestigatorName' on this record model
        """
        self.set_field_value(self.INVESTIGATORNAME__FIELD_NAME.field_name, value)

    def get_InvestigatorName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InvestigatorName' from this record model
        """
        return self.get_field_value(self.INVESTIGATORNAME__FIELD_NAME.field_name)

    def set_PercentTilesToScan_field(self, value: Optional[str]):
        """
        Set data field with field name 'PercentTilesToScan' on this record model
        """
        self.set_field_value(self.PERCENTTILESTOSCAN__FIELD_NAME.field_name, value)

    def get_PercentTilesToScan_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PercentTilesToScan' from this record model
        """
        return self.get_field_value(self.PERCENTTILESTOSCAN__FIELD_NAME.field_name)

    def set_QualityScoreTrim_field(self, value: Optional[str]):
        """
        Set data field with field name 'QualityScoreTrim' on this record model
        """
        self.set_field_value(self.QUALITYSCORETRIM__FIELD_NAME.field_name, value)

    def get_QualityScoreTrim_field(self) -> Optional[str]:
        """
        Get data field value with field name 'QualityScoreTrim' from this record model
        """
        return self.get_field_value(self.QUALITYSCORETRIM__FIELD_NAME.field_name)

    def set_ReadType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReadType' on this record model
        """
        self.set_field_value(self.READTYPE__FIELD_NAME.field_name, value)

    def get_ReadType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReadType' from this record model
        """
        return self.get_field_value(self.READTYPE__FIELD_NAME.field_name)

    def set_ReagentCartridgeBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReagentCartridgeBarcode' on this record model
        """
        self.set_field_value(self.REAGENTCARTRIDGEBARCODE__FIELD_NAME.field_name, value)

    def get_ReagentCartridgeBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReagentCartridgeBarcode' from this record model
        """
        return self.get_field_value(self.REAGENTCARTRIDGEBARCODE__FIELD_NAME.field_name)

    def set_StitchReads_field(self, value: Optional[bool]):
        """
        Set data field with field name 'StitchReads' on this record model
        """
        self.set_field_value(self.STITCHREADS__FIELD_NAME.field_name, value)

    def get_StitchReads_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'StitchReads' from this record model
        """
        return self.get_field_value(self.STITCHREADS__FIELD_NAME.field_name)

    def set_Workflow_field(self, value: Optional[str]):
        """
        Set data field with field name 'Workflow' on this record model
        """
        self.set_field_value(self.WORKFLOW__FIELD_NAME.field_name, value)

    def get_Workflow_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Workflow' from this record model
        """
        return self.get_field_value(self.WORKFLOW__FIELD_NAME.field_name)


class IlluminaSequenceStatusModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IlluminaSequenceStatus
    Data Type Display Name: Illumina Sequencing Status (Illumina Sequencing Statuses)
    Fields: CurrentRead, CyclesCompleted, DateOfRun, DateOfUpdate, FlowcellId, InstrumentId, LaneCount, ReadIndexed, RunId, RunNumber, SurfaceCount, SwathCount, TileCount, TimeOfRun, TimeOfUpdate
    <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'IlluminaSequenceStatus'
    CURRENTREAD__FIELD_NAME: WrapperField = WrapperField("CurrentRead", FieldType.LONG)
    CYCLESCOMPLETED__FIELD_NAME: WrapperField = WrapperField("CyclesCompleted", FieldType.STRING)
    DATEOFRUN__FIELD_NAME: WrapperField = WrapperField("DateOfRun", FieldType.DATE)
    DATEOFUPDATE__FIELD_NAME: WrapperField = WrapperField("DateOfUpdate", FieldType.DATE)
    FLOWCELLID__FIELD_NAME: WrapperField = WrapperField("FlowcellId", FieldType.STRING)
    INSTRUMENTID__FIELD_NAME: WrapperField = WrapperField("InstrumentId", FieldType.STRING)
    LANECOUNT__FIELD_NAME: WrapperField = WrapperField("LaneCount", FieldType.LONG)
    READINDEXED__FIELD_NAME: WrapperField = WrapperField("ReadIndexed", FieldType.BOOLEAN)
    RUNID__FIELD_NAME: WrapperField = WrapperField("RunId", FieldType.STRING)
    RUNNUMBER__FIELD_NAME: WrapperField = WrapperField("RunNumber", FieldType.LONG)
    SURFACECOUNT__FIELD_NAME: WrapperField = WrapperField("SurfaceCount", FieldType.INTEGER)
    SWATHCOUNT__FIELD_NAME: WrapperField = WrapperField("SwathCount", FieldType.LONG)
    TILECOUNT__FIELD_NAME: WrapperField = WrapperField("TileCount", FieldType.LONG)
    TIMEOFRUN__FIELD_NAME: WrapperField = WrapperField("TimeOfRun", FieldType.STRING)
    TIMEOFUPDATE__FIELD_NAME: WrapperField = WrapperField("TimeOfUpdate", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_CurrentRead_field(self, value: Optional[int]):
        """
        Set data field with field name 'CurrentRead' on this record model
        """
        self.set_field_value(self.CURRENTREAD__FIELD_NAME.field_name, value)

    def get_CurrentRead_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CurrentRead' from this record model
        """
        return self.get_field_value(self.CURRENTREAD__FIELD_NAME.field_name)

    def set_CyclesCompleted_field(self, value: Optional[str]):
        """
        Set data field with field name 'CyclesCompleted' on this record model
        """
        self.set_field_value(self.CYCLESCOMPLETED__FIELD_NAME.field_name, value)

    def get_CyclesCompleted_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CyclesCompleted' from this record model
        """
        return self.get_field_value(self.CYCLESCOMPLETED__FIELD_NAME.field_name)

    def set_DateOfRun_field(self, value: Optional[int]):
        """
        Set data field with field name 'DateOfRun' on this record model
        """
        self.set_field_value(self.DATEOFRUN__FIELD_NAME.field_name, value)

    def get_DateOfRun_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DateOfRun' from this record model
        """
        return self.get_field_value(self.DATEOFRUN__FIELD_NAME.field_name)

    def set_DateOfUpdate_field(self, value: Optional[int]):
        """
        Set data field with field name 'DateOfUpdate' on this record model
        """
        self.set_field_value(self.DATEOFUPDATE__FIELD_NAME.field_name, value)

    def get_DateOfUpdate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DateOfUpdate' from this record model
        """
        return self.get_field_value(self.DATEOFUPDATE__FIELD_NAME.field_name)

    def set_FlowcellId_field(self, value: Optional[str]):
        """
        Set data field with field name 'FlowcellId' on this record model
        """
        self.set_field_value(self.FLOWCELLID__FIELD_NAME.field_name, value)

    def get_FlowcellId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FlowcellId' from this record model
        """
        return self.get_field_value(self.FLOWCELLID__FIELD_NAME.field_name)

    def set_InstrumentId_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentId' on this record model
        """
        self.set_field_value(self.INSTRUMENTID__FIELD_NAME.field_name, value)

    def get_InstrumentId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentId' from this record model
        """
        return self.get_field_value(self.INSTRUMENTID__FIELD_NAME.field_name)

    def set_LaneCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'LaneCount' on this record model
        """
        self.set_field_value(self.LANECOUNT__FIELD_NAME.field_name, value)

    def get_LaneCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LaneCount' from this record model
        """
        return self.get_field_value(self.LANECOUNT__FIELD_NAME.field_name)

    def set_ReadIndexed_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ReadIndexed' on this record model
        """
        self.set_field_value(self.READINDEXED__FIELD_NAME.field_name, value)

    def get_ReadIndexed_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ReadIndexed' from this record model
        """
        return self.get_field_value(self.READINDEXED__FIELD_NAME.field_name)

    def set_RunId_field(self, value: Optional[str]):
        """
        Set data field with field name 'RunId' on this record model
        """
        self.set_field_value(self.RUNID__FIELD_NAME.field_name, value)

    def get_RunId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RunId' from this record model
        """
        return self.get_field_value(self.RUNID__FIELD_NAME.field_name)

    def set_RunNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'RunNumber' on this record model
        """
        self.set_field_value(self.RUNNUMBER__FIELD_NAME.field_name, value)

    def get_RunNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RunNumber' from this record model
        """
        return self.get_field_value(self.RUNNUMBER__FIELD_NAME.field_name)

    def set_SurfaceCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'SurfaceCount' on this record model
        """
        self.set_field_value(self.SURFACECOUNT__FIELD_NAME.field_name, value)

    def get_SurfaceCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SurfaceCount' from this record model
        """
        return self.get_field_value(self.SURFACECOUNT__FIELD_NAME.field_name)

    def set_SwathCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'SwathCount' on this record model
        """
        self.set_field_value(self.SWATHCOUNT__FIELD_NAME.field_name, value)

    def get_SwathCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SwathCount' from this record model
        """
        return self.get_field_value(self.SWATHCOUNT__FIELD_NAME.field_name)

    def set_TileCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'TileCount' on this record model
        """
        self.set_field_value(self.TILECOUNT__FIELD_NAME.field_name, value)

    def get_TileCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TileCount' from this record model
        """
        return self.get_field_value(self.TILECOUNT__FIELD_NAME.field_name)

    def set_TimeOfRun_field(self, value: Optional[str]):
        """
        Set data field with field name 'TimeOfRun' on this record model
        """
        self.set_field_value(self.TIMEOFRUN__FIELD_NAME.field_name, value)

    def get_TimeOfRun_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TimeOfRun' from this record model
        """
        return self.get_field_value(self.TIMEOFRUN__FIELD_NAME.field_name)

    def set_TimeOfUpdate_field(self, value: Optional[str]):
        """
        Set data field with field name 'TimeOfUpdate' on this record model
        """
        self.set_field_value(self.TIMEOFUPDATE__FIELD_NAME.field_name, value)

    def get_TimeOfUpdate_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TimeOfUpdate' from this record model
        """
        return self.get_field_value(self.TIMEOFUPDATE__FIELD_NAME.field_name)


class IndexAssignmentModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IndexAssignment
    Data Type Display Name: Index Assignment (Index Assignments)
    Fields: ColPosition, IndexId, IndexTag, IndexType, MultiParentLink175, MultiParentLink193, MultiplexInstructions, RowPosition
    """
    DATA_TYPE_NAME: str = 'IndexAssignment'
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    INDEXID__FIELD_NAME: WrapperField = WrapperField("IndexId", FieldType.STRING)
    INDEXTAG__FIELD_NAME: WrapperField = WrapperField("IndexTag", FieldType.STRING)
    INDEXTYPE__FIELD_NAME: WrapperField = WrapperField("IndexType", FieldType.PICKLIST)
    MULTIPARENTLINK175__FIELD_NAME: WrapperField = WrapperField("MultiParentLink175", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK193__FIELD_NAME: WrapperField = WrapperField("MultiParentLink193", FieldType.MULTIPARENTLINK)
    MULTIPLEXINSTRUCTIONS__FIELD_NAME: WrapperField = WrapperField("MultiplexInstructions", FieldType.PICKLIST)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_IndexId_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexId' on this record model
        """
        self.set_field_value(self.INDEXID__FIELD_NAME.field_name, value)

    def get_IndexId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexId' from this record model
        """
        return self.get_field_value(self.INDEXID__FIELD_NAME.field_name)

    def set_IndexTag_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexTag' on this record model
        """
        self.set_field_value(self.INDEXTAG__FIELD_NAME.field_name, value)

    def get_IndexTag_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexTag' from this record model
        """
        return self.get_field_value(self.INDEXTAG__FIELD_NAME.field_name)

    def set_IndexType_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexType' on this record model
        """
        self.set_field_value(self.INDEXTYPE__FIELD_NAME.field_name, value)

    def get_IndexType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexType' from this record model
        """
        return self.get_field_value(self.INDEXTYPE__FIELD_NAME.field_name)

    def set_MultiplexInstructions_field(self, value: Optional[str]):
        """
        Set data field with field name 'MultiplexInstructions' on this record model
        """
        self.set_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name, value)

    def get_MultiplexInstructions_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MultiplexInstructions' from this record model
        """
        return self.get_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)


class IndexAssignmentBatchModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IndexAssignmentBatch
    Data Type Display Name: Index Assignment Batch (Index Assignment Batches)
    Fields: BatchSize, IndexSetName, IndexType, LastUsed, MultiplexInstructions
    A batch record that contains Index Assignment data records. This is used in providing support to Multiplexing specifications in index assignment.
    """
    DATA_TYPE_NAME: str = 'IndexAssignmentBatch'
    BATCHSIZE__FIELD_NAME: WrapperField = WrapperField("BatchSize", FieldType.LONG)
    INDEXSETNAME__FIELD_NAME: WrapperField = WrapperField("IndexSetName", FieldType.STRING)
    INDEXTYPE__FIELD_NAME: WrapperField = WrapperField("IndexType", FieldType.STRING)
    LASTUSED__FIELD_NAME: WrapperField = WrapperField("LastUsed", FieldType.BOOLEAN)
    MULTIPLEXINSTRUCTIONS__FIELD_NAME: WrapperField = WrapperField("MultiplexInstructions", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_BatchSize_field(self, value: Optional[int]):
        """
        Set data field with field name 'BatchSize' on this record model
        """
        self.set_field_value(self.BATCHSIZE__FIELD_NAME.field_name, value)

    def get_BatchSize_field(self) -> Optional[int]:
        """
        Get data field value with field name 'BatchSize' from this record model
        """
        return self.get_field_value(self.BATCHSIZE__FIELD_NAME.field_name)

    def set_IndexSetName_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexSetName' on this record model
        """
        self.set_field_value(self.INDEXSETNAME__FIELD_NAME.field_name, value)

    def get_IndexSetName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexSetName' from this record model
        """
        return self.get_field_value(self.INDEXSETNAME__FIELD_NAME.field_name)

    def set_IndexType_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexType' on this record model
        """
        self.set_field_value(self.INDEXTYPE__FIELD_NAME.field_name, value)

    def get_IndexType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexType' from this record model
        """
        return self.get_field_value(self.INDEXTYPE__FIELD_NAME.field_name)

    def set_LastUsed_field(self, value: Optional[bool]):
        """
        Set data field with field name 'LastUsed' on this record model
        """
        self.set_field_value(self.LASTUSED__FIELD_NAME.field_name, value)

    def get_LastUsed_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'LastUsed' from this record model
        """
        return self.get_field_value(self.LASTUSED__FIELD_NAME.field_name)

    def set_MultiplexInstructions_field(self, value: Optional[str]):
        """
        Set data field with field name 'MultiplexInstructions' on this record model
        """
        self.set_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name, value)

    def get_MultiplexInstructions_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MultiplexInstructions' from this record model
        """
        return self.get_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name)


class IndexAssignmentTypeModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IndexAssignmentType
    Data Type Display Name: Index Assignment Type (Index Assignment Types)
    Fields: IndexQty, IndexType
    A data record that encompasses multiple Index Assignment records and groups them into a single type.
    """
    DATA_TYPE_NAME: str = 'IndexAssignmentType'
    INDEXQTY__FIELD_NAME: WrapperField = WrapperField("IndexQty", FieldType.LONG)
    INDEXTYPE__FIELD_NAME: WrapperField = WrapperField("IndexType", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_IndexQty_field(self, value: Optional[int]):
        """
        Set data field with field name 'IndexQty' on this record model
        """
        self.set_field_value(self.INDEXQTY__FIELD_NAME.field_name, value)

    def get_IndexQty_field(self) -> Optional[int]:
        """
        Get data field value with field name 'IndexQty' from this record model
        """
        return self.get_field_value(self.INDEXQTY__FIELD_NAME.field_name)

    def set_IndexType_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexType' on this record model
        """
        self.set_field_value(self.INDEXTYPE__FIELD_NAME.field_name, value)

    def get_IndexType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexType' from this record model
        """
        return self.get_field_value(self.INDEXTYPE__FIELD_NAME.field_name)


class IndexBarcodeModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IndexBarcode
    Data Type Display Name: Assigned Index (Assigned Indices)
    Fields: ColPosition, IndexId, IndexTag, InputAssignmentMultiRecordId, InputAssignmentRecordId, MultiplexInstructions, OtherSampleId, RowPosition, SampleId
    """
    DATA_TYPE_NAME: str = 'IndexBarcode'
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    INDEXID__FIELD_NAME: WrapperField = WrapperField("IndexId", FieldType.STRING)
    INDEXTAG__FIELD_NAME: WrapperField = WrapperField("IndexTag", FieldType.STRING)
    INPUTASSIGNMENTMULTIRECORDID__FIELD_NAME: WrapperField = WrapperField("InputAssignmentMultiRecordId", FieldType.STRING)
    INPUTASSIGNMENTRECORDID__FIELD_NAME: WrapperField = WrapperField("InputAssignmentRecordId", FieldType.LONG)
    MULTIPLEXINSTRUCTIONS__FIELD_NAME: WrapperField = WrapperField("MultiplexInstructions", FieldType.SELECTION)
    OTHERSAMPLEID__FIELD_NAME: WrapperField = WrapperField("OtherSampleId", FieldType.STRING)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_IndexId_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexId' on this record model
        """
        self.set_field_value(self.INDEXID__FIELD_NAME.field_name, value)

    def get_IndexId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexId' from this record model
        """
        return self.get_field_value(self.INDEXID__FIELD_NAME.field_name)

    def set_IndexTag_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexTag' on this record model
        """
        self.set_field_value(self.INDEXTAG__FIELD_NAME.field_name, value)

    def get_IndexTag_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexTag' from this record model
        """
        return self.get_field_value(self.INDEXTAG__FIELD_NAME.field_name)

    def set_InputAssignmentMultiRecordId_field(self, value: Optional[str]):
        """
        Set data field with field name 'InputAssignmentMultiRecordId' on this record model
        """
        self.set_field_value(self.INPUTASSIGNMENTMULTIRECORDID__FIELD_NAME.field_name, value)

    def get_InputAssignmentMultiRecordId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InputAssignmentMultiRecordId' from this record model
        """
        return self.get_field_value(self.INPUTASSIGNMENTMULTIRECORDID__FIELD_NAME.field_name)

    def set_InputAssignmentRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'InputAssignmentRecordId' on this record model
        """
        self.set_field_value(self.INPUTASSIGNMENTRECORDID__FIELD_NAME.field_name, value)

    def get_InputAssignmentRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'InputAssignmentRecordId' from this record model
        """
        return self.get_field_value(self.INPUTASSIGNMENTRECORDID__FIELD_NAME.field_name)

    def set_MultiplexInstructions_field(self, value: Optional[str]):
        """
        Set data field with field name 'MultiplexInstructions' on this record model
        """
        self.set_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name, value)

    def get_MultiplexInstructions_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MultiplexInstructions' from this record model
        """
        return self.get_field_value(self.MULTIPLEXINSTRUCTIONS__FIELD_NAME.field_name)

    def set_OtherSampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'OtherSampleId' on this record model
        """
        self.set_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name, value)

    def get_OtherSampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OtherSampleId' from this record model
        """
        return self.get_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)


class IndexMetricModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type IndexMetric
    Data Type Display Name: Index Metric (Index Metrics)
    Fields: ColRead, IndexSeq, Lane, LaneCol, NumClusters, Project, SampleId
    <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'IndexMetric'
    COLREAD__FIELD_NAME: WrapperField = WrapperField("ColRead", FieldType.STRING)
    INDEXSEQ__FIELD_NAME: WrapperField = WrapperField("IndexSeq", FieldType.STRING)
    LANE__FIELD_NAME: WrapperField = WrapperField("Lane", FieldType.LONG)
    LANECOL__FIELD_NAME: WrapperField = WrapperField("LaneCol", FieldType.STRING)
    NUMCLUSTERS__FIELD_NAME: WrapperField = WrapperField("NumClusters", FieldType.LONG)
    PROJECT__FIELD_NAME: WrapperField = WrapperField("Project", FieldType.STRING)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColRead_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColRead' on this record model
        """
        self.set_field_value(self.COLREAD__FIELD_NAME.field_name, value)

    def get_ColRead_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColRead' from this record model
        """
        return self.get_field_value(self.COLREAD__FIELD_NAME.field_name)

    def set_IndexSeq_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndexSeq' on this record model
        """
        self.set_field_value(self.INDEXSEQ__FIELD_NAME.field_name, value)

    def get_IndexSeq_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndexSeq' from this record model
        """
        return self.get_field_value(self.INDEXSEQ__FIELD_NAME.field_name)

    def set_Lane_field(self, value: Optional[int]):
        """
        Set data field with field name 'Lane' on this record model
        """
        self.set_field_value(self.LANE__FIELD_NAME.field_name, value)

    def get_Lane_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Lane' from this record model
        """
        return self.get_field_value(self.LANE__FIELD_NAME.field_name)

    def set_LaneCol_field(self, value: Optional[str]):
        """
        Set data field with field name 'LaneCol' on this record model
        """
        self.set_field_value(self.LANECOL__FIELD_NAME.field_name, value)

    def get_LaneCol_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LaneCol' from this record model
        """
        return self.get_field_value(self.LANECOL__FIELD_NAME.field_name)

    def set_NumClusters_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumClusters' on this record model
        """
        self.set_field_value(self.NUMCLUSTERS__FIELD_NAME.field_name, value)

    def get_NumClusters_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumClusters' from this record model
        """
        return self.get_field_value(self.NUMCLUSTERS__FIELD_NAME.field_name)

    def set_Project_field(self, value: Optional[str]):
        """
        Set data field with field name 'Project' on this record model
        """
        self.set_field_value(self.PROJECT__FIELD_NAME.field_name, value)

    def get_Project_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Project' from this record model
        """
        return self.get_field_value(self.PROJECT__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)


class InstrumentModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Instrument
    Data Type Display Name: Instrument (Instruments)
    Fields: Barcode, DatePurchased, Description, FilePath, InstrumentName, InstrumentType, IsActive, ModelNumber, NetworkFilePath, SerialNumber, Site, Vendor, WorkstationId
    <!-- CONFIG: Environmental -->
    """
    DATA_TYPE_NAME: str = 'Instrument'
    BARCODE__FIELD_NAME: WrapperField = WrapperField("Barcode", FieldType.STRING)
    DATEPURCHASED__FIELD_NAME: WrapperField = WrapperField("DatePurchased", FieldType.DATE)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    INSTRUMENTNAME__FIELD_NAME: WrapperField = WrapperField("InstrumentName", FieldType.STRING)
    INSTRUMENTTYPE__FIELD_NAME: WrapperField = WrapperField("InstrumentType", FieldType.SELECTION)
    ISACTIVE__FIELD_NAME: WrapperField = WrapperField("IsActive", FieldType.BOOLEAN)
    MODELNUMBER__FIELD_NAME: WrapperField = WrapperField("ModelNumber", FieldType.STRING)
    NETWORKFILEPATH__FIELD_NAME: WrapperField = WrapperField("NetworkFilePath", FieldType.STRING)
    SERIALNUMBER__FIELD_NAME: WrapperField = WrapperField("SerialNumber", FieldType.STRING)
    SITE__FIELD_NAME: WrapperField = WrapperField("Site", FieldType.STRING)
    VENDOR__FIELD_NAME: WrapperField = WrapperField("Vendor", FieldType.STRING)
    WORKSTATIONID__FIELD_NAME: WrapperField = WrapperField("WorkstationId", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Barcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'Barcode' on this record model
        """
        self.set_field_value(self.BARCODE__FIELD_NAME.field_name, value)

    def get_Barcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Barcode' from this record model
        """
        return self.get_field_value(self.BARCODE__FIELD_NAME.field_name)

    def set_DatePurchased_field(self, value: Optional[int]):
        """
        Set data field with field name 'DatePurchased' on this record model
        """
        self.set_field_value(self.DATEPURCHASED__FIELD_NAME.field_name, value)

    def get_DatePurchased_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DatePurchased' from this record model
        """
        return self.get_field_value(self.DATEPURCHASED__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_InstrumentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentName' on this record model
        """
        self.set_field_value(self.INSTRUMENTNAME__FIELD_NAME.field_name, value)

    def get_InstrumentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentName' from this record model
        """
        return self.get_field_value(self.INSTRUMENTNAME__FIELD_NAME.field_name)

    def set_InstrumentType_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentType' on this record model
        """
        self.set_field_value(self.INSTRUMENTTYPE__FIELD_NAME.field_name, value)

    def get_InstrumentType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentType' from this record model
        """
        return self.get_field_value(self.INSTRUMENTTYPE__FIELD_NAME.field_name)

    def set_IsActive_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsActive' on this record model
        """
        self.set_field_value(self.ISACTIVE__FIELD_NAME.field_name, value)

    def get_IsActive_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsActive' from this record model
        """
        return self.get_field_value(self.ISACTIVE__FIELD_NAME.field_name)

    def set_ModelNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'ModelNumber' on this record model
        """
        self.set_field_value(self.MODELNUMBER__FIELD_NAME.field_name, value)

    def get_ModelNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ModelNumber' from this record model
        """
        return self.get_field_value(self.MODELNUMBER__FIELD_NAME.field_name)

    def set_NetworkFilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'NetworkFilePath' on this record model
        """
        self.set_field_value(self.NETWORKFILEPATH__FIELD_NAME.field_name, value)

    def get_NetworkFilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NetworkFilePath' from this record model
        """
        return self.get_field_value(self.NETWORKFILEPATH__FIELD_NAME.field_name)

    def set_SerialNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'SerialNumber' on this record model
        """
        self.set_field_value(self.SERIALNUMBER__FIELD_NAME.field_name, value)

    def get_SerialNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SerialNumber' from this record model
        """
        return self.get_field_value(self.SERIALNUMBER__FIELD_NAME.field_name)

    def set_Site_field(self, value: Optional[str]):
        """
        Set data field with field name 'Site' on this record model
        """
        self.set_field_value(self.SITE__FIELD_NAME.field_name, value)

    def get_Site_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Site' from this record model
        """
        return self.get_field_value(self.SITE__FIELD_NAME.field_name)

    def set_Vendor_field(self, value: Optional[str]):
        """
        Set data field with field name 'Vendor' on this record model
        """
        self.set_field_value(self.VENDOR__FIELD_NAME.field_name, value)

    def get_Vendor_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Vendor' from this record model
        """
        return self.get_field_value(self.VENDOR__FIELD_NAME.field_name)

    def set_WorkstationId_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkstationId' on this record model
        """
        self.set_field_value(self.WORKSTATIONID__FIELD_NAME.field_name, value)

    def get_WorkstationId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkstationId' from this record model
        """
        return self.get_field_value(self.WORKSTATIONID__FIELD_NAME.field_name)


class InstrumentConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type InstrumentConfig
    Data Type Display Name: Instrument Configuration (Instrument Configurations)
    Fields: ContainsKey1, ContainsKey2, ContainsKey3, FileCreator, FileDifferentiator, FileKeyIdentifier1, FileKeyIdentifier2, FileKeyIdentifier3, FileLoader, FileParser, InstrumentConfigurationName, InstrumentType, OutputFileCreator, Presenter, RecordHandler, RecordProcessor, SupportsMolarity, Validator
    """
    DATA_TYPE_NAME: str = 'InstrumentConfig'
    CONTAINSKEY1__FIELD_NAME: WrapperField = WrapperField("ContainsKey1", FieldType.BOOLEAN)
    CONTAINSKEY2__FIELD_NAME: WrapperField = WrapperField("ContainsKey2", FieldType.BOOLEAN)
    CONTAINSKEY3__FIELD_NAME: WrapperField = WrapperField("ContainsKey3", FieldType.BOOLEAN)
    FILECREATOR__FIELD_NAME: WrapperField = WrapperField("FileCreator", FieldType.SELECTION)
    FILEDIFFERENTIATOR__FIELD_NAME: WrapperField = WrapperField("FileDifferentiator", FieldType.SELECTION)
    FILEKEYIDENTIFIER1__FIELD_NAME: WrapperField = WrapperField("FileKeyIdentifier1", FieldType.STRING)
    FILEKEYIDENTIFIER2__FIELD_NAME: WrapperField = WrapperField("FileKeyIdentifier2", FieldType.STRING)
    FILEKEYIDENTIFIER3__FIELD_NAME: WrapperField = WrapperField("FileKeyIdentifier3", FieldType.STRING)
    FILELOADER__FIELD_NAME: WrapperField = WrapperField("FileLoader", FieldType.SELECTION)
    FILEPARSER__FIELD_NAME: WrapperField = WrapperField("FileParser", FieldType.SELECTION)
    INSTRUMENTCONFIGURATIONNAME__FIELD_NAME: WrapperField = WrapperField("InstrumentConfigurationName", FieldType.STRING)
    INSTRUMENTTYPE__FIELD_NAME: WrapperField = WrapperField("InstrumentType", FieldType.STRING)
    OUTPUTFILECREATOR__FIELD_NAME: WrapperField = WrapperField("OutputFileCreator", FieldType.SELECTION)
    PRESENTER__FIELD_NAME: WrapperField = WrapperField("Presenter", FieldType.SELECTION)
    RECORDHANDLER__FIELD_NAME: WrapperField = WrapperField("RecordHandler", FieldType.SELECTION)
    RECORDPROCESSOR__FIELD_NAME: WrapperField = WrapperField("RecordProcessor", FieldType.SELECTION)
    SUPPORTSMOLARITY__FIELD_NAME: WrapperField = WrapperField("SupportsMolarity", FieldType.BOOLEAN)
    VALIDATOR__FIELD_NAME: WrapperField = WrapperField("Validator", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ContainsKey1_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ContainsKey1' on this record model
        """
        self.set_field_value(self.CONTAINSKEY1__FIELD_NAME.field_name, value)

    def get_ContainsKey1_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ContainsKey1' from this record model
        """
        return self.get_field_value(self.CONTAINSKEY1__FIELD_NAME.field_name)

    def set_ContainsKey2_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ContainsKey2' on this record model
        """
        self.set_field_value(self.CONTAINSKEY2__FIELD_NAME.field_name, value)

    def get_ContainsKey2_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ContainsKey2' from this record model
        """
        return self.get_field_value(self.CONTAINSKEY2__FIELD_NAME.field_name)

    def set_ContainsKey3_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ContainsKey3' on this record model
        """
        self.set_field_value(self.CONTAINSKEY3__FIELD_NAME.field_name, value)

    def get_ContainsKey3_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ContainsKey3' from this record model
        """
        return self.get_field_value(self.CONTAINSKEY3__FIELD_NAME.field_name)

    def set_FileCreator_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileCreator' on this record model
        """
        self.set_field_value(self.FILECREATOR__FIELD_NAME.field_name, value)

    def get_FileCreator_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileCreator' from this record model
        """
        return self.get_field_value(self.FILECREATOR__FIELD_NAME.field_name)

    def set_FileDifferentiator_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileDifferentiator' on this record model
        """
        self.set_field_value(self.FILEDIFFERENTIATOR__FIELD_NAME.field_name, value)

    def get_FileDifferentiator_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileDifferentiator' from this record model
        """
        return self.get_field_value(self.FILEDIFFERENTIATOR__FIELD_NAME.field_name)

    def set_FileKeyIdentifier1_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileKeyIdentifier1' on this record model
        """
        self.set_field_value(self.FILEKEYIDENTIFIER1__FIELD_NAME.field_name, value)

    def get_FileKeyIdentifier1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileKeyIdentifier1' from this record model
        """
        return self.get_field_value(self.FILEKEYIDENTIFIER1__FIELD_NAME.field_name)

    def set_FileKeyIdentifier2_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileKeyIdentifier2' on this record model
        """
        self.set_field_value(self.FILEKEYIDENTIFIER2__FIELD_NAME.field_name, value)

    def get_FileKeyIdentifier2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileKeyIdentifier2' from this record model
        """
        return self.get_field_value(self.FILEKEYIDENTIFIER2__FIELD_NAME.field_name)

    def set_FileKeyIdentifier3_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileKeyIdentifier3' on this record model
        """
        self.set_field_value(self.FILEKEYIDENTIFIER3__FIELD_NAME.field_name, value)

    def get_FileKeyIdentifier3_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileKeyIdentifier3' from this record model
        """
        return self.get_field_value(self.FILEKEYIDENTIFIER3__FIELD_NAME.field_name)

    def set_FileLoader_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileLoader' on this record model
        """
        self.set_field_value(self.FILELOADER__FIELD_NAME.field_name, value)

    def get_FileLoader_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileLoader' from this record model
        """
        return self.get_field_value(self.FILELOADER__FIELD_NAME.field_name)

    def set_FileParser_field(self, value: Optional[str]):
        """
        Set data field with field name 'FileParser' on this record model
        """
        self.set_field_value(self.FILEPARSER__FIELD_NAME.field_name, value)

    def get_FileParser_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FileParser' from this record model
        """
        return self.get_field_value(self.FILEPARSER__FIELD_NAME.field_name)

    def set_InstrumentConfigurationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentConfigurationName' on this record model
        """
        self.set_field_value(self.INSTRUMENTCONFIGURATIONNAME__FIELD_NAME.field_name, value)

    def get_InstrumentConfigurationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentConfigurationName' from this record model
        """
        return self.get_field_value(self.INSTRUMENTCONFIGURATIONNAME__FIELD_NAME.field_name)

    def set_InstrumentType_field(self, value: Optional[str]):
        """
        Set data field with field name 'InstrumentType' on this record model
        """
        self.set_field_value(self.INSTRUMENTTYPE__FIELD_NAME.field_name, value)

    def get_InstrumentType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InstrumentType' from this record model
        """
        return self.get_field_value(self.INSTRUMENTTYPE__FIELD_NAME.field_name)

    def set_OutputFileCreator_field(self, value: Optional[str]):
        """
        Set data field with field name 'OutputFileCreator' on this record model
        """
        self.set_field_value(self.OUTPUTFILECREATOR__FIELD_NAME.field_name, value)

    def get_OutputFileCreator_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OutputFileCreator' from this record model
        """
        return self.get_field_value(self.OUTPUTFILECREATOR__FIELD_NAME.field_name)

    def set_Presenter_field(self, value: Optional[str]):
        """
        Set data field with field name 'Presenter' on this record model
        """
        self.set_field_value(self.PRESENTER__FIELD_NAME.field_name, value)

    def get_Presenter_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Presenter' from this record model
        """
        return self.get_field_value(self.PRESENTER__FIELD_NAME.field_name)

    def set_RecordHandler_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecordHandler' on this record model
        """
        self.set_field_value(self.RECORDHANDLER__FIELD_NAME.field_name, value)

    def get_RecordHandler_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecordHandler' from this record model
        """
        return self.get_field_value(self.RECORDHANDLER__FIELD_NAME.field_name)

    def set_RecordProcessor_field(self, value: Optional[str]):
        """
        Set data field with field name 'RecordProcessor' on this record model
        """
        self.set_field_value(self.RECORDPROCESSOR__FIELD_NAME.field_name, value)

    def get_RecordProcessor_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RecordProcessor' from this record model
        """
        return self.get_field_value(self.RECORDPROCESSOR__FIELD_NAME.field_name)

    def set_SupportsMolarity_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SupportsMolarity' on this record model
        """
        self.set_field_value(self.SUPPORTSMOLARITY__FIELD_NAME.field_name, value)

    def get_SupportsMolarity_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SupportsMolarity' from this record model
        """
        return self.get_field_value(self.SUPPORTSMOLARITY__FIELD_NAME.field_name)

    def set_Validator_field(self, value: Optional[str]):
        """
        Set data field with field name 'Validator' on this record model
        """
        self.set_field_value(self.VALIDATOR__FIELD_NAME.field_name, value)

    def get_Validator_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Validator' from this record model
        """
        return self.get_field_value(self.VALIDATOR__FIELD_NAME.field_name)


class InstrumentFieldMapModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type InstrumentFieldMap
    Data Type Display Name: Instrument Field Map (Instrument Field Maps)
    Fields: FromFileField, ToRecordField
    """
    DATA_TYPE_NAME: str = 'InstrumentFieldMap'
    FROMFILEFIELD__FIELD_NAME: WrapperField = WrapperField("FromFileField", FieldType.STRING)
    TORECORDFIELD__FIELD_NAME: WrapperField = WrapperField("ToRecordField", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FromFileField_field(self, value: Optional[str]):
        """
        Set data field with field name 'FromFileField' on this record model
        """
        self.set_field_value(self.FROMFILEFIELD__FIELD_NAME.field_name, value)

    def get_FromFileField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FromFileField' from this record model
        """
        return self.get_field_value(self.FROMFILEFIELD__FIELD_NAME.field_name)

    def set_ToRecordField_field(self, value: Optional[str]):
        """
        Set data field with field name 'ToRecordField' on this record model
        """
        self.set_field_value(self.TORECORDFIELD__FIELD_NAME.field_name, value)

    def get_ToRecordField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ToRecordField' from this record model
        """
        return self.get_field_value(self.TORECORDFIELD__FIELD_NAME.field_name)


class InstrumentMaintenanceReceiptModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type InstrumentMaintenanceReceipt
    Data Type Display Name: Instrument Maintenance Log (Instrument Maintenance Logs)
    Fields: ActiveWorkflowId, ActiveWorkflowName, ApproverComment, ApproverGroupName, ApproverName, ApproverUsername, DateApproved, MaintenanceComments, MaintenancePendingDate, MaintenancePerformedBy, MaintenancePerformedDate, MaintenanceStatus, NextDueDate
    """
    DATA_TYPE_NAME: str = 'InstrumentMaintenanceReceipt'
    ACTIVEWORKFLOWID__FIELD_NAME: WrapperField = WrapperField("ActiveWorkflowId", FieldType.LONG)
    ACTIVEWORKFLOWNAME__FIELD_NAME: WrapperField = WrapperField("ActiveWorkflowName", FieldType.SELECTION)
    APPROVERCOMMENT__FIELD_NAME: WrapperField = WrapperField("ApproverComment", FieldType.STRING)
    APPROVERGROUPNAME__FIELD_NAME: WrapperField = WrapperField("ApproverGroupName", FieldType.STRING)
    APPROVERNAME__FIELD_NAME: WrapperField = WrapperField("ApproverName", FieldType.STRING)
    APPROVERUSERNAME__FIELD_NAME: WrapperField = WrapperField("ApproverUsername", FieldType.STRING)
    DATEAPPROVED__FIELD_NAME: WrapperField = WrapperField("DateApproved", FieldType.DATE)
    MAINTENANCECOMMENTS__FIELD_NAME: WrapperField = WrapperField("MaintenanceComments", FieldType.STRING)
    MAINTENANCEPENDINGDATE__FIELD_NAME: WrapperField = WrapperField("MaintenancePendingDate", FieldType.DATE)
    MAINTENANCEPERFORMEDBY__FIELD_NAME: WrapperField = WrapperField("MaintenancePerformedBy", FieldType.SELECTION)
    MAINTENANCEPERFORMEDDATE__FIELD_NAME: WrapperField = WrapperField("MaintenancePerformedDate", FieldType.DATE)
    MAINTENANCESTATUS__FIELD_NAME: WrapperField = WrapperField("MaintenanceStatus", FieldType.PICKLIST)
    NEXTDUEDATE__FIELD_NAME: WrapperField = WrapperField("NextDueDate", FieldType.DATE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActiveWorkflowId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ActiveWorkflowId' on this record model
        """
        self.set_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name, value)

    def get_ActiveWorkflowId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ActiveWorkflowId' from this record model
        """
        return self.get_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name)

    def set_ActiveWorkflowName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ActiveWorkflowName' on this record model
        """
        self.set_field_value(self.ACTIVEWORKFLOWNAME__FIELD_NAME.field_name, value)

    def get_ActiveWorkflowName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ActiveWorkflowName' from this record model
        """
        return self.get_field_value(self.ACTIVEWORKFLOWNAME__FIELD_NAME.field_name)

    def set_ApproverComment_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApproverComment' on this record model
        """
        self.set_field_value(self.APPROVERCOMMENT__FIELD_NAME.field_name, value)

    def get_ApproverComment_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApproverComment' from this record model
        """
        return self.get_field_value(self.APPROVERCOMMENT__FIELD_NAME.field_name)

    def set_ApproverGroupName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApproverGroupName' on this record model
        """
        self.set_field_value(self.APPROVERGROUPNAME__FIELD_NAME.field_name, value)

    def get_ApproverGroupName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApproverGroupName' from this record model
        """
        return self.get_field_value(self.APPROVERGROUPNAME__FIELD_NAME.field_name)

    def set_ApproverName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApproverName' on this record model
        """
        self.set_field_value(self.APPROVERNAME__FIELD_NAME.field_name, value)

    def get_ApproverName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApproverName' from this record model
        """
        return self.get_field_value(self.APPROVERNAME__FIELD_NAME.field_name)

    def set_ApproverUsername_field(self, value: Optional[str]):
        """
        Set data field with field name 'ApproverUsername' on this record model
        """
        self.set_field_value(self.APPROVERUSERNAME__FIELD_NAME.field_name, value)

    def get_ApproverUsername_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ApproverUsername' from this record model
        """
        return self.get_field_value(self.APPROVERUSERNAME__FIELD_NAME.field_name)

    def set_DateApproved_field(self, value: Optional[int]):
        """
        Set data field with field name 'DateApproved' on this record model
        """
        self.set_field_value(self.DATEAPPROVED__FIELD_NAME.field_name, value)

    def get_DateApproved_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DateApproved' from this record model
        """
        return self.get_field_value(self.DATEAPPROVED__FIELD_NAME.field_name)

    def set_MaintenanceComments_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaintenanceComments' on this record model
        """
        self.set_field_value(self.MAINTENANCECOMMENTS__FIELD_NAME.field_name, value)

    def get_MaintenanceComments_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaintenanceComments' from this record model
        """
        return self.get_field_value(self.MAINTENANCECOMMENTS__FIELD_NAME.field_name)

    def set_MaintenancePendingDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'MaintenancePendingDate' on this record model
        """
        self.set_field_value(self.MAINTENANCEPENDINGDATE__FIELD_NAME.field_name, value)

    def get_MaintenancePendingDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MaintenancePendingDate' from this record model
        """
        return self.get_field_value(self.MAINTENANCEPENDINGDATE__FIELD_NAME.field_name)

    def set_MaintenancePerformedBy_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaintenancePerformedBy' on this record model
        """
        self.set_field_value(self.MAINTENANCEPERFORMEDBY__FIELD_NAME.field_name, value)

    def get_MaintenancePerformedBy_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaintenancePerformedBy' from this record model
        """
        return self.get_field_value(self.MAINTENANCEPERFORMEDBY__FIELD_NAME.field_name)

    def set_MaintenancePerformedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'MaintenancePerformedDate' on this record model
        """
        self.set_field_value(self.MAINTENANCEPERFORMEDDATE__FIELD_NAME.field_name, value)

    def get_MaintenancePerformedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MaintenancePerformedDate' from this record model
        """
        return self.get_field_value(self.MAINTENANCEPERFORMEDDATE__FIELD_NAME.field_name)

    def set_MaintenanceStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaintenanceStatus' on this record model
        """
        self.set_field_value(self.MAINTENANCESTATUS__FIELD_NAME.field_name, value)

    def get_MaintenanceStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaintenanceStatus' from this record model
        """
        return self.get_field_value(self.MAINTENANCESTATUS__FIELD_NAME.field_name)

    def set_NextDueDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'NextDueDate' on this record model
        """
        self.set_field_value(self.NEXTDUEDATE__FIELD_NAME.field_name, value)

    def get_NextDueDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NextDueDate' from this record model
        """
        return self.get_field_value(self.NEXTDUEDATE__FIELD_NAME.field_name)


class InstrumentParseConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type InstrumentParseConfig
    Data Type Display Name: Instrument Parser Config (Instrument Parser Configs)
    Fields: BlockIdentifier, BlockType, DataLoaderConfig, EndPivotOnColumn, FieldName1, FieldName2, FieldName3, StartPivotOnColumn
    This is for the Generic Instrument Parser.
    """
    DATA_TYPE_NAME: str = 'InstrumentParseConfig'
    BLOCKIDENTIFIER__FIELD_NAME: WrapperField = WrapperField("BlockIdentifier", FieldType.STRING)
    BLOCKTYPE__FIELD_NAME: WrapperField = WrapperField("BlockType", FieldType.PICKLIST)
    DATALOADERCONFIG__FIELD_NAME: WrapperField = WrapperField("DataLoaderConfig", FieldType.STRING)
    ENDPIVOTONCOLUMN__FIELD_NAME: WrapperField = WrapperField("EndPivotOnColumn", FieldType.STRING)
    FIELDNAME1__FIELD_NAME: WrapperField = WrapperField("FieldName1", FieldType.STRING)
    FIELDNAME2__FIELD_NAME: WrapperField = WrapperField("FieldName2", FieldType.STRING)
    FIELDNAME3__FIELD_NAME: WrapperField = WrapperField("FieldName3", FieldType.STRING)
    STARTPIVOTONCOLUMN__FIELD_NAME: WrapperField = WrapperField("StartPivotOnColumn", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_BlockIdentifier_field(self, value: Optional[str]):
        """
        Set data field with field name 'BlockIdentifier' on this record model
        """
        self.set_field_value(self.BLOCKIDENTIFIER__FIELD_NAME.field_name, value)

    def get_BlockIdentifier_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BlockIdentifier' from this record model
        """
        return self.get_field_value(self.BLOCKIDENTIFIER__FIELD_NAME.field_name)

    def set_BlockType_field(self, value: Optional[str]):
        """
        Set data field with field name 'BlockType' on this record model
        """
        self.set_field_value(self.BLOCKTYPE__FIELD_NAME.field_name, value)

    def get_BlockType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BlockType' from this record model
        """
        return self.get_field_value(self.BLOCKTYPE__FIELD_NAME.field_name)

    def set_DataLoaderConfig_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataLoaderConfig' on this record model
        """
        self.set_field_value(self.DATALOADERCONFIG__FIELD_NAME.field_name, value)

    def get_DataLoaderConfig_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataLoaderConfig' from this record model
        """
        return self.get_field_value(self.DATALOADERCONFIG__FIELD_NAME.field_name)

    def set_EndPivotOnColumn_field(self, value: Optional[str]):
        """
        Set data field with field name 'EndPivotOnColumn' on this record model
        """
        self.set_field_value(self.ENDPIVOTONCOLUMN__FIELD_NAME.field_name, value)

    def get_EndPivotOnColumn_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EndPivotOnColumn' from this record model
        """
        return self.get_field_value(self.ENDPIVOTONCOLUMN__FIELD_NAME.field_name)

    def set_FieldName1_field(self, value: Optional[str]):
        """
        Set data field with field name 'FieldName1' on this record model
        """
        self.set_field_value(self.FIELDNAME1__FIELD_NAME.field_name, value)

    def get_FieldName1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FieldName1' from this record model
        """
        return self.get_field_value(self.FIELDNAME1__FIELD_NAME.field_name)

    def set_FieldName2_field(self, value: Optional[str]):
        """
        Set data field with field name 'FieldName2' on this record model
        """
        self.set_field_value(self.FIELDNAME2__FIELD_NAME.field_name, value)

    def get_FieldName2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FieldName2' from this record model
        """
        return self.get_field_value(self.FIELDNAME2__FIELD_NAME.field_name)

    def set_FieldName3_field(self, value: Optional[str]):
        """
        Set data field with field name 'FieldName3' on this record model
        """
        self.set_field_value(self.FIELDNAME3__FIELD_NAME.field_name, value)

    def get_FieldName3_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FieldName3' from this record model
        """
        return self.get_field_value(self.FIELDNAME3__FIELD_NAME.field_name)

    def set_StartPivotOnColumn_field(self, value: Optional[str]):
        """
        Set data field with field name 'StartPivotOnColumn' on this record model
        """
        self.set_field_value(self.STARTPIVOTONCOLUMN__FIELD_NAME.field_name, value)

    def get_StartPivotOnColumn_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StartPivotOnColumn' from this record model
        """
        return self.get_field_value(self.STARTPIVOTONCOLUMN__FIELD_NAME.field_name)


class InstrumentStatusModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type InstrumentStatus
    Data Type Display Name: Instrument Status (Instrument Status)
    Fields: CurrentRunDate, CurrentRunId, LastUpdated, PercentCompletion, Position, Status
    """
    DATA_TYPE_NAME: str = 'InstrumentStatus'
    CURRENTRUNDATE__FIELD_NAME: WrapperField = WrapperField("CurrentRunDate", FieldType.INTEGER)
    CURRENTRUNID__FIELD_NAME: WrapperField = WrapperField("CurrentRunId", FieldType.STRING)
    LASTUPDATED__FIELD_NAME: WrapperField = WrapperField("LastUpdated", FieldType.DATE)
    PERCENTCOMPLETION__FIELD_NAME: WrapperField = WrapperField("PercentCompletion", FieldType.DOUBLE)
    POSITION__FIELD_NAME: WrapperField = WrapperField("Position", FieldType.STRING)
    STATUS__FIELD_NAME: WrapperField = WrapperField("Status", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_CurrentRunDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'CurrentRunDate' on this record model
        """
        self.set_field_value(self.CURRENTRUNDATE__FIELD_NAME.field_name, value)

    def get_CurrentRunDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CurrentRunDate' from this record model
        """
        return self.get_field_value(self.CURRENTRUNDATE__FIELD_NAME.field_name)

    def set_CurrentRunId_field(self, value: Optional[str]):
        """
        Set data field with field name 'CurrentRunId' on this record model
        """
        self.set_field_value(self.CURRENTRUNID__FIELD_NAME.field_name, value)

    def get_CurrentRunId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CurrentRunId' from this record model
        """
        return self.get_field_value(self.CURRENTRUNID__FIELD_NAME.field_name)

    def set_LastUpdated_field(self, value: Optional[int]):
        """
        Set data field with field name 'LastUpdated' on this record model
        """
        self.set_field_value(self.LASTUPDATED__FIELD_NAME.field_name, value)

    def get_LastUpdated_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LastUpdated' from this record model
        """
        return self.get_field_value(self.LASTUPDATED__FIELD_NAME.field_name)

    def set_PercentCompletion_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentCompletion' on this record model
        """
        self.set_field_value(self.PERCENTCOMPLETION__FIELD_NAME.field_name, value)

    def get_PercentCompletion_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentCompletion' from this record model
        """
        return self.get_field_value(self.PERCENTCOMPLETION__FIELD_NAME.field_name)

    def set_Position_field(self, value: Optional[str]):
        """
        Set data field with field name 'Position' on this record model
        """
        self.set_field_value(self.POSITION__FIELD_NAME.field_name, value)

    def get_Position_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Position' from this record model
        """
        return self.get_field_value(self.POSITION__FIELD_NAME.field_name)

    def set_Status_field(self, value: Optional[str]):
        """
        Set data field with field name 'Status' on this record model
        """
        self.set_field_value(self.STATUS__FIELD_NAME.field_name, value)

    def get_Status_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Status' from this record model
        """
        return self.get_field_value(self.STATUS__FIELD_NAME.field_name)


class LearnedModelsModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type LearnedModels
    Data Type Display Name: Learned Model (Learned Models)
    Fields: FilePath, FormulaName, IndependentVariableNames, IndependentVariableTypes, ModelId, ModelInputType, ModelType, ResponseVariableName, ResponseVariableType, SoftwareSuite, SoftwareVersion, VeloxCurrentVersion
    This is a repository of all statistical models which can be used to generate predictions.
    """
    DATA_TYPE_NAME: str = 'LearnedModels'
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    FORMULANAME__FIELD_NAME: WrapperField = WrapperField("FormulaName", FieldType.STRING)
    INDEPENDENTVARIABLENAMES__FIELD_NAME: WrapperField = WrapperField("IndependentVariableNames", FieldType.SELECTION)
    INDEPENDENTVARIABLETYPES__FIELD_NAME: WrapperField = WrapperField("IndependentVariableTypes", FieldType.STRING)
    MODELID__FIELD_NAME: WrapperField = WrapperField("ModelId", FieldType.STRING)
    MODELINPUTTYPE__FIELD_NAME: WrapperField = WrapperField("ModelInputType", FieldType.STRING)
    MODELTYPE__FIELD_NAME: WrapperField = WrapperField("ModelType", FieldType.STRING)
    RESPONSEVARIABLENAME__FIELD_NAME: WrapperField = WrapperField("ResponseVariableName", FieldType.STRING)
    RESPONSEVARIABLETYPE__FIELD_NAME: WrapperField = WrapperField("ResponseVariableType", FieldType.STRING)
    SOFTWARESUITE__FIELD_NAME: WrapperField = WrapperField("SoftwareSuite", FieldType.STRING)
    SOFTWAREVERSION__FIELD_NAME: WrapperField = WrapperField("SoftwareVersion", FieldType.STRING)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_FormulaName_field(self, value: Optional[str]):
        """
        Set data field with field name 'FormulaName' on this record model
        """
        self.set_field_value(self.FORMULANAME__FIELD_NAME.field_name, value)

    def get_FormulaName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FormulaName' from this record model
        """
        return self.get_field_value(self.FORMULANAME__FIELD_NAME.field_name)

    def set_IndependentVariableNames_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndependentVariableNames' on this record model
        """
        self.set_field_value(self.INDEPENDENTVARIABLENAMES__FIELD_NAME.field_name, value)

    def get_IndependentVariableNames_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndependentVariableNames' from this record model
        """
        return self.get_field_value(self.INDEPENDENTVARIABLENAMES__FIELD_NAME.field_name)

    def set_IndependentVariableTypes_field(self, value: Optional[str]):
        """
        Set data field with field name 'IndependentVariableTypes' on this record model
        """
        self.set_field_value(self.INDEPENDENTVARIABLETYPES__FIELD_NAME.field_name, value)

    def get_IndependentVariableTypes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'IndependentVariableTypes' from this record model
        """
        return self.get_field_value(self.INDEPENDENTVARIABLETYPES__FIELD_NAME.field_name)

    def set_ModelId_field(self, value: Optional[str]):
        """
        Set data field with field name 'ModelId' on this record model
        """
        self.set_field_value(self.MODELID__FIELD_NAME.field_name, value)

    def get_ModelId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ModelId' from this record model
        """
        return self.get_field_value(self.MODELID__FIELD_NAME.field_name)

    def set_ModelInputType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ModelInputType' on this record model
        """
        self.set_field_value(self.MODELINPUTTYPE__FIELD_NAME.field_name, value)

    def get_ModelInputType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ModelInputType' from this record model
        """
        return self.get_field_value(self.MODELINPUTTYPE__FIELD_NAME.field_name)

    def set_ModelType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ModelType' on this record model
        """
        self.set_field_value(self.MODELTYPE__FIELD_NAME.field_name, value)

    def get_ModelType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ModelType' from this record model
        """
        return self.get_field_value(self.MODELTYPE__FIELD_NAME.field_name)

    def set_ResponseVariableName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ResponseVariableName' on this record model
        """
        self.set_field_value(self.RESPONSEVARIABLENAME__FIELD_NAME.field_name, value)

    def get_ResponseVariableName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ResponseVariableName' from this record model
        """
        return self.get_field_value(self.RESPONSEVARIABLENAME__FIELD_NAME.field_name)

    def set_ResponseVariableType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ResponseVariableType' on this record model
        """
        self.set_field_value(self.RESPONSEVARIABLETYPE__FIELD_NAME.field_name, value)

    def get_ResponseVariableType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ResponseVariableType' from this record model
        """
        return self.get_field_value(self.RESPONSEVARIABLETYPE__FIELD_NAME.field_name)

    def set_SoftwareSuite_field(self, value: Optional[str]):
        """
        Set data field with field name 'SoftwareSuite' on this record model
        """
        self.set_field_value(self.SOFTWARESUITE__FIELD_NAME.field_name, value)

    def get_SoftwareSuite_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SoftwareSuite' from this record model
        """
        return self.get_field_value(self.SOFTWARESUITE__FIELD_NAME.field_name)

    def set_SoftwareVersion_field(self, value: Optional[str]):
        """
        Set data field with field name 'SoftwareVersion' on this record model
        """
        self.set_field_value(self.SOFTWAREVERSION__FIELD_NAME.field_name, value)

    def get_SoftwareVersion_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SoftwareVersion' from this record model
        """
        return self.get_field_value(self.SOFTWAREVERSION__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class LinearRegressionModelModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type LinearRegressionModel
    Data Type Display Name: Linear Regression Model (Linear Regression Models)
    Fields: A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, AdjRSquared, DegreeOfPolynomial, DenominatorDOF, EntryName, fValue, MultiParentLink207, NumeratorDOF, pValue, RSquared, SeriesName, SourceEntryId
    """
    DATA_TYPE_NAME: str = 'LinearRegressionModel'
    A0__FIELD_NAME: WrapperField = WrapperField("A0", FieldType.DOUBLE)
    A1__FIELD_NAME: WrapperField = WrapperField("A1", FieldType.DOUBLE)
    A2__FIELD_NAME: WrapperField = WrapperField("A2", FieldType.DOUBLE)
    A3__FIELD_NAME: WrapperField = WrapperField("A3", FieldType.DOUBLE)
    A4__FIELD_NAME: WrapperField = WrapperField("A4", FieldType.DOUBLE)
    A5__FIELD_NAME: WrapperField = WrapperField("A5", FieldType.DOUBLE)
    A6__FIELD_NAME: WrapperField = WrapperField("A6", FieldType.DOUBLE)
    A7__FIELD_NAME: WrapperField = WrapperField("A7", FieldType.DOUBLE)
    A8__FIELD_NAME: WrapperField = WrapperField("A8", FieldType.DOUBLE)
    A9__FIELD_NAME: WrapperField = WrapperField("A9", FieldType.DOUBLE)
    A10__FIELD_NAME: WrapperField = WrapperField("A10", FieldType.DOUBLE)
    ADJRSQUARED__FIELD_NAME: WrapperField = WrapperField("AdjRSquared", FieldType.DOUBLE)
    DEGREEOFPOLYNOMIAL__FIELD_NAME: WrapperField = WrapperField("DegreeOfPolynomial", FieldType.INTEGER)
    DENOMINATORDOF__FIELD_NAME: WrapperField = WrapperField("DenominatorDOF", FieldType.DOUBLE)
    ENTRYNAME__FIELD_NAME: WrapperField = WrapperField("EntryName", FieldType.STRING)
    FVALUE__FIELD_NAME: WrapperField = WrapperField("fValue", FieldType.DOUBLE)
    MULTIPARENTLINK207__FIELD_NAME: WrapperField = WrapperField("MultiParentLink207", FieldType.MULTIPARENTLINK)
    NUMERATORDOF__FIELD_NAME: WrapperField = WrapperField("NumeratorDOF", FieldType.DOUBLE)
    PVALUE__FIELD_NAME: WrapperField = WrapperField("pValue", FieldType.DOUBLE)
    RSQUARED__FIELD_NAME: WrapperField = WrapperField("RSquared", FieldType.DOUBLE)
    SERIESNAME__FIELD_NAME: WrapperField = WrapperField("SeriesName", FieldType.STRING)
    SOURCEENTRYID__FIELD_NAME: WrapperField = WrapperField("SourceEntryId", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_A0_field(self, value: Optional[float]):
        """
        Set data field with field name 'A0' on this record model
        """
        self.set_field_value(self.A0__FIELD_NAME.field_name, value)

    def get_A0_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A0' from this record model
        """
        return self.get_field_value(self.A0__FIELD_NAME.field_name)

    def set_A1_field(self, value: Optional[float]):
        """
        Set data field with field name 'A1' on this record model
        """
        self.set_field_value(self.A1__FIELD_NAME.field_name, value)

    def get_A1_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A1' from this record model
        """
        return self.get_field_value(self.A1__FIELD_NAME.field_name)

    def set_A2_field(self, value: Optional[float]):
        """
        Set data field with field name 'A2' on this record model
        """
        self.set_field_value(self.A2__FIELD_NAME.field_name, value)

    def get_A2_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A2' from this record model
        """
        return self.get_field_value(self.A2__FIELD_NAME.field_name)

    def set_A3_field(self, value: Optional[float]):
        """
        Set data field with field name 'A3' on this record model
        """
        self.set_field_value(self.A3__FIELD_NAME.field_name, value)

    def get_A3_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A3' from this record model
        """
        return self.get_field_value(self.A3__FIELD_NAME.field_name)

    def set_A4_field(self, value: Optional[float]):
        """
        Set data field with field name 'A4' on this record model
        """
        self.set_field_value(self.A4__FIELD_NAME.field_name, value)

    def get_A4_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A4' from this record model
        """
        return self.get_field_value(self.A4__FIELD_NAME.field_name)

    def set_A5_field(self, value: Optional[float]):
        """
        Set data field with field name 'A5' on this record model
        """
        self.set_field_value(self.A5__FIELD_NAME.field_name, value)

    def get_A5_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A5' from this record model
        """
        return self.get_field_value(self.A5__FIELD_NAME.field_name)

    def set_A6_field(self, value: Optional[float]):
        """
        Set data field with field name 'A6' on this record model
        """
        self.set_field_value(self.A6__FIELD_NAME.field_name, value)

    def get_A6_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A6' from this record model
        """
        return self.get_field_value(self.A6__FIELD_NAME.field_name)

    def set_A7_field(self, value: Optional[float]):
        """
        Set data field with field name 'A7' on this record model
        """
        self.set_field_value(self.A7__FIELD_NAME.field_name, value)

    def get_A7_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A7' from this record model
        """
        return self.get_field_value(self.A7__FIELD_NAME.field_name)

    def set_A8_field(self, value: Optional[float]):
        """
        Set data field with field name 'A8' on this record model
        """
        self.set_field_value(self.A8__FIELD_NAME.field_name, value)

    def get_A8_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A8' from this record model
        """
        return self.get_field_value(self.A8__FIELD_NAME.field_name)

    def set_A9_field(self, value: Optional[float]):
        """
        Set data field with field name 'A9' on this record model
        """
        self.set_field_value(self.A9__FIELD_NAME.field_name, value)

    def get_A9_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A9' from this record model
        """
        return self.get_field_value(self.A9__FIELD_NAME.field_name)

    def set_A10_field(self, value: Optional[float]):
        """
        Set data field with field name 'A10' on this record model
        """
        self.set_field_value(self.A10__FIELD_NAME.field_name, value)

    def get_A10_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A10' from this record model
        """
        return self.get_field_value(self.A10__FIELD_NAME.field_name)

    def set_AdjRSquared_field(self, value: Optional[float]):
        """
        Set data field with field name 'AdjRSquared' on this record model
        """
        self.set_field_value(self.ADJRSQUARED__FIELD_NAME.field_name, value)

    def get_AdjRSquared_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AdjRSquared' from this record model
        """
        return self.get_field_value(self.ADJRSQUARED__FIELD_NAME.field_name)

    def set_DegreeOfPolynomial_field(self, value: Optional[int]):
        """
        Set data field with field name 'DegreeOfPolynomial' on this record model
        """
        self.set_field_value(self.DEGREEOFPOLYNOMIAL__FIELD_NAME.field_name, value)

    def get_DegreeOfPolynomial_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DegreeOfPolynomial' from this record model
        """
        return self.get_field_value(self.DEGREEOFPOLYNOMIAL__FIELD_NAME.field_name)

    def set_DenominatorDOF_field(self, value: Optional[float]):
        """
        Set data field with field name 'DenominatorDOF' on this record model
        """
        self.set_field_value(self.DENOMINATORDOF__FIELD_NAME.field_name, value)

    def get_DenominatorDOF_field(self) -> Optional[float]:
        """
        Get data field value with field name 'DenominatorDOF' from this record model
        """
        return self.get_field_value(self.DENOMINATORDOF__FIELD_NAME.field_name)

    def set_EntryName_field(self, value: Optional[str]):
        """
        Set data field with field name 'EntryName' on this record model
        """
        self.set_field_value(self.ENTRYNAME__FIELD_NAME.field_name, value)

    def get_EntryName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EntryName' from this record model
        """
        return self.get_field_value(self.ENTRYNAME__FIELD_NAME.field_name)

    def set_fValue_field(self, value: Optional[float]):
        """
        Set data field with field name 'fValue' on this record model
        """
        self.set_field_value(self.FVALUE__FIELD_NAME.field_name, value)

    def get_fValue_field(self) -> Optional[float]:
        """
        Get data field value with field name 'fValue' from this record model
        """
        return self.get_field_value(self.FVALUE__FIELD_NAME.field_name)

    def set_NumeratorDOF_field(self, value: Optional[float]):
        """
        Set data field with field name 'NumeratorDOF' on this record model
        """
        self.set_field_value(self.NUMERATORDOF__FIELD_NAME.field_name, value)

    def get_NumeratorDOF_field(self) -> Optional[float]:
        """
        Get data field value with field name 'NumeratorDOF' from this record model
        """
        return self.get_field_value(self.NUMERATORDOF__FIELD_NAME.field_name)

    def set_pValue_field(self, value: Optional[float]):
        """
        Set data field with field name 'pValue' on this record model
        """
        self.set_field_value(self.PVALUE__FIELD_NAME.field_name, value)

    def get_pValue_field(self) -> Optional[float]:
        """
        Get data field value with field name 'pValue' from this record model
        """
        return self.get_field_value(self.PVALUE__FIELD_NAME.field_name)

    def set_RSquared_field(self, value: Optional[float]):
        """
        Set data field with field name 'RSquared' on this record model
        """
        self.set_field_value(self.RSQUARED__FIELD_NAME.field_name, value)

    def get_RSquared_field(self) -> Optional[float]:
        """
        Get data field value with field name 'RSquared' from this record model
        """
        return self.get_field_value(self.RSQUARED__FIELD_NAME.field_name)

    def set_SeriesName_field(self, value: Optional[str]):
        """
        Set data field with field name 'SeriesName' on this record model
        """
        self.set_field_value(self.SERIESNAME__FIELD_NAME.field_name, value)

    def get_SeriesName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SeriesName' from this record model
        """
        return self.get_field_value(self.SERIESNAME__FIELD_NAME.field_name)

    def set_SourceEntryId_field(self, value: Optional[int]):
        """
        Set data field with field name 'SourceEntryId' on this record model
        """
        self.set_field_value(self.SOURCEENTRYID__FIELD_NAME.field_name, value)

    def get_SourceEntryId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SourceEntryId' from this record model
        """
        return self.get_field_value(self.SOURCEENTRYID__FIELD_NAME.field_name)


class MaintenanceItemModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type MaintenanceItem
    Data Type Display Name: Instrument Maintenance Item (Instrument Maintenance Items)
    Fields: ActiveWorkflowId, ActiveWorkflowName, AlertAdvanceNoticeInDays, CanPerformMaintenance, DeactivateIfPastDue, LastPerformedDate, MaintenanceComment, MaintenanceDate, MaintenanceGracePeriod, MaintenanceReason, MaintenanceStatus, MaintenanceTechnician, MaxNotifications, NextDueDate, NotificationUserGroupList, PreReceiptCount, RepeatInstrumentMaintenance, RepeatInterval, RepeatIntervalTime, RequirementType, RequiresApproval, RequiresESignatures, SentNotifications, ServiceDescription, WorkOrderNumber
    """
    DATA_TYPE_NAME: str = 'MaintenanceItem'
    ACTIVEWORKFLOWID__FIELD_NAME: WrapperField = WrapperField("ActiveWorkflowId", FieldType.LONG)
    ACTIVEWORKFLOWNAME__FIELD_NAME: WrapperField = WrapperField("ActiveWorkflowName", FieldType.SELECTION)
    ALERTADVANCENOTICEINDAYS__FIELD_NAME: WrapperField = WrapperField("AlertAdvanceNoticeInDays", FieldType.LONG)
    CANPERFORMMAINTENANCE__FIELD_NAME: WrapperField = WrapperField("CanPerformMaintenance", FieldType.SELECTION)
    DEACTIVATEIFPASTDUE__FIELD_NAME: WrapperField = WrapperField("DeactivateIfPastDue", FieldType.BOOLEAN)
    LASTPERFORMEDDATE__FIELD_NAME: WrapperField = WrapperField("LastPerformedDate", FieldType.DATE)
    MAINTENANCECOMMENT__FIELD_NAME: WrapperField = WrapperField("MaintenanceComment", FieldType.STRING)
    MAINTENANCEDATE__FIELD_NAME: WrapperField = WrapperField("MaintenanceDate", FieldType.DATE)
    MAINTENANCEGRACEPERIOD__FIELD_NAME: WrapperField = WrapperField("MaintenanceGracePeriod", FieldType.LONG)
    MAINTENANCEREASON__FIELD_NAME: WrapperField = WrapperField("MaintenanceReason", FieldType.PICKLIST)
    MAINTENANCESTATUS__FIELD_NAME: WrapperField = WrapperField("MaintenanceStatus", FieldType.PICKLIST)
    MAINTENANCETECHNICIAN__FIELD_NAME: WrapperField = WrapperField("MaintenanceTechnician", FieldType.SELECTION)
    MAXNOTIFICATIONS__FIELD_NAME: WrapperField = WrapperField("MaxNotifications", FieldType.INTEGER)
    NEXTDUEDATE__FIELD_NAME: WrapperField = WrapperField("NextDueDate", FieldType.DATE)
    NOTIFICATIONUSERGROUPLIST__FIELD_NAME: WrapperField = WrapperField("NotificationUserGroupList", FieldType.SELECTION)
    PRERECEIPTCOUNT__FIELD_NAME: WrapperField = WrapperField("PreReceiptCount", FieldType.LONG)
    REPEATINSTRUMENTMAINTENANCE__FIELD_NAME: WrapperField = WrapperField("RepeatInstrumentMaintenance", FieldType.PICKLIST)
    REPEATINTERVAL__FIELD_NAME: WrapperField = WrapperField("RepeatInterval", FieldType.LONG)
    REPEATINTERVALTIME__FIELD_NAME: WrapperField = WrapperField("RepeatIntervalTime", FieldType.PICKLIST)
    REQUIREMENTTYPE__FIELD_NAME: WrapperField = WrapperField("RequirementType", FieldType.PICKLIST)
    REQUIRESAPPROVAL__FIELD_NAME: WrapperField = WrapperField("RequiresApproval", FieldType.PICKLIST)
    REQUIRESESIGNATURES__FIELD_NAME: WrapperField = WrapperField("RequiresESignatures", FieldType.BOOLEAN)
    SENTNOTIFICATIONS__FIELD_NAME: WrapperField = WrapperField("SentNotifications", FieldType.INTEGER)
    SERVICEDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("ServiceDescription", FieldType.STRING)
    WORKORDERNUMBER__FIELD_NAME: WrapperField = WrapperField("WorkOrderNumber", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActiveWorkflowId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ActiveWorkflowId' on this record model
        """
        self.set_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name, value)

    def get_ActiveWorkflowId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ActiveWorkflowId' from this record model
        """
        return self.get_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name)

    def set_ActiveWorkflowName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ActiveWorkflowName' on this record model
        """
        self.set_field_value(self.ACTIVEWORKFLOWNAME__FIELD_NAME.field_name, value)

    def get_ActiveWorkflowName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ActiveWorkflowName' from this record model
        """
        return self.get_field_value(self.ACTIVEWORKFLOWNAME__FIELD_NAME.field_name)

    def set_AlertAdvanceNoticeInDays_field(self, value: Optional[int]):
        """
        Set data field with field name 'AlertAdvanceNoticeInDays' on this record model
        """
        self.set_field_value(self.ALERTADVANCENOTICEINDAYS__FIELD_NAME.field_name, value)

    def get_AlertAdvanceNoticeInDays_field(self) -> Optional[int]:
        """
        Get data field value with field name 'AlertAdvanceNoticeInDays' from this record model
        """
        return self.get_field_value(self.ALERTADVANCENOTICEINDAYS__FIELD_NAME.field_name)

    def set_CanPerformMaintenance_field(self, value: Optional[str]):
        """
        Set data field with field name 'CanPerformMaintenance' on this record model
        """
        self.set_field_value(self.CANPERFORMMAINTENANCE__FIELD_NAME.field_name, value)

    def get_CanPerformMaintenance_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CanPerformMaintenance' from this record model
        """
        return self.get_field_value(self.CANPERFORMMAINTENANCE__FIELD_NAME.field_name)

    def set_DeactivateIfPastDue_field(self, value: Optional[bool]):
        """
        Set data field with field name 'DeactivateIfPastDue' on this record model
        """
        self.set_field_value(self.DEACTIVATEIFPASTDUE__FIELD_NAME.field_name, value)

    def get_DeactivateIfPastDue_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'DeactivateIfPastDue' from this record model
        """
        return self.get_field_value(self.DEACTIVATEIFPASTDUE__FIELD_NAME.field_name)

    def set_LastPerformedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'LastPerformedDate' on this record model
        """
        self.set_field_value(self.LASTPERFORMEDDATE__FIELD_NAME.field_name, value)

    def get_LastPerformedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'LastPerformedDate' from this record model
        """
        return self.get_field_value(self.LASTPERFORMEDDATE__FIELD_NAME.field_name)

    def set_MaintenanceComment_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaintenanceComment' on this record model
        """
        self.set_field_value(self.MAINTENANCECOMMENT__FIELD_NAME.field_name, value)

    def get_MaintenanceComment_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaintenanceComment' from this record model
        """
        return self.get_field_value(self.MAINTENANCECOMMENT__FIELD_NAME.field_name)

    def set_MaintenanceDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'MaintenanceDate' on this record model
        """
        self.set_field_value(self.MAINTENANCEDATE__FIELD_NAME.field_name, value)

    def get_MaintenanceDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MaintenanceDate' from this record model
        """
        return self.get_field_value(self.MAINTENANCEDATE__FIELD_NAME.field_name)

    def set_MaintenanceGracePeriod_field(self, value: Optional[int]):
        """
        Set data field with field name 'MaintenanceGracePeriod' on this record model
        """
        self.set_field_value(self.MAINTENANCEGRACEPERIOD__FIELD_NAME.field_name, value)

    def get_MaintenanceGracePeriod_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MaintenanceGracePeriod' from this record model
        """
        return self.get_field_value(self.MAINTENANCEGRACEPERIOD__FIELD_NAME.field_name)

    def set_MaintenanceReason_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaintenanceReason' on this record model
        """
        self.set_field_value(self.MAINTENANCEREASON__FIELD_NAME.field_name, value)

    def get_MaintenanceReason_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaintenanceReason' from this record model
        """
        return self.get_field_value(self.MAINTENANCEREASON__FIELD_NAME.field_name)

    def set_MaintenanceStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaintenanceStatus' on this record model
        """
        self.set_field_value(self.MAINTENANCESTATUS__FIELD_NAME.field_name, value)

    def get_MaintenanceStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaintenanceStatus' from this record model
        """
        return self.get_field_value(self.MAINTENANCESTATUS__FIELD_NAME.field_name)

    def set_MaintenanceTechnician_field(self, value: Optional[str]):
        """
        Set data field with field name 'MaintenanceTechnician' on this record model
        """
        self.set_field_value(self.MAINTENANCETECHNICIAN__FIELD_NAME.field_name, value)

    def get_MaintenanceTechnician_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MaintenanceTechnician' from this record model
        """
        return self.get_field_value(self.MAINTENANCETECHNICIAN__FIELD_NAME.field_name)

    def set_MaxNotifications_field(self, value: Optional[int]):
        """
        Set data field with field name 'MaxNotifications' on this record model
        """
        self.set_field_value(self.MAXNOTIFICATIONS__FIELD_NAME.field_name, value)

    def get_MaxNotifications_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MaxNotifications' from this record model
        """
        return self.get_field_value(self.MAXNOTIFICATIONS__FIELD_NAME.field_name)

    def set_NextDueDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'NextDueDate' on this record model
        """
        self.set_field_value(self.NEXTDUEDATE__FIELD_NAME.field_name, value)

    def get_NextDueDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NextDueDate' from this record model
        """
        return self.get_field_value(self.NEXTDUEDATE__FIELD_NAME.field_name)

    def set_NotificationUserGroupList_field(self, value: Optional[str]):
        """
        Set data field with field name 'NotificationUserGroupList' on this record model
        """
        self.set_field_value(self.NOTIFICATIONUSERGROUPLIST__FIELD_NAME.field_name, value)

    def get_NotificationUserGroupList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NotificationUserGroupList' from this record model
        """
        return self.get_field_value(self.NOTIFICATIONUSERGROUPLIST__FIELD_NAME.field_name)

    def set_PreReceiptCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'PreReceiptCount' on this record model
        """
        self.set_field_value(self.PRERECEIPTCOUNT__FIELD_NAME.field_name, value)

    def get_PreReceiptCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PreReceiptCount' from this record model
        """
        return self.get_field_value(self.PRERECEIPTCOUNT__FIELD_NAME.field_name)

    def set_RepeatInstrumentMaintenance_field(self, value: Optional[str]):
        """
        Set data field with field name 'RepeatInstrumentMaintenance' on this record model
        """
        self.set_field_value(self.REPEATINSTRUMENTMAINTENANCE__FIELD_NAME.field_name, value)

    def get_RepeatInstrumentMaintenance_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RepeatInstrumentMaintenance' from this record model
        """
        return self.get_field_value(self.REPEATINSTRUMENTMAINTENANCE__FIELD_NAME.field_name)

    def set_RepeatInterval_field(self, value: Optional[int]):
        """
        Set data field with field name 'RepeatInterval' on this record model
        """
        self.set_field_value(self.REPEATINTERVAL__FIELD_NAME.field_name, value)

    def get_RepeatInterval_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RepeatInterval' from this record model
        """
        return self.get_field_value(self.REPEATINTERVAL__FIELD_NAME.field_name)

    def set_RepeatIntervalTime_field(self, value: Optional[str]):
        """
        Set data field with field name 'RepeatIntervalTime' on this record model
        """
        self.set_field_value(self.REPEATINTERVALTIME__FIELD_NAME.field_name, value)

    def get_RepeatIntervalTime_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RepeatIntervalTime' from this record model
        """
        return self.get_field_value(self.REPEATINTERVALTIME__FIELD_NAME.field_name)

    def set_RequirementType_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequirementType' on this record model
        """
        self.set_field_value(self.REQUIREMENTTYPE__FIELD_NAME.field_name, value)

    def get_RequirementType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequirementType' from this record model
        """
        return self.get_field_value(self.REQUIREMENTTYPE__FIELD_NAME.field_name)

    def set_RequiresApproval_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequiresApproval' on this record model
        """
        self.set_field_value(self.REQUIRESAPPROVAL__FIELD_NAME.field_name, value)

    def get_RequiresApproval_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequiresApproval' from this record model
        """
        return self.get_field_value(self.REQUIRESAPPROVAL__FIELD_NAME.field_name)

    def set_RequiresESignatures_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RequiresESignatures' on this record model
        """
        self.set_field_value(self.REQUIRESESIGNATURES__FIELD_NAME.field_name, value)

    def get_RequiresESignatures_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RequiresESignatures' from this record model
        """
        return self.get_field_value(self.REQUIRESESIGNATURES__FIELD_NAME.field_name)

    def set_SentNotifications_field(self, value: Optional[int]):
        """
        Set data field with field name 'SentNotifications' on this record model
        """
        self.set_field_value(self.SENTNOTIFICATIONS__FIELD_NAME.field_name, value)

    def get_SentNotifications_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SentNotifications' from this record model
        """
        return self.get_field_value(self.SENTNOTIFICATIONS__FIELD_NAME.field_name)

    def set_ServiceDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'ServiceDescription' on this record model
        """
        self.set_field_value(self.SERVICEDESCRIPTION__FIELD_NAME.field_name, value)

    def get_ServiceDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ServiceDescription' from this record model
        """
        return self.get_field_value(self.SERVICEDESCRIPTION__FIELD_NAME.field_name)

    def set_WorkOrderNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkOrderNumber' on this record model
        """
        self.set_field_value(self.WORKORDERNUMBER__FIELD_NAME.field_name, value)

    def get_WorkOrderNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkOrderNumber' from this record model
        """
        return self.get_field_value(self.WORKORDERNUMBER__FIELD_NAME.field_name)


class MasterMixIngredientModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type MasterMixIngredient
    Data Type Display Name: Master Mix Ingredient Definition (Master Mix Ingredient Definitions)
    Fields: ConcentrationUnits, ConsumableDataType, ConsumableItemDataType, ConsumableName, ConsumableRecordId, ConsumableType, ContributionPercent, ItemExtensionDataType, PartNumber, Quantity, Units
    """
    DATA_TYPE_NAME: str = 'MasterMixIngredient'
    CONCENTRATIONUNITS__FIELD_NAME: WrapperField = WrapperField("ConcentrationUnits", FieldType.PICKLIST)
    CONSUMABLEDATATYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableDataType", FieldType.STRING)
    CONSUMABLEITEMDATATYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableItemDataType", FieldType.SELECTION)
    CONSUMABLENAME__FIELD_NAME: WrapperField = WrapperField("ConsumableName", FieldType.STRING)
    CONSUMABLERECORDID__FIELD_NAME: WrapperField = WrapperField("ConsumableRecordId", FieldType.LONG)
    CONSUMABLETYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableType", FieldType.STRING)
    CONTRIBUTIONPERCENT__FIELD_NAME: WrapperField = WrapperField("ContributionPercent", FieldType.DOUBLE)
    ITEMEXTENSIONDATATYPE__FIELD_NAME: WrapperField = WrapperField("ItemExtensionDataType", FieldType.SELECTION)
    PARTNUMBER__FIELD_NAME: WrapperField = WrapperField("PartNumber", FieldType.STRING)
    QUANTITY__FIELD_NAME: WrapperField = WrapperField("Quantity", FieldType.DOUBLE)
    UNITS__FIELD_NAME: WrapperField = WrapperField("Units", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ConcentrationUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConcentrationUnits' on this record model
        """
        self.set_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name, value)

    def get_ConcentrationUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConcentrationUnits' from this record model
        """
        return self.get_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name)

    def set_ConsumableDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableDataType' on this record model
        """
        self.set_field_value(self.CONSUMABLEDATATYPE__FIELD_NAME.field_name, value)

    def get_ConsumableDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableDataType' from this record model
        """
        return self.get_field_value(self.CONSUMABLEDATATYPE__FIELD_NAME.field_name)

    def set_ConsumableItemDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableItemDataType' on this record model
        """
        self.set_field_value(self.CONSUMABLEITEMDATATYPE__FIELD_NAME.field_name, value)

    def get_ConsumableItemDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableItemDataType' from this record model
        """
        return self.get_field_value(self.CONSUMABLEITEMDATATYPE__FIELD_NAME.field_name)

    def set_ConsumableName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableName' on this record model
        """
        self.set_field_value(self.CONSUMABLENAME__FIELD_NAME.field_name, value)

    def get_ConsumableName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableName' from this record model
        """
        return self.get_field_value(self.CONSUMABLENAME__FIELD_NAME.field_name)

    def set_ConsumableRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ConsumableRecordId' on this record model
        """
        self.set_field_value(self.CONSUMABLERECORDID__FIELD_NAME.field_name, value)

    def get_ConsumableRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ConsumableRecordId' from this record model
        """
        return self.get_field_value(self.CONSUMABLERECORDID__FIELD_NAME.field_name)

    def set_ConsumableType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableType' on this record model
        """
        self.set_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name, value)

    def get_ConsumableType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableType' from this record model
        """
        return self.get_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name)

    def set_ContributionPercent_field(self, value: Optional[float]):
        """
        Set data field with field name 'ContributionPercent' on this record model
        """
        self.set_field_value(self.CONTRIBUTIONPERCENT__FIELD_NAME.field_name, value)

    def get_ContributionPercent_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ContributionPercent' from this record model
        """
        return self.get_field_value(self.CONTRIBUTIONPERCENT__FIELD_NAME.field_name)

    def set_ItemExtensionDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ItemExtensionDataType' on this record model
        """
        self.set_field_value(self.ITEMEXTENSIONDATATYPE__FIELD_NAME.field_name, value)

    def get_ItemExtensionDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ItemExtensionDataType' from this record model
        """
        return self.get_field_value(self.ITEMEXTENSIONDATATYPE__FIELD_NAME.field_name)

    def set_PartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PartNumber' on this record model
        """
        self.set_field_value(self.PARTNUMBER__FIELD_NAME.field_name, value)

    def get_PartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PartNumber' from this record model
        """
        return self.get_field_value(self.PARTNUMBER__FIELD_NAME.field_name)

    def set_Quantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'Quantity' on this record model
        """
        self.set_field_value(self.QUANTITY__FIELD_NAME.field_name, value)

    def get_Quantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Quantity' from this record model
        """
        return self.get_field_value(self.QUANTITY__FIELD_NAME.field_name)

    def set_Units_field(self, value: Optional[str]):
        """
        Set data field with field name 'Units' on this record model
        """
        self.set_field_value(self.UNITS__FIELD_NAME.field_name, value)

    def get_Units_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Units' from this record model
        """
        return self.get_field_value(self.UNITS__FIELD_NAME.field_name)


class MasterMixInstructionsModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type MasterMixInstructions
    Data Type Display Name: Master Mix Instruction (Master Mix Instructions)
    Fields: Instructions
    """
    DATA_TYPE_NAME: str = 'MasterMixInstructions'
    INSTRUCTIONS__FIELD_NAME: WrapperField = WrapperField("Instructions", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Instructions_field(self, value: Optional[str]):
        """
        Set data field with field name 'Instructions' on this record model
        """
        self.set_field_value(self.INSTRUCTIONS__FIELD_NAME.field_name, value)

    def get_Instructions_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Instructions' from this record model
        """
        return self.get_field_value(self.INSTRUCTIONS__FIELD_NAME.field_name)


class MasterMixItemModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type MasterMixItem
    Data Type Display Name: Master Mix Ingredient (Master Mix Ingredients)
    Fields: ConcentrationUnits, ConsumableBarcode, ConsumableDataType, ConsumableItemDataType, ConsumableRecordId, ConsumableType, ItemExtensionDataType, LockFields, LotNumber, Notes, PartNumber, QuantityToUse, Units
    The MasterMixItem Data Type
    """
    DATA_TYPE_NAME: str = 'MasterMixItem'
    CONCENTRATIONUNITS__FIELD_NAME: WrapperField = WrapperField("ConcentrationUnits", FieldType.PICKLIST)
    CONSUMABLEBARCODE__FIELD_NAME: WrapperField = WrapperField("ConsumableBarcode", FieldType.SELECTION)
    CONSUMABLEDATATYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableDataType", FieldType.STRING)
    CONSUMABLEITEMDATATYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableItemDataType", FieldType.SELECTION)
    CONSUMABLERECORDID__FIELD_NAME: WrapperField = WrapperField("ConsumableRecordId", FieldType.LONG)
    CONSUMABLETYPE__FIELD_NAME: WrapperField = WrapperField("ConsumableType", FieldType.SELECTION)
    ITEMEXTENSIONDATATYPE__FIELD_NAME: WrapperField = WrapperField("ItemExtensionDataType", FieldType.SELECTION)
    LOCKFIELDS__FIELD_NAME: WrapperField = WrapperField("LockFields", FieldType.BOOLEAN)
    LOTNUMBER__FIELD_NAME: WrapperField = WrapperField("LotNumber", FieldType.SELECTION)
    NOTES__FIELD_NAME: WrapperField = WrapperField("Notes", FieldType.STRING)
    PARTNUMBER__FIELD_NAME: WrapperField = WrapperField("PartNumber", FieldType.STRING)
    QUANTITYTOUSE__FIELD_NAME: WrapperField = WrapperField("QuantityToUse", FieldType.DOUBLE)
    UNITS__FIELD_NAME: WrapperField = WrapperField("Units", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ConcentrationUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConcentrationUnits' on this record model
        """
        self.set_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name, value)

    def get_ConcentrationUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConcentrationUnits' from this record model
        """
        return self.get_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name)

    def set_ConsumableBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableBarcode' on this record model
        """
        self.set_field_value(self.CONSUMABLEBARCODE__FIELD_NAME.field_name, value)

    def get_ConsumableBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableBarcode' from this record model
        """
        return self.get_field_value(self.CONSUMABLEBARCODE__FIELD_NAME.field_name)

    def set_ConsumableDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableDataType' on this record model
        """
        self.set_field_value(self.CONSUMABLEDATATYPE__FIELD_NAME.field_name, value)

    def get_ConsumableDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableDataType' from this record model
        """
        return self.get_field_value(self.CONSUMABLEDATATYPE__FIELD_NAME.field_name)

    def set_ConsumableItemDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableItemDataType' on this record model
        """
        self.set_field_value(self.CONSUMABLEITEMDATATYPE__FIELD_NAME.field_name, value)

    def get_ConsumableItemDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableItemDataType' from this record model
        """
        return self.get_field_value(self.CONSUMABLEITEMDATATYPE__FIELD_NAME.field_name)

    def set_ConsumableRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ConsumableRecordId' on this record model
        """
        self.set_field_value(self.CONSUMABLERECORDID__FIELD_NAME.field_name, value)

    def get_ConsumableRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ConsumableRecordId' from this record model
        """
        return self.get_field_value(self.CONSUMABLERECORDID__FIELD_NAME.field_name)

    def set_ConsumableType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConsumableType' on this record model
        """
        self.set_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name, value)

    def get_ConsumableType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConsumableType' from this record model
        """
        return self.get_field_value(self.CONSUMABLETYPE__FIELD_NAME.field_name)

    def set_ItemExtensionDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ItemExtensionDataType' on this record model
        """
        self.set_field_value(self.ITEMEXTENSIONDATATYPE__FIELD_NAME.field_name, value)

    def get_ItemExtensionDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ItemExtensionDataType' from this record model
        """
        return self.get_field_value(self.ITEMEXTENSIONDATATYPE__FIELD_NAME.field_name)

    def set_LockFields_field(self, value: Optional[bool]):
        """
        Set data field with field name 'LockFields' on this record model
        """
        self.set_field_value(self.LOCKFIELDS__FIELD_NAME.field_name, value)

    def get_LockFields_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'LockFields' from this record model
        """
        return self.get_field_value(self.LOCKFIELDS__FIELD_NAME.field_name)

    def set_LotNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'LotNumber' on this record model
        """
        self.set_field_value(self.LOTNUMBER__FIELD_NAME.field_name, value)

    def get_LotNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LotNumber' from this record model
        """
        return self.get_field_value(self.LOTNUMBER__FIELD_NAME.field_name)

    def set_Notes_field(self, value: Optional[str]):
        """
        Set data field with field name 'Notes' on this record model
        """
        self.set_field_value(self.NOTES__FIELD_NAME.field_name, value)

    def get_Notes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Notes' from this record model
        """
        return self.get_field_value(self.NOTES__FIELD_NAME.field_name)

    def set_PartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PartNumber' on this record model
        """
        self.set_field_value(self.PARTNUMBER__FIELD_NAME.field_name, value)

    def get_PartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PartNumber' from this record model
        """
        return self.get_field_value(self.PARTNUMBER__FIELD_NAME.field_name)

    def set_QuantityToUse_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityToUse' on this record model
        """
        self.set_field_value(self.QUANTITYTOUSE__FIELD_NAME.field_name, value)

    def get_QuantityToUse_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityToUse' from this record model
        """
        return self.get_field_value(self.QUANTITYTOUSE__FIELD_NAME.field_name)

    def set_Units_field(self, value: Optional[str]):
        """
        Set data field with field name 'Units' on this record model
        """
        self.set_field_value(self.UNITS__FIELD_NAME.field_name, value)

    def get_Units_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Units' from this record model
        """
        return self.get_field_value(self.UNITS__FIELD_NAME.field_name)


class NotebookDirectoryModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type NotebookDirectory
    Data Type Display Name: Directory (Directories)
    Fields: DirectoryName, InheritRolesFromParent
    """
    DATA_TYPE_NAME: str = 'NotebookDirectory'
    DIRECTORYNAME__FIELD_NAME: WrapperField = WrapperField("DirectoryName", FieldType.STRING)
    INHERITROLESFROMPARENT__FIELD_NAME: WrapperField = WrapperField("InheritRolesFromParent", FieldType.BOOLEAN)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DirectoryName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DirectoryName' on this record model
        """
        self.set_field_value(self.DIRECTORYNAME__FIELD_NAME.field_name, value)

    def get_DirectoryName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DirectoryName' from this record model
        """
        return self.get_field_value(self.DIRECTORYNAME__FIELD_NAME.field_name)

    def set_InheritRolesFromParent_field(self, value: Optional[bool]):
        """
        Set data field with field name 'InheritRolesFromParent' on this record model
        """
        self.set_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name, value)

    def get_InheritRolesFromParent_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'InheritRolesFromParent' from this record model
        """
        return self.get_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name)


class PhasingPrephasingScoreModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PhasingPrephasingScore
    Data Type Display Name: Phasing and Prephasing Score (Phasing and Prephasing Scores)
    Fields: ColRead, Lane, LaneCol, ScoreOne, ScoreTwo
    <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'PhasingPrephasingScore'
    COLREAD__FIELD_NAME: WrapperField = WrapperField("ColRead", FieldType.STRING)
    LANE__FIELD_NAME: WrapperField = WrapperField("Lane", FieldType.LONG)
    LANECOL__FIELD_NAME: WrapperField = WrapperField("LaneCol", FieldType.STRING)
    SCOREONE__FIELD_NAME: WrapperField = WrapperField("ScoreOne", FieldType.DOUBLE)
    SCORETWO__FIELD_NAME: WrapperField = WrapperField("ScoreTwo", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColRead_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColRead' on this record model
        """
        self.set_field_value(self.COLREAD__FIELD_NAME.field_name, value)

    def get_ColRead_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColRead' from this record model
        """
        return self.get_field_value(self.COLREAD__FIELD_NAME.field_name)

    def set_Lane_field(self, value: Optional[int]):
        """
        Set data field with field name 'Lane' on this record model
        """
        self.set_field_value(self.LANE__FIELD_NAME.field_name, value)

    def get_Lane_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Lane' from this record model
        """
        return self.get_field_value(self.LANE__FIELD_NAME.field_name)

    def set_LaneCol_field(self, value: Optional[str]):
        """
        Set data field with field name 'LaneCol' on this record model
        """
        self.set_field_value(self.LANECOL__FIELD_NAME.field_name, value)

    def get_LaneCol_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LaneCol' from this record model
        """
        return self.get_field_value(self.LANECOL__FIELD_NAME.field_name)

    def set_ScoreOne_field(self, value: Optional[float]):
        """
        Set data field with field name 'ScoreOne' on this record model
        """
        self.set_field_value(self.SCOREONE__FIELD_NAME.field_name, value)

    def get_ScoreOne_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ScoreOne' from this record model
        """
        return self.get_field_value(self.SCOREONE__FIELD_NAME.field_name)

    def set_ScoreTwo_field(self, value: Optional[float]):
        """
        Set data field with field name 'ScoreTwo' on this record model
        """
        self.set_field_value(self.SCORETWO__FIELD_NAME.field_name, value)

    def get_ScoreTwo_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ScoreTwo' from this record model
        """
        return self.get_field_value(self.SCORETWO__FIELD_NAME.field_name)


class PlasmidModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Plasmid
    Data Type Display Name: Plasmid Part (Plasmid Parts)
    Fields: DownloadGenbankFile, GenebankAttachment, Name, PlasmidClassification, PlasmidName, QuantityOnHand, QuantityPerItem, ReorderLevelQuantity, Sequence, Units, Vendor
    """
    DATA_TYPE_NAME: str = 'Plasmid'
    DOWNLOADGENBANKFILE__FIELD_NAME: WrapperField = WrapperField("DownloadGenbankFile", FieldType.ACTION)
    GENEBANKATTACHMENT__FIELD_NAME: WrapperField = WrapperField("GenebankAttachment", FieldType.STRING)
    NAME__FIELD_NAME: WrapperField = WrapperField("Name", FieldType.STRING)
    PLASMIDCLASSIFICATION__FIELD_NAME: WrapperField = WrapperField("PlasmidClassification", FieldType.SELECTION)
    PLASMIDNAME__FIELD_NAME: WrapperField = WrapperField("PlasmidName", FieldType.AUTO_ACCESSION)
    QUANTITYONHAND__FIELD_NAME: WrapperField = WrapperField("QuantityOnHand", FieldType.DOUBLE)
    QUANTITYPERITEM__FIELD_NAME: WrapperField = WrapperField("QuantityPerItem", FieldType.DOUBLE)
    REORDERLEVELQUANTITY__FIELD_NAME: WrapperField = WrapperField("ReorderLevelQuantity", FieldType.DOUBLE)
    SEQUENCE__FIELD_NAME: WrapperField = WrapperField("Sequence", FieldType.STRING)
    UNITS__FIELD_NAME: WrapperField = WrapperField("Units", FieldType.PICKLIST)
    VENDOR__FIELD_NAME: WrapperField = WrapperField("Vendor", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_GenebankAttachment_field(self, value: Optional[str]):
        """
        Set data field with field name 'GenebankAttachment' on this record model
        """
        self.set_field_value(self.GENEBANKATTACHMENT__FIELD_NAME.field_name, value)

    def get_GenebankAttachment_field(self) -> Optional[str]:
        """
        Get data field value with field name 'GenebankAttachment' from this record model
        """
        return self.get_field_value(self.GENEBANKATTACHMENT__FIELD_NAME.field_name)

    def set_Name_field(self, value: Optional[str]):
        """
        Set data field with field name 'Name' on this record model
        """
        self.set_field_value(self.NAME__FIELD_NAME.field_name, value)

    def get_Name_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Name' from this record model
        """
        return self.get_field_value(self.NAME__FIELD_NAME.field_name)

    def set_PlasmidClassification_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlasmidClassification' on this record model
        """
        self.set_field_value(self.PLASMIDCLASSIFICATION__FIELD_NAME.field_name, value)

    def get_PlasmidClassification_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlasmidClassification' from this record model
        """
        return self.get_field_value(self.PLASMIDCLASSIFICATION__FIELD_NAME.field_name)

    def set_PlasmidName_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlasmidName' on this record model
        """
        self.set_field_value(self.PLASMIDNAME__FIELD_NAME.field_name, value)

    def get_PlasmidName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlasmidName' from this record model
        """
        return self.get_field_value(self.PLASMIDNAME__FIELD_NAME.field_name)

    def set_QuantityOnHand_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityOnHand' on this record model
        """
        self.set_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name, value)

    def get_QuantityOnHand_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityOnHand' from this record model
        """
        return self.get_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name)

    def set_QuantityPerItem_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityPerItem' on this record model
        """
        self.set_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name, value)

    def get_QuantityPerItem_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityPerItem' from this record model
        """
        return self.get_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name)

    def set_ReorderLevelQuantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'ReorderLevelQuantity' on this record model
        """
        self.set_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name, value)

    def get_ReorderLevelQuantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ReorderLevelQuantity' from this record model
        """
        return self.get_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name)

    def set_Sequence_field(self, value: Optional[str]):
        """
        Set data field with field name 'Sequence' on this record model
        """
        self.set_field_value(self.SEQUENCE__FIELD_NAME.field_name, value)

    def get_Sequence_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Sequence' from this record model
        """
        return self.get_field_value(self.SEQUENCE__FIELD_NAME.field_name)

    def set_Units_field(self, value: Optional[str]):
        """
        Set data field with field name 'Units' on this record model
        """
        self.set_field_value(self.UNITS__FIELD_NAME.field_name, value)

    def get_Units_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Units' from this record model
        """
        return self.get_field_value(self.UNITS__FIELD_NAME.field_name)

    def set_Vendor_field(self, value: Optional[str]):
        """
        Set data field with field name 'Vendor' on this record model
        """
        self.set_field_value(self.VENDOR__FIELD_NAME.field_name, value)

    def get_Vendor_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Vendor' from this record model
        """
        return self.get_field_value(self.VENDOR__FIELD_NAME.field_name)


class PlasmidItemModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PlasmidItem
    Data Type Display Name: Plasmid (Plasmids)
    Fields: ExpirationDate, Expired, KitLotNumbers, LotNumber, Name, PlasmidName, Sequence, Units
    """
    DATA_TYPE_NAME: str = 'PlasmidItem'
    EXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("ExpirationDate", FieldType.DATE)
    EXPIRED__FIELD_NAME: WrapperField = WrapperField("Expired", FieldType.BOOLEAN)
    KITLOTNUMBERS__FIELD_NAME: WrapperField = WrapperField("KitLotNumbers", FieldType.STRING)
    LOTNUMBER__FIELD_NAME: WrapperField = WrapperField("LotNumber", FieldType.STRING)
    NAME__FIELD_NAME: WrapperField = WrapperField("Name", FieldType.STRING)
    PLASMIDNAME__FIELD_NAME: WrapperField = WrapperField("PlasmidName", FieldType.STRING)
    SEQUENCE__FIELD_NAME: WrapperField = WrapperField("Sequence", FieldType.STRING)
    UNITS__FIELD_NAME: WrapperField = WrapperField("Units", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ExpirationDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ExpirationDate' on this record model
        """
        self.set_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_ExpirationDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ExpirationDate' from this record model
        """
        return self.get_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name)

    def set_Expired_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Expired' on this record model
        """
        self.set_field_value(self.EXPIRED__FIELD_NAME.field_name, value)

    def get_Expired_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Expired' from this record model
        """
        return self.get_field_value(self.EXPIRED__FIELD_NAME.field_name)

    def set_KitLotNumbers_field(self, value: Optional[str]):
        """
        Set data field with field name 'KitLotNumbers' on this record model
        """
        self.set_field_value(self.KITLOTNUMBERS__FIELD_NAME.field_name, value)

    def get_KitLotNumbers_field(self) -> Optional[str]:
        """
        Get data field value with field name 'KitLotNumbers' from this record model
        """
        return self.get_field_value(self.KITLOTNUMBERS__FIELD_NAME.field_name)

    def set_LotNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'LotNumber' on this record model
        """
        self.set_field_value(self.LOTNUMBER__FIELD_NAME.field_name, value)

    def get_LotNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LotNumber' from this record model
        """
        return self.get_field_value(self.LOTNUMBER__FIELD_NAME.field_name)

    def set_Name_field(self, value: Optional[str]):
        """
        Set data field with field name 'Name' on this record model
        """
        self.set_field_value(self.NAME__FIELD_NAME.field_name, value)

    def get_Name_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Name' from this record model
        """
        return self.get_field_value(self.NAME__FIELD_NAME.field_name)

    def set_PlasmidName_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlasmidName' on this record model
        """
        self.set_field_value(self.PLASMIDNAME__FIELD_NAME.field_name, value)

    def get_PlasmidName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlasmidName' from this record model
        """
        return self.get_field_value(self.PLASMIDNAME__FIELD_NAME.field_name)

    def set_Sequence_field(self, value: Optional[str]):
        """
        Set data field with field name 'Sequence' on this record model
        """
        self.set_field_value(self.SEQUENCE__FIELD_NAME.field_name, value)

    def get_Sequence_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Sequence' from this record model
        """
        return self.get_field_value(self.SEQUENCE__FIELD_NAME.field_name)

    def set_Units_field(self, value: Optional[str]):
        """
        Set data field with field name 'Units' on this record model
        """
        self.set_field_value(self.UNITS__FIELD_NAME.field_name, value)

    def get_Units_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Units' from this record model
        """
        return self.get_field_value(self.UNITS__FIELD_NAME.field_name)


class PlateModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Plate
    Data Type Display Name: Plate (Plates)
    Fields: ColPosition, ExemplarPlateStatus, MultiParentLink133, MultiParentLink153, MultiParentLink155, PlateColumns, PlateId, PlateRows, PlateSampleType, PlateWellCnt, RowPosition, StorageLocationBarcode, StorageUnitPath
    The Plate Data Type
    """
    DATA_TYPE_NAME: str = 'Plate'
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    EXEMPLARPLATESTATUS__FIELD_NAME: WrapperField = WrapperField("ExemplarPlateStatus", FieldType.SELECTION)
    MULTIPARENTLINK133__FIELD_NAME: WrapperField = WrapperField("MultiParentLink133", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK153__FIELD_NAME: WrapperField = WrapperField("MultiParentLink153", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK155__FIELD_NAME: WrapperField = WrapperField("MultiParentLink155", FieldType.MULTIPARENTLINK)
    PLATECOLUMNS__FIELD_NAME: WrapperField = WrapperField("PlateColumns", FieldType.INTEGER)
    PLATEID__FIELD_NAME: WrapperField = WrapperField("PlateId", FieldType.STRING)
    PLATEROWS__FIELD_NAME: WrapperField = WrapperField("PlateRows", FieldType.INTEGER)
    PLATESAMPLETYPE__FIELD_NAME: WrapperField = WrapperField("PlateSampleType", FieldType.SELECTION)
    PLATEWELLCNT__FIELD_NAME: WrapperField = WrapperField("PlateWellCnt", FieldType.ENUM)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    STORAGELOCATIONBARCODE__FIELD_NAME: WrapperField = WrapperField("StorageLocationBarcode", FieldType.SELECTION)
    STORAGEUNITPATH__FIELD_NAME: WrapperField = WrapperField("StorageUnitPath", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_ExemplarPlateStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExemplarPlateStatus' on this record model
        """
        self.set_field_value(self.EXEMPLARPLATESTATUS__FIELD_NAME.field_name, value)

    def get_ExemplarPlateStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExemplarPlateStatus' from this record model
        """
        return self.get_field_value(self.EXEMPLARPLATESTATUS__FIELD_NAME.field_name)

    def set_PlateColumns_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlateColumns' on this record model
        """
        self.set_field_value(self.PLATECOLUMNS__FIELD_NAME.field_name, value)

    def get_PlateColumns_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlateColumns' from this record model
        """
        return self.get_field_value(self.PLATECOLUMNS__FIELD_NAME.field_name)

    def set_PlateId_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlateId' on this record model
        """
        self.set_field_value(self.PLATEID__FIELD_NAME.field_name, value)

    def get_PlateId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlateId' from this record model
        """
        return self.get_field_value(self.PLATEID__FIELD_NAME.field_name)

    def set_PlateRows_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlateRows' on this record model
        """
        self.set_field_value(self.PLATEROWS__FIELD_NAME.field_name, value)

    def get_PlateRows_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlateRows' from this record model
        """
        return self.get_field_value(self.PLATEROWS__FIELD_NAME.field_name)

    def set_PlateSampleType_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlateSampleType' on this record model
        """
        self.set_field_value(self.PLATESAMPLETYPE__FIELD_NAME.field_name, value)

    def get_PlateSampleType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlateSampleType' from this record model
        """
        return self.get_field_value(self.PLATESAMPLETYPE__FIELD_NAME.field_name)

    def set_PlateWellCnt_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlateWellCnt' on this record model
        """
        self.set_field_value(self.PLATEWELLCNT__FIELD_NAME.field_name, value)

    def get_PlateWellCnt_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlateWellCnt' from this record model
        """
        return self.get_field_value(self.PLATEWELLCNT__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_StorageLocationBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageLocationBarcode' on this record model
        """
        self.set_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name, value)

    def get_StorageLocationBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageLocationBarcode' from this record model
        """
        return self.get_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name)

    def set_StorageUnitPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitPath' on this record model
        """
        self.set_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name, value)

    def get_StorageUnitPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitPath' from this record model
        """
        return self.get_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name)


class PlateDesignerWellAnnotationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PlateDesignerWellAnnotation
    Data Type Display Name: Plate Designer Well Annotation (Plate Designer Well Annotations)
    Fields: Notes
    Annotations for well element allows users to add additional notes at any location in a 3D plate.
    """
    DATA_TYPE_NAME: str = 'PlateDesignerWellAnnotation'
    NOTES__FIELD_NAME: WrapperField = WrapperField("Notes", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Notes_field(self, value: Optional[str]):
        """
        Set data field with field name 'Notes' on this record model
        """
        self.set_field_value(self.NOTES__FIELD_NAME.field_name, value)

    def get_Notes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Notes' from this record model
        """
        return self.get_field_value(self.NOTES__FIELD_NAME.field_name)


class PlateDesignerWellElementModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PlateDesignerWellElement
    Data Type Display Name: Plate Designer Well Element (Plate Designer Well Element)
    Fields: ActualVolumeRemoved, AliquotSampleRecordId, ColPosition, Concentration, ConcentrationUnits, ControlType, IsControl, Layer, PlateRecordId, RowPosition, SourceDataTypeName, SourceRecordId, SourceSampleConcentration, SourceSampleMass, SourceSampleVolume, SourceVolumeToRemove, TargetMass, Volume
    A well element describes a particular location in a 3D plate. Each well element in the system is uniquely identified by (Plate ID, Layer #, Row, Column).
A well element is always describing about either a payload of an existing record, or an annotation (or both).
    """
    DATA_TYPE_NAME: str = 'PlateDesignerWellElement'
    ACTUALVOLUMEREMOVED__FIELD_NAME: WrapperField = WrapperField("ActualVolumeRemoved", FieldType.DOUBLE)
    ALIQUOTSAMPLERECORDID__FIELD_NAME: WrapperField = WrapperField("AliquotSampleRecordId", FieldType.LONG)
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    CONCENTRATION__FIELD_NAME: WrapperField = WrapperField("Concentration", FieldType.DOUBLE)
    CONCENTRATIONUNITS__FIELD_NAME: WrapperField = WrapperField("ConcentrationUnits", FieldType.STRING)
    CONTROLTYPE__FIELD_NAME: WrapperField = WrapperField("ControlType", FieldType.STRING)
    ISCONTROL__FIELD_NAME: WrapperField = WrapperField("IsControl", FieldType.BOOLEAN)
    LAYER__FIELD_NAME: WrapperField = WrapperField("Layer", FieldType.INTEGER)
    PLATERECORDID__FIELD_NAME: WrapperField = WrapperField("PlateRecordId", FieldType.LONG)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    SOURCEDATATYPENAME__FIELD_NAME: WrapperField = WrapperField("SourceDataTypeName", FieldType.STRING)
    SOURCERECORDID__FIELD_NAME: WrapperField = WrapperField("SourceRecordId", FieldType.LONG)
    SOURCESAMPLECONCENTRATION__FIELD_NAME: WrapperField = WrapperField("SourceSampleConcentration", FieldType.DOUBLE)
    SOURCESAMPLEMASS__FIELD_NAME: WrapperField = WrapperField("SourceSampleMass", FieldType.DOUBLE)
    SOURCESAMPLEVOLUME__FIELD_NAME: WrapperField = WrapperField("SourceSampleVolume", FieldType.DOUBLE)
    SOURCEVOLUMETOREMOVE__FIELD_NAME: WrapperField = WrapperField("SourceVolumeToRemove", FieldType.DOUBLE)
    TARGETMASS__FIELD_NAME: WrapperField = WrapperField("TargetMass", FieldType.DOUBLE)
    VOLUME__FIELD_NAME: WrapperField = WrapperField("Volume", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActualVolumeRemoved_field(self, value: Optional[float]):
        """
        Set data field with field name 'ActualVolumeRemoved' on this record model
        """
        self.set_field_value(self.ACTUALVOLUMEREMOVED__FIELD_NAME.field_name, value)

    def get_ActualVolumeRemoved_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ActualVolumeRemoved' from this record model
        """
        return self.get_field_value(self.ACTUALVOLUMEREMOVED__FIELD_NAME.field_name)

    def set_AliquotSampleRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'AliquotSampleRecordId' on this record model
        """
        self.set_field_value(self.ALIQUOTSAMPLERECORDID__FIELD_NAME.field_name, value)

    def get_AliquotSampleRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'AliquotSampleRecordId' from this record model
        """
        return self.get_field_value(self.ALIQUOTSAMPLERECORDID__FIELD_NAME.field_name)

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_Concentration_field(self, value: Optional[float]):
        """
        Set data field with field name 'Concentration' on this record model
        """
        self.set_field_value(self.CONCENTRATION__FIELD_NAME.field_name, value)

    def get_Concentration_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Concentration' from this record model
        """
        return self.get_field_value(self.CONCENTRATION__FIELD_NAME.field_name)

    def set_ConcentrationUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConcentrationUnits' on this record model
        """
        self.set_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name, value)

    def get_ConcentrationUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConcentrationUnits' from this record model
        """
        return self.get_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name)

    def set_ControlType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ControlType' on this record model
        """
        self.set_field_value(self.CONTROLTYPE__FIELD_NAME.field_name, value)

    def get_ControlType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ControlType' from this record model
        """
        return self.get_field_value(self.CONTROLTYPE__FIELD_NAME.field_name)

    def set_IsControl_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsControl' on this record model
        """
        self.set_field_value(self.ISCONTROL__FIELD_NAME.field_name, value)

    def get_IsControl_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsControl' from this record model
        """
        return self.get_field_value(self.ISCONTROL__FIELD_NAME.field_name)

    def set_Layer_field(self, value: Optional[int]):
        """
        Set data field with field name 'Layer' on this record model
        """
        self.set_field_value(self.LAYER__FIELD_NAME.field_name, value)

    def get_Layer_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Layer' from this record model
        """
        return self.get_field_value(self.LAYER__FIELD_NAME.field_name)

    def set_PlateRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'PlateRecordId' on this record model
        """
        self.set_field_value(self.PLATERECORDID__FIELD_NAME.field_name, value)

    def get_PlateRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PlateRecordId' from this record model
        """
        return self.get_field_value(self.PLATERECORDID__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_SourceDataTypeName_field(self, value: Optional[str]):
        """
        Set data field with field name 'SourceDataTypeName' on this record model
        """
        self.set_field_value(self.SOURCEDATATYPENAME__FIELD_NAME.field_name, value)

    def get_SourceDataTypeName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SourceDataTypeName' from this record model
        """
        return self.get_field_value(self.SOURCEDATATYPENAME__FIELD_NAME.field_name)

    def set_SourceRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'SourceRecordId' on this record model
        """
        self.set_field_value(self.SOURCERECORDID__FIELD_NAME.field_name, value)

    def get_SourceRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SourceRecordId' from this record model
        """
        return self.get_field_value(self.SOURCERECORDID__FIELD_NAME.field_name)

    def set_SourceSampleConcentration_field(self, value: Optional[float]):
        """
        Set data field with field name 'SourceSampleConcentration' on this record model
        """
        self.set_field_value(self.SOURCESAMPLECONCENTRATION__FIELD_NAME.field_name, value)

    def get_SourceSampleConcentration_field(self) -> Optional[float]:
        """
        Get data field value with field name 'SourceSampleConcentration' from this record model
        """
        return self.get_field_value(self.SOURCESAMPLECONCENTRATION__FIELD_NAME.field_name)

    def set_SourceSampleMass_field(self, value: Optional[float]):
        """
        Set data field with field name 'SourceSampleMass' on this record model
        """
        self.set_field_value(self.SOURCESAMPLEMASS__FIELD_NAME.field_name, value)

    def get_SourceSampleMass_field(self) -> Optional[float]:
        """
        Get data field value with field name 'SourceSampleMass' from this record model
        """
        return self.get_field_value(self.SOURCESAMPLEMASS__FIELD_NAME.field_name)

    def set_SourceSampleVolume_field(self, value: Optional[float]):
        """
        Set data field with field name 'SourceSampleVolume' on this record model
        """
        self.set_field_value(self.SOURCESAMPLEVOLUME__FIELD_NAME.field_name, value)

    def get_SourceSampleVolume_field(self) -> Optional[float]:
        """
        Get data field value with field name 'SourceSampleVolume' from this record model
        """
        return self.get_field_value(self.SOURCESAMPLEVOLUME__FIELD_NAME.field_name)

    def set_SourceVolumeToRemove_field(self, value: Optional[float]):
        """
        Set data field with field name 'SourceVolumeToRemove' on this record model
        """
        self.set_field_value(self.SOURCEVOLUMETOREMOVE__FIELD_NAME.field_name, value)

    def get_SourceVolumeToRemove_field(self) -> Optional[float]:
        """
        Get data field value with field name 'SourceVolumeToRemove' from this record model
        """
        return self.get_field_value(self.SOURCEVOLUMETOREMOVE__FIELD_NAME.field_name)

    def set_TargetMass_field(self, value: Optional[float]):
        """
        Set data field with field name 'TargetMass' on this record model
        """
        self.set_field_value(self.TARGETMASS__FIELD_NAME.field_name, value)

    def get_TargetMass_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TargetMass' from this record model
        """
        return self.get_field_value(self.TARGETMASS__FIELD_NAME.field_name)

    def set_Volume_field(self, value: Optional[float]):
        """
        Set data field with field name 'Volume' on this record model
        """
        self.set_field_value(self.VOLUME__FIELD_NAME.field_name, value)

    def get_Volume_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Volume' from this record model
        """
        return self.get_field_value(self.VOLUME__FIELD_NAME.field_name)


class PlateMappingSrcItemModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PlateMappingSrcItem
    Data Type Display Name: Plate Mapping Source Item (Plate Mapping Source Items)
    Fields: ColPosition, Description, IsControl, MultiParentLink133, RowPosition, SourceItemId
    """
    DATA_TYPE_NAME: str = 'PlateMappingSrcItem'
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    ISCONTROL__FIELD_NAME: WrapperField = WrapperField("IsControl", FieldType.BOOLEAN)
    MULTIPARENTLINK133__FIELD_NAME: WrapperField = WrapperField("MultiParentLink133", FieldType.MULTIPARENTLINK)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    SOURCEITEMID__FIELD_NAME: WrapperField = WrapperField("SourceItemId", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_IsControl_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsControl' on this record model
        """
        self.set_field_value(self.ISCONTROL__FIELD_NAME.field_name, value)

    def get_IsControl_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsControl' from this record model
        """
        return self.get_field_value(self.ISCONTROL__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_SourceItemId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SourceItemId' on this record model
        """
        self.set_field_value(self.SOURCEITEMID__FIELD_NAME.field_name, value)

    def get_SourceItemId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SourceItemId' from this record model
        """
        return self.get_field_value(self.SOURCEITEMID__FIELD_NAME.field_name)


class PlateMappingTemplateExpModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PlateMappingTemplateExp
    Data Type Display Name: Plate Mapping Template (Plate Mapping Template)
    Fields: AllowControlsToShift, ControlType, DestinationPlatingOrder, DstPlateSizeCol, DstPlateSizeRow, MappingName, NumberOfPlates, NumberOfSamples, PlatingMethod, ReverseSortingOrder, SamplesHaveSourcePosition, SortOnField, SourcePlateDoesNotMatter, SrcPlateSizeCol, SrcPlateSizeRow, TargetConcentration, TargetVol, UseCustomPlatePrefix, WellCompaction
    """
    DATA_TYPE_NAME: str = 'PlateMappingTemplateExp'
    ALLOWCONTROLSTOSHIFT__FIELD_NAME: WrapperField = WrapperField("AllowControlsToShift", FieldType.BOOLEAN)
    CONTROLTYPE__FIELD_NAME: WrapperField = WrapperField("ControlType", FieldType.SELECTION)
    DESTINATIONPLATINGORDER__FIELD_NAME: WrapperField = WrapperField("DestinationPlatingOrder", FieldType.PICKLIST)
    DSTPLATESIZECOL__FIELD_NAME: WrapperField = WrapperField("DstPlateSizeCol", FieldType.INTEGER)
    DSTPLATESIZEROW__FIELD_NAME: WrapperField = WrapperField("DstPlateSizeRow", FieldType.INTEGER)
    MAPPINGNAME__FIELD_NAME: WrapperField = WrapperField("MappingName", FieldType.STRING)
    NUMBEROFPLATES__FIELD_NAME: WrapperField = WrapperField("NumberOfPlates", FieldType.INTEGER)
    NUMBEROFSAMPLES__FIELD_NAME: WrapperField = WrapperField("NumberOfSamples", FieldType.INTEGER)
    PLATINGMETHOD__FIELD_NAME: WrapperField = WrapperField("PlatingMethod", FieldType.PICKLIST)
    REVERSESORTINGORDER__FIELD_NAME: WrapperField = WrapperField("ReverseSortingOrder", FieldType.BOOLEAN)
    SAMPLESHAVESOURCEPOSITION__FIELD_NAME: WrapperField = WrapperField("SamplesHaveSourcePosition", FieldType.BOOLEAN)
    SORTONFIELD__FIELD_NAME: WrapperField = WrapperField("SortOnField", FieldType.SELECTION)
    SOURCEPLATEDOESNOTMATTER__FIELD_NAME: WrapperField = WrapperField("SourcePlateDoesNotMatter", FieldType.BOOLEAN)
    SRCPLATESIZECOL__FIELD_NAME: WrapperField = WrapperField("SrcPlateSizeCol", FieldType.INTEGER)
    SRCPLATESIZEROW__FIELD_NAME: WrapperField = WrapperField("SrcPlateSizeRow", FieldType.INTEGER)
    TARGETCONCENTRATION__FIELD_NAME: WrapperField = WrapperField("TargetConcentration", FieldType.DOUBLE)
    TARGETVOL__FIELD_NAME: WrapperField = WrapperField("TargetVol", FieldType.DOUBLE)
    USECUSTOMPLATEPREFIX__FIELD_NAME: WrapperField = WrapperField("UseCustomPlatePrefix", FieldType.BOOLEAN)
    WELLCOMPACTION__FIELD_NAME: WrapperField = WrapperField("WellCompaction", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AllowControlsToShift_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AllowControlsToShift' on this record model
        """
        self.set_field_value(self.ALLOWCONTROLSTOSHIFT__FIELD_NAME.field_name, value)

    def get_AllowControlsToShift_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AllowControlsToShift' from this record model
        """
        return self.get_field_value(self.ALLOWCONTROLSTOSHIFT__FIELD_NAME.field_name)

    def set_ControlType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ControlType' on this record model
        """
        self.set_field_value(self.CONTROLTYPE__FIELD_NAME.field_name, value)

    def get_ControlType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ControlType' from this record model
        """
        return self.get_field_value(self.CONTROLTYPE__FIELD_NAME.field_name)

    def set_DestinationPlatingOrder_field(self, value: Optional[str]):
        """
        Set data field with field name 'DestinationPlatingOrder' on this record model
        """
        self.set_field_value(self.DESTINATIONPLATINGORDER__FIELD_NAME.field_name, value)

    def get_DestinationPlatingOrder_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DestinationPlatingOrder' from this record model
        """
        return self.get_field_value(self.DESTINATIONPLATINGORDER__FIELD_NAME.field_name)

    def set_DstPlateSizeCol_field(self, value: Optional[int]):
        """
        Set data field with field name 'DstPlateSizeCol' on this record model
        """
        self.set_field_value(self.DSTPLATESIZECOL__FIELD_NAME.field_name, value)

    def get_DstPlateSizeCol_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DstPlateSizeCol' from this record model
        """
        return self.get_field_value(self.DSTPLATESIZECOL__FIELD_NAME.field_name)

    def set_DstPlateSizeRow_field(self, value: Optional[int]):
        """
        Set data field with field name 'DstPlateSizeRow' on this record model
        """
        self.set_field_value(self.DSTPLATESIZEROW__FIELD_NAME.field_name, value)

    def get_DstPlateSizeRow_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DstPlateSizeRow' from this record model
        """
        return self.get_field_value(self.DSTPLATESIZEROW__FIELD_NAME.field_name)

    def set_MappingName_field(self, value: Optional[str]):
        """
        Set data field with field name 'MappingName' on this record model
        """
        self.set_field_value(self.MAPPINGNAME__FIELD_NAME.field_name, value)

    def get_MappingName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MappingName' from this record model
        """
        return self.get_field_value(self.MAPPINGNAME__FIELD_NAME.field_name)

    def set_NumberOfPlates_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumberOfPlates' on this record model
        """
        self.set_field_value(self.NUMBEROFPLATES__FIELD_NAME.field_name, value)

    def get_NumberOfPlates_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumberOfPlates' from this record model
        """
        return self.get_field_value(self.NUMBEROFPLATES__FIELD_NAME.field_name)

    def set_NumberOfSamples_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumberOfSamples' on this record model
        """
        self.set_field_value(self.NUMBEROFSAMPLES__FIELD_NAME.field_name, value)

    def get_NumberOfSamples_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumberOfSamples' from this record model
        """
        return self.get_field_value(self.NUMBEROFSAMPLES__FIELD_NAME.field_name)

    def set_PlatingMethod_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlatingMethod' on this record model
        """
        self.set_field_value(self.PLATINGMETHOD__FIELD_NAME.field_name, value)

    def get_PlatingMethod_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlatingMethod' from this record model
        """
        return self.get_field_value(self.PLATINGMETHOD__FIELD_NAME.field_name)

    def set_ReverseSortingOrder_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ReverseSortingOrder' on this record model
        """
        self.set_field_value(self.REVERSESORTINGORDER__FIELD_NAME.field_name, value)

    def get_ReverseSortingOrder_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ReverseSortingOrder' from this record model
        """
        return self.get_field_value(self.REVERSESORTINGORDER__FIELD_NAME.field_name)

    def set_SamplesHaveSourcePosition_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SamplesHaveSourcePosition' on this record model
        """
        self.set_field_value(self.SAMPLESHAVESOURCEPOSITION__FIELD_NAME.field_name, value)

    def get_SamplesHaveSourcePosition_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SamplesHaveSourcePosition' from this record model
        """
        return self.get_field_value(self.SAMPLESHAVESOURCEPOSITION__FIELD_NAME.field_name)

    def set_SortOnField_field(self, value: Optional[str]):
        """
        Set data field with field name 'SortOnField' on this record model
        """
        self.set_field_value(self.SORTONFIELD__FIELD_NAME.field_name, value)

    def get_SortOnField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SortOnField' from this record model
        """
        return self.get_field_value(self.SORTONFIELD__FIELD_NAME.field_name)

    def set_SourcePlateDoesNotMatter_field(self, value: Optional[bool]):
        """
        Set data field with field name 'SourcePlateDoesNotMatter' on this record model
        """
        self.set_field_value(self.SOURCEPLATEDOESNOTMATTER__FIELD_NAME.field_name, value)

    def get_SourcePlateDoesNotMatter_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'SourcePlateDoesNotMatter' from this record model
        """
        return self.get_field_value(self.SOURCEPLATEDOESNOTMATTER__FIELD_NAME.field_name)

    def set_SrcPlateSizeCol_field(self, value: Optional[int]):
        """
        Set data field with field name 'SrcPlateSizeCol' on this record model
        """
        self.set_field_value(self.SRCPLATESIZECOL__FIELD_NAME.field_name, value)

    def get_SrcPlateSizeCol_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SrcPlateSizeCol' from this record model
        """
        return self.get_field_value(self.SRCPLATESIZECOL__FIELD_NAME.field_name)

    def set_SrcPlateSizeRow_field(self, value: Optional[int]):
        """
        Set data field with field name 'SrcPlateSizeRow' on this record model
        """
        self.set_field_value(self.SRCPLATESIZEROW__FIELD_NAME.field_name, value)

    def get_SrcPlateSizeRow_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SrcPlateSizeRow' from this record model
        """
        return self.get_field_value(self.SRCPLATESIZEROW__FIELD_NAME.field_name)

    def set_TargetConcentration_field(self, value: Optional[float]):
        """
        Set data field with field name 'TargetConcentration' on this record model
        """
        self.set_field_value(self.TARGETCONCENTRATION__FIELD_NAME.field_name, value)

    def get_TargetConcentration_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TargetConcentration' from this record model
        """
        return self.get_field_value(self.TARGETCONCENTRATION__FIELD_NAME.field_name)

    def set_TargetVol_field(self, value: Optional[float]):
        """
        Set data field with field name 'TargetVol' on this record model
        """
        self.set_field_value(self.TARGETVOL__FIELD_NAME.field_name, value)

    def get_TargetVol_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TargetVol' from this record model
        """
        return self.get_field_value(self.TARGETVOL__FIELD_NAME.field_name)

    def set_UseCustomPlatePrefix_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UseCustomPlatePrefix' on this record model
        """
        self.set_field_value(self.USECUSTOMPLATEPREFIX__FIELD_NAME.field_name, value)

    def get_UseCustomPlatePrefix_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UseCustomPlatePrefix' from this record model
        """
        return self.get_field_value(self.USECUSTOMPLATEPREFIX__FIELD_NAME.field_name)

    def set_WellCompaction_field(self, value: Optional[str]):
        """
        Set data field with field name 'WellCompaction' on this record model
        """
        self.set_field_value(self.WELLCOMPACTION__FIELD_NAME.field_name, value)

    def get_WellCompaction_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WellCompaction' from this record model
        """
        return self.get_field_value(self.WELLCOMPACTION__FIELD_NAME.field_name)


class PlateTemplateModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PlateTemplate
    Data Type Display Name: Plate Template (Plate Templates)
    Fields: TemplateDescription, TemplateDimensions, TemplateName
    """
    DATA_TYPE_NAME: str = 'PlateTemplate'
    TEMPLATEDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("TemplateDescription", FieldType.STRING)
    TEMPLATEDIMENSIONS__FIELD_NAME: WrapperField = WrapperField("TemplateDimensions", FieldType.STRING)
    TEMPLATENAME__FIELD_NAME: WrapperField = WrapperField("TemplateName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_TemplateDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateDescription' on this record model
        """
        self.set_field_value(self.TEMPLATEDESCRIPTION__FIELD_NAME.field_name, value)

    def get_TemplateDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateDescription' from this record model
        """
        return self.get_field_value(self.TEMPLATEDESCRIPTION__FIELD_NAME.field_name)

    def set_TemplateDimensions_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateDimensions' on this record model
        """
        self.set_field_value(self.TEMPLATEDIMENSIONS__FIELD_NAME.field_name, value)

    def get_TemplateDimensions_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateDimensions' from this record model
        """
        return self.get_field_value(self.TEMPLATEDIMENSIONS__FIELD_NAME.field_name)

    def set_TemplateName_field(self, value: Optional[str]):
        """
        Set data field with field name 'TemplateName' on this record model
        """
        self.set_field_value(self.TEMPLATENAME__FIELD_NAME.field_name, value)

    def get_TemplateName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TemplateName' from this record model
        """
        return self.get_field_value(self.TEMPLATENAME__FIELD_NAME.field_name)


class PlateWellMappingModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type PlateWellMapping
    Data Type Display Name: Plate Well Mapping (Plate Well Mapping)
    Fields: Description, ExemplarSampleType, MultiParentLink133, NewControl, SourceItemId, SrcPlateIdAliq1, SrcWellPosAliq1, TargetConcentration, TargetPlateIdAliq1, TargetVol, TargetWellPosAliq1
    """
    DATA_TYPE_NAME: str = 'PlateWellMapping'
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    EXEMPLARSAMPLETYPE__FIELD_NAME: WrapperField = WrapperField("ExemplarSampleType", FieldType.SELECTION)
    MULTIPARENTLINK133__FIELD_NAME: WrapperField = WrapperField("MultiParentLink133", FieldType.MULTIPARENTLINK)
    NEWCONTROL__FIELD_NAME: WrapperField = WrapperField("NewControl", FieldType.BOOLEAN)
    SOURCEITEMID__FIELD_NAME: WrapperField = WrapperField("SourceItemId", FieldType.STRING)
    SRCPLATEIDALIQ1__FIELD_NAME: WrapperField = WrapperField("SrcPlateIdAliq1", FieldType.STRING)
    SRCWELLPOSALIQ1__FIELD_NAME: WrapperField = WrapperField("SrcWellPosAliq1", FieldType.STRING)
    TARGETCONCENTRATION__FIELD_NAME: WrapperField = WrapperField("TargetConcentration", FieldType.DOUBLE)
    TARGETPLATEIDALIQ1__FIELD_NAME: WrapperField = WrapperField("TargetPlateIdAliq1", FieldType.STRING)
    TARGETVOL__FIELD_NAME: WrapperField = WrapperField("TargetVol", FieldType.DOUBLE)
    TARGETWELLPOSALIQ1__FIELD_NAME: WrapperField = WrapperField("TargetWellPosAliq1", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_ExemplarSampleType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExemplarSampleType' on this record model
        """
        self.set_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name, value)

    def get_ExemplarSampleType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExemplarSampleType' from this record model
        """
        return self.get_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name)

    def set_NewControl_field(self, value: Optional[bool]):
        """
        Set data field with field name 'NewControl' on this record model
        """
        self.set_field_value(self.NEWCONTROL__FIELD_NAME.field_name, value)

    def get_NewControl_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'NewControl' from this record model
        """
        return self.get_field_value(self.NEWCONTROL__FIELD_NAME.field_name)

    def set_SourceItemId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SourceItemId' on this record model
        """
        self.set_field_value(self.SOURCEITEMID__FIELD_NAME.field_name, value)

    def get_SourceItemId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SourceItemId' from this record model
        """
        return self.get_field_value(self.SOURCEITEMID__FIELD_NAME.field_name)

    def set_SrcPlateIdAliq1_field(self, value: Optional[str]):
        """
        Set data field with field name 'SrcPlateIdAliq1' on this record model
        """
        self.set_field_value(self.SRCPLATEIDALIQ1__FIELD_NAME.field_name, value)

    def get_SrcPlateIdAliq1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SrcPlateIdAliq1' from this record model
        """
        return self.get_field_value(self.SRCPLATEIDALIQ1__FIELD_NAME.field_name)

    def set_SrcWellPosAliq1_field(self, value: Optional[str]):
        """
        Set data field with field name 'SrcWellPosAliq1' on this record model
        """
        self.set_field_value(self.SRCWELLPOSALIQ1__FIELD_NAME.field_name, value)

    def get_SrcWellPosAliq1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SrcWellPosAliq1' from this record model
        """
        return self.get_field_value(self.SRCWELLPOSALIQ1__FIELD_NAME.field_name)

    def set_TargetConcentration_field(self, value: Optional[float]):
        """
        Set data field with field name 'TargetConcentration' on this record model
        """
        self.set_field_value(self.TARGETCONCENTRATION__FIELD_NAME.field_name, value)

    def get_TargetConcentration_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TargetConcentration' from this record model
        """
        return self.get_field_value(self.TARGETCONCENTRATION__FIELD_NAME.field_name)

    def set_TargetPlateIdAliq1_field(self, value: Optional[str]):
        """
        Set data field with field name 'TargetPlateIdAliq1' on this record model
        """
        self.set_field_value(self.TARGETPLATEIDALIQ1__FIELD_NAME.field_name, value)

    def get_TargetPlateIdAliq1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TargetPlateIdAliq1' from this record model
        """
        return self.get_field_value(self.TARGETPLATEIDALIQ1__FIELD_NAME.field_name)

    def set_TargetVol_field(self, value: Optional[float]):
        """
        Set data field with field name 'TargetVol' on this record model
        """
        self.set_field_value(self.TARGETVOL__FIELD_NAME.field_name, value)

    def get_TargetVol_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TargetVol' from this record model
        """
        return self.get_field_value(self.TARGETVOL__FIELD_NAME.field_name)

    def set_TargetWellPosAliq1_field(self, value: Optional[str]):
        """
        Set data field with field name 'TargetWellPosAliq1' on this record model
        """
        self.set_field_value(self.TARGETWELLPOSALIQ1__FIELD_NAME.field_name, value)

    def get_TargetWellPosAliq1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TargetWellPosAliq1' from this record model
        """
        return self.get_field_value(self.TARGETWELLPOSALIQ1__FIELD_NAME.field_name)


class ProcessModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Process
    Data Type Display Name: Process (Processes)
    Fields: DisplayName, IsActive, ProcessDescription, ProcessName, ProcessType
    """
    DATA_TYPE_NAME: str = 'Process'
    DISPLAYNAME__FIELD_NAME: WrapperField = WrapperField("DisplayName", FieldType.STRING)
    ISACTIVE__FIELD_NAME: WrapperField = WrapperField("IsActive", FieldType.BOOLEAN)
    PROCESSDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("ProcessDescription", FieldType.STRING)
    PROCESSNAME__FIELD_NAME: WrapperField = WrapperField("ProcessName", FieldType.STRING)
    PROCESSTYPE__FIELD_NAME: WrapperField = WrapperField("ProcessType", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DisplayName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DisplayName' on this record model
        """
        self.set_field_value(self.DISPLAYNAME__FIELD_NAME.field_name, value)

    def get_DisplayName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DisplayName' from this record model
        """
        return self.get_field_value(self.DISPLAYNAME__FIELD_NAME.field_name)

    def set_IsActive_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsActive' on this record model
        """
        self.set_field_value(self.ISACTIVE__FIELD_NAME.field_name, value)

    def get_IsActive_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsActive' from this record model
        """
        return self.get_field_value(self.ISACTIVE__FIELD_NAME.field_name)

    def set_ProcessDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProcessDescription' on this record model
        """
        self.set_field_value(self.PROCESSDESCRIPTION__FIELD_NAME.field_name, value)

    def get_ProcessDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProcessDescription' from this record model
        """
        return self.get_field_value(self.PROCESSDESCRIPTION__FIELD_NAME.field_name)

    def set_ProcessName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProcessName' on this record model
        """
        self.set_field_value(self.PROCESSNAME__FIELD_NAME.field_name, value)

    def get_ProcessName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProcessName' from this record model
        """
        return self.get_field_value(self.PROCESSNAME__FIELD_NAME.field_name)

    def set_ProcessType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProcessType' on this record model
        """
        self.set_field_value(self.PROCESSTYPE__FIELD_NAME.field_name, value)

    def get_ProcessType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProcessType' from this record model
        """
        return self.get_field_value(self.PROCESSTYPE__FIELD_NAME.field_name)


class ProcessConfigDisplayModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ProcessConfigDisplay
    Data Type Display Name: Process Config Display (Process Config Displays)
    Fields: Imported, ProcessDescription, ProcessName
    """
    DATA_TYPE_NAME: str = 'ProcessConfigDisplay'
    IMPORTED__FIELD_NAME: WrapperField = WrapperField("Imported", FieldType.BOOLEAN)
    PROCESSDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("ProcessDescription", FieldType.STRING)
    PROCESSNAME__FIELD_NAME: WrapperField = WrapperField("ProcessName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Imported_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Imported' on this record model
        """
        self.set_field_value(self.IMPORTED__FIELD_NAME.field_name, value)

    def get_Imported_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Imported' from this record model
        """
        return self.get_field_value(self.IMPORTED__FIELD_NAME.field_name)

    def set_ProcessDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProcessDescription' on this record model
        """
        self.set_field_value(self.PROCESSDESCRIPTION__FIELD_NAME.field_name, value)

    def get_ProcessDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProcessDescription' from this record model
        """
        return self.get_field_value(self.PROCESSDESCRIPTION__FIELD_NAME.field_name)

    def set_ProcessName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProcessName' on this record model
        """
        self.set_field_value(self.PROCESSNAME__FIELD_NAME.field_name, value)

    def get_ProcessName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProcessName' from this record model
        """
        return self.get_field_value(self.PROCESSNAME__FIELD_NAME.field_name)


class ProcessWorkflowModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ProcessWorkflow
    Data Type Display Name: Process Workflow (Process Workflows)
    Fields: CompletionContribution, InputContainerType, InputSampleType, IsELNTemplate, IsPlatesOnly, OutputSampleType, ProcessStepNumber, ResultTypes, WorkflowDescription, WorkflowExpectedQueueTime, WorkflowExpectedTAT, WorkflowHistoricQueueTime, WorkflowHistoricTAT, WorkflowName
    """
    DATA_TYPE_NAME: str = 'ProcessWorkflow'
    COMPLETIONCONTRIBUTION__FIELD_NAME: WrapperField = WrapperField("CompletionContribution", FieldType.INTEGER)
    INPUTCONTAINERTYPE__FIELD_NAME: WrapperField = WrapperField("InputContainerType", FieldType.PICKLIST)
    INPUTSAMPLETYPE__FIELD_NAME: WrapperField = WrapperField("InputSampleType", FieldType.SELECTION)
    ISELNTEMPLATE__FIELD_NAME: WrapperField = WrapperField("IsELNTemplate", FieldType.BOOLEAN)
    ISPLATESONLY__FIELD_NAME: WrapperField = WrapperField("IsPlatesOnly", FieldType.BOOLEAN)
    OUTPUTSAMPLETYPE__FIELD_NAME: WrapperField = WrapperField("OutputSampleType", FieldType.SELECTION)
    PROCESSSTEPNUMBER__FIELD_NAME: WrapperField = WrapperField("ProcessStepNumber", FieldType.LONG)
    RESULTTYPES__FIELD_NAME: WrapperField = WrapperField("ResultTypes", FieldType.SELECTION)
    WORKFLOWDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("WorkflowDescription", FieldType.STRING)
    WORKFLOWEXPECTEDQUEUETIME__FIELD_NAME: WrapperField = WrapperField("WorkflowExpectedQueueTime", FieldType.STRING)
    WORKFLOWEXPECTEDTAT__FIELD_NAME: WrapperField = WrapperField("WorkflowExpectedTAT", FieldType.STRING)
    WORKFLOWHISTORICQUEUETIME__FIELD_NAME: WrapperField = WrapperField("WorkflowHistoricQueueTime", FieldType.STRING)
    WORKFLOWHISTORICTAT__FIELD_NAME: WrapperField = WrapperField("WorkflowHistoricTAT", FieldType.STRING)
    WORKFLOWNAME__FIELD_NAME: WrapperField = WrapperField("WorkflowName", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_CompletionContribution_field(self, value: Optional[int]):
        """
        Set data field with field name 'CompletionContribution' on this record model
        """
        self.set_field_value(self.COMPLETIONCONTRIBUTION__FIELD_NAME.field_name, value)

    def get_CompletionContribution_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CompletionContribution' from this record model
        """
        return self.get_field_value(self.COMPLETIONCONTRIBUTION__FIELD_NAME.field_name)

    def set_InputContainerType_field(self, value: Optional[str]):
        """
        Set data field with field name 'InputContainerType' on this record model
        """
        self.set_field_value(self.INPUTCONTAINERTYPE__FIELD_NAME.field_name, value)

    def get_InputContainerType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InputContainerType' from this record model
        """
        return self.get_field_value(self.INPUTCONTAINERTYPE__FIELD_NAME.field_name)

    def set_InputSampleType_field(self, value: Optional[str]):
        """
        Set data field with field name 'InputSampleType' on this record model
        """
        self.set_field_value(self.INPUTSAMPLETYPE__FIELD_NAME.field_name, value)

    def get_InputSampleType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'InputSampleType' from this record model
        """
        return self.get_field_value(self.INPUTSAMPLETYPE__FIELD_NAME.field_name)

    def set_IsELNTemplate_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsELNTemplate' on this record model
        """
        self.set_field_value(self.ISELNTEMPLATE__FIELD_NAME.field_name, value)

    def get_IsELNTemplate_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsELNTemplate' from this record model
        """
        return self.get_field_value(self.ISELNTEMPLATE__FIELD_NAME.field_name)

    def set_IsPlatesOnly_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsPlatesOnly' on this record model
        """
        self.set_field_value(self.ISPLATESONLY__FIELD_NAME.field_name, value)

    def get_IsPlatesOnly_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsPlatesOnly' from this record model
        """
        return self.get_field_value(self.ISPLATESONLY__FIELD_NAME.field_name)

    def set_OutputSampleType_field(self, value: Optional[str]):
        """
        Set data field with field name 'OutputSampleType' on this record model
        """
        self.set_field_value(self.OUTPUTSAMPLETYPE__FIELD_NAME.field_name, value)

    def get_OutputSampleType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OutputSampleType' from this record model
        """
        return self.get_field_value(self.OUTPUTSAMPLETYPE__FIELD_NAME.field_name)

    def set_ProcessStepNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'ProcessStepNumber' on this record model
        """
        self.set_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name, value)

    def get_ProcessStepNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ProcessStepNumber' from this record model
        """
        return self.get_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name)

    def set_ResultTypes_field(self, value: Optional[str]):
        """
        Set data field with field name 'ResultTypes' on this record model
        """
        self.set_field_value(self.RESULTTYPES__FIELD_NAME.field_name, value)

    def get_ResultTypes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ResultTypes' from this record model
        """
        return self.get_field_value(self.RESULTTYPES__FIELD_NAME.field_name)

    def set_WorkflowDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowDescription' on this record model
        """
        self.set_field_value(self.WORKFLOWDESCRIPTION__FIELD_NAME.field_name, value)

    def get_WorkflowDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowDescription' from this record model
        """
        return self.get_field_value(self.WORKFLOWDESCRIPTION__FIELD_NAME.field_name)

    def set_WorkflowExpectedQueueTime_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowExpectedQueueTime' on this record model
        """
        self.set_field_value(self.WORKFLOWEXPECTEDQUEUETIME__FIELD_NAME.field_name, value)

    def get_WorkflowExpectedQueueTime_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowExpectedQueueTime' from this record model
        """
        return self.get_field_value(self.WORKFLOWEXPECTEDQUEUETIME__FIELD_NAME.field_name)

    def set_WorkflowExpectedTAT_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowExpectedTAT' on this record model
        """
        self.set_field_value(self.WORKFLOWEXPECTEDTAT__FIELD_NAME.field_name, value)

    def get_WorkflowExpectedTAT_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowExpectedTAT' from this record model
        """
        return self.get_field_value(self.WORKFLOWEXPECTEDTAT__FIELD_NAME.field_name)

    def set_WorkflowHistoricQueueTime_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowHistoricQueueTime' on this record model
        """
        self.set_field_value(self.WORKFLOWHISTORICQUEUETIME__FIELD_NAME.field_name, value)

    def get_WorkflowHistoricQueueTime_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowHistoricQueueTime' from this record model
        """
        return self.get_field_value(self.WORKFLOWHISTORICQUEUETIME__FIELD_NAME.field_name)

    def set_WorkflowHistoricTAT_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowHistoricTAT' on this record model
        """
        self.set_field_value(self.WORKFLOWHISTORICTAT__FIELD_NAME.field_name, value)

    def get_WorkflowHistoricTAT_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowHistoricTAT' from this record model
        """
        return self.get_field_value(self.WORKFLOWHISTORICTAT__FIELD_NAME.field_name)

    def set_WorkflowName_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowName' on this record model
        """
        self.set_field_value(self.WORKFLOWNAME__FIELD_NAME.field_name, value)

    def get_WorkflowName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowName' from this record model
        """
        return self.get_field_value(self.WORKFLOWNAME__FIELD_NAME.field_name)


class ProcessWorkflowTrackingModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ProcessWorkflowTracking
    Data Type Display Name: Process Workflow Tracking (Process Workflow Trackings)
    Fields: ActiveWorkflowId, EndDate, EndHour, EndMinuteTime, ExpectedQueueTime, ExpectedTAT, MultiParentLink204, ProcessStepNumber, QueuedHours, QueuedMinutes, QueuedTime, QueueStartDate, QueueStartHour, QueueStartMinuteTime, SampleRecordId, StartDate, StartHour, StartMinuteTime, Status, TurnAroundHours, TurnAroundMinutes, WorkflowEndUserId, WorkflowExpectedQueueTime, WorkflowExpectedTAT, WorkflowExpectedTotalTAT, WorkflowIdNumber, WorkflowName, WorkflowProcessTAT, WorkflowStartUserId, WorkflowTAT, WorkflowVersion
    Records to track time spent on process workflows
    """
    DATA_TYPE_NAME: str = 'ProcessWorkflowTracking'
    ACTIVEWORKFLOWID__FIELD_NAME: WrapperField = WrapperField("ActiveWorkflowId", FieldType.LONG)
    ENDDATE__FIELD_NAME: WrapperField = WrapperField("EndDate", FieldType.DATE)
    ENDHOUR__FIELD_NAME: WrapperField = WrapperField("EndHour", FieldType.LONG)
    ENDMINUTETIME__FIELD_NAME: WrapperField = WrapperField("EndMinuteTime", FieldType.LONG)
    EXPECTEDQUEUETIME__FIELD_NAME: WrapperField = WrapperField("ExpectedQueueTime", FieldType.DOUBLE)
    EXPECTEDTAT__FIELD_NAME: WrapperField = WrapperField("ExpectedTAT", FieldType.DOUBLE)
    MULTIPARENTLINK204__FIELD_NAME: WrapperField = WrapperField("MultiParentLink204", FieldType.MULTIPARENTLINK)
    PROCESSSTEPNUMBER__FIELD_NAME: WrapperField = WrapperField("ProcessStepNumber", FieldType.LONG)
    QUEUEDHOURS__FIELD_NAME: WrapperField = WrapperField("QueuedHours", FieldType.LONG)
    QUEUEDMINUTES__FIELD_NAME: WrapperField = WrapperField("QueuedMinutes", FieldType.LONG)
    QUEUEDTIME__FIELD_NAME: WrapperField = WrapperField("QueuedTime", FieldType.DOUBLE)
    QUEUESTARTDATE__FIELD_NAME: WrapperField = WrapperField("QueueStartDate", FieldType.DATE)
    QUEUESTARTHOUR__FIELD_NAME: WrapperField = WrapperField("QueueStartHour", FieldType.LONG)
    QUEUESTARTMINUTETIME__FIELD_NAME: WrapperField = WrapperField("QueueStartMinuteTime", FieldType.LONG)
    SAMPLERECORDID__FIELD_NAME: WrapperField = WrapperField("SampleRecordId", FieldType.LONG)
    STARTDATE__FIELD_NAME: WrapperField = WrapperField("StartDate", FieldType.DATE)
    STARTHOUR__FIELD_NAME: WrapperField = WrapperField("StartHour", FieldType.LONG)
    STARTMINUTETIME__FIELD_NAME: WrapperField = WrapperField("StartMinuteTime", FieldType.LONG)
    STATUS__FIELD_NAME: WrapperField = WrapperField("Status", FieldType.PICKLIST)
    TURNAROUNDHOURS__FIELD_NAME: WrapperField = WrapperField("TurnAroundHours", FieldType.LONG)
    TURNAROUNDMINUTES__FIELD_NAME: WrapperField = WrapperField("TurnAroundMinutes", FieldType.LONG)
    WORKFLOWENDUSERID__FIELD_NAME: WrapperField = WrapperField("WorkflowEndUserId", FieldType.STRING)
    WORKFLOWEXPECTEDQUEUETIME__FIELD_NAME: WrapperField = WrapperField("WorkflowExpectedQueueTime", FieldType.STRING)
    WORKFLOWEXPECTEDTAT__FIELD_NAME: WrapperField = WrapperField("WorkflowExpectedTAT", FieldType.STRING)
    WORKFLOWEXPECTEDTOTALTAT__FIELD_NAME: WrapperField = WrapperField("WorkflowExpectedTotalTAT", FieldType.DOUBLE)
    WORKFLOWIDNUMBER__FIELD_NAME: WrapperField = WrapperField("WorkflowIdNumber", FieldType.LONG)
    WORKFLOWNAME__FIELD_NAME: WrapperField = WrapperField("WorkflowName", FieldType.STRING)
    WORKFLOWPROCESSTAT__FIELD_NAME: WrapperField = WrapperField("WorkflowProcessTAT", FieldType.DOUBLE)
    WORKFLOWSTARTUSERID__FIELD_NAME: WrapperField = WrapperField("WorkflowStartUserId", FieldType.STRING)
    WORKFLOWTAT__FIELD_NAME: WrapperField = WrapperField("WorkflowTAT", FieldType.DOUBLE)
    WORKFLOWVERSION__FIELD_NAME: WrapperField = WrapperField("WorkflowVersion", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActiveWorkflowId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ActiveWorkflowId' on this record model
        """
        self.set_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name, value)

    def get_ActiveWorkflowId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ActiveWorkflowId' from this record model
        """
        return self.get_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name)

    def set_EndDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'EndDate' on this record model
        """
        self.set_field_value(self.ENDDATE__FIELD_NAME.field_name, value)

    def get_EndDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'EndDate' from this record model
        """
        return self.get_field_value(self.ENDDATE__FIELD_NAME.field_name)

    def set_EndHour_field(self, value: Optional[int]):
        """
        Set data field with field name 'EndHour' on this record model
        """
        self.set_field_value(self.ENDHOUR__FIELD_NAME.field_name, value)

    def get_EndHour_field(self) -> Optional[int]:
        """
        Get data field value with field name 'EndHour' from this record model
        """
        return self.get_field_value(self.ENDHOUR__FIELD_NAME.field_name)

    def set_EndMinuteTime_field(self, value: Optional[int]):
        """
        Set data field with field name 'EndMinuteTime' on this record model
        """
        self.set_field_value(self.ENDMINUTETIME__FIELD_NAME.field_name, value)

    def get_EndMinuteTime_field(self) -> Optional[int]:
        """
        Get data field value with field name 'EndMinuteTime' from this record model
        """
        return self.get_field_value(self.ENDMINUTETIME__FIELD_NAME.field_name)

    def set_ExpectedQueueTime_field(self, value: Optional[float]):
        """
        Set data field with field name 'ExpectedQueueTime' on this record model
        """
        self.set_field_value(self.EXPECTEDQUEUETIME__FIELD_NAME.field_name, value)

    def get_ExpectedQueueTime_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ExpectedQueueTime' from this record model
        """
        return self.get_field_value(self.EXPECTEDQUEUETIME__FIELD_NAME.field_name)

    def set_ExpectedTAT_field(self, value: Optional[float]):
        """
        Set data field with field name 'ExpectedTAT' on this record model
        """
        self.set_field_value(self.EXPECTEDTAT__FIELD_NAME.field_name, value)

    def get_ExpectedTAT_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ExpectedTAT' from this record model
        """
        return self.get_field_value(self.EXPECTEDTAT__FIELD_NAME.field_name)

    def set_ProcessStepNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'ProcessStepNumber' on this record model
        """
        self.set_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name, value)

    def get_ProcessStepNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ProcessStepNumber' from this record model
        """
        return self.get_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name)

    def set_QueuedHours_field(self, value: Optional[int]):
        """
        Set data field with field name 'QueuedHours' on this record model
        """
        self.set_field_value(self.QUEUEDHOURS__FIELD_NAME.field_name, value)

    def get_QueuedHours_field(self) -> Optional[int]:
        """
        Get data field value with field name 'QueuedHours' from this record model
        """
        return self.get_field_value(self.QUEUEDHOURS__FIELD_NAME.field_name)

    def set_QueuedMinutes_field(self, value: Optional[int]):
        """
        Set data field with field name 'QueuedMinutes' on this record model
        """
        self.set_field_value(self.QUEUEDMINUTES__FIELD_NAME.field_name, value)

    def get_QueuedMinutes_field(self) -> Optional[int]:
        """
        Get data field value with field name 'QueuedMinutes' from this record model
        """
        return self.get_field_value(self.QUEUEDMINUTES__FIELD_NAME.field_name)

    def set_QueuedTime_field(self, value: Optional[float]):
        """
        Set data field with field name 'QueuedTime' on this record model
        """
        self.set_field_value(self.QUEUEDTIME__FIELD_NAME.field_name, value)

    def get_QueuedTime_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QueuedTime' from this record model
        """
        return self.get_field_value(self.QUEUEDTIME__FIELD_NAME.field_name)

    def set_QueueStartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'QueueStartDate' on this record model
        """
        self.set_field_value(self.QUEUESTARTDATE__FIELD_NAME.field_name, value)

    def get_QueueStartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'QueueStartDate' from this record model
        """
        return self.get_field_value(self.QUEUESTARTDATE__FIELD_NAME.field_name)

    def set_QueueStartHour_field(self, value: Optional[int]):
        """
        Set data field with field name 'QueueStartHour' on this record model
        """
        self.set_field_value(self.QUEUESTARTHOUR__FIELD_NAME.field_name, value)

    def get_QueueStartHour_field(self) -> Optional[int]:
        """
        Get data field value with field name 'QueueStartHour' from this record model
        """
        return self.get_field_value(self.QUEUESTARTHOUR__FIELD_NAME.field_name)

    def set_QueueStartMinuteTime_field(self, value: Optional[int]):
        """
        Set data field with field name 'QueueStartMinuteTime' on this record model
        """
        self.set_field_value(self.QUEUESTARTMINUTETIME__FIELD_NAME.field_name, value)

    def get_QueueStartMinuteTime_field(self) -> Optional[int]:
        """
        Get data field value with field name 'QueueStartMinuteTime' from this record model
        """
        return self.get_field_value(self.QUEUESTARTMINUTETIME__FIELD_NAME.field_name)

    def set_SampleRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'SampleRecordId' on this record model
        """
        self.set_field_value(self.SAMPLERECORDID__FIELD_NAME.field_name, value)

    def get_SampleRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SampleRecordId' from this record model
        """
        return self.get_field_value(self.SAMPLERECORDID__FIELD_NAME.field_name)

    def set_StartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'StartDate' on this record model
        """
        self.set_field_value(self.STARTDATE__FIELD_NAME.field_name, value)

    def get_StartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StartDate' from this record model
        """
        return self.get_field_value(self.STARTDATE__FIELD_NAME.field_name)

    def set_StartHour_field(self, value: Optional[int]):
        """
        Set data field with field name 'StartHour' on this record model
        """
        self.set_field_value(self.STARTHOUR__FIELD_NAME.field_name, value)

    def get_StartHour_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StartHour' from this record model
        """
        return self.get_field_value(self.STARTHOUR__FIELD_NAME.field_name)

    def set_StartMinuteTime_field(self, value: Optional[int]):
        """
        Set data field with field name 'StartMinuteTime' on this record model
        """
        self.set_field_value(self.STARTMINUTETIME__FIELD_NAME.field_name, value)

    def get_StartMinuteTime_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StartMinuteTime' from this record model
        """
        return self.get_field_value(self.STARTMINUTETIME__FIELD_NAME.field_name)

    def set_Status_field(self, value: Optional[str]):
        """
        Set data field with field name 'Status' on this record model
        """
        self.set_field_value(self.STATUS__FIELD_NAME.field_name, value)

    def get_Status_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Status' from this record model
        """
        return self.get_field_value(self.STATUS__FIELD_NAME.field_name)

    def set_TurnAroundHours_field(self, value: Optional[int]):
        """
        Set data field with field name 'TurnAroundHours' on this record model
        """
        self.set_field_value(self.TURNAROUNDHOURS__FIELD_NAME.field_name, value)

    def get_TurnAroundHours_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TurnAroundHours' from this record model
        """
        return self.get_field_value(self.TURNAROUNDHOURS__FIELD_NAME.field_name)

    def set_TurnAroundMinutes_field(self, value: Optional[int]):
        """
        Set data field with field name 'TurnAroundMinutes' on this record model
        """
        self.set_field_value(self.TURNAROUNDMINUTES__FIELD_NAME.field_name, value)

    def get_TurnAroundMinutes_field(self) -> Optional[int]:
        """
        Get data field value with field name 'TurnAroundMinutes' from this record model
        """
        return self.get_field_value(self.TURNAROUNDMINUTES__FIELD_NAME.field_name)

    def set_WorkflowEndUserId_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowEndUserId' on this record model
        """
        self.set_field_value(self.WORKFLOWENDUSERID__FIELD_NAME.field_name, value)

    def get_WorkflowEndUserId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowEndUserId' from this record model
        """
        return self.get_field_value(self.WORKFLOWENDUSERID__FIELD_NAME.field_name)

    def set_WorkflowExpectedQueueTime_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowExpectedQueueTime' on this record model
        """
        self.set_field_value(self.WORKFLOWEXPECTEDQUEUETIME__FIELD_NAME.field_name, value)

    def get_WorkflowExpectedQueueTime_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowExpectedQueueTime' from this record model
        """
        return self.get_field_value(self.WORKFLOWEXPECTEDQUEUETIME__FIELD_NAME.field_name)

    def set_WorkflowExpectedTAT_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowExpectedTAT' on this record model
        """
        self.set_field_value(self.WORKFLOWEXPECTEDTAT__FIELD_NAME.field_name, value)

    def get_WorkflowExpectedTAT_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowExpectedTAT' from this record model
        """
        return self.get_field_value(self.WORKFLOWEXPECTEDTAT__FIELD_NAME.field_name)

    def set_WorkflowExpectedTotalTAT_field(self, value: Optional[float]):
        """
        Set data field with field name 'WorkflowExpectedTotalTAT' on this record model
        """
        self.set_field_value(self.WORKFLOWEXPECTEDTOTALTAT__FIELD_NAME.field_name, value)

    def get_WorkflowExpectedTotalTAT_field(self) -> Optional[float]:
        """
        Get data field value with field name 'WorkflowExpectedTotalTAT' from this record model
        """
        return self.get_field_value(self.WORKFLOWEXPECTEDTOTALTAT__FIELD_NAME.field_name)

    def set_WorkflowIdNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'WorkflowIdNumber' on this record model
        """
        self.set_field_value(self.WORKFLOWIDNUMBER__FIELD_NAME.field_name, value)

    def get_WorkflowIdNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'WorkflowIdNumber' from this record model
        """
        return self.get_field_value(self.WORKFLOWIDNUMBER__FIELD_NAME.field_name)

    def set_WorkflowName_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowName' on this record model
        """
        self.set_field_value(self.WORKFLOWNAME__FIELD_NAME.field_name, value)

    def get_WorkflowName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowName' from this record model
        """
        return self.get_field_value(self.WORKFLOWNAME__FIELD_NAME.field_name)

    def set_WorkflowProcessTAT_field(self, value: Optional[float]):
        """
        Set data field with field name 'WorkflowProcessTAT' on this record model
        """
        self.set_field_value(self.WORKFLOWPROCESSTAT__FIELD_NAME.field_name, value)

    def get_WorkflowProcessTAT_field(self) -> Optional[float]:
        """
        Get data field value with field name 'WorkflowProcessTAT' from this record model
        """
        return self.get_field_value(self.WORKFLOWPROCESSTAT__FIELD_NAME.field_name)

    def set_WorkflowStartUserId_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowStartUserId' on this record model
        """
        self.set_field_value(self.WORKFLOWSTARTUSERID__FIELD_NAME.field_name, value)

    def get_WorkflowStartUserId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowStartUserId' from this record model
        """
        return self.get_field_value(self.WORKFLOWSTARTUSERID__FIELD_NAME.field_name)

    def set_WorkflowTAT_field(self, value: Optional[float]):
        """
        Set data field with field name 'WorkflowTAT' on this record model
        """
        self.set_field_value(self.WORKFLOWTAT__FIELD_NAME.field_name, value)

    def get_WorkflowTAT_field(self) -> Optional[float]:
        """
        Get data field value with field name 'WorkflowTAT' from this record model
        """
        return self.get_field_value(self.WORKFLOWTAT__FIELD_NAME.field_name)

    def set_WorkflowVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'WorkflowVersion' on this record model
        """
        self.set_field_value(self.WORKFLOWVERSION__FIELD_NAME.field_name, value)

    def get_WorkflowVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'WorkflowVersion' from this record model
        """
        return self.get_field_value(self.WORKFLOWVERSION__FIELD_NAME.field_name)


class ProjectModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Project
    Data Type Display Name: Project (Projects)
    Fields: EndDate, InheritRolesFromParent, Leader, ProjectDesc, ProjectId, ProjectName, StartDate, VeloxApprover
    """
    DATA_TYPE_NAME: str = 'Project'
    ENDDATE__FIELD_NAME: WrapperField = WrapperField("EndDate", FieldType.DATE)
    INHERITROLESFROMPARENT__FIELD_NAME: WrapperField = WrapperField("InheritRolesFromParent", FieldType.BOOLEAN)
    LEADER__FIELD_NAME: WrapperField = WrapperField("Leader", FieldType.SELECTION)
    PROJECTDESC__FIELD_NAME: WrapperField = WrapperField("ProjectDesc", FieldType.STRING)
    PROJECTID__FIELD_NAME: WrapperField = WrapperField("ProjectId", FieldType.STRING)
    PROJECTNAME__FIELD_NAME: WrapperField = WrapperField("ProjectName", FieldType.STRING)
    STARTDATE__FIELD_NAME: WrapperField = WrapperField("StartDate", FieldType.DATE)
    VELOXAPPROVER__FIELD_NAME: WrapperField = WrapperField("VeloxApprover", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_EndDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'EndDate' on this record model
        """
        self.set_field_value(self.ENDDATE__FIELD_NAME.field_name, value)

    def get_EndDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'EndDate' from this record model
        """
        return self.get_field_value(self.ENDDATE__FIELD_NAME.field_name)

    def set_InheritRolesFromParent_field(self, value: Optional[bool]):
        """
        Set data field with field name 'InheritRolesFromParent' on this record model
        """
        self.set_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name, value)

    def get_InheritRolesFromParent_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'InheritRolesFromParent' from this record model
        """
        return self.get_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name)

    def set_Leader_field(self, value: Optional[str]):
        """
        Set data field with field name 'Leader' on this record model
        """
        self.set_field_value(self.LEADER__FIELD_NAME.field_name, value)

    def get_Leader_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Leader' from this record model
        """
        return self.get_field_value(self.LEADER__FIELD_NAME.field_name)

    def set_ProjectDesc_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProjectDesc' on this record model
        """
        self.set_field_value(self.PROJECTDESC__FIELD_NAME.field_name, value)

    def get_ProjectDesc_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProjectDesc' from this record model
        """
        return self.get_field_value(self.PROJECTDESC__FIELD_NAME.field_name)

    def set_ProjectId_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProjectId' on this record model
        """
        self.set_field_value(self.PROJECTID__FIELD_NAME.field_name, value)

    def get_ProjectId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProjectId' from this record model
        """
        return self.get_field_value(self.PROJECTID__FIELD_NAME.field_name)

    def set_ProjectName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProjectName' on this record model
        """
        self.set_field_value(self.PROJECTNAME__FIELD_NAME.field_name, value)

    def get_ProjectName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProjectName' from this record model
        """
        return self.get_field_value(self.PROJECTNAME__FIELD_NAME.field_name)

    def set_StartDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'StartDate' on this record model
        """
        self.set_field_value(self.STARTDATE__FIELD_NAME.field_name, value)

    def get_StartDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StartDate' from this record model
        """
        return self.get_field_value(self.STARTDATE__FIELD_NAME.field_name)

    def set_VeloxApprover_field(self, value: Optional[str]):
        """
        Set data field with field name 'VeloxApprover' on this record model
        """
        self.set_field_value(self.VELOXAPPROVER__FIELD_NAME.field_name, value)

    def get_VeloxApprover_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VeloxApprover' from this record model
        """
        return self.get_field_value(self.VELOXAPPROVER__FIELD_NAME.field_name)


class ProteinModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Protein
    Data Type Display Name: Protein (Proteins)
    Fields: Barcode, ExpirationDate, Expired, LotNumber, PartNumber, StructureName
    """
    DATA_TYPE_NAME: str = 'Protein'
    BARCODE__FIELD_NAME: WrapperField = WrapperField("Barcode", FieldType.AUTO_ACCESSION)
    EXPIRATIONDATE__FIELD_NAME: WrapperField = WrapperField("ExpirationDate", FieldType.DATE)
    EXPIRED__FIELD_NAME: WrapperField = WrapperField("Expired", FieldType.BOOLEAN)
    LOTNUMBER__FIELD_NAME: WrapperField = WrapperField("LotNumber", FieldType.STRING)
    PARTNUMBER__FIELD_NAME: WrapperField = WrapperField("PartNumber", FieldType.STRING)
    STRUCTURENAME__FIELD_NAME: WrapperField = WrapperField("StructureName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Barcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'Barcode' on this record model
        """
        self.set_field_value(self.BARCODE__FIELD_NAME.field_name, value)

    def get_Barcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Barcode' from this record model
        """
        return self.get_field_value(self.BARCODE__FIELD_NAME.field_name)

    def set_ExpirationDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ExpirationDate' on this record model
        """
        self.set_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name, value)

    def get_ExpirationDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ExpirationDate' from this record model
        """
        return self.get_field_value(self.EXPIRATIONDATE__FIELD_NAME.field_name)

    def set_Expired_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Expired' on this record model
        """
        self.set_field_value(self.EXPIRED__FIELD_NAME.field_name, value)

    def get_Expired_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Expired' from this record model
        """
        return self.get_field_value(self.EXPIRED__FIELD_NAME.field_name)

    def set_LotNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'LotNumber' on this record model
        """
        self.set_field_value(self.LOTNUMBER__FIELD_NAME.field_name, value)

    def get_LotNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LotNumber' from this record model
        """
        return self.get_field_value(self.LOTNUMBER__FIELD_NAME.field_name)

    def set_PartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PartNumber' on this record model
        """
        self.set_field_value(self.PARTNUMBER__FIELD_NAME.field_name, value)

    def get_PartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PartNumber' from this record model
        """
        return self.get_field_value(self.PARTNUMBER__FIELD_NAME.field_name)

    def set_StructureName_field(self, value: Optional[str]):
        """
        Set data field with field name 'StructureName' on this record model
        """
        self.set_field_value(self.STRUCTURENAME__FIELD_NAME.field_name, value)

    def get_StructureName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StructureName' from this record model
        """
        return self.get_field_value(self.STRUCTURENAME__FIELD_NAME.field_name)


class ProteinPartModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ProteinPart
    Data Type Display Name: Protein Part (Protein Parts)
    Fields: Descriptor, FilePath, IsStructureEstimated, Keywords, MolecularWeight, NumChains, PartNumber, PDBId, ProteinSequence, QuantityOnHand, QuantityPerItem, ReorderLevelQuantity, StructureName, Units, VeloxCurrentVersion
    """
    DATA_TYPE_NAME: str = 'ProteinPart'
    DESCRIPTOR__FIELD_NAME: WrapperField = WrapperField("Descriptor", FieldType.STRING)
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    ISSTRUCTUREESTIMATED__FIELD_NAME: WrapperField = WrapperField("IsStructureEstimated", FieldType.BOOLEAN)
    KEYWORDS__FIELD_NAME: WrapperField = WrapperField("Keywords", FieldType.STRING)
    MOLECULARWEIGHT__FIELD_NAME: WrapperField = WrapperField("MolecularWeight", FieldType.DOUBLE)
    NUMCHAINS__FIELD_NAME: WrapperField = WrapperField("NumChains", FieldType.INTEGER)
    PARTNUMBER__FIELD_NAME: WrapperField = WrapperField("PartNumber", FieldType.STRING)
    PDBID__FIELD_NAME: WrapperField = WrapperField("PDBId", FieldType.STRING)
    PROTEINSEQUENCE__FIELD_NAME: WrapperField = WrapperField("ProteinSequence", FieldType.STRING)
    QUANTITYONHAND__FIELD_NAME: WrapperField = WrapperField("QuantityOnHand", FieldType.DOUBLE)
    QUANTITYPERITEM__FIELD_NAME: WrapperField = WrapperField("QuantityPerItem", FieldType.DOUBLE)
    REORDERLEVELQUANTITY__FIELD_NAME: WrapperField = WrapperField("ReorderLevelQuantity", FieldType.DOUBLE)
    STRUCTURENAME__FIELD_NAME: WrapperField = WrapperField("StructureName", FieldType.STRING)
    UNITS__FIELD_NAME: WrapperField = WrapperField("Units", FieldType.PICKLIST)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Descriptor_field(self, value: Optional[str]):
        """
        Set data field with field name 'Descriptor' on this record model
        """
        self.set_field_value(self.DESCRIPTOR__FIELD_NAME.field_name, value)

    def get_Descriptor_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Descriptor' from this record model
        """
        return self.get_field_value(self.DESCRIPTOR__FIELD_NAME.field_name)

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_IsStructureEstimated_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsStructureEstimated' on this record model
        """
        self.set_field_value(self.ISSTRUCTUREESTIMATED__FIELD_NAME.field_name, value)

    def get_IsStructureEstimated_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsStructureEstimated' from this record model
        """
        return self.get_field_value(self.ISSTRUCTUREESTIMATED__FIELD_NAME.field_name)

    def set_Keywords_field(self, value: Optional[str]):
        """
        Set data field with field name 'Keywords' on this record model
        """
        self.set_field_value(self.KEYWORDS__FIELD_NAME.field_name, value)

    def get_Keywords_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Keywords' from this record model
        """
        return self.get_field_value(self.KEYWORDS__FIELD_NAME.field_name)

    def set_MolecularWeight_field(self, value: Optional[float]):
        """
        Set data field with field name 'MolecularWeight' on this record model
        """
        self.set_field_value(self.MOLECULARWEIGHT__FIELD_NAME.field_name, value)

    def get_MolecularWeight_field(self) -> Optional[float]:
        """
        Get data field value with field name 'MolecularWeight' from this record model
        """
        return self.get_field_value(self.MOLECULARWEIGHT__FIELD_NAME.field_name)

    def set_NumChains_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumChains' on this record model
        """
        self.set_field_value(self.NUMCHAINS__FIELD_NAME.field_name, value)

    def get_NumChains_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumChains' from this record model
        """
        return self.get_field_value(self.NUMCHAINS__FIELD_NAME.field_name)

    def set_PartNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'PartNumber' on this record model
        """
        self.set_field_value(self.PARTNUMBER__FIELD_NAME.field_name, value)

    def get_PartNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PartNumber' from this record model
        """
        return self.get_field_value(self.PARTNUMBER__FIELD_NAME.field_name)

    def set_PDBId_field(self, value: Optional[str]):
        """
        Set data field with field name 'PDBId' on this record model
        """
        self.set_field_value(self.PDBID__FIELD_NAME.field_name, value)

    def get_PDBId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PDBId' from this record model
        """
        return self.get_field_value(self.PDBID__FIELD_NAME.field_name)

    def set_ProteinSequence_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProteinSequence' on this record model
        """
        self.set_field_value(self.PROTEINSEQUENCE__FIELD_NAME.field_name, value)

    def get_ProteinSequence_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProteinSequence' from this record model
        """
        return self.get_field_value(self.PROTEINSEQUENCE__FIELD_NAME.field_name)

    def set_QuantityOnHand_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityOnHand' on this record model
        """
        self.set_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name, value)

    def get_QuantityOnHand_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityOnHand' from this record model
        """
        return self.get_field_value(self.QUANTITYONHAND__FIELD_NAME.field_name)

    def set_QuantityPerItem_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityPerItem' on this record model
        """
        self.set_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name, value)

    def get_QuantityPerItem_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityPerItem' from this record model
        """
        return self.get_field_value(self.QUANTITYPERITEM__FIELD_NAME.field_name)

    def set_ReorderLevelQuantity_field(self, value: Optional[float]):
        """
        Set data field with field name 'ReorderLevelQuantity' on this record model
        """
        self.set_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name, value)

    def get_ReorderLevelQuantity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ReorderLevelQuantity' from this record model
        """
        return self.get_field_value(self.REORDERLEVELQUANTITY__FIELD_NAME.field_name)

    def set_StructureName_field(self, value: Optional[str]):
        """
        Set data field with field name 'StructureName' on this record model
        """
        self.set_field_value(self.STRUCTURENAME__FIELD_NAME.field_name, value)

    def get_StructureName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StructureName' from this record model
        """
        return self.get_field_value(self.STRUCTURENAME__FIELD_NAME.field_name)

    def set_Units_field(self, value: Optional[str]):
        """
        Set data field with field name 'Units' on this record model
        """
        self.set_field_value(self.UNITS__FIELD_NAME.field_name, value)

    def get_Units_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Units' from this record model
        """
        return self.get_field_value(self.UNITS__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class QCConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type QCConfig
    Data Type Display Name: Workflow Specific QC Config (Workflow Specific QC Configs)
    Fields: A260MAX, A260MIN, A280MAX, A280MIN, A260230MAX, A260230MIN, A260280MAX, A260280MIN, AreaMAX, AreaMIN, AvgSizeMAX, AvgSizeMIN, CalculatedConcentrationMAX, CalculatedConcentrationMIN, CalculatedMolarityMAX, CalculatedMolarityMIN, ConcentrationMAX, ConcentrationMIN, CtMAX, CtMeanMAX, CtMeanMIN, CtMIN, CtSDMAX, CtSDMIN, DatumType, DilutionFactorMAX, DilutionFactorMIN, FailedReprocess, MapToConcentration, MapToConcentrationUnits, MolarityMAX, MolarityMIN, MultiParentLink199, PeakValueMAX, PeakValueMIN, PreferredExperiment, QCConfigId, QuantityMAX, QuantityMeanMAX, QuantityMeanMIN, QuantityMIN, QuantitySDMAX, QuantitySDMIN, RequiredResultsPerSample, RequiresConcentration, RequiresQC, RINMAX, RINMIN
    """
    DATA_TYPE_NAME: str = 'QCConfig'
    A260MAX__FIELD_NAME: WrapperField = WrapperField("A260MAX", FieldType.DOUBLE)
    A260MIN__FIELD_NAME: WrapperField = WrapperField("A260MIN", FieldType.DOUBLE)
    A280MAX__FIELD_NAME: WrapperField = WrapperField("A280MAX", FieldType.DOUBLE)
    A280MIN__FIELD_NAME: WrapperField = WrapperField("A280MIN", FieldType.DOUBLE)
    A260230MAX__FIELD_NAME: WrapperField = WrapperField("A260230MAX", FieldType.DOUBLE)
    A260230MIN__FIELD_NAME: WrapperField = WrapperField("A260230MIN", FieldType.DOUBLE)
    A260280MAX__FIELD_NAME: WrapperField = WrapperField("A260280MAX", FieldType.DOUBLE)
    A260280MIN__FIELD_NAME: WrapperField = WrapperField("A260280MIN", FieldType.DOUBLE)
    AREAMAX__FIELD_NAME: WrapperField = WrapperField("AreaMAX", FieldType.DOUBLE)
    AREAMIN__FIELD_NAME: WrapperField = WrapperField("AreaMIN", FieldType.DOUBLE)
    AVGSIZEMAX__FIELD_NAME: WrapperField = WrapperField("AvgSizeMAX", FieldType.DOUBLE)
    AVGSIZEMIN__FIELD_NAME: WrapperField = WrapperField("AvgSizeMIN", FieldType.DOUBLE)
    CALCULATEDCONCENTRATIONMAX__FIELD_NAME: WrapperField = WrapperField("CalculatedConcentrationMAX", FieldType.DOUBLE)
    CALCULATEDCONCENTRATIONMIN__FIELD_NAME: WrapperField = WrapperField("CalculatedConcentrationMIN", FieldType.DOUBLE)
    CALCULATEDMOLARITYMAX__FIELD_NAME: WrapperField = WrapperField("CalculatedMolarityMAX", FieldType.DOUBLE)
    CALCULATEDMOLARITYMIN__FIELD_NAME: WrapperField = WrapperField("CalculatedMolarityMIN", FieldType.DOUBLE)
    CONCENTRATIONMAX__FIELD_NAME: WrapperField = WrapperField("ConcentrationMAX", FieldType.DOUBLE)
    CONCENTRATIONMIN__FIELD_NAME: WrapperField = WrapperField("ConcentrationMIN", FieldType.DOUBLE)
    CTMAX__FIELD_NAME: WrapperField = WrapperField("CtMAX", FieldType.DOUBLE)
    CTMEANMAX__FIELD_NAME: WrapperField = WrapperField("CtMeanMAX", FieldType.DOUBLE)
    CTMEANMIN__FIELD_NAME: WrapperField = WrapperField("CtMeanMIN", FieldType.DOUBLE)
    CTMIN__FIELD_NAME: WrapperField = WrapperField("CtMIN", FieldType.DOUBLE)
    CTSDMAX__FIELD_NAME: WrapperField = WrapperField("CtSDMAX", FieldType.DOUBLE)
    CTSDMIN__FIELD_NAME: WrapperField = WrapperField("CtSDMIN", FieldType.DOUBLE)
    DATUMTYPE__FIELD_NAME: WrapperField = WrapperField("DatumType", FieldType.SELECTION)
    DILUTIONFACTORMAX__FIELD_NAME: WrapperField = WrapperField("DilutionFactorMAX", FieldType.DOUBLE)
    DILUTIONFACTORMIN__FIELD_NAME: WrapperField = WrapperField("DilutionFactorMIN", FieldType.DOUBLE)
    FAILEDREPROCESS__FIELD_NAME: WrapperField = WrapperField("FailedReprocess", FieldType.BOOLEAN)
    MAPTOCONCENTRATION__FIELD_NAME: WrapperField = WrapperField("MapToConcentration", FieldType.SELECTION)
    MAPTOCONCENTRATIONUNITS__FIELD_NAME: WrapperField = WrapperField("MapToConcentrationUnits", FieldType.SELECTION)
    MOLARITYMAX__FIELD_NAME: WrapperField = WrapperField("MolarityMAX", FieldType.DOUBLE)
    MOLARITYMIN__FIELD_NAME: WrapperField = WrapperField("MolarityMIN", FieldType.DOUBLE)
    MULTIPARENTLINK199__FIELD_NAME: WrapperField = WrapperField("MultiParentLink199", FieldType.MULTIPARENTLINK)
    PEAKVALUEMAX__FIELD_NAME: WrapperField = WrapperField("PeakValueMAX", FieldType.DOUBLE)
    PEAKVALUEMIN__FIELD_NAME: WrapperField = WrapperField("PeakValueMIN", FieldType.DOUBLE)
    PREFERREDEXPERIMENT__FIELD_NAME: WrapperField = WrapperField("PreferredExperiment", FieldType.BOOLEAN)
    QCCONFIGID__FIELD_NAME: WrapperField = WrapperField("QCConfigId", FieldType.STRING)
    QUANTITYMAX__FIELD_NAME: WrapperField = WrapperField("QuantityMAX", FieldType.DOUBLE)
    QUANTITYMEANMAX__FIELD_NAME: WrapperField = WrapperField("QuantityMeanMAX", FieldType.DOUBLE)
    QUANTITYMEANMIN__FIELD_NAME: WrapperField = WrapperField("QuantityMeanMIN", FieldType.DOUBLE)
    QUANTITYMIN__FIELD_NAME: WrapperField = WrapperField("QuantityMIN", FieldType.DOUBLE)
    QUANTITYSDMAX__FIELD_NAME: WrapperField = WrapperField("QuantitySDMAX", FieldType.DOUBLE)
    QUANTITYSDMIN__FIELD_NAME: WrapperField = WrapperField("QuantitySDMIN", FieldType.DOUBLE)
    REQUIREDRESULTSPERSAMPLE__FIELD_NAME: WrapperField = WrapperField("RequiredResultsPerSample", FieldType.INTEGER)
    REQUIRESCONCENTRATION__FIELD_NAME: WrapperField = WrapperField("RequiresConcentration", FieldType.BOOLEAN)
    REQUIRESQC__FIELD_NAME: WrapperField = WrapperField("RequiresQC", FieldType.BOOLEAN)
    RINMAX__FIELD_NAME: WrapperField = WrapperField("RINMAX", FieldType.DOUBLE)
    RINMIN__FIELD_NAME: WrapperField = WrapperField("RINMIN", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_A260MAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'A260MAX' on this record model
        """
        self.set_field_value(self.A260MAX__FIELD_NAME.field_name, value)

    def get_A260MAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A260MAX' from this record model
        """
        return self.get_field_value(self.A260MAX__FIELD_NAME.field_name)

    def set_A260MIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'A260MIN' on this record model
        """
        self.set_field_value(self.A260MIN__FIELD_NAME.field_name, value)

    def get_A260MIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A260MIN' from this record model
        """
        return self.get_field_value(self.A260MIN__FIELD_NAME.field_name)

    def set_A280MAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'A280MAX' on this record model
        """
        self.set_field_value(self.A280MAX__FIELD_NAME.field_name, value)

    def get_A280MAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A280MAX' from this record model
        """
        return self.get_field_value(self.A280MAX__FIELD_NAME.field_name)

    def set_A280MIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'A280MIN' on this record model
        """
        self.set_field_value(self.A280MIN__FIELD_NAME.field_name, value)

    def get_A280MIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A280MIN' from this record model
        """
        return self.get_field_value(self.A280MIN__FIELD_NAME.field_name)

    def set_A260230MAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'A260230MAX' on this record model
        """
        self.set_field_value(self.A260230MAX__FIELD_NAME.field_name, value)

    def get_A260230MAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A260230MAX' from this record model
        """
        return self.get_field_value(self.A260230MAX__FIELD_NAME.field_name)

    def set_A260230MIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'A260230MIN' on this record model
        """
        self.set_field_value(self.A260230MIN__FIELD_NAME.field_name, value)

    def get_A260230MIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A260230MIN' from this record model
        """
        return self.get_field_value(self.A260230MIN__FIELD_NAME.field_name)

    def set_A260280MAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'A260280MAX' on this record model
        """
        self.set_field_value(self.A260280MAX__FIELD_NAME.field_name, value)

    def get_A260280MAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A260280MAX' from this record model
        """
        return self.get_field_value(self.A260280MAX__FIELD_NAME.field_name)

    def set_A260280MIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'A260280MIN' on this record model
        """
        self.set_field_value(self.A260280MIN__FIELD_NAME.field_name, value)

    def get_A260280MIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'A260280MIN' from this record model
        """
        return self.get_field_value(self.A260280MIN__FIELD_NAME.field_name)

    def set_AreaMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'AreaMAX' on this record model
        """
        self.set_field_value(self.AREAMAX__FIELD_NAME.field_name, value)

    def get_AreaMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AreaMAX' from this record model
        """
        return self.get_field_value(self.AREAMAX__FIELD_NAME.field_name)

    def set_AreaMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'AreaMIN' on this record model
        """
        self.set_field_value(self.AREAMIN__FIELD_NAME.field_name, value)

    def get_AreaMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AreaMIN' from this record model
        """
        return self.get_field_value(self.AREAMIN__FIELD_NAME.field_name)

    def set_AvgSizeMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'AvgSizeMAX' on this record model
        """
        self.set_field_value(self.AVGSIZEMAX__FIELD_NAME.field_name, value)

    def get_AvgSizeMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AvgSizeMAX' from this record model
        """
        return self.get_field_value(self.AVGSIZEMAX__FIELD_NAME.field_name)

    def set_AvgSizeMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'AvgSizeMIN' on this record model
        """
        self.set_field_value(self.AVGSIZEMIN__FIELD_NAME.field_name, value)

    def get_AvgSizeMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'AvgSizeMIN' from this record model
        """
        return self.get_field_value(self.AVGSIZEMIN__FIELD_NAME.field_name)

    def set_CalculatedConcentrationMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'CalculatedConcentrationMAX' on this record model
        """
        self.set_field_value(self.CALCULATEDCONCENTRATIONMAX__FIELD_NAME.field_name, value)

    def get_CalculatedConcentrationMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CalculatedConcentrationMAX' from this record model
        """
        return self.get_field_value(self.CALCULATEDCONCENTRATIONMAX__FIELD_NAME.field_name)

    def set_CalculatedConcentrationMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'CalculatedConcentrationMIN' on this record model
        """
        self.set_field_value(self.CALCULATEDCONCENTRATIONMIN__FIELD_NAME.field_name, value)

    def get_CalculatedConcentrationMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CalculatedConcentrationMIN' from this record model
        """
        return self.get_field_value(self.CALCULATEDCONCENTRATIONMIN__FIELD_NAME.field_name)

    def set_CalculatedMolarityMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'CalculatedMolarityMAX' on this record model
        """
        self.set_field_value(self.CALCULATEDMOLARITYMAX__FIELD_NAME.field_name, value)

    def get_CalculatedMolarityMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CalculatedMolarityMAX' from this record model
        """
        return self.get_field_value(self.CALCULATEDMOLARITYMAX__FIELD_NAME.field_name)

    def set_CalculatedMolarityMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'CalculatedMolarityMIN' on this record model
        """
        self.set_field_value(self.CALCULATEDMOLARITYMIN__FIELD_NAME.field_name, value)

    def get_CalculatedMolarityMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CalculatedMolarityMIN' from this record model
        """
        return self.get_field_value(self.CALCULATEDMOLARITYMIN__FIELD_NAME.field_name)

    def set_ConcentrationMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'ConcentrationMAX' on this record model
        """
        self.set_field_value(self.CONCENTRATIONMAX__FIELD_NAME.field_name, value)

    def get_ConcentrationMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ConcentrationMAX' from this record model
        """
        return self.get_field_value(self.CONCENTRATIONMAX__FIELD_NAME.field_name)

    def set_ConcentrationMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'ConcentrationMIN' on this record model
        """
        self.set_field_value(self.CONCENTRATIONMIN__FIELD_NAME.field_name, value)

    def get_ConcentrationMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ConcentrationMIN' from this record model
        """
        return self.get_field_value(self.CONCENTRATIONMIN__FIELD_NAME.field_name)

    def set_CtMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'CtMAX' on this record model
        """
        self.set_field_value(self.CTMAX__FIELD_NAME.field_name, value)

    def get_CtMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CtMAX' from this record model
        """
        return self.get_field_value(self.CTMAX__FIELD_NAME.field_name)

    def set_CtMeanMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'CtMeanMAX' on this record model
        """
        self.set_field_value(self.CTMEANMAX__FIELD_NAME.field_name, value)

    def get_CtMeanMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CtMeanMAX' from this record model
        """
        return self.get_field_value(self.CTMEANMAX__FIELD_NAME.field_name)

    def set_CtMeanMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'CtMeanMIN' on this record model
        """
        self.set_field_value(self.CTMEANMIN__FIELD_NAME.field_name, value)

    def get_CtMeanMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CtMeanMIN' from this record model
        """
        return self.get_field_value(self.CTMEANMIN__FIELD_NAME.field_name)

    def set_CtMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'CtMIN' on this record model
        """
        self.set_field_value(self.CTMIN__FIELD_NAME.field_name, value)

    def get_CtMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CtMIN' from this record model
        """
        return self.get_field_value(self.CTMIN__FIELD_NAME.field_name)

    def set_CtSDMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'CtSDMAX' on this record model
        """
        self.set_field_value(self.CTSDMAX__FIELD_NAME.field_name, value)

    def get_CtSDMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CtSDMAX' from this record model
        """
        return self.get_field_value(self.CTSDMAX__FIELD_NAME.field_name)

    def set_CtSDMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'CtSDMIN' on this record model
        """
        self.set_field_value(self.CTSDMIN__FIELD_NAME.field_name, value)

    def get_CtSDMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'CtSDMIN' from this record model
        """
        return self.get_field_value(self.CTSDMIN__FIELD_NAME.field_name)

    def set_DatumType_field(self, value: Optional[str]):
        """
        Set data field with field name 'DatumType' on this record model
        """
        self.set_field_value(self.DATUMTYPE__FIELD_NAME.field_name, value)

    def get_DatumType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DatumType' from this record model
        """
        return self.get_field_value(self.DATUMTYPE__FIELD_NAME.field_name)

    def set_DilutionFactorMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'DilutionFactorMAX' on this record model
        """
        self.set_field_value(self.DILUTIONFACTORMAX__FIELD_NAME.field_name, value)

    def get_DilutionFactorMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'DilutionFactorMAX' from this record model
        """
        return self.get_field_value(self.DILUTIONFACTORMAX__FIELD_NAME.field_name)

    def set_DilutionFactorMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'DilutionFactorMIN' on this record model
        """
        self.set_field_value(self.DILUTIONFACTORMIN__FIELD_NAME.field_name, value)

    def get_DilutionFactorMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'DilutionFactorMIN' from this record model
        """
        return self.get_field_value(self.DILUTIONFACTORMIN__FIELD_NAME.field_name)

    def set_FailedReprocess_field(self, value: Optional[bool]):
        """
        Set data field with field name 'FailedReprocess' on this record model
        """
        self.set_field_value(self.FAILEDREPROCESS__FIELD_NAME.field_name, value)

    def get_FailedReprocess_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'FailedReprocess' from this record model
        """
        return self.get_field_value(self.FAILEDREPROCESS__FIELD_NAME.field_name)

    def set_MapToConcentration_field(self, value: Optional[str]):
        """
        Set data field with field name 'MapToConcentration' on this record model
        """
        self.set_field_value(self.MAPTOCONCENTRATION__FIELD_NAME.field_name, value)

    def get_MapToConcentration_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MapToConcentration' from this record model
        """
        return self.get_field_value(self.MAPTOCONCENTRATION__FIELD_NAME.field_name)

    def set_MapToConcentrationUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'MapToConcentrationUnits' on this record model
        """
        self.set_field_value(self.MAPTOCONCENTRATIONUNITS__FIELD_NAME.field_name, value)

    def get_MapToConcentrationUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MapToConcentrationUnits' from this record model
        """
        return self.get_field_value(self.MAPTOCONCENTRATIONUNITS__FIELD_NAME.field_name)

    def set_MolarityMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'MolarityMAX' on this record model
        """
        self.set_field_value(self.MOLARITYMAX__FIELD_NAME.field_name, value)

    def get_MolarityMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'MolarityMAX' from this record model
        """
        return self.get_field_value(self.MOLARITYMAX__FIELD_NAME.field_name)

    def set_MolarityMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'MolarityMIN' on this record model
        """
        self.set_field_value(self.MOLARITYMIN__FIELD_NAME.field_name, value)

    def get_MolarityMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'MolarityMIN' from this record model
        """
        return self.get_field_value(self.MOLARITYMIN__FIELD_NAME.field_name)

    def set_PeakValueMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'PeakValueMAX' on this record model
        """
        self.set_field_value(self.PEAKVALUEMAX__FIELD_NAME.field_name, value)

    def get_PeakValueMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PeakValueMAX' from this record model
        """
        return self.get_field_value(self.PEAKVALUEMAX__FIELD_NAME.field_name)

    def set_PeakValueMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'PeakValueMIN' on this record model
        """
        self.set_field_value(self.PEAKVALUEMIN__FIELD_NAME.field_name, value)

    def get_PeakValueMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PeakValueMIN' from this record model
        """
        return self.get_field_value(self.PEAKVALUEMIN__FIELD_NAME.field_name)

    def set_PreferredExperiment_field(self, value: Optional[bool]):
        """
        Set data field with field name 'PreferredExperiment' on this record model
        """
        self.set_field_value(self.PREFERREDEXPERIMENT__FIELD_NAME.field_name, value)

    def get_PreferredExperiment_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'PreferredExperiment' from this record model
        """
        return self.get_field_value(self.PREFERREDEXPERIMENT__FIELD_NAME.field_name)

    def set_QCConfigId_field(self, value: Optional[str]):
        """
        Set data field with field name 'QCConfigId' on this record model
        """
        self.set_field_value(self.QCCONFIGID__FIELD_NAME.field_name, value)

    def get_QCConfigId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'QCConfigId' from this record model
        """
        return self.get_field_value(self.QCCONFIGID__FIELD_NAME.field_name)

    def set_QuantityMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityMAX' on this record model
        """
        self.set_field_value(self.QUANTITYMAX__FIELD_NAME.field_name, value)

    def get_QuantityMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityMAX' from this record model
        """
        return self.get_field_value(self.QUANTITYMAX__FIELD_NAME.field_name)

    def set_QuantityMeanMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityMeanMAX' on this record model
        """
        self.set_field_value(self.QUANTITYMEANMAX__FIELD_NAME.field_name, value)

    def get_QuantityMeanMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityMeanMAX' from this record model
        """
        return self.get_field_value(self.QUANTITYMEANMAX__FIELD_NAME.field_name)

    def set_QuantityMeanMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityMeanMIN' on this record model
        """
        self.set_field_value(self.QUANTITYMEANMIN__FIELD_NAME.field_name, value)

    def get_QuantityMeanMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityMeanMIN' from this record model
        """
        return self.get_field_value(self.QUANTITYMEANMIN__FIELD_NAME.field_name)

    def set_QuantityMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantityMIN' on this record model
        """
        self.set_field_value(self.QUANTITYMIN__FIELD_NAME.field_name, value)

    def get_QuantityMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantityMIN' from this record model
        """
        return self.get_field_value(self.QUANTITYMIN__FIELD_NAME.field_name)

    def set_QuantitySDMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantitySDMAX' on this record model
        """
        self.set_field_value(self.QUANTITYSDMAX__FIELD_NAME.field_name, value)

    def get_QuantitySDMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantitySDMAX' from this record model
        """
        return self.get_field_value(self.QUANTITYSDMAX__FIELD_NAME.field_name)

    def set_QuantitySDMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'QuantitySDMIN' on this record model
        """
        self.set_field_value(self.QUANTITYSDMIN__FIELD_NAME.field_name, value)

    def get_QuantitySDMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'QuantitySDMIN' from this record model
        """
        return self.get_field_value(self.QUANTITYSDMIN__FIELD_NAME.field_name)

    def set_RequiredResultsPerSample_field(self, value: Optional[int]):
        """
        Set data field with field name 'RequiredResultsPerSample' on this record model
        """
        self.set_field_value(self.REQUIREDRESULTSPERSAMPLE__FIELD_NAME.field_name, value)

    def get_RequiredResultsPerSample_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RequiredResultsPerSample' from this record model
        """
        return self.get_field_value(self.REQUIREDRESULTSPERSAMPLE__FIELD_NAME.field_name)

    def set_RequiresConcentration_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RequiresConcentration' on this record model
        """
        self.set_field_value(self.REQUIRESCONCENTRATION__FIELD_NAME.field_name, value)

    def get_RequiresConcentration_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RequiresConcentration' from this record model
        """
        return self.get_field_value(self.REQUIRESCONCENTRATION__FIELD_NAME.field_name)

    def set_RequiresQC_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RequiresQC' on this record model
        """
        self.set_field_value(self.REQUIRESQC__FIELD_NAME.field_name, value)

    def get_RequiresQC_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RequiresQC' from this record model
        """
        return self.get_field_value(self.REQUIRESQC__FIELD_NAME.field_name)

    def set_RINMAX_field(self, value: Optional[float]):
        """
        Set data field with field name 'RINMAX' on this record model
        """
        self.set_field_value(self.RINMAX__FIELD_NAME.field_name, value)

    def get_RINMAX_field(self) -> Optional[float]:
        """
        Get data field value with field name 'RINMAX' from this record model
        """
        return self.get_field_value(self.RINMAX__FIELD_NAME.field_name)

    def set_RINMIN_field(self, value: Optional[float]):
        """
        Set data field with field name 'RINMIN' on this record model
        """
        self.set_field_value(self.RINMIN__FIELD_NAME.field_name, value)

    def get_RINMIN_field(self) -> Optional[float]:
        """
        Get data field value with field name 'RINMIN' from this record model
        """
        return self.get_field_value(self.RINMIN__FIELD_NAME.field_name)


class QScoreDistributionModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type QScoreDistribution
    Data Type Display Name: Q Score Distribution (Q Score Distributions)
    Fields: ColRead, Lane, LaneCol, PercentGreatQThirty, PercentGreatQTwenty
    <!-- DISPLAY IN INSTRUMENT RUN MONITOR -->
    """
    DATA_TYPE_NAME: str = 'QScoreDistribution'
    COLREAD__FIELD_NAME: WrapperField = WrapperField("ColRead", FieldType.STRING)
    LANE__FIELD_NAME: WrapperField = WrapperField("Lane", FieldType.LONG)
    LANECOL__FIELD_NAME: WrapperField = WrapperField("LaneCol", FieldType.STRING)
    PERCENTGREATQTHIRTY__FIELD_NAME: WrapperField = WrapperField("PercentGreatQThirty", FieldType.DOUBLE)
    PERCENTGREATQTWENTY__FIELD_NAME: WrapperField = WrapperField("PercentGreatQTwenty", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColRead_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColRead' on this record model
        """
        self.set_field_value(self.COLREAD__FIELD_NAME.field_name, value)

    def get_ColRead_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColRead' from this record model
        """
        return self.get_field_value(self.COLREAD__FIELD_NAME.field_name)

    def set_Lane_field(self, value: Optional[int]):
        """
        Set data field with field name 'Lane' on this record model
        """
        self.set_field_value(self.LANE__FIELD_NAME.field_name, value)

    def get_Lane_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Lane' from this record model
        """
        return self.get_field_value(self.LANE__FIELD_NAME.field_name)

    def set_LaneCol_field(self, value: Optional[str]):
        """
        Set data field with field name 'LaneCol' on this record model
        """
        self.set_field_value(self.LANECOL__FIELD_NAME.field_name, value)

    def get_LaneCol_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LaneCol' from this record model
        """
        return self.get_field_value(self.LANECOL__FIELD_NAME.field_name)

    def set_PercentGreatQThirty_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentGreatQThirty' on this record model
        """
        self.set_field_value(self.PERCENTGREATQTHIRTY__FIELD_NAME.field_name, value)

    def get_PercentGreatQThirty_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentGreatQThirty' from this record model
        """
        return self.get_field_value(self.PERCENTGREATQTHIRTY__FIELD_NAME.field_name)

    def set_PercentGreatQTwenty_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentGreatQTwenty' on this record model
        """
        self.set_field_value(self.PERCENTGREATQTWENTY__FIELD_NAME.field_name, value)

    def get_PercentGreatQTwenty_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentGreatQTwenty' from this record model
        """
        return self.get_field_value(self.PERCENTGREATQTWENTY__FIELD_NAME.field_name)


class ReactionModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Reaction
    Data Type Display Name: Reaction (Reactions)
    Fields: Formula, GenerateName, Products, Reactants, ReactionCoefficient, Render, SMILES, SubstanceName
    """
    DATA_TYPE_NAME: str = 'Reaction'
    FORMULA__FIELD_NAME: WrapperField = WrapperField("Formula", FieldType.STRING)
    GENERATENAME__FIELD_NAME: WrapperField = WrapperField("GenerateName", FieldType.ACTION)
    PRODUCTS__FIELD_NAME: WrapperField = WrapperField("Products", FieldType.SELECTION)
    REACTANTS__FIELD_NAME: WrapperField = WrapperField("Reactants", FieldType.SELECTION)
    REACTIONCOEFFICIENT__FIELD_NAME: WrapperField = WrapperField("ReactionCoefficient", FieldType.INTEGER)
    RENDER__FIELD_NAME: WrapperField = WrapperField("Render", FieldType.STRING)
    SMILES__FIELD_NAME: WrapperField = WrapperField("SMILES", FieldType.STRING)
    SUBSTANCENAME__FIELD_NAME: WrapperField = WrapperField("SubstanceName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Formula_field(self, value: Optional[str]):
        """
        Set data field with field name 'Formula' on this record model
        """
        self.set_field_value(self.FORMULA__FIELD_NAME.field_name, value)

    def get_Formula_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Formula' from this record model
        """
        return self.get_field_value(self.FORMULA__FIELD_NAME.field_name)

    def set_Products_field(self, value: Optional[str]):
        """
        Set data field with field name 'Products' on this record model
        """
        self.set_field_value(self.PRODUCTS__FIELD_NAME.field_name, value)

    def get_Products_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Products' from this record model
        """
        return self.get_field_value(self.PRODUCTS__FIELD_NAME.field_name)

    def set_Reactants_field(self, value: Optional[str]):
        """
        Set data field with field name 'Reactants' on this record model
        """
        self.set_field_value(self.REACTANTS__FIELD_NAME.field_name, value)

    def get_Reactants_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Reactants' from this record model
        """
        return self.get_field_value(self.REACTANTS__FIELD_NAME.field_name)

    def set_ReactionCoefficient_field(self, value: Optional[int]):
        """
        Set data field with field name 'ReactionCoefficient' on this record model
        """
        self.set_field_value(self.REACTIONCOEFFICIENT__FIELD_NAME.field_name, value)

    def get_ReactionCoefficient_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ReactionCoefficient' from this record model
        """
        return self.get_field_value(self.REACTIONCOEFFICIENT__FIELD_NAME.field_name)

    def set_Render_field(self, value: Optional[str]):
        """
        Set data field with field name 'Render' on this record model
        """
        self.set_field_value(self.RENDER__FIELD_NAME.field_name, value)

    def get_Render_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Render' from this record model
        """
        return self.get_field_value(self.RENDER__FIELD_NAME.field_name)

    def set_SMILES_field(self, value: Optional[str]):
        """
        Set data field with field name 'SMILES' on this record model
        """
        self.set_field_value(self.SMILES__FIELD_NAME.field_name, value)

    def get_SMILES_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SMILES' from this record model
        """
        return self.get_field_value(self.SMILES__FIELD_NAME.field_name)

    def set_SubstanceName_field(self, value: Optional[str]):
        """
        Set data field with field name 'SubstanceName' on this record model
        """
        self.set_field_value(self.SUBSTANCENAME__FIELD_NAME.field_name, value)

    def get_SubstanceName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SubstanceName' from this record model
        """
        return self.get_field_value(self.SUBSTANCENAME__FIELD_NAME.field_name)


class ReactionComponentModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ReactionComponent
    Data Type Display Name: Reaction Component (Reaction Components)
    Fields: LimitingReactant, Name, ReactionCoefficient, Role
    """
    DATA_TYPE_NAME: str = 'ReactionComponent'
    LIMITINGREACTANT__FIELD_NAME: WrapperField = WrapperField("LimitingReactant", FieldType.BOOLEAN)
    NAME__FIELD_NAME: WrapperField = WrapperField("Name", FieldType.STRING)
    REACTIONCOEFFICIENT__FIELD_NAME: WrapperField = WrapperField("ReactionCoefficient", FieldType.DOUBLE)
    ROLE__FIELD_NAME: WrapperField = WrapperField("Role", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_LimitingReactant_field(self, value: Optional[bool]):
        """
        Set data field with field name 'LimitingReactant' on this record model
        """
        self.set_field_value(self.LIMITINGREACTANT__FIELD_NAME.field_name, value)

    def get_LimitingReactant_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'LimitingReactant' from this record model
        """
        return self.get_field_value(self.LIMITINGREACTANT__FIELD_NAME.field_name)

    def set_Name_field(self, value: Optional[str]):
        """
        Set data field with field name 'Name' on this record model
        """
        self.set_field_value(self.NAME__FIELD_NAME.field_name, value)

    def get_Name_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Name' from this record model
        """
        return self.get_field_value(self.NAME__FIELD_NAME.field_name)

    def set_ReactionCoefficient_field(self, value: Optional[float]):
        """
        Set data field with field name 'ReactionCoefficient' on this record model
        """
        self.set_field_value(self.REACTIONCOEFFICIENT__FIELD_NAME.field_name, value)

    def get_ReactionCoefficient_field(self) -> Optional[float]:
        """
        Get data field value with field name 'ReactionCoefficient' from this record model
        """
        return self.get_field_value(self.REACTIONCOEFFICIENT__FIELD_NAME.field_name)

    def set_Role_field(self, value: Optional[str]):
        """
        Set data field with field name 'Role' on this record model
        """
        self.set_field_value(self.ROLE__FIELD_NAME.field_name, value)

    def get_Role_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Role' from this record model
        """
        return self.get_field_value(self.ROLE__FIELD_NAME.field_name)


class RequestModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Request
    Data Type Display Name: Request (Requests)
    Fields: AddSamplesMethod, ArePoolsIncluded, AreSamplesLibraries, CompletedDate, DisableRequetFields, InProcessDate, NumberOfSamples, PartiallyReceivedDate, ReceivedDate, RequestApproved, RequestDate, RequesterEmail, RequesterName, RequesterOrganization, RequesterPhoneNumber, RequestId, RequestName, Status, TATFromInProcessing, TATFromReceiving
    """
    DATA_TYPE_NAME: str = 'Request'
    ADDSAMPLESMETHOD__FIELD_NAME: WrapperField = WrapperField("AddSamplesMethod", FieldType.PICKLIST)
    AREPOOLSINCLUDED__FIELD_NAME: WrapperField = WrapperField("ArePoolsIncluded", FieldType.BOOLEAN)
    ARESAMPLESLIBRARIES__FIELD_NAME: WrapperField = WrapperField("AreSamplesLibraries", FieldType.BOOLEAN)
    COMPLETEDDATE__FIELD_NAME: WrapperField = WrapperField("CompletedDate", FieldType.DATE)
    DISABLEREQUETFIELDS__FIELD_NAME: WrapperField = WrapperField("DisableRequetFields", FieldType.BOOLEAN)
    INPROCESSDATE__FIELD_NAME: WrapperField = WrapperField("InProcessDate", FieldType.DATE)
    NUMBEROFSAMPLES__FIELD_NAME: WrapperField = WrapperField("NumberOfSamples", FieldType.LONG)
    PARTIALLYRECEIVEDDATE__FIELD_NAME: WrapperField = WrapperField("PartiallyReceivedDate", FieldType.DATE)
    RECEIVEDDATE__FIELD_NAME: WrapperField = WrapperField("ReceivedDate", FieldType.DATE)
    REQUESTAPPROVED__FIELD_NAME: WrapperField = WrapperField("RequestApproved", FieldType.BOOLEAN)
    REQUESTDATE__FIELD_NAME: WrapperField = WrapperField("RequestDate", FieldType.DATE)
    REQUESTEREMAIL__FIELD_NAME: WrapperField = WrapperField("RequesterEmail", FieldType.STRING)
    REQUESTERNAME__FIELD_NAME: WrapperField = WrapperField("RequesterName", FieldType.STRING)
    REQUESTERORGANIZATION__FIELD_NAME: WrapperField = WrapperField("RequesterOrganization", FieldType.STRING)
    REQUESTERPHONENUMBER__FIELD_NAME: WrapperField = WrapperField("RequesterPhoneNumber", FieldType.STRING)
    REQUESTID__FIELD_NAME: WrapperField = WrapperField("RequestId", FieldType.AUTO_ACCESSION)
    REQUESTNAME__FIELD_NAME: WrapperField = WrapperField("RequestName", FieldType.STRING)
    STATUS__FIELD_NAME: WrapperField = WrapperField("Status", FieldType.PICKLIST)
    TATFROMINPROCESSING__FIELD_NAME: WrapperField = WrapperField("TATFromInProcessing", FieldType.STRING)
    TATFROMRECEIVING__FIELD_NAME: WrapperField = WrapperField("TATFromReceiving", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AddSamplesMethod_field(self, value: Optional[str]):
        """
        Set data field with field name 'AddSamplesMethod' on this record model
        """
        self.set_field_value(self.ADDSAMPLESMETHOD__FIELD_NAME.field_name, value)

    def get_AddSamplesMethod_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AddSamplesMethod' from this record model
        """
        return self.get_field_value(self.ADDSAMPLESMETHOD__FIELD_NAME.field_name)

    def set_ArePoolsIncluded_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ArePoolsIncluded' on this record model
        """
        self.set_field_value(self.AREPOOLSINCLUDED__FIELD_NAME.field_name, value)

    def get_ArePoolsIncluded_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ArePoolsIncluded' from this record model
        """
        return self.get_field_value(self.AREPOOLSINCLUDED__FIELD_NAME.field_name)

    def set_AreSamplesLibraries_field(self, value: Optional[bool]):
        """
        Set data field with field name 'AreSamplesLibraries' on this record model
        """
        self.set_field_value(self.ARESAMPLESLIBRARIES__FIELD_NAME.field_name, value)

    def get_AreSamplesLibraries_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'AreSamplesLibraries' from this record model
        """
        return self.get_field_value(self.ARESAMPLESLIBRARIES__FIELD_NAME.field_name)

    def set_CompletedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'CompletedDate' on this record model
        """
        self.set_field_value(self.COMPLETEDDATE__FIELD_NAME.field_name, value)

    def get_CompletedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CompletedDate' from this record model
        """
        return self.get_field_value(self.COMPLETEDDATE__FIELD_NAME.field_name)

    def set_DisableRequetFields_field(self, value: Optional[bool]):
        """
        Set data field with field name 'DisableRequetFields' on this record model
        """
        self.set_field_value(self.DISABLEREQUETFIELDS__FIELD_NAME.field_name, value)

    def get_DisableRequetFields_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'DisableRequetFields' from this record model
        """
        return self.get_field_value(self.DISABLEREQUETFIELDS__FIELD_NAME.field_name)

    def set_InProcessDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'InProcessDate' on this record model
        """
        self.set_field_value(self.INPROCESSDATE__FIELD_NAME.field_name, value)

    def get_InProcessDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'InProcessDate' from this record model
        """
        return self.get_field_value(self.INPROCESSDATE__FIELD_NAME.field_name)

    def set_NumberOfSamples_field(self, value: Optional[int]):
        """
        Set data field with field name 'NumberOfSamples' on this record model
        """
        self.set_field_value(self.NUMBEROFSAMPLES__FIELD_NAME.field_name, value)

    def get_NumberOfSamples_field(self) -> Optional[int]:
        """
        Get data field value with field name 'NumberOfSamples' from this record model
        """
        return self.get_field_value(self.NUMBEROFSAMPLES__FIELD_NAME.field_name)

    def set_PartiallyReceivedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'PartiallyReceivedDate' on this record model
        """
        self.set_field_value(self.PARTIALLYRECEIVEDDATE__FIELD_NAME.field_name, value)

    def get_PartiallyReceivedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'PartiallyReceivedDate' from this record model
        """
        return self.get_field_value(self.PARTIALLYRECEIVEDDATE__FIELD_NAME.field_name)

    def set_ReceivedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ReceivedDate' on this record model
        """
        self.set_field_value(self.RECEIVEDDATE__FIELD_NAME.field_name, value)

    def get_ReceivedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ReceivedDate' from this record model
        """
        return self.get_field_value(self.RECEIVEDDATE__FIELD_NAME.field_name)

    def set_RequestApproved_field(self, value: Optional[bool]):
        """
        Set data field with field name 'RequestApproved' on this record model
        """
        self.set_field_value(self.REQUESTAPPROVED__FIELD_NAME.field_name, value)

    def get_RequestApproved_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'RequestApproved' from this record model
        """
        return self.get_field_value(self.REQUESTAPPROVED__FIELD_NAME.field_name)

    def set_RequestDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'RequestDate' on this record model
        """
        self.set_field_value(self.REQUESTDATE__FIELD_NAME.field_name, value)

    def get_RequestDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'RequestDate' from this record model
        """
        return self.get_field_value(self.REQUESTDATE__FIELD_NAME.field_name)

    def set_RequesterEmail_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequesterEmail' on this record model
        """
        self.set_field_value(self.REQUESTEREMAIL__FIELD_NAME.field_name, value)

    def get_RequesterEmail_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequesterEmail' from this record model
        """
        return self.get_field_value(self.REQUESTEREMAIL__FIELD_NAME.field_name)

    def set_RequesterName_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequesterName' on this record model
        """
        self.set_field_value(self.REQUESTERNAME__FIELD_NAME.field_name, value)

    def get_RequesterName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequesterName' from this record model
        """
        return self.get_field_value(self.REQUESTERNAME__FIELD_NAME.field_name)

    def set_RequesterOrganization_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequesterOrganization' on this record model
        """
        self.set_field_value(self.REQUESTERORGANIZATION__FIELD_NAME.field_name, value)

    def get_RequesterOrganization_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequesterOrganization' from this record model
        """
        return self.get_field_value(self.REQUESTERORGANIZATION__FIELD_NAME.field_name)

    def set_RequesterPhoneNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequesterPhoneNumber' on this record model
        """
        self.set_field_value(self.REQUESTERPHONENUMBER__FIELD_NAME.field_name, value)

    def get_RequesterPhoneNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequesterPhoneNumber' from this record model
        """
        return self.get_field_value(self.REQUESTERPHONENUMBER__FIELD_NAME.field_name)

    def set_RequestId_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequestId' on this record model
        """
        self.set_field_value(self.REQUESTID__FIELD_NAME.field_name, value)

    def get_RequestId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequestId' from this record model
        """
        return self.get_field_value(self.REQUESTID__FIELD_NAME.field_name)

    def set_RequestName_field(self, value: Optional[str]):
        """
        Set data field with field name 'RequestName' on this record model
        """
        self.set_field_value(self.REQUESTNAME__FIELD_NAME.field_name, value)

    def get_RequestName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RequestName' from this record model
        """
        return self.get_field_value(self.REQUESTNAME__FIELD_NAME.field_name)

    def set_Status_field(self, value: Optional[str]):
        """
        Set data field with field name 'Status' on this record model
        """
        self.set_field_value(self.STATUS__FIELD_NAME.field_name, value)

    def get_Status_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Status' from this record model
        """
        return self.get_field_value(self.STATUS__FIELD_NAME.field_name)

    def set_TATFromInProcessing_field(self, value: Optional[str]):
        """
        Set data field with field name 'TATFromInProcessing' on this record model
        """
        self.set_field_value(self.TATFROMINPROCESSING__FIELD_NAME.field_name, value)

    def get_TATFromInProcessing_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TATFromInProcessing' from this record model
        """
        return self.get_field_value(self.TATFROMINPROCESSING__FIELD_NAME.field_name)

    def set_TATFromReceiving_field(self, value: Optional[str]):
        """
        Set data field with field name 'TATFromReceiving' on this record model
        """
        self.set_field_value(self.TATFROMRECEIVING__FIELD_NAME.field_name, value)

    def get_TATFromReceiving_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TATFromReceiving' from this record model
        """
        return self.get_field_value(self.TATFROMRECEIVING__FIELD_NAME.field_name)


class ReturnPointModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type ReturnPoint
    Data Type Display Name: Return Point (Return Points)
    Fields: AttachPointId, ExemplarSampleType, MultiParentLink204, NextWorkflow, ProcessName, ProcessPointNumber, ProcessStepNumber, SampleId, SampleRecordId, TrackedRecordDataType
    This data is used to determine where you should restart a sample during reprocessing.
    """
    DATA_TYPE_NAME: str = 'ReturnPoint'
    ATTACHPOINTID__FIELD_NAME: WrapperField = WrapperField("AttachPointId", FieldType.STRING)
    EXEMPLARSAMPLETYPE__FIELD_NAME: WrapperField = WrapperField("ExemplarSampleType", FieldType.SELECTION)
    MULTIPARENTLINK204__FIELD_NAME: WrapperField = WrapperField("MultiParentLink204", FieldType.MULTIPARENTLINK)
    NEXTWORKFLOW__FIELD_NAME: WrapperField = WrapperField("NextWorkflow", FieldType.STRING)
    PROCESSNAME__FIELD_NAME: WrapperField = WrapperField("ProcessName", FieldType.STRING)
    PROCESSPOINTNUMBER__FIELD_NAME: WrapperField = WrapperField("ProcessPointNumber", FieldType.LONG)
    PROCESSSTEPNUMBER__FIELD_NAME: WrapperField = WrapperField("ProcessStepNumber", FieldType.LONG)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)
    SAMPLERECORDID__FIELD_NAME: WrapperField = WrapperField("SampleRecordId", FieldType.LONG)
    TRACKEDRECORDDATATYPE__FIELD_NAME: WrapperField = WrapperField("TrackedRecordDataType", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AttachPointId_field(self, value: Optional[str]):
        """
        Set data field with field name 'AttachPointId' on this record model
        """
        self.set_field_value(self.ATTACHPOINTID__FIELD_NAME.field_name, value)

    def get_AttachPointId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AttachPointId' from this record model
        """
        return self.get_field_value(self.ATTACHPOINTID__FIELD_NAME.field_name)

    def set_ExemplarSampleType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExemplarSampleType' on this record model
        """
        self.set_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name, value)

    def get_ExemplarSampleType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExemplarSampleType' from this record model
        """
        return self.get_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name)

    def set_NextWorkflow_field(self, value: Optional[str]):
        """
        Set data field with field name 'NextWorkflow' on this record model
        """
        self.set_field_value(self.NEXTWORKFLOW__FIELD_NAME.field_name, value)

    def get_NextWorkflow_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NextWorkflow' from this record model
        """
        return self.get_field_value(self.NEXTWORKFLOW__FIELD_NAME.field_name)

    def set_ProcessName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ProcessName' on this record model
        """
        self.set_field_value(self.PROCESSNAME__FIELD_NAME.field_name, value)

    def get_ProcessName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ProcessName' from this record model
        """
        return self.get_field_value(self.PROCESSNAME__FIELD_NAME.field_name)

    def set_ProcessPointNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'ProcessPointNumber' on this record model
        """
        self.set_field_value(self.PROCESSPOINTNUMBER__FIELD_NAME.field_name, value)

    def get_ProcessPointNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ProcessPointNumber' from this record model
        """
        return self.get_field_value(self.PROCESSPOINTNUMBER__FIELD_NAME.field_name)

    def set_ProcessStepNumber_field(self, value: Optional[int]):
        """
        Set data field with field name 'ProcessStepNumber' on this record model
        """
        self.set_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name, value)

    def get_ProcessStepNumber_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ProcessStepNumber' from this record model
        """
        return self.get_field_value(self.PROCESSSTEPNUMBER__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)

    def set_SampleRecordId_field(self, value: Optional[int]):
        """
        Set data field with field name 'SampleRecordId' on this record model
        """
        self.set_field_value(self.SAMPLERECORDID__FIELD_NAME.field_name, value)

    def get_SampleRecordId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SampleRecordId' from this record model
        """
        return self.get_field_value(self.SAMPLERECORDID__FIELD_NAME.field_name)

    def set_TrackedRecordDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'TrackedRecordDataType' on this record model
        """
        self.set_field_value(self.TRACKEDRECORDDATATYPE__FIELD_NAME.field_name, value)

    def get_TrackedRecordDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TrackedRecordDataType' from this record model
        """
        return self.get_field_value(self.TRACKEDRECORDDATATYPE__FIELD_NAME.field_name)


class SampleModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Sample
    Data Type Display Name: Sample (Samples)
    Fields: ActiveWorkflowId, AssayType, C_GinkgoMaterial, CollectionDate, CollectionDateTime, ColPosition, Comments, Concentration, ConcentrationUnits, ContainerType, ControlType, ElnbNumber, ExemplarSampleStatus, ExemplarSampleType, Flags, IsControl, IsInvalid, IsPooled, LastEditedBy, MultiParentLink153, MultiParentLink197, MultiParentLink204, MultiParentLink207, NGSSingleTemplateProcess, ObservedCondition, Organism, Organism_todo1, Organism_todo2, OtherSampleId, PercentRecoveries, PlateId, PreviousExemplarStatus, RowPosition, SacrificedDate, SampleId, SapioSingleTemplateProcess, StorageLocationBarcode, StorageUnitPath, TatProgressStatus, TimePoint, TotalMass, TubeBarcode, Volume, VolumeUnits
    """
    DATA_TYPE_NAME: str = 'Sample'
    ACTIVEWORKFLOWID__FIELD_NAME: WrapperField = WrapperField("ActiveWorkflowId", FieldType.LONG)
    ASSAYTYPE__FIELD_NAME: WrapperField = WrapperField("AssayType", FieldType.STRING)
    C_GINKGOMATERIAL__FIELD_NAME: WrapperField = WrapperField("C_GinkgoMaterial", FieldType.SELECTION)
    COLLECTIONDATE__FIELD_NAME: WrapperField = WrapperField("CollectionDate", FieldType.DATE)
    COLLECTIONDATETIME__FIELD_NAME: WrapperField = WrapperField("CollectionDateTime", FieldType.DATE)
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    COMMENTS__FIELD_NAME: WrapperField = WrapperField("Comments", FieldType.STRING)
    CONCENTRATION__FIELD_NAME: WrapperField = WrapperField("Concentration", FieldType.DOUBLE)
    CONCENTRATIONUNITS__FIELD_NAME: WrapperField = WrapperField("ConcentrationUnits", FieldType.PICKLIST)
    CONTAINERTYPE__FIELD_NAME: WrapperField = WrapperField("ContainerType", FieldType.PICKLIST)
    CONTROLTYPE__FIELD_NAME: WrapperField = WrapperField("ControlType", FieldType.STRING)
    ELNBNUMBER__FIELD_NAME: WrapperField = WrapperField("ElnbNumber", FieldType.STRING)
    EXEMPLARSAMPLESTATUS__FIELD_NAME: WrapperField = WrapperField("ExemplarSampleStatus", FieldType.SELECTION)
    EXEMPLARSAMPLETYPE__FIELD_NAME: WrapperField = WrapperField("ExemplarSampleType", FieldType.SELECTION)
    FLAGS__FIELD_NAME: WrapperField = WrapperField("Flags", FieldType.STRING)
    ISCONTROL__FIELD_NAME: WrapperField = WrapperField("IsControl", FieldType.BOOLEAN)
    ISINVALID__FIELD_NAME: WrapperField = WrapperField("IsInvalid", FieldType.BOOLEAN)
    ISPOOLED__FIELD_NAME: WrapperField = WrapperField("IsPooled", FieldType.BOOLEAN)
    LASTEDITEDBY__FIELD_NAME: WrapperField = WrapperField("LastEditedBy", FieldType.STRING)
    MULTIPARENTLINK153__FIELD_NAME: WrapperField = WrapperField("MultiParentLink153", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK197__FIELD_NAME: WrapperField = WrapperField("MultiParentLink197", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK204__FIELD_NAME: WrapperField = WrapperField("MultiParentLink204", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK207__FIELD_NAME: WrapperField = WrapperField("MultiParentLink207", FieldType.MULTIPARENTLINK)
    NGSSINGLETEMPLATEPROCESS__FIELD_NAME: WrapperField = WrapperField("NGSSingleTemplateProcess", FieldType.PICKLIST)
    OBSERVEDCONDITION__FIELD_NAME: WrapperField = WrapperField("ObservedCondition", FieldType.SELECTION)
    ORGANISM__FIELD_NAME: WrapperField = WrapperField("Organism", FieldType.PICKLIST)
    ORGANISM_TODO1__FIELD_NAME: WrapperField = WrapperField("Organism_todo1", FieldType.BOOLEAN)
    ORGANISM_TODO2__FIELD_NAME: WrapperField = WrapperField("Organism_todo2", FieldType.BOOLEAN)
    OTHERSAMPLEID__FIELD_NAME: WrapperField = WrapperField("OtherSampleId", FieldType.STRING)
    PERCENTRECOVERIES__FIELD_NAME: WrapperField = WrapperField("PercentRecoveries", FieldType.DOUBLE)
    PLATEID__FIELD_NAME: WrapperField = WrapperField("PlateId", FieldType.STRING)
    PREVIOUSEXEMPLARSTATUS__FIELD_NAME: WrapperField = WrapperField("PreviousExemplarStatus", FieldType.SELECTION)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    SACRIFICEDDATE__FIELD_NAME: WrapperField = WrapperField("SacrificedDate", FieldType.DATE)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)
    SAPIOSINGLETEMPLATEPROCESS__FIELD_NAME: WrapperField = WrapperField("SapioSingleTemplateProcess", FieldType.PICKLIST)
    STORAGELOCATIONBARCODE__FIELD_NAME: WrapperField = WrapperField("StorageLocationBarcode", FieldType.SELECTION)
    STORAGEUNITPATH__FIELD_NAME: WrapperField = WrapperField("StorageUnitPath", FieldType.STRING)
    TATPROGRESSSTATUS__FIELD_NAME: WrapperField = WrapperField("TatProgressStatus", FieldType.PICKLIST)
    TIMEPOINT__FIELD_NAME: WrapperField = WrapperField("TimePoint", FieldType.DOUBLE)
    TOTALMASS__FIELD_NAME: WrapperField = WrapperField("TotalMass", FieldType.DOUBLE)
    TUBEBARCODE__FIELD_NAME: WrapperField = WrapperField("TubeBarcode", FieldType.STRING)
    VOLUME__FIELD_NAME: WrapperField = WrapperField("Volume", FieldType.DOUBLE)
    VOLUMEUNITS__FIELD_NAME: WrapperField = WrapperField("VolumeUnits", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ActiveWorkflowId_field(self, value: Optional[int]):
        """
        Set data field with field name 'ActiveWorkflowId' on this record model
        """
        self.set_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name, value)

    def get_ActiveWorkflowId_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ActiveWorkflowId' from this record model
        """
        return self.get_field_value(self.ACTIVEWORKFLOWID__FIELD_NAME.field_name)

    def set_AssayType_field(self, value: Optional[str]):
        """
        Set data field with field name 'AssayType' on this record model
        """
        self.set_field_value(self.ASSAYTYPE__FIELD_NAME.field_name, value)

    def get_AssayType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AssayType' from this record model
        """
        return self.get_field_value(self.ASSAYTYPE__FIELD_NAME.field_name)

    def set_C_GinkgoMaterial_field(self, value: Optional[str]):
        """
        Set data field with field name 'C_GinkgoMaterial' on this record model
        """
        self.set_field_value(self.C_GINKGOMATERIAL__FIELD_NAME.field_name, value)

    def get_C_GinkgoMaterial_field(self) -> Optional[str]:
        """
        Get data field value with field name 'C_GinkgoMaterial' from this record model
        """
        return self.get_field_value(self.C_GINKGOMATERIAL__FIELD_NAME.field_name)

    def set_CollectionDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'CollectionDate' on this record model
        """
        self.set_field_value(self.COLLECTIONDATE__FIELD_NAME.field_name, value)

    def get_CollectionDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CollectionDate' from this record model
        """
        return self.get_field_value(self.COLLECTIONDATE__FIELD_NAME.field_name)

    def set_CollectionDateTime_field(self, value: Optional[int]):
        """
        Set data field with field name 'CollectionDateTime' on this record model
        """
        self.set_field_value(self.COLLECTIONDATETIME__FIELD_NAME.field_name, value)

    def get_CollectionDateTime_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CollectionDateTime' from this record model
        """
        return self.get_field_value(self.COLLECTIONDATETIME__FIELD_NAME.field_name)

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_Comments_field(self, value: Optional[str]):
        """
        Set data field with field name 'Comments' on this record model
        """
        self.set_field_value(self.COMMENTS__FIELD_NAME.field_name, value)

    def get_Comments_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Comments' from this record model
        """
        return self.get_field_value(self.COMMENTS__FIELD_NAME.field_name)

    def set_Concentration_field(self, value: Optional[float]):
        """
        Set data field with field name 'Concentration' on this record model
        """
        self.set_field_value(self.CONCENTRATION__FIELD_NAME.field_name, value)

    def get_Concentration_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Concentration' from this record model
        """
        return self.get_field_value(self.CONCENTRATION__FIELD_NAME.field_name)

    def set_ConcentrationUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'ConcentrationUnits' on this record model
        """
        self.set_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name, value)

    def get_ConcentrationUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ConcentrationUnits' from this record model
        """
        return self.get_field_value(self.CONCENTRATIONUNITS__FIELD_NAME.field_name)

    def set_ContainerType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ContainerType' on this record model
        """
        self.set_field_value(self.CONTAINERTYPE__FIELD_NAME.field_name, value)

    def get_ContainerType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ContainerType' from this record model
        """
        return self.get_field_value(self.CONTAINERTYPE__FIELD_NAME.field_name)

    def set_ControlType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ControlType' on this record model
        """
        self.set_field_value(self.CONTROLTYPE__FIELD_NAME.field_name, value)

    def get_ControlType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ControlType' from this record model
        """
        return self.get_field_value(self.CONTROLTYPE__FIELD_NAME.field_name)

    def set_ElnbNumber_field(self, value: Optional[str]):
        """
        Set data field with field name 'ElnbNumber' on this record model
        """
        self.set_field_value(self.ELNBNUMBER__FIELD_NAME.field_name, value)

    def get_ElnbNumber_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ElnbNumber' from this record model
        """
        return self.get_field_value(self.ELNBNUMBER__FIELD_NAME.field_name)

    def set_ExemplarSampleStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExemplarSampleStatus' on this record model
        """
        self.set_field_value(self.EXEMPLARSAMPLESTATUS__FIELD_NAME.field_name, value)

    def get_ExemplarSampleStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExemplarSampleStatus' from this record model
        """
        return self.get_field_value(self.EXEMPLARSAMPLESTATUS__FIELD_NAME.field_name)

    def set_ExemplarSampleType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExemplarSampleType' on this record model
        """
        self.set_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name, value)

    def get_ExemplarSampleType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExemplarSampleType' from this record model
        """
        return self.get_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name)

    def set_Flags_field(self, value: Optional[str]):
        """
        Set data field with field name 'Flags' on this record model
        """
        self.set_field_value(self.FLAGS__FIELD_NAME.field_name, value)

    def get_Flags_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Flags' from this record model
        """
        return self.get_field_value(self.FLAGS__FIELD_NAME.field_name)

    def set_IsControl_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsControl' on this record model
        """
        self.set_field_value(self.ISCONTROL__FIELD_NAME.field_name, value)

    def get_IsControl_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsControl' from this record model
        """
        return self.get_field_value(self.ISCONTROL__FIELD_NAME.field_name)

    def set_IsInvalid_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsInvalid' on this record model
        """
        self.set_field_value(self.ISINVALID__FIELD_NAME.field_name, value)

    def get_IsInvalid_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsInvalid' from this record model
        """
        return self.get_field_value(self.ISINVALID__FIELD_NAME.field_name)

    def set_IsPooled_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsPooled' on this record model
        """
        self.set_field_value(self.ISPOOLED__FIELD_NAME.field_name, value)

    def get_IsPooled_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsPooled' from this record model
        """
        return self.get_field_value(self.ISPOOLED__FIELD_NAME.field_name)

    def set_LastEditedBy_field(self, value: Optional[str]):
        """
        Set data field with field name 'LastEditedBy' on this record model
        """
        self.set_field_value(self.LASTEDITEDBY__FIELD_NAME.field_name, value)

    def get_LastEditedBy_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LastEditedBy' from this record model
        """
        return self.get_field_value(self.LASTEDITEDBY__FIELD_NAME.field_name)

    def set_NGSSingleTemplateProcess_field(self, value: Optional[str]):
        """
        Set data field with field name 'NGSSingleTemplateProcess' on this record model
        """
        self.set_field_value(self.NGSSINGLETEMPLATEPROCESS__FIELD_NAME.field_name, value)

    def get_NGSSingleTemplateProcess_field(self) -> Optional[str]:
        """
        Get data field value with field name 'NGSSingleTemplateProcess' from this record model
        """
        return self.get_field_value(self.NGSSINGLETEMPLATEPROCESS__FIELD_NAME.field_name)

    def set_ObservedCondition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ObservedCondition' on this record model
        """
        self.set_field_value(self.OBSERVEDCONDITION__FIELD_NAME.field_name, value)

    def get_ObservedCondition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ObservedCondition' from this record model
        """
        return self.get_field_value(self.OBSERVEDCONDITION__FIELD_NAME.field_name)

    def set_Organism_field(self, value: Optional[str]):
        """
        Set data field with field name 'Organism' on this record model
        """
        self.set_field_value(self.ORGANISM__FIELD_NAME.field_name, value)

    def get_Organism_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Organism' from this record model
        """
        return self.get_field_value(self.ORGANISM__FIELD_NAME.field_name)

    def set_Organism_todo1_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Organism_todo1' on this record model
        """
        self.set_field_value(self.ORGANISM_TODO1__FIELD_NAME.field_name, value)

    def get_Organism_todo1_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Organism_todo1' from this record model
        """
        return self.get_field_value(self.ORGANISM_TODO1__FIELD_NAME.field_name)

    def set_Organism_todo2_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Organism_todo2' on this record model
        """
        self.set_field_value(self.ORGANISM_TODO2__FIELD_NAME.field_name, value)

    def get_Organism_todo2_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Organism_todo2' from this record model
        """
        return self.get_field_value(self.ORGANISM_TODO2__FIELD_NAME.field_name)

    def set_OtherSampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'OtherSampleId' on this record model
        """
        self.set_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name, value)

    def get_OtherSampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OtherSampleId' from this record model
        """
        return self.get_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name)

    def set_PercentRecoveries_field(self, value: Optional[float]):
        """
        Set data field with field name 'PercentRecoveries' on this record model
        """
        self.set_field_value(self.PERCENTRECOVERIES__FIELD_NAME.field_name, value)

    def get_PercentRecoveries_field(self) -> Optional[float]:
        """
        Get data field value with field name 'PercentRecoveries' from this record model
        """
        return self.get_field_value(self.PERCENTRECOVERIES__FIELD_NAME.field_name)

    def set_PlateId_field(self, value: Optional[str]):
        """
        Set data field with field name 'PlateId' on this record model
        """
        self.set_field_value(self.PLATEID__FIELD_NAME.field_name, value)

    def get_PlateId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PlateId' from this record model
        """
        return self.get_field_value(self.PLATEID__FIELD_NAME.field_name)

    def set_PreviousExemplarStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'PreviousExemplarStatus' on this record model
        """
        self.set_field_value(self.PREVIOUSEXEMPLARSTATUS__FIELD_NAME.field_name, value)

    def get_PreviousExemplarStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PreviousExemplarStatus' from this record model
        """
        return self.get_field_value(self.PREVIOUSEXEMPLARSTATUS__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_SacrificedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'SacrificedDate' on this record model
        """
        self.set_field_value(self.SACRIFICEDDATE__FIELD_NAME.field_name, value)

    def get_SacrificedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'SacrificedDate' from this record model
        """
        return self.get_field_value(self.SACRIFICEDDATE__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)

    def set_SapioSingleTemplateProcess_field(self, value: Optional[str]):
        """
        Set data field with field name 'SapioSingleTemplateProcess' on this record model
        """
        self.set_field_value(self.SAPIOSINGLETEMPLATEPROCESS__FIELD_NAME.field_name, value)

    def get_SapioSingleTemplateProcess_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SapioSingleTemplateProcess' from this record model
        """
        return self.get_field_value(self.SAPIOSINGLETEMPLATEPROCESS__FIELD_NAME.field_name)

    def set_StorageLocationBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageLocationBarcode' on this record model
        """
        self.set_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name, value)

    def get_StorageLocationBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageLocationBarcode' from this record model
        """
        return self.get_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name)

    def set_StorageUnitPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitPath' on this record model
        """
        self.set_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name, value)

    def get_StorageUnitPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitPath' from this record model
        """
        return self.get_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name)

    def set_TatProgressStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'TatProgressStatus' on this record model
        """
        self.set_field_value(self.TATPROGRESSSTATUS__FIELD_NAME.field_name, value)

    def get_TatProgressStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TatProgressStatus' from this record model
        """
        return self.get_field_value(self.TATPROGRESSSTATUS__FIELD_NAME.field_name)

    def set_TimePoint_field(self, value: Optional[float]):
        """
        Set data field with field name 'TimePoint' on this record model
        """
        self.set_field_value(self.TIMEPOINT__FIELD_NAME.field_name, value)

    def get_TimePoint_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TimePoint' from this record model
        """
        return self.get_field_value(self.TIMEPOINT__FIELD_NAME.field_name)

    def set_TotalMass_field(self, value: Optional[float]):
        """
        Set data field with field name 'TotalMass' on this record model
        """
        self.set_field_value(self.TOTALMASS__FIELD_NAME.field_name, value)

    def get_TotalMass_field(self) -> Optional[float]:
        """
        Get data field value with field name 'TotalMass' from this record model
        """
        return self.get_field_value(self.TOTALMASS__FIELD_NAME.field_name)

    def set_TubeBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'TubeBarcode' on this record model
        """
        self.set_field_value(self.TUBEBARCODE__FIELD_NAME.field_name, value)

    def get_TubeBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TubeBarcode' from this record model
        """
        return self.get_field_value(self.TUBEBARCODE__FIELD_NAME.field_name)

    def set_Volume_field(self, value: Optional[float]):
        """
        Set data field with field name 'Volume' on this record model
        """
        self.set_field_value(self.VOLUME__FIELD_NAME.field_name, value)

    def get_Volume_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Volume' from this record model
        """
        return self.get_field_value(self.VOLUME__FIELD_NAME.field_name)

    def set_VolumeUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'VolumeUnits' on this record model
        """
        self.set_field_value(self.VOLUMEUNITS__FIELD_NAME.field_name, value)

    def get_VolumeUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VolumeUnits' from this record model
        """
        return self.get_field_value(self.VOLUMEUNITS__FIELD_NAME.field_name)


class SampleImporterMappingModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type SampleImporterMapping
    Data Type Display Name: Sample Importer Mapping (Sample Importer Mappings)
    Fields: DataField, DataType, DisplayName, MappingGroup, MappingName, MappingOrder
    """
    DATA_TYPE_NAME: str = 'SampleImporterMapping'
    DATAFIELD__FIELD_NAME: WrapperField = WrapperField("DataField", FieldType.SELECTION)
    DATATYPE__FIELD_NAME: WrapperField = WrapperField("DataType", FieldType.PICKLIST)
    DISPLAYNAME__FIELD_NAME: WrapperField = WrapperField("DisplayName", FieldType.STRING)
    MAPPINGGROUP__FIELD_NAME: WrapperField = WrapperField("MappingGroup", FieldType.STRING)
    MAPPINGNAME__FIELD_NAME: WrapperField = WrapperField("MappingName", FieldType.STRING)
    MAPPINGORDER__FIELD_NAME: WrapperField = WrapperField("MappingOrder", FieldType.SHORT)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DataField_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataField' on this record model
        """
        self.set_field_value(self.DATAFIELD__FIELD_NAME.field_name, value)

    def get_DataField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataField' from this record model
        """
        return self.get_field_value(self.DATAFIELD__FIELD_NAME.field_name)

    def set_DataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataType' on this record model
        """
        self.set_field_value(self.DATATYPE__FIELD_NAME.field_name, value)

    def get_DataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataType' from this record model
        """
        return self.get_field_value(self.DATATYPE__FIELD_NAME.field_name)

    def set_DisplayName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DisplayName' on this record model
        """
        self.set_field_value(self.DISPLAYNAME__FIELD_NAME.field_name, value)

    def get_DisplayName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DisplayName' from this record model
        """
        return self.get_field_value(self.DISPLAYNAME__FIELD_NAME.field_name)

    def set_MappingGroup_field(self, value: Optional[str]):
        """
        Set data field with field name 'MappingGroup' on this record model
        """
        self.set_field_value(self.MAPPINGGROUP__FIELD_NAME.field_name, value)

    def get_MappingGroup_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MappingGroup' from this record model
        """
        return self.get_field_value(self.MAPPINGGROUP__FIELD_NAME.field_name)

    def set_MappingName_field(self, value: Optional[str]):
        """
        Set data field with field name 'MappingName' on this record model
        """
        self.set_field_value(self.MAPPINGNAME__FIELD_NAME.field_name, value)

    def get_MappingName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MappingName' from this record model
        """
        return self.get_field_value(self.MAPPINGNAME__FIELD_NAME.field_name)

    def set_MappingOrder_field(self, value: Optional[int]):
        """
        Set data field with field name 'MappingOrder' on this record model
        """
        self.set_field_value(self.MAPPINGORDER__FIELD_NAME.field_name, value)

    def get_MappingOrder_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MappingOrder' from this record model
        """
        return self.get_field_value(self.MAPPINGORDER__FIELD_NAME.field_name)


class SampleImporterMappingConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type SampleImporterMappingConfig
    Data Type Display Name: Sample Importer Mapping Configuration (Sample Importer Mapping Configurations)
    Fields: HandleLibraries, HandlePlateManifest, HandlePools, HandleSampleManifest, MappingGroup, MappingOrder
    """
    DATA_TYPE_NAME: str = 'SampleImporterMappingConfig'
    HANDLELIBRARIES__FIELD_NAME: WrapperField = WrapperField("HandleLibraries", FieldType.BOOLEAN)
    HANDLEPLATEMANIFEST__FIELD_NAME: WrapperField = WrapperField("HandlePlateManifest", FieldType.BOOLEAN)
    HANDLEPOOLS__FIELD_NAME: WrapperField = WrapperField("HandlePools", FieldType.BOOLEAN)
    HANDLESAMPLEMANIFEST__FIELD_NAME: WrapperField = WrapperField("HandleSampleManifest", FieldType.BOOLEAN)
    MAPPINGGROUP__FIELD_NAME: WrapperField = WrapperField("MappingGroup", FieldType.STRING)
    MAPPINGORDER__FIELD_NAME: WrapperField = WrapperField("MappingOrder", FieldType.SHORT)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_HandleLibraries_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HandleLibraries' on this record model
        """
        self.set_field_value(self.HANDLELIBRARIES__FIELD_NAME.field_name, value)

    def get_HandleLibraries_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HandleLibraries' from this record model
        """
        return self.get_field_value(self.HANDLELIBRARIES__FIELD_NAME.field_name)

    def set_HandlePlateManifest_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HandlePlateManifest' on this record model
        """
        self.set_field_value(self.HANDLEPLATEMANIFEST__FIELD_NAME.field_name, value)

    def get_HandlePlateManifest_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HandlePlateManifest' from this record model
        """
        return self.get_field_value(self.HANDLEPLATEMANIFEST__FIELD_NAME.field_name)

    def set_HandlePools_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HandlePools' on this record model
        """
        self.set_field_value(self.HANDLEPOOLS__FIELD_NAME.field_name, value)

    def get_HandlePools_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HandlePools' from this record model
        """
        return self.get_field_value(self.HANDLEPOOLS__FIELD_NAME.field_name)

    def set_HandleSampleManifest_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HandleSampleManifest' on this record model
        """
        self.set_field_value(self.HANDLESAMPLEMANIFEST__FIELD_NAME.field_name, value)

    def get_HandleSampleManifest_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HandleSampleManifest' from this record model
        """
        return self.get_field_value(self.HANDLESAMPLEMANIFEST__FIELD_NAME.field_name)

    def set_MappingGroup_field(self, value: Optional[str]):
        """
        Set data field with field name 'MappingGroup' on this record model
        """
        self.set_field_value(self.MAPPINGGROUP__FIELD_NAME.field_name, value)

    def get_MappingGroup_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MappingGroup' from this record model
        """
        return self.get_field_value(self.MAPPINGGROUP__FIELD_NAME.field_name)

    def set_MappingOrder_field(self, value: Optional[int]):
        """
        Set data field with field name 'MappingOrder' on this record model
        """
        self.set_field_value(self.MAPPINGORDER__FIELD_NAME.field_name, value)

    def get_MappingOrder_field(self) -> Optional[int]:
        """
        Get data field value with field name 'MappingOrder' from this record model
        """
        return self.get_field_value(self.MAPPINGORDER__FIELD_NAME.field_name)


class SampleReceiptModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type SampleReceipt
    Data Type Display Name: Sample Receipt (Sample Receipts)
    Fields: ExemplarSampleType, FailureComment, OtherSampleId, ReceivedBy, ReceivedDate, RejectionReason, SampleId, SampleReceivedRejected, Volume
    """
    DATA_TYPE_NAME: str = 'SampleReceipt'
    EXEMPLARSAMPLETYPE__FIELD_NAME: WrapperField = WrapperField("ExemplarSampleType", FieldType.SELECTION)
    FAILURECOMMENT__FIELD_NAME: WrapperField = WrapperField("FailureComment", FieldType.STRING)
    OTHERSAMPLEID__FIELD_NAME: WrapperField = WrapperField("OtherSampleId", FieldType.STRING)
    RECEIVEDBY__FIELD_NAME: WrapperField = WrapperField("ReceivedBy", FieldType.SELECTION)
    RECEIVEDDATE__FIELD_NAME: WrapperField = WrapperField("ReceivedDate", FieldType.DATE)
    REJECTIONREASON__FIELD_NAME: WrapperField = WrapperField("RejectionReason", FieldType.PICKLIST)
    SAMPLEID__FIELD_NAME: WrapperField = WrapperField("SampleId", FieldType.STRING)
    SAMPLERECEIVEDREJECTED__FIELD_NAME: WrapperField = WrapperField("SampleReceivedRejected", FieldType.PICKLIST)
    VOLUME__FIELD_NAME: WrapperField = WrapperField("Volume", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ExemplarSampleType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExemplarSampleType' on this record model
        """
        self.set_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name, value)

    def get_ExemplarSampleType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExemplarSampleType' from this record model
        """
        return self.get_field_value(self.EXEMPLARSAMPLETYPE__FIELD_NAME.field_name)

    def set_FailureComment_field(self, value: Optional[str]):
        """
        Set data field with field name 'FailureComment' on this record model
        """
        self.set_field_value(self.FAILURECOMMENT__FIELD_NAME.field_name, value)

    def get_FailureComment_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FailureComment' from this record model
        """
        return self.get_field_value(self.FAILURECOMMENT__FIELD_NAME.field_name)

    def set_OtherSampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'OtherSampleId' on this record model
        """
        self.set_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name, value)

    def get_OtherSampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'OtherSampleId' from this record model
        """
        return self.get_field_value(self.OTHERSAMPLEID__FIELD_NAME.field_name)

    def set_ReceivedBy_field(self, value: Optional[str]):
        """
        Set data field with field name 'ReceivedBy' on this record model
        """
        self.set_field_value(self.RECEIVEDBY__FIELD_NAME.field_name, value)

    def get_ReceivedBy_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ReceivedBy' from this record model
        """
        return self.get_field_value(self.RECEIVEDBY__FIELD_NAME.field_name)

    def set_ReceivedDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'ReceivedDate' on this record model
        """
        self.set_field_value(self.RECEIVEDDATE__FIELD_NAME.field_name, value)

    def get_ReceivedDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'ReceivedDate' from this record model
        """
        return self.get_field_value(self.RECEIVEDDATE__FIELD_NAME.field_name)

    def set_RejectionReason_field(self, value: Optional[str]):
        """
        Set data field with field name 'RejectionReason' on this record model
        """
        self.set_field_value(self.REJECTIONREASON__FIELD_NAME.field_name, value)

    def get_RejectionReason_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RejectionReason' from this record model
        """
        return self.get_field_value(self.REJECTIONREASON__FIELD_NAME.field_name)

    def set_SampleId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleId' on this record model
        """
        self.set_field_value(self.SAMPLEID__FIELD_NAME.field_name, value)

    def get_SampleId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleId' from this record model
        """
        return self.get_field_value(self.SAMPLEID__FIELD_NAME.field_name)

    def set_SampleReceivedRejected_field(self, value: Optional[str]):
        """
        Set data field with field name 'SampleReceivedRejected' on this record model
        """
        self.set_field_value(self.SAMPLERECEIVEDREJECTED__FIELD_NAME.field_name, value)

    def get_SampleReceivedRejected_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SampleReceivedRejected' from this record model
        """
        return self.get_field_value(self.SAMPLERECEIVEDREJECTED__FIELD_NAME.field_name)

    def set_Volume_field(self, value: Optional[float]):
        """
        Set data field with field name 'Volume' on this record model
        """
        self.set_field_value(self.VOLUME__FIELD_NAME.field_name, value)

    def get_Volume_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Volume' from this record model
        """
        return self.get_field_value(self.VOLUME__FIELD_NAME.field_name)


class StereoisomerModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Stereoisomer
    Data Type Display Name: Stereoisomer (Stereoisomers)
    Fields: MOL, SMILES
    Possible stereoisomer of a parent compound.
    """
    DATA_TYPE_NAME: str = 'Stereoisomer'
    MOL__FIELD_NAME: WrapperField = WrapperField("MOL", FieldType.STRING)
    SMILES__FIELD_NAME: WrapperField = WrapperField("SMILES", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_MOL_field(self, value: Optional[str]):
        """
        Set data field with field name 'MOL' on this record model
        """
        self.set_field_value(self.MOL__FIELD_NAME.field_name, value)

    def get_MOL_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MOL' from this record model
        """
        return self.get_field_value(self.MOL__FIELD_NAME.field_name)

    def set_SMILES_field(self, value: Optional[str]):
        """
        Set data field with field name 'SMILES' on this record model
        """
        self.set_field_value(self.SMILES__FIELD_NAME.field_name, value)

    def get_SMILES_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SMILES' from this record model
        """
        return self.get_field_value(self.SMILES__FIELD_NAME.field_name)


class StorageConfigurationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type StorageConfiguration
    Data Type Display Name: Storage Configuration (Storage Configurations)
    Fields: StorableItemDataType, StorableItemScanMatchField, StorableItemStorageUnits
    """
    DATA_TYPE_NAME: str = 'StorageConfiguration'
    STORABLEITEMDATATYPE__FIELD_NAME: WrapperField = WrapperField("StorableItemDataType", FieldType.SELECTION)
    STORABLEITEMSCANMATCHFIELD__FIELD_NAME: WrapperField = WrapperField("StorableItemScanMatchField", FieldType.SELECTION)
    STORABLEITEMSTORAGEUNITS__FIELD_NAME: WrapperField = WrapperField("StorableItemStorageUnits", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_StorableItemDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorableItemDataType' on this record model
        """
        self.set_field_value(self.STORABLEITEMDATATYPE__FIELD_NAME.field_name, value)

    def get_StorableItemDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorableItemDataType' from this record model
        """
        return self.get_field_value(self.STORABLEITEMDATATYPE__FIELD_NAME.field_name)

    def set_StorableItemScanMatchField_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorableItemScanMatchField' on this record model
        """
        self.set_field_value(self.STORABLEITEMSCANMATCHFIELD__FIELD_NAME.field_name, value)

    def get_StorableItemScanMatchField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorableItemScanMatchField' from this record model
        """
        return self.get_field_value(self.STORABLEITEMSCANMATCHFIELD__FIELD_NAME.field_name)

    def set_StorableItemStorageUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorableItemStorageUnits' on this record model
        """
        self.set_field_value(self.STORABLEITEMSTORAGEUNITS__FIELD_NAME.field_name, value)

    def get_StorableItemStorageUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorableItemStorageUnits' from this record model
        """
        return self.get_field_value(self.STORABLEITEMSTORAGEUNITS__FIELD_NAME.field_name)


class StorageEventModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type StorageEvent
    Data Type Display Name: Storage Event (Storage Events)
    Fields: DurationHours, DurationMinutes, EventDate, EventTime, EventType, StorageUnitId, StorageUnitPath, StorageUnitTemperature
    """
    DATA_TYPE_NAME: str = 'StorageEvent'
    DURATIONHOURS__FIELD_NAME: WrapperField = WrapperField("DurationHours", FieldType.SHORT)
    DURATIONMINUTES__FIELD_NAME: WrapperField = WrapperField("DurationMinutes", FieldType.SHORT)
    EVENTDATE__FIELD_NAME: WrapperField = WrapperField("EventDate", FieldType.DATE)
    EVENTTIME__FIELD_NAME: WrapperField = WrapperField("EventTime", FieldType.STRING)
    EVENTTYPE__FIELD_NAME: WrapperField = WrapperField("EventType", FieldType.PICKLIST)
    STORAGEUNITID__FIELD_NAME: WrapperField = WrapperField("StorageUnitId", FieldType.STRING)
    STORAGEUNITPATH__FIELD_NAME: WrapperField = WrapperField("StorageUnitPath", FieldType.STRING)
    STORAGEUNITTEMPERATURE__FIELD_NAME: WrapperField = WrapperField("StorageUnitTemperature", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DurationHours_field(self, value: Optional[int]):
        """
        Set data field with field name 'DurationHours' on this record model
        """
        self.set_field_value(self.DURATIONHOURS__FIELD_NAME.field_name, value)

    def get_DurationHours_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DurationHours' from this record model
        """
        return self.get_field_value(self.DURATIONHOURS__FIELD_NAME.field_name)

    def set_DurationMinutes_field(self, value: Optional[int]):
        """
        Set data field with field name 'DurationMinutes' on this record model
        """
        self.set_field_value(self.DURATIONMINUTES__FIELD_NAME.field_name, value)

    def get_DurationMinutes_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DurationMinutes' from this record model
        """
        return self.get_field_value(self.DURATIONMINUTES__FIELD_NAME.field_name)

    def set_EventDate_field(self, value: Optional[int]):
        """
        Set data field with field name 'EventDate' on this record model
        """
        self.set_field_value(self.EVENTDATE__FIELD_NAME.field_name, value)

    def get_EventDate_field(self) -> Optional[int]:
        """
        Get data field value with field name 'EventDate' from this record model
        """
        return self.get_field_value(self.EVENTDATE__FIELD_NAME.field_name)

    def set_EventTime_field(self, value: Optional[str]):
        """
        Set data field with field name 'EventTime' on this record model
        """
        self.set_field_value(self.EVENTTIME__FIELD_NAME.field_name, value)

    def get_EventTime_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EventTime' from this record model
        """
        return self.get_field_value(self.EVENTTIME__FIELD_NAME.field_name)

    def set_EventType_field(self, value: Optional[str]):
        """
        Set data field with field name 'EventType' on this record model
        """
        self.set_field_value(self.EVENTTYPE__FIELD_NAME.field_name, value)

    def get_EventType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EventType' from this record model
        """
        return self.get_field_value(self.EVENTTYPE__FIELD_NAME.field_name)

    def set_StorageUnitId_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitId' on this record model
        """
        self.set_field_value(self.STORAGEUNITID__FIELD_NAME.field_name, value)

    def get_StorageUnitId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitId' from this record model
        """
        return self.get_field_value(self.STORAGEUNITID__FIELD_NAME.field_name)

    def set_StorageUnitPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitPath' on this record model
        """
        self.set_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name, value)

    def get_StorageUnitPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitPath' from this record model
        """
        return self.get_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name)

    def set_StorageUnitTemperature_field(self, value: Optional[float]):
        """
        Set data field with field name 'StorageUnitTemperature' on this record model
        """
        self.set_field_value(self.STORAGEUNITTEMPERATURE__FIELD_NAME.field_name, value)

    def get_StorageUnitTemperature_field(self) -> Optional[float]:
        """
        Get data field value with field name 'StorageUnitTemperature' from this record model
        """
        return self.get_field_value(self.STORAGEUNITTEMPERATURE__FIELD_NAME.field_name)


class StorageHierarchyConfigModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type StorageHierarchyConfig
    Data Type Display Name: Storage Hierarchy Configuration (Storage Hierarchy Configurations)
    Fields: Hierarchy
    """
    DATA_TYPE_NAME: str = 'StorageHierarchyConfig'
    HIERARCHY__FIELD_NAME: WrapperField = WrapperField("Hierarchy", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Hierarchy_field(self, value: Optional[str]):
        """
        Set data field with field name 'Hierarchy' on this record model
        """
        self.set_field_value(self.HIERARCHY__FIELD_NAME.field_name, value)

    def get_Hierarchy_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Hierarchy' from this record model
        """
        return self.get_field_value(self.HIERARCHY__FIELD_NAME.field_name)


class StorageUnitModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type StorageUnit
    Data Type Display Name: Storage Unit (Storage Units)
    Fields: ColPosition, Humidity, OccupiedCount, RecomputeOccupancy, RowPosition, StorageUnitCapacity, StorageUnitId, StorageUnitPath, StorageUnitType, Temperature, UnitColumns, UnitRows
    """
    DATA_TYPE_NAME: str = 'StorageUnit'
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.STRING)
    HUMIDITY__FIELD_NAME: WrapperField = WrapperField("Humidity", FieldType.DOUBLE)
    OCCUPIEDCOUNT__FIELD_NAME: WrapperField = WrapperField("OccupiedCount", FieldType.LONG)
    RECOMPUTEOCCUPANCY__FIELD_NAME: WrapperField = WrapperField("RecomputeOccupancy", FieldType.ACTION)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.STRING)
    STORAGEUNITCAPACITY__FIELD_NAME: WrapperField = WrapperField("StorageUnitCapacity", FieldType.LONG)
    STORAGEUNITID__FIELD_NAME: WrapperField = WrapperField("StorageUnitId", FieldType.STRING)
    STORAGEUNITPATH__FIELD_NAME: WrapperField = WrapperField("StorageUnitPath", FieldType.STRING)
    STORAGEUNITTYPE__FIELD_NAME: WrapperField = WrapperField("StorageUnitType", FieldType.SELECTION)
    TEMPERATURE__FIELD_NAME: WrapperField = WrapperField("Temperature", FieldType.DOUBLE)
    UNITCOLUMNS__FIELD_NAME: WrapperField = WrapperField("UnitColumns", FieldType.LONG)
    UNITROWS__FIELD_NAME: WrapperField = WrapperField("UnitRows", FieldType.LONG)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_Humidity_field(self, value: Optional[float]):
        """
        Set data field with field name 'Humidity' on this record model
        """
        self.set_field_value(self.HUMIDITY__FIELD_NAME.field_name, value)

    def get_Humidity_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Humidity' from this record model
        """
        return self.get_field_value(self.HUMIDITY__FIELD_NAME.field_name)

    def set_OccupiedCount_field(self, value: Optional[int]):
        """
        Set data field with field name 'OccupiedCount' on this record model
        """
        self.set_field_value(self.OCCUPIEDCOUNT__FIELD_NAME.field_name, value)

    def get_OccupiedCount_field(self) -> Optional[int]:
        """
        Get data field value with field name 'OccupiedCount' from this record model
        """
        return self.get_field_value(self.OCCUPIEDCOUNT__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_StorageUnitCapacity_field(self, value: Optional[int]):
        """
        Set data field with field name 'StorageUnitCapacity' on this record model
        """
        self.set_field_value(self.STORAGEUNITCAPACITY__FIELD_NAME.field_name, value)

    def get_StorageUnitCapacity_field(self) -> Optional[int]:
        """
        Get data field value with field name 'StorageUnitCapacity' from this record model
        """
        return self.get_field_value(self.STORAGEUNITCAPACITY__FIELD_NAME.field_name)

    def set_StorageUnitId_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitId' on this record model
        """
        self.set_field_value(self.STORAGEUNITID__FIELD_NAME.field_name, value)

    def get_StorageUnitId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitId' from this record model
        """
        return self.get_field_value(self.STORAGEUNITID__FIELD_NAME.field_name)

    def set_StorageUnitPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitPath' on this record model
        """
        self.set_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name, value)

    def get_StorageUnitPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitPath' from this record model
        """
        return self.get_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name)

    def set_StorageUnitType_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitType' on this record model
        """
        self.set_field_value(self.STORAGEUNITTYPE__FIELD_NAME.field_name, value)

    def get_StorageUnitType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitType' from this record model
        """
        return self.get_field_value(self.STORAGEUNITTYPE__FIELD_NAME.field_name)

    def set_Temperature_field(self, value: Optional[float]):
        """
        Set data field with field name 'Temperature' on this record model
        """
        self.set_field_value(self.TEMPERATURE__FIELD_NAME.field_name, value)

    def get_Temperature_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Temperature' from this record model
        """
        return self.get_field_value(self.TEMPERATURE__FIELD_NAME.field_name)

    def set_UnitColumns_field(self, value: Optional[int]):
        """
        Set data field with field name 'UnitColumns' on this record model
        """
        self.set_field_value(self.UNITCOLUMNS__FIELD_NAME.field_name, value)

    def get_UnitColumns_field(self) -> Optional[int]:
        """
        Get data field value with field name 'UnitColumns' from this record model
        """
        return self.get_field_value(self.UNITCOLUMNS__FIELD_NAME.field_name)

    def set_UnitRows_field(self, value: Optional[int]):
        """
        Set data field with field name 'UnitRows' on this record model
        """
        self.set_field_value(self.UNITROWS__FIELD_NAME.field_name, value)

    def get_UnitRows_field(self) -> Optional[int]:
        """
        Get data field value with field name 'UnitRows' from this record model
        """
        return self.get_field_value(self.UNITROWS__FIELD_NAME.field_name)


class StudyModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Study
    Data Type Display Name: Study (Studies)
    Fields: Description, InheritRolesFromParent, InheritRolesFromProject, IsClinical, StudyId, StudyName, StudyType
    The Study Data Type
    """
    DATA_TYPE_NAME: str = 'Study'
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    INHERITROLESFROMPARENT__FIELD_NAME: WrapperField = WrapperField("InheritRolesFromParent", FieldType.BOOLEAN)
    INHERITROLESFROMPROJECT__FIELD_NAME: WrapperField = WrapperField("InheritRolesFromProject", FieldType.BOOLEAN)
    ISCLINICAL__FIELD_NAME: WrapperField = WrapperField("IsClinical", FieldType.BOOLEAN)
    STUDYID__FIELD_NAME: WrapperField = WrapperField("StudyId", FieldType.AUTO_ACCESSION)
    STUDYNAME__FIELD_NAME: WrapperField = WrapperField("StudyName", FieldType.STRING)
    STUDYTYPE__FIELD_NAME: WrapperField = WrapperField("StudyType", FieldType.PICKLIST)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_InheritRolesFromParent_field(self, value: Optional[bool]):
        """
        Set data field with field name 'InheritRolesFromParent' on this record model
        """
        self.set_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name, value)

    def get_InheritRolesFromParent_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'InheritRolesFromParent' from this record model
        """
        return self.get_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name)

    def set_InheritRolesFromProject_field(self, value: Optional[bool]):
        """
        Set data field with field name 'InheritRolesFromProject' on this record model
        """
        self.set_field_value(self.INHERITROLESFROMPROJECT__FIELD_NAME.field_name, value)

    def get_InheritRolesFromProject_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'InheritRolesFromProject' from this record model
        """
        return self.get_field_value(self.INHERITROLESFROMPROJECT__FIELD_NAME.field_name)

    def set_IsClinical_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsClinical' on this record model
        """
        self.set_field_value(self.ISCLINICAL__FIELD_NAME.field_name, value)

    def get_IsClinical_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsClinical' from this record model
        """
        return self.get_field_value(self.ISCLINICAL__FIELD_NAME.field_name)

    def set_StudyId_field(self, value: Optional[str]):
        """
        Set data field with field name 'StudyId' on this record model
        """
        self.set_field_value(self.STUDYID__FIELD_NAME.field_name, value)

    def get_StudyId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StudyId' from this record model
        """
        return self.get_field_value(self.STUDYID__FIELD_NAME.field_name)

    def set_StudyName_field(self, value: Optional[str]):
        """
        Set data field with field name 'StudyName' on this record model
        """
        self.set_field_value(self.STUDYNAME__FIELD_NAME.field_name, value)

    def get_StudyName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StudyName' from this record model
        """
        return self.get_field_value(self.STUDYNAME__FIELD_NAME.field_name)

    def set_StudyType_field(self, value: Optional[str]):
        """
        Set data field with field name 'StudyType' on this record model
        """
        self.set_field_value(self.STUDYTYPE__FIELD_NAME.field_name, value)

    def get_StudyType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StudyType' from this record model
        """
        return self.get_field_value(self.STUDYTYPE__FIELD_NAME.field_name)


class SubjectModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type Subject
    Data Type Display Name: Subject (Subjects)
    Fields: Age, BodyMass, BodyMassUnits, ColPosition, DateOfBirth, Gender, Height, RowPosition, Site, Species, StorageLocationBarcode, StorageUnitPath, Strain, SubjectCondition, SubjectId, SubjectName, SubjectStatus, Vendor, Weight
    """
    DATA_TYPE_NAME: str = 'Subject'
    AGE__FIELD_NAME: WrapperField = WrapperField("Age", FieldType.DOUBLE)
    BODYMASS__FIELD_NAME: WrapperField = WrapperField("BodyMass", FieldType.DOUBLE)
    BODYMASSUNITS__FIELD_NAME: WrapperField = WrapperField("BodyMassUnits", FieldType.PICKLIST)
    COLPOSITION__FIELD_NAME: WrapperField = WrapperField("ColPosition", FieldType.SELECTION)
    DATEOFBIRTH__FIELD_NAME: WrapperField = WrapperField("DateOfBirth", FieldType.DATE)
    GENDER__FIELD_NAME: WrapperField = WrapperField("Gender", FieldType.SELECTION)
    HEIGHT__FIELD_NAME: WrapperField = WrapperField("Height", FieldType.DOUBLE)
    ROWPOSITION__FIELD_NAME: WrapperField = WrapperField("RowPosition", FieldType.SELECTION)
    SITE__FIELD_NAME: WrapperField = WrapperField("Site", FieldType.PICKLIST)
    SPECIES__FIELD_NAME: WrapperField = WrapperField("Species", FieldType.PICKLIST)
    STORAGELOCATIONBARCODE__FIELD_NAME: WrapperField = WrapperField("StorageLocationBarcode", FieldType.SELECTION)
    STORAGEUNITPATH__FIELD_NAME: WrapperField = WrapperField("StorageUnitPath", FieldType.STRING)
    STRAIN__FIELD_NAME: WrapperField = WrapperField("Strain", FieldType.SELECTION)
    SUBJECTCONDITION__FIELD_NAME: WrapperField = WrapperField("SubjectCondition", FieldType.SELECTION)
    SUBJECTID__FIELD_NAME: WrapperField = WrapperField("SubjectId", FieldType.AUTO_ACCESSION)
    SUBJECTNAME__FIELD_NAME: WrapperField = WrapperField("SubjectName", FieldType.STRING)
    SUBJECTSTATUS__FIELD_NAME: WrapperField = WrapperField("SubjectStatus", FieldType.PICKLIST)
    VENDOR__FIELD_NAME: WrapperField = WrapperField("Vendor", FieldType.STRING)
    WEIGHT__FIELD_NAME: WrapperField = WrapperField("Weight", FieldType.DOUBLE)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Age_field(self, value: Optional[float]):
        """
        Set data field with field name 'Age' on this record model
        """
        self.set_field_value(self.AGE__FIELD_NAME.field_name, value)

    def get_Age_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Age' from this record model
        """
        return self.get_field_value(self.AGE__FIELD_NAME.field_name)

    def set_BodyMass_field(self, value: Optional[float]):
        """
        Set data field with field name 'BodyMass' on this record model
        """
        self.set_field_value(self.BODYMASS__FIELD_NAME.field_name, value)

    def get_BodyMass_field(self) -> Optional[float]:
        """
        Get data field value with field name 'BodyMass' from this record model
        """
        return self.get_field_value(self.BODYMASS__FIELD_NAME.field_name)

    def set_BodyMassUnits_field(self, value: Optional[str]):
        """
        Set data field with field name 'BodyMassUnits' on this record model
        """
        self.set_field_value(self.BODYMASSUNITS__FIELD_NAME.field_name, value)

    def get_BodyMassUnits_field(self) -> Optional[str]:
        """
        Get data field value with field name 'BodyMassUnits' from this record model
        """
        return self.get_field_value(self.BODYMASSUNITS__FIELD_NAME.field_name)

    def set_ColPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'ColPosition' on this record model
        """
        self.set_field_value(self.COLPOSITION__FIELD_NAME.field_name, value)

    def get_ColPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ColPosition' from this record model
        """
        return self.get_field_value(self.COLPOSITION__FIELD_NAME.field_name)

    def set_DateOfBirth_field(self, value: Optional[int]):
        """
        Set data field with field name 'DateOfBirth' on this record model
        """
        self.set_field_value(self.DATEOFBIRTH__FIELD_NAME.field_name, value)

    def get_DateOfBirth_field(self) -> Optional[int]:
        """
        Get data field value with field name 'DateOfBirth' from this record model
        """
        return self.get_field_value(self.DATEOFBIRTH__FIELD_NAME.field_name)

    def set_Gender_field(self, value: Optional[str]):
        """
        Set data field with field name 'Gender' on this record model
        """
        self.set_field_value(self.GENDER__FIELD_NAME.field_name, value)

    def get_Gender_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Gender' from this record model
        """
        return self.get_field_value(self.GENDER__FIELD_NAME.field_name)

    def set_Height_field(self, value: Optional[float]):
        """
        Set data field with field name 'Height' on this record model
        """
        self.set_field_value(self.HEIGHT__FIELD_NAME.field_name, value)

    def get_Height_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Height' from this record model
        """
        return self.get_field_value(self.HEIGHT__FIELD_NAME.field_name)

    def set_RowPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'RowPosition' on this record model
        """
        self.set_field_value(self.ROWPOSITION__FIELD_NAME.field_name, value)

    def get_RowPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'RowPosition' from this record model
        """
        return self.get_field_value(self.ROWPOSITION__FIELD_NAME.field_name)

    def set_Site_field(self, value: Optional[str]):
        """
        Set data field with field name 'Site' on this record model
        """
        self.set_field_value(self.SITE__FIELD_NAME.field_name, value)

    def get_Site_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Site' from this record model
        """
        return self.get_field_value(self.SITE__FIELD_NAME.field_name)

    def set_Species_field(self, value: Optional[str]):
        """
        Set data field with field name 'Species' on this record model
        """
        self.set_field_value(self.SPECIES__FIELD_NAME.field_name, value)

    def get_Species_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Species' from this record model
        """
        return self.get_field_value(self.SPECIES__FIELD_NAME.field_name)

    def set_StorageLocationBarcode_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageLocationBarcode' on this record model
        """
        self.set_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name, value)

    def get_StorageLocationBarcode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageLocationBarcode' from this record model
        """
        return self.get_field_value(self.STORAGELOCATIONBARCODE__FIELD_NAME.field_name)

    def set_StorageUnitPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'StorageUnitPath' on this record model
        """
        self.set_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name, value)

    def get_StorageUnitPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'StorageUnitPath' from this record model
        """
        return self.get_field_value(self.STORAGEUNITPATH__FIELD_NAME.field_name)

    def set_Strain_field(self, value: Optional[str]):
        """
        Set data field with field name 'Strain' on this record model
        """
        self.set_field_value(self.STRAIN__FIELD_NAME.field_name, value)

    def get_Strain_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Strain' from this record model
        """
        return self.get_field_value(self.STRAIN__FIELD_NAME.field_name)

    def set_SubjectCondition_field(self, value: Optional[str]):
        """
        Set data field with field name 'SubjectCondition' on this record model
        """
        self.set_field_value(self.SUBJECTCONDITION__FIELD_NAME.field_name, value)

    def get_SubjectCondition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SubjectCondition' from this record model
        """
        return self.get_field_value(self.SUBJECTCONDITION__FIELD_NAME.field_name)

    def set_SubjectId_field(self, value: Optional[str]):
        """
        Set data field with field name 'SubjectId' on this record model
        """
        self.set_field_value(self.SUBJECTID__FIELD_NAME.field_name, value)

    def get_SubjectId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SubjectId' from this record model
        """
        return self.get_field_value(self.SUBJECTID__FIELD_NAME.field_name)

    def set_SubjectName_field(self, value: Optional[str]):
        """
        Set data field with field name 'SubjectName' on this record model
        """
        self.set_field_value(self.SUBJECTNAME__FIELD_NAME.field_name, value)

    def get_SubjectName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SubjectName' from this record model
        """
        return self.get_field_value(self.SUBJECTNAME__FIELD_NAME.field_name)

    def set_SubjectStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'SubjectStatus' on this record model
        """
        self.set_field_value(self.SUBJECTSTATUS__FIELD_NAME.field_name, value)

    def get_SubjectStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'SubjectStatus' from this record model
        """
        return self.get_field_value(self.SUBJECTSTATUS__FIELD_NAME.field_name)

    def set_Vendor_field(self, value: Optional[str]):
        """
        Set data field with field name 'Vendor' on this record model
        """
        self.set_field_value(self.VENDOR__FIELD_NAME.field_name, value)

    def get_Vendor_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Vendor' from this record model
        """
        return self.get_field_value(self.VENDOR__FIELD_NAME.field_name)

    def set_Weight_field(self, value: Optional[float]):
        """
        Set data field with field name 'Weight' on this record model
        """
        self.set_field_value(self.WEIGHT__FIELD_NAME.field_name, value)

    def get_Weight_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Weight' from this record model
        """
        return self.get_field_value(self.WEIGHT__FIELD_NAME.field_name)


class TemplateWellModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type TemplateWell
    Data Type Display Name: Template Plate Well (Template Plate Wells)
    Fields: WellPosition
    """
    DATA_TYPE_NAME: str = 'TemplateWell'
    WELLPOSITION__FIELD_NAME: WrapperField = WrapperField("WellPosition", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_WellPosition_field(self, value: Optional[str]):
        """
        Set data field with field name 'WellPosition' on this record model
        """
        self.set_field_value(self.WELLPOSITION__FIELD_NAME.field_name, value)

    def get_WellPosition_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WellPosition' from this record model
        """
        return self.get_field_value(self.WELLPOSITION__FIELD_NAME.field_name)


class VeloxAppRecordModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type VeloxAppRecord
    Data Type Display Name: Organization Details (Organization Details)
    Fields: Address1, Address2, City, CompanyDescription, CompanyName, CompanyWebsite, Country, PostalCode, Region, State, VeloxPublicUrl
    This data type includes exactly one data record about the application's info.This data type is protected. Only system admins and portal admins can modify. This datatype cannot have any parents.
    """
    DATA_TYPE_NAME: str = 'VeloxAppRecord'
    ADDRESS1__FIELD_NAME: WrapperField = WrapperField("Address1", FieldType.STRING)
    ADDRESS2__FIELD_NAME: WrapperField = WrapperField("Address2", FieldType.STRING)
    CITY__FIELD_NAME: WrapperField = WrapperField("City", FieldType.STRING)
    COMPANYDESCRIPTION__FIELD_NAME: WrapperField = WrapperField("CompanyDescription", FieldType.STRING)
    COMPANYNAME__FIELD_NAME: WrapperField = WrapperField("CompanyName", FieldType.STRING)
    COMPANYWEBSITE__FIELD_NAME: WrapperField = WrapperField("CompanyWebsite", FieldType.STRING)
    COUNTRY__FIELD_NAME: WrapperField = WrapperField("Country", FieldType.STRING)
    POSTALCODE__FIELD_NAME: WrapperField = WrapperField("PostalCode", FieldType.STRING)
    REGION__FIELD_NAME: WrapperField = WrapperField("Region", FieldType.STRING)
    STATE__FIELD_NAME: WrapperField = WrapperField("State", FieldType.STRING)
    VELOXPUBLICURL__FIELD_NAME: WrapperField = WrapperField("VeloxPublicUrl", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Address1_field(self, value: Optional[str]):
        """
        Set data field with field name 'Address1' on this record model
        """
        self.set_field_value(self.ADDRESS1__FIELD_NAME.field_name, value)

    def get_Address1_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Address1' from this record model
        """
        return self.get_field_value(self.ADDRESS1__FIELD_NAME.field_name)

    def set_Address2_field(self, value: Optional[str]):
        """
        Set data field with field name 'Address2' on this record model
        """
        self.set_field_value(self.ADDRESS2__FIELD_NAME.field_name, value)

    def get_Address2_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Address2' from this record model
        """
        return self.get_field_value(self.ADDRESS2__FIELD_NAME.field_name)

    def set_City_field(self, value: Optional[str]):
        """
        Set data field with field name 'City' on this record model
        """
        self.set_field_value(self.CITY__FIELD_NAME.field_name, value)

    def get_City_field(self) -> Optional[str]:
        """
        Get data field value with field name 'City' from this record model
        """
        return self.get_field_value(self.CITY__FIELD_NAME.field_name)

    def set_CompanyDescription_field(self, value: Optional[str]):
        """
        Set data field with field name 'CompanyDescription' on this record model
        """
        self.set_field_value(self.COMPANYDESCRIPTION__FIELD_NAME.field_name, value)

    def get_CompanyDescription_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CompanyDescription' from this record model
        """
        return self.get_field_value(self.COMPANYDESCRIPTION__FIELD_NAME.field_name)

    def set_CompanyName_field(self, value: Optional[str]):
        """
        Set data field with field name 'CompanyName' on this record model
        """
        self.set_field_value(self.COMPANYNAME__FIELD_NAME.field_name, value)

    def get_CompanyName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CompanyName' from this record model
        """
        return self.get_field_value(self.COMPANYNAME__FIELD_NAME.field_name)

    def set_CompanyWebsite_field(self, value: Optional[str]):
        """
        Set data field with field name 'CompanyWebsite' on this record model
        """
        self.set_field_value(self.COMPANYWEBSITE__FIELD_NAME.field_name, value)

    def get_CompanyWebsite_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CompanyWebsite' from this record model
        """
        return self.get_field_value(self.COMPANYWEBSITE__FIELD_NAME.field_name)

    def set_Country_field(self, value: Optional[str]):
        """
        Set data field with field name 'Country' on this record model
        """
        self.set_field_value(self.COUNTRY__FIELD_NAME.field_name, value)

    def get_Country_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Country' from this record model
        """
        return self.get_field_value(self.COUNTRY__FIELD_NAME.field_name)

    def set_PostalCode_field(self, value: Optional[str]):
        """
        Set data field with field name 'PostalCode' on this record model
        """
        self.set_field_value(self.POSTALCODE__FIELD_NAME.field_name, value)

    def get_PostalCode_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PostalCode' from this record model
        """
        return self.get_field_value(self.POSTALCODE__FIELD_NAME.field_name)

    def set_Region_field(self, value: Optional[str]):
        """
        Set data field with field name 'Region' on this record model
        """
        self.set_field_value(self.REGION__FIELD_NAME.field_name, value)

    def get_Region_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Region' from this record model
        """
        return self.get_field_value(self.REGION__FIELD_NAME.field_name)

    def set_State_field(self, value: Optional[str]):
        """
        Set data field with field name 'State' on this record model
        """
        self.set_field_value(self.STATE__FIELD_NAME.field_name, value)

    def get_State_field(self) -> Optional[str]:
        """
        Get data field value with field name 'State' from this record model
        """
        return self.get_field_value(self.STATE__FIELD_NAME.field_name)

    def set_VeloxPublicUrl_field(self, value: Optional[str]):
        """
        Set data field with field name 'VeloxPublicUrl' on this record model
        """
        self.set_field_value(self.VELOXPUBLICURL__FIELD_NAME.field_name, value)

    def get_VeloxPublicUrl_field(self) -> Optional[str]:
        """
        Get data field value with field name 'VeloxPublicUrl' from this record model
        """
        return self.get_field_value(self.VELOXPUBLICURL__FIELD_NAME.field_name)


class VeloxCsvExportModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type VeloxCsvExport
    Data Type Display Name: CSV Export (CSV Exports)
    Fields: CsvExportReportExecutionId, CsvExportSourceTempTypePojo, Description, ExportStatus, FilePath, VeloxCurrentVersion
    This data type is used to store the file created when exporting a table to a CSV from anywhere in the system.
    """
    DATA_TYPE_NAME: str = 'VeloxCsvExport'
    CSVEXPORTREPORTEXECUTIONID__FIELD_NAME: WrapperField = WrapperField("CsvExportReportExecutionId", FieldType.STRING)
    CSVEXPORTSOURCETEMPTYPEPOJO__FIELD_NAME: WrapperField = WrapperField("CsvExportSourceTempTypePojo", FieldType.STRING)
    DESCRIPTION__FIELD_NAME: WrapperField = WrapperField("Description", FieldType.STRING)
    EXPORTSTATUS__FIELD_NAME: WrapperField = WrapperField("ExportStatus", FieldType.STRING)
    FILEPATH__FIELD_NAME: WrapperField = WrapperField("FilePath", FieldType.STRING)
    VELOXCURRENTVERSION__FIELD_NAME: WrapperField = WrapperField("VeloxCurrentVersion", FieldType.INTEGER)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_CsvExportReportExecutionId_field(self, value: Optional[str]):
        """
        Set data field with field name 'CsvExportReportExecutionId' on this record model
        """
        self.set_field_value(self.CSVEXPORTREPORTEXECUTIONID__FIELD_NAME.field_name, value)

    def get_CsvExportReportExecutionId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CsvExportReportExecutionId' from this record model
        """
        return self.get_field_value(self.CSVEXPORTREPORTEXECUTIONID__FIELD_NAME.field_name)

    def set_CsvExportSourceTempTypePojo_field(self, value: Optional[str]):
        """
        Set data field with field name 'CsvExportSourceTempTypePojo' on this record model
        """
        self.set_field_value(self.CSVEXPORTSOURCETEMPTYPEPOJO__FIELD_NAME.field_name, value)

    def get_CsvExportSourceTempTypePojo_field(self) -> Optional[str]:
        """
        Get data field value with field name 'CsvExportSourceTempTypePojo' from this record model
        """
        return self.get_field_value(self.CSVEXPORTSOURCETEMPTYPEPOJO__FIELD_NAME.field_name)

    def set_Description_field(self, value: Optional[str]):
        """
        Set data field with field name 'Description' on this record model
        """
        self.set_field_value(self.DESCRIPTION__FIELD_NAME.field_name, value)

    def get_Description_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Description' from this record model
        """
        return self.get_field_value(self.DESCRIPTION__FIELD_NAME.field_name)

    def set_ExportStatus_field(self, value: Optional[str]):
        """
        Set data field with field name 'ExportStatus' on this record model
        """
        self.set_field_value(self.EXPORTSTATUS__FIELD_NAME.field_name, value)

    def get_ExportStatus_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ExportStatus' from this record model
        """
        return self.get_field_value(self.EXPORTSTATUS__FIELD_NAME.field_name)

    def set_FilePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'FilePath' on this record model
        """
        self.set_field_value(self.FILEPATH__FIELD_NAME.field_name, value)

    def get_FilePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FilePath' from this record model
        """
        return self.get_field_value(self.FILEPATH__FIELD_NAME.field_name)

    def set_VeloxCurrentVersion_field(self, value: Optional[int]):
        """
        Set data field with field name 'VeloxCurrentVersion' on this record model
        """
        self.set_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name, value)

    def get_VeloxCurrentVersion_field(self) -> Optional[int]:
        """
        Get data field value with field name 'VeloxCurrentVersion' from this record model
        """
        return self.get_field_value(self.VELOXCURRENTVERSION__FIELD_NAME.field_name)


class VeloxDepartmentModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type VeloxDepartment
    Data Type Display Name: Department (Departments)
    Fields: DepartmentName, InheritRolesFromParent
    """
    DATA_TYPE_NAME: str = 'VeloxDepartment'
    DEPARTMENTNAME__FIELD_NAME: WrapperField = WrapperField("DepartmentName", FieldType.STRING)
    INHERITROLESFROMPARENT__FIELD_NAME: WrapperField = WrapperField("InheritRolesFromParent", FieldType.BOOLEAN)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_DepartmentName_field(self, value: Optional[str]):
        """
        Set data field with field name 'DepartmentName' on this record model
        """
        self.set_field_value(self.DEPARTMENTNAME__FIELD_NAME.field_name, value)

    def get_DepartmentName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DepartmentName' from this record model
        """
        return self.get_field_value(self.DEPARTMENTNAME__FIELD_NAME.field_name)

    def set_InheritRolesFromParent_field(self, value: Optional[bool]):
        """
        Set data field with field name 'InheritRolesFromParent' on this record model
        """
        self.set_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name, value)

    def get_InheritRolesFromParent_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'InheritRolesFromParent' from this record model
        """
        return self.get_field_value(self.INHERITROLESFROMPARENT__FIELD_NAME.field_name)


class VeloxLocationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type VeloxLocation
    Data Type Display Name: Location (Locations)
    Fields: LocationName
    """
    DATA_TYPE_NAME: str = 'VeloxLocation'
    LOCATIONNAME__FIELD_NAME: WrapperField = WrapperField("LocationName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_LocationName_field(self, value: Optional[str]):
        """
        Set data field with field name 'LocationName' on this record model
        """
        self.set_field_value(self.LOCATIONNAME__FIELD_NAME.field_name, value)

    def get_LocationName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LocationName' from this record model
        """
        return self.get_field_value(self.LOCATIONNAME__FIELD_NAME.field_name)


class VeloxUserModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type VeloxUser
    Data Type Display Name: User (Users)
    Fields: EmailAddress, FirstName, JobTitle, LastName, MiddleName, Username
    Data type to represent each user in the system.  These records can be searched using api methods and CustomReports but cannot be edited like typical records.
    """
    DATA_TYPE_NAME: str = 'VeloxUser'
    EMAILADDRESS__FIELD_NAME: WrapperField = WrapperField("EmailAddress", FieldType.STRING)
    FIRSTNAME__FIELD_NAME: WrapperField = WrapperField("FirstName", FieldType.STRING)
    JOBTITLE__FIELD_NAME: WrapperField = WrapperField("JobTitle", FieldType.STRING)
    LASTNAME__FIELD_NAME: WrapperField = WrapperField("LastName", FieldType.STRING)
    MIDDLENAME__FIELD_NAME: WrapperField = WrapperField("MiddleName", FieldType.STRING)
    USERNAME__FIELD_NAME: WrapperField = WrapperField("Username", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_EmailAddress_field(self, value: Optional[str]):
        """
        Set data field with field name 'EmailAddress' on this record model
        """
        self.set_field_value(self.EMAILADDRESS__FIELD_NAME.field_name, value)

    def get_EmailAddress_field(self) -> Optional[str]:
        """
        Get data field value with field name 'EmailAddress' from this record model
        """
        return self.get_field_value(self.EMAILADDRESS__FIELD_NAME.field_name)

    def set_FirstName_field(self, value: Optional[str]):
        """
        Set data field with field name 'FirstName' on this record model
        """
        self.set_field_value(self.FIRSTNAME__FIELD_NAME.field_name, value)

    def get_FirstName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'FirstName' from this record model
        """
        return self.get_field_value(self.FIRSTNAME__FIELD_NAME.field_name)

    def set_JobTitle_field(self, value: Optional[str]):
        """
        Set data field with field name 'JobTitle' on this record model
        """
        self.set_field_value(self.JOBTITLE__FIELD_NAME.field_name, value)

    def get_JobTitle_field(self) -> Optional[str]:
        """
        Get data field value with field name 'JobTitle' from this record model
        """
        return self.get_field_value(self.JOBTITLE__FIELD_NAME.field_name)

    def set_LastName_field(self, value: Optional[str]):
        """
        Set data field with field name 'LastName' on this record model
        """
        self.set_field_value(self.LASTNAME__FIELD_NAME.field_name, value)

    def get_LastName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'LastName' from this record model
        """
        return self.get_field_value(self.LASTNAME__FIELD_NAME.field_name)

    def set_MiddleName_field(self, value: Optional[str]):
        """
        Set data field with field name 'MiddleName' on this record model
        """
        self.set_field_value(self.MIDDLENAME__FIELD_NAME.field_name, value)

    def get_MiddleName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'MiddleName' from this record model
        """
        return self.get_field_value(self.MIDDLENAME__FIELD_NAME.field_name)

    def set_Username_field(self, value: Optional[str]):
        """
        Set data field with field name 'Username' on this record model
        """
        self.set_field_value(self.USERNAME__FIELD_NAME.field_name, value)

    def get_Username_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Username' from this record model
        """
        return self.get_field_value(self.USERNAME__FIELD_NAME.field_name)


class WellElementModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type WellElement
    Data Type Display Name: Well Element (Well Elements)
    Fields: Amount, ControlType, ElementId, isControl, Layer, MultiParentLink137, MultiParentLink207, Notes, Required, TimePoint, UnitOfMeasure, WellElementDataType, WellElementFilterField, WellElementSubType
    """
    DATA_TYPE_NAME: str = 'WellElement'
    AMOUNT__FIELD_NAME: WrapperField = WrapperField("Amount", FieldType.DOUBLE)
    CONTROLTYPE__FIELD_NAME: WrapperField = WrapperField("ControlType", FieldType.STRING)
    ELEMENTID__FIELD_NAME: WrapperField = WrapperField("ElementId", FieldType.STRING)
    ISCONTROL__FIELD_NAME: WrapperField = WrapperField("isControl", FieldType.BOOLEAN)
    LAYER__FIELD_NAME: WrapperField = WrapperField("Layer", FieldType.INTEGER)
    MULTIPARENTLINK137__FIELD_NAME: WrapperField = WrapperField("MultiParentLink137", FieldType.MULTIPARENTLINK)
    MULTIPARENTLINK207__FIELD_NAME: WrapperField = WrapperField("MultiParentLink207", FieldType.MULTIPARENTLINK)
    NOTES__FIELD_NAME: WrapperField = WrapperField("Notes", FieldType.STRING)
    REQUIRED__FIELD_NAME: WrapperField = WrapperField("Required", FieldType.BOOLEAN)
    TIMEPOINT__FIELD_NAME: WrapperField = WrapperField("TimePoint", FieldType.STRING)
    UNITOFMEASURE__FIELD_NAME: WrapperField = WrapperField("UnitOfMeasure", FieldType.PICKLIST)
    WELLELEMENTDATATYPE__FIELD_NAME: WrapperField = WrapperField("WellElementDataType", FieldType.STRING)
    WELLELEMENTFILTERFIELD__FIELD_NAME: WrapperField = WrapperField("WellElementFilterField", FieldType.STRING)
    WELLELEMENTSUBTYPE__FIELD_NAME: WrapperField = WrapperField("WellElementSubType", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_Amount_field(self, value: Optional[float]):
        """
        Set data field with field name 'Amount' on this record model
        """
        self.set_field_value(self.AMOUNT__FIELD_NAME.field_name, value)

    def get_Amount_field(self) -> Optional[float]:
        """
        Get data field value with field name 'Amount' from this record model
        """
        return self.get_field_value(self.AMOUNT__FIELD_NAME.field_name)

    def set_ControlType_field(self, value: Optional[str]):
        """
        Set data field with field name 'ControlType' on this record model
        """
        self.set_field_value(self.CONTROLTYPE__FIELD_NAME.field_name, value)

    def get_ControlType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ControlType' from this record model
        """
        return self.get_field_value(self.CONTROLTYPE__FIELD_NAME.field_name)

    def set_ElementId_field(self, value: Optional[str]):
        """
        Set data field with field name 'ElementId' on this record model
        """
        self.set_field_value(self.ELEMENTID__FIELD_NAME.field_name, value)

    def get_ElementId_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ElementId' from this record model
        """
        return self.get_field_value(self.ELEMENTID__FIELD_NAME.field_name)

    def set_isControl_field(self, value: Optional[bool]):
        """
        Set data field with field name 'isControl' on this record model
        """
        self.set_field_value(self.ISCONTROL__FIELD_NAME.field_name, value)

    def get_isControl_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'isControl' from this record model
        """
        return self.get_field_value(self.ISCONTROL__FIELD_NAME.field_name)

    def set_Layer_field(self, value: Optional[int]):
        """
        Set data field with field name 'Layer' on this record model
        """
        self.set_field_value(self.LAYER__FIELD_NAME.field_name, value)

    def get_Layer_field(self) -> Optional[int]:
        """
        Get data field value with field name 'Layer' from this record model
        """
        return self.get_field_value(self.LAYER__FIELD_NAME.field_name)

    def set_Notes_field(self, value: Optional[str]):
        """
        Set data field with field name 'Notes' on this record model
        """
        self.set_field_value(self.NOTES__FIELD_NAME.field_name, value)

    def get_Notes_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Notes' from this record model
        """
        return self.get_field_value(self.NOTES__FIELD_NAME.field_name)

    def set_Required_field(self, value: Optional[bool]):
        """
        Set data field with field name 'Required' on this record model
        """
        self.set_field_value(self.REQUIRED__FIELD_NAME.field_name, value)

    def get_Required_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'Required' from this record model
        """
        return self.get_field_value(self.REQUIRED__FIELD_NAME.field_name)

    def set_TimePoint_field(self, value: Optional[str]):
        """
        Set data field with field name 'TimePoint' on this record model
        """
        self.set_field_value(self.TIMEPOINT__FIELD_NAME.field_name, value)

    def get_TimePoint_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TimePoint' from this record model
        """
        return self.get_field_value(self.TIMEPOINT__FIELD_NAME.field_name)

    def set_UnitOfMeasure_field(self, value: Optional[str]):
        """
        Set data field with field name 'UnitOfMeasure' on this record model
        """
        self.set_field_value(self.UNITOFMEASURE__FIELD_NAME.field_name, value)

    def get_UnitOfMeasure_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UnitOfMeasure' from this record model
        """
        return self.get_field_value(self.UNITOFMEASURE__FIELD_NAME.field_name)

    def set_WellElementDataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'WellElementDataType' on this record model
        """
        self.set_field_value(self.WELLELEMENTDATATYPE__FIELD_NAME.field_name, value)

    def get_WellElementDataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WellElementDataType' from this record model
        """
        return self.get_field_value(self.WELLELEMENTDATATYPE__FIELD_NAME.field_name)

    def set_WellElementFilterField_field(self, value: Optional[str]):
        """
        Set data field with field name 'WellElementFilterField' on this record model
        """
        self.set_field_value(self.WELLELEMENTFILTERFIELD__FIELD_NAME.field_name, value)

    def get_WellElementFilterField_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WellElementFilterField' from this record model
        """
        return self.get_field_value(self.WELLELEMENTFILTERFIELD__FIELD_NAME.field_name)

    def set_WellElementSubType_field(self, value: Optional[str]):
        """
        Set data field with field name 'WellElementSubType' on this record model
        """
        self.set_field_value(self.WELLELEMENTSUBTYPE__FIELD_NAME.field_name, value)

    def get_WellElementSubType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WellElementSubType' from this record model
        """
        return self.get_field_value(self.WELLELEMENTSUBTYPE__FIELD_NAME.field_name)


class WorkQueueButtonConfigurationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type WorkQueueButtonConfiguration
    Data Type Display Name: Work Queue Button Configuration (Work Queue Button Configurations)
    Fields: ButtonName, DataType, Line2Text, NoSelectionRequired, PackagePath, ViewUploadImageButton
    """
    DATA_TYPE_NAME: str = 'WorkQueueButtonConfiguration'
    BUTTONNAME__FIELD_NAME: WrapperField = WrapperField("ButtonName", FieldType.STRING)
    DATATYPE__FIELD_NAME: WrapperField = WrapperField("DataType", FieldType.SELECTION)
    LINE2TEXT__FIELD_NAME: WrapperField = WrapperField("Line2Text", FieldType.STRING)
    NOSELECTIONREQUIRED__FIELD_NAME: WrapperField = WrapperField("NoSelectionRequired", FieldType.BOOLEAN)
    PACKAGEPATH__FIELD_NAME: WrapperField = WrapperField("PackagePath", FieldType.STRING)
    VIEWUPLOADIMAGEBUTTON__FIELD_NAME: WrapperField = WrapperField("ViewUploadImageButton", FieldType.ACTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_ButtonName_field(self, value: Optional[str]):
        """
        Set data field with field name 'ButtonName' on this record model
        """
        self.set_field_value(self.BUTTONNAME__FIELD_NAME.field_name, value)

    def get_ButtonName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ButtonName' from this record model
        """
        return self.get_field_value(self.BUTTONNAME__FIELD_NAME.field_name)

    def set_DataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataType' on this record model
        """
        self.set_field_value(self.DATATYPE__FIELD_NAME.field_name, value)

    def get_DataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataType' from this record model
        """
        return self.get_field_value(self.DATATYPE__FIELD_NAME.field_name)

    def set_Line2Text_field(self, value: Optional[str]):
        """
        Set data field with field name 'Line2Text' on this record model
        """
        self.set_field_value(self.LINE2TEXT__FIELD_NAME.field_name, value)

    def get_Line2Text_field(self) -> Optional[str]:
        """
        Get data field value with field name 'Line2Text' from this record model
        """
        return self.get_field_value(self.LINE2TEXT__FIELD_NAME.field_name)

    def set_NoSelectionRequired_field(self, value: Optional[bool]):
        """
        Set data field with field name 'NoSelectionRequired' on this record model
        """
        self.set_field_value(self.NOSELECTIONREQUIRED__FIELD_NAME.field_name, value)

    def get_NoSelectionRequired_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'NoSelectionRequired' from this record model
        """
        return self.get_field_value(self.NOSELECTIONREQUIRED__FIELD_NAME.field_name)

    def set_PackagePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'PackagePath' on this record model
        """
        self.set_field_value(self.PACKAGEPATH__FIELD_NAME.field_name, value)

    def get_PackagePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'PackagePath' from this record model
        """
        return self.get_field_value(self.PACKAGEPATH__FIELD_NAME.field_name)


class WorkQueueDataTypeConfigurationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type WorkQueueDataTypeConfiguration
    Data Type Display Name: Work Queue Data Type Configuration (Work Queue Data Type Configurations)
    Fields: BatchRetrieval, DataType, DoubleClickActionPluginPath, IsReportBacked, ItemQueuePackagePath, ShowDefaultButtons, UseSingleSelection
    """
    DATA_TYPE_NAME: str = 'WorkQueueDataTypeConfiguration'
    BATCHRETRIEVAL__FIELD_NAME: WrapperField = WrapperField("BatchRetrieval", FieldType.BOOLEAN)
    DATATYPE__FIELD_NAME: WrapperField = WrapperField("DataType", FieldType.SELECTION)
    DOUBLECLICKACTIONPLUGINPATH__FIELD_NAME: WrapperField = WrapperField("DoubleClickActionPluginPath", FieldType.STRING)
    ISREPORTBACKED__FIELD_NAME: WrapperField = WrapperField("IsReportBacked", FieldType.BOOLEAN)
    ITEMQUEUEPACKAGEPATH__FIELD_NAME: WrapperField = WrapperField("ItemQueuePackagePath", FieldType.STRING)
    SHOWDEFAULTBUTTONS__FIELD_NAME: WrapperField = WrapperField("ShowDefaultButtons", FieldType.BOOLEAN)
    USESINGLESELECTION__FIELD_NAME: WrapperField = WrapperField("UseSingleSelection", FieldType.BOOLEAN)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_BatchRetrieval_field(self, value: Optional[bool]):
        """
        Set data field with field name 'BatchRetrieval' on this record model
        """
        self.set_field_value(self.BATCHRETRIEVAL__FIELD_NAME.field_name, value)

    def get_BatchRetrieval_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'BatchRetrieval' from this record model
        """
        return self.get_field_value(self.BATCHRETRIEVAL__FIELD_NAME.field_name)

    def set_DataType_field(self, value: Optional[str]):
        """
        Set data field with field name 'DataType' on this record model
        """
        self.set_field_value(self.DATATYPE__FIELD_NAME.field_name, value)

    def get_DataType_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DataType' from this record model
        """
        return self.get_field_value(self.DATATYPE__FIELD_NAME.field_name)

    def set_DoubleClickActionPluginPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'DoubleClickActionPluginPath' on this record model
        """
        self.set_field_value(self.DOUBLECLICKACTIONPLUGINPATH__FIELD_NAME.field_name, value)

    def get_DoubleClickActionPluginPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DoubleClickActionPluginPath' from this record model
        """
        return self.get_field_value(self.DOUBLECLICKACTIONPLUGINPATH__FIELD_NAME.field_name)

    def set_IsReportBacked_field(self, value: Optional[bool]):
        """
        Set data field with field name 'IsReportBacked' on this record model
        """
        self.set_field_value(self.ISREPORTBACKED__FIELD_NAME.field_name, value)

    def get_IsReportBacked_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'IsReportBacked' from this record model
        """
        return self.get_field_value(self.ISREPORTBACKED__FIELD_NAME.field_name)

    def set_ItemQueuePackagePath_field(self, value: Optional[str]):
        """
        Set data field with field name 'ItemQueuePackagePath' on this record model
        """
        self.set_field_value(self.ITEMQUEUEPACKAGEPATH__FIELD_NAME.field_name, value)

    def get_ItemQueuePackagePath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'ItemQueuePackagePath' from this record model
        """
        return self.get_field_value(self.ITEMQUEUEPACKAGEPATH__FIELD_NAME.field_name)

    def set_ShowDefaultButtons_field(self, value: Optional[bool]):
        """
        Set data field with field name 'ShowDefaultButtons' on this record model
        """
        self.set_field_value(self.SHOWDEFAULTBUTTONS__FIELD_NAME.field_name, value)

    def get_ShowDefaultButtons_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'ShowDefaultButtons' from this record model
        """
        return self.get_field_value(self.SHOWDEFAULTBUTTONS__FIELD_NAME.field_name)

    def set_UseSingleSelection_field(self, value: Optional[bool]):
        """
        Set data field with field name 'UseSingleSelection' on this record model
        """
        self.set_field_value(self.USESINGLESELECTION__FIELD_NAME.field_name, value)

    def get_UseSingleSelection_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'UseSingleSelection' from this record model
        """
        return self.get_field_value(self.USESINGLESELECTION__FIELD_NAME.field_name)


class WorkQueueTabConfigurationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type WorkQueueTabConfiguration
    Data Type Display Name: Work Queue Tab Configuration (Work Queue Tab Configurations)
    Fields: HidePlateView, HideStorageView, HideTab, TabDisplayName, TabName, TabPluralDisplayName
    """
    DATA_TYPE_NAME: str = 'WorkQueueTabConfiguration'
    HIDEPLATEVIEW__FIELD_NAME: WrapperField = WrapperField("HidePlateView", FieldType.BOOLEAN)
    HIDESTORAGEVIEW__FIELD_NAME: WrapperField = WrapperField("HideStorageView", FieldType.BOOLEAN)
    HIDETAB__FIELD_NAME: WrapperField = WrapperField("HideTab", FieldType.BOOLEAN)
    TABDISPLAYNAME__FIELD_NAME: WrapperField = WrapperField("TabDisplayName", FieldType.STRING)
    TABNAME__FIELD_NAME: WrapperField = WrapperField("TabName", FieldType.STRING)
    TABPLURALDISPLAYNAME__FIELD_NAME: WrapperField = WrapperField("TabPluralDisplayName", FieldType.STRING)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_HidePlateView_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HidePlateView' on this record model
        """
        self.set_field_value(self.HIDEPLATEVIEW__FIELD_NAME.field_name, value)

    def get_HidePlateView_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HidePlateView' from this record model
        """
        return self.get_field_value(self.HIDEPLATEVIEW__FIELD_NAME.field_name)

    def set_HideStorageView_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HideStorageView' on this record model
        """
        self.set_field_value(self.HIDESTORAGEVIEW__FIELD_NAME.field_name, value)

    def get_HideStorageView_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HideStorageView' from this record model
        """
        return self.get_field_value(self.HIDESTORAGEVIEW__FIELD_NAME.field_name)

    def set_HideTab_field(self, value: Optional[bool]):
        """
        Set data field with field name 'HideTab' on this record model
        """
        self.set_field_value(self.HIDETAB__FIELD_NAME.field_name, value)

    def get_HideTab_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'HideTab' from this record model
        """
        return self.get_field_value(self.HIDETAB__FIELD_NAME.field_name)

    def set_TabDisplayName_field(self, value: Optional[str]):
        """
        Set data field with field name 'TabDisplayName' on this record model
        """
        self.set_field_value(self.TABDISPLAYNAME__FIELD_NAME.field_name, value)

    def get_TabDisplayName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TabDisplayName' from this record model
        """
        return self.get_field_value(self.TABDISPLAYNAME__FIELD_NAME.field_name)

    def set_TabName_field(self, value: Optional[str]):
        """
        Set data field with field name 'TabName' on this record model
        """
        self.set_field_value(self.TABNAME__FIELD_NAME.field_name, value)

    def get_TabName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TabName' from this record model
        """
        return self.get_field_value(self.TABNAME__FIELD_NAME.field_name)

    def set_TabPluralDisplayName_field(self, value: Optional[str]):
        """
        Set data field with field name 'TabPluralDisplayName' on this record model
        """
        self.set_field_value(self.TABPLURALDISPLAYNAME__FIELD_NAME.field_name, value)

    def get_TabPluralDisplayName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'TabPluralDisplayName' from this record model
        """
        return self.get_field_value(self.TABPLURALDISPLAYNAME__FIELD_NAME.field_name)


class WorkQueueTaskConfigurationModel(WrappedRecordModel):
    """
    Auto-Generated Record Model Wrapper for data type WorkQueueTaskConfiguration
    Data Type Display Name: Work Queue Category Configuration (Work Queue Category Configurations)
    Fields: AddManageBatchPluginPath, CategoryOrder, DefaultBatchButtonsToExclude, DisableDeleteBatchPrompt, UserGroupList, ViewUploadImageButton, WorkflowOrCategoryName
    """
    DATA_TYPE_NAME: str = 'WorkQueueTaskConfiguration'
    ADDMANAGEBATCHPLUGINPATH__FIELD_NAME: WrapperField = WrapperField("AddManageBatchPluginPath", FieldType.STRING)
    CATEGORYORDER__FIELD_NAME: WrapperField = WrapperField("CategoryOrder", FieldType.LONG)
    DEFAULTBATCHBUTTONSTOEXCLUDE__FIELD_NAME: WrapperField = WrapperField("DefaultBatchButtonsToExclude", FieldType.SELECTION)
    DISABLEDELETEBATCHPROMPT__FIELD_NAME: WrapperField = WrapperField("DisableDeleteBatchPrompt", FieldType.BOOLEAN)
    USERGROUPLIST__FIELD_NAME: WrapperField = WrapperField("UserGroupList", FieldType.SELECTION)
    VIEWUPLOADIMAGEBUTTON__FIELD_NAME: WrapperField = WrapperField("ViewUploadImageButton", FieldType.ACTION)
    WORKFLOWORCATEGORYNAME__FIELD_NAME: WrapperField = WrapperField("WorkflowOrCategoryName", FieldType.SELECTION)

    @classmethod
    def get_wrapper_data_type_name(cls):
        return cls.DATA_TYPE_NAME

    def set_AddManageBatchPluginPath_field(self, value: Optional[str]):
        """
        Set data field with field name 'AddManageBatchPluginPath' on this record model
        """
        self.set_field_value(self.ADDMANAGEBATCHPLUGINPATH__FIELD_NAME.field_name, value)

    def get_AddManageBatchPluginPath_field(self) -> Optional[str]:
        """
        Get data field value with field name 'AddManageBatchPluginPath' from this record model
        """
        return self.get_field_value(self.ADDMANAGEBATCHPLUGINPATH__FIELD_NAME.field_name)

    def set_CategoryOrder_field(self, value: Optional[int]):
        """
        Set data field with field name 'CategoryOrder' on this record model
        """
        self.set_field_value(self.CATEGORYORDER__FIELD_NAME.field_name, value)

    def get_CategoryOrder_field(self) -> Optional[int]:
        """
        Get data field value with field name 'CategoryOrder' from this record model
        """
        return self.get_field_value(self.CATEGORYORDER__FIELD_NAME.field_name)

    def set_DefaultBatchButtonsToExclude_field(self, value: Optional[str]):
        """
        Set data field with field name 'DefaultBatchButtonsToExclude' on this record model
        """
        self.set_field_value(self.DEFAULTBATCHBUTTONSTOEXCLUDE__FIELD_NAME.field_name, value)

    def get_DefaultBatchButtonsToExclude_field(self) -> Optional[str]:
        """
        Get data field value with field name 'DefaultBatchButtonsToExclude' from this record model
        """
        return self.get_field_value(self.DEFAULTBATCHBUTTONSTOEXCLUDE__FIELD_NAME.field_name)

    def set_DisableDeleteBatchPrompt_field(self, value: Optional[bool]):
        """
        Set data field with field name 'DisableDeleteBatchPrompt' on this record model
        """
        self.set_field_value(self.DISABLEDELETEBATCHPROMPT__FIELD_NAME.field_name, value)

    def get_DisableDeleteBatchPrompt_field(self) -> Optional[bool]:
        """
        Get data field value with field name 'DisableDeleteBatchPrompt' from this record model
        """
        return self.get_field_value(self.DISABLEDELETEBATCHPROMPT__FIELD_NAME.field_name)

    def set_UserGroupList_field(self, value: Optional[str]):
        """
        Set data field with field name 'UserGroupList' on this record model
        """
        self.set_field_value(self.USERGROUPLIST__FIELD_NAME.field_name, value)

    def get_UserGroupList_field(self) -> Optional[str]:
        """
        Get data field value with field name 'UserGroupList' from this record model
        """
        return self.get_field_value(self.USERGROUPLIST__FIELD_NAME.field_name)

    def set_WorkflowOrCategoryName_field(self, value: Optional[str]):
        """
        Set data field with field name 'WorkflowOrCategoryName' on this record model
        """
        self.set_field_value(self.WORKFLOWORCATEGORYNAME__FIELD_NAME.field_name, value)

    def get_WorkflowOrCategoryName_field(self) -> Optional[str]:
        """
        Get data field value with field name 'WorkflowOrCategoryName' from this record model
        """
        return self.get_field_value(self.WORKFLOWORCATEGORYNAME__FIELD_NAME.field_name)


