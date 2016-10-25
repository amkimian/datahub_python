# DataElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of this data element | [optional] 
**dataset** | **str** | The data set this element relates to | [optional] 
**owner** | **str** | The user this element relates to | [optional] 
**release** | **str** | The release this element relates to | [optional] 
**mime_type** | **str** | The mime type of the data element | [optional] 
**description** | **str** | Some information about this element | [optional] 
**type** | **str** | The underlying data type of this element | [optional] 
**schema** | **str** | The underlying format of the data | [optional] 
**state** | **str** | The state of this element (is it published?) | [optional] 
**storage** | **str** | Where blocks are stored for this element | [optional] 
**content** | **str** | If the type is text, this is the text | [optional] 
**block_id** | **int** | If the type is csv, this is the next block when added | [optional] 
**key_field** | **str** | If the type is keyed, this is the key field that represents the unique key | [optional] 
**display_info** | [**DataElementDisplayInfo**](DataElementDisplayInfo.md) |  | [optional] 
**csv_info** | [**DataElementCsvInfo**](DataElementCsvInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


